# Exact rank stratification of a genus-five generalized Howe family in characteristic eleven

## Finding

Let \(k=\overline{\mathbb F}_{11}\). For parameters \((u,v)\) in the open set
\[
U=\{(u,v)\in k^2:\ uv(u^2-4)(v^2-4)(u-v)\ne0\},
\]
let \(C_{u,v}\) be the smooth projective normalization of the fiber product over the \(x\)-line of
\[
D_u:\quad y_1^2=(x^4-1)(x^2-ux+1),\qquad
D_v:\quad y_2^2=(x^4-1)(x^2-vx+1).
\]
Define \(H(u,v)=[x^{10}]((x^2-ux+1)(x^2-vx+1))^5\), with coefficients reduced modulo eleven. Put \(\epsilon(w)=1\) for \(w\in\{5,6\}\subset\mathbb F_{11}\) and \(\epsilon(w)=0\) otherwise. Then every smooth geometric fiber has genus five and
\[
f_{11}(C_{u,v})=5-2\epsilon(u)-2\epsilon(v)-\mathbf1_{H(u,v)=0},\qquad
a(C_{u,v})=5-f_{11}(C_{u,v}).
\]
All five ranks \(1,2,3,4,5\) occur, and rank zero does not occur in this family. The rank-one locus consists of precisely the two reduced coefficient-marked points \((5,6)\) and \((6,5)\). The rank-two locus consists of exactly sixteen reduced geometric points, all transverse intersections of the elliptic Hasse curve \(V(H)\) with one of the four lines \(u=5\), \(u=6\), \(v=5\), \(v=6\). Eight rank-two parameters are rational over \(\mathbb F_{11}\), and the other eight form four Frobenius pairs over \(\mathbb F_{121}\). The corresponding transverse intersection scheme of the reduced special lines with \(V(H)\) is finite étale of degree sixteen over \(\mathbb F_{11}\); no claim about a nonreduced determinantal scheme structure is made. These assertions count ordered coefficient pairs, not isomorphism classes of genus-five curves.

## Assumptions and scope

All calculations concern characteristic eleven and geometric parameters in \(U\); excluded parameters correspond to repeated branch points or coincident covers, and their normalized fiber products are not part of this theorem. The \(11\)-rank \(f_{11}(C)\) is the dimension of the maximal étale summand of the \(11\)-torsion of the Jacobian, and \(a(C)\) is its \(a\)-number \(\dim_k\operatorname{Hom}(\alpha_{11},J(C)[11])\). The bracket \([x^{10}]\) means coefficient extraction before reduction modulo eleven.

## Proof

### Geometry and the three quotient Jacobians

The four roots of \(x^4-1\) are distinct in characteristic eleven. The quadratic \(Q_u=x^2-ux+1\) has distinct roots and meets this four-point set nowhere exactly when \(u\ne0,\pm2\). Under \(u\ne v\), the two quadratic factors also have no common root. Thus \(D_u\) and \(D_v\) are smooth genus-two double covers sharing precisely four of their six branch points. The Riemann–Hurwitz formula for their \(V_4\)-fiber product gives \(g(C_{u,v})=2(2+2)+1-4=5\). The standard generalized Howe isogeny of Katsura–Takashima, also obtainable from the three nontrivial involution quotients, gives a separable isogeny of \(2\)-power degree
\[
J(C_{u,v})\longrightarrow J(D_u)\times J(D_v)\times E_{u,v},
\qquad E_{u,v}:z^2=Q_uQ_v.
\]
As the isogeny degree is prime to eleven, it identifies the relevant \(11\)-divisible groups; both \(11\)-rank and \(a\)-number are additive across the three factors.

### The genus-two Cartier calculation

For \(D_w:y^2=F_w(x)\) with \(F_w=(x^4-1)(x^2-wx+1)\), take the differential basis \(dx/y\), \(x\,dx/y\). The Cartier–Manin coefficient matrix, with \((i,j)\)-entry \([x^{11i-j}]F_w(x)^5\) for \(1\le i,j\le2\), is
\[
M(w)=\begin{pmatrix}
3w^4-5w^2-1&-5w^5-w^3+4w\\
5w^5+w^3-4w&-3w^4+5w^2+1
\end{pmatrix}
=(w^2-3)\begin{pmatrix}
3w^2+4&w(-5w^2+6)\\
-w(-5w^2+6)&-3w^2-4
\end{pmatrix}.
\]
These identities and all following coefficient identities are in characteristic eleven. Direct expansion yields
\[
\det M(w)=3(w^2-3)^2(w^2-4)^3.
\]
Because \(w^2-4\ne0\) on \(U\), the Cartier map on each genus-two factor is invertible unless \(w^2=3\). The two roots of \(w^2=3\) in \(\mathbb F_{11}\) are \(5,6\), and at either root the entire matrix vanishes. Thus each \(J(D_w)\) is ordinary with rank two and \(a\)-number zero, or superspecial with rank zero and \(a\)-number two, according as \(\epsilon(w)=0\) or \(1\). For the elliptic quotient \(E_{u,v}\), its Hasse coefficient is \(H(u,v)\); this quotient has rank one and \(a\)-number zero if \(H\ne0\), or rank zero and \(a\)-number one if \(H=0\). Additivity proves the stated rank and \(a\)-number formulas, including the semilinear stable-rank assertion: the only genus-two Cartier blocks encountered are invertible or zero, and the elliptic block is one-dimensional.

