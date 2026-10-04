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
# Verification

The proof is symbolic. The upper bound explicitly reuses one pool of \(M+1\) variable names to state exact class sizes and exact multiplicities. The lower bound gives a permanent Duplicator strategy in the \(M\)-pebble game against one of two nonisomorphic witnesses.

As a supplementary check, `verify.py` performs three tests. First, for every integer partition of total size at most twelve it constructs the lower witness and compares capped finite-variable class profiles at \(M\) and \(M+1\). Second, for small state spaces it computes the greatest fixed point of the full back-and-forth pebble relation and checks that Duplicator wins at \(M\) while the next level separates when enumerated. Third, it checks the balanced specialization on all \(1\le r,s\le8\).

Running the embedded script with Python 3 produces exactly:

`VERIFY_OK profile_cases=271 pebble_cases=18 balanced_cases=64`

The computation is a finite sanity check and is not used to extrapolate the theorem. The general result follows from the proof in `RESULT.md`.
