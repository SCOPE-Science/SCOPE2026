# Mathematical review

## Correctness — PASS

The claim specifies a fixed origin-centered convex polyhedron, every vertex-avoiding central plane, and a separate Haar-a.s. consequence. In a generic section, vertices are precisely crossing edges. The radial-neighbor-pairing lemma explicitly handles wall crossings (including antipodal vertices sharing a wall), so it proves constancy on all generic orientation chambers. The exact coordinate reconstruction and 30 finite pairing checks are reproduced by the bundled Python program without a tolerance at any critical step. The independent Crofton computation uses 60 edges, endpoint radius \(\varphi\), length \(1\), central angle \(\pi/5\), and crossing probability \(1/5\), giving the constant \(12\). The checker ran to completion; finite simulations are corroboration only. A nongeneric plane is expressly excluded.

## Originality — PASS (historical priority provisional)

Brandenburg–De Loera–Meroni (2023), Theorem 1.1, identifies the edge sets within each slicing chamber and supplies general optimization algorithms. It does not prove that edge counts on **different** chambers agree for this solid. Reid (2016) describes the rectification and face vector, not its generic central-plane side-count rigidity. Published classifications for icosahedron sections and cuboctahedron sections are closely related but not the same assertion under a known implication or polarity. Exact object, claim aliases, paired-neighbor criterion and 12-side invariant were queried against accessible historical records, published-finding corpus and primary literature. No directly stronger or equivalent published theorem was verified. Classical geometric and stereological descriptions could nonetheless contain this property, so priority is not certified.

## Mathematical value — PASS

This is a natural **complete** classification of a topological invariant for every generic central section of a familiar non-zonohedral Archimedean solid; its 32 facets have two different side counts, yet all generic central sections unexpectedly have the same number of sides. The local radial-neighbor lemma explains the rigidity and supplies a reusable sufficient mechanism; the exact Crofton argument avoids brute-force enumeration of spherical orientation chambers. The result is not a slight numerical improvement or a special direction calculation.

## Closest sources and limitations

The closest inspected primary sources were arXiv:2304.14239v1 (all sections by chambers, not across-chamber side-count equality) and arXiv:1604.00580v1 (rectification geometry, not section rigidity). Some older specialist descriptions of Archimedean solids or stereological polyhedra could already state the same count; no novelty certificate is claimed. Nongeneric planes, off-center sections, other observables, and other solids are outside the theorem.

Self-review: passed. Independent audit: not yet performed.
