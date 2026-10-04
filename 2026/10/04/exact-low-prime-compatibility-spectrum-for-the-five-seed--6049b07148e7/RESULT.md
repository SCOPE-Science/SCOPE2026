# Exact low-prime compatibility spectrum for the five-seed
## Finding
Let
\[
E_N=\left\{\sum_{n=1}^{N}\frac{t_n}{n}:t_n\in\{0,1\}\right\}
\]
and let \(\mathcal U\) be the set of positive integers \(N\) for which
\[
\sum_{n=1}^{N-1}\frac{w_n}{n}\ne\frac1N
\qquad\text{for every }w_n\in\{-1,0,1\}.
\]
For a prime \(p\), call \(p\) compatible with \(m\) when \(p\) divides none of the reduced numerators of
\[
\frac1m-\sum_{j=1}^{m-1}\frac{w_j}{j},\qquad w_j\in\{-1,0,1\}.
\]
For \(m=5\), the compatible primes are exactly
\[
\{5,59,71,79,89,101,103,109,127,131\}\cup\{p\text{ prime}:p>137\}.
\]
In particular, for each
\[
p\in\{59,71,79,89,101,103,109,127,131\}
\]
and every integer \(k\ge1\),
\[
5p^k\in\mathcal U
\quad\text{and hence}\quad
|E_{5p^k}|=2|E_{5p^k-1}|.
\]

## Assumptions and scope
The compatibility definition is the one introduced by Bettin, Grenié, Molteni and Sanna for their recursive construction of doubling indices. The claim is an exact classification only for the natural seed \(m=5\). It does not assert an asymptotic improvement for \(|\mathcal U(x)|\) or \(|E_N|\).

## Proof
For \(w_1,w_2,w_3,w_4\in\{-1,0,1\}\), set
\[
R(w_1,w_2,w_3,w_4)=\frac15-w_1-\frac{w_2}{2}-\frac{w_3}{3}-\frac{w_4}{4}.
\]
Since \(\operatorname{lcm}(1,2,3,4,5)=60\),
\[
R=\frac{A}{60},\qquad
A=12-60w_1-30w_2-20w_3-15w_4.
\]
Thus the reduced numerator is
\[
\frac{A}{\gcd(|A|,60)}
\]
when \(A\ne0\). Exhausting the \(3^4=81\) coefficient vectors gives no zero residual and gives exactly the following absolute reduced numerators:
\[
\begin{aligned}
\{&1,2,3,4,6,7,8,9,11,13,17,19,21,23,29,31,37,39,41,43,47,49,\\
&53,61,67,73,77,83,97,107,113,137\}.
\end{aligned}
\]
The absence of zero proves \(5\in\mathcal U\). Taking the union of the prime divisors of these numerators gives exactly
\[
\{2,3,7,11,13,17,19,23,29,31,37,41,43,47,53,61,67,73,83,97,107,113,137\}.
\]
Therefore the compatible primes at most \(137\) are exactly
\[
\{5,59,71,79,89,101,103,109,127,131\}.
\]
Every absolute reduced numerator is at most \(137\), so every prime \(p>137\) is automatically compatible. This proves the compatibility classification.

For completeness, the propagation from compatibility is reconstructed directly. Let \(p\) be compatible with \(5\) and suppose, toward a contradiction, that \(N=5p^k\notin\mathcal U\) for some \(k\ge1\). Then there are \(w_n\in\{-1,0,1\}\) with
\[
\sum_{n=1}^{N-1}\frac{w_n}{n}=\frac1{5p^k}.
\]
Separate the terms for which \(p^k\mid n\). Writing the reduced residual
\[
\frac15-\sum_{j=1}^{4}\frac{w_{p^k j}}{j}=\frac{B}{D},\qquad \gcd(B,D)=1,
\]
gives
\[
p^kD\sum_{\substack{1\le n<N\\p^k\nmid n}}\frac{w_n}{n}=B.
\]
For every term on the left, \(v_p(n)<k\), hence
\[
v_p\!\left(\frac{p^kD}{n}\right)=k+v_p(D)-v_p(n)\ge1.
\]
The left side is therefore in \(p\mathbf Z_{(p)}\). Since it equals the integer \(B\), one has \(p\mid B\), contradicting compatibility. Thus \(5p^k\in\mathcal U\).

Finally,
\[
E_N=E_{N-1}\cup\left(E_{N-1}+\frac1N\right).
\]
The two sets overlap exactly when \(1/N\) is a signed reciprocal sum using denominators below \(N\). Hence \(N\in\mathcal U\) if and only if \(|E_N|=2|E_{N-1}|\), which yields the stated doubling consequence.

## Verification
The standalone script `verify_compat5.py` enumerates all \(81\) coefficient vectors using exact rational arithmetic, independently checks the integer reduction formula, factors the complete numerator set by trial division, and asserts both the incompatible-prime set and the compatible-prime set through \(137\). Its successful terminal line is `VERIFY_OK`.

The proof of propagation above is symbolic and does not depend on finite experimentation beyond the exact \(m=5\) compatibility census.

## Relationship to prior work
Bettin, Grenié, Molteni and Sanna define \(\mathcal U\) and compatibility and prove the general propagation principle \(m\in\mathcal U\) plus compatibility of \(p\) implies \(mp^k\in\mathcal U\). For \(m=5\), they use the coarse sufficient condition \(p>g_5=137\) when deriving their explicit lower bound. Their inspected text explicitly singles out an exceptional compatible prime for \(m=4\), namely \(23\), but does not give the complete exceptional compatibility spectrum for \(m=5\).

The earlier Bleicher--Erdős work studies distinct reciprocal subsums and supplies the asymptotic framework that the recent paper improves; it does not provide this finite compatibility classification. The present result is therefore a local exact refinement of the recent recursive mechanism, not a replacement for its asymptotic argument.

## Limitations
This result classifies one seed, \(m=5\). The nine mixed prime rays below the coarse cutoff are finitely many fixed-prime families, so by themselves they do not change the leading asymptotic constant in the cited lower bound. A literature search cannot exclude the possibility that the same finite list appears in an unindexed computation; no such occurrence was found in the inspected primary sources or targeted searches.

## References
1. S. Bettin, L. Grenié, G. Molteni, C. Sanna, *A lower bound for the number of Egyptian fractions*, arXiv:2509.10030v1, 12 September 2025. Primary MSC 11D68.
2. M. N. Bleicher, P. Erdős, *The number of distinct subsums of* \(\sum_{i=1}^{N}1/i\), *Mathematics of Computation* 29 (1975), 29--42.
