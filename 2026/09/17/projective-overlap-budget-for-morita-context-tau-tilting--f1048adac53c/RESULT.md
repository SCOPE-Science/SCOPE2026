# Projective-overlap budget for direct support tau-tilting induction

## Statement

Let
\[
\Lambda=\begin{pmatrix}A&N\\ M&B\end{pmatrix}_{\phi,\psi}
\]
be a finite-dimensional Morita context algebra over a field \(k\), with diagonal idempotents \(e,f\), and let
\[
F_A=-\otimes_A e\Lambda,\qquad F_B=-\otimes_B f\Lambda.
\]
Write \(\operatorname{iproj}C\) for the set of isomorphism classes of indecomposable projective right \(C\)-modules and \(|C|=|\operatorname{iproj}C|\).

Because \(F_A,F_B\) are fully faithful and preserve projectives, they induce injections
\[
\iota_A:\operatorname{iproj}A\hookrightarrow\operatorname{iproj}\Lambda,
\qquad
\iota_B:\operatorname{iproj}B\hookrightarrow\operatorname{iproj}\Lambda.
\]
Define the **projective-overlap number**
\[
\omega(\Lambda;e,f)
=
|\operatorname{im}\iota_A\cap\operatorname{im}\iota_B|.
\]

### Theorem A: overlap and the radical condition

Every indecomposable projective \(\Lambda\)-module is induced from at least one corner, and
\[
\boxed{\omega(\Lambda;e,f)=|A|+|B|-|\Lambda|.}
\]
If
\[
S=\Lambda/J(\Lambda)=\prod_i S_i
\]
is the Wedderburn decomposition, then \(\omega(\Lambda;e,f)\) is exactly the number of simple factors \(S_i\) for which both \(eS_i\neq0\) and \(fS_i\neq0\).

Consequently,
\[
\boxed{\omega(\Lambda;e,f)=0
\iff
\operatorname{Im}\phi\subseteq J(A),\quad
\operatorname{Im}\psi\subseteq J(B).}
\]
Thus the radical condition used in Zhang's direct-induction converse is precisely the zero-overlap case.

### Theorem B: an exact overlap budget for arbitrary connecting maps

Let \(X\in\operatorname{mod}A\) and \(Y\in\operatorname{mod}B\) be basic, and set
\[
Z=(F_AX\oplus F_BY)^{\mathrm{basic}}.
\]
Assume first that \(Z\) is \(\tau\)-rigid. Define
\[
\mathcal Q_X=\{[Q]\in\operatorname{iproj}A:\operatorname{Hom}_A(Q,X)=0\},
\]
and let
\[
\mathcal R_X=\{[Q]\in\mathcal Q_X:
\operatorname{Hom}_A(Q,Y\otimes_BM)=0\}.
\]
Define \(\mathcal Q_Y,\mathcal R_Y\) symmetrically, with \(X\otimes_AN\). Put
\[
q_X=|\mathcal Q_X|,\quad r_X=|\mathcal R_X|,
\qquad
q_Y=|\mathcal Q_Y|,\quad r_Y=|\mathcal R_Y|.
\]
Set the corner defects
\[
\delta_X=|A|-|X|-q_X,\qquad
\delta_Y=|B|-|Y|-q_Y,
\]
and the cross-blocking counts
\[
\beta_X=q_X-r_X,\qquad \beta_Y=q_Y-r_Y.
\]
Finally define
\[
d_Z=
|\operatorname{ind}(F_AX)\cap\operatorname{ind}(F_BY)|
\]
and
\[
d_P=
|\iota_A(\mathcal R_X)\cap\iota_B(\mathcal R_Y)|.
\]
All six quantities
\[
\delta_X,\delta_Y,\beta_X,\beta_Y,d_Z,d_P
\]
are nonnegative integers. Then
\[
\boxed{
\Delta(X,Y):=
\delta_X+\delta_Y+\beta_X+\beta_Y+d_Z+d_P
\ge \omega(\Lambda;e,f),
}
\]
and equality holds if and only if \(Z\) is support \(\tau\)-tilting.

Combining this with Zhang's condition-free \(\tau\)-rigidity test gives a complete direct-induction criterion for arbitrary connecting maps:

\[
\boxed{
F_AX\oplus F_BY\text{ is support }\tau\text{-tilting}
}
\]
if and only if
\[
X,Y\text{ are }\tau\text{-rigid},
\]
\[
\operatorname{Hom}_A(Y\otimes_BM,\tau_AX)=0,\qquad
\operatorname{Hom}_B(X\otimes_AN,\tau_BY)=0,
\]
and
\[
\Delta(X,Y)=\omega(\Lambda;e,f).
\]

