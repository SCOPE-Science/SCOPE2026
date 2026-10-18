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

# Verification of the palindrome Hankel Schatten thresholds

The proof is infinite-dimensional and self-contained. The critical pieces are: (a) disjoint supports of palindrome-completing columns or rows, implying the exact singular spectrum for each word-length block; (b) the divergent empty-word column at the fourth-root threshold; (c) exact palindrome counts for the Hilbert--Schmidt norm; (d) gauge averaging to the diagonal reversible-permutation blocks, forcing every Schatten threshold; (e) geometric block-norm summation for sufficiency; and (f) separate signed length-band singular spectra and Ky Fan bounds for the nontrivial weak endpoint.

The included `palindrome_schatten_check.py` was executed with NumPy. At alphabet size 2 and maximum block length 5, its finite squared Hilbert--Schmidt norm is 1.9415433818 (full formula 1.9422444995). At alphabet size 3 and maximum block length 4, the finite value is 1.8799893737 (full formula 1.8815272153). All computed rectangular block singular-value formulas passed within stated floating-point tolerances. The finite cutoffs do not establish any infinite result; the analytic proof does.

The comparison to available primary literature covers the operator domains, normalizations and mathematical implications rather than only keyword matches. Earlier and differently indexed results remain a residual priority risk. No separate independent audit has taken place.
