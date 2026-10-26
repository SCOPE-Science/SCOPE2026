# Sharp Tjurina bound and a free extremizer for one-conic five-line ADE arrangements

## Finding
Consider all reduced plane curves over \(\mathbb C\) consisting of one smooth conic and five distinct lines, and having only simple ADE singularities. Their largest global Tjurina number is exactly
\[
\max_C\tau(C)=27.
\]
Equality occurs for the explicitly defined degree-seven arrangement
\[
C=V(f)\subset\mathbb P^2_{\mathbb C},\qquad
f=xyz(x+y)(x+z)\bigl(y^2+yz+z^2+xy+xz\bigr).
\]
Its singularity basket is \(2D_6+3D_4+3A_1\); moreover the logarithmic derivation module is free, with projective exponents \((3,3)\).

## Assumptions and scope
The global Tjurina number is \(\tau(C)=\sum_{p\in\operatorname{Sing}C}\dim_{\mathbb C}\mathcal O_{\mathbb P^2,p}/(f,f_u,f_v)\), with local affine coordinates at \(p\). Each component is geometrically reduced, every line is distinct, the conic is smooth, and all singularities are of ADE type. The claim does not range over two-conic arrangements, reducible conics, non-ADE singularities, or arbitrary septic curves. All statements are in characteristic zero.

## Proof
**Universal combinatorial estimate.** A singularity of a union of a smooth conic and distinct lines can involve at most three smooth local branches if it is ADE. By degree considerations and the ADE classification, the possibilities are a transverse node \(A_1\), a line tangent to the conic with contact two \(A_3\), three pairwise transverse smooth branches \(D_4\), and a tangent conic-line pair plus a transverse line \(D_6\). Write \(t\) for the number of lines tangent to the conic; \(e\) for the number of distinct line-pair intersection points that lie on the conic; and \(r\) for the number of off-conic ordinary triple intersections of lines. By Bézout, the baseline sum of pairwise local intersection multiplicities is \(\binom52+5\cdot2=20\). Relative to that baseline, the Tjurina excess of each \(A_3\) is one, each \(D_4\) is one, and each \(D_6\) is two (one tangency and one on-conic line crossing); therefore
\[
\tau(C)=20+t+e+r.
\]
Distinct triples of five line labels must share at most one label, so at most two ordinary line-only triple intersections exist: \(r\le2\). The five lines meet the conic in \(10-t\) distinct incidence slots counted before identifying different lines. Each on-conic pair consumes two such slots, hence \(e\le\lfloor(10-t)/2\rfloor\). If \(t=4\), only one line is secant; since distinct tangents never meet the conic at the same point, each on-conic line crossing must use the secant, so \(e\le2\). If \(t=5\), then \(e=0\). Checking \(t\in\{0,1,2,3,4,5\}\) yields \(t+e\le6\). Therefore \(\tau(C)\le20+6+2=28\). Merta and Zieliński (2026), Proposition 3.2, prove nonexistence of a *maximizing* one-conic five-line arrangement of degree seven with exactly the allowed ADE types, i.e. \(\tau=28\) is excluded. Consequently \(\tau(C)\le27\).

**Construction and exact singularity basket.** Put \(q=y^2+yz+z^2+xy+xz\). Its constant Hessian matrix is
\[
\begin{pmatrix}0&1&1\\1&2&1\\1&1&2\end{pmatrix},\qquad\det=-2,
\]
so \(V(q)\) is smooth. The lines are \(x=0\), \(y=0\), \(z=0\), \(x+y=0\), and \(x+z=0\). The points \([1:0:-1]\) and \([1:-1:0]\) are each a triple meeting of two lines and the conic; its conic tangent equals one of the two lines, with contact order exactly two, producing \(D_6\) at both points. The points \([0:0:1]\), \([0:1:0]\), and \([1:0:0]\) give \(D_4\) (the first two from three lines, the third from two lines and the conic with three distinct tangents). The point \([1:-1:-1]\), together with \([0:\omega:1]\) and \([0:\omega^2:1]\), where \(\omega^2+\omega+1=0\), gives three transverse nodes. For the two points with \(x=0\), the conic is transverse to that line because \(q(0,y,1)=y^2+y+1\) has two simple roots. No other intersections remain: the displayed two \(D_6\), three \(D_4\), and three \(A_1\) points use the entire Bézout pairwise multiplicity budget \(2\cdot4+3\cdot3+3\cdot1=20\). Thus the list is exhaustive, and
\[
\tau(C)=2\cdot6+3\cdot4+3=27.
\]

