# Sharp global quadratic projection stability of the regular tetrahedron

## Finding
Let \(\Delta=\operatorname{conv}\{e_1,e_2,e_3,e_4\}\) be the regular tetrahedron of edge length \(\sqrt2\), lying in the affine hyperplane \(\mathcal H=\{x\in\mathbb R^4:\sum_i x_i=1\}\). Let \(\mathcal H_0=\{u\in\mathbb R^4:\sum_i u_i=0\}\), and for any unit \(u\in\mathcal H_0\) let \(A(u)\) be the Euclidean area of the orthogonal projection of \(\Delta\) onto the affine two-plane in \(\mathcal H\) perpendicular to \(u\). Define the complete maximizing-normal orbit
\[
\mathcal E=\{(\epsilon_1,\epsilon_2,\epsilon_3,\epsilon_4)/2:\epsilon_i\in\{-1,1\},\ \sum_i\epsilon_i=0\}.
\]
Then \(\max_u A(u)=1\), and the **optimal global stability inequality** is
\[
\boxed{1-A(u)\ \ge\ \frac{3-\sqrt3}{8}\operatorname{dist}(u,\mathcal E)^2.}
\]
Here the distance is ambient Euclidean chord distance on the unit sphere of \(\mathcal H_0\). The constant is optimal, not merely a local asymptotic coefficient. Apart from the zero-deficit maximizing normals \(u\in\mathcal E\), equality holds **exactly** at the eight vertex-axis normals, namely signed permutations of \((3,-1,-1,-1)/\sqrt{12}\). In particular, the sharp global obstruction to strengthening the quadratic stability bound occurs at a triangular-shadow (vertex-axis) direction, not infinitesimally near a maximizing square-shadow direction.

## Assumptions and scope
The tetrahedron and the orthogonal projections use the standard Euclidean metric on the three-dimensional affine space \(\mathcal H\). Every projection direction is represented by a unit vector in \(\mathcal H_0\), with both signs admitted. The constant is sharp for this full direction space. No claim is made about higher-dimensional regular simplices or arbitrary tetrahedra.

## Proof
**Step 1: An independent projection-area formula.** Each facet of \(\Delta\) has area \(\sqrt3/2\), and its outward unit normal within \(\mathcal H\) is
\[
 n_i=-\frac{2}{\sqrt3}\left(e_i-\frac14(1,1,1,1)\right).
\]
Cauchy's elementary projection formula for a convex polytope gives projected area as one-half the sum over facets of facet area times the absolute normal component. Since \(u\cdot(1,1,1,1)=0\),
\[
 A(u)=\frac12\sum_{i=1}^4\frac{\sqrt3}{2}\left|u\cdot n_i\right|=\frac12\sum_{i=1}^4|u_i|.
\]
By Cauchy--Schwarz, \(\sum|u_i|\le2\), with equality precisely when all \(|u_i|=1/2\); the zero-sum constraint forces two plus and two minus signs. Thus the maximizing orbit is exactly \(\mathcal E\).

**Step 2: The exact distance parameter.** The inequality and orbit are invariant under coordinate permutations and \(u\mapsto-u\). We may therefore sort the coordinates and choose the sign so that
\[
 a\ge b\ge c\ge d,\qquad a+b+c+d=0,\qquad a^2+b^2+c^2+d^2=1,
\]
with at most two strictly positive coordinates. Pairing the two largest coordinates with the two positive entries of an element of \(\mathcal E\),
\[
 \max_{v\in\mathcal E}u\cdot v=a+b,
 \qquad \operatorname{dist}(u,\mathcal E)^2=2(1-a-b).
\]

**Step 3: Two-positive chamber.** When \(b\ge0\ge c\), the zero-sum condition gives \(A(u)=a+b\). Therefore
\[
 1-A(u)=1-a-b=\frac12\operatorname{dist}(u,\mathcal E)^2.
\]
This includes the boundary case \(b=0\). The coefficient \(1/2\) exceeds the claimed optimal constant.

