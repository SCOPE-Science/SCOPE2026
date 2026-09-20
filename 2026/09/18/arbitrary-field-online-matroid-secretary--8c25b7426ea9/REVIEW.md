# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The motivating online algorithm has finite state support at every observed prefix because each state is the span of a subset of the finite observed set. For a current set \(Y\), the signature consisting of \(\dim L\) and the intersection dimensions \(\dim(W\cap L)\) for all subset-span states \(W\in\mathcal S_Y\) determines every term in the acceptance constraint \(g_p(L)\le0\), including post-acceptance states \(W+\langle e\rangle\). Hence only finitely many distinct constraints occur over an arbitrary field.

The paper already proves the exact finite-signature/minimax repair needed when its modular extension has infinitely many flats: representative signatures suffice, supermodular uncrossing reduces an optimal dual solution to a chain, and the fixed-chain acceptance construction then establishes feasibility. The vector-space lattice over any field is modular, so the same proof applies. Rationality and finite support propagate inductively. The source proof of the conditional acceptance probability \(k/(i-1)\) and its averaging to \(1/e\) is independent of the field.

The generalized finite-rank modular-ambient statement is checked against the same identities used in the source's modular-extension corollary. Requiring the ambient geometry to have finite rank ensures finitely many possible rank signatures without knowing the future finite subset.

A standalone exact-rational verification artifact checks signature invariance and supermodularity on a representative four-dimensional instance. It is supplementary rather than a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** Bérczi--Dughmi--Livanos--Soto--Verdugo explicitly state the online-representation theorem only over a finite field. They separately remove field dependence in the known-matroid model by re-representing the fully known finite matroid over a finite field, and separately develop finite signatures for infinitely many flats in their known-matroid modular-extension section. The present result combines the online construction with that finite-signature argument and imposes the invariant on the fixed ambient geometry, so future vectors need not be known.

Abdi--Banihashem--Hajiaghayi--Mittal prove the \(1/e\) theorem for a linear matroid given before arrivals and do not state the arbitrary-field online-representation extension in the inspected version. Searches for `arbitrary field`, `infinite field`, `online-representation`, and modular-ambient variants of matroid secretary found no inspected prior statement of this theorem. The motivating manuscripts were posted on September 16--17, 2026, so near-simultaneous observations or imminent revisions are an unusually significant residual risk.

No inaccessible older paper was identified as especially likely to contain this exact extension. The principal originality risk is contemporaneous work around the two new strong-secretary manuscripts, not an inaccessible historical source.

## Value

**PASS.** The result removes a conspicuous model restriction from a major new secretary theorem. The distinction is real: the source's Rado re-representation argument is offline and uses advance knowledge of the whole matroid, whereas the online-representation model requires decisions before future dependencies are known. The extension covers natural online vector streams over \(\mathbb Q\), \(\mathbb R\), and \(\mathbb C\), and identifies the true structural requirement as finite-rank modular ambient geometry rather than field finiteness.

The result also clarifies the role of the source's finite-field assumption: it is needed only to make the family of subspace constraints visibly finite, and the later signature compression supplies a field-independent replacement.

## Limitations and residual risks

The construction remains computationally unrestricted and no polynomial running time is proved. For general infinite-field or abstract modular representations, finite essential constraint types exist mathematically, but the cost of discovering realized types depends on the access model. The theorem assumes a fixed finite-rank ambient geometry. It does not address arbitrary unknown ambient lattices of unbounded rank, nor does it improve the optimal constant \(1/e\).

Originality is to the best of our knowledge and is unusually exposed to rapid revision because the motivating preprints are only days old.
