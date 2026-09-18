# A 2-adic symmetry-phase dichotomy for Chair44 tilings

## Statement

Let \(Q\) be Tsiokos's Chair44 monotile, and let \(T\) be a registered tiling of \(\mathbb R^3\) by congruent copies of \(Q\). The unique hierarchy proved for Chair44 assigns, for every \(n\ge 1\), a unique coset
\[
\alpha_n(T)+2^n\mathbb Z^3
\]
containing the level-\(n\) parent anchors, with
\[
\alpha_{n+1}(T)\equiv \alpha_n(T)\pmod{2^n}.
\]
Write
\[
\alpha(T)=(\alpha_n(T))_{n\ge1}\in \mathbb Z_2^3
\]
for the resulting coherent 2-adic hierarchy phase. Let \(\mathcal O\le SO(3,\mathbb Z)\) be the proper cubic rotation group, of order \(24\).

For \(a\in\mathbb Z_2^3\), define the **phase-compatible point group**
\[
P_a:=\{R\in\mathcal O:(I-R)a\in\mathbb Z^3\}.
\]
Then:

1. \(P_a\) is a subgroup of \(\mathcal O\).
2. If \(g(x)=Rx+t\) is a Euclidean symmetry of \(T\), then \(R\in\mathcal O\), \(t\in\mathbb Z^3\), and
   \[
   (I-R)\alpha(T)=t\qquad\text{in }\mathbb Z_2^3.
   \]
   Consequently the linear-part map embeds \(\operatorname{Sym}(T)\) into \(P_{\alpha(T)}\).
3. For every nonidentity \(R\in\mathcal O\), the compatible phase set
   \[
   E_R:=\{a\in\mathbb Z_2^3:(I-R)a\in\mathbb Z^3\}
   \]
   is, after a change of coordinates in \(GL(3,\mathbb Z)\), exactly
   \[
   \mathbb Z\times\mathbb Z\times\mathbb Z_2.
   \]
   Hence \(E_R\) is dense, meager, Haar-null, and has Hausdorff dimension \(1\) in the standard 2-adic metric on \(\mathbb Z_2^3\).
4. The total nontrivial-symmetry-compatible phase set
   \[
   E:=\bigcup_{R\in\mathcal O\setminus\{I\}}E_R
   \]
   is also dense, meager, Haar-null, and has Hausdorff dimension exactly \(1\). Thus
   \[
   \alpha(T)\notin E\quad\Longrightarrow\quad \operatorname{Sym}(T)=\{1\}.
   \]
5. If \(H\le\mathcal O\) is noncyclic, then
   \[
   E_H:=\{a\in\mathbb Z_2^3:H\le P_a\}=\mathbb Z^3.
   \]
   Therefore every Chair44 tiling with noncyclic Euclidean symmetry has an **ordinary integral hierarchy phase**. After an integer translation it has phase \(0\).

Since every cyclic subgroup of the proper cubic group has order at most \(4\), an immediate consequence is
\[
|\operatorname{Sym}(T)|>4
\quad\Longrightarrow\quad
\alpha(T)\in\mathbb Z^3.
\]
In particular, the question whether the published upper bound \(|\operatorname{Sym}(T)|\le24\) is attained can be reduced, up to integer translation, to the zero-phase fiber \(\alpha(T)=0\).

There is also a measure-theoretic consequence. Let \(\mathcal X\) be any translation-invariant registered Chair44 tiling hull carrying a \(\mathbb Z^3\)-invariant Borel probability measure \(\mu\). Then
\[
\alpha_*\mu=m_{\mathbb Z_2^3},
\]
the Haar probability measure on \(\mathbb Z_2^3\), and consequently
\[
\mu\{T:\operatorname{Sym}(T)\ne\{1\}\}=0.
\]
For the primitive registered substitution hull described in the source paper, primitivity gives minimality; hence the asymmetric tilings form a dense \(G_\delta\) set and have full measure for every invariant probability measure on that hull.

## Proof

### 1. Phase covariance under a symmetry

The Chair44 hierarchy is unique. Therefore any Euclidean symmetry of a registered tiling must carry every level-\(n\) supertile partition to itself. The registration theorem in the source paper puts tile anchors on \(\mathbb Z^3\) with frames in the proper cubic group. Thus a symmetry has the form
\[
g(x)=Rx+t,
\qquad R\in\mathcal O,\quad t\in\mathbb Z^3.
\]
At level \(n\), the parent-anchor coset is sent to
\[
R\alpha_n(T)+t+2^n\mathbb Z^3.
\]
Uniqueness of that coset gives
\[
R\alpha_n(T)+t\equiv \alpha_n(T)\pmod{2^n},
\]
or
\[
(I-R)\alpha_n(T)\equiv t\pmod{2^n}.
\]
Passing to the inverse limit yields
\[
(I-R)\alpha(T)=t.
\]

