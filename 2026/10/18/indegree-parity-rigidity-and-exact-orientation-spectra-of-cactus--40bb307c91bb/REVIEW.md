# Independent mathematical audit

## correctness

PASS

Indegree-parity variation is the F_2 unoriented incidence map of the set of reversed edges: each edge toggles two endpoints. Its rank on a connected graph is |V|-1, so exactly 2^{|V|-1} signatures are feasible and every fibre has 2^{|E|-|V|+1} orientations. Cactus simple cycles are edge-disjoint and span the cycle space; reversing each whole cycle leaves coherent directedness of it unchanged and leaves other cycles fixed, so every fibre has a constant number of directed cycles. In any noncactus a theta subgraph with three internally disjoint u-v paths exists. Direct all three paths u-to-v (acyclic), extend by topological order, then reverse two paths, which preserves parity but creates a directed cycle with the third path. For cacti, orientation count is 2^b product_i(2^{ell_i}-2+2z); division by the 2^c-element fibre yields P_G(z)=2^b product_i(2^{ell_i-1}-1+z). P_G(1)=2^{|V|-1}. The singleton and trees satisfy empty-product conventions. A fresh independent exhaustive verifier confirmed the iff and polynomial for all 772 labeled connected simple graphs on up to five vertices (399 cacti, 373 noncacti). Finite checks cannot replace the unrestricted proof.

## originality

PASS

No identified primary theorem or published mathematical record covered the complete cactus fibre-rigidity iff together with its exact parity-signature polynomial. Classical parity feasibility and cactus cycle-block factorization are credited. Originality is best-of-knowledge with explicit alternate-terminology risk.

## value

PASS

This is a motivated classification of a natural invariance property for graph orientations, identifying exactly the connected simple graphs where indegree parity makes acyclicity uniform within each fibre. Theta subgraphs provide a sharp structural obstruction, and the all-cycle coefficient product enumerates feasible target signatures by forced directed-cycle count for arbitrarily many cactus cycles. Existence of an acyclic target or classical coset size alone does not answer this question. Its short graph-theoretic proof does not make the precise invariant a routine normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
