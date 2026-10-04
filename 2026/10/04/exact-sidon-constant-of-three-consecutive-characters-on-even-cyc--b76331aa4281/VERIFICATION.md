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

The proof in `RESULT.md` is the evidence for the infinite theorem. Its critical steps are: pairing the samples indexed by \(k\) and \(k+N/2\); the exact covering radius \(2\pi/N\) for the \(N/2\)-th roots; the identity reducing the two-term bound to \((1-q)(a-c)^2\); weighted Cauchy--Schwarz; and the explicit equality construction.

Run `python3 artifacts/verify.py` for a finite regression check. The script evaluates the proposed extremizer for every even \(N\) with \(4\le N\le200\), compares its measured ratio with \(\sqrt{1+\sec^2(\pi/N)}\), and tests the proved upper bound on randomized complex coefficient triples. The packaged script was replayed successfully before serialization and printed `VERIFY_OK`.

The numerical checks do not certify the theorem for untested orders and are not used as a substitute for the analytic proof. Odd \(N\) and arbitrary three-point frequency sets are unproved here.