The set \(P_a\) is a subgroup because, whenever \(R,S\in P_a\),
\[
(I-RS)a=(I-R)a+R(I-S)a\in\mathbb Z^3,
\]
and
\[
(I-R^{-1})a=-R^{-1}(I-R)a\in\mathbb Z^3.
\]
The linear-part map on \(\operatorname{Sym}(T)\) is injective: two symmetries with the same linear part differ by a translation, while the phase identity with \(R=I\) forces any translational symmetry vector to be \(0\).

### 2. A single nontrivial cubic rotation leaves only one 2-adic degree of freedom

Fix \(R\ne I\) in \(\mathcal O\). Since \(R\) is a nontrivial proper rotation in three dimensions, \(I-R\) has rational rank \(2\). For the 23 nonidentity signed permutation matrices in \(\mathcal O\), the Smith forms of \(I-R\) have nonzero invariant factors
\[
(1,1),\qquad (1,2),\qquad (2,2).
\]
Thus there are \(U,V\in GL(3,\mathbb Z)\) such that
\[
U(I-R)V=\operatorname{diag}(d_1,d_2,0),
\qquad d_1,d_2\in\{1,2\}.
\]
Writing \(a=Vy\), the condition \((I-R)a\in\mathbb Z^3\) becomes
\[
d_1y_1\in\mathbb Z,
\qquad
d_2y_2\in\mathbb Z.
\]
If \(y\in\mathbb Z_2\) and \(dy\in\mathbb Z\) with \(d\in\{1,2\}\), then \(y\in\mathbb Z\). The case \(d=1\) is immediate. If \(d=2\), write \(2y=m\in\mathbb Z\); since \(y\in\mathbb Z_2\), the integer \(m\) is even, so again \(y\in\mathbb Z\). Hence
\[
E_R=V(\mathbb Z\times\mathbb Z\times\mathbb Z_2).
\]

This set contains \(\mathbb Z^3\), so it is dense in \(\mathbb Z_2^3\). It is a countable union of affine copies of a rank-one closed \(\mathbb Z_2\)-submodule, so it is meager and Haar-null. With the standard max 2-adic metric, each such line has Hausdorff dimension \(1\); the countable union therefore has dimension at most \(1\), and the rank-one kernel itself shows equality. A finite union over the 23 possible nonidentity \(R\) gives the corresponding assertions for \(E\).

### 3. Noncyclic point groups force an integral phase

Let \(H\le\mathcal O\) be noncyclic. The proper cubic group is isomorphic to \(S_4\). Up to conjugacy, the minimal noncyclic subgroup types that must be considered are the two conjugacy classes of Klein four groups and a dihedral group of order \(6\); the larger noncyclic subgroup types contain one of these.

For the coordinate-axis Klein four group, two half-turns may be taken as
\[
R_1=\operatorname{diag}(1,-1,-1),
\qquad
R_2=\operatorname{diag}(-1,1,-1).
\]
If \((I-R_i)a\in\mathbb Z^3\), then \(2a_1,2a_2,2a_3\in\mathbb Z\), so \(a\in\mathbb Z^3\) because \(a\in\mathbb Z_2^3\).

For the other Klein-four type one may take
\[
R_1=\operatorname{diag}(-1,-1,1),
\qquad
R_2=
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&-1
\end{pmatrix}.
\]
The first condition makes \(a_1,a_2\) integral; the second gives \(2a_3\in\mathbb Z\), hence \(a_3\in\mathbb Z\).

For a dihedral subgroup of order \(6\), two half-turns can be chosen, after cubic conjugacy, as
\[
R_1=
\begin{pmatrix}
-1&0&0\\
0&0&1\\
0&1&0
\end{pmatrix},
\qquad
R_2=
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&-1
\end{pmatrix}.
\]
The first condition gives \(2a_1\in\mathbb Z\) and \(a_2-a_3\in\mathbb Z\); the second gives \(a_1-a_2\in\mathbb Z\) and \(2a_3\in\mathbb Z\). Thus \(a_1,a_3\in\mathbb Z\), then \(a_2\in\mathbb Z\).

Hence every noncyclic \(H\) forces \(a\in\mathbb Z^3\). The reverse inclusion is immediate because \((I-R)a\in\mathbb Z^3\) for every integer \(a\) and every integral matrix \(R\). Therefore \(E_H=\mathbb Z^3\).

