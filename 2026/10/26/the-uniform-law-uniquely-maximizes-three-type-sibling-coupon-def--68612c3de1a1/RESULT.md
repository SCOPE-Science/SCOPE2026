# The uniform law uniquely maximizes three-type sibling coupon-deficit variance

## Finding
Let \(a,b,c>0\) satisfy \(a+b+c=1\). A principal collector draws independent coupons of three types with probabilities \(a,b,c\), stopping immediately when each type has appeared. Duplicate coupons are passed to a second collector. Let \(U\in\{1,2,3\}\) be the number of types still missing from the second collector at that stopping time. Then
\[
\operatorname{Var}(U)\le\frac7{12},
\]
with equality **only** for \(a=b=c=1/3\). The uniform law of \(U\) is \(\Pr(U=1,2,3)=(7,7,4)/18\).

## Assumptions and scope
Draws are independent, all three coupon probabilities are strictly positive, and the collection stops after the first full principal album. Only one secondary collector is considered. Define
\[
M=a^2+b^2+c^2+\frac{2ab}{(a+b)^2}+\frac{2ac}{(a+c)^2}+\frac{2bc}{(b+c)^2}.
\]
For every admissible parameter triple,
\[
\Pr(U=3)=6abc,\qquad \Pr(U=1)=2+6abc-M,\qquad \Pr(U=2)=M-1-12abc,
\]
and consequently
\[
\operatorname{Var}(U)=3M-2+12abc-M^2.
\]
The variance inequality concerns the **deficit** rather than the time needed to fill a collection. This is the first size with three possible deficit values; two-type deficits have only two values.

## Proof
First, \(U=3\) precisely when the first three draws have distinct types, yielding \(6abc\). To calculate \(\Pr(U=1)\), Poissonize the independent coupon streams, assigning rates \(a,b,c\). The order of arriving types is unchanged. For each type \(i\), condition on its first arrival at time \(t\), which must be the last first arrival. The other two types must each have appeared at least twice before time \(t\). Thus, writing \(p_1=a,p_2=b,p_3=c\),
\[
\Pr(U=1)=\sum_{i=1}^3\int_0^\infty p_i e^{-p_i t}\prod_{j\ne i}\left[1-(1+p_jt)e^{-p_jt}\right]\,dt.
\]
Expand the product; elementary exponential integrals give \(\Pr(U=1)=2+6abc-M\). Subtracting these two probabilities from one gives \(\Pr(U=2)=M-1-12abc\). Hence \(\mathbb E U=M\), \(\mathbb E U^2=3M-2+12abc\) and the displayed variance formula follows.

By symmetry, assume \(a\ge b\ge c\). Write \(a=(z+x+y)/S\), \(b=(z+y)/S\), \(c=z/S\), where \(x,y\ge0\), \(z>0\), and \(S=x+2y+3z\). Exact rational simplification yields
\[
\frac7{12}-\operatorname{Var}(U)
=\frac{P(x,y,z)}{12(y+2z)^4(x+y+2z)^4(x+2y+2z)^4(x+2y+3z)^4}.
\]
Here \(P\) is homogeneous of degree 16 and has exactly 140 nonzero monomials. Every coefficient is a positive integer, and each monomial contains a positive power of \(x\) or \(y\). The **entire coefficient certificate** is included in `CERTIFICATE.txt`, with an exact symbolic replay in `verify.py`. Since the denominator is positive and \(z>0\), the gap is zero exactly when \(x=y=0\), equivalent to \(a=b=c\). Substituting the uniform triple yields \(7/12\), completing the proof.

## Verification
Run `python verify.py` with Python 3 and SymPy. It reconstructs the rational identity and all 140 coefficients, checks their signs and boundary vanishing, and compares the formula against an independent exact-rational 27-state occupancy recursion for seven probability triples. The recorded output is in `verification-output.txt`. Finite enumerations check examples only; the symbolic identity plus positive-coefficient certificate proves the global inequality.

## Relationship to prior work
Doumas and Spektor (2026) proved uniform maximality of the **mean** sibling deficit. Long (2026, arXiv:2606.29635) also proved expectation extremality and uniform-model stochastic monotonicity across album size. Long (2026, arXiv:2606.31391) established uniform extremality of the **entire probability generating function** in the appropriate two-sided radial order and of every binomial moment; those stronger-in-transform results are explicitly credited, not claimed here. They do **not logically entail a variance inequality**: the uniform three-type deficit law \((7,7,4)/18\) dominates the artificial law \((79/100,0,21/100)\) in this same PGF/binomial-moment sense but has *smaller* variance, \(7/12<1659/2500\). The result proved here instead is the exact global variance extremum restricted to the natural three-coupon probability family. Long's April 2026 variance theorem concerns the *collection completion time*, not the secondary album's missing-type count.

## Limitations
The proof does not show global variance extremality for four or more coupon types, or other sibling indices. The strongest 2026 radial-transform paper was accessible by its abstract but not in full through available authorized routes; an explicit historical priority risk remains. The proof is mathematical and computationally reproducible, but no independent validation has been performed.

## References
- A. V. Doumas and S. Spektor, *Equal probabilities maximize the expected deficit in the siblings of the coupon collector*, arXiv:2606.21591v1 (19 June 2026), https://arxiv.org/abs/2606.21591.
- C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635v1 (28 June 2026), https://arxiv.org/abs/2606.29635.
- C. D. Long, *Radial Transform Extremality for the Siblings of the Coupon Collector*, arXiv:2606.31391v1 (30 June 2026), https://arxiv.org/abs/2606.31391.
- C. D. Long, *Terminal Defects, Growing Multiplicity, and Variance Extremality in the Double Dixie Cup Problem*, arXiv:2604.25108v1 (28 April 2026), https://arxiv.org/abs/2604.25108.
