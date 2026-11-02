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

The analytic proof uses a four-space orthogonal decomposition and projector-rank calculation, with the sole exceptional parameter \(t=1\). No finite computation is used as a proof for every \(m\) or every real \(t>0\).

The file `paired_bipartite_rank_verify.py` constructs the \(2m\)-state Laplacian and computes exact modular Kalman ranks over the prime \(1000003\), comparing them with the claimed formula. It uses only Python's standard library and deterministic inputs. Its complete run reported `PASS 2450 exact finite-field Kalman rank comparisons; modulus 1000003`. Full exhaustive nonempty-site subsets are tested at \(m=2,3,4\) and conductances \(1,1/2,3/2,4/3,2\); deterministic samples and boundary configurations are checked for \(m=5,6,7,8\). This does not prove the infinite family or arbitrary real conductances, and modular coincidences would be possible in principle; the separate exact real-algebra proof supplies the universal claim.

The proof's hypotheses exclude zero or negative matching conductance, unequal off-matching weights and all other matrix families. Control energy and numerical conditioning were not assessed. Self-review passed; independent mathematical review has not been performed.
