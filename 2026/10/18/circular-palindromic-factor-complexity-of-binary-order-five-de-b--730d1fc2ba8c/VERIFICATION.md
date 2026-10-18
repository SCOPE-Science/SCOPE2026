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

Run `python3 verify.py` in the directory containing `verify.py`, `spectrum.csv`, and `profiles.csv`. Only the Python standard library is required. The script enumerates all \(65536\) local edge-pairing assignments, independently enumerates all Euler circuits with the distinguished zero edge, checks the complete \(2048\)-cycle sets against each other, and verifies the binary de Bruijn property of each cycle. It computes all nonempty circular palindromic factors in two different ways, comparing the entire returned sets of strings.

The computed histogram is `22:32,23:32,24:200,27:192,28:920,29:544,30:128`; exactly `51` distinct full length profiles occur; the symmetry action produces `528` orbits. The script checks that both CSV files contain precisely the independently computed exact counts and recomputes rational mean `1775/64` and variance `12511/4096`. On success it prints `VERIFY_OK` followed by the verified counts. A failure raises an exception.

The finite exhaustive proof does not require sampling or pseudorandom behavior. It does not verify a statement for other de Bruijn orders, and no independent scientific audit or historical-priority certification is asserted.
