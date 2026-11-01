# The complete persistent homology of anisotropic box offsets of cubical skeleta

## Finding
For positive vectors \(a,b\in(0,\infty)^d\), \(d\ge2\), and \(0\le k<d\), write
\[Q=\prod_{i=1}^d[-a_i,a_i],\quad K=\prod_{i=1}^d[-b_i,b_i],\quad X_\lambda=S_k(Q)+\lambda K\quad(\lambda\ge0),\]
where \(S_k(Q)\) is the union of all faces of \(Q\) of dimension at most \(k\). Define \(q(\lambda)=\#\{i:a_i/b_i>\lambda\}\). For integers \(q>k\), put
\[\beta(q,k)=\sum_{j=k+1}^{q}(-1)^{j-k-1}2^{q-j}\binom{q}{j},\qquad\beta(q,k)=0\ \text{if }q\le k.\]
Then \(X_\lambda\) is homotopy equivalent to the \(k\)-skeleton of the \(q(\lambda)\)-cube for \(q(\lambda)>k\), and is the entire convex outer box \(Q+\lambda K\) for \(q(\lambda)\le k\). For \(q>k\), the former has the homotopy type \(\bigvee^{\beta(q,k)}S^k\) when \(k\ge1\); for \(k=0\) it has \(\beta(q,0)+1=2^q\) components.

For every field \(\mathbb F\), all reduced persistent-homology maps \(\widetilde H_k(X_\lambda;\mathbb F)\to\widetilde H_k(X_\mu;\mathbb F)\), \(\lambda\le\mu\), are surjective. The only nonzero reduced degree is \(k\). If \(t\) is any distinct ratio among \(a_i/b_i\) and \(q_-:=\#\{i:a_i/b_i\ge t\}\), \(q_+:=\#\{i:a_i/b_i>t\}\), its barcode contains precisely \(\beta(q_-,k)-\beta(q_+,k)\) copies of the interval \([0,t)\). No other bars occur. The sharp scale at which \(X_\lambda\) is convex is the \((d-k)\)-th smallest coordinate ratio, including equality.

For instance, when \(d=4\) and \(k=1\), the reduced first Betti ranks at successive distinct critical ratios are \(17,5,1,0\); consequently the deaths have multiplicities \(12,4,1\) at the first three ratios. More precisely, the counts as the active coordinate number falls \(4\to3\to2\to1\) are \(17\to5\to1\to0\). Tied ratios combine their jumps.

## Assumptions and scope
The coordinate boxes are nondegenerate and axis-aligned in the same orthogonal coordinates. The offset uses Minkowski addition, not Euclidean-ball thickening. All ratios and thresholds are positive, and homology is reduced over an arbitrary field. The \(0\)-skeleton case uses reduced degree-zero persistence. No generic distinctness of the ratios is assumed; the convention is that a critical bar dies *at* its ratio, as intervals \([0,t)\).

## Proof
**1. A direct membership criterion.** For \(x\in\mathbb R^d\), the defining finite union of faces gives
\[x\in X_\lambda\iff |x_i|\le a_i+\lambda b_i\ (1\le i\le d)\text{ and }\#\{i:||x_i|-a_i|\le\lambda b_i\}\ge d-k.\]
Indeed, for the forward implication choose \(d-k\) coordinates fixed at an endpoint of a \(k\)-face. Conversely, if \(d-k\) coordinates are within the offset of one endpoint, fix those face coordinates at that endpoint; in every remaining coordinate choose the closest point of \([-a_i,a_i]\) to \(x_i\). The resulting face point is at coordinatewise box distance at most \(\lambda b_i\).

Put \(I_\lambda=\{i:a_i>\lambda b_i\}\), so \(|I_\lambda|=q(\lambda)\). For coordinates outside \(I_\lambda\), the two endpoint slabs overlap and their union covers the whole outer interval. Thus the criterion becomes
\[x\in X_\lambda\iff x\in Q+\lambda K\ \text{and}\ \#\{i\in I_\lambda:|x_i|\ge a_i-\lambda b_i\}\ge q(\lambda)-k.\tag{1}\]
If \(q(\lambda)\le k\), (1) imposes no restriction, so \(X_\lambda=Q+\lambda K\).

**2. Explicit homotopy equivalence.** Fix a scale where \(q=q(\lambda)>k\). For each active coordinate, apply the continuous saturation
\[x_i\longmapsto (a_i+\lambda b_i)\operatorname{clip}\left(\frac{x_i}{a_i-\lambda b_i},-1,1\right),\]
and linearly send each inactive coordinate to zero. The straight-line homotopy from the identity to this map stays within the outer box and preserves every active condition \(|x_i|\ge a_i-\lambda b_i\) that held at the starting point. Hence it stays in \(X_\lambda\). Its image is the rescaled \(k\)-skeleton of the active \(q\)-cube (with inactive coordinates fixed to zero). The same homotopy, restricted to this skeleton, stays in it, proving homotopy equivalence.

**3. Homology and homotopy of the skeleton.** The cubical \(q\)-cube has \(2^{q-j}\binom qj\) faces in dimension \(j\). Its \(k\)-skeleton, when \(q>k\), is \((k-1)\)-connected: the full cube is contractible and adjoining cells of dimension at least \(k+1\) does not change homotopy groups in degrees below \(k\). The only possible nonzero reduced homology is therefore degree \(k\), free abelian with rank \(\beta(q,k)\) by the Euler characteristic. For \(k\ge2\), standard cellular/Hurewicz–Whitehead arguments yield a wedge of \(k\)-spheres. The cases \(k=1\) (a connected graph) and \(k=0\) (vertices) follow directly.

**4. Exact persistence maps.** Fix \(\lambda\le\mu\). Every coordinate active at \(\mu\) was active at \(\lambda\). On these surviving coordinates, the two saturation maps take the values \(\operatorname{clip}(x_i/(a_i-\lambda b_i),-1,1)\) and \(\operatorname{clip}(x_i/(a_i-\mu b_i),-1,1)\). The straight-line interpolation between these two normalized values lies in the smaller active-cube \(k\)-skeleton: at least \(q(\mu)-k\) surviving coordinates were already endpoint coordinates at scale \(\lambda\), and both saturation values in such coordinates are identical signs \(\pm1\). Thus, after the homotopy equivalences in step 2, the inclusion-induced map is the coordinate-deletion projection from the \(q(\lambda)\)-cube \(k\)-skeleton to the \(q(\mu)\)-cube \(k\)-skeleton. That projection is well defined, since deleting \(m\) coordinates removes at most \(m\) forced endpoints, and it has a continuous right inverse: append fixed \(+1\) values in all deleted coordinates. It is therefore surjective on homology. When the target active count is at most \(k\), its reduced homology vanishes and surjectivity is automatic.

**5. Barcodes and the exact convexification scale.** The filtration starts with all \(d\) coordinates active, has no births in positive scale because every reduced persistence map is surjective, and has rank \(\beta(q(\lambda),k)\) at each scale. Over a field, the interval decomposition of a finite-jump persistence module therefore consists of the stated \([0,t)\) bars with multiplicities equal to successive rank drops. The equality-time convention follows from \(I_t=\{i:a_i>tb_i\}\). Since the outer box is the convex hull of \(X_\lambda\), convexity is equivalent to equality with the outer box, which by (1) occurs precisely when \(q(\lambda)\le k\). This first happens at the \((d-k)\)-th smallest ratio. For \(q>k\), an interior point of the outer box with all active coordinates zero violates (1), so the failure of convexity is strict. \(\square\)

## Verification
Run `python verify.py` with Python 3 and no additional packages. The program checks cubical homology ranks over \(\mathbb F_2\) against the closed formula through dimension six, and independently tests the face-union/slab-count/active-count membership identities on exact rational grids in dimensions two to four. The checked run passed 48,479 assertions. The general statement, including field independence and all scales, is established by the proof above; finite computations are not a substitute for that proof.

## Relationship to prior work
Meyer, *Finite convexification by Minkowski summation* (arXiv:2610.26744, first submitted October 19, 2026), characterizes when Minkowski addition by a convex body eventually convexifies a compact set, using exposed faces and covering radii. The present calculation specializes to a natural explicit cubical family but determines its **entire anisotropic persistent homology and every exact critical scale**, rather than only the eventual-convexity condition. Dłotko–Wanner, *Rigorous cubical approximation and persistent homology of continuous functions* (arXiv:1610.03833), gives general methods for cubical persistent-homology computation, without this box-skeleton formula. An indexed record entitled *Sharp finite convexification thresholds for every skeleton of a simplex* concerns repeated equal-weight Minkowski sums of simplex skeletons, not external box-offset filtration of cubical skeletons; the statements do not imply each other. That latter record was compared from its indexed summary; the complete item was not accessible, leaving some priority uncertainty.

## Limitations
The derivation assumes aligned boxes and a cubical skeleton; it does not describe arbitrary polytopes or Euclidean-ball offsets. It establishes algebraic barcodes over fields and homotopy types at individual scales, not a coherent filtered homotopy equivalence or persistent homotopy groups. A search cannot prove historical novelty, and unindexed equivalent special-case results remain possible. No independent mathematical audit has been performed.

## References
- Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744 (v1, October 19, 2026), https://arxiv.org/html/2610.26744v1.
- Paweł Dłotko and Thomas Wanner, *Rigorous cubical approximation and persistent homology of continuous functions*, arXiv:1610.03833, https://arxiv.org/html/1610.03833v1.
- Indexed mathematical research record, *Sharp finite convexification thresholds for every skeleton of a simplex*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-finite-convexification-thresholds-for-every-skeleton-of-a--92b027220722 (record summary compared; full text unavailable).