The finite matrix census in `artifacts/verify_cubic_phase.py` separately checks the same group arithmetic: all 23 nonidentity rotations have rank-two \(I-R\) with the Smith invariant factors listed above, and all 16 noncyclic subgroups have stacked \((I-R)\)-matrices of rank \(3\) whose third determinantal divisor is a power of two.

### 4. Haar phase for every invariant random Chair44 tiling

Let \(\nu=\alpha_*\mu\). The hierarchy phase obeys
\[
\alpha(T+p)=\alpha(T)+p,
\qquad p\in\mathbb Z^3.
\]
Hence \(\nu\) is invariant under addition by the dense subgroup \(\mathbb Z^3\subset\mathbb Z_2^3\). If \(z\in\mathbb Z_2^3\) and \(p_j\in\mathbb Z^3\) tends to \(z\), then for every continuous \(f\), uniform continuity gives
\[
\int f(x+z)\,d\nu(x)
=
\lim_j\int f(x+p_j)\,d\nu(x)
=
\int f(x)\,d\nu(x).
\]
Thus \(\nu\) is invariant under all translations of \(\mathbb Z_2^3\), so \(\nu\) is Haar measure. Since \(E\) is Haar-null, almost every tiling has trivial symmetry.

On the primitive substitution hull, standard primitivity implies minimality. Every invariant probability measure therefore has full support. For each nonidentity affine cubic isometry \(g\), its fixed set in the hull is closed and has measure zero, hence has empty interior. There are only countably many such \(g\) because the linear part has 24 possibilities and the translation part lies in \(\mathbb Z^3\). Therefore symmetric tilings form a meager \(F_\sigma\), and asymmetric tilings form a dense \(G_\delta\).

## Why this sharpens the current symmetry picture

The source paper proves that every Chair44 tiling has a finite symmetry group of order at most \(24\), and asks which finite groups actually occur and whether the bound \(24\) is attained. The phase obstruction above does not solve that classification, but it separates the search into two sharply different regimes:

- away from the dense Hausdorff-dimension-one set \(E\), no nontrivial symmetry is possible at all;
- at nonintegral phases, only cyclic groups of orders \(2,3,4\) can occur;
- every noncyclic group, hence every symmetry group of order greater than \(4\), is confined up to translation to the zero-phase fiber.

Thus the maximum-symmetry question is reduced from the full tiling space to a single hierarchy-phase fiber.

## Limitations

The phase condition is necessary, not sufficient: \(R\in P_{\alpha(T)}\) does not imply that \(T\) actually has an \(R\)-symmetry. In particular, this result does not determine which groups occur inside the zero-phase fiber and does not decide whether order \(24\) is attained.

The Hausdorff-dimension statements concern the 2-adic phase space \(\mathbb Z_2^3\), not the tiling hull itself. The dense \(G_\delta\) conclusion is stated only for the primitive substitution hull, where minimality is available; no claim is made that the entire matching-rule tiling space equals that substitution hull.

The motivating Chair44 preprint is very recent, so unindexed parallel work remains a residual originality risk.

## Reproducibility

`artifacts/verify_cubic_phase.py` is a standalone Python-standard-library check of the finite cubic-group arithmetic. It was executed with Python 3.13.5. Its verified output is stored in `artifacts/verify_cubic_phase.out`.

## References

1. I. Tsiokos, *A Strongly Aperiodic Monotile in Three Dimensions*, arXiv:2609.19214 (2026). In particular, the registration and unique-hierarchy results, the symmetry bound, the hierarchy-phase construction in Proposition 9.1, and the primitive registered substitution are used here. https://arxiv.org/abs/2609.19214
2. J.-Y. Lee and R. V. Moody, *Taylor--Socolar hexagonal tilings as model sets*, Symmetry **5** (2013), 1--46; arXiv:1207.6237. This is a related precedent for an adic internal factor with a dense measure-zero singular set, but not for the Chair44 symmetry-phase obstruction proved here. https://arxiv.org/abs/1207.6237
3. M. Baake, J. A. G. Roberts, and R. Yassawi, *Reversing and extended symmetries of shift spaces*, Discrete Contin. Dyn. Syst. **38** (2018), 835--866. This studies global extended symmetries of shift spaces, including the classical chair tiling shift, rather than stabilizers of individual Chair44 tilings. https://doi.org/10.3934/dcds.2018036
4. A. Bustos, D. Luz, and N. Mañibo, *Admissible Reversing and Extended Symmetries for Bijective Substitutions*, Discrete Comput. Geom. **69** (2023), 421--455. This concerns global extended symmetry groups of substitution systems. https://doi.org/10.1007/s00454-022-00387-8
