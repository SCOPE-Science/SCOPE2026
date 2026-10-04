# Pell rigidity at the five-term boundary for equal proper-divisor sums

## Finding
Let
\[
s(n)=\sigma(n)-n
\]
be the sum of the proper divisors of the positive integer \(n\).

Suppose
\[
s(N)=s(N+1)=s(N+2)=s(N+3)=s(N+4)=S.
\]
Then \(S\) is odd and \(N\) is odd. The two even terms \(N+1\) and \(N+3\) must be of opposite parity types in the classical criterion for odd divisor sums: one is a square and the other is twice a square.

More precisely, every five-term constant run belongs to exactly one of the following two families.

In the first family,
\[
N+1=a^2,\qquad N+3=2b^2,
\]
so
\[
a^2-2b^2=-2,
\]
and the positive solutions are
\[
a+b\sqrt2=\sqrt2(3+2\sqrt2)^t,\qquad t\ge1.
\]
Equality of the two proper-divisor sums forces
\[
\sigma(a^2)+2=3\sigma(b^2).
\]

In the second family,
\[
N+1=2a^2,\qquad N+3=b^2,
\]
so
\[
b^2-2a^2=2,
\]
and the positive solutions are
\[
b+a\sqrt2=(2+\sqrt2)(3+2\sqrt2)^t,\qquad t\ge0.
\]
Equality of the two proper-divisor sums forces
\[
3\sigma(a^2)+2=\sigma(b^2).
\]

Consequently, the set of possible starting points \(N\le X\) for a five-term constant run has size
\[
O(\log X).
\]

An exact replay of the two Pell families through the threshold
\[
N<10^{38}
\]
produces exactly \(50\) candidate even pairs. Deterministic factorization of every Pell coordinate and exact evaluation of the required divisor sums rejects all \(50\). Therefore there is no positive integer
\[
N<10^{38}
\]
for which
\[
s(N)=s(N+1)=s(N+2)=s(N+3)=s(N+4).
\]

## Assumptions and scope
The function \(s(n)\) is the ordinary sum of proper positive divisors. All integers in the theorem are positive.

The structural reduction is unconditional and global. The numerical cutoff \(10^{38}\) is a finite theorem obtained only after the global reduction: it is not a brute-force scan through all integers below the cutoff.

The result does not prove that five-term constant runs are impossible for every \(N\). Beyond the verified cutoff, a run would still have to satisfy one of the two displayed Pell equations together with its corresponding divisor-sum identity.

## Proof
We use the classical parity criterion
\[
\sigma(m)\ \text{is odd}
\quad\Longleftrightarrow\quad
m=u^2\ \text{or}\ m=2u^2.
\]
This criterion is also the lemma used in the published proof that six consecutive equal proper-divisor sums are impossible.

Assume that
\[
s(N)=s(N+1)=\cdots=s(N+4)=S.
\]

First suppose that \(S\) is even. Every odd integer \(m\) in the block then satisfies
\[
\sigma(m)=m+S,
\]
which is odd. Because \(m\) itself is odd, the parity criterion forces \(m\) to be a square. Any block of five consecutive integers contains at least two odd terms whose difference is \(2\). Two positive squares cannot differ by \(2\). Hence \(S\) cannot be even, so \(S\) is odd.

Now every even integer \(m\) in the block has
\[
\sigma(m)=m+S
\]
odd. Thus each even term is either a square or twice a square.

If \(N\) were even, the three terms
\[
N,\quad N+2,\quad N+4
\]
would all be even and hence each would be a square or twice a square. Two of the three would have the same type. Two positive squares cannot differ by \(2\) or \(4\), and two positive twice-squares cannot differ by \(2\) or \(4\), since after division by \(2\) this would require two positive squares to differ by \(1\) or \(2\). Therefore \(N\) is odd.

The only even terms are now \(N+1\) and \(N+3\). They differ by \(2\), so they cannot have the same type. There are two cases.

If
\[
N+1=a^2,\qquad N+3=2b^2,
\]
then
\[
a^2-2b^2=-2.
\]
Here \(a\) is even and \(b\) is odd. Because \(b\) is odd,
\[
\sigma(2b^2)=3\sigma(b^2).
\]
The equality
\[
s(a^2)=s(2b^2)
\]
becomes
\[
\sigma(a^2)-a^2=3\sigma(b^2)-2b^2.
\]
Using \(a^2=2b^2-2\) gives
\[
\sigma(a^2)+2=3\sigma(b^2).
\]

If
\[
N+1=2a^2,\qquad N+3=b^2,
\]
then
\[
b^2-2a^2=2.
\]
Here \(a\) is odd and \(b\) is even, so
\[
\sigma(2a^2)=3\sigma(a^2).
\]
The equality
\[
s(2a^2)=s(b^2)
\]
reduces to
\[
3\sigma(a^2)+2=\sigma(b^2).
\]

