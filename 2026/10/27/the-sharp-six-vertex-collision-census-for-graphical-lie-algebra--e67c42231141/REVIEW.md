# Research review

## Correctness — PASS

The previously known support-rank formula is re-derived from the edge-bracket equations over an arbitrary field. The new claim is a finite *complete* graph-isomorphism census: `verify.py` iterates every labeled graph on up to six vertices and computes every orbit under the full symmetric group, then compares exact coefficient dictionaries of the formal polynomial. It verifies 156 six-vertex isomorphism classes, 149 distinct rank polynomials, and precisely seven doubleton collisions, with none on smaller orders. A concrete nonisomorphic witness is certified by different triangle-intersection patterns, and all its rank multiplicities agree in exact field-matrix computations for prime fields of sizes 2, 3, and 5. The nonisomorphic-Lie-algebra conclusion in odd characteristic follows from Mainkar's published reconstruction theorem.

## Originality — PASS, with bounded residual risk

Rossmann's prior Equation (1.2) is *literally the same* polynomial: its formula, rank identity, and group class-size interpretation are credited fully, not presented as new. The new assertion is the sharp first collision at six graph vertices and the exact seven-pair census. The inspected Remm, Mainkar, and Rossmann texts give motivations, graph reconstruction, and the general invariant but do not state that six-vertex classification. Available six-vertex Rossmann–Voll ask-zeta tables list a distinct matrix-module invariant, not explicit classes of the two-variable vertex-support polynomial; indirect derivability from those data remains a priority risk. A previous related result on seven-vertex groups does not contain a smaller-vertex census. This is a best-knowledge comparison, not uniqueness proof by failed searching.

## Value — PASS

The sharp failure threshold settles a natural completeness question for an established algebraic graph polynomial. Listing all seven indistinguishable pairs identifies the exact small-order obstruction and shows that *the entire* adjoint-rank and centralizer-dimension distributions are insufficient to classify finite-field graphical two-step nilpotent Lie algebras even when dimensions agree. This is a motivated finite classification, not a routine recomputation of the known subset formula.

Self-review: passed. Independent audit: not yet performed.
