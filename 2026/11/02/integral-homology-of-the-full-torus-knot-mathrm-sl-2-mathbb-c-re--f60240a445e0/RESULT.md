# Integral homology of the full torus-knot \(\mathrm{SL}_2(\mathbb C)\)-representation variety

## Finding

**Theorem.** For coprime integers \(p,q>1\), let
\[
\Gamma_{p,q}=\langle x,y\mid x^p=y^q\rangle,\qquad
R_{p,q}=\operatorname{Hom}(\Gamma_{p,q},\mathrm{SL}_2(\mathbb C))_{\mathrm{red}},\qquad
g=\frac{(p-1)(q-1)}2.
\]
With the Euclidean (complex-analytic) topology, its **integral singular homology** is
\[
H_k(R_{p,q};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,3,\\
\mathbb Z^g,&k=1,4,\\
(\mathbb Z/2\mathbb Z)^g,&k=2,\\
0,&k\geq5.
\end{cases}
\]
In particular, the entire variety has nonzero two-torsion in second homology, unlike its singular locus, whose integral homology is free abelian [1].

## Assumptions and scope

All varieties are considered over \(\mathbb C\), and \(R_{p,q}\) denotes the **full reduced affine representation variety of matrices**, not its character variety (the conjugation quotient), its irreducible-representation locus, or the singular locus. The exponents are coprime integers strictly greater than one. Singular homology is taken with \(\mathbb Z\) coefficients. Write \(Q=\{U\in\mathfrak{sl}_2(\mathbb C):U^2=I\}\cong\{z_1^2+z_2^2+z_3^2=1\}\).

## Proof

**1. Closed-component cover.** Liriano [1, Section 2, Lemmas 1–2] proves an explicit decomposition of the reduced variety into closed algebraic subvarieties
\[
R_{p,q}=R_0\cup\bigcup_{i=1}^{g}Y_i,
\qquad R_0\cong\mathrm{SL}_2(\mathbb C),\quad Y_i\cong Q\times Q.
\]
The distinct \(Y_i\) are disjoint, and, under the specified product coordinates, the entire intersection with \(R_0\) is
\[
Z_i=R_0\cap Y_i=\Delta_{+,i}\sqcup\Delta_{-,i},\quad
\Delta_{\pm,i}=\{(U,\pm U):U\in Q\}\cong Q.
\]
The indexing count is \(g\). Set \(A=R_0\), \(B=\bigsqcup_{i=1}^{g}Y_i\), and \(Z=A\cap B=\bigsqcup_{i=1}^{g}Z_i\). Since this is a finite family of closed real-semialgebraic sets, a semialgebraic triangulation compatible with every component produces a common CW model in which the inclusions of the intersections are cofibrations. Consequently the integral Mayer–Vietoris long exact sequence for this **closed** cover applies.

**2. Component topology and the involution.** Polar decomposition retracts \(R_0\cong\mathrm{SL}_2(\mathbb C)\) onto \(\mathrm{SU}_2\cong S^3\). Write a point of \(Q\) in its quadratic form as \(z=u+iv\), where \(u,v\in\mathbb R^3\). Its equation implies \(\|u\|^2-\|v\|^2=1\) and \(u\cdot v=0\), identifying \(Q\) diffeomorphically with \(TS^2\). Fiber contraction gives \(Q\simeq S^2\) [1, Theorem 4]. Therefore
\[
H_*(R_0)=H_*(S^3),\quad H_*(Y_i)=H_*(S^2\times S^2),\quad
H_*(Z_i)=H_*(S^2\sqcup S^2)
\]
with integer coefficients. Under the retraction of \(Q\), \(U\mapsto-U\) restricts on the zero section to the antipodal map \(S^2\to S^2\), whose degree is \(-1\). In particular it acts as multiplication by \(-1\) on \(H_2(Q;\mathbb Z)\).

**3. The decisive integral map.** Choose a generator for \(H_2(Q;\mathbb Z)\), the two product-factor generators for \(H_2(Y_i;\mathbb Z)\cong\mathbb Z^2\), and the generator on each component of \(Z_i\). The two inclusions \(U\mapsto(U,U)\) and \(U\mapsto(U,-U)\) therefore induce
\[
H_2(Z_i;\mathbb Z)\longrightarrow H_2(Y_i;\mathbb Z),\qquad
M=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
The other target \(H_2(R_0;\mathbb Z)\) is zero. Since \(\det M=-2\), the map is injective and its integer Smith normal form is \(\operatorname{diag}(1,2)\). Thus, on all components,
\[
H_2(Z;\mathbb Z)\longrightarrow H_2(A;\mathbb Z)\oplus H_2(B;\mathbb Z)
\]
is injective with cokernel \((\mathbb Z/2\mathbb Z)^g\). As \(H_1(Z)=H_1(A)=H_1(B)=0\), Mayer–Vietoris yields the asserted \(H_2(R_{p,q})\).

**4. The remaining degrees.** The same exact sequence has \(H_3(Z)=H_4(Z)=0\), \(H_3(A)=\mathbb Z\), \(H_3(B)=0\), \(H_4(A)=0\), and \(H_4(B)=\mathbb Z^g\). Injectivity of the map in Step 3 therefore implies \(H_3(R_{p,q})\cong\mathbb Z\) and \(H_4(R_{p,q})\cong\mathbb Z^g\). All groups above degree four vanish. In degree zero, \(H_0(Z)\cong\mathbb Z^{2g}\) maps to \(H_0(A)\oplus H_0(B)\cong\mathbb Z^{g+1}\). The two generators belonging to each \(Z_i\) have the same image, namely the difference between the connected-component generator of \(A\) and that of \(Y_i\). These \(g\) image vectors are independent and primitive. Thus its kernel is \(\mathbb Z^g\) and its cokernel is \(\mathbb Z\), yielding \(H_1(R_{p,q})\cong\mathbb Z^g\) and \(H_0(R_{p,q})\cong\mathbb Z\). This exhausts all degrees.

By the integral universal-coefficient theorem, one also obtains
\[
H^k(R_{p,q};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z^g,&k=1,4,\\
\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^g,&k=3,\\
0,&k=2\text{ or }k\geq5.
\end{cases}
\]
The alternating sum of the free ranks is zero, consistent with the componentwise Euler-characteristic inclusion–exclusion formula.

## Verification

The standalone `verify.py` independently constructs the integral Mayer–Vietoris degree-two matrix for the explicitly enumerated parity-admissible indices in several coprime examples, computes its integer Smith normal form, and checks the degree-zero incidence matrix, the number of branches and the Betti-number Euler characteristic. It prints `VERIFY_OK` when all tests pass. This arithmetic exercises the lattice calculations but is **not** a substitute for Step 1's geometric decomposition, the antipodal degree in Step 2, or the all-exponent exact-sequence proof.

## Relationship to prior work

Liriano [1] computes the singular locus and its free integral homology, and its Lemmas 1–2 give precisely the component/intersection geometry used here; [1] does **not** compute the homology of the entire representation variety. Florentino–Lawton [2] establish path-connectedness in much greater generality and count irreducible components, but do not obtain the degree-two integral torsion. Muñoz [3] computes the **character variety**, a distinct conjugation quotient with components that are affine lines; it does not calculate the integer homology of this full representation variety. The present computation extracts new integral torsion from the anti-diagonal gluing: it is invisible to rational Betti numbers and to character-variety component counts. A complete priority search of all historical topology papers has not been established.

## Limitations

The calculation concerns only the reduced full \(\mathrm{SL}_2(\mathbb C)\) representation variety of a two-generator coprime torus-knot group. It does not identify the homotopy type up to equivalence, cup products, the scheme structure before reduction, other reductive target groups, or arbitrary knot groups. The asserted torsion depends on the **integral** antipodal map; rational calculations alone cannot detect it. Priority relative to inaccessible or unindexed historical sources remains a residual risk. No independent mathematical audit has been performed.

## References

[1] S. Liriano, *Singular Loci of \(\mathrm{SL}_2(\mathbb C)\)-Representation Varieties of Torus Knot Groups*, arXiv:2610.32064v1 (first posted 2026-10-23), https://arxiv.org/html/2610.32064v1 . Section 2, Lemmas 1–2 and Section 3, Theorem 4.

[2] C. Florentino and S. Lawton, *Character Varieties of Generalized Torus Knot Groups*, Mediterranean Journal of Mathematics 22, 177 (2025), https://doi.org/10.1007/s00009-025-02947-7 . Theorems 1.1 and 1.2.

[3] V. Muñoz, *The \(\mathrm{SL}(2,\mathbb C)\)-Character Varieties of Torus Knots*, Revista Matemática Complutense 22 (2009), https://arxiv.org/abs/0901.1783 . Theorem 3.1.
