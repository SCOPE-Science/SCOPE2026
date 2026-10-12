# Projective stabilizer of Czarnota's Configuration B

## Finding
Let
\[
A=V(Q_6)\subset\mathbb P^2_{\mathbb C},
\qquad
Q_6=x(x-z)(x+z)(y-z)(y+z)(x^2+y^2-z^2),
\]
be Configuration B from Czarnota's *On maximizing curves of degree 7*. Then the full projective stabilizer of the reduced arrangement is
\[
\operatorname{Aut}_{\mathbb P^2}(A)
=
\left\{[x:y:z]\longmapsto[\varepsilon x:\delta y:z]
:\ \varepsilon,\delta\in\{\pm1\}\right\}
\cong C_2\times C_2.
\]
In particular, the secant line \(x=0\) is fixed, the involution changing the sign of \(x\) exchanges the two tangent lines \(x=z\) and \(x=-z\), and the involution changing the sign of \(y\) exchanges \(y=z\) and \(y=-z\). There is no projective automorphism exchanging these two tangent-line pairs.

## Assumptions and scope
The ground field is \(\mathbb C\). The arrangement is the specific reduced degree-seven curve displayed above. Its unique nonlinear irreducible component is the smooth conic
\[
K:x^2+y^2-z^2=0.
\]
The five line components are
\[
L_0:x=0,
\qquad
L_{x,+}:x=z,
\qquad
L_{x,-}:x=-z,
\qquad
L_{y,+}:y=z,
\qquad
L_{y,-}:y=-z.
\]
The claim concerns projective automorphisms of this embedded reduced curve, not abstract automorphisms of its normalization or of its incidence graph.

## Proof
Because \(K\) is the unique irreducible component of degree two, every projective automorphism of \(A\) preserves \(K\). Intersecting the five line components with \(K\) gives
\[
K\cap L_0=V(x,y^2-z^2),
\]
which consists of two distinct points, whereas
\[
K|_{x=z}=y^2,
\quad
K|_{x=-z}=y^2,
\quad
K|_{y=z}=x^2,
\quad
K|_{y=-z}=x^2.
\]
Thus \(L_0\) is the unique secant line among the five line components, and the other four are tangent to \(K\). Hence every projective automorphism of \(A\) fixes \(L_0\), preserves its unordered intersection pair with \(K\), and permutes the four tangency points
\[
P_1=[1:0:1],
\quad
P_2=[-1:0:1],
\quad
P_3=[0:1:1],
\quad
P_4=[0:-1:1].
\]
Moreover,
\[
K\cap L_0=\{P_3,P_4\}.
\]

Parametrize the conic by
\[
\nu(t)=[2t:1-t^2:1+t^2],
\qquad t\in\mathbb P^1.
\]
Then
\[
P_3=\nu(0),
\qquad
P_4=\nu(\infty),
\qquad
P_1=\nu(1),
\qquad
P_2=\nu(-1).
\]
Therefore the restriction to \(K\) of any projective stabilizer element is a Möbius transformation preserving both
\[
\{0,\infty\}
\quad\text{and}\quad
\{1,-1\}.
\]
A Möbius transformation preserving \(\{0,\infty\}\) setwise has one of the two forms
\[
t\longmapsto at
\qquad\text{or}\qquad
t\longmapsto \frac{a}{t}
\]
with \(a\ne0\). Preservation of \(\{1,-1\}\) forces \(a=\pm1\). Thus the induced transformation on \(K\) is one of
\[
t,
\quad -t,
\quad t^{-1},
\quad -t^{-1}.
\]
Restriction from the projective stabilizer of a smooth plane conic to the conic is injective: a projective transformation acting trivially on \(K\) fixes more than four points in general position and is therefore the identity. Hence \(\operatorname{Aut}_{\mathbb P^2}(A)\) has at most four elements.

All four possibilities occur. The transformations
\[
[x:y:z]\mapsto[-x:y:z]
\qquad\text{and}\qquad
[x:y:z]\mapsto[x:-y:z]
\]
preserve \(K\), preserve \(L_0\), and exchange respectively the two \(x\)-tangents and the two \(y\)-tangents. Together with their product and the identity they form a Klein four group. Under \(\nu\), their restrictions are respectively \(-t\), \(t^{-1}\), and \(-t^{-1}\). This realizes all four possibilities found above and proves the claim.

## Verification
The accompanying `verify.py` performs exact symbolic checks. It verifies that all four diagonal sign maps preserve \(Q_6\) up to a nonzero scalar; checks the secant-versus-tangent restrictions of \(K\); verifies the conic parametrization and the induced maps \(t\mapsto-t\), \(t\mapsto t^{-1}\), and \(t\mapsto-t^{-1}\); and checks the final equation \(a^2=1\) governing the two Möbius branches. Running the script returns

`VERIFY_OK group_order=4 group=C2xC2 restrictions=t,-t,1/t,-1/t`.

The upper bound of four elements is a proof from the conic restriction and is not inferred from finite sampling.

## Relationship to prior work
Czarnota introduces Configuration B with exactly the displayed equation and proves that it is a free conic-line arrangement with five \(A_1\) singularities, two \(A_3\) singularities, one \(D_4\) singularity, two \(D_6\) singularities, total Tjurina number \(27\), and \(\operatorname{mdr}=3\). The surrounding text identifies Configurations A, B, and C as constructions found during preparation of that work. The inspected article contains no occurrence of “automorphism”, “symmetry”, or “stabilizer”, and does not determine the projective isotropy of Configuration B.

Exact-equation and Configuration-B searches for projective automorphisms found no source stating this Klein-four stabilizer. The closest indexed stabilizer results concern different conic-line arrangements or different geometric objects and do not imply the present claim.

## Limitations
The result is specific to the displayed complex projective arrangement. It does not classify all one-conic five-line arrangements with the same weak singularity counts, nor does it claim that the weak combinatorics determine the stabilizer. An older or poorly indexed computation in equivalent coordinates could contain the same stabilizer without using the name Configuration B; exact-equation and alias searches did not locate such a source.

## References
1. I. Czarnota, *On maximizing curves of degree 7*, arXiv:2401.14721v1, first posted 2024-01-26; Ann. Univ. Ferrara 70 (2024), 1479–1489; DOI:10.1007/s11565-024-00523-7. See Section 4, especially Example 4.7.
