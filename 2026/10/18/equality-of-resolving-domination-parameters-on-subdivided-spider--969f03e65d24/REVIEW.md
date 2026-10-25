# Independent mathematical audit

## correctness

PASS

For t>=3 arms ell_i>=2, the resolving-arm lemma reduces vertex and edge resolution to occupying t-1 arms. Vertex domination forces at least one selection on every arm; 3-step coverage plus center constraint yields U+eta. Center/first-depth exhaustive edge cases yield the three four-step ceilings; residue comparisons show equality iff every arm is 2 or 3 and some is 2. Independent all-subsets BFS and endpoint-min edge distances on (2,2,2),(2,3,4),(3,3,4),(2,5,6),(4,4,4) matched the pair of formulas. Unit arms and nonspiders excluded; finite tests are checks, not infinite proof.

## originality

PASS

Statement-level best-of-knowledge check: Potential alternative notation gamma_md and vertex-edge gamma_emd, and tree metric bases: searched aliases. Only tree general inequality prior; the precise spider equality and both formulas not implied. Existing tree inequality and general graph bounds cover a direction of comparison but cannot give modular formula or iff in spider subclass. Ikhlaq tree inequality gamma_emd<=gamma_md is consistent with, but does not force, exactly which arm tuples have equality.

## value

PASS

This addresses a published equality-classification question on a natural infinite tree class and gives a sharp iff, both exact parameters and an unbounded family of gaps; nontrivial coupling of arm resolution and domination, not a textbook restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
