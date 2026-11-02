---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. For the Wolfram Rule-54 map specified by its eight three-bit input neighborhoods, four input pair states form a labelled de Bruijn graph. A periodic output word w^Z has any biinfinite preimage iff its Boolean relation R(w) contains a directed cycle; it has an n-periodic predecessor for |w|=n iff R(w) has a diagonal loop. Exhaustive closure of all products of two 4x4 Boolean adjacency generators has exactly 109 matrices, 77 with a loop, 31 acyclic, one cyclic but loopless. My independent monoid implementation verified that the exceptional matrix is R_1, that its only entering right-transition is I --1--> R_1, and there are no transitions into I; thus the only word with a cyclic relation but no loop is length-one '1'. Consequently F(P_n)=Y∩P_n for every n>=2. The constant output 1^Z is in Y via alternating predecessor but neither constant input maps to it, giving the unique n=1 exception. When output has least period n, a P_n predecessor must also have least period n by shift commutation. Ring tests ≤12 are separate corroboration, not all-n proof. The 109-state finite closure is genuinely exhaustive, not mere length-cutoff testing.

## originality

PASS

PASS best-of-knowledge for the uniform same-period one-step lifting and unique fixed-point exception. Martínez–Adamatzky–McIntosh (2014) develops Rule 54 de Bruijn and subset diagrams, Garden-of-Eden words and spatial patterns; all of those representations are prior, while the inspected primary discussions do not establish the 109-relation-monoid classification and n>=2 lifting. Mariot–Leporati–Dennunzio–Formenti (2017) studies preimage periods of surjective cellular automata and its standard period-multiplicity tools cannot directly assert this for the non-surjective Rule 54. Possible unindexed period-lifting catalogues are a residual risk.

## value

PASS

PASS. An exact exceptional-period classification for a paradigmatic non-surjective elementary cellular automaton is a natural symbolic-dynamics result. The theorem resolves all spatial periods using a nontrivial finite Boolean semigroup certificate; the fixed-point obstruction cannot be dismissed as a generic periodic-image fact. It explicitly excludes iterated temporal inverse dynamics and predecessor multiplicities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
