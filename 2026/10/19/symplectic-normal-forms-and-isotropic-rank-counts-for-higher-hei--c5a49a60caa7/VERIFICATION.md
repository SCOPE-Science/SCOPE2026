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

# Reproducibility and verification

Execute the included dependency-free Python script: `python verify_rb_heisenberg.py`.

Exact arithmetic over the stated prime fields was used. For \(p=3,m=1\), all \(2{,}187\) triples \((A,c,\ell)\) were tested, each against all \(729\) ordered input pairs, and the direct identity agreed with the proposed matrix criterion in every case. For \(p=3,m=2\), all \(243^2\) input pairs were checked for each of \(18\) matrices satisfying the criterion, with a nonzero linear correction. For \(p=5,m=2\), another \(1{,}000\) deterministic input pairs checked a nondegenerate scalar case. The rank-count routine verifies the exact isotropic-subspace and surjection formulas and returns matrix counts \(1,3{,}200,249{,}600\) for ranks \(0,1,2\) at \(p=3,m=2\).

Expected terminal suffix: `VERIFY_OK 2187 full H3 map cases; 18 exhaustive H5 pair tests; 1000 further checks`.

Computations are neither a proof for all higher dimensions nor a complete enumeration of the intermediate central-character stratum. The manuscript supplies the universal proof. No independent mathematical audit has been performed.
