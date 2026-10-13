# Sharp parameter interval for the exceptional ordinary Dirichlet-inverse prime criterion
## Finding
Let \(\sigma_1(n)=\sum_{d\mid n}d\), let \(\sigma_1^{(-1)}\) be its Dirichlet inverse, and let \(\varphi\) and \(\mu\) denote Euler's totient and the Möbius function. For \(t\in\mathbb R\) and \(n\in\mathbb Z_{>0}\), define
\[
P_t(n)=\sigma_1^{(-1)}(n)+\varphi(n)+2+t(\mu(n)+1).
\]
Then, for every real \(t\) with
\[
-2<t<1,
\]
one has
\[
P_t(n)=0\quad\Longleftrightarrow\quad n\text{ is prime}.
\]
Both endpoints are sharp:
\[
P_{-2}(1)=0,\qquad P_1(18)=0.
\]
Therefore \((-2,1)\) is the maximal open interval containing \(t=0\) on which the zero set of \(P_t\) is exactly the primes.

## Assumptions and scope
The domain is all positive integers \(n\), and \(t\) is an arbitrary real number in the stated interval. Dirichlet inversion is convolution inversion, not pointwise reciprocal. No primality-testing speed claim is made.

The local inverse formula is
\[
\sigma_1^{(-1)}(p)=-(p+1),\qquad
\sigma_1^{(-1)}(p^2)=p,\qquad
\sigma_1^{(-1)}(p^e)=0\quad(e\ge3).
\]
It follows directly because the prime-local generating series of \(\sigma_1\) is \(1/((1-X)(1-pX))\), whose multiplicative inverse is \((1-X)(1-pX)\). The recent source independently records the same formula and the exhaustive squarefree / prime-cube / cube-free-nonsquarefree decomposition.

## Proof
For a prime \(p\),
\[
P_t(p)=-(p+1)+(p-1)+2+t(-1+1)=0,
\]
so every prime is a zero for every real \(t\). Also \(P_t(1)=4+2t\), which is positive on \((-2,1)\).

Suppose first that \(n=p_1\cdots p_r\) is squarefree and composite. If \(r\) is even, then \(\mu(n)=1\) and
\[
P_t(n)=\prod_{j=1}^r(p_j+1)+\prod_{j=1}^r(p_j-1)+2+2t>0
\]
for \(t>-2\). If \(r\) is odd, then \(r\ge3\) and the parameter term vanishes. Expanding the two products gives
\[
\prod_{j=1}^r(p_j+1)-\prod_{j=1}^r(p_j-1)
=2\!\sum_{\substack{S\subseteq\{1,\ldots,r\}\\r-|S|\text{ odd}}}\prod_{j\in S}p_j,
\]
a positive sum containing the term \(2\prod_{j=2}^r p_j\). Hence the difference is greater than \(2\), and
\[
P_t(n)=-\prod_{j=1}^r(p_j+1)+\prod_{j=1}^r(p_j-1)+2<0.
\]
Thus no squarefree composite is a zero.

If a prime cube divides \(n\), then \(\sigma_1^{(-1)}(n)=0\) and \(\mu(n)=0\). Therefore
\[
P_t(n)=\varphi(n)+2+t>0
\]
for \(t>-2\).

It remains to treat cube-free nonsquarefree integers. Write uniquely
\[
n=ab^2,
\]
where \(a,b\) are squarefree, \(\gcd(a,b)=1\), and \(b>1\). Multiplicativity and the local formula give
\[
P_t(n)=bT+2+t,
\qquad
T=\mu(a)\sigma_1(a)+\varphi(a)\varphi(b)\in\mathbb Z.
\]
If \(T\ge0\), then \(P_t(n)>0\) for \(t>-2\). If \(T\le-1\) and \(b\ge3\), then
\[
P_t(n)\le-b+2+t<0
\]
for \(t<1\).

The only remaining possibility is \(b=2\). Then \(a\) is odd. If \(\mu(a)=1\), the integer \(T\) is positive. If \(\mu(a)=-1\), then
\[
T=-\sigma_1(a)+\varphi(a).
\]
Here \(a>1\) has an odd number of distinct odd prime factors. Both \(\sigma_1(a)=\prod_{p\mid a}(p+1)\) and \(\varphi(a)=\prod_{p\mid a}(p-1)\) are divisible by \(2\), and the first is larger, so \(T\le-2\). Consequently
\[
P_t(n)\le-4+2+t=t-2<0.
\]
This exhausts all composite integers and proves the prime-only zero set on \((-2,1)\).

Finally,
\[
P_{-2}(1)=4-4=0.
\]
For \(18=2\cdot3^2\), one has \(\sigma_1^{(-1)}(18)=(-3)(3)=-9\), \(\varphi(18)=6\), and \(\mu(18)=0\), so
\[
P_1(18)=-9+6+2+1=0.
\]
Any open interval containing \(t=0\) that extends past either endpoint contains a failing endpoint. Thus \((-2,1)\) is maximal. \(\square\)

## Verification
The proof above is exact and infinite. The supplied `verify.py` is corroborative only. It implements trial-division factorization, the local Dirichlet-inverse formula, \(\mu\), and \(\varphi\) using exact integer and rational arithmetic. It checks the prime-only zero set through \(n=20000\) for six rational parameters strictly inside \((-2,1)\), checks the two endpoint witnesses exactly, and independently verifies the convolution identity \(\sigma_1^{(-1)}*\sigma_1=\varepsilon\) through \(n=500\).

The expected terminal line is:
`VERIFY_OK exact_params=6 n_max=20000 endpoint_witnesses=2 convolution_cases=500`

## Relationship to prior work
Zhichen Liu's recent preprint gives the local prime-power formula above, primary MSC 11A25, and proves that the three-function expression at the parameter value \(t=1\) has exactly the primes and \(18\) as zeros when the Jordan index is \(1\). It does not state the real-parameter interval \((-2,1)\).

A closely related published published-finding corpus finding proves a sharp parameter interval for the higher-index family \(k\ge2\): every \(t>-2\) preserves the prime-only zero set. That theorem explicitly excludes \(k=1\), where \(18\) is the obstruction at \(t=1\). The present result resolves exactly that exceptional index. Its proof is not an implication of the higher-index result: the higher-index positivity estimate fails at \(k=1\), and the argument here instead uses the integer factor \(bT\) together with the special \(b=2\) parity obstruction.

Targeted searches for the exact affine family, the exceptional-index interval, endpoint formulations, and stronger coverage returned the higher-index published-finding corpus theorem as the closest statement but no result covering the \(k=1\) interval.

## Limitations
The theorem classifies only the maximal connected open parameter interval containing \(t=0\). It does not classify all isolated or disconnected real parameter values outside \((-2,1)\). The finite verifier is not used to infer the infinite statement. Search cannot exclude an unindexed equivalent formulation outside the inspected literature and databases.

## References
1. Zhichen Liu, *Prime-Detecting Identities from Dirichlet Inversion and Jordan Totients*, arXiv:2609.33278v1, first publicly posted 27 September 2026; primary MSC 11A25.
2. published-finding corpus record `2026/10/4/SCOPE-sharp-parameter-stability-for-mixed-dirichlet-inverse-prime-crit--09c92f70d81c`, *Sharp parameter stability for mixed Dirichlet-inverse prime criteria*.
