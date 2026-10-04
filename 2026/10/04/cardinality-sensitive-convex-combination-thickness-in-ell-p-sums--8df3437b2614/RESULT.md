# Cardinality-sensitive convex-combination thickness in \(\ell_p\)-sums

## Finding
Let \(1<p<\infty\), let \(\Gamma\) have at least two elements, and let every \(X_\gamma\) be a nonzero real Banach space. For
\[
Z=\left(\bigoplus_{\gamma\in\Gamma}X_\gamma\right)_p,
\]
write \(\mathcal T^{cc}(Z)\) for the Daugavet thickness index obtained from finite convex combinations of nonempty slices of \(B_Z\). If \(|\Gamma|=n<\infty\), then
\[
\mathcal T^{cc}(Z)\le \left(1+(n-1)^{1-p}\right)^{1/p}.
\]
If \(\Gamma\) is infinite, then
\[
\mathcal T^{cc}(Z)\le 1.
\]

## Assumptions and scope
A slice of \(B_Z\) is written
\[
S(B_Z,F,\delta)=\{z\in B_Z:F(z)>1-\delta\},
\]
where \(F\in S_{Z^*}\) and \(0<\delta<1\). We use the slice formulation of \(\mathcal T^{cc}\): it is the infimum of radii \(r>0\) for which some \(x\in S_Z\) and some finite convex combination \(C\) of nonempty slices of \(B_Z\) satisfy \(C\subset B(x,r)\). The argument applies to arbitrary nonzero real summands; no Daugavet, octahedrality, separability, or norm-attainment hypothesis is used. The range \(1<p<\infty\) is essential to the decay in the displayed bound.

## Proof
Assume first that \(\Gamma\) is finite and \(|\Gamma|=n\ge2\). Put \(m=n-1\), choose distinct indices \(\gamma_0,\gamma_1,\ldots,\gamma_m\), and choose \(x_0\in S_{X_{\gamma_0}}\), viewed as a vector of \(S_Z\) supported on \(\gamma_0\). For each \(1\le j\le m\), choose \(f_j\in S_{X_{\gamma_j}^*}\), extend it to \(F_j\in S_{Z^*}\) by putting it on coordinate \(\gamma_j\) and zero elsewhere, and let
\[
S_j=S(B_Z,F_j,\delta).
\]
These slices are nonempty because a norm-one functional has supremum one on the unit ball.

If \(z^{(j)}\in S_j\), then \(\|z^{(j)}_{\gamma_j}\|>1-\delta\). Hence, for the coordinate projection \(P_{\gamma_j}\),
\[
\left\|(I-P_{\gamma_j})z^{(j)}\right\|_p
\le \eta_\delta:=\left(1-(1-\delta)^p\right)^{1/p}.
\]
Consider the equal-weight convex combination
\[
C_\delta=\frac1m\sum_{j=1}^m S_j.
\]
For arbitrary \(y\in C_\delta\), select \(z^{(j)}\in S_j\) with \(y=m^{-1}\sum_jz^{(j)}\), and split
\[
a=\frac1m\sum_{j=1}^mP_{\gamma_j}z^{(j)},\qquad
r=\frac1m\sum_{j=1}^m(I-P_{\gamma_j})z^{(j)}.
\]
Then \(y=a+r\) and \(\|r\|_p\le\eta_\delta\). The main terms in \(a\) have disjoint supports, so
\[
\|a\|_p^p
=\frac1{m^p}\sum_{j=1}^m\|z^{(j)}_{\gamma_j}\|^p
\le m^{1-p}.
\]
Moreover, \(a\) vanishes on coordinate \(\gamma_0\), whereas \(x_0\) is supported there. Therefore
\[
\|x_0-a\|_p^p=1+\|a\|_p^p\le1+m^{1-p}.
\]
The triangle inequality now gives, uniformly for \(y\in C_\delta\),
\[
\|x_0-y\|_p
\le \left(1+m^{1-p}\right)^{1/p}+\eta_\delta.
\]
Since \(\eta_\delta\to0\) as \(\delta\downarrow0\), the definition of \(\mathcal T^{cc}\) yields
\[
\mathcal T^{cc}(Z)\le\left(1+(n-1)^{1-p}\right)^{1/p}.
\]

If \(\Gamma\) is infinite, choose \(m+1\) distinct coordinates for any positive integer \(m\) and repeat the same construction. The unselected coordinates are absorbed into the remainder \(r\), so the same estimate holds:
\[
\mathcal T^{cc}(Z)\le\left(1+m^{1-p}\right)^{1/p}.
\]
Letting \(m\to\infty\) gives \(\mathcal T^{cc}(Z)\le1\).

## Verification
Every estimate above is analytic. The only limiting steps are \(\eta_\delta\to0\) as \(\delta\downarrow0\) and \(m^{1-p}\to0\) as \(m\to\infty\), both valid because \(p>1\). At \(n=2\), the finite bound becomes \(2^{1/p}\), agreeing with the published two-summand upper bound. No finite experiment, enumeration, or numerical certificate is used as a substitute for proof.

## Relationship to prior work
Haller, Langemets, Lima, Nadel and Rueda Zoca introduced the three Daugavet thickness indices and developed their behavior under two-factor direct sums in arXiv:2005.02045. In particular, their two-summand \(\ell_p\) result gives the upper scale \(2^{1/p}\), and for Daugavet summands it is an equality for all three indices. Their finite-sum remarks extend certain lower estimates and the slice-index upper argument, but the inspected statements do not give a cardinality-dependent upper bound for \(\mathcal T^{cc}\). The present argument uses the extra freedom of averaging many coordinate slices, producing the factor \((n-1)^{1-p}\) and the infinite-family limit one.

The earlier absolute-sum work of Haller, Langemets and Nadel, arXiv:1702.03140, studies average roughness, octahedrality and diameter-two properties of absolute sums. Those convex-combination diameter results concern a different invariant and do not imply containment of a convex combination of slices in a ball centered at a sphere point, which is the requirement defining \(\mathcal T^{cc}\).

## Limitations
The result is only an upper bound. It does not claim optimality for \(n\ge3\) or for infinite \(\Gamma\), nor does it classify equality cases. The proof does not address \(p=1\) or \(p=\infty\). A 2014 paper of Oja on sums of slices in direct sums was identified as relevant background, but only bibliographic metadata was available in this review; consequently, an unindexed equivalent estimate in that older literature remains a residual literature risk.

## References
1. R. Haller, J. Langemets, V. Lima, R. Nadel, A. Rueda Zoca, *On Daugavet indices of thickness*, arXiv:2005.02045, first public version 2020-05-05.
2. R. Haller, J. Langemets, R. Nadel, *Stability of average roughness, octahedrality, and strong diameter 2 properties of Banach spaces with respect to absolute sums*, arXiv:1702.03140, first public version 2017-02-10.
3. E. Oja, *Sums of slices in direct sums of Banach spaces*, Proceedings of the Estonian Academy of Sciences 63 (2014), DOI:10.3176/proc.2014.1.03.