### Complete exceptional zero-dimensional strata

The elliptic Hasse polynomial is symmetric in \(u,v\). Exact coefficient extraction and factorization yield
\[
\begin{aligned}
H(5,v)&=-2(v-4)(v-3)(v^2+4v+2),\\
H(6,v)&=-2(v+3)(v+4)(v^2-4v+2).
\end{aligned}
\]
Both quadratics have discriminant \(8\ne0\). Each of these quartics has four pairwise distinct roots, none in the excluded values \(0,2,9\), none equal to the fixed parameter, and none in \(\{5,6\}\). Consequently, the four exceptional lines \(u\in\{5,6\}\) and \(v\in\{5,6\}\) meet \(V(H)\cap U\) in sixteen distinct points, and at each intersection the derivative of the relevant one-variable quartic is nonzero. These are reduced transverse intersections. The linear roots on each of the four special lines are in \(\mathbb F_{11}\), giving eight rational points. Each quadratic has nonsquare discriminant \(8\) in \(\mathbb F_{11}\), hence defines one Frobenius-conjugate pair over \(\mathbb F_{121}\) on each special line, giving four pairs. This proves the field-of-definition and finite-étale assertions.

For rank two, exactly one genus-two factor must be superspecial and the elliptic quotient must be supersingular, so these sixteen intersections are exhaustive. For rank one, both genus-two factors must be superspecial and the elliptic quotient must be ordinary: distinctness of parameters leaves only \((5,6)\) and \((6,5)\), and coefficient extraction gives \(H(5,6)=4\ne0\). The rank-zero condition would force both exceptional parameters and \(H=0\), which is impossible. The following admissible rational-parameter witnesses have ranks \(1,2,3,4,5\), respectively:
\[
(5,6),\quad(5,3),\quad(5,1),\quad(1,3),\quad(1,8).
\]
This also proves that every asserted rank occurs.

## Verification

Run `python3 verify_symbolic.py` using SymPy and `python3 verify_fields.py` using only the Python standard library. The first script checks every displayed characteristic-eleven matrix and factorization, the sixteen simple intersections, and the rank witnesses. The second reconstructs the quotient Cartier coefficients independently by direct arithmetic in \(\mathbb F_{121}\), exhausting all \(13{,}806\) admissible ordered parameter pairs. It reports exactly two rank-one and sixteen rank-two pairs over this field. These finite enumerations are checks, not substitutes for the geometric proof and separable-isogeny argument.

## Relationship to prior work

Katsura and Takashima (first public in 2021) established the generalized Howe framework and its decomposed Richelot isogeny. Moriya and Kudo (2023) constructed plane-sextic models for the same genus-five quotient type. Kawakita (2024) gave a five-elliptic-factor decomposition under related genus-five Howe hypotheses and a characteristic-eleven maximal-curve example in the larger family; that example does not imply rank zero for this restricted two-parameter subfamily. Ohashi (2026) studies a Möbius-equivalent symmetric genus-five generalized Howe family, its completely decomposable Jacobians, and superspecial parameters. Explicitly, after adjoining \(i\) with \(i^2=-1\), the substitution \(z=-i(x-1)/(x+1)\) maps the common roots of \(x^4-1\) to \(0,\infty,1,-1\), and the roots of \(Q_w\) to \(\pm s\) with \(s^2=(2-w)/(2+w)\). In particular, the existence of this family, the quotient-isogeny mechanism, and the genus-two superspecial parameter condition are **not** claimed as new. The result assessed here is the complete characteristic-eleven \(11\)-rank/\(a\)-number stratification together with the exact reduced sixteen-point rank-two incidence scheme and two-point rank-one locus. The field-specific intersection calculation is not among the identified statements in these primary papers.

## Limitations

This classification is confined to the ordered two-dimensional family on \(U\); it does not classify all genus-five curves, geometric isomorphism classes, or degeneration fibers outside \(U\). The irreducible decomposition of the entire elliptic Hasse curve \(V(H)\) is not asserted. The two ordered rank-one parameters are exchanged by swapping the two genus-two covers. The study has not received independent external mathematical validation. Prior results on the equivalent parameter family make a previously published equivalent specialization a residual priority risk.

## References

1. T. Katsura and K. Takashima, *Decomposed Richelot isogenies of Jacobian varieties of hyperelliptic curves and generalized Howe curves*, arXiv:2108.06936 (initially published 2021-08-16), https://arxiv.org/abs/2108.06936 .
2. T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993 (initially published 2023-10-24), https://arxiv.org/abs/2310.15993 .
3. M. Q. Kawakita, *Generalised Howe curves of genus five attaining the Serre bound*, arXiv:2412.03071 (2024-12-04), https://arxiv.org/abs/2412.03071 .
4. R. Ohashi, *Superspecial generalized Howe curves of genus 4, 5, and 6 with completely decomposable Jacobians*, arXiv:2604.18074 (2026-04-20), https://arxiv.org/abs/2604.18074 .
