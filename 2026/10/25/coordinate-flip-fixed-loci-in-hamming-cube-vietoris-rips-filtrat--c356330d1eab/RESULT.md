# Coordinate-flip fixed loci in Hamming-cube Vietoris–Rips filtrations

## Finding

For every integer \(n\ge2\), integer \(r\ge1\), and coordinate \(i\in\{1,\ldots,n\}\), the geometric fixed-point set of the \(i\)-th coordinate flip on the inclusive Vietoris–Rips complex of the Boolean Hamming cube admits a canonical piecewise-linear homeomorphism
\[
\boxed{\Phi_{n,r,i}:\ |\operatorname{VR}_{\le r-1}(Q_{n-1})|\ \xrightarrow{\cong}\ |\operatorname{VR}_{\le r}(Q_n)|^{\tau_i}.}
\]
The **scale decreases by one**, not zero. The homeomorphism commutes with scale-inclusion maps and is equivariant under signed permutations of all remaining coordinates.

For \(n\ge6\), its scale-four consequence, using Feng's previously established scale-three homotopy theorem, is the integral homotopy equivalence
\[
|\operatorname{VR}_{\le4}(Q_n)|^{\tau_i}\simeq
\bigvee^{a_n}S^4\vee\bigvee^{b_n}S^7,
\quad a_n=\sum_{j=4}^{n-2}2^{j-4}\binom j4,
\quad b_n=2^{n-5}\binom{n-1}4.
\]
Thus at \(n=6\) the fixed space has type \(S^4\vee\bigvee^{10}S^7\). The sphere multiplicities are not claimed as a new computation of the ambient scale-three complex: they are exactly the credited values from Feng after this geometric identification.

## Assumptions and scope

Write \(Q_n=\{0,1\}^n\) with Hamming metric \(d_n\). For integer \(r\ge0\), \(\operatorname{VR}_{\le r}(Q_n)\) is the finite abstract simplicial complex whose faces are the nonempty subsets of pairwise Hamming distance at most \(r\); its geometric realization sits in the usual coordinate simplex on \(Q_n\). The map \(\tau_i\) flips only the \(i\)-th bit. Superscript \(\tau_i\) means **pointwise fixed points in the geometric realization**, not the subcomplex of individually fixed vertices, which is empty. The PL theorem requires \(n\ge2\) and \(r\ge1\). For \(r=0\) the fixed space is empty and no map from a negative scale is asserted. The ambient scale-four homotopy type and the fixed-locus inclusion-induced homology map are not determined here.

## Proof

**1. Vertex orbits.** Put the flipped bit last, identifying \(Q_n=Q_{n-1}\times\{0,1\}\). The involution has free vertex orbits \(O_x=\{(x,0),(x,1)\}\), one for each \(x\in Q_{n-1}\). For \(r\ge1\), the two vertices of each orbit span an edge. Denote the midpoint of that edge in the standard simplex realization by \(m_x=(e_{(x,0)}+e_{(x,1)})/2\).

**2. Exact orbit-union face condition.** If \(x\ne y\), the four distances between \(O_x\) and \(O_y\) comprise two occurrences of \(d_{n-1}(x,y)\) and two of \(d_{n-1}(x,y)+1\). The diameter of the union of any nonempty family of entire orbits is therefore \(1+\max_{x,y\in S}d_{n-1}(x,y)\), taking the maximum for a singleton to be zero. Thus
\[
\bigcup_{x\in S}O_x\text{ is a face of }\operatorname{VR}_{\le r}(Q_n)
\quad\Longleftrightarrow\quad
S\text{ is a face of }\operatorname{VR}_{\le r-1}(Q_{n-1}).
\]
In particular, it is **not** equivalent to the radius-\(r\) face condition in dimension \(n-1\).

**3. Pointwise geometric fixed points.** Every point of the realization of a finite complex has unique barycentric coordinates \(\lambda_v\), with positive support contained in a simplex. It is fixed by \(\tau_i\) if and only if \(\lambda_{(x,0)}=\lambda_{(x,1)}\) for each \(x\), hence its support is a disjoint union of whole vertex orbits. The preceding face criterion says that precisely the faces of \(\operatorname{VR}_{\le r-1}(Q_{n-1})\) arise. The affine map
\[
\sum_{x\in S}t_xe_x\longmapsto\sum_{x\in S}t_xm_x,
\qquad t_x\ge0,\quad\sum_xt_x=1,
\]
is consequently a continuous piecewise-linear bijection from the smaller complex realization onto the fixed subspace. Its inverse is explicitly \(t_x=2\lambda_{(x,0)}\), so it is a PL homeomorphism respecting all face intersections and boundary strata.

