# Curvature-distortion numbers of spider trees

## Result

For integers \(d\ge 3\) and \(\ell_1,\ldots,\ell_d\ge 1\), let
\[
\operatorname{Sp}(\ell_1,\ldots,\ell_d)
\]
be the spider tree with center \(c\) of degree \(d\), whose \(i\)-th arm is a path of
\(\ell_i\) edges from \(c\) to a leaf. We determine exactly the LLY curvature-distortion
number introduced by Xia.

For \(s\ge d\) and \(\ell\ge 2\), let \(\rho_\ell(s)>1\) be the unique solution of
\[
\rho^{\ell-1}(\rho+1)=s,
\]
and define
\[
h_1(s)=\frac1s,\qquad
h_\ell(s)=\frac{1}{1+\rho_\ell(s)}\quad(\ell\ge2).
\]
There is a unique \(s_\ast\ge d\) satisfying
\[
\sum_{i=1}^d h_{\ell_i}(s_\ast)=1.
\]

If \(L=\max_i\ell_i\ge2\), then
\[
\boxed{\operatorname{DN}_{\mathrm{LLY}}
\bigl(\operatorname{Sp}(\ell_1,\ldots,\ell_d)\bigr)
=\rho_L(s_\ast)^{L-1}.}
\]
If \(L=1\), the spider is the star \(K_{1,d}\) and the value is \(1\).

More precisely, write the edges on arm \(i\), from the center outward, as
\(e_{i,1},\ldots,e_{i,\ell_i}\). The canonical normalized optimal weight is
\[
w^\star(e_{i,j})=
\begin{cases}
1,&\ell_i=1,\\
\rho_{\ell_i}(s_\ast)^{\ell_i-j},&\ell_i\ge2.
\end{cases}
\]
Thus every long arm carries a geometric progression of weights ending at the
pendant value \(1\).

### Uniform subdivisions and sharp extremals

If every arm has the same length \(L\), i.e. the tree is obtained by subdividing
every edge of \(K_{1,d}\) into a path of length \(L\), then
\[
\boxed{\operatorname{DN}_{\mathrm{LLY}}=(d-1)^{L-1}.}
\]
Hence a tree with only one branch vertex can have exponentially large
curvature-distortion under uniform subdivision.

At the opposite extreme, if exactly one arm has length \(L\ge2\) and the other
\(d-1\) arms have length \(1\), then
\[
\boxed{\operatorname{DN}_{\mathrm{LLY}}
=(d-1)^{(L-1)/L}.}
\]
Consequently, among all \(d\)-arm spiders with maximum arm length \(L\ge2\),
\[
\boxed{
(d-1)^{(L-1)/L}
\le
\operatorname{DN}_{\mathrm{LLY}}
\le
(d-1)^{L-1}.
}
\]
The lower equality occurs exactly when, up to permutation, the arm-length vector is
\((L,1,\ldots,1)\); the upper equality occurs exactly for
\((L,\ldots,L)\).

This sharpens suppression monotonicity on a natural family: suppressing all
degree-two vertices always produces \(K_{1,d}\), of distortion \(1\), while the
unsuppressed distortion can be as large as \((d-1)^{L-1}\).

## Proof

Xia's tree-like edge formula says that for an edge \(uv\) of a tree,
\[
\kappa_{\mathrm{LLY}}^w(u,v)\ge0
\quad\Longleftrightarrow\quad
w_{uv}^2\ge
A_{u\mid v}(w)A_{v\mid u}(w),
\]
where \(A_{u\mid v}\) is the total weight at \(u\) excluding \(uv\).
The finite-tree fixed-point theorem further states that the unique normalized
optimal weight \(w^\star\) assigns weight \(1\) to every pendant edge and satisfies
equality on every non-pendant edge.

Fix one arm of length \(\ell\ge2\), and denote its canonical weights from the
center outward by \(x_1,\ldots,x_\ell\). Since \(x_\ell=1\), the zero-curvature
equations at the internal degree-two edges give
\[
x_j^2=x_{j-1}x_{j+1}.
\]
Thus consecutive ratios are constant. Writing that ratio as \(\rho\ge1\),
\[
x_j=\rho^{\ell-j}.
\]

Let
\[
s=\sum_{i=1}^d w^\star(e_{i,1})
\]
be the total canonical weighted degree of the center. On a long arm, the
center-adjacent edge is non-pendant, and its zero-curvature equation is
\[
x_1^2=(s-x_1)x_2.
\]
Substituting \(x_1=\rho^{\ell-1}\) and \(x_2=\rho^{\ell-2}\) yields
\[
s=\rho^{\ell-1}(\rho+1).
\]
A unit-length arm contributes the pendant weight \(1\). Therefore
\[
s=
\#\{i:\ell_i=1\}
+
\sum_{\ell_i\ge2}\rho_{\ell_i}(s)^{\ell_i-1}.
\]
Dividing by \(s\) and using
\[
\rho_\ell(s)^{\ell-1}=\frac{s}{1+\rho_\ell(s)}
\]
gives exactly
\[
\sum_i h_{\ell_i}(s)=1.
\]

