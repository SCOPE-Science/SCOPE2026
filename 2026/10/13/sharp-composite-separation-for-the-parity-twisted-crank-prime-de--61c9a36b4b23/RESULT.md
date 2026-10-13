# Sharp composite separation for the parity-twisted crank prime detector

## Finding
Let \\(F_{2k}(n)=2^{2k}\\sigma_{2k-1}(n/2)-\\sigma_{2k-1}(n)\\), where \\(\\sigma_r(x)=0\\) when \\(x\\) is not a positive integer, and define Kang's prime-detecting coefficient by
\[
h(n)=2F_6(n)-2(n^2-n+3)F_4(n)+2(-n^3+4n^2-3n+2)F_2(n).
\]
For every composite integer \\(n\\ge2\\),
\[
|h(n)|\\ge120,
\]
and equality holds if and only if \\(n=4\\). The three residue classes admit sharper exact boundary statements:
\[
\\begin{aligned}
n\\text{ odd composite}&\\implies h(n)\\ge6144, &&\\text{equality iff }n=9,\\\\
n\\equiv2\\pmod4\\text{ composite}&\\implies h(n)\\ge1488, &&\\text{equality iff }n=6,\\\\
4\\mid n&\\implies h(n)\\le-120, &&\\text{equality iff }n=4.
\\end{aligned}
\]
Thus the coefficient detector has a sharp nonzero composite separation margin of \\(120\\).

## Assumptions and scope
The definition is the coefficient form of the parity-twisted crank prime detector in Kang's 2026 preprint. The source proves that \\(h(n)=0\\) exactly for primes \\(n\\ge2\\), with positive sign on composite \\(n\\) not divisible by \\(4\\) and negative sign on multiples of \\(4\\). The present statement is a quantitative sharpening for this same normalized coefficient sequence; no rescaling of \\(h\\) is allowed.

The proof uses only exact divisor-sum identities from the source and elementary inequalities. Finite computation is used solely to replay the normalization and stress-test the theorem, not to infer any infinite case.

## Proof
For odd \\(n\\), direct rearrangement of the source's divisor-sum formulas gives
\[
h(n)=(n-2)u(n)+z(n),
\]
with
\[
u(n)=2\\sum_{d\\mid n}d(d^2-1)\\left((n/d)^2-1\\right),
\qquad
z(n)=2\\sum_{d\\mid n}d(d^2-1)(n^2-d^2).
\]
Let \\(n\\) be odd composite, let \\(p\\) be its least prime divisor, and write \\(n=pq\\). Then \\(p,q\\ge3\\). Keeping only the divisor \\(d=p\\) in the two nonnegative sums yields
\[
h(n)\\ge2p(p^2-1)(q^2-1)(p^2+pq-2).
\]
The right side is strictly increasing in each variable for \\(p,q\\ge3\\), so it is at least its value at \\(p=q=3\\), namely \\(6144\\). Equality is possible only for \\(n=9\\), and substitution gives \\(h(9)=6144\\).

Now let \\(n=2m\\), where \\(m\\ge3\\) is odd. Expanding the source formula gives
\[
h(2m)=62\\sigma_5(m)-14(4m^2-2m+3)\\sigma_3(m)-4(4m^3-8m^2+3m-1)\\sigma_1(m).
\]
For odd \\(m\\),
\[
\\sigma_5(m)\\ge m^5,
\qquad
\\sigma_3(m)\\le\\frac{16}{15}m^3,
\qquad
\\sigma_1(m)\\le m\\left(1+\\frac12\\log m\\right).
\]
The middle inequality is weaker than the explicit odd-divisor bound used in the source. For the last inequality, use \\(\\sigma_1(m)/m=\\sum_{d\\mid m}1/d\\) and dominate the odd reciprocal divisors by \\(1+\\sum_{j=1}^{(m-1)/2}(2j+1)^{-1}\\le1+\\tfrac12\\log m\\). Hence \\(h(2m)\\ge L(m)\\), where
\[
L(x)=\\frac{34}{15}x^5+\\frac{208}{15}x^4-\\frac{64}{5}x^3-12x^2+4x+(-8x^4+16x^3-6x^2+2x)\\log x.
\]
For \\(x\\ge5\\), \\(\\log x\\le x/3\\). Differentiation gives
\[
\\frac{15}{2}L'(x)=85x^4-240x^3\\log x+356x^3+360x^2\\log x-168x^2-90x\\log x-225x+15\\log x+45.
\]
Bounding only the negative logarithmic terms by \\(\\log x\\le x/3\\) and dropping the positive logarithmic terms gives
\[
\\frac{15}{2}L'(x)\\ge5x^4+356x^3-198x^2-225x+45>0
\]
for \\(x\\ge5\\). Moreover
\[
L(5)=13870-3140\\log5>\\frac{25910}{3}>1488.
\]
Thus \\(h(2m)>1488\\) for every odd \\(m\\ge5\\). The remaining case \\(m=3\\) gives \\(h(6)=1488\\), proving the second sharp bound.

