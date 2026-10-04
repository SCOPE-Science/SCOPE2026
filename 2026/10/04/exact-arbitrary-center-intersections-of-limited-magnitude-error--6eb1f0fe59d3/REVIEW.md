# Same-model review

## Correctness
**PASS.** Translating the centers reduces a common output to one coordinate choice \(e_i\in[-k_-,k_+]\cap(d_i+[-k_-,k_+])\). The three possible support-cost types at a nonzero displacement coordinate are exactly \((1,0)\), \((0,1)\), and \((1,1)\), with counts \(\alpha_s\), \(\beta_s\), and \(\gamma_s\). At zero displacement the types are \((0,0)\) once and \((1,1)\) exactly \(K\) times. Product enumeration followed by truncation at support \(t\) is therefore bijective. The direct finite verifier independently agrees with the formula throughout its exhaustive grid and checks the one-coordinate corollary and global maximum.

## Originality
**PASS.** The closest primary source defines the same pair-intersection quantity, proves its global maximum over all centers, and gives distance-based upper and lower bounds for general pairs. Statement-level inspection did not find an exact arbitrary-displacement product formula. Related limited-magnitude tiling papers concern packing/tiling structure rather than exact pairwise intersections. Targeted published-result searches under intersection, preimage, generating-function, displacement, reconstruction, and limited-magnitude aliases returned no claim implying this formula. A residual risk remains that an unindexed note, thesis, or implicit generating-function reformulation contains the same elementary factorization.

## Value
**PASS.** Pairwise ball intersection is the ambiguity quantity controlling the number of reads needed for reconstruction. Replacing only distance-based bounds by an exact arbitrary-pair law yields a complete instance-level invariant and a direct \(O(nt^2)\) evaluator. The result is all-parameter and structural, not a finite census. Its value is exact ambiguity evaluation rather than a claimed improvement in asymptotic code density.

## Closest literature and limitations
The 2022 reconstruction paper is the direct comparison: its unit-displacement extremal formula is recovered as a special case, while its general-pair treatment supplies bounds rather than this full signed-displacement enumerator. The tiling literature is adjacent but does not dominate the claim. The main residual originality risk is differently phrased or unindexed prior enumeration.

Same-model review: passed. Independent audit: not yet performed.
