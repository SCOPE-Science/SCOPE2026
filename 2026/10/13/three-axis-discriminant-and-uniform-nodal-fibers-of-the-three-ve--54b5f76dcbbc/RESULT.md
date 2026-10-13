# Three-axis discriminant and uniform nodal fibers of the three-vector off-diagonal Gram map

## Finding
For an integer \(M\ge3\), let \(E=\mathbb C^M\) with its standard nondegenerate **symmetric bilinear** form \(B(v,w)=\sum_{a=1}^M v_aw_a\). Consider the off-diagonal Gram morphism
\[
\Phi:E^3\longrightarrow\mathbb A^3,\qquad
(v_1,v_2,v_3)\longmapsto(B(v_1,v_2),B(v_1,v_3),B(v_2,v_3)).
\]
For each \(\{i,j,k\}=\{1,2,3\}\), let
\[
C_{ij}=\{v_k=0,\ \operatorname{rank}[v_i\ v_j]\le1\}\subset E^3.
\]
**Theorem.** The reduced critical-point locus is exactly \(C_{12}\cup C_{13}\cup C_{23}\). The three \(C_{ij}\) are distinct irreducible determinantal cones of dimension \(M+1\), and the *set* of critical values is the union of the three target coordinate axes. In particular every fiber outside those axes is smooth.

For each nonzero \(\tau\in\mathbb C\), the scheme-theoretic singular locus of \(X_{\tau}=\Phi^{-1}(\tau,0,0)\) is smooth and reduced; its points are precisely
\[
\left(v,\frac{\tau}{B(v,v)}v,0\right)
\quad\text{with}\quad B(v,v)\ne0.
\]
It is naturally isomorphic to the principal open subset \(U=E\setminus\{B(v,v)=0\}\), of dimension \(M\). At **every** singular point, not merely generically, the completed local ring of \(X_{\tau}\) is
\[
\mathbb C[[s_1,\ldots,s_M,z_1,\ldots,z_{2M-2}]]
\big/\left(\sum_{a=1}^{M-1}z_a z_{M-1+a}\right).
\]
Thus the transverse singularity is an ordinary quadratic double point of rank \(2M-2\) and multiplicity \(2\). Permuting columns gives the identical statement on both other punctured axes.

## Assumptions and scope
The ground field is \(\mathbb C\); \(B\) is bilinear, **not** Hermitian. The discriminant statement concerns the **set-theoretic image** of the differential critical locus, not its potentially nonreduced scheme-theoretic image or a branch divisor. By a critical point we mean a point where the differential of \(\Phi\) fails to be surjective. The source theorem [1] proves that, for \(M\ge3\), every coefficient fiber is an integral complete intersection of dimension \(3M-3\) (and the map is flat). Thus its singular points coincide with the differential critical points lying on the fiber. The assertion about the singular *scheme* of a nonzero-axis fiber follows from an explicit local equation below.

## Proof
**1. Global differential rank.** Write \(V=[v_1\ v_2\ v_3]\). A linear combination of the differentials of the three component functions vanishes at \(V\) precisely when
\[
VH=0,\qquad H=\begin{pmatrix}0&a&b\\a&0&c\\b&c&0\end{pmatrix}\ne0.
\]
Every nonzero hollow symmetric \(3\times3\) matrix has rank at least two: a rank-one symmetric matrix over \(\mathbb C\) cannot have all its diagonal entries zero. Consequently the existence of such an \(H\) forces \(\operatorname{rank}V\le1\). The rank-zero frame is critical and belongs to every \(C_{ij}\). If \(V\) has rank one, write \(V=u(\alpha,\beta,\gamma)\) with \(u\ne0\). The equations \((\alpha,\beta,\gamma)H=0\) are a homogeneous linear system in \((a,b,c)\) whose determinant, up to sign, is \(2\alpha\beta\gamma\). Hence a nonzero solution exists exactly when \(\alpha\beta\gamma=0\), i.e., at least one of the three columns vanishes. This proves the **complete reduced critical support** is \(\bigcup C_{ij}\), including all coordinate-overlap and origin cases. Each cone is the rank-at-most-one determinantal variety of an \(M\times2\) matrix in the subspace where the third column is zero; it is irreducible of dimension \(M+1\). The components are distinct.

