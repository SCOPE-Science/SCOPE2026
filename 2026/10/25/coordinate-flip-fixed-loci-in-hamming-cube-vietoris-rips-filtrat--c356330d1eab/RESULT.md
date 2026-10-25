# Coordinate-flip fixed loci in Hamming-cube Vietoris–Rips filtrations

## Finding
For every integer \(n\ge2\), every integer \(r\ge1\), and every coordinate \(i\in\{1,\ldots,n\}\), let \(\tau_i\) flip the \(i\)-th binary coordinate. There is a canonical piecewise-linear homeomorphism
\[
\Phi_{n,r,i}:\ |\operatorname{VR}_{\le r}(Q_{n-1})|\xrightarrow{\cong}|\operatorname{VR}_{\le r}(Q_n)|^{\tau_i}.
\]
It is compatible with the scale-inclusion maps for every integer \(r\ge1\) and equivariant for the signed permutations of the remaining coordinates.

In particular, for \(n\ge6\), the scale-four fixed space has the **integral homotopy type**
\[
|\operatorname{VR}_{\le4}(Q_n)|^{\tau_i}\simeq
\bigvee^{a_n}S^4\vee\bigvee^{b_n}S^7,
\qquad
 a_n=\sum_{j=4}^{n-2}2^{j-4}\binom j4,
\quad b_n=2^{n-5}\binom{n-1}{4}.
\]
Both multiplicities are positive; the smallest instance \(n=6\) has type \(S^4\vee\bigvee^{10} S^7\). The second statement combines the new homeomorphism with the **previously published** scale-three homotopy theorem of Feng; that earlier theorem is not claimed as new.

## Assumptions and scope
Let \(Q_n=\{0,1\}^n\) carry the Hamming distance \(d_n\). The *inclusive* Vietoris–Rips complex \(K_{n,r}=\operatorname{VR}_{\le r}(Q_n)\) consists of all subsets of diameter at most \(r\), with the standard geometric realization in the simplex on \(Q_n\). The involution \(\tau_i\) sends a bit string to the string differing only at position \(i\). Superscript \(\tau_i\) denotes **pointwise fixed points in the geometric realization**, not the subcomplex of individually fixed vertices (which is empty). The main homeomorphism requires \(n\ge2\), integral \(r\ge1\). No assertion at \(r=0\) is included: that fixed space is empty. No homotopy type of the ambient scale-four complex is claimed.

## Proof
**1. Orbit coordinates.** Identify \(Q_n\cong Q_{n-1}\times\{0,1\}\), with the last coordinate the chosen coordinate. The orbits of \(\tau_i\) on vertices are \(O_x=\{(x,0),(x,1)\}\), indexed by \(x\in Q_{n-1}\). Every orbit is an edge of \(K_{n,r}\), since its endpoints are at Hamming distance one and \(r\ge1\). Let \(m_x\) be the midpoint of the edge \(O_x\), expressed in the standard affine simplex as \((e_{(x,0)}+e_{(x,1)})/2\).

**2. Exact orbit-diameter criterion.** For distinct \(x,y\in Q_{n-1}\), the four cross-orbit distances are \(d_{n-1}(x,y)\) (twice) and \(d_{n-1}(x,y)+1\) (twice). The diameter of \(O_x\cup O_y\) is therefore \(d_{n-1}(x,y)+1\). Consequently, for every nonempty \(S\subseteq Q_{n-1}\), the union \(\bigcup_{x\in S}O_x\) is a simplex of \(K_{n,r}\) **if and only if** \(S\) is a simplex of \(K_{n-1,r-1}\). The singleton case uses \(r\ge1\).

**3. Geometric fixed points.** A point of \(|K_{n,r}|\) has unique barycentric coordinates \((\lambda_v)_{v\in Q_n}\) with support a face. It is fixed by \(\tau_i\) precisely when \(\lambda_{(x,0)}=\lambda_{(x,1)}\) for every \(x\). Its support is then a union of entire orbits. The correspondence
\[
\sum_{x\in S}t_x e_x\longmapsto \sum_{x\in S}t_x m_x,
\qquad t_x\ge0,\quad \sum_{x\in S}t_x=1,
\]
is thus defined exactly on the simplices of \(K_{n-1,r-1}\), is a continuous piecewise-linear bijection onto the fixed subspace, and has the continuous inverse \(t_x=2\lambda_{(x,0)}\). Compactness and the explicit affine inverse prove the claimed PL homeomorphism, including all boundaries and face intersections.

