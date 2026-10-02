# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** For every connected graph \(H\) of order \(n\ge2\) and every \(k\ge1\), rooting \(C_{4k+1}\) at any vertex gives \(\gamma_t^L(H\odot C_{4k+1})=2kn+\gamma_L(H)\); in particular \(\gamma_t^L(P_q\odot C_{4k+1})=2kq+\lceil2q/5\rceil\).

## C — PASS

The proof was reconstructed from the actual RESULT.md. Removing the root constraint from each \(C_{4k+1}\) copy leaves the step-two graph on the other \(4k\) vertices, which is an odd path with a unique minimum vertex cover of size \(2k\). Copies using only that minimum pattern expose the root, so total domination and location force their base vertices to be distinguished by selected neighboring roots. Because every selected root lies in a copy paying the extra unit, those extra-copy vertices form a locating-dominating set of \(H\), giving the lower bound. Conversely, a minimum locating-dominating set of \(H\) chooses the high local pattern exactly in its copies and the low pattern elsewhere; the local open-neighborhood signatures are distinct and the base set separates the roots. This yields equality. The finite verifier is corroborative only; the argument is infinite in \(H,k\).

Residual risk: No correctness gap was found. The statement is specific to cycle length \(4k+1\); no conclusion for the other congruence classes is inferred.

## O — PASS

Wei et al. (2020) gives exact path-by-cycle rooted-product formulas and explicitly treats the \(4k+1\) cycle case, but its path-only construction does not imply the arbitrary connected-base identity and its displayed case is precisely the one corrected by the audited theorem. The comb-product paper of Pribadi–Saputro treats ordinary locating domination, not locating-total domination. A Resultary semantic search returned the audited record as the direct match and no earlier stronger SCOPE result.

Residual risk: Alternate terminology or a poorly indexed correction could still exist; unsuccessful search is not a proof of novelty.

### Equivalent formulations

**Searches:** Resultary: locating-total domination rooted product cycle 4k+1 locating domination identity; Wei et al., DOI 10.1155/2020/6197065, rooted-product Theorem 9; Pribadi–Saputro, DOI 10.19184/ijc.2020.4.1.4

**Evidence:** Wei et al. studies locating-total domination of rooted products \(P_q\odot C_m\). Pribadi–Saputro studies the different parameter locating-domination on comb products.

**Reasoning:** The located papers use closely related product language, but neither states an equivalent arbitrary-base locating-total identity.

### Broader coverage

**Searches:** Resultary semantic search over locating-total/rooted-product aliases; Wei et al. 2020 full article

**Evidence:** Wei et al. covers path and cycle base families, not arbitrary connected \(H\). No earlier published SCOPE hit stronger than the audited theorem appeared in the semantic results.

**Reasoning:** No inspected source dominates the arbitrary-base statement.

### Exact database or table

**Searches:** Wei et al. exact rooted-product formulas; Resultary exact-title/parameter search

**Evidence:** The only exact prior formula found for the same \(4k+1\) rooted-cycle setting is the path-base formula in Wei et al.

**Reasoning:** This is a structural graph theorem rather than a database-table lookup; the exact-formula comparison is the relevant check.

### Claim versus prior implication

**Searches:** Wei et al. Theorem 9 proof and case \(q_1\equiv1\pmod4\); Pribadi–Saputro ordinary locating-domination theorem

**Evidence:** A path-base formula cannot imply the dependence on \(\gamma_L(H)\) for arbitrary connected \(H\). Ordinary locating domination lacks the total-domination constraint used here.

**Reasoning:** The final claim is not a corollary or special case of a stronger inspected theorem; rather, it specializes to and corrects the earlier path case.

### Source inspections

- **Locating-Total Domination Number of Cacti Graphs** (https://doi.org/10.1155/2020/6197065): PARTIAL_COVERAGE. Trigger: Same parameter and rooted-product construction. Material read: Full accessible HTML including the rooted-product section, Theorem 9 cases, and conclusion. Method: Full-text web inspection. Evidence: The paper treats \(P_q\odot C_m\), including the \(m\equiv1\pmod4\) case, but not the arbitrary-base identity.
- **On locating-dominating number of comb product graphs** (https://doi.org/10.19184/ijc.2020.4.1.4): NOT_COVERING. Trigger: Potential alias through comb-product terminology. Material read: Abstract and accessible article text identifying the parameter as ordinary locating-domination. Method: Full-text/abstract web inspection. Evidence: It studies locating-domination, not locating-total domination.

### Residual risks

- A correction or generalization indexed under different rooted/comb product terminology may have been missed.

## V — PASS

The result repairs a published exact rooted-product formula by a nontrivial amount and replaces a path-specific case with a natural identity valid for every connected base graph, cleanly embedding ordinary locating domination into locating-total domination on a standard graph product family.

Residual risk: Its value is concentrated in the \(1\bmod4\) cycle family; it does not classify all rooted products.

## Overall disposition

**PASSED**
