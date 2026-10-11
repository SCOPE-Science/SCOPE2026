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

# Verification of the finite modular-hyperbola Fourier theorem

The attached `verify_hyperbola.py` uses exact integer arithmetic for all Fourier-zero tests. For a primitive \(p^k\)-th root \(\zeta\), an integer polynomial \(F\) of degree less than \(p^k\) vanishes at \(\zeta\) exactly when its residue-class coefficient blocks indexed modulo \(p^{k-1}\) agree, because \(\Phi_{p^k}(X)=\sum_{j=0}^{p-1}X^{jp^{k-1}}\). The checker applies that criterion independently to the actual exponential-sum exponents.

The checker tests all \(p^{2k}\) frequency pairs for ten moduli: \((3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,2)\). Total Fourier-pair tests: 40,746. It also checks the explicit optimal \(p^{k-1}\)-frequency line construction, and exhaustively counts maximal compatible child-digit subsets for primes \(3\) and \(5\). Their respective counts are 27 and 120. On success the script prints `VERIFY_OK`.

The infinite-prime-power capacity theorem, precise zero criterion and all-family tree characterization rely on the mathematical proof in `RESULT.md`, not on these finite computations. In particular, exact small-case enumeration is not presented as exhaustive across all primes or all depths. Independent validation has not been performed.
