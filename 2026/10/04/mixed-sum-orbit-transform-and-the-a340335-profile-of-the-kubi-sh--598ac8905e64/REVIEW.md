# Independent mathematical audit

## correctness

PASS

By homogeneity, two injective ordered tuples are in the same automorphism orbit exactly when their coordinate-labelled induced finite substructures agree. Choosing which \(p\) coordinates lie on the left contributes \(\binom np\), the two internal structures contribute \(f_p g_{n-p}\), and the unrestricted bipartite cross relation contributes \(2^{p(n-p)}\). Every finite structure embeds in the Fraïssé limit, so the count is exact. For pure finite sets and finite linear orders, \(f_p=1\) and \(g_q=q!\), yielding the displayed closed form; formal rearrangement gives both OEIS exponential generating functions. Partitioning an arbitrary ordered tuple by its equality kernel gives the Stirling transform. A fresh computation reproduced \(1,2,7,43,441,7241,185233,7252337,429318529,38079107713,5026601726721\), matching OEIS A340335, and the actual frozen verifier was read.

## originality

PASS

Kubiś and Shelah define mixed sums, prove the Fraïssé/strong-amalgamation theorem, and single out the finite-set/linear-order example for its torsion-free automorphism group, but their full open text does not enumerate tuple orbits. OEIS A340335 already contains the sequence and both generating functions, but not the Kubiś-Shelah model-theoretic interpretation. A later source on the same one-side-ordered bipartite limit was inspected and did not state an orbit/profile or A340335 theorem. No source found implication-wise contained the general mixed-sum transform plus this identification.

## value

PASS

Orbit profiles are a canonical quantitative invariant of oligomorphic homogeneous structures. The theorem gives a reusable transform for an entire natural Fraïssé construction and identifies the precise profile of the torsion-free Kubiś-Shelah example with a pre-existing OEIS sequence. Although the derivation is short, the object and invariant are independently motivated and the formula packages exact information that is useful across mixed-sum examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
