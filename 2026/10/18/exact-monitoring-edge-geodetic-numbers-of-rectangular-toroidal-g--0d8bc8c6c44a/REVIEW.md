# Scientific review

## Correctness

**PASS.** The fiber criterion follows by reordering coordinate moves in shortest paths. The cycle-gap characterization follows because a gap of length strictly under half the circumference is uniquely geodesic and one of length at least half cannot be uniquely traversed by a pair of selected endpoints. The proposed columns have three selections, and the explicit block-start formula \(J_v=\lceil vn/m\rceil\) gives the row-gap upper bound \(B=1+\lceil(\lceil m/3\rceil-1)n/m\rceil\). The bound is strictly below \(n/2\) for \(n\ge12\); direct finite integer substitution leaves only dimensions \((5,6)\) and \((7,8)\), for which complete certificates are supplied. Exhaustive small-cycle checks, thousands of row/column tests and independent edge-deletion BFS agree with the theorem. No inference from samples is needed for unbounded parameters.

## Originality

**PASS (same-model, with literature-access limitations).** The closest full-text precedent is Haslegrave, arXiv:2210.08955, Theorem 4, proving \(\operatorname{meg}(C_m\square C_m)=3m\); its Theorem 1 gives the lower bound but not the unequal-side upper bound, and its published diagonal construction uses equal cyclic dimensions. The new balanced-floor construction closes all unequal-side cases, including non-coprime and opposite-parity circumferences. Foucaud et al. arXiv:2210.03774 prove cycle factors and path-grid results, not the rectangular toroidal formula. Xu et al. DOI:10.1080/17445760.2024.2301929 list join/corona/cluster/lexicographic/direct products in the accessible abstract, not Cartesian tori. Tan et al. DOI:10.1080/17445760.2023.2220143 list circulant networks, which can be relevant when the torus has coprime dimensions, but the full paper could not be accessed. The related public mathematical-record searches did not return a result implying the unequal-side exact formula. Remaining risk: uninspected full text could contain a stronger unadvertised statement. Failed or absent searches are not treated as novelty proofs.

## Value

**PASS.** Rectangular toroidal grids are canonical finite networks, and the prior sharp product lower bound left a genuine parameter gap beyond square tori. The theorem determines the invariant for every allowed pair of circumferences, including arbitrarily unbalanced rectangles, while the explicit optimal monitor placement has a direct network-coverage interpretation. A natural all-parameter exact evaluation is stronger than isolated small computations or a routine parameter substitution.

## Limits and verification state

The arithmetic finite boundary check is fully enumerated; the universal claim rests on the displayed inequalities and constructed sets. Exact minimum-set enumeration, special small cycles, strong products, and twisted tori are not addressed. The available primary papers and publisher abstracts were checked within their accessible portions, with the uninspected publisher papers named above as residual originality risks.

Self-review: passed. Independent audit: not yet performed.
