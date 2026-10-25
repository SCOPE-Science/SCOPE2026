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

# Verification details

Execute `python3 verify.py` without external Python packages. All assertions must complete and the last output line must be `CHECK_OK`.

The complete labeled connected-graph counts checked at orders two through five are respectively 1, 4, 38 and 728; the corresponding unlabeled counts are 1, 2, 6 and 21. The positive-support Markov chains have respectively 4, 8, 16 and 32 opinion colorings for these orders. Two separately implemented transition-support tests agree on every coloring of every connected labeled graph; two separately implemented terminal-class algorithms agree on every computed chain. The exact exceptional labeled count at order five is 135, partitioned into three unlabeled classes of orbit sizes 60, 60 and 15.

The three explicit five-vertex graphs have closed four-coloring classes with transition probabilities exactly one half to each member of the opposite phase. The code tests all pendant-leaf distributions in the bull family at every order between five and sixteen. Existence at every larger order is established by the direct strict-majority proof in `RESULT.md` and is not inferred from those finite construction checks.

No stochastic simulation, numerical tolerance or inferred infinite assertion is used for the finite classification. The source-model and publication-priority comparisons are research judgments rather than machine certificates. This package has not received independent external audit or validation.
