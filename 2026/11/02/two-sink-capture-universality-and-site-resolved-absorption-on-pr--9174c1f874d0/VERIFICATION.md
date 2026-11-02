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

Run `python verify.py` and `python exact_examples.py` from this directory after installing the packages listed in `requirements.txt`. The provided `verification_output.txt` is the output from running these source files, not a substitute for them.

The numerical verifier independently builds seven known strongly regular graphs, verifies their parameters, computes all 598 distinct pairs of sink vertices, calculates the six-column two-sink Krylov matrix and its SVD, and compares the projector from the exact eigenspace/Gram formula. It checks the site-resolved probability at every vertex in every case: 8,849 comparisons in total. It also checks trace five, probability one at both sinks, and nonsink probability sum three. Maximum absolute discrepancy in the tested matrices was below \(1.6\times10^{-15}\). The imprimitive complete tripartite boundary was checked for sink pairs in the same versus different parts. The symbolic verifier confirms all population normalization identities and representative exact rational probabilities using algebraic eigenvalues.

Neither finite enumeration nor numerical agreement is a general proof. The all-order argument depends on the strict nonprincipal spectral radii of both a primitive strongly regular graph and its complement, the two-sink Gram determinants, and decay of the bright part with strictly positive sink rates; these are proved in `RESULT.md`. No independent scientific audit or experimental physical validation is asserted.
