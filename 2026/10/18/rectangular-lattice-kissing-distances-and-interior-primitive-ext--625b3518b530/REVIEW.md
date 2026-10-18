# Scientific review: rectangular lattice kissing distances

## Correctness — PASS

The claim covers all positive integral side lengths and all pairs of disjoint lattice polytopes, including points and segments. The proof uses (a) the planar closest-face classification; (b) a nonzero integer determinant for parallel supporting lines and primitive edge directions; (c) an explicit modular inverse/Bézout point whose orthogonal projection is inside the corresponding lattice segment; and (d) divisibility barriers at the two sides of the exhibited infinite family. The two strict norm comparisons, \(88t-7>0\) and \(40t-7>0\), cover every boundary candidate. The code checks exact squared distances for all \(1\le a,b\le5\) and four instances of the infinite family. The infinite assertions rest on the proof, not the sample checks.

## Originality — PASS (residual risk disclosed)

The closest results are the cube-only problem and general bounds in Deza–Onn–Pokutta–Pournin, arXiv:2305.18597, and the exact square formula in Deza–Liu–Pournin, arXiv:2412.03479, Theorem 1.1, Section 3. They neither give a two-independent-side-length arithmetic characterization nor treat the infinite family where all maximizing primitive directions avoid the rectangle's full side bounds. Cubical results cannot imply Euclidean anisotropic-box minima by affine normalization: coordinate rescaling is not an isometry. Later dimension-three and flat-simplex papers have different parameter domains. Targeted literature and mathematical-record searches did not reveal an equivalent published rectangular statement. A prior unindexed lattice-geometric formulation remains possible.

## Value — PASS

This is the exact all-parameters version of a natural geometric separation invariant when the bounding cube is replaced by the canonical anisotropic integer box. In contrast with the known square case, the best primitive normal does not always reach a side-length bound. The proved infinite arithmetic family demonstrates that an algorithm searching only the extremal side slopes fails; the global optimum reduces instead to a finite gcd-controlled direction search rather than enumeration of all polygon pairs. This is a complete natural rectangular classification with an equality-contact condition, not a renamed square theorem.

## Reproducibility and limits

`rectangular_kissing_check.py` uses only Python 3 built-ins and checks finite cases by exact `fractions.Fraction` arithmetic. Complete binary-independent verification is not claimed. The equality-contact proof is intrinsic to the Euclidean integer-lattice setting; no arbitrary-lattice or dimension-three extension is claimed.

Self-review: passed. Independent audit: not yet performed.
