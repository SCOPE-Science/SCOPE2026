# Sharp dimension-three majorization law for logarithmic widths of orthogonal crosspolytopes

## Finding

The geometric mean of directional widths of an orthogonal crosspolytope exhibits a sharp *dimension-three cutoff* for monotonicity under majorization of its squared semiaxes. For dimensions \(d=2,3\), it is strictly increased by every nontrivial balancing of squared semiaxes, and hence regular crosspolytopes are its unique maximizers up to orthogonal transformations and prescribed normalization. In all dimensions \(d\ge4\), this global majorization principle is false even for full-dimensional crosspolytopes; the counterexample and its quantitative gap below are exact.

## Assumptions and scope

Fix an integer \(d\ge2\) and a probability vector \(w=(w_1,\ldots,w_d)\) in the closed simplex \(\Delta_{d-1}\). Write
\[
 C_d(w)=\operatorname{conv}\{\pm\sqrt{w_i}e_i:1\le i\le d\},\qquad
 W_w(u)=2\max_{1\le i\le d}\sqrt{w_i}|u_i|,
\]
where \(u\in S^{d-1}\). The quantity of interest is
\[
 L_d(w)=\int_{S^{d-1}}\log W_w(u)\,d\sigma(u),\qquad G_d(w)=\exp L_d(w),
\]
with \(\sigma\) the Haar *probability* measure. Coordinate vectors with zero squared semiaxes are allowed as boundary limits; their logarithmic mean widths are finite. Majorization uses sorted partial sums: \(a\succ b\) means \(\sum_{i=1}^k a_i^\downarrow\ge\sum_{i=1}^k b_i^\downarrow\) for \(1\le k<d\), with equal totals.

**Theorem.** If \(d\in\{2,3\}\), then \(a\succ b\) implies \(L_d(a)\le L_d(b)\), with equality only for permutations. The unique maximizer is \(w=(1/d,\ldots,1/d)\); the only minimizers are permutations of \((1,0,\ldots,0)\). If \(d=3\) and all \(w_i>0\), define \(q=\sqrt{w_1w_2+w_1w_3+w_2w_3}\); the exact ambient partial derivatives are
\[
 \frac{\partial L_3}{\partial w_i}=\frac{1}{\pi w_i}\arctan\!\left(\frac{w_i}{q}\right),\quad i=1,2,3.
\]
For every \(d\ge4\), put \(a=(1/3,1/3,1/3,0,\ldots,0)\) and \(b=(8/25,8/25,8/25,1/25,0,\ldots,0)\). Then \(a\succ b\), whereas
\[
 L_d(b)-L_d(a)\le\frac12\log\frac{24}{25}+\frac{1}{6\sqrt2\pi^2}<0.
\]
The same reversal holds for *strictly positive* squared semiaxes after replacing \(a,b\) by \((1-\eta)a+\eta(1/d,\ldots,1/d)\) and \((1-\eta)b+\eta(1/d,\ldots,1/d)\) for all sufficiently small \(\eta>0\).

## Proof

**Gaussian reduction and finiteness.** Let \(Z=(Z_1,\ldots,Z_d)\) have independent standard-normal coordinates, write \(Z=RU\), where \(U\) is Haar-uniform on \(S^{d-1}\), and \(R\) is independent of \(U\). Thus
\[
 L_d(w)=\log2+F_d(w)-\mathbb E\log R,\qquad
 F_d(w)=\mathbb E\log\max_i\sqrt{w_i}|Z_i|.
\]
The radial term depends on dimension, not \(w\). Since some \(w_i\ge1/d\), \(\max_i\sqrt{w_i}|Z_i|\ge d^{-1/2}\min_j|Z_j|\). Since the minimum absolute Gaussian coordinate has finite logarithmic moment and the maximum is bounded by \(\max_i|Z_i|\), \(F_d\) is finite and continuous on the closed simplex by dominated convergence. For positive \(w\), ties in the maximizing coordinate have probability zero; differentiation under the integral is justified locally by \(\left|\partial_{w_i}\log\max_j\sqrt{w_j}|Z_j|\right|\le1/(2w_i)\). Therefore
\[
 \frac{\partial F_d}{\partial w_i}=\frac{\Pr\{i\text{ is the unique maximum}\}}{2w_i}.
\]

**Exact three-dimensional winner probabilities.** For three positive weights, conditioning on the sign of \(Z_i\) identifies the event that coordinate \(i\) wins with two opposite rectangular cones. In the positive half-space, the cone at unit height has rectangular half-sides \(A=\sqrt{w_i/w_j}\) and \(B=\sqrt{w_i/w_k}\), where \(\{i,j,k\}=\{1,2,3\}\). The solid angle of that cone is
\[
 \Omega(A,B)=4\int_0^A\int_0^B(1+x^2+y^2)^{-3/2}\,dy\,dx
 =4\arctan\frac{AB}{\sqrt{1+A^2+B^2}}.
\]
Including its opposite cone and dividing by the full sphere area \(4\pi\) gives
\[
 \Pr\{i\text{ wins}\}=\frac{2}{\pi}\arctan\!\frac{w_i}{q},\qquad q=\sqrt{w_1w_2+w_1w_3+w_2w_3}.
\]
Substitution gives the derivative formula in the theorem. For every fixed \(q>0\), the function \(t\mapsto\arctan(t/q)/t\) decreases strictly on \(t>0\): its derivative has the sign of \(z/(1+z^2)-\arctan z<0\) at \(z=t/q\). Consequently, whenever \(w_i>w_j\), one has \(\partial_{w_i}L_3<\partial_{w_j}L_3\). Along every two-coordinate balancing path with positive entries, \(L_3\) therefore increases strictly. The standard finite decomposition of majorization into coordinate-balancing operations and continuity extend the ordering and strictness to the closed simplex. Restricting the three-coordinate Gaussian formula to \(w_3=0\) yields the two-dimensional ordering: although \(\mathbb E\log R\) is dimension-dependent, it is independent of \(w\), and all three-coordinate zero-padded Gaussian comparisons are identical to the two-coordinate ones. Strictness on each two-coordinate edge follows either from the preceding strict three-dimensional comparisons by limits or directly from the two-coordinate winner formula \(\Pr\{1\text{ wins}\}=(2/\pi)\arctan\sqrt{w_1/w_2}\), yielding the strict derivative comparison. The extremal equality cases follow.