Finally write \\(n=tm\\), with \\(t=2^a\\ge4\\) and \\(m\\) odd. Put
\[
A_1(t)=2t-3,
\quad
A_3(t)=\\frac{8t^3-15}{7},
\quad
A_5(t)=\\frac{32t^5-63}{31}.
\]
The source's exact formulas imply
\[
\\frac{z(n)}2\\le\\bigl(m^2K(t)-A_3(t)\\bigr)\\sigma_3(m),
\]
where
\[
K(t)=-\\frac{24}{217}t^5+2t^3-\\frac67t^2-\\frac{63}{31}.
\]
Here \\(K(4)=-1\\), while for \\(t\\ge8\\),
\[
K(t)=t^3\\left(2-\\frac{24t^2}{217}\\right)-\\frac67t^2-\\frac{63}{31}<-1.
\]
Since \\(A_3(t)\\ge A_3(4)=71\\), it follows that \\(z(n)\\le-144\\). Also
\[
\\frac{u(n)}2=A_3(t)\\sigma_3(m)-(t^2m^2-tm+1)A_1(t)\\sigma_1(m).
\]
Using \\(\\sigma_3(m)\\le m^2\\sigma_1(m)\\), the bracket controlling \\(u(n)\\) is negative for \\(t=4,m\\ge3\\); for \\(t\\ge8\\), the inequality \\(t^2A_1(t)-A_3(t)\\ge tA_1(t)\\) makes it negative for every \\(m\\ge1\\). Therefore \\(u(n)<0\\) except at the separately evaluated case \\(n=4\\). At \\(n=4\\), the exact values are \\(u(4)=12\\), \\(z(4)=-144\\), hence \\(h(4)=-120\\). For every other multiple of \\(4\\), \\(h(n)=(n-2)u(n)+z(n)<-144\\). This proves the third bound and the global equality statement.

## Verification
The bundled checker reconstructs \\(h(n)\\) directly from the divisor-sum coefficient formula, verifies \\(h(4)=-120\\), \\(h(6)=1488\\), and \\(h(9)=6144\\), and checks the three residue-class inequalities for every \\(2\\le n\\le20000\\). It also checks the source normalization \\(h(p)=0\\) for every prime in that range. The replay is a finite consistency check only; the proof above establishes the infinite statement.

## Relationship to prior work
Kang proves the zero-set and sign classification for this coefficient sequence and records the exceptional direct calculation at \\(n=4\\). The quantitative lower bounds \\(6144\\) and \\(1488\\), the unique equality cases \\(9\\) and \\(6\\), and the resulting exact global composite separation \\(120\\) are not stated in the inspected theorem or its proof. Craig, van Ittersum, and Ono previously constructed partition-theoretic prime-detecting equations, providing broader motivation for quantitative robustness of such detectors, but their expressions are different and do not imply these constants for Kang's \\(h(n)\\).

## Limitations
The result is tied to Kang's normalization of \\(h(n)\\); multiplying the detector by a scalar changes the numerical margin. It does not claim an optimal margin among all prime-detecting elements of the algebra, nor a stability theorem under arbitrary perturbations of the defining coefficients. The finite verifier is not an exhaustiveness argument and is not used to prove the bounds beyond its checked range.

## References
1. Soon-Yi Kang, “The Algebra of Parity-Twisted Crank Moments and a Prime-Detecting Expression,” arXiv:2609.37301v1, 29 September 2026. See Theorem 2.3 and Section 5.
2. William Craig, Jan-Willem van Ittersum, and Ken Ono, “Integer partitions detect the primes,” Proceedings of the National Academy of Sciences 121 (2024), e2409417121; arXiv:2405.06451.
