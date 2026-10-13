---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The deductive proof is contained in `RESULT.md`. An unrestricted structure may have arbitrarily many elements and a formula may have arbitrarily high finite quantifier rank; neither kind of unboundedness is discharged by checking a finite set of examples.

The exact finite support tests in `verify.py` independently evaluate the defining sentence on every binary-relation pair on one or two labeled elements, confirm closure under pairwise disjoint union for all \(6561\) ordered pairs of satisfying test structures, and check the finite separating models and both induced relation-closed embeddings. Run `python3 verify.py` with the standard Python interpreter; no external files, datasets, or packages are required.

The crucial general claim is the structural-induction lemma preserving allowed matrices forward across relation-closed induced embeddings; its proof addresses atoms, negated atoms, both positive Boolean connectives, unrestricted existential quantification, and either direction of guarded universal quantification. In particular, the argument does not substitute a finite enumeration or a failed search for an infinite proof.

The literature comparison uses arXiv:2603.12171v1, §3.4, including its expressly open identity-free question. Independent audit or external formal certification has not been performed.
