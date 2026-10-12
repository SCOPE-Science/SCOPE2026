# Full generalized Hamming hierarchy from induced subcomplex maxima
## Finding
Let \(q\) be prime and let \(\Delta\) be an abstract simplicial complex on the full vertex set \([k]\). Identify each face \(\sigma\) with its characteristic vector \(\chi_\sigma\in\mathbb F_q^k\), and let \(C_{\Delta}^{*}\) be the code obtained by evaluating \(u\cdot\chi_\sigma\) on the nonempty faces, as in Lorite López--Camazón Portela--López Ramos. For \(P\subseteq[k]\), define the induced subcomplex
\[
\Delta|_P=\{\sigma\in\Delta:\sigma\subseteq P\}.
\]
Then for every \(1\le r\le k\),
\[
d_r(C_{\Delta}^{*})=|\Delta|-\max_{\substack{P\subseteq[k]\\|P|=k-r}}|\Delta|_P|.
\]
Equivalently,
\[
d_r(C_{\Delta}^{*})=\min_{\substack{I\subseteq[k]\\|I|=r}}|\{\sigma\in\Delta:\sigma\cap I\ne\varnothing\}|.
\]
Every minimum is attained by the coordinate \(r\)-space supported on such an \(I\). Hence the complete generalized Hamming-weight hierarchy is independent of the prime \(q\). For \(r=1\), the formula is the source paper's vertex-link/minimum-distance formula.

## Assumptions and scope
The complex is on the full vertex set \([k]\), so every singleton \(\{i\}\) is a face. Consequently the nonzero face-characteristic matrix contains every standard basis vector, and the message map \(\mathbb F_q^k\to C_{\Delta}^{*}\) is injective. The result concerns the face-characteristic code \(C_{\Delta}^{*}\), not the complementary anticode. The field is prime because that is the standing hypothesis of the motivating 2026 construction; the proof itself uses only finite-field linear algebra and downward closure.

## Proof
Let
\[
D=\{\chi_\sigma:\sigma\in\Delta\}\subseteq\mathbb F_q^k,
\]
including \(0=\chi_\varnothing\). Because the message map is injective, every \(r\)-dimensional subcode is the image of a unique \(r\)-dimensional message subspace \(U\le\mathbb F_q^k\). A nonempty-face coordinate indexed by \(x\in D\setminus\{0\}\) vanishes on the whole subcode exactly when \(u\cdot x=0\) for every \(u\in U\), i.e. exactly when \(x\in U^\perp\). Therefore, with \(W=U^\perp\) and \(\dim W=k-r\),
\[
|\operatorname{Supp}(U)|=(|\Delta|-1)-|(D\setminus\{0\})\cap W|=|\Delta|-|D\cap W|.
\]
It remains to maximize \(|D\cap W|\) over \((k-r)\)-dimensional subspaces \(W\).

We use a sharp projection lemma. Let \(W\le\mathbb F_q^k\) have dimension \(d\). Some set \(P\subseteq[k]\) of \(d\) coordinate positions is an information set for \(W\), so coordinate projection \(\pi_P:W\to\mathbb F_q^P\) is injective. If \(\chi_\sigma\in D\cap W\), then
\[
\pi_P(\chi_\sigma)=\chi_{\sigma\cap P}.
\]
Since \(\Delta\) is downward closed, \(\sigma\cap P\in\Delta\). Thus \(\pi_P\) injects \(D\cap W\) into the characteristic vectors of \(\Delta|_P\), and
\[
|D\cap W|\le |\Delta|_P|.
\]
Taking the largest induced subcomplex over all \(|P|=d\) yields
\[
\max_{\dim W=d}|D\cap W|\le\max_{|P|=d}|\Delta|_P|.
\]
Equality is attained by the coordinate subspace \(W=\mathbb F_q^P\), because then \(D\cap W\) is exactly the characteristic-vector set of \(\Delta|_P\). Substituting \(d=k-r\) proves the first formula. Writing \(I=[k]\setminus P\) gives the second formula, since the faces not contained in \(P\) are precisely the faces meeting \(I\).

## Verification
The proof is symbolic and does not rely on numerical enumeration. The critical points were checked directly: the singleton columns make the message map injective; subcode support complements are exactly intersections with \(U^\perp\); an information set exists for every linear subspace; and deleting coordinates from a characteristic face vector corresponds to passing to a subface. The bound is sharp because every coordinate subspace is itself an admissible orthogonal complement.

Boundary checks agree with the construction. For \(r=1\), deleting one vertex complement gives the number of faces containing that vertex, recovering the published minimum-distance formula. For \(r=k\), \(P=\varnothing\), so \(|\Delta|_P|=1\) and \(d_k=|\Delta|-1\), the full code length.

## Relationship to prior work
Lorite López--Camazón Portela--López Ramos define the characteristic-face code for arbitrary simplicial complexes and prove that its minimum distance is obtained from a one-vertex message vector; they state the arbitrary-complex parameters as \([|\Delta|-1,k,\min_i|\operatorname{lk}_\Delta(i)|]\). The theorem above extends that result from the first generalized Hamming weight to the entire hierarchy.

Liu--Zheng--Lu--Wang study generalized Hamming weights for a related defining-set construction. Their primary preprint explicitly says that for a general simplicial complex the relevant maximum intersection is difficult to determine, and then determines complete hierarchies only in special cases. Their finite-field notion of simplicial complex is a union of coordinate subspaces; for \(q=2\) it overlaps the characteristic-vector setting. The information-set projection lemma above supplies a direct sharp maximum-intersection principle for the arbitrary characteristic-face complexes considered here, rather than an inclusion--exclusion calculation for a prescribed small or specially arranged set of maximal supports.

## Limitations
This result does not give a closed formula for the combinatorial optimization \(\max_{|P|=k-r}|\Delta|_P|\) beyond reducing it to induced subcomplexes of a fixed cardinality. It does not address generalized weights of the complementary anticode or how higher weights transform under the topological operations studied in the source. The literature comparison was focused on the source construction, the closely related complete-weight-hierarchy paper of Liu--Zheng--Lu--Wang, and general generalized-weight formulations; a differently phrased equivalent theorem elsewhere remains a residual bibliographic risk.

## References
1. A. J. Lorite López, D. Camazón Portela, J. A. López Ramos, “Linear codes arising from geometrical operations,” *AIMS Mathematics* 11(4) (2026), 10033–10048, DOI 10.3934/math.2026414.
2. C. Liu, D. Zheng, W. Lu, X. Wang, “The Weight Hierarchies of Linear Codes from Simplicial Complexes,” arXiv:2310.11873v1; later *Discrete Mathematics* 348(1) (2025), 114240, DOI 10.1016/j.disc.2024.114240.
