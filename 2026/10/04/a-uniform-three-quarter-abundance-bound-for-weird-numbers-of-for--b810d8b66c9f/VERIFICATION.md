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

The symbolic proof uses only the exact identities and necessary-and-sufficient criterion stated in the cited primary source. The critical steps checked are:

1. \(a=M(M+1)-(p-M)(q-M)\).
2. The forbidden equation \(pq=r+sp+tq\), with \(1\le r,s,t\le M\), is exactly equivalent to forbidding \(a-M+1\le up+vq\le a\) for \(0\le u,v\le M-1\).
3. In the case \(q\le a\), the residues \((a-vq)\bmod p\) for \(0\le v\le\lfloor a/q\rfloor\) are distinct and all lie in the terminal interval of length \(p-M\), which gives \(a<(p-M)q\).
4. In the case \(q>a\), direct substitution gives \((q-M)(p-M+1)>M^2\).
5. Both cases imply \((p-M)(q-M)>M^2/4\), hence the stated abundance bound.

The included `verify.py` performs exact integer arithmetic. It re-enumerates candidate prime pairs for \(1\le k\le8\), reproduces the published counts \(1,1,5,3,10,23,29,53\), and checks the theorem on every weird pair found. Its successful output is:

`VERIFY_OK counts=[1, 1, 5, 3, 10, 23, 29, 53] prime_pairs_checked=29490 max_a_over_M2=(0.4444444444444444, (1, 5, 7, 4, 3))`

The finite computation is not an exhaustive proof over all \(k\). The infinite theorem is established by the symbolic argument in `RESULT.md`.
