"""Exact finite-word checks for a threshold observation of the logistic map.

Only standard-library rational arithmetic is used. Finite checks supplement,
but do not substitute for, the analytical infinite-length proof.
"""
from fractions import Fraction as F
from itertools import product

P = ((F(1,2),F(1,2),F(0)),
     (F(0),F(0),F(1)),
     (F(1,2),F(1,2),F(0)))
output = (0,1,1)
pi = (F(1,3), F(1,3), F(1,3))


def hidden_word_probability(w):
    row = [pi[i] if output[i]==w[0] else F(0) for i in range(3)]
    for symbol in w[1:]:
        row = [sum(row[i]*P[i][j] for i in range(3))
               if output[j]==symbol else F(0) for j in range(3)]
    return sum(row)


def direct_counts(n):
    # Markov endpoints are at integer multiples of 1/6; the n-letter
    # partition is refined by an exact grid of mesh 1/(6*2**(n-1)).
    D = 6 * 2**(n-1)
    modulus = 2*D
    counts = {}
    for k in range(D):
        residue = 2*k + 1  # midpoint with denominator 2D
        bits = []
        for _ in range(n):
            bits.append(int(D < 3*residue < 5*D))
            residue = (2*residue) % modulus
        word = tuple(bits)
        counts[word] = counts.get(word, 0) + 1
    return {w:F(c,D) for w,c in counts.items()}


def check(nmax=11):
    trials=0
    for n in range(1,nmax+1):
        direct=direct_counts(n)
        assert sum(direct.values()) == 1
        for word in product((0,1), repeat=n):
            prob=hidden_word_probability(word)
            assert prob == direct.get(word,F(0)), (n,word,prob,direct.get(word))
            trials += 1
        ones=hidden_word_probability((1,)*n)
        predicted=(F(2,3)*F(1,2)**((n-1)//2)
                   if n%2 else F(1,2)**(n//2))
        assert ones==predicted,(n,ones,predicted)
        zeros=hidden_word_probability((0,)*n)
        assert zeros==F(1,3)*F(1,2)**(n-1)
    mean=F(2,3)
    for n in range(0,14):
        row = [pi[i]*output[i] for i in range(3)]
        for _ in range(n):
            row = [sum(row[i]*P[i][j] for i in range(3)) for j in range(3)]
        covariance=sum(row[i]*output[i] for i in range(3))-mean**2
        expected=(F(2,9) if n==0 else F((-1)**(n+1),9*2**n))
        assert covariance==expected,(n,covariance,expected)
    # Characteristic polynomial of tilted kernel has coefficients
    # (1, -1/2, -exp(2t)/2, 0), verified for several exact weights.
    for z in (F(1,2),F(1),F(2),F(7)):
        M=[[P[i][j]*(z if output[i] else 1) for j in range(3)] for i in range(3)]
        trace=sum(M[i][i] for i in range(3))
        minors=sum(M[i][i]*M[j][j]-M[i][j]*M[j][i]
                   for i in range(3) for j in range(i+1,3))
        det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
        assert (trace,minors,det)==(F(1,2),-z*z/2,F(0))
    print(f'VERIFY_OK {trials} exact word comparisons; 14 covariance checks; 4 tilted-kernel checks')

if __name__=='__main__':
    check()
