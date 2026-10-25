# A sharp two-pair correlation law for the four-cube Hypercube inequality

## Finding

Let \(Q=\{0,1\}^4\), and let \(a,b,c,d>0\). For each vertex \(v=(v_1,v_2,v_3,v_4)\), define its weight by the parities of the disjoint coordinate pairs:
\[
x_v=\begin{cases}a&v_1=v_2,\\ b&v_1\ne v_2\end{cases}\cdot
\begin{cases}c&v_3=v_4,\\ d&v_3\ne v_4.\end{cases}
\]
For a five-element subset \(U\subset Q\), put \(\operatorname{Vol}(U)=4!\,\operatorname{vol}_4(\operatorname{conv}U)\), and set
\[
P(x)=\sum_{\substack{U\subset Q\\ |U|=5}}\operatorname{Vol}(U)\prod_{v\in U}x_v,\qquad T=\sum_{v\in Q}x_v,\qquad S_F=\sum_{v\in F}x_v,
\]
where \(F\) ranges over all eight facets of \(Q\). Define the two within-pair correlations
\[
\rho=\frac{a-b}{a+b},\qquad \sigma=\frac{c-d}{c+d}.
\]
Then the following **exact identity** holds:
\[
\boxed{\frac{P(x)T^3}{\prod_F S_F}=
\frac{(1-\rho^2)(1-\sigma^2)\bigl(105+15\rho^2+15\sigma^2-7\rho^2\sigma^2\bigr)}{128}.}
\]
Consequently, for every choice of strictly positive parameters,
\[
\boxed{0<\frac{P(x)T^3}{\prod_F S_F}\le\frac{105}{128}<1,}
\]
and the upper bound is attained **if and only if** \(a=b\) and \(c=d\) (all sixteen vertex weights are equal). Thus the dimension-four Hypercube inequality has a sharp relative gap of \(23/128\) on this full two-correlation-parameter family. The exact ratio decreases strictly as either squared correlation increases with the other fixed.

## Assumptions and scope

All coordinates take values in \(\{0,1\}\), the volume is the ordinary four-dimensional Euclidean volume normalized by \(4!\), and the parameters are strictly positive. Positive common rescaling of the first pair \((a,b)\), independently of the second pair \((c,d)\), leaves the ratio unchanged. Thus \((\rho,\sigma)\in(-1,1)^2\) parametrizes the family up to its irrelevant scalings.

The normalized weights are equivalent to the probability distribution on four fair bits formed by taking two independent **pairs**, with arbitrary correlation inside each pair. More explicitly, \(x_v/T=(1+\rho(-1)^{v_1+v_2})(1+\sigma(-1)^{v_3+v_4})/16\). Individual bits are unbiased, but nonzero within-pair correlations mean that the four bits are not all independent. No conclusion is asserted for arbitrary sixteen-tuples of weights, or for general four-bit joint distributions.

## Proof

For any fixed first coordinate, the sum of the weights of its partner is \(a+b\). Analogously, the sum of the second pair after fixing either of its coordinates is \(c+d\). Hence
\[
T=4(a+b)(c+d),\qquad S_F=2(a+b)(c+d)=T/2\quad\text{for each facet }F.
\]
Therefore the ratio to be determined is \(P(x)/[4(a+b)^5(c+d)^5]\).

The finite exact determinant enumeration, independently reconstructed in `verify.py`, yields
\[
\begin{aligned}
P(x)={}&8abcd(a+b)(c+d)\bigl[8(a^2+b^2)(c^2+d^2)\\
&+14(a^2+b^2)cd+14ab(c^2+d^2)+17abcd\bigr].
\end{aligned}
\]
For completeness, its coefficients at monomials \(a^j b^{5-j}c^k d^{5-k}\), with \(j,k\in\{1,2,3,4\}\), are exactly the following matrix, with rows and columns ordered increasingly:
\[
\begin{pmatrix}
64&176&176&64\\
176&424&424&176\\
176&424&424&176\\
64&176&176&64
\end{pmatrix}.
\]
All other monomial coefficients vanish. Each coefficient is the sum of exact absolute four-by-four determinants of differences of vertices from a five-vertex subset. There are exactly \(\binom{16}{5}=4368\) possible subsets, so this gives an exhaustive finite coefficient identity, not a sample-based approximation. The companion checker uses both integer-preserving elimination and an independent Leibniz determinant expression for every subset, then verifies the factored polynomial coefficientwise.

