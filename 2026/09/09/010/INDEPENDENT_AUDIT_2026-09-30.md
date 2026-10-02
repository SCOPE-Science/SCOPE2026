# Independent mathematical audit — 2026-09-30

## Outcome

**PASSED** for the final finding as stated.

## Correctness — PASS

The no-careful-word theorem has a short set-dynamics proof and was independently checked by exact subset BFS. With \(Q=\{0,\ldots,6\}\), \(F=\{0,\ldots,5\}\) and \(G=\{1,\ldots,6\}\), the only carefully reachable sets in the exceptional \(a\)-hole-at-6 case are \(Q,F,G\); for every \(b\)-hole, \(b\) is already undefined on \(Q\) and \(a\) fixes \(Q\) setwise. The committed verifier exhausts at most 128 subsets per mutant and recomputes every one of the 98 ordinary completion cells. The baseline reset length 36 and all 14 negative careful-synchronization verdicts were independently replayed.

Checked sources:
- actual committed `artifacts/verify.py`, `artifacts/gap_table.csv`, `artifacts/fill_landscape.csv`; independent subset-BFS replay

Residual risks:
- A sentence in RESULT overstates \(s\in F\cap G\) for the \(b\)-hole case when \(s=0\); the simpler preceding fact that \(b\) is undefined on the initial set \(Q\) while \(a(Q)=Q\) proves the case anyway.
- Scope is the stated labeling and single-deletion neighborhood only.

## Originality — PASS

No inspected source or published-result search contained the complete one-hole \(C_7\) careful-synchronizability map or the 98-cell completion landscape. Prior work on one-undefined-transition automata and careful synchronization is much broader in complexity and extremal-threshold scope, without implying this local census.

### equivalent_formulations

Searches: Resultary semantic search for \(C_7\) one-hole careful synchronization; Martyugin 2012 one undefined transition; Vorel arXiv:1403.3972

Evidence: Only the audited record matched the exact local census.

Reasoning: The equivalent formulation as careful reachability in the subset automaton was compared; no published exact \(C_7\) one-hole map was found.

### broader_coverage

Searches: P. Martyugin, Synchronization of Automata with One Undefined or Ambiguous Transition; Vorel, Subset Synchronization and Careful Synchronization of Binary Finite Automata

Evidence: Martyugin proves complexity results for automata with one undefined transition; Vorel gives general/exponential careful-synchronization results.

Reasoning: These broader results neither imply that all 14 specific mutants fail nor determine the 98 ordinary fill distances.

### exact_database_or_table

Searches: Published-result search for Cerny one-hole mutants and fill landscape

Evidence: No exact table or database row was found.

Reasoning: The 98-cell table is independently recomputable from the canonical small automaton but was not found pre-tabulated.

### claim_vs_prior_implication

Searches: Comparison against PSPACE-completeness and lower-bound theorems

Evidence: Complexity/lower-bound statements do not force the status of these particular 14 mutants.

Reasoning: The final local classification is not a corollary of the inspected general theorems.

### source_inspections

- **Synchronization of Automata with One Undefined or Ambiguous Transition** (https://doi.org/10.1007/978-3-642-31606-7_24): trigger=Exactly the one-undefined-transition setting.; material read=Accessible abstract and bibliographic record.; method=Primary-publication abstract inspection.; assessment=RELATED, NOT COVERING.; evidence=The paper establishes PSPACE-completeness, including binary automata, not the exact Cerny-neighborhood census.
- **Subset Synchronization and Careful Synchronization of Binary Finite Automata** (https://arxiv.org/abs/1403.3972): trigger=Canonical careful-synchronization literature.; material read=Accessible arXiv full-text/abstract material on general lower bounds and subset synchronization.; method=Primary-source inspection.; assessment=RELATED, NOT COVERING.; evidence=The results are general asymptotic/lower-bound statements, not the 14-mutant map.
- **Committed C7 one-hole verifier** (artifacts/verify.py): trigger=Critical finite classification certificate.; material read=Complete source plus both committed CSV tables.; method=Line-by-line inspection and independent subset-BFS replay.; assessment=Supports correctness.; evidence=All 14 careful searches terminate without a singleton and all 98 ordinary fill cells are recomputed from transition tables.

### checked_sources

- Martyugin 2012 DOI:10.1007/978-3-642-31606-7_24
- arXiv:1403.3972
- Resultary semantic search
- actual committed verifier/tables

### residual_risks

- Small automata may have appeared in unpublished exhaustive searches.
- Best-of-knowledge originality is not a priority certificate.

## Scientific value — PASS

The one-transition-deletion ball around the canonical \(C_7\) extremal automaton is a natural local testbed for how partiality changes synchronization. A complete negative careful-synchronization map plus all 98 ordinary fills is a compact exact benchmark and boundary result, not an arbitrary collection of unrelated automata.

Checked sources:
- careful-synchronization literature and the canonical Cerny family

Residual risks:
- The result is local to one labeling and does not imply behavior for larger one-hole neighborhoods or multiple holes.

## Limitations

- The classification is only for the stated \(C_7\) labeling and one missing transition.
- The 98 ordinary completion distances are computational BFS certificates.
- The repository stores inspected artifacts at `artifacts/...`; legacy prose/metadata retain an `output/artifacts/...` prefix.
