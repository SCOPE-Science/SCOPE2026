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

# Mathematical verification and limits

Run the standalone `verify.py` with `python3 verify.py`. This program implements conjugacy in \(S_m\), orbit counting for unordered permutation tuples, and the exact finite orbit sum of Militaru for \(1\le n\le8\). It checks all 25 computed conjugacy-orbit parameter pairs and recovers the sequence \(1,2,3,7,17,57,305,4120\). It also evaluates the discrete saddle at \(n=200,500,1000,4000,10000\) and prints the scaled displacement and normalized three-term error. Its expected terminal message is `VERIFY_OK`.

The infinite proof in `RESULT.md` rests on (i) Stirling-controlled multiset orbit bounds, (ii) a strictly concave saddle expansion, (iii) a nonidentity fixed-tuple bound based on the smallest nontrivial conjugacy class of the symmetric group and (iv) Burnside's lemma and its stabilizer correction. These are explicit symbolic arguments. Finite enumeration and finite saddle approximations alone cannot establish the asymptotic equivalences or rigidity. No claim of independent review or certification is made.
