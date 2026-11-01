# An integral 64-fold gluing obstruction in Fano-matroid homology

## Finding
Let \(F_7\) be the binary rank-three Fano matroid on the nonzero vectors \(V=\mathbb F_2^3\setminus\{0\}\), and let \(K\) be its independence complex: all vertices and edges, together with precisely those unordered triples \(\{a,b,c\}\) for which \(a\oplus b\oplus c\ne0\). Put \(G=\operatorname{GL}_3(\mathbb F_2)\) and \(H=\widetilde H_2(K;\mathbb Z)\), with the natural signed simplicial action. Then \(H\cong\mathbb Z^{13}\).

Let \(U_7\subseteq H\otimes\mathbb Q\) be the canonical seven-dimensional irreducible isotypic summand of the rational \(G\)-representation, and \(U_6\) its six-dimensional complementary isotypic summand. Define the **saturated integral lattices** \(L_7=H\cap U_7\) and \(L_6=H\cap U_6\), inside \(H\otimes\mathbb Q\). Their sum is proper and its precise obstruction group is
\[
\boxed{H/(L_7\oplus L_6)\cong(\mathbb Z/4\mathbb Z)^3.}
\]
In particular, the two canonical rational summands fail to split the natural integral homology lattice by exactly index \(64\). The theorem is about this integral extension invariant, not merely the rational character or the known rank of homology.

## Assumptions and scope
The vertices are enumerated as integers \(1,\ldots,7\), interpreted as the three binary coordinate bits, with XOR written \(\oplus\). Chain orientations are ascending-vertex order; all homology and the gluing quotient are over \(\mathbb Z\) unless a field is explicitly displayed. The action uses every one of the \(168\) invertible binary linear substitutions. The seven-dimensional representation is specified intrinsically by the reduced permutation action on the eight Sylow-seven subgroups of \(G\), and hence does not depend on a chosen rational decomposition. The statement is specific to \(F_7\) and the canonical full collineation group.

## Proof
**1. Integral cycle lattice.** The nonempty faces of \(K\) number \(7\) vertices, \(21\) edges, and \(28\) triangles. With ascending orientations, the simplicial boundary \(B=\partial_2\) is the \(21\)-by-\(28\) matrix whose column for \(a<b<c\) is \([b,c]-[a,c]+[a,b]\). The fifteen triangle columns having zero-based indices
\[
(0,1,2,3,4,5,6,7,8,9,10,11,12,16,19)
\]
form a rank-fifteen submatrix with Smith factors \(1\) repeated fifteen times. Each of the other thirteen boundary columns is an *integer* combination of these fifteen. Subtracting those combinations gives thirteen independent integer cycles with an identity submatrix in the thirteen free triangle coordinates. Conversely, every integer cycle is uniquely determined by those thirteen coordinates, since the selected columns are rationally linearly independent. Thus \(H=\ker\partial_2\cong\mathbb Z^{13}\); no three-simplices exist. The same calculation yields \(\widetilde H_1(K;\mathbb Z)=0\) since the complete one-skeleton has boundary-cycle rank fifteen.

**2. The canonical rational projector.** The invertible maps of \(\mathbb F_2^3\) give \(|G|=168\), and the \(48\) elements of order seven form exactly eight cyclic subgroups of order seven. Conjugation permutes these eight subgroups; subtracting the trivial line from the permutation module defines an irreducible rational character \(\chi_7\), since the exact class calculation gives \(\langle\chi_7,\chi_7\rangle_G=1\). Relative to the five point-permutation cycle types \((1^7),(1^3 2^2),(1 3^2),(1 2 4),(7)\), the conjugacy-class sizes are \(1,21,56,42,48\). The characters of \(H\otimes\mathbb Q\) and \(U_7\) are respectively
\[
\chi_H=(13,-3,1,1,-1),\qquad \chi_7=(7,-1,1,-1,0).
\]
Their inner product is one. Thus the \(\chi_7\)-isotypic component \(U_7\) has dimension seven and appears once; its complementary component \(U_6\) has dimension six. The full character \(\chi_H\) is also independently checked by reduced simplicial Lefschetz traces on every group element.

