# Six singular components and transverse nodes of orthogonal three-frame varieties

## Finding
For each integer \(M\ge4\), let \(E=\mathbb C^M\) carry the standard nondegenerate symmetric bilinear form \(\langle\ ,\ \rangle\), and set
\[
X_M=\{(v_1,v_2,v_3)\in E^3:\langle v_1,v_2\rangle=\langle v_1,v_3\rangle=\langle v_2,v_3\rangle=0\}.
\]
The scheme \(X_M\) is an integral complete intersection of dimension \(3M-3\) (the prerequisite is already known). The following statements concern its *reduced* singular locus, not the possibly nonreduced Jacobian ideal.

For every permutation \(\{i,j,k\}=\{1,2,3\}\), define
\[
B_k=\{v_i=v_j=0\}\cong\mathbb A^M
\]
and
\[
A_k=\{v_k=0,\ \operatorname{rank}[v_i\ v_j]\le1,
\ \langle v_i,v_i\rangle=\langle v_i,v_j\rangle=\langle v_j,v_j\rangle=0\}.
\]
Then the complete irreducible-component decomposition is
\[
(\operatorname{Sing}X_M)_{\mathrm{red}}
  = A_1\cup A_2\cup A_3\cup B_1\cup B_2\cup B_3.
\]
All six components are distinct, irreducible, and have dimension \(M\). Each \(B_k\) is linear, and \(\mathbb P(A_k)\simeq\mathbb P^1\times Q^{M-2}\) under the Segre embedding, where \(Q^{M-2}\subset\mathbb P^{M-1}\) is a nonsingular quadric. Therefore
\[
\operatorname{codim}_{X_M}\operatorname{Sing}(X_M)=2M-3,
\qquad
\deg\bigl((\operatorname{Sing}X_M)_{\mathrm{red}}\bigr)=6M-3.
\]
On a dense open subset of *each* of these six components, the analytic local germ of \(X_M\) is the product of a smooth \(M\)-fold germ and a nondegenerate quadratic hypersurface germ in \(2M-2\) variables. Thus its generic transverse type is an ordinary double point of complex dimension \(2M-3\).

## Assumptions and scope
All schemes are over \(\mathbb C\); the bilinear form is symmetric, not Hermitian. A column is isotropic if \(\langle v,v\rangle=0\). The singular locus in the theorem has its reduced induced structure. The degree is the projective degree of the homogeneous affine cone, equivalently the degree of its projectivization. The assertion about generic analytic germs concerns dense Zariski-open subsets, **not** every point on the singular locus; intersections of components may have more complicated singularities.

## Proof
**Complete intersection and Jacobian criterion.** The three defining quadrics are a prime regular sequence for \(M\ge4\), so \(\dim X_M=3M-3\), by Casabella--Sammartano's criterion [2]. Label these quadrics \(f_{12},f_{13},f_{23}\). Their differentials at a frame \(V=[v_1\ v_2\ v_3]\) are linearly dependent if and only if there is a nonzero *hollow symmetric* matrix
\[
H=\begin{pmatrix}0&a&b\\a&0&c\\b&c&0\end{pmatrix}
\]
such that \(VH=0\). This follows by differentiating \(\sum_{i<j}h_{ij} f_{ij}\) in each column. The rank of the Jacobian is less than three precisely in this situation. Since \(X_M\) is an integral codimension-three complete intersection, this is precisely its singular locus.

**Classifying all points.** If \(abc\ne0\), then \(\det H=2abc\ne0\), hence \(V=0\); the origin belongs to all six sets. If exactly one among \(a,b,c\) is nonzero, the two columns incident to its edge are zero, giving a point of some \(B_k\). If exactly two entries are nonzero, after a permutation we may assume \(a,b\ne0,c=0\). Then \(VH=0\) says \(v_1=0\) and \(a v_2+b v_3=0\), so the other columns are proportional. Their orthogonality forces the common direction to be isotropic unless both vanish; the frame belongs to \(A_1\) or to the origin. Conversely, any point of \(B_k\) has an obvious single-edge dependency. A point of \(A_k\) with both nonzero remaining columns admits a two-edge dependency; if one remaining column vanishes, it also belongs to a \(B_j\) and is singular by the preceding case. This proves the exact set-theoretic union.

**Irreducibility, dimension, and degree.** Each \(B_k\) is a linear \(M\)-space. A nonzero element of \(A_k\) is a pair \((s w,t w)\), with \([s:t]\in\mathbb P^1\) and \([w]\in Q^{M-2}\); thus its projectivization is exactly the Segre embedding of \(\mathbb P^1\times Q^{M-2}\). For \(M\ge4\), the quadric is smooth and irreducible. Hence \(A_k\) is irreducible of dimension \(M\), and its degree is
\[
\int_{\mathbb P^1\times Q^{M-2}}
\bigl(h_1+h_Q\bigr)^{M-1}
=(M-1)\int_{Q^{M-2}}h_Q^{M-2}
=2(M-1).
\]
The six sets are distinct (generic points have different vanishing patterns or ranks) and equidimensional. Their sum-of-top-cycles degree is \(3\cdot1+3\cdot2(M-1)=6M-3\). The dimension formula gives singular codimension \((3M-3)-M=2M-3\).

