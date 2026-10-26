# Lagrangian jumping planes of the rank-nine uniform symplectic bundle

## Finding
Fix a six-dimensional complex vector space \(V\) and a nondegenerate bivector \(\omega\in\bigwedge^2V\). Define the hyperplane \(W_\omega=\{\alpha\in\bigwedge^2V^*: \langle\alpha,\omega\rangle=0\}\). For the rank-nine bundle \(E_\omega\) in the exact sequence
\[
0\longrightarrow E_\omega\longrightarrow W_\omega\otimes\mathcal O_{\mathbb P(V)}(1)\longrightarrow\Omega^1_{\mathbb P(V)}(3)\longrightarrow0,
\]
consider projective planes \(\Pi=\mathbb P(H)\), with \(H\subset V\) three-dimensional. Let \(H\) be *Lagrangian* when the alternating form inverse to \(\omega\) vanishes identically on \(H\).

If \(H\) is not Lagrangian, there is an isomorphism
\[
E_\omega|_\Pi\simeq\mathcal O_\Pi\oplus\Omega^1_\Pi(2)^{\oplus3}\oplus\mathcal O_\Pi(1)^{\oplus2}.
\]
If \(H\) is Lagrangian, there is an isomorphism
\[
E_\omega|_\Pi\simeq\mathcal O_\Pi\oplus\mathcal O_\Pi(1)^{\oplus3}\oplus K_H,
\]
where \(K_H\) is the rank-five kernel of a surjection \(\Omega^1_\Pi(2)^{\oplus3}\to\mathcal O_\Pi(1)\). Consequently
\[
h^0(\Pi,E_\omega|_\Pi(-1))=\begin{cases}2& H\text{ non-Lagrangian},\\3&H\text{ Lagrangian}.\end{cases}
\]
The entire jumping-plane locus is \(\operatorname{LG}(3,V)\), a smooth sixfold of codimension three inside \(\operatorname{Gr}(3,V)\).

## Assumptions and scope
The ground field is \(\mathbb C\). Every projective plane means a linear \(\mathbb P^2\subset\mathbb P^5\). The bivector is assumed nondegenerate (rank six). We assert an exhaustive set-theoretic cohomology jump classification and identify a smooth natural zero scheme cutting it out; we do not assert a scheme-theoretic identification with a separately defined Fitting jumping scheme.

## Proof
**1. A global kernel.** The Euler–Koszul sequence gives
\[
0\longrightarrow\Omega^2_{\mathbb P(V)}(3)\longrightarrow\bigwedge^2V^*\otimes\mathcal O(1)\longrightarrow\Omega^1_{\mathbb P(V)}(3)\longrightarrow0.
\]
Taking the inverse image of \(W_\omega\otimes\mathcal O(1)\) identifies \(E_\omega\) with the kernel of the contraction morphism
\[
\Omega^2_{\mathbb P(V)}(3)\xrightarrow{\omega}\mathcal O(1).
\]
At \([v]\in\mathbb P(V)\), contraction is nonzero exactly when the image of \(\omega\) in \(\bigwedge^2(V/\langle v\rangle)\) is nonzero. A nondegenerate bivector cannot belong to \(v\wedge V\), which consists of bivectors of rank at most two. Therefore contraction is everywhere surjective, so \(E_\omega\) is locally free of rank nine.

**2. Restriction to a plane.** Choose a vector-space complement \(V=H\oplus M\), \(\dim H=\dim M=3\). Restricting the Euler sequence to \(\Pi=\mathbb P(H)\) yields the splitting
\[
\Omega^1_{\mathbb P(V)}(1)|_\Pi\simeq\Omega^1_\Pi(1)\oplus\mathcal O_\Pi^{\oplus3}.
\]
Taking its exterior square and twisting by \(\mathcal O_\Pi(1)\) gives
\[
\Omega^2_{\mathbb P(V)}(3)|_\Pi\simeq
\mathcal O_\Pi\oplus\Omega^1_\Pi(2)^{\oplus3}\oplus\mathcal O_\Pi(1)^{\oplus3}.
\]
In this decomposition, the last summand maps to \(\mathcal O_\Pi(1)\) by a constant linear functional specified by \(\bar\omega\in\bigwedge^2(V/H)\). Thus \(\bar\omega\ne0\) allows one copy of \(\mathcal O_\Pi(1)\) to be split off from this surjection. Elementary elimination of the other components proves the stated non-Lagrangian direct-sum formula.

