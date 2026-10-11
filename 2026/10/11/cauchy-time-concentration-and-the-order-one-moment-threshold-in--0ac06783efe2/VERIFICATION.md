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
# Verification notes

The proof uses a smooth canonical coordinate change with no time reparametrization; the original clock is essential to the displayed density. The endpoint estimate is proved by splitting at half the energy and bounding the moving singular layer by an exponentially small factor times energy. The moment asymptotics use exact integration at \(p=1\), a beta integral when \(p<1\), and an integrable gamma kernel when \(p>1\). The proofs cover every fixed real \(p\ge0\).

The standalone script `verify.py` uses only the Python standard library. Run it with `python verify.py` in the directory containing the files. It regularizes the turning-point square root by \(u=L\sin^2\theta\), tests positive decreasing periods, exactly normalized zero-order moments, the critical finite-amplitude identity and representative large-energy ratios. The successful diagnostic output begins `CHECK_OK`. No finite numerical computation establishes weak convergence or an infinite-range limit; those follow from the proved integral estimates.

The global-center existence and conjugate period asymptotics are credited to earlier results; no independent audit or validation is asserted.