## Proof

### 1. Projective overlap

As right \(\Lambda\)-modules,
\[
\Lambda=e\Lambda\oplus f\Lambda=F_AA\oplus F_BB.
\]
Since the induction functors are fully faithful, they preserve indecomposability and distinguish nonisomorphic indecomposable projectives within each corner. By Krull--Schmidt, every indecomposable projective summand of the regular module \(\Lambda\) therefore lies in the image of \(\iota_A\) or \(\iota_B\). Inclusion--exclusion gives
\[
|\Lambda|
=
|\operatorname{im}\iota_A\cup\operatorname{im}\iota_B|
=
|A|+|B|-\omega,
\]
proving the first formula.

Let \(S=\Lambda/J(\Lambda)\). For an idempotent \(g\), \(J(g\Lambda g)=gJ(\Lambda)g\), hence
\[
A/J(A)\cong eSe,\qquad B/J(B)\cong fSf.
\]
In a simple Artinian factor \(S_i\), the corner \(eS_ie\) is nonzero precisely when \(eS_i\neq0\), and similarly for \(f\). There is one simple-module, equivalently one indecomposable-projective, isomorphism class associated with \(S_i\). Hence the same class occurs in both induced corner families exactly when both \(eS_i\) and \(fS_i\) are nonzero. This proves the Wedderburn-block interpretation of \(\omega\).

Modulo \(J(\Lambda)\), the image of \(NM=\operatorname{Im}\phi\) is \(eSfSe\), while the image of \(MN=\operatorname{Im}\psi\) is \(fSeSf\). In a simple Artinian block \(S_i\), if both \(e_i\) and \(f_i\) are nonzero then
\[
S_if_iS_i=S_i,
\]
so
\[
e_iS_if_iS_ie_i=e_iS_ie_i\neq0.
\]
If one of \(e_i,f_i\) is zero, this product is zero. Therefore both connecting-map images are radical-valued exactly when there is no mixed Wedderburn block, i.e. exactly when \(\omega=0\).

### 2. The numerical budget

Since \(Z\) is \(\tau\)-rigid, Zhang's Lemma 5.4 implies that \(X\) and \(Y\) are \(\tau\)-rigid. The pairs
\[
(X,Q_X),\qquad (Y,Q_Y),
\]
where \(Q_X,Q_Y\) are the basic sums represented by \(\mathcal Q_X,\mathcal Q_Y\), are therefore \(\tau\)-rigid pairs. The standard summand bound gives
\[
|X|+q_X\le |A|,\qquad |Y|+q_Y\le |B|,
\]
so \(\delta_X,\delta_Y\ge0\).

Adjunction gives, for an indecomposable projective \(A\)-module \(Q\),
\[
\operatorname{Hom}_\Lambda(F_AQ,Z)
\cong
\operatorname{Hom}_A\!\left(Q,X\oplus(Y\otimes_BM)\right).
\]
Thus the \(A\)-induced indecomposable projectives orthogonal to \(Z\) are exactly the classes \(\iota_A(\mathcal R_X)\); similarly the \(B\)-induced ones are \(\iota_B(\mathcal R_Y)\). Since every indecomposable projective \(\Lambda\)-module comes from at least one corner, the basic sum \(P^\perp_Z\) of all indecomposable projectives orthogonal to \(Z\) has
\[
|P^\perp_Z|=r_X+r_Y-d_P.
\]
Also,
\[
|Z|=|X|+|Y|-d_Z.
\]
Hence
\[
\begin{aligned}
|Z|+|P^\perp_Z|
&=|X|+|Y|+r_X+r_Y-d_Z-d_P\\
&=|A|+|B|-\Delta(X,Y).
\end{aligned}
\]
The pair \((Z,P^\perp_Z)\) is \(\tau\)-rigid, so
\[
|Z|+|P^\perp_Z|\le |\Lambda|
=|A|+|B|-\omega.
\]
Therefore \(\Delta(X,Y)\ge\omega\).

If equality holds, then
\[
|Z|+|P^\perp_Z|=|\Lambda|,
\]
so \((Z,P^\perp_Z)\) is a support \(\tau\)-tilting pair by definition. Conversely, if \(Z\) is support \(\tau\)-tilting, its projective complement contains every indecomposable projective orthogonal to \(Z\): otherwise one could add another such projective and violate the \(\tau\)-rigid-pair summand bound. Thus its projective complement is exactly \(P^\perp_Z\), and equality follows.

