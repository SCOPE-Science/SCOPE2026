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

# Computational verification

Execute `python3 verify_petersen_B3.py` with the standard Python library. The output is included verbatim in `verification_output.txt`. The verifier checks: Petersen graph edges/valences, complete weight-three reduced Świątkowski bases of dimensions 680/2400/2700/960, integer \(\partial^2=0\), exact modular elimination over primes two/three/five, six pentagons with independent 15-edge incidence vectors mod 101, all seven \(S_5\) conjugacy-class signed chain traces, and all seven rational irreducible multiplicities.

The rank conclusions over \(\mathbb Q\) require the independently stated augmentation and six-moving-cycle bounds. In particular, modular ranks alone are not claimed to certify rational ranks. The topological comparison to the reduced Świątkowski complex uses [1,2], not an empirical test. Zero third integral homology follows from the full-column rank of the integral top boundary, but **no complete integral homology classification** is claimed. No external audit has been conducted.
