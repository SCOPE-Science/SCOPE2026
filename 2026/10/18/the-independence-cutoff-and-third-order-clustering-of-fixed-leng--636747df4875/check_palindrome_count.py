"""Independent finite checks for palindrome-count dependence statements.

Requires Python 3 standard library only. Fully enumerates short words and
all finite offsets needed for the four- and five-letter third cumulants.
"""
from fractions import Fraction
from itertools import product, combinations
from math import comb

checks = 0

def verify(statement):
    global checks
    checks += 1
    if not statement:
        raise AssertionError('check %d failed' % checks)

def palindrome(word, start, k):
    return word[start:start+k] == tuple(reversed(word[start:start+k]))

def joint_rank(k, starts):
    if not starts:
        return 0
    size=max(starts)+k
    parent=list(range(size))
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for a in starts:
        for j in range(k//2):
            parent[root(a+j)]=root(a+k-1-j)
    return size-len({root(x) for x in range(size)})

def third_cumulant_of_counts(counts):
    N=len(counts)
    a=Fraction(sum(counts),N)
    b=Fraction(sum(x*x for x in counts),N)
    c=Fraction(sum(x*x*x for x in counts),N)
    return c-3*a*b+2*a**3

# Pairwise joint probabilities and triple adjacent probabilities from equality graphs.
for k in range(2,19):
    r=k//2
    for d in range(1,2*k+3):
        verify(joint_rank(k,(0,d)) == 2*r)
    verify(joint_rank(k,(0,1,2))==2*r+1)

# Full exhaustive small-word tests, without presuming independence.
for q,largest in ((2,12),(3,8)):
    for N in range(2,largest+1):
        for k in range(2,N+1):
            M=N-k+1
            r=k//2
            p=Fraction(1,q**r)
            observations=[tuple(int(palindrome(word,i,k)) for i in range(M))
                          for word in product(range(q), repeat=N)]
            count=[sum(v) for v in observations]
            verify(Fraction(sum(count),len(count))==M*p)
            expected_var=M*p*(1-p)
            mean=M*p
            verify(Fraction(sum((s-mean)**2 for s in count),len(count))==expected_var)
            for a,b in combinations(range(M),2):
                verify(Fraction(sum(v[a]*v[b] for v in observations),len(observations))==p*p)
            if M>=3:
                observed=Fraction(sum(v[0]*v[1]*v[2] for v in observations),len(observations))
                verify(observed==Fraction(1,q**(2*r+1)))
            actual_kappa=third_cumulant_of_counts(count)
            nominal=M*p*(1-p)*(1-2*p)
            if k<=3 or M<=2:
                verify(actual_kappa==nominal)
            else:
                verify(actual_kappa>nominal)
            if k in (4,5):
                expected=nominal+6*max(M-2,0)*p**3*(q-1)
                verify(actual_kappa==expected)

# Exhaustively verify that for lengths four and five the sole dependent
# triple of positions has consecutive starting indices.
for k in (4,5):
    r=k//2
    exceptions=[]
    for a in range(1,2*k-1):
        for b in range(a+1,2*k-1):
            defect=3*r-joint_rank(k,(0,a,b))
            verify(defect>=0)
            if defect: exceptions.append((a,b,defect))
    verify(exceptions==[(1,2,1)])

# Exact nonuniform boundary-overlap covariance: specific windows sharing a
# single endpoint; equality holds precisely for uniform positive masses.
for masses in ((Fraction(1,2),Fraction(1,3),Fraction(1,6)),
               (Fraction(1,4),)*4,
               (Fraction(1,3),Fraction(2,3))):
    a=sum(x*x for x in masses)
    b=sum(x*x*x for x in masses)
    for k in range(2,12):
        r=k//2
        expected=a**(2*r-2)*(b-a*a)
        by_patterns=Fraction(0)
        for word in product(range(len(masses)),repeat=2*k-1) if k<=5 else ():
            if palindrome(word,0,k) and palindrome(word,k-1,k):
                prob=Fraction(1)
                for symbol in word: prob*=masses[symbol]
                by_patterns+=prob
        if k<=5: verify(by_patterns-a**(2*r)==expected)
        verify((expected==0)==(len(set(masses))==1))


# All specified joint occurrences are governed by the mirror-constraint graph.
for q,largest in ((2,9),(3,7)):
    for N in range(2,largest+1):
        for k in range(2,N+1):
            m=N-k+1
            words=list(product(range(q),repeat=N))
            for h in range(m+1):
                for selected in combinations(range(m),h):
                    count=sum(all(palindrome(w,i,k) for i in selected) for w in words)
                    verify(Fraction(count,len(words))==Fraction(1,q**joint_rank(k,selected)))

print('PASS', checks, 'exact assertions')
