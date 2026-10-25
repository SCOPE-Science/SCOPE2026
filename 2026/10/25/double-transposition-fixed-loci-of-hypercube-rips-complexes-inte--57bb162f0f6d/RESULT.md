# Double-transposition fixed loci of hypercube Rips complexes: integral homotopy and dimensional retractions

## Finding

Let \(Q_n=\{0,1\}^n\) with Hamming metric, \(n\ge4\), and let \(\sigma\) simultaneously interchange coordinates \(1\leftrightarrow2\) and \(3\leftrightarrow4\), fixing all others. Write \(F_n=|\operatorname{VR}_{\le 2}(Q_n)|^{\langle\sigma\rangle}\) for the **geometric** fixed-point subspace of the inclusive Vietoris–Rips complex at scale two. Then the following integral homotopy classifications hold:

\[
F_4\simeq S^1,\qquad
F_5\simeq S^1\vee\bigvee^{4} S^2,\qquad
F_6\simeq S^1\vee\bigvee^{20} S^2.
\]

The next dimension has a genuinely new integral homology degree:

\[
\pi_1(F_7)\cong\mathbb Z,\qquad
\widetilde H_i(F_7;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=1,\\
\mathbb Z^{68},&i=2,\\
\mathbb Z^4,&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]

Moreover, for each \(n\ge k\ge4\), there is a topological retraction \(F_n\to F_k\) with a section. Consequently, for all \(n\ge7\), the groups \(H_1(F_n;\mathbb Z)\), \(H_2(F_n;\mathbb Z)\), and \(H_3(F_n;\mathbb Z)\) have split free-abelian summands of respective ranks \(1,68,4\). In particular, \(F_n\) is not simply connected for any \(n\ge4\). These are topological fixed-point results, not a calculation of invariant subspaces in the ambient homology representation.

## Assumptions and scope

The geometric realization uses the ordinary finite abstract simplicial complex whose simplices are finite subsets of \(Q_n\) with pairwise Hamming distance at most two. The involution acts simplicially by permuting bit coordinates. The fixed-point space consists of the points fixed in the geometric realization, and is not the fixed-vertex subcomplex. All assertions use integral coefficients unless another ring is stated. For \(n=7\) no full wedge-of-spheres homotopy decomposition is claimed. For \(n>7\) only the explicit split summand bounds, not the full homology or homotopy type, are asserted.

## Proof

**Orbit-barycenter model.** Each geometric point of an invariant simplex is fixed by \(\sigma\) precisely when its barycentric coordinates are constant along every \(\sigma\)-orbit of vertices. Hence \(F_n\) is canonically piecewise-linearly homeomorphic to a simplicial complex \(L_n\) whose vertices are the orbits \(O\subseteq Q_n\) having Hamming diameter at most two, and whose simplices consist exactly of orbit families with union of Hamming diameter at most two. Distinct eligible orbits \(O,O'\) are adjacent precisely when every pair in \(O\times O'\) is at distance at most two. Because this condition is pairwise, \(L_n\) is the flag complex of its orbit-compatibility graph.

For a bit word \(x\), the involution changes the first pair of coordinates if and only if those two bits differ, and likewise the second pair. An orbit has diameter at most two exactly when at most one of those pairs differs. Twelve of the sixteen four-bit prefixes participate in eligible orbits: the four prefixes with equal bits in both pairs each give a singleton orbit, and the eight prefixes having one unequal pair give four two-element orbits. Thus the eligible orbit count is exactly \(8\cdot2^{n-4}\). For orbits represented by four-bit prefixes \(a,b\) and tails \(u,v\), their maximum union cross-distance is the maximum prefix cross-distance plus the Hamming distance between tails. This gives an explicit complete integer predicate for each edge of \(L_n\).

**Finite exhaustive certificate.** The accompanying standard-library program `verify_double_swap.py` constructs the eligible orbits from the original coordinate involution (independently checks the prefix/tail distance formula), enumerates all maximal orbit-compatibility cliques and their complete nonempty face sets, and constructs a deterministic matching on the simplicial face poset: for every orbit index in increasing order, it pairs each still-unmatched face without that index to the corresponding coface with the index, whenever both are still unmatched. Each pair is a genuine codimension-one incidence. The program exhaustively orients all Hasse incidences downward except matched incidences upward, and topologically sorts this directed graph; every sort exhausts all faces, proving the matching acyclic. The matched incidence coefficients in the integral oriented simplicial boundary matrices are all units \(\pm1\). Their elimination gives the exact integral cellular Morse boundary. The executable recursively eliminates every matched lower simplex using its matched upper simplex's signed boundary; for every critical cell in each positive degree, it verifies the final integral boundary is zero. These are exhaustive checks on the precisely specified finite complexes, not samples of an infinite family.

The exhaustive face-vector/critical-cell/matched-pair certificates, respectively, are

\[
\begin{array}{c|c|c|c}
n&\text{nonempty face vector}&\text{critical cells by dimension}&\text{matched pairs}\\\hline
4&(8,16,8)&(1,1)&15\\
5&(16,52,48,8)&(1,1,4)&59\\
6&(32,152,208,84,16)&(1,1,20)&235\\
7&(64,416,768,512,192,32)&(1,1,68,4)&955
\end{array}
\]

The respective directed Hasse-graph incidence counts are \(56,280,1344,6336\). The **zero integral Morse differential** and the cell counts give the asserted integral homology in all four dimensions. The single critical zero-cell makes each complex path connected. The CW models for \(n=4,5,6\) contain exactly one zero-cell, one one-cell and respectively zero, four, or twenty two-cells. Since each two-cell has zero attaching degree on the unique one-cell, its attaching loop is nullhomotopic in the circle; this identifies the asserted integral homotopy wedges. The \(n=7\) CW model has one one-cell and 68 two-cells with trivial attaching degrees, so its fundamental group is \(\mathbb Z\); the four additional three-cells may have nontrivial higher attaching maps, which is why a stronger homotopy claim is withheld.

**Retraction for all larger cubes.** For any \(n\ge k\ge4\), truncating to the first \(k\) bit coordinates is a \(1\)-Lipschitz, \(\sigma\)-equivariant map \(Q_n\to Q_k\). Appending \(n-k\) zero coordinates is an equivariant isometric section. Both induce simplicial maps on inclusive scale-two Rips complexes; their composition on \(Q_k\) is the identity. Restricting their geometric realizations to the fixed-point spaces therefore gives a continuous retraction \(F_n\to F_k\) with section. Homology induced by the section is split injective in every degree. This proves the stable lower bounds, and the split injection on fundamental groups from \(F_4\) prevents simple connectivity.

## Verification

Run `python3 verify_double_swap.py` in the extracted package directory. The checker uses only the Python standard library and terminates with `VERIFY_OK integral_morse=zero acyclic=all raw_orbits=all mod2=all`. It reconstructs every one of the \(4\)- through \(7\)-cube orbit complexes and all signed boundaries. A separate mod-two Gaussian-elimination computation directly on the original simplicial boundary matrices confirms the homology ranks; this is independent of the integral Morse boundary elimination. The verified critical vectors are \((1,1)\), \((1,1,4)\), \((1,1,20)\) and \((1,1,68,4)\).

## Relationship to prior work

Galetto, Montaño and Wellner (arXiv:2606.20784, first publicly available June 18, 2026) study homology representations under hypercube symmetries, including the ambient scale-two Rips complex. Their character formulas describe how a symmetry acts on ambient homology; a geometric fixed-point subspace is a different construction and cannot be recovered solely by taking invariant homology. Bendersky, Elia and Grbić (arXiv:2605.00705) study the ambient hypercube Rips cohomology, and Adamaszek and Adams (arXiv:2103.01040) develop ambient hypercube Rips homotopy types. None of those inspected statements classifies this simultaneous double-coordinate-swap geometric fixed locus. Single-coordinate swaps and pure bit translations also define different involutions. Search non-detection is not a proof of mathematical priority.

## Limitations

The finite integral homotopy classifications are proved only for \(n\in\{4,5,6\}\); at \(n=7\) the exact integral homology and fundamental group are proved, but not a three-dimensional wedge decomposition. For \(n\ge8\), retractions supply split summands and do not establish all Betti numbers. The method uses integer Hamming scale two and the specified double-transposition involution. Unindexed or inaccessible equivalent prior work remains possible; no independent scientific review or external certification has been performed.

## References

- Galetto, F.; Montaño, C.; Wellner, A., *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first posted 2026-06-18).
- Bendersky, M.; Elia, S.; Grbić, J., *Cohomological properties of the Vietoris-Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (first posted 2026-05-01).
- Adamaszek, M.; Adams, H., *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (2021).