It remains to parameterize the Pell equations. The positive solutions of
\[
a^2-2b^2=-2
\]
with \(a>0\) are generated from \(4+3\sqrt2\) by multiplication by the fundamental positive unit
\[
3+2\sqrt2,
\]
giving
\[
a+b\sqrt2=\sqrt2(3+2\sqrt2)^t,\qquad t\ge1.
\]
Likewise the positive solutions of
\[
b^2-2a^2=2
\]
are
\[
b+a\sqrt2=(2+\sqrt2)(3+2\sqrt2)^t,\qquad t\ge0.
\]
For completeness, these descriptions can be obtained by descent with the inverse unit \(3-2\sqrt2\): every nonminimal positive solution descends to the indicated seed, and multiplication by \(3+2\sqrt2\) recovers all larger solutions.

Each Pell coordinate grows geometrically like \((3+2\sqrt2)^t\), while the candidate integer \(N+1\) is quadratic in a coordinate. Thus each family contributes only \(O(\log X)\) candidates with \(N\le X\).

For the explicit cutoff, the accompanying verifier generates both families until \(N+1>10^{38}\). There are \(25\) candidates from each family. Every coordinate used in these \(50\) candidates is smaller than \(2^{64}\). The verifier therefore factors each coordinate with a deterministic Miller--Rabin primality test valid on the full \(64\)-bit range together with exact Pollard--Rho splitting, checks that the factors multiply back to the original coordinate, and evaluates
\[
\sigma(a^2)
\]
and
\[
\sigma(b^2)
\]
from those certified factorizations. None of the \(50\) candidates satisfies its required divisor-sum identity. Hence no five-term constant run starts below \(10^{38}\).

## Verification
Run
`python3 verify.py`.

The program regenerates both Pell families from their seeds, checks the Pell equations and parity conditions, verifies that there are exactly \(25+25=50\) candidates with \(N<10^{38}\), and confirms that the next candidate in each family lies beyond the cutoff.

Every Pell coordinate occurring below the cutoff is below \(2^{64}\). The factorization routine uses the standard deterministic Miller--Rabin base set for \(64\)-bit integers, followed by exact Pollard--Rho splitting. After factorization, every prime factor is rechecked and the product is reconstructed exactly.

The file `pell_candidates.csv` records every candidate and the exact nonzero residual in the required divisor-sum identity. The program regenerates this table and checks it byte-for-byte.

A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Lebowitz-Lockard and Vandehey prove that six consecutive integers cannot have the same sum of proper divisors. Their proof uses the same classical parity characterization of odd values of \(\sigma\): in a six-term block, three even terms force two of the same square/twice-square type and hence a contradiction.

The five-term boundary is different. Once the block starts at an odd integer, only two even terms remain, and they can have opposite types. The published six-term argument therefore does not rule out a five-term run. The present theorem identifies the exact residual structure: the two even terms must form one of two Pell families and satisfy an additional divisor-sum identity. This makes the possible starting set logarithmically sparse and yields the exact \(10^{38}\) exclusion.

The MathOverflow question on adjacent equal proper-divisor sums records the basic observation that any equal adjacent pair must involve a square or twice a square. It does not derive the five-term Pell reduction or either divisor-sum identity.

OEIS A001065 is the canonical table of the proper-divisor-sum function. Its inspected entry does not contain a five-term constant-run classification or the Pell reduction.

Targeted searches for five consecutive equal proper-divisor sums, the two Pell equations in this context, and the exact divisor-sum identities did not locate a source stating or implying the theorem.

## Limitations
The global result is a necessary-condition theorem, not a proof that five-term constant runs never exist. The exact finite exclusion ends at \(N<10^{38}\).

The Pell reduction uses only the two even terms of a hypothetical five-term block. A future global nonexistence proof would still need to rule out the two divisor-sum identities on every Pell solution, or use additional information from the three odd terms.

The deterministic computation is exhaustive only after the symbolic Pell reduction. It is not an enumeration of all integers below \(10^{38}\).

## References
1. Noah Lebowitz-Lockard and Joseph Vandehey, “Arithmetic Functions that Remain Constant on Runs of Consecutive Integers,” Journal of Integer Sequences 26 (2023), Article 23.8.4. Primary MSC \(11A25\). Published 3 October 2023.
2. OEIS A001065, “Sum of proper divisors (or aliquot parts) of \(n\).”
3. Alan Frank, “Are there pairs of consecutive integers with the same sum of factors?”, MathOverflow question 14459.
