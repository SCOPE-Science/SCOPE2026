---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently reconstructed the normalized DFT on G=Z/(2N): with z_k=e^{pi ik/N}, half-window frequency Gram has diagonal 1/2, zero distinct same-parity entries, and opposite-parity centered block B_{ac}=(2/N) z_a/(z_a-z_c). Every z_k is distinct and Cauchy determinant shows every maximal r=min(e,o) square minor nonzero. Thus rank(B)=r, nullity of 2C-I is |e-o| and its other eigenvalues are paired singular values ±s_j. Cauchy–Binet gives exactly the stated positive product (2/N)^{2r} times the sum of squared Cauchy chord products. Balanced determinant sign is (-1)^r. N=1, r=0, unbalanced masks and all frequencies satisfy the stated boundary conventions. Independently built direct truncated DFT matrices for N=1..4 illustrative masks; spectral products matched chord sums to <4e-16. This finite check is not the proof.

## originality

PASS

Best-of-knowledge, after comparing the actual theorem and its Toeplitz/Gram formulations. Classical periodic-DPSS papers treat consecutive spectral intervals and/or asymptotic/estimated eigenvalue concentration; the exact parity-rank law for ALL gapped frequency subsets and the Cauchy–Vandermonde all-gap product do not follow from those statements. Cauchy determinant itself is classical, not claimed new. The 1984 Xu–Chamzas full text remains an acknowledged primary-source gap (the authorized institutional tool returned a verification-interrupted state; no bypass/retry). A hidden equivalent Cauchy-matrix theorem remains a serious residual risk, not silently ruled out.

## value

PASS

An exact all-frequency-mask transition eigenspace dimension for the natural even-cycle half-window is a structural signal-concentration invariant; arbitrary gapped and multiband spectra are mathematically motivated beyond a chosen small index. The full gap product is an exact aggregate measure of noncentral spectral separation available algebraically without diagonalization. This is more than routine even/odd pairing or a numerical lookup, although classical Cauchy identities do the proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
