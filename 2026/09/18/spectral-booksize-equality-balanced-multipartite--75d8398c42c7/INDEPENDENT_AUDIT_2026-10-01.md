# Independent audit — Equality cases in the universal spectral booksize bound

Audited: 2026-10-01 UTC

## Correctness — PASS

For every edge, the degree sum is at most \(n+\operatorname{bk}(G)\). On a spectral-radius component, the standard edge degree-product bound and AM--GM give \(\lambda\le\frac12\max_{uv}(d(u)+d(v))\), hence the universal inequality. Equality forces equality throughout: the component is regular (the semiregular bipartite alternative also balances), spans all vertices, and every edge is dominating. Thus the complement has no induced three-vertex path and is a disjoint union of cliques; regularity forces those clique sizes to be equal. Equivalently, \(G\) is balanced complete multipartite. Direct substitution verifies the converse.

Risks: The standard equality characterization for the edge degree-product spectral-radius bound was used as a classical input; no computational certificate is needed.

## Originality — PASS

Targeted statement and implication searches located the audited classification itself in the published archive but no earlier source stating that equality in \(\operatorname{bk}(G)\ge2\lambda(G)-n\) is exactly balanced complete multipartite. The source preprint's later 2026-09-24 expansion contains the universal bound and stronger stability results, but postdates this record and its accessible abstract still does not state the exact equality classification.

Equivalent-formulation search: Searches compared the full iff equality structure, not just the Turán example.

Broader-coverage search: Later stability is not automatically the same as the exact universal equality classification and postdates the audited record.

Database/table check: The claim is an all-graph structural classification.

Claim-versus-prior implication: The conclusion is not merely the statement of the universal inequality or its Turán sharpness example.

### Source inspections

- **The spectral Erdős book theorem: sharp bounds and stability** — Current version abstract and version metadata; direct arXiv/Oxford full-text retrieval failed. Assessment: The current abstract includes \(2\lambda-n\) among three sharp lower bounds but does not state the audited equality classification; the substantial post-record revision is retained as a coverage risk.
- **Spectral radius and degree-product bound literature** — Bibliographic/statement-level material identified by the record and current searches; full article was not obtained in this run. Assessment: This bound supplies an equality input but not the booksize equality classification.

## Scientific value — PASS

Exact equality structure for a sharp universal spectral extremal inequality is a natural complete classification. It identifies all extremizers at every order and makes the balanced Turán examples structurally forced rather than merely examples, so it clears the value bar despite the proof being concise.

## Limitations

This is an equality classification, not a stability theorem. The source preprint changed substantially after this record: its 2026-09-24 version added many results including the \(2\lambda-n\) term. The accessible current abstract does not state the exact equality classification, but the unavailable full version leaves a residual source-version overlap risk. Originality is to the best of current knowledge.