**4. Naturality and remaining symmetries.** The barycenters \(m_x\) do not depend on the scale. Increasing \(r\) by one on the right corresponds to increasing \(r-1\) by one on the left, so the maps commute with the inclusions of the two filtrations. Every signed permutation of the unflipped coordinates sends \(O_x\) to \(O_{gx}\) and \(m_x\) to \(m_{gx}\). This proves residual equivariance.

**5. The scale-four homotopy consequence.** For \(r=4\), put \(m=n-1\). The homeomorphism gives the exact fixed space \(|\operatorname{VR}_{\le3}(Q_m)|\). Feng's published Theorem 24 establishes for every \(m\ge5\) an integral homotopy wedge with \(\sum_{j=4}^{m-1}2^{j-4}\binom j4\) four-spheres and \(2^{m-4}\binom m4\) seven-spheres. Substitute \(m=n-1\) to obtain the displayed formula. At \(n=6\), it yields \(a_6=1\) and \(b_6=10\).

**6. Boundary check and necessary correction.** The one-unit radius loss is essential, not a harmless notation change. At \(n=2,r=1\), the fixed set on the right consists of two isolated orbit-edge midpoints, whereas \(|\operatorname{VR}_{\le1}(Q_1)|\) is a connected interval. These spaces are not homeomorphic. The correct source is \(|\operatorname{VR}_{\le0}(Q_1)|\), two discrete points, as the theorem states. All statements and implications above use the corrected radius \(r-1\).

## Verification and its limits

The existing standalone `verify.py` reconstructs the orbit-union face predicate directly in the \(n\)-cube and compares it with the scale-\(r-1\) predicate in dimension \(n-1\). It exhaustively tests all orbit subsets for \(2\le n\le5\), all orbit pairs through \(n=6\), and every positive integer scale up to \(n\). It also instantiates Feng's previously proved homotopy multiplicities for \(6\le n\le11\). These finite checks corroborate normalization and the essential scale shift. The unrestricted result follows from the preceding exact orbit-coordinate argument and the cited general theorem, not extrapolation from finite tests.

## Relationship to prior work

Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs* (arXiv:2305.07084, 2023), Theorem 24, proved the nonequivariant \(r=3\) sphere-wedge classification; every numerical sphere count used here comes from that source. Adams and Virk, *Lower Bounds on the Homology of Vietoris–Rips Complexes of Hypercube Graphs* (2024), discuss the ambient homotopy problem at larger scales. Galetto, Montaño, and Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions* (arXiv:2606.20784, 2026), compute representations of ambient homology, which are not in general the homology or homotopy type of pointwise geometric fixed loci. The generic orbit-barycenter principle for finite simplicial actions is elementary and is not claimed as new; the explicit dimension/scale reduction, naturality, and application to this fixed-locus filtration are the particular results evaluated here. Relevant general equivariant-topology literature may subsume this reduction, so literature priority is not exhaustive.

## Limitations

The homeomorphism applies to a **single** coordinate flip, not arbitrary simultaneous flips or general cube automorphisms. No claim is made at scale zero, about the ambient \(r=4\) homotopy type, or about inclusion-induced maps from the fixed space into the ambient complex. The scale-four formula is obtained from the previously published scale-three theorem and is valid for \(n\ge6\). Numerical checks do not substitute for the all-parameter proof. A literature search cannot certify historical priority beyond the materially inspected sources.

## References

1. Ziqin Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs*, arXiv:2305.07084 (2023), Theorem 24. https://arxiv.org/abs/2305.07084.
2. Henry Adams and Žiga Virk, *Lower Bounds on the Homology of Vietoris–Rips Complexes of Hypercube Graphs*, *Bulletin of the Malaysian Mathematical Sciences Society* (2024), DOI:10.1007/s40840-024-01663-x.
3. Federico Galetto, Jonathan Montaño, and Zoe Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (2026). https://arxiv.org/abs/2606.20784.
