# Long-lived coordinate-symmetric fixed persistence in binary hypercube Rips filtrations

## Finding
For every integer \(n\ge2\), consider the inclusive Hamming Vietoris–Rips filtration \(X_n(r)=\operatorname{VR}_{\le r}(\{0,1\}^n,d_H)\). Let \(\mathfrak S_n\) permute the coordinates and let \(F_n(r)=|X_n(r)|^{\mathfrak S_n}\) denote the **geometric fixed-point space**, not the invariant homology or a quotient space.

For integers \(0\le r<n\), set
\[
 d_n(r)=\left\lfloor\frac{\lfloor r/2\rfloor}{n-r}\right\rfloor.
\]
There is a simplicial collapse of a canonical PL triangulation of \(F_n(r)\) onto the boundary of a \((d_n(r)+1)\)-dimensional cross-polytope. In particular,
\[
 F_n(r)\simeq S^{d_n(r)}.
\]
For \(r\ge n\), the fixed space is a simplex and hence contractible. The same descriptions apply to nonnegative real scales by replacing \(r\) with \(\lfloor r\rfloor\) below \(n\).

More strongly, the **complete reduced integral persistent-homology barcode** is explicit. Put
\[
 b_{n,q}=\left\lceil\frac{2qn}{2q+1}\right\rceil \quad(q\ge0).
\]
For each \(q\ge0\) with \(b_{n,q}<b_{n,q+1}\), there is exactly one degree-\(q\) bar
\[
 [b_{n,q},b_{n,q+1}),
\]
and there are no other reduced bars. A coincident endpoint gives no bar. In unreduced homology there is one additional eternal degree-zero bar \([0,\infty)\). For example, \(n=30\) gives a degree-one bar \([20,24)\) of length four. These lengths are unbounded with \(n\), even though the ambient cube Rips filtration has nullhomotopic maps between distinct integer scales.

## Assumptions and scope
The parameter \(n\) is an integer at least two; the metric \(d_H\) is Hamming distance; a subset spans a simplex exactly when its diameter is at most \(r\). Homology has integral coefficients unless otherwise specified. Fixed points are taken in the **geometric realization** of the simplicial complex under the full coordinate-permutation action. No statement is made about the homotopy type of the ambient Rips complex beyond the cited prior results.

## Proof
**1. Exact fixed-point triangulation.** A point of the realization is fixed by all coordinate permutations if and only if its barycentric coordinates are constant on each vertex orbit in its supporting simplex. Thus its fixed realization is PL homeomorphic to the simplicial complex whose vertices are the barycenters of coordinate-permutation orbits whose entire union is a simplex, with simplices defined by unions of such orbits. The orbits on binary strings are the Hamming-weight layers \(O_w\), where \(0\le w\le n\).

The maximum Hamming distance between a word of weight \(a\) and one of weight \(b\) is
\[
 D(a,b)=\min(a+b,2n-a-b).
\]
Indeed, the minimum possible support intersection is \(\max(0,a+b-n)\). In particular the diameter of \(O_w\) is \(2\min(w,n-w)\).

Fix \(0\le r<n\) and put \(p=\lfloor r/2\rfloor\), \(m=p+1\), \(k=n-r\). The admissible weight orbits are exactly \(O_0,\ldots,O_p,O_{n-p},\ldots,O_n\). Label them \(L_i=O_i\), \(H_i=O_{n-i}\) for \(0\le i<m\). All pairs within either \(L\)-side or \(H\)-side are mutually compatible, since their maximum Hamming distance is at most \(2p\le r\). Cross-pairs satisfy
\[
 D(i,n-j)=n-|i-j|,
\]
so \(L_i\) and \(H_j\) are **incompatible** exactly when \(|i-j|<k\).

Consequently the canonical fixed-point triangulation is the independence complex \(K_{m,k}=\operatorname{Ind}(B_{m,k})\) of the bipartite graph with vertices \(L_0,\ldots,L_{m-1},H_0,\ldots,H_{m-1}\) and edges \(L_iH_j\) exactly when \(|i-j|<k\). This identification respects all scale inclusions.

**2. Integral collapse.** For a graph with distinct nonadjacent vertices \(u,v\) satisfying \(N(u)\subseteq N(v)\), the independence complex simplicially collapses onto the independence complex with \(v\) deleted: match faces containing \(v\) but not \(u\) with those obtained by adding \(u\). The corresponding vertex fold \(v\mapsto u\) is a simplicial retraction contiguous to the identity.