**Generic transverse node at a linear component.** Up to permuting columns choose \(p=(0,0,z)\) with \(\langle z,z\rangle\ne0\), a dense open point of \(B_3\). Near \(p\), the differentials of \(f_{13},f_{23}\) are independent and eliminate the \(z\)-components of \(v_1,v_2\). The remaining local equation is \(\langle v_1,v_2\rangle=0\) on the orthogonal complement \(z^\perp\). The latter is a nondegenerate bilinear space of dimension \(M-1\), so the quadratic Hessian in its two copies has rank \(2M-2\); the remaining \(M\) directions are smooth parameters. The holomorphic Morse lemma with parameters gives the stated analytic product.

**Generic transverse node at an isotropic component.** After permuting columns take a dense open point \(p=(0,w,\lambda w)\in A_1\), with \(w\ne0\), \(\langle w,w\rangle=0\), and \(\lambda\ne0\). Put \(u=v_1\), \(v=v_2\), and \(r=v_3-\lambda v_2\). The equations become \(\langle u,v\rangle=0\), \(\langle u,r\rangle=0\), and \(\langle v,r\rangle+\lambda\langle v,v\rangle=0\). Choose a Witt basis \(w,z,W\) with \(\langle w,z\rangle=1\), \(\langle w,w\rangle=\langle z,z\rangle=0\), and \(\dim W=M-2\). Write
\[
 v=(1+\alpha)w+\beta z+q,
\quad u=xw+yz+s,
\quad r=cw+\delta z+t,
\qquad q,s,t\in W.
\]
The first and third equations have independent linear parts \(y\) and \(\delta+2\lambda\beta\); using them to solve locally for \(y,\delta\) leaves a single hypersurface equation \(\langle u,r\rangle=0\). Its quadratic part is
\[
-2\lambda x\beta+\langle s,t\rangle_W,
\]
which has rank \(2+2(M-2)=2M-2\). The remaining \(M\) coordinates are parameters. Since the set-theoretic singular locus is precisely the smooth dense stratum of \(A_1\) here, the kernel of the quadratic Hessian identifies those parameter directions. The analytic Morse lemma with parameters again produces a smooth \(M\)-factor times an ordinary quadratic singularity. Symmetry treats \(A_2,A_3\).

## Verification
The accompanying `CHECK.py` uses exact symbolic Jacobians and Hessians at explicit representatives of the two kinds of components for \(M=4,5,6,7\). It checks Jacobian rank two and transverse Hessian rank \(2M-2\), together with the degree formula; the expected output ends in `EXACT_CHECK_OK`. These tests are independent consistency checks of local calculations, not substitutes for the proof over every integer \(M\ge4\). Run `python CHECK.py` with SymPy installed.

## Relationship to prior work
Ying Xie [1] studies sharp rational-singularity and log-canonical thresholds for the off-diagonal Gram map, including these three-vector zero fibers. Casabella and Sammartano [2] establish the prime and complete-intersection criteria and investigate smoothness strata and factoriality of orthogonal-frame schemes. Conca and Welker [3] develop the underlying Lovász--Saks--Schrijver ideals and associated primality and complete-intersection results. Their cited results supply context and the integral-complete-intersection premise, but the inspected statements do not give this six-component reduced singular locus, its projective degree, or generic transverse quadratic types. Classical Jacobian and analytic Morse criteria are proof tools, not claimed innovations.

## Limitations
This theorem does not describe the full scheme structure of the Jacobian singular subscheme, the singularity type at component intersections or the origin, or the analogous classification for four or more frame columns. It applies over \(\mathbb C\); extensions to other characteristics require separate arguments. The classification and degree concern the reduced support. A prior equivalent computation hidden in earlier specialized incidence-geometry literature cannot be categorically excluded.

## References
[1] Ying Xie, *Sharp FRS and singularity thresholds for off-diagonal Gram maps*, arXiv:2610.02585v1 (first posted 2026-10-01), Sections 1, 5--8. https://arxiv.org/abs/2610.02585

[2] Laura Casabella and Alessio Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058v1 (first posted 2025-12-31), Sections 3, 6, 7. https://arxiv.org/abs/2512.25058

[3] Aldo Conca and Volkmar Welker, *Lovász--Saks--Schrijver ideals and coordinate sections of determinantal varieties*, arXiv:1801.07916v1 (first posted 2018-01-24). https://arxiv.org/abs/1801.07916