**Freeness.** There are two explicit degree-three Jacobian syzygies. With \(f_x,f_y,f_z\) denoting the partials, let
\[
\begin{aligned}
a_1&=x(y-z)(3x+8y+8z),\\
b_1&=-y(11xy+10xz+6y^2+7yz+8z^2),\\
c_1&=z(10xy+11xz+8y^2+7yz+6z^2),\\[2pt]
a_2&=-x(3x^2+7xy+4xz+4y^2+9yz-4z^2),\\
b_2&=y(4x^2+7xy+10xz+3y^2+5yz+4z^2),\\
c_2&=z(4x^2-4xz-4y^2-2yz-3z^2).
\end{aligned}
\]
An exact expansion over \(\mathbb Z[x,y,z]\) gives \(a_i f_x+b_i f_y+c_i f_z=0\) for both \(i=1,2\), and
\[
\det\begin{pmatrix}x&a_1&a_2\\y&b_1&b_2\\z&c_1&c_2\end{pmatrix}=-147f.
\]
The Euler derivation sends \(f\) to \(7f\). Thus the displayed determinant and logarithmic derivations satisfy Saito's freeness criterion, with syzygy exponents \((3,3)\). Their exact integer coefficients and identities are independently rechecked by the attached dependency-free `verify.py`.

## Verification
Run `python3 verify.py`. The program implements multivariate integer polynomial arithmetic directly, expands and checks both syzygy identities, checks the exact Saito determinant, and verifies the key point and incidence arithmetic; its successful result is `VERIFY_OK`. The numerical check verifies the explicit construction, not the cited 2026 universal nonexistence theorem. The latter is a separate published mathematical premise, checked against Proposition 3.2 of the source PDF.

## Relationship to prior work
Merta–Zieliński, *On the non-existence of certain maximizing curves of degree 7* (2026), Proposition 3.2, exclude \(\tau=28\) for one-conic five-line ADE arrangements; they neither give nor imply sharp attainability of \(27\), and their enumeration targets \(\tau=28\). Gałecka (2022) studies *nearly free* line-conic arrangements with only nodes, tacnodes and ordinary triple points, and exhibits a one-conic five-line degree-seven arrangement in that restricted class; the \(D_6\) singularities and free exponents here are outside its hypotheses. Dimca–Pokora (2021/2026) classify free line-conic arrangements under the same restricted list \(A_1,A_3,D_4\), excluding \(D_6\). The new contribution is the sharp maximum \(27\) in the specified broader ADE class and its explicit free witness. Absence from indexed searches is not a formal priority proof.

## Limitations
The result does not classify all extremizers or their projective equivalence classes. The upper-bound sharpness depends on the published nonexistence result for \(\tau=28\), while the lower bound and freeness have standalone exact certificates. A potentially unindexed earlier explicit example cannot be ruled out by literature searches. Independent human audit has not been performed.

## References
1. Ł. Merta and M. Zieliński, *On the non-existence of certain maximizing curves of degree 7*, arXiv:2610.16658v1 (first public 2026-10-12), Proposition 3.2 and Section 3, https://arxiv.org/abs/2610.16658.
2. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969v2 (2022), https://arxiv.org/abs/2204.13969.
3. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2111.12349v3 (originally 2021), https://arxiv.org/abs/2111.12349.
4. K. Saito, *Theory of logarithmic differential forms and logarithmic vector fields*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. 27 (1980), 265–291.
