# Complete Bravais-crystal classification of frozen two-by-two hard-square hopping

## Finding

Consider square anchors \(p\in\mathbb Z^2\), each occupying \(p+\{0,1\}^2\); distinct squares cannot overlap. A legal elementary move replaces one anchor \(p\) by \(p+e\), where \(e\in\{(1,0),(-1,0),(0,1),(0,-1)\}\), provided the new square does not overlap any other square. A configuration is **frozen** when it admits no elementary move.

**Theorem.** Suppose the entire anchor set is \(t+L\), one coset of a full-rank sublattice \(L\le\mathbb Z^2\), and the occupied squares do not overlap. The configuration is frozen if and only if \(L\) is exactly one of the following five lattices, listed by generators:

\[
\begin{array}{c|c}
[\mathbb Z^2:L]&\text{generators of }L\\
4&(2,0),(0,2)\\
4&(2,1),(0,2)\\
4&(2,0),(1,2)\\
5&(2,1),(-1,2)\\
5&(2,-1),(1,2)
\end{array}
\]

They are pairwise distinct. In particular, the **lowest density among single-coset Bravais frozen configurations** is exactly \(1/5\). The two index-five lattices are the two congruence classes of period lattices \(x-2y\equiv0\pmod5\) and \(x+2y\equiv0\pmod5\), reflecting two opposite orientations.

**Finite-volume consequence.** On the torus \((\mathbb Z/N\mathbb Z)^2\), for every \(N\ge10\) divisible by \(10\), the two index-five lattices induce ten pairwise distinct frozen states, five translations per lattice, with \(N^2/5\) anchors each. A close-packed state has \(N^2/4\) anchors; hence these absorbing states are present at \(4/5\) of the maximum packing count. The conservative nearest-neighbor-jump Markov chain at \(N^2/5\) anchors is therefore reducible and has at least ten distinct absorbing point-mass stationary distributions, assuming every otherwise legal jump has a positive rate.

## Assumptions and scope

The hard-square footprint \(\{0,1\}^2\), infinite integer lattice, single-coset rank-two Bravais restriction, exclusion of overlapping occupied footprint sites, and elementary one-anchor coordinate-neighbor moves are essential. Finite tori use periodic hard-square footprints and the same allowed jumps. A Bravais density is \(1/[\mathbb Z^2:L]\). Frozen means no allowed jump, not no legal addition of another particle. No statement is made about arbitrary periodic or nonperiodic non-Bravais states, stochastic dynamical scaling limits, or thermodynamic entropy.

## Proof

1. **Hard-core packing index.** Distinct translates of the four-site footprint are disjoint. Inside large boxes, this gives square-anchor density at most \(1/4\). For a coset \(t+L\), its density is exactly \(1/d\), with \(d=[\mathbb Z^2:L]\). Thus \(d\ge4\).

2. **Exact directional blocking condition.** Move an anchor at the origin to \((1,0)\). Since the original arrangement is admissible, the move can create a collision only with an anchor whose displacement from the origin is \((2,a)\), where \(a\in\{-1,0,1\}\). (Potential differences between new and other anchors lie in \(\{-1,0,1\}^2\); subtract the displacement of the moved anchor and discard displacements already forbidden by original hard-core admissibility.) A move to \((-1,0)\) is blocked equivalently by \((-2,a)\), and the north/south analogue is \((b,\pm2)\) for \(b\in\{-1,0,1\}\). In a lattice, if \((2,a)\in L\), its negative blocks the opposite horizontal move; similarly \((b,2)\in L\) blocks both vertical moves. Therefore a Bravais state is frozen **exactly when** for some \(a,b\in\{-1,0,1\}\), both \(u=(2,a)\) and \(v=(b,2)\) lie in \(L\).