In \(B_{m,k}\), divide the indices \(0,\ldots,m-1\) into consecutive blocks of length \(k\), with a possibly shorter last block. For each block with first index \(a\), first delete all \(L_{a+i}\) with \(1\le i<k\) still in the block, using \(N(L_a)\subseteq N(L_{a+i})\). Next delete all \(H_{a+i}\) with the same range, using \(N(H_a)\subseteq N(H_{a+i})\) in the graph remaining after the first deletions. The asserted containments follow directly from \(|i-j|<k\), including for the short final block. Earlier blocks have already been deleted except for their anchors and introduce no edges to the current anchor pair. What remains is precisely a disjoint union of
\[
 t=\left\lceil\frac{m}{k}\right\rceil=d_n(r)+1
\]
independent edges \(L_{ak}H_{ak}\), with \(a=0,\ldots,t-1\). Thus
\[
 K_{m,k}\searrow\operatorname{Ind}(tK_2)
 =\underbrace{S^0*\cdots*S^0}_{t\text{ factors}}
 \cong S^{t-1}=S^{d_n(r)}.
\]
The collapse proves integral as well as homotopy statements; no inference from finite tests is involved. The fold retraction maps each \(L_i\) to \(L_{k\lfloor i/k\rfloor}\) and each \(H_i\) to \(H_{k\lfloor i/k\rfloor}\).

**3. Actual persistence maps.** For adjacent scales \(0\le r<n-1\), write \((m,k)\) and \((m',k')\) for the old and new parameters; then \(m'\ge m\), \(k'=k-1\). The old core consists of the antipodal pairs with indices \(0,k,2k,\ldots,d_n(r)k\). Under inclusion followed by the new fold retraction, these pairs go to indices
\[
 k'\left\lfloor\frac{ak}{k'}\right\rfloor,
 \qquad 0\le a\le d_n(r).
\]
Because \(k\ge k'\), their images are all distinct. If \(d_n(r+1)=d_n(r)\), there are exactly as many image pairs as new core pairs, so all the new pairs occur, in order. The induced map on the integral sphere fundamental class has degree \(+1\) (with the displayed compatible core order), hence is an isomorphism. If \(d_n(r+1)>d_n(r)\), the reduced homology in the old degree vanishes at the new stage, so the map is zero. The step into \(r=n\) is zero because the target is contractible. This proves all scale-inclusion maps.

Finally, for \(q\ge0\),
\[
 d_n(r)\ge q\iff\lfloor r/2\rfloor\ge q(n-r)
 \iff (2q+1)r\ge 2qn
 \iff r\ge b_{n,q}.
\]
Since the sphere dimension is nondecreasing, the degree-\(q\) plateau is exactly \([b_{n,q},b_{n,q+1})\), if nonempty. The integer-scale barcode follows; the real-scale barcode has the same endpoints. The final full simplex establishes the stated finite deaths.

## Verification
The standalone program `verify_symmetric_fixed_rips.py` independently enumerates 55 raw weight-orbit scale comparisons for dimensions up to ten, checks 400 dominated-vertex deletion sequences, computes reduced mod-two chain homology in 105 cases through dimension fourteen, and checks 4,950 adjacent-scale core maps plus all threshold inequalities through dimension one hundred. These tests all passed. They validate examples and implementation details, while the universal statements above follow from the displayed exact distance and fold arguments.

## Relationship to prior work
Galetto, Montaño and Wellner (first posted June 18, 2026) determine hyperoctahedral **ambient homology representations** at scales up to three and at the penultimate scale; these do not determine geometric fixed loci or their inclusion maps. Bendersky, Elia and Grbić (2026) study ambient connectivity and cohomology of hypercube Rips complexes, also without supplying the fixed-space classification above.

Adams and Virk (2024, Proposition 3.3) prove that successive **ambient** Rips inclusions are nullhomotopic, so ambient reduced persistence bars cannot span more than one unit of scale. Our fixed-point filtration has positive-degree intervals whose lengths grow linearly with \(n\). This is compatible: their homotopies do not preserve the full coordinate-permutation fixed locus. The new contribution is the exact all-scale geometric fixed-space collapse **and** its full integral persistence barcode, not a rederivation of any ambient homology results.

## Limitations
Only the full coordinate-symmetric fixed locus of binary Hamming cubes is classified, not fixed spaces for arbitrary subgroups, the ambient homotopy types at intermediate scales, or other alphabet sizes. The work is supported by an explicit proof and finite checks, but has not received independent mathematical validation. Possible unindexed equivalent work remains an originality risk. The fixed-point filtration is a different persistence module from the ambient one.

## References
1. Federico Galetto, Jonathan Montaño and Zoe Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first posted June 18, 2026), https://arxiv.org/abs/2606.20784.
2. Henry Adams and Žiga Virk, *Lower Bounds on the Homology of Vietoris–Rips Complexes of Hypercube Graphs*, Bulletin of the Malaysian Mathematical Sciences Society 47 (2024), article 72, Proposition 3.3, https://doi.org/10.1007/s40840-024-01663-x.
3. Martin Bendersky, Salvatore Elia and Jelena Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (2026), https://arxiv.org/abs/2605.00705.
