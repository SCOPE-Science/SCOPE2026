# Exact John ellipsoid of the Khachiyan half-cone
## Finding
For every integer \(n\ge 2\), define
\[
K_n=\{(t,y)\in\mathbb R\times\mathbb R^{n-1}:t\ge-1,\ t+\sqrt{n^2-1}\,\|y\|\le n\}
\]
and let \(K_n^-=K_n\cap\{t\le0\}\). The unique maximum-volume ellipsoid in \(K_n^-\) is
\[
E_n=-\frac12e_1+\operatorname{diag}\!\left(\frac12,\sqrt{\frac n{n-1}},\ldots,\sqrt{\frac n{n-1}}\right)B_2^n.
\]
Thus, if \(w(C)\) denotes the volume of the maximum-volume ellipsoid contained in a convex body \(C\), then
\[
\frac{w(K_n^-)}{w(K_n)}=\frac12\left(\frac n{n-1}\right)^{(n-1)/2}.
\]
The normalization \(J(K_n)=B_2^n\) is the one proved for this cone family in Zhou--Zou--Liu.

## Assumptions and scope
The statement concerns exactly the circular cone family above and the central cut \(t\le0\). It does not determine the best central-cut constant among all convex bodies in any fixed dimension. The ambient dimension satisfies \(n\ge2\).

Write \(q=\sqrt{n^2-1}\). The body \(K_n^-\) is invariant under every orthogonal transformation of the transverse variable \(y\in\mathbb R^{n-1}\). Maximum-volume inscribed ellipsoids are unique. Hence its John ellipsoid is invariant under the same transverse orthogonal group.

## Proof
By the transverse rotational symmetry and uniqueness, the maximizing ellipsoid has center \(ce_1\) and semiaxes \(a>0\) in the \(t\)-direction and \(b>0\) in every transverse direction. Put \(s=-c\). It therefore has the form
\[
\mathcal E(c,a,b)=ce_1+\operatorname{diag}(a,b,\ldots,b)B_2^n.
\]
The slab restrictions \(-1\le t\le0\) give
\[
0<s<1,\qquad a\le \min\{s,1-s\}.
\]
The cone inequality is equivalent to the family of linear inequalities
\[
t+q\,z\mathbin{\cdot}y\le n\qquad (z\in S^{n-2}).
\]
The support function of \(\mathcal E(c,a,b)\) in direction \((1,qz)\) is
\[
c+\sqrt{a^2+q^2b^2}.
\]
Consequently cone containment is equivalent to
\[
c+\sqrt{a^2+q^2b^2}\le n,
\]
or
\[
b^2\le\frac{(n+s)^2-a^2}{n^2-1}.
\]
For fixed \(s,a\), volume increases with \(b\), so equality holds at an optimum. Up to the constant \(\operatorname{vol}(B_2^n)\), the volume to maximize is
\[
G_s(a)=a\left(\frac{(n+s)^2-a^2}{n^2-1}\right)^{(n-1)/2}.
\]
Its logarithmic derivative is
\[
\frac{d}{da}\log G_s(a)=
\frac{(n+s)^2-na^2}{a((n+s)^2-a^2)}.
\]
Since \(0<a\le\min\{s,1-s\}\le1/2\) and \(n\ge2\), the numerator is strictly positive. Therefore
\[
a=\min\{s,1-s\}.
\]
For \(0<s\le1/2\), substituting \(a=s\) gives
\[
b^2=\frac{n(n+2s)}{(n-1)(n+1)}
\]
and
\[
\frac{d}{ds}\log\!\left[s\,b^{n-1}\right]
=\frac{ns+n+s}{s(n+2s)}>0.
\]
Thus the optimal volume is strictly increasing on this branch. For \(1/2\le s<1\), substituting \(a=1-s\) gives
\[
b^2=\frac{n-1+2s}{n-1}
\]
and
\[
\frac{d}{ds}\log\!\left[(1-s)b^{n-1}\right]
=-\frac{s(n+1)}{(1-s)(n-1+2s)}<0.
\]
Thus the optimal volume is strictly decreasing on this branch. The unique global maximum occurs at \(s=1/2\). There
\[
c=-\frac12,\qquad a=\frac12,\qquad b^2=\frac n{n-1},
\]
which is exactly \(E_n\). Its volume relative to \(B_2^n\) is the product of its semiaxes,
\[
\frac{\operatorname{vol}(E_n)}{\operatorname{vol}(B_2^n)}
=\frac12\left(\frac n{n-1}\right)^{(n-1)/2}.
\]
Zhou--Zou--Liu prove \(J(K_n)=B_2^n\), so \(w(K_n)=\operatorname{vol}(B_2^n)\). The displayed equality follows.

## Verification
The proof reduces the full ellipsoid optimization to three scalar variables using a symmetry that the unique optimizer must inherit. All containment inequalities are then exact support-function inequalities. The two one-variable branches have derivatives of fixed, strict sign, so there is no unexamined stationary point or numerical step. Substitution at \(s=1/2\) reproduces exactly the ellipsoid displayed in the source's sharpness construction.

## Relationship to prior work
Zhou--Zou--Liu introduce the same cone \(K_n\) and ellipsoid \(E_n\), prove \(J(K_n)=B_2^n\) and \(E_n\subset K_n^-\), and use its volume only as a lower bound tending to \(\sqrt e/2\). Their Section 4 explicitly says that no maximality assertion about \(E_n\) inside the half-cone is needed, while Section 7.4 says the best constant in each prescribed dimension remains undetermined. The result here identifies the exact John ellipsoid of their canonical half-cone, without claiming that this cone is extremal among all bodies in its dimension.

Güler--Gürtuna develop symmetry methods for extremal ellipsoids and treat truncated second-order cones on the covering side; their introduction explicitly states that they do not solve the inscribed-ellipsoid problem for that second class. Their general symmetry principle is consistent with, but does not state, the exact formula above.

The earlier Khachiyan and Tarasov--Khachiyan--Erlikh literature is credited by Zhou--Zou--Liu with the cone example and its limiting \(\sqrt e/2\) ratio. The present claim is narrower than the open fixed-dimensional extremal problem and stronger than the feasibility statement used in the recent sharpness proof.

## Limitations
This result determines the maximum-volume ellipsoid only for the specific retained half-cone \(K_n^-\). It does not prove that
\[
\frac12\left(\frac n{n-1}\right)^{(n-1)/2}
\]
is the optimal central-cut ratio over all \(n\)-dimensional convex bodies. The original 1988 Russian paper of Tarasov--Khachiyan--Erlikh and the early Khachiyan literature were not independently checked line by line here; the comparison relies in part on the detailed historical account in the 2026 source, so a residual bibliographic risk remains.

## References
1. Zhou Longfei, Haijun Zou, Tianhao Liu, “A Spectral Proof of Khachiyan's Ellipsoid Conjecture,” arXiv:2609.28447v1, 23 September 2026, especially Sections 4, 5.1, and 7.4.
2. Osman Güler, Filiz Gürtuna, “The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases,” arXiv:0709.0707v1, 5 September 2007.
3. S. P. Tarasov, L. G. Khachiyan, I. I. Erlikh, “The method of inscribed ellipsoids,” Doklady Akademii Nauk SSSR 298(5) (1988), 1081–1085; English translation Soviet Mathematics Doklady 37 (1988), 226–230.