3. **Determinant squeeze.** The two blocking vectors are independent, with \(\lvert\det(u,v)\rvert=4-ab\in\{3,4,5\}\). Their span \(L_0\subseteq L\) has index \(4-ab\), so \(d=[\mathbb Z^2:L]\) divides \(4-ab\). Combining \(d\ge4\) with this divisibility forces \(d=4\) or \(5\), and in each case \(L=L_0\). For \(d=4\), \(ab=0\); replacing a generator by itself plus or minus the other shows there are just three distinct spans, displayed in the theorem. For \(d=5\), \(ab=-1\), leaving precisely the two displayed chiral spans. This proves necessity and exhaustiveness.

4. **Admissibility and sufficiency.** For \(L=\langle(2,0),(0,2)\rangle\), no nonzero lattice vector lies in \(\{-1,0,1\}^2\). For \(L=\langle(2,1),(0,2)\rangle\), the first coordinate of a lattice vector is even, and when it vanishes the second is even; hence the same exclusion holds. The transposed shear is identical by coordinate symmetry. For the index-five lattices, every lattice vector satisfies \(x\mp2y\equiv0\pmod5\). If \(x,y\in\{-1,0,1\}\), the congruence entails \(x\mp2y=0\), which implies \(x=y=0\). Thus all five lattices satisfy hard-core exclusion. Every one also contains the horizontal and vertical blocking vectors used above, hence is frozen.

5. **Torus consequence.** When \(10\mid N\), reduction modulo \(N\) preserves the five displayed lattices and their indices and exclusion relations; the local blocker vectors persist. Each of the two index-five lattices has five distinct cosets, and the two sets of cosets are disjoint because their period sublattices differ. Their ten torus configurations are therefore absorbing. A periodic even-even tiling attains the universal \(N^2/4\) hard-core packing upper bound. This yields the stated \(4/5\) ratio and reducibility.

## Verification

The accompanying standard-library Python script `verify.py` enumerates all sites of each of the five crystal types on compatible small tori, confirms the predicted anchor count, checks every nonzero short displacement for hard-core exclusion, and checks that every coordinate-neighbor move has a collision with a *different* anchor. The tests cover sizes \(4,8,12,20\) for index four and \(5,10,15,20\) for index five. The finite checks corroborate but do not replace the infinite-lattice determinant proof.

## Relationship to prior work

Berrens, Betz, Giesselmann and Walter (2026, arXiv:2610.21787v1) investigate hydrodynamic limits for finite-range exclusion processes, including two-dimensional hard-square footprints and conservative hops. The present theorem isolates a different finite-move structural question: the full list of one-coset Bravais configurations that have no outgoing moves. Jaleel and collaborators (arXiv:2108.01402) investigate the equilibrium two-nearest-neighbor hard-core lattice gas and computational sampling, but the material inspected did not present this lattice-determinant classification of frozen hopping crystals. Ramola and Dhar (arXiv:1204.4484) study a high-activity equilibrium expansion, not this kinetic classification. These scope distinctions are not a claim of exhaustive novelty proof.

## Limitations

The classification is only for **one coset of one rank-two sublattice**, not for all jammed configurations; other frozen configurations at lower densities are not excluded. The finite-volume consequence is established for square tori with \(10\mid N\), not all possible boundary conditions. Reducibility is a fixed-particle-number finite-state conclusion, not by itself a failure of a hydrodynamic limit under restricted initial-data hypotheses. An equivalent crystallographic statement in older or unindexed kinetic literature could reduce originality; no independent review has been performed.

## References

- Berrens, Betz, Giesselmann, Walter, *Hydrodynamic limits of finite range exclusion processes*, arXiv:2610.21787v1 (first public October 15, 2026), https://arxiv.org/html/2610.21787v1.
- Jaleel and collaborators, *Rejection-free cluster Wang-Landau algorithm for hard-core lattice gases*, arXiv:2108.01402, https://arxiv.org/pdf/2108.01402.
- Ramola and Dhar, *High-Activity Perturbation Expansion for the Hard Square Lattice Gas*, arXiv:1204.4484, https://arxiv.org/pdf/1204.4484.