Set \(r=ab/(a+b)^2\) and \(s=cd/(c+d)^2\). Substituting the factored identity into the ratio and simplifying gives
\[
\frac{P(x)T^3}{\prod_F S_F}=2rs\bigl(8-2r-2s-7rs\bigr).
\]
Since \(r=(1-\rho^2)/4\) and \(s=(1-\sigma^2)/4\), this is precisely the boxed correlation identity.

To establish the sharp global bound (not just a finite test), set \(u=\rho^2\), \(v=\sigma^2\), both in \([0,1)\), and denote the boxed expression by \(R(u,v)\). Direct exact differentiation yields
\[
\frac{\partial R}{\partial u}=-\frac{(1-v)(90+30u+22v-14uv)}{128}<0,
\]
for \(u,v\in[0,1)\): indeed \(90+30u+22v-14uv>0\) there. The derivative in \(v\) is the symmetric expression. Consequently \(R\) has its unique maximum at \(u=v=0\), namely \(105/128\), and is strictly decreasing in either squared correlation while the other is fixed. Strict positivity follows directly from the formula. This proves all stated assertions. By continuity the ratio tends to zero when either squared correlation tends to one.

## Verification

Run `python3 verify.py` with Python 3 standard library only. The exact-arithmetic checker enumerates all \(4368\) vertex subsets, computes the normalized simplex volume in two independent integer determinant routines, groups the monomials, and verifies the displayed factorization in the integer polynomial ring. It reports \(1360\) zero-volume subsets and positive determinant multiplicities \(2672,320,16\) for normalized volumes \(1,2,3\), respectively. It also checks the uniform value \(105/128\) and selected rational-parameter evaluations; the latter numerical evaluations are diagnostic only. The all-real-parameter result follows from the proved symbolic identity and strict derivative sign.

## Relationship to prior work

Averkov, von Dichter and Soprunov formulated the Hypercube inequality for nonnegative weights on the \(d\)-cube as a partial-submodularity problem associated with projection volumes of zonoids. Their first unresolved unrestricted instance is \(d=4\), the dimension treated here. Their paper establishes \(d=3\), but not the general sixteen-variable \(d=4\) statement. This result is a **restricted exact confirmation**, not a proof of the unrestricted conjecture.

Another exact investigation of that same conjectural dimension gives the sharp factor \(105/128\) when the vertex weights depend only on Hamming weight and are unchanged by complementation. The present family instead treats pair parity: for example, vertices of the same Hamming weight can have different weights. Neither family contains the other, except at special intersections, so the earlier symmetry-cone bound does not establish the correlated-pair identity. Likewise, a family with four mutually independent Bernoulli bits does not encompass nonzero pair correlations. The matching numerical sharp constant is explained by the shared uniform-weight extremizer, not by containment of the parameter spaces.

## Limitations

This solves the exact ratio only for two independent correlated pairs of unbiased bits. It makes no claim for general correlated four-bit measures, biased pair marginals, or unrestricted nonnegative vertex weights. Its optimal constant is only for the stated parameter family. The finite determinant enumeration establishes a finite polynomial identity; the analytic inequality for all positive real inputs separately requires (and is supplied by) the derivative argument. Priority against inaccessible or unindexed older mathematical work has not been independently established.

## References

1. G. Averkov, K. von Dichter, and I. Soprunov, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909v1, first posted 14 August 2026, https://arxiv.org/abs/2608.14909 (full primary paper examined).
2. *Sharp symmetric gap for the first open hypercube inequality*, mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-symmetric-gap-for-the-first-open-hypercube-inequality--4f3e013d18c9 (complete mathematical result read for implication comparison).
