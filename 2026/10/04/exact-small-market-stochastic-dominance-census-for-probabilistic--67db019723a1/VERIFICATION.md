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
The embedded `verify_ps_rsd4_census.py` is a standard-library-only exact verifier.

It enumerates every labeled strict square profile for \(n=1,2,3\). For \(n=4\), it exhausts all \(17{,}550\) anonymous multisets of four rankings, computes PS and RSD with exact `Fraction` arithmetic, classifies stochastic dominance by every cumulative preference cutoff, restores exact agent-label multiplicities, and canonicalizes under all \(24\) object relabelings.

A separate type-stratified Burnside calculation over the same complete anonymous domain independently reproduces the symmetry-class counts. A direct walk through all \(24^4\) labeled ranking-index tuples reconstructs the labeled totals from the exhaustive anonymous classification. The verifier also replays the published four-agent dominance example exactly.

Run:

`python3 verify_ps_rsd4_census.py`

The first output line must be:

`VERIFY_OK`

The expected main outputs include:

- \(n=3\): \(144\) equal and \(72\) incomparable labeled profiles;
- \(n=4\): \(72{,}288\) equal, \(11{,}664\) PS-dominance, and \(247{,}824\) incomparable labeled profiles;
- exact probabilities \(251/1152\), \(9/256\), and \(1721/2304\);
- \(n=4\) symmetry classes \(209\), \(36\), and \(517\);
- four minimum PS-dominance classes using two preference orders.

The finite replay certifies only the finite claims stated in RESULT.md. It does not establish any asymptotic conjecture.
