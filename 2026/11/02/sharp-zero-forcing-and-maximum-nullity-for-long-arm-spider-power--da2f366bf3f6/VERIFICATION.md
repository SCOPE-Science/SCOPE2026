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
# Verification summary

The result concerns equal-arm spider powers with \(m\ge3\), \(k\ge3\), \(\ell\ge k+1\), and \(2(\ell+1)\ge3k\). The proof constructs a symmetric matrix with exact nonzero off-diagonal entries at tree distances one through \(k\), and at least \((m-1)k\) independent null vectors. A separately given zero-forcing sequence supplies the reverse inequality.

Run `python3 verify.py` from the same directory. The finite checks independently (i) build the tree and all distances, (ii) evaluate the stated degree-\(k\) adjacency polynomial, (iii) check its off-diagonal zero/nonzero pattern, (iv) test explicit repeated-eigenvalue null vectors, and (v) run greedy forcing from the proposed set. Tested are 63 triples: three arm counts, seven powers, and three lengths at or above the threshold. Observed output:

```
FINITE_POLYNOMIAL_SUPPORT_AND_KERNEL_MODES_OK 63
INDEPENDENT_GREEDY_FORCING_OK 63
ALL_SPECTRAL_PAIRING_AND_BOUNDARY_CHECKS_OK
VERIFY_OK
```

Floating-point tests are not exact certificates and do not prove the infinite statement. Exact universal justification is the sine-wave eigenvector identity, factorization of paired path roots, positivity of every required matrix entry via a factor-walk, and the chronological forcing sequence in `RESULT.md`. No independent audit has been performed. The unproved shorter-arm region and historical-priority uncertainty are explicitly retained.