**4. Naturality.** The midpoint assignment does not depend on \(r\), so it intertwines \(K_{n-1,r-1}\subseteq K_{n-1,r}\) and \(|K_{n,r}|^{\tau_i}\subseteq|K_{n,r+1}|^{\tau_i}\). Each translation or permutation of the other coordinates sends \(m_x\) to \(m_{gx}\); hence \(\Phi_{n,r,i}\) is equivariant for the full hyperoctahedral group on those coordinates.

**5. Scale-four consequence.** Put \(m=n-1\ge5\) and \(r=4\). By the homeomorphism, the fixed space equals \(|\operatorname{VR}_{\le3}(Q_m)|\). Feng's Theorem 24 gives, for every \(m\ge5\), precisely \(2^{m-4}\binom m4\) seven-spheres and \(\sum_{j=4}^{m-1}2^{j-4}\binom j4\) four-spheres in an integral homotopy wedge. Substituting \(m=n-1\) proves the displayed scale-four classification; for \(n=6\), the multiplicities are \(1\) and \(10\).

## Verification
The included reproducible script `verify.py` uses two independent face predicates: it tests all pairs of orbit unions directly in the length-\(n\) cube, and compares every orbit-subset face against a separately evaluated Hamming-distance predicate in dimension \(n-1\). It exhausts all orbit subsets for \(2\le n\le5\) and all orbit pairs for \(2\le n\le6\), over every integer scale \(1\le r\le n\), covering 20 scale cases, 4,028 orbit-pair comparisons and 72,946 nonempty accepted faces in the exhaustive cases. It also checks the scale-four sphere-multiplicity formula for \(6\le n\le11\) and its \(n=6\) boundary. Recorded output is in `verify-output.txt`. These finite checks are supplementary: the unrestricted theorem follows from the proof above and Feng's published general theorem.

## Relationship to prior work
Feng (2023, Theorem 24) classified the ordinary, nonequivariant homotopy type of \(\operatorname{VR}_{\le3}(Q_m)\); the four- and seven-sphere counts are fully credited to that source. Adams and Virk (2024, Theorem 2.5 and Section 6.4) restated the result and identified the largely unresolved region of ambient scales at least four. Galetto, Montaño and Wellner (arXiv:2606.20784v1, 2026) determine hyperoctahedral homology representations at scales at most three and at the submaximal scale. Their full text focuses on homology modules of the **ambient** complex; it does not state an exact topological fixed-point homeomorphism for coordinate flips nor give the geometric fixed-space filtration at scale four. The present assertion concerns a different, naturally equivariant topological object: the fixed **locus** rather than the ambient homology representation. It should not be interpreted as an original derivation of Feng's counts or a solution to the ambient scale-four homotopy question.

## Limitations
The theorem concerns single-coordinate involutions, not simultaneous flips in several coordinates or general automorphisms. The identification does not compute the ambient homotopy type or the embedding-induced homology map of the fixed locus. The use of the existing scale-three theorem establishes the scale-four sphere formula only for \(n\ge6\). Published-priority checks are not a uniqueness guarantee; broader abstract equivariant simplicial techniques might recover the orbit-midpoint observation, though no explicit identical hypercube fixed-space classification was located.

## References
1. Federico Galetto, Jonathan Montaño, Zoe Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (first posted June 18, 2026), Sections 1, 4, 6–8; https://arxiv.org/abs/2606.20784.
2. Ziqin Feng, *Homotopy types of Vietoris-Rips complexes of Hypercube Graphs*, arXiv:2305.07084v1 (first posted May 11, 2023), Theorem 24; https://arxiv.org/abs/2305.07084.
3. Henry Adams and Žiga Virk, *Lower Bounds on the Homology of Vietoris–Rips Complexes of Hypercube Graphs*, Bulletin of the Malaysian Mathematical Sciences Society (2024), Theorem 2.5 and Section 6.4; DOI:10.1007/s40840-024-01663-x.
