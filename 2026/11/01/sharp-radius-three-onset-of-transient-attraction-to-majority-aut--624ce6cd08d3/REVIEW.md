# Scientific review

## Correctness
PASS. The elementary ten-bit majority identities were reconstructed and directly checked; the all-length exponential predecessor count follows from a bijection between incoming cyclic configurations and closed phase-window graph walks. Its unique recurrent component has 17 vertices and 18 edges; the exact ten-step phase-zero return matrix has all four entries one, so the closed-walk trace is \(2^m\) for every positive integer \(m\). A standard-library program exhaustively builds the graphs and confirms the finite matrix certificates. The radius-one/two exclusion is conditional on the complete periodic-word classification explicitly attributed to Nakar–Ron and verified by their full text; given those forms, the independent predecessor-graph computation proves the exclusion for every admissible size.

## Originality
PASS, with residual historical risk. Nakar–Ron (2022, page 6) explicitly contains the periodic word templates, so these are not claimed as new. Liu–Chen (2002/2003, Section 4) studies radius-two attractor patterns but does not give the exact radius-three inverse-image law. Most importantly, Tosic–Agha (2004, Lemma 5, author-hosted full text) states the opposite universal no-incoming-transients property: the radius-three witness is a concrete counterexample, not its corollary. published-finding corpus searches for the exact ten-bit words, radius-three inverse-image exponential multiplicity, alias phrases about repelling/isolated two-cycles, and published related work found no equivalent theorem. The precise possible risk is an uncatalogued precursor computation or other correction of the 2004 lemma.

## Value
PASS. The exact minimum interaction radius at which oscillations become accessible from outside their cycles is a motivated dynamical boundary. The result gives explicit exponentially many incoming transient states on a natural increasing sequence of rings, and it corrects a published universal structural assertion. It is not solely a finite enumeration or a restatement of already classified periodic patterns.

## Scope and closest literature
Primary comparison: Tosic–Agha (2004), Lemma 5, pages 7–8, covers the same synchronous threshold mechanism but asserts no transient incoming states. Nakar–Ron (2022), Section 1.4, covers periodic configurations but not the claimed one-step inverse-image count. Liu–Chen (2002/2003), Section 4, analyzes infinite-radius-two attractors; its scope excludes this radius-three preimage multiplicity. Aledo–Martínez–Valverde (2015) is a general survey. All source inspections are characterized in `AUDIT.json`. The exact ten-bit result does not count the entire attraction basin at deeper transient times.

Self-review: passed. Independent audit: not yet performed.