**3. The exceptional planes.** Let \(b\in\bigwedge^2V^*\) be the inverse symplectic form. The condition \(\bar\omega=0\) is equivalent to \(\omega\in H\wedge V\). For \(\dim H=3\) and nondegenerate \(\omega\), this holds precisely when \(b|_H=0\): this is immediate from a symplectic basis for \(V\), or by identifying the annihilator of \(H\) under \(b\). Such \(H\) are the Lagrangian three-planes. Choosing a Lagrangian complement \(M\) writes \(\omega\in H\wedge M\). Consequently both the \(\mathcal O_\Pi\) summand (the \(\bigwedge^2H\)-part) and all three \(\mathcal O_\Pi(1)\) summands (the \(\bigwedge^2M\)-part) have zero contraction with \(\omega\). The remaining restriction is a surjection \(\Omega^1_\Pi(2)^{\oplus3}\to\mathcal O_\Pi(1)\), since global contraction was everywhere surjective. Its kernel is \(K_H\), yielding the exceptional decomposition.

**4. Cohomology.** From the Euler sequence on \(\mathbb P^2\), \(H^0(\Pi,\Omega^1_\Pi(1))=0\). Twisting the non-Lagrangian decomposition by \(\mathcal O_\Pi(-1)\) gives precisely two global sections. In the Lagrangian case, \(K_H(-1)\) injects into \(\Omega^1_\Pi(1)^{\oplus3}\), so it has no global sections. The three copies of \(\mathcal O_\Pi\) give exactly three global sections.

**5. Geometry of the locus.** The projection \(\bar\omega\) is a section of \(\bigwedge^2\mathcal Q\) on \(\operatorname{Gr}(3,V)\), where \(\mathcal Q\) is its universal rank-three quotient. Its zero locus is precisely \(\operatorname{LG}(3,V)\). The latter is smooth of dimension \(3(3+1)/2=6\), hence codimension three in the nine-dimensional Grassmannian. More concretely, the differential of the section at a Lagrangian plane, in tangent coordinates \(\operatorname{Hom}(H,H^*)\), is its skew-symmetrization onto \(\bigwedge^2H^*\), which is surjective. The section is therefore regular and its zero scheme reduced.

## Verification
The accompanying `verify_planes.py` performs exact rational-matrix checks of canonical bivector rank, all twenty coordinate three-planes, the eight coordinate Lagrangian planes, and the ranks and degree-one Chern numbers of the displayed bundle decompositions. Reproduce with `python3 verify_planes.py`. These finite checks are consistency tests; the theorem for all planes is established by the Euler–Koszul and symplectic-linear-algebra arguments above.

## Relationship to prior work
Denham–Miró-Roig–Schenck establish the rank-nine uniform non-homogeneous bundle from a fourteen-dimensional space of sections and give its splitting type on every projective line. Landsberg–Manivel construct a rank-nine symplectic example from a constant-rank matrix and describe its extension and deformations. Neither paper supplies the complete jumping-plane cohomology stratification here. The new statement concerns restrictions to \(\mathbb P^2\), not line jumping, and explains why a bundle uniform on all lines retains geometric information detectable on planes.

## Limitations
The argument assumes a nondegenerate complex bivector and only studies linear projective planes and the indicated zeroth cohomology jump. It does not classify general deformations of this bundle or identify a scheme structure on an independently defined cohomology Fitting locus. Priority cannot be ruled out for work not indexed by the literature searches.

## References
1. G. Denham, R. Miró-Roig, H. Schenck, *Uniform non-homogeneous vector bundles: A counterexample to the conjecture of Drézet and Ballico-Ellia*, arXiv:2610.20208v1 (first public 2026-10-14), Theorem 3.3 and Remarks 3.4–3.5, https://arxiv.org/abs/2610.20208 .
2. J. M. Landsberg, L. Manivel, *Equivariant spaces of matrices of constant rank*, arXiv:2212.04228v1 (2022), Section 6.2 and Lemma 21, https://arxiv.org/abs/2212.04228 .
