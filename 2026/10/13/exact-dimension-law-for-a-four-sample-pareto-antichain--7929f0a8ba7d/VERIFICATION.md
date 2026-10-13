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

Run `python3 verify.py` from the same directory. It uses only Python 3 standard library and deterministically reconstructs every one of the 64 pairs-of-label constraint subsets and every one of the 24 orders. The signed extension coefficients are exact: \(1,-5,1,8,-6,1\) at extension sizes \(4,5,6,8,12,24\), with cancellation at \(1,2,3\).

Independent direct permutation-tuple enumeration (through dimension 5) and a 64-state inversion-union dynamic program (through dimension 12) reproduce the same exact probabilities. Expected verifier output starts with `VERIFY_OK subsets=64 orders=24 dimensions=12 explicit_tuples_to_d=5`.

These are exhaustive *finite* checks of the lemma and special dimensions, not finite approximations to an infinite proof. The analytic rank-symmetry argument and coordinate coupling prove the theorem for all positive integer dimensions. Checked examples include \(\mathbb P(A_3)=151/576\), \(\mathbb P(A_4)=7207/13824\), and \(\mathbb P(A_5)=238555/331776\). The result requires independent atomless coordinate distributions and precisely four i.i.d. observations; no dependent-coordinate or general sample-size assertion was verified.
