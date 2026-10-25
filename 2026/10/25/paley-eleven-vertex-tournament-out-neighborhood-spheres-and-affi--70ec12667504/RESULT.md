# The Paley eleven-vertex tournament has an out-neighborhood complex of twenty-one two-spheres

## Finding
Let \(P_{11}\) be the quadratic-residue tournament on \(\mathbb F_{11}\), with arcs \(x\to y\) exactly when \(y-x\in R=\{1,3,4,5,9\}\). Let \(X\) be its directed **out-neighborhood** simplicial complex: a nonempty subset is a face precisely when all of its vertices are out-neighbors of a common tournament vertex. Then
\[
X\simeq\bigvee^{21}S^2.
\]
The affine group \(G=\mathbb F_{11}\rtimes R\), of order \(55\), acts on \(X\) by \(x\mapsto ax+b\). Its complete rational reduced-homology representation is
\[
\widetilde H_2(X;\mathbb Q)\cong\mathbf 1\oplus2\,\operatorname{Aug}_{\mathbb Q}(\mathbb F_{11}),
\]
where \(\operatorname{Aug}_{\mathbb Q}(\mathbb F_{11})\) is the ten-dimensional augmentation subrepresentation of the natural permutation module on the eleven field elements. Its character is \(21\) at the identity, \(-1\) at every nonidentity translation, and \(1\) at each of the forty-four affine transformations whose multiplier differs from \(1\). Therefore \(\widetilde H_2(X/G;\mathbb Q)\cong\mathbb Q\), while all other reduced rational homology groups of the quotient vanish.

## Assumptions and scope
All complexes are finite abstract simplicial complexes, and the geometric realization is understood. In a directed graph, the out-neighborhood of \(x\) is \(N^+(x)=\{y:x\to y\}\); this **is not** the directed flag complex and is not the neighborhood complex of an undirected Paley graph. The eleven maximal simplices of \(X\) are the sets \(x+R\) for \(x\in\mathbb F_{11}\). Homology is reduced, with integer coefficients for the homotopy claim and rational coefficients for the representation. The group claim is for the canonical affine subgroup \(G\), without asserting it is the complete automorphism group.

## Proof
**(1) Canonical face construction.** Enumerate the eleven distinct five-element sets \(x+R\). Every nonempty face is exactly a nonempty subset of at least one such set. Enumerating these subsets with integer bit masks yields the face vector \((11,55,110,55,11)\) in dimensions zero through four. There are exactly \(242\) nonempty faces and \(715\) codimension-one incidences.

**(2) Integral homotopy certificate.** The accompanying `PALEY11_VERIFY.py` computes a matching on the complete nonempty-face poset. At each step it pairs a face with its unique remaining immediate coface when such a pair exists; otherwise it declares one maximal remaining face critical. The algorithm is specified entirely in the attached executable, including fixed pseudorandom seed \(0\). It produces \(110\) disjoint matched pairs, exactly one critical vertex and exactly twenty-one critical two-simplices, with no other critical cells. For **every** original face incidence, orient the Hasse edge upward except for matched edges, which are reversed. The verifier builds this entire directed graph and topologically sorts all \(242\) vertices, demonstrating that it is acyclic. Discrete Morse theory therefore yields a CW complex with one zero-cell, no one-cells, twenty-one two-cells, and no higher cells. Every two-cell has constant attaching map to the point, so this CW complex is a wedge of twenty-one two-spheres. In particular, the integral reduced homology is free of rank \(21\) in degree two and vanishes elsewhere.

**(3) Affine character.** Every \(x\mapsto ax+b\) with \(a\in R\) preserves the family of out-neighborhoods, and these transformations form the order-\(55\) semidirect product \(G\). The reduced simplicial Lefschetz number of \(g\) is the signed fixed-face sum, including the empty face with contribution \(-1\); a stable face of dimension \(d\) contributes \((-1)^d\) times the sign of its vertex permutation. For the identity this equals the reduced Euler characteristic \(21\). Every nonidentity translation is an eleven-cycle, and fixes no nonempty face (every face has at most five vertices), giving trace \(-1\). For \(a\ne1\), the affine map has one fixed vertex \(v\) and two orbits of size five. Its only nonempty fixed faces are the singleton \(\{v\}\) and the facet \(v+R\): the other five-orbit \(v+(-R)\) is not a facet and faces have size at most five. The five-cycle acts evenly on that facet, giving reduced Lefschetz number \(-1+1+1=1\). Since reduced homology is concentrated in degree two, these are the actual rational homology traces.

**(4) Representation and quotient.** The natural eleven-point permutation representation of \(G\) has character \((11,0,1)\) on the three element types above. Its augmentation module therefore has character \((10,-1,0)\). Thus the character \((21,-1,1)\) of \(\widetilde H_2(X;\mathbb Q)\) agrees with \(\mathbf1\oplus2\operatorname{Aug}_{\mathbb Q}(\mathbb F_{11})\). Character equality and complete reducibility in characteristic zero establish the module isomorphism. By finite-group averaging, rational homology of \(X/G\) is the invariant subspace; its degree-two dimension is \((21+10(-1)+44(1))/55=1\), with no other reduced homology.

## Verification
With Python 3.10 or later, run `python PALEY11_VERIFY.py` without third-party packages. This program reconstructs all \(242\) faces, tests the entire \(715\)-incidence directed Hasse graph for acyclicity, checks the Morse critical-cell vector, enumerates all \(55\) affine elements, and independently calculates signed traces from oriented fixed faces. The expected successful marker is `PALEY11_CERTIFICATE_PASSED`. Re-run from the provided source file rather than relying on a transcript.

## Relationship to prior work
Dochtermann and Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs* (first publicly posted 2021-08-24, arXiv:2108.10948), develop directed neighborhood complexes and identify their homotopy type through the Hom complex of a directed edge. Their discussion of tournaments and example computations does not supply the Paley eleven-vertex complex's exact integral homotopy type or the affine rational homology character. A six-vertex tournament out-neighborhood census and a torsion-freeness result through seven vertices concern strictly smaller orders. Results on Paley **undirected graph** neighborhoods or Paley tournament **directed flag** complexes concern different simplicial constructions. These differences do not by themselves prove absolute historical uniqueness.

## Limitations
The homotopy computation treats only this one canonical eleven-vertex tournament. The character classification is rational and refers only to the exhibited affine group, not to the integral group-ring lattice or every graph automorphism. The algorithm provides an exact finite certificate rather than a closed-form family theorem. No assertion of independent mathematical validation or priority over inaccessible and unindexed literature is made.

## References
1. Anton Dochtermann and Anurag Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948 (original version 2021-08-24), European Journal of Combinatorics 110 (2023), article 103704. https://arxiv.org/abs/2108.10948
2. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. DOI: 10.1006/aima.1997.1650.
3. `PALEY11_VERIFY.py`, accompanying standalone computational certificate, specifying the full finite complex, acyclic matching, and signed Lefschetz computations.
