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

# Verification and scope

The proof in `RESULT.md` is valid symbolically for every finite field and \(n\ge2\). Matrix multiplication and Gaussian coefficients are independently implemented in the included files.

Run `g++ -O2 -std=c++17 verify_idempotent.cpp -o verify_idempotent && ./verify_idempotent` to enumerate all coefficient arrays for \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3)\). The implementation constructs the entire derivation matrix on the wedge-basis Lie algebra, checks \(D^2=D\), and computes its ordinary rank by modular elimination. Its expected final marker is `VERIFY_OK_IDEMPOTENT_FREE_CLASS2`.

Run `python3 verify_gf4.py` for a separately implemented exhaustive extension-field test with \(n=2\) and \(q=4\). It constructs multiplication in \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\) and directly computes the idempotent derivation rank histogram. Its expected marker is `VERIFY_OK_IDEMPOTENT_FREE_CLASS2_GF4`.

The finite checks do **not** verify all \(n\) or all fields. The orbit classification, exact counts, and sharp rank boundary follow instead from the stated block calculation and conjugacy argument. A separate independent scientific audit has not been performed.
