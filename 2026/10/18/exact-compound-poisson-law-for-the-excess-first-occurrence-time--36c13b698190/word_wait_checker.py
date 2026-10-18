"""Exact-rational finite tests for a word-waiting-time determinant identity.

No external dependencies. Universal assertions in the accompanying theorem are
proved mathematically, not by these bounded computations.
"""
from fractions import Fraction as Q
from itertools import product


def mat_mul(a, b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def prefix_matrix(word, probabilities):
    n=len(word)
    A=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        history=word[:i]
        for letter, prob in probabilities.items():
            after=history+(letter,)
            if after[-n:]==word:
                assert i==n-1 and letter==word[-1]
                continue
            j=max(j for j in range(n) if j==0 or after[-j:]==word[:j])
            assert j<=i+1
            A[i][j]+=prob
    return A


def determinant_coefficients(A):
    n=len(A)
    P=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    traces=[]
    for _ in range(n):
        P=mat_mul(P,A)
        traces.append(sum(P[i][i] for i in range(n)))
    d=[Q(1)]
    for k in range(1,n+1):
        d.append(-sum(d[k-i]*traces[i-1] for i in range(1,k+1))/k)
    return d,traces


def first_occurrence_masses(word, probs, extra):
    A=prefix_matrix(word,probs)
    n=len(word)
    dist=[Q(0) for _ in range(n)];dist[0]=Q(1)
    masses=[]
    for step in range(1,n+extra+1):
        masses.append(dist[n-1]*probs[word[-1]])
        new=[Q(0) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new[j]+=dist[i]*A[i][j]
        dist=new
    assert masses[:n-1]==[Q(0)]*(n-1)
    return masses[n-1:]


def test(word,probs):
    A=prefix_matrix(word,probs)
    d,traces=determinant_coefficients(A)
    p=Q(1)
    for w in word:p*=probs[w]
    assert sum(d)==p,('det at one',word,probs)
    assert all(t>=0 for t in traces),('trace',word)
    extra=15
    h=first_occurrence_masses(word,probs,extra)
    assert h[0]==p
    for n in range(extra+1):
        lhs=sum(d[j]*h[n-j] for j in range(min(len(d)-1,n)+1))
        assert lhs==(p if n==0 else 0),('PGF',word,probs,n)
    # Exact check of the first 15 Levy masses computed from traces.
    power=[[Q(int(i==j)) for j in range(len(A))] for i in range(len(A))]
    for k in range(1,extra+1):
        power=mat_mul(power,A)
        tr=sum(power[i][i] for i in range(len(A)))
        assert tr>=0
    return extra+1



def brute_hit_probability(word, probabilities, length):
    """Enumerate independent strings without using the prefix automaton."""
    hit=Q(0)
    symbols=tuple(probabilities)
    m=len(word)
    for s in product(symbols, repeat=length):
        if s[-m:]!=word or any(s[i-m+1:i+1]==word for i in range(m-1,length-1)):
            continue
        prob=Q(1)
        for c in s:prob*=probabilities[c]
        hit+=prob
    return hit


def main():
    tested=0; eqs=0
    families=[({'A':Q(2,5),'B':Q(3,5)},6),
              ({'A':Q(1,7),'B':Q(6,7)},6),
              ({'A':Q(1,2),'B':Q(1,2)},6),
              ({'A':Q(1,2),'B':Q(1,3),'C':Q(1,6)},4)]
    for probs,maxlen in families:
        for m in range(1,maxlen+1):
            for word in product(tuple(probs),repeat=m):
                eqs+=test(word,probs);tested+=1
    independent_checks=0
    for probabilities, maxlen, extension in [({'A':Q(2,5),'B':Q(3,5)},5,3),
                                             ({'A':Q(1,2),'B':Q(1,3),'C':Q(1,6)},3,2)]:
        for m in range(1,maxlen+1):
            for word in product(tuple(probabilities),repeat=m):
                hits=first_occurrence_masses(word, probabilities,extension)
                for extra in range(extension+1):
                    assert hits[extra]==brute_hit_probability(word, probabilities,m+extra)
                    independent_checks+=1
    print('PASS: %d words; %d exact coefficient identities; %d nonnegative trace checks; %d brute enumerations.'%(tested,eqs,tested*15,independent_checks))
    # Nontrivial overlap example HTH: display exact rational Levy masses.
    prob={'H':Q(2,5),'T':Q(3,5)}
    A=prefix_matrix(('H','T','H'),prob)
    X=[[Q(int(i==j)) for j in range(3)] for i in range(3)]
    vals=[]
    for k in range(1,7):
        X=mat_mul(X,A)
        vals.append(str(sum(X[i][i] for i in range(3))/k))
    print('HTH p(H)=2/5: Levy masses k=1..6:',', '.join(vals))


if __name__=='__main__':
    main()