**2. Critical values.** The image of \(C_{12}\) is contained in the \(t_{12}\)-axis, and similarly cyclically. Conversely, for any \(\tau\in\mathbb C\), the frame \((e_1,\tau e_1,0)\in C_{12}\) maps to \((\tau,0,0)\). Thus the critical-value set is exactly all three coordinate axes. Flatness and complete-intersection fibers from [1] justify the Jacobian criterion for the fibers, so every fiber at a point of the complementary open target is smooth.

**3. Entire punctured-axis singular scheme.** Fix \(\tau\ne0\) and write \(q(v)=B(v,v)\). A critical point mapping to \((\tau,0,0)\) must have rank one, third column zero and the first two columns nonzero. Writing \((v_1,v_2)=(v,\lambda v)\), the equation \(\lambda q(v)=\tau\) forces \(q(v)\ne0\) and \(\lambda=\tau/q(v)\). This identifies the set-theoretic singular locus with \(U=\{q(v)\ne0\}\), smooth irreducible of dimension \(M\).

Near any of its points, \(v_1\) remains in \(U\). The orthogonal direct-sum splitting \(E=\mathbb Cv_1\oplus v_1^\perp\) is algebraic in the base \(v_1\) on this open set. Write uniquely
\[
v_2=bv_1+w_2,\qquad v_3=cv_1+w_3,\qquad w_2,w_3\in v_1^\perp.
\]
The first two equations \(B(v_1,v_2)=\tau\), \(B(v_1,v_3)=0\) set \(b=\tau/q(v_1)\), \(c=0\). The remaining equation becomes **exactly** \(B(w_2,w_3)=0\), in the rank-\(2(M-1)\) vector bundle \(v_1^\perp\oplus v_1^\perp\to U\). The restriction of \(B\) to \(v_1^\perp\) is nondegenerate; formal (or analytic) trivialization around any chosen point turns the equation into \(\sum_{a=1}^{M-1}z_a z_{M-1+a}=0\), with \(M\) smooth base variables.

Its relative derivatives are the \(2(M-1)\) linear normal coordinates, so the full Jacobian singular **scheme** near the singular locus is exactly the reduced zero section \(w_2=w_3=0\). All other points on the fiber are smooth by Step 1. Thus the singular scheme is globally the stated smooth reduced \(U\), and each transverse Hessian has full rank \(2M-2\). This proves the claim.

## Verification
The included `check_discriminant.py` uses only the Python standard library. It exhaustively checks all \(3^9=19683\) frames over \(\mathbb F_3\) with \(M=3\): rank deficiency occurs precisely for rank-at-most-one frames with a zero column; the observed critical values are precisely the three finite-field coordinate axes. It also verifies the Hessian rank of the displayed transverse quadratic form for \(3\le M\le8\). Expected terminal line: `GRAM_DISCRIMINANT_EXACT_OK; frames= 19683`. These checks are finite controls; the argument in the preceding section proves the result for every \(M\ge3\) over \(\mathbb C\).

## Relationship to prior work
Xie [1] proves a uniform flatness, reducedness, integrality, and rational-singularity classification for **all fibers** of the off-diagonal Gram morphism. Its full introduction and coefficient-fiber section do not give the precise differential critical locus, the three-axis critical-value discriminant, or the scheme-theoretic singular locus and completed local rings of fibers over nonzero targets. Casabella--Sammartano [2] analyze the **zero** orthogonal-frame fiber, establishing prime/complete-intersection thresholds and geometric properties; zero-fiber results alone do not imply which nonzero target fibers are singular. The contribution here is an all-target smoothness stratification together with the uniform, everywhere-nodal local model on the punctured critical-value axes. Standard determinantal and Jacobian linear algebra is used in the proof, not claimed as a separate innovation.

## Limitations
The theorem does not calculate the scheme-theoretic discriminant or critical-scheme multiplicities along their intersections; it does not classify the full singular scheme of the **zero** fiber, nor classify Gram maps for four or more columns. It is not a statement about real positive-definite Hermitian Gram matrices. Prior unlocated equivalent special-case computations remain a bibliographic risk. The proof of the fiber complete-intersection property invokes the explicitly cited source [1].

## References
[1] Ying Xie, *Sharp FRS and singularity thresholds for off-diagonal Gram maps*, arXiv:2610.02585v1, first public 2026-10-01, especially Theorem 1.1 and Section 4. https://arxiv.org/html/2610.02585v1

[2] Laura Casabella and Alessio Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058v1, first public 2025-12-31, Theorems 1–3 and Sections 2.3, 6, 8. https://arxiv.org/pdf/2512.25058
