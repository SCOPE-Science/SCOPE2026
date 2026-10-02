# Independent scientific review — 2026-10-01

## Final claim

For every connected graph \(H\) of order \(n\ge2\) and every \(k\ge1\), rooting \(C_{4k+1}\) at any vertex gives \(\gamma_t^L(H\odot C_{4k+1})=2kn+\gamma_L(H)\); in particular \(\gamma_t^L(P_q\odot C_{4k+1})=2kq+\lceil2q/5\rceil\).

## Correctness — PASS

The proof was reconstructed from the actual RESULT.md. Removing the root constraint from each \(C_{4k+1}\) copy leaves the step-two graph on the other \(4k\) vertices, which is an odd path with a unique minimum vertex cover of size \(2k\). Copies using only that minimum pattern expose the root, so total domination and location force their base vertices to be distinguished by selected neighboring roots. Because every selected root lies in a copy paying the extra unit, those extra-copy vertices form a locating-dominating set of \(H\), giving the lower bound. Conversely, a minimum locating-dominating set of \(H\) chooses the high local pattern exactly in its copies and the low pattern elsewhere; the local open-neighborhood signatures are distinct and the base set separates the roots. This yields equality. The finite verifier is corroborative only; the argument is infinite in \(H,k\).

**Risk:** No correctness gap was found. The statement is specific to cycle length \(4k+1\); no conclusion for the other congruence classes is inferred.

## Originality — PASS

Wei et al. (2020) gives exact path-by-cycle rooted-product formulas and explicitly treats the \(4k+1\) cycle case, but its path-only construction does not imply the arbitrary connected-base identity and its displayed case is precisely the one corrected by the audited theorem. The comb-product paper of Pribadi–Saputro treats ordinary locating domination, not locating-total domination. A Resultary semantic search returned the audited record as the direct match and no earlier stronger SCOPE result.

**Risk:** Alternate terminology or a poorly indexed correction could still exist; unsuccessful search is not a proof of novelty.

## Value — PASS

The result repairs a published exact rooted-product formula by a nontrivial amount and replaces a path-specific case with a natural identity valid for every connected base graph, cleanly embedding ordinary locating domination into locating-total domination on a standard graph product family.

**Risk:** Its value is concentrated in the \(1\bmod4\) cycle family; it does not classify all rooted products.

## Overall disposition

**PASSED**