Let \(\rho:G\to\operatorname{GL}(H)\) be the integral action, and form the endomorphism
\[
C=\sum_{g\in G}\chi_7(g^{-1})\rho(g).
\]
The rational central-idempotent formula gives \(C=24P_7\), where \(P_7\) is projection onto \(U_7\); in particular \(C^2=24C\), \(\operatorname{rank}(C)=7\), \(\ker C=U_6\). All of these identities are also verified by exact integer matrices.

**3. Smith form and integral gluing.** In the explicit thirteen-cycle integral basis constructed in step 1, the computed Smith diagonal of the *entire* thirteen-by-thirteen matrix \(C\) is
\[
(6,6,6,24,24,24,24,0,0,0,0,0,0).
\]
Set \(L_7=H\cap U_7\), \(L_6=H\cap U_6\). As \(C(H)\subseteq L_7\) and \(C|_{L_7}=24\operatorname{id}\), we have \(24L_7\subseteq C(H)\subseteq L_7\). The map \([x]\mapsto[Cx]\) therefore gives an isomorphism
\[
H/(L_7+L_6)\overset\sim\longrightarrow C(H)/24L_7.
\]
Indeed its kernel consists precisely of \(x=y+z\) with \(y\in L_7\), \(z\in L_6\). By the Smith theorem, the nonzero diagonal entries \(d_i\) above are the invariant factors of the inclusion \(C(H)\hookrightarrow L_7\), because \(L_7\) is the saturation of \(C(H)\) in the free lattice \(H\). Therefore
\[
C(H)/24L_7\cong\bigoplus_{i=1}^{7}\mathbb Z/(24/d_i)\mathbb Z
\cong(\mathbb Z/4\mathbb Z)^3.
\]
All denominators and bases are over the integers; no rational rank computation is used as a substitute for the Smith calculation.

## Verification
Run `python verify_fano.py` with Python 3 and SymPy available in the directory containing `certificate.json`. The code constructs the entire chain complex, exact integer cycle basis, all \(168\) group actions, Sylow subgroup permutation character, independently computed reduced Lefschetz character, central projector, and integral Smith factors. It recomputes all assertions from definitions and compares its numerical summary with the independent expected-data file `certificate.json`. The supplied `verification_output.txt` records a completed execution with `FANO_INTEGRAL_GLUING_VERIFY_OK`. The certificate is a finite exact calculation, not a claim of formal external proof certification.

## Relationship to prior work
De Loera, Lee, Margulies and Miller (2013, Section 4) specify the same seven-point Fano matroid and study its orientability by polynomial equations, rather than the integral automorphism-module structure of its independence homology. Moci and Pezzoli (2020 preprint; 2021 journal publication, Theorems 14–17) establish general equivariant relationships between matroid homology representations **over \(\mathbb C\)**; their formulas and examples do not determine this natural integral lattice's index. Even an exact rational character would not imply the abelian group \((\mathbb Z/4\mathbb Z)^3\). The computation is compatible with earlier same-complex work on minimal supports of integral cycles, which does not specify the canonical isotypic gluing lattice. Closely related topology of the Heawood incidence graph concerns different complexes.

## Limitations
This identifies the abelian group and index of the natural saturated-lattice gluing for one matroid and one group; it is not a classification of the full \(\mathbb Z[G]\)-module up to isomorphism or of equivariant stable homotopy type. The gluing quotient is not claimed to determine extensions for all matroids. Full publication priority cannot be established by a finite database and literature search; an unindexed equivalent calculation is possible. The finite exact script verifies the stated inputs and arithmetic but is not independent scholarly review.

## References
1. J. A. De Loera, J. Lee, S. Margulies, and J. Miller, *Weak Orientability of Matroids and Polynomial Equations*, arXiv:1309.7719v1 (first public 2013-09-30), Section 4. https://arxiv.org/abs/1309.7719
2. L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760 (first public 2020-01-11), particularly Section 4, Theorems 14–17. https://arxiv.org/abs/2001.03760
3. Supplementary exact reproducibility artifacts: `verify_fano.py`, `certificate.json`, and `verification_output.txt`.
