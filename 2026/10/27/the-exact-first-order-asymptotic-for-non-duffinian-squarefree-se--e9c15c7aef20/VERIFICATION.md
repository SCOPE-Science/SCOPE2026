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

# Verification details

Run `python3 verify.py` from this directory with a standard Python 3 interpreter. No dependencies beyond the standard library are required. The expected final line contains `VERIFY_OK`. The verifier constructs its own prime sieve, scans every unordered pair of distinct primes with product not exceeding \(10^6\), and compares the number-theoretic divisibility predicate with an independent direct gcd evaluation. The finite experimental totals are compared exactly, not probabilistically. The prime-series constant is evaluated to a fixed cutoff and enclosed using the elementary reciprocal-telescoping bound \(\sum_{n>N}1/[n(n-1)]=1/N\).

The analytic inference \(E(x)\sim C x/\log x\) is not established by these finite checks. Its proof depends on the prime number theorem in fixed reduced residue classes, Brun–Titchmarsh for varying moduli up to \(x^{1/4}\), and a direct upper bound on the remaining progression terms. No computational certificate for an infinite claim is asserted. No independent audit was performed.