The final criterion now follows by adjoining Zhang's arbitrary-connecting-map characterization of \(\tau\)-rigidity.

## Recovery of the radical-valued converse

Under the radical condition, Theorem A gives \(\omega=0\). If direct induction is support \(\tau\)-tilting, Theorem B forces
\[
\delta_X=\delta_Y=\beta_X=\beta_Y=d_Z=d_P=0.
\]
The equalities \(\delta_X=\delta_Y=0\) say that \(X\) and \(Y\) are support \(\tau\)-tilting. The equalities \(\beta_X=\beta_Y=0\), together with the two cross-\(\tau\) Hom vanishings from the \(\tau\)-rigidity test, give
\[
Y\otimes_BM\in\operatorname{Fac}_AX,\qquad
X\otimes_AN\in\operatorname{Fac}_BY
\]
by the standard support-\(\tau\)-tilting torsion-class criterion. Thus Zhang's Theorem 5.2 converse is exactly the zero-budget case of the condition-free formula.

## Sharp non-radical example

Take the strict context
\[
A=B=M=N=k,\qquad \Lambda=M_2(k),
\]
with \(X=k\) and \(Y=0\). Then
\[
\omega=1.
\]
The module \(F_AX=e\Lambda\) is the unique indecomposable projective \(\Lambda\)-module up to isomorphism, hence is \(\tau\)-tilting. Here
\[
\delta_X=\delta_Y=\beta_X=d_Z=d_P=0,\qquad \beta_Y=1,
\]
so
\[
\Delta=1=\omega.
\]
This identifies the failure in Zhang's counterexample exactly: the single unit of projective overlap is spent on one blocked \(B\)-corner projective.

More generally, the direct product of \(c\) copies of this strict context has \(\omega=c\); with \(X=A\) and \(Y=0\), one gets \(\beta_Y=c\) and all other defect terms zero. Hence the budget is sharp for every \(c\ge1\).

## Relation to the literature

Zhang's preprint, submitted 16 September 2026, proves the direct-induction converse under the radical condition and explicitly states that this hypothesis is used in the summand count; it also gives the \(M_2(k)\) counterexample when the condition is removed. The same paper proves the \(\tau\)-rigidity test for arbitrary connecting maps. The present result replaces the failed summand count by an exact overlap budget and thereby gives a condition-free numerical characterization.

The \(\tau\)-rigid-pair summand bound and the support-\(\tau\)-tilting torsion criterion are standard results of Adachi--Iyama--Reiten. Jacobson-radical formulas for Morita contexts are classical; no novelty is claimed for those ingredients individually.

Sources inspected:
- Yingying Zhang, *Support \(\tau\)-tilting modules over Morita context algebras: A bilateral approximation approach*, arXiv:2609.18746v1: https://arxiv.org/abs/2609.18746
- T. Adachi, O. Iyama, I. Reiten, *\(\tau\)-tilting theory*, Compositio Math. 150 (2014), arXiv:1210.1036: https://arxiv.org/abs/1210.1036
- D. Asefa, Q. Xu, *Silting modules over a class of Morita rings*, Open Mathematics 22 (2024), DOI 10.1515/math-2024-0009: https://doi.org/10.1515/math-2024-0009
- E. L. Green, C. Psaroudakis, *On Artin algebras arising from Morita contexts*, Algebras and Representation Theory 17 (2014), arXiv:1303.2083: https://arxiv.org/abs/1303.2083

## Originality and limitations

To the best of our knowledge, the exact six-term overlap budget and the resulting arbitrary-connecting-map support-\(\tau\)-tilting criterion do not appear in the literature located for this review. Targeted searches for Morita-context support-\(\tau\)-tilting projective overlap, direct-induction overlap criteria, and projective-complement defects returned Zhang's recent paper and older zero-product/triangular special cases, but no matching formula.

The structural interpretation of \(\omega\) uses standard semisimple-ring and Morita-context facts and is not claimed as an independent historical first. A. D. Sands, *Radicals and Morita contexts*, J. Algebra 24 (1973), 335--345, DOI 10.1016/0021-8693(73)90143-9, was identified as a classical source but its full text was not inspected. It could contain an equivalent structural observation about radical-valued pairings, though it predates \(\tau\)-tilting theory and cannot contain the budget criterion in its present form.

The criterion is exact but not automatically algorithmic: computing \(d_Z\) and \(d_P\) can require recognizing cross-corner isomorphisms. Because Zhang's preprint is extremely recent, a concurrent revision or independent observation is also possible.