**Step 4: One-positive chamber.** When \(a>0>b\) (or \(b=0\), already covered), the zero-sum condition instead gives \(A(u)=a\). Since \(b\) is the largest of the three nonpositive coordinates,
\[
 b\ge\frac{b+c+d}{3}=-\frac a3,
 \qquad a+b\ge\frac{2a}{3}.
\]
Cauchy--Schwarz on their sum yields
\[
 1=a^2+b^2+c^2+d^2\ge a^2+\frac{(b+c+d)^2}{3}=\frac{4a^2}{3},
 \qquad a\le\frac{\sqrt3}{2}.
\]
When \(u\notin\mathcal E\), all relevant denominators are strictly positive. Consequently,
\[
 \frac{1-A(u)}{\operatorname{dist}(u,\mathcal E)^2}
 =\frac{1-a}{2(1-a-b)}
 \ge\frac{1-a}{2(1-2a/3)}.
\]
The function \(f(t)=(1-t)/(2(1-2t/3))\) has derivative \(-1/[6(1-2t/3)^2]<0\) for \(0<t\le\sqrt3/2\). Hence the ratio is at least
\[
 f(\sqrt3/2)=\frac{3-\sqrt3}{8}.
\]
Equality throughout requires \(a=\sqrt3/2\) and \(b=c=d=-a/3\), which means \(u=(3,-1,-1,-1)/\sqrt{12}\) up to the stated symmetries. Conversely, substitution shows the exact equality there. All maximizing normals satisfy the deficit inequality with both sides zero. This proves the sharp coefficient and all equality cases.

## Verification
The independent finite-dimensional proof above is valid for every direction: it rests on the exact projection identity, an exhaustive split into sign chambers, and two elementary inequalities. The included dependency-free `verify.py` checks the proposed equality normal exactly to floating precision and searches 200,000 seeded random directions for a violation; this finite check is corroboration and is not used as proof. At the nontrivial equality normal the area ratio is \(\sqrt3/2\) and the squared distance to the maximizing orbit is \(2(1-1/\sqrt3)\); their quotient is \((3-\sqrt3)/8\).

## Relationship to prior work
Pandis, *On Extremal Volume Projections of the Simplex and the Cube* (arXiv:2601.18436, first public 2026-01-26), obtains the all-dimensional projection formula and identifies extrema. Jakimiuk and Pandis, *Stability of Hyperplane Projections of the Regular Simplex and \(L_p\)-Projection Bodies of balls in \(\ell_q^n(\mathbb R)\)* (arXiv:2610.23489, first public 2026-10-16), Theorem 1.1, establishes global quadratic stability for maximal simplex projections with coefficient \(1/[2(n+2)]\) when the simplex dimension is odd, and the optimal quadratic **exponent**. In dimension three its stated coefficient is \(1/10\). The theorem proved here gives the **best possible coefficient** \((3-\sqrt3)/8>1/10\) in precisely the same distance normalization, together with its entire equality set. The previously known area formula, maximizing normals and existence/order of stability are not claimed as new. Results on simplex *sections* use a different operation and do not by themselves determine this projection constant.

## Limitations
The exact coefficient is established for the three-dimensional regular tetrahedron, not for arbitrary dimension or general polyhedra. Originality is assessed from identified accessible primary texts and mathematical-record searches, not certified against every historical source. No independent mathematical audit has been performed. Finite numerical trials do not establish the theorem; the proof above does.

## References
1. J. Jakimiuk and C. Pandis, *Stability of Hyperplane Projections of the Regular Simplex and \(L_p\)-Projection Bodies of balls in \(\ell_q^n(\mathbb R)\)*, arXiv:2610.23489v1, 2026-10-16, §1.2 and §2. https://arxiv.org/html/2610.23489v1
2. C. Pandis, *On Extremal Volume Projections of the Simplex and the Cube*, arXiv:2601.18436v1, 2026-01-26, §1.1 and §3. https://arxiv.org/html/2601.18436v1
3. H. Martini and B. Weissbach, *On quermasses of simplices*, Studia Sci. Math. Hungar. 27 (1992), 213–221; historical antecedent cited in References 1–2.