For \(\ell\ge2\), the function
\(\rho\mapsto \rho^{\ell-1}(\rho+1)\) is strictly increasing on
\([1,\infty)\), so \(\rho_\ell(s)\) is well defined for \(s\ge d\ge3\).
Each \(h_\ell(s)\) is continuous and strictly decreasing in \(s\). At \(s=d\),
\(\rho_\ell(d)\le d-1\), hence every \(h_{\ell_i}(d)\ge1/d\); while the sum tends
to \(0\) as \(s\to\infty\). This proves existence and uniqueness of \(s_\ast\).

The displayed geometric weights therefore satisfy the full fixed-point system,
so the finite-tree fixed-point theorem identifies them with the canonical optimal
weight.

For fixed \(s>2\), \(h_\ell(s)\) is strictly increasing in \(\ell\). For
\(\ell=1\) versus \(2\), if \(r=\rho_2(s)>1\), then
\(h_2(s)=r/s>1/s=h_1(s)\). For \(\ell\ge2\),
\[
r^{\ell}(r+1)>r^{\ell-1}(r+1)\qquad(r>1),
\]
so \(\rho_{\ell+1}(s)<\rho_\ell(s)\), and hence
\(h_{\ell+1}(s)>h_\ell(s)\). Therefore the first edge on a longest arm has the
largest canonical weight, proving the formula for the distortion.

The same monotonicity also shows that lengthening any arm strictly increases the
root \(s_\ast\), and hence strictly increases the distortion. It follows that,
among spiders with fixed \(d\) and maximum arm length \(L\), the unique minimum
has one arm of length \(L\) and all others of length \(1\), while the unique
maximum has all arms of length \(L\).

For the minimum pattern, let \(r=\rho_L(s_\ast)\). Then
\[
\frac{d-1}{s_\ast}+\frac1{1+r}=1,\qquad
s_\ast=r^{L-1}(r+1),
\]
which reduces to \(r^L=d-1\), giving
\[
\operatorname{DN}_{\mathrm{LLY}}=r^{L-1}
=(d-1)^{(L-1)/L}.
\]
For the uniform pattern,
\[
\frac{d}{1+r}=1,
\]
so \(r=d-1\) and
\[
\operatorname{DN}_{\mathrm{LLY}}=(d-1)^{L-1}.
\]
This proves all claims.

## Relation to prior literature

Q. Xia introduced the curvature-distortion number and proved the finite-tree
fixed-point formula, uniqueness of the canonical optimal weight, suppression
monotonicity, and a branch-vertex bound in
*Curvature-Distortion Numbers of Graphs: Nonnegative Lin--Lu--Yau Curvature*,
arXiv:2609.12125v2 (2026).

The current v2 full text was inspected. Its explicit finite-tree examples are
double stars and a symmetric three-center tree. It also gives the strict
suppression example \(ST_{2,1}\), which is the special case
\(\operatorname{Sp}(2,1,1)\) of the one-long-arm formula above. The paper does
not state a spider-family formula or the sharp fixed-\((d,L)\) extremal law.

Related 2026 work on weighted Lin--Lu--Yau curvature studies prescribed-curvature
flows and constant-curvature discrete Einstein metrics rather than the minimum
multiplicative spread required for nonnegative curvature. In particular,
Bai--Hua study Perron eigenvectors for constant-curvature metrics on trees, and
Lin--Liu study prescribed-curvature Ricci flow.

To the best of our knowledge, the scalar spider law, the geometric canonical
weights for arbitrary arm lengths, and the sharp exponential uniform-subdivision
extremum above have not appeared previously.

## Limitations

The result concerns finite spider trees under the fixed-combinatorial-distance
weighted Lin--Lu--Yau convention used in arXiv:2609.12125. It does not give a
closed elementary expression for \(s_\ast\) for arbitrary mixed arm lengths;
instead it reduces the full edge fixed-point system to a unique scalar equation.
The main originality risk is very recent parallel work or a differently
terminologized consequence in the rapidly developing weighted-curvature
literature. No independent validation is asserted.

## References

1. Q. Xia, *Curvature-Distortion Numbers of Graphs: Nonnegative Lin--Lu--Yau Curvature*, arXiv:2609.12125v2, 2026. https://arxiv.org/abs/2609.12125
2. S. Bai and B. Hua, *Discrete Einstein metrics on trees*, arXiv:2604.22449, 2026. https://arxiv.org/abs/2604.22449
3. Y. Lin and S. Liu, *The Ricci flow with prescribed curvature on graphs*, arXiv:2603.10479, 2026. https://arxiv.org/abs/2603.10479
4. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: heat equation, Laplacian comparison, non-explosion and diameter bounds*, Adv. Math. 356 (2019), 106759.
