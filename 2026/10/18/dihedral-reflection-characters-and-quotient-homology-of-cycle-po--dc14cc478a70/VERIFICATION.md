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

# Reproducibility

With Python 3 installed, run `python3 verify.py` in this directory. The complete expected deterministic output is in `verify_output.txt`. The verifier reconstructs vertex-orbit invariant faces directly from all connected three-vertex tests, implements the signed action on oriented simplices, and compares the resulting Lefschetz traces with the proved formulas in 90 reflection instances covering \(2\le p\le7\). It separately builds the original cut complex for six small reflection cases, including the empty-face reduction, rather than reusing the Alexander dual representation. Full rational dihedral quotient ranks are independently reconstructed by averaging all signed dual-chain traces at 21 parameter pairs, without using the known closed rotational-character formula. Exact mod-two triangle boundary ranks check the dual first Betti number at five parameters.

The program uses only standard-library modules. All finite checks returned `VERIFY_OK`. It does not independently prove the general reflection-localization lemma, the published shellability theorem, or full integral homotopy, and it is not an independent scientific audit. The displayed mathematical conclusions have received only the stated self-review.