**A sharp dimensional obstruction.** Let \(a=(1/3,1/3,1/3,0,\ldots,0)\), and set \(b=((1-\varepsilon)/3,(1-\varepsilon)/3,(1-\varepsilon)/3,\varepsilon,0,\ldots,0)\). For \(0<\varepsilon\le1/4\), \(a\succ b\). Define \(H=\max_{i\le3}|Z_i|/\sqrt3\), \(Y=|Z_4|\), and \(t=\sqrt{\varepsilon/(1-\varepsilon)}\). Independence gives
\[
 F_d(b)-F_d(a)=\frac12\log(1-\varepsilon)+J(t),\qquad
 J(t)=\mathbb E[\log(tY/H)]_+.
\]
For each fixed positive \(Y\), the tail-integral identity gives
\[
 \mathbb E[\log(tY/H)]_+\mid Y=\int_0^{tY}\frac{\Pr(H<s)}s\,ds.
\]
The folded-normal bound \(\Pr(|Z_i|<x)\le\sqrt{2/\pi}\,x\) implies \(\Pr(H<s)\le(\sqrt{6/\pi}\,s)^3\). As \(\mathbb EY^3=2\sqrt2/\sqrt\pi\),
\[
 0\le J(t)\le\frac{(6/\pi)^{3/2}}3\,\mathbb EY^3\,t^3
 =\frac{8\sqrt3}{\pi^2}t^3.
\]
Choose \(\varepsilon=1/25\), so \(t^2=1/24\). Then
\[
 F_d(b)-F_d(a)\le\frac12\log\frac{24}{25}+\frac1{6\sqrt2\pi^2}<0.
\]
The explicit numerical constant is negative (a purely analytic verification uses \(\log(1+x)>x/(1+x)\) for \(x>0\), with \(x=1/24\), and \(\pi>3\)). Since the radial normalizing term cancels, this is exactly the asserted inequality for \(L_d\). The two vectors have a strict majorization relation. By the Hardy–Littlewood–Pólya doubly stochastic characterization, uniform mixing preserves the majorization relation, and by continuity preserves the strict reversed inequality for small \(\eta>0\). Hence all dimensions \(d\ge4\) fail the property even for genuine full-dimensional crosspolytopes.

## Verification

The accompanying executable \(verify.py\) checks the exact signed upper bound, the three-dimensional solid-angle derivative against centered finite differences of the independent Gaussian maximum density integral, and the four-coordinate counterexample against independent numerical integration. Run \(\texttt{python3 verify.py}\) in the directory containing this document. The analytic proof above, not the finite quadrature, establishes the statements for all permitted dimensions and weights.

## Relationship to prior work

Gergely Ambrus, *Extremal cross-polytopes and Gaussian vectors*, arXiv:1208.5923 (first public August 29, 2012), proves a striking extremum theorem for the **arithmetic** mean width of orthogonal crosspolytopes: in dimensions at least three it is minimized by equal axes and maximized by at-most-two-coordinate supports. The present quantity is the **exponential of the mean logarithm** of directional widths; it is a lower-tail-sensitive, non-linear functional, not a reformulation of the arithmetic mean. Indeed our direction of extremization in dimension three is opposite Ambrus's. Finch's regular-crosspolytope mean-width calculation (arXiv:1112.0499) and the moment/distribution results for regular polytopes of Kabluchko, Litvak and Zaporozhets (arXiv:1511.08479) do not imply the arbitrary-axis majorization law and the dimension-four obstruction. Comparisons also considered the squared-axes Gaussian maximum and positive-moment formulations.

## Limitations

The positive theorem asserts Schur concavity only in dimensions two and three; the higher-dimensional result is a counterexample to *Schur concavity*, not a complete classification of all higher-dimensional maximizers. Zero squared axes are included solely as boundary limits of full-dimensional convex bodies. Numerical verification supplies examples but cannot certify the infinite-dimensional scope. Equivalence under another name in older convex-geometric or Gaussian-inequality literature remains possible; absence from inspected sources does not establish absolute novelty. No independent scientific validation has been performed.

## References

1. G. Ambrus, *Extremal cross-polytopes and Gaussian vectors*, arXiv:1208.5923v1 (August 29, 2012), https://arxiv.org/abs/1208.5923 ; Theorems 1–3 and Section 2.
2. S. R. Finch, *Mean Width of a Regular Cross-Polytope*, arXiv:1112.0499 (December 2, 2011), https://arxiv.org/abs/1112.0499 .
3. Z. Kabluchko, A. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (November 2015), https://arxiv.org/abs/1511.08479 .
