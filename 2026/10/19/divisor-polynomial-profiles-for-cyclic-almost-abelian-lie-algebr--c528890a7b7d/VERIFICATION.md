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

# Reproduction and verification

`verify.py` uses only the Python 3 standard library. From the directory containing this file, run `python3 verify.py`. An original successful run returned `VERIFY_OK 11 independent finite-field configurations`.

The program constructs every subspace in each small tested Lie algebra by canonical row-reduced bases and performs direct bracket tests to enumerate subalgebras and ideals. Separately, it repeatedly takes pairwise Lie brackets until closure for every ordered pair, then tallies the generated dimension. It computes predicted counts from monic polynomial divisors, residue-ring units and Gaussian coefficients and asserts exact equality of all three distributions for every case. Test polynomials include characteristic-two degree-five irreducible and nilpotent examples and mixed/repeated polynomials in small degrees over primes two and three; the degree-five nilpotent test is a control against previously known formulas.

The finite checks do not imply the theorem for arbitrary prime powers or arbitrary degrees, do not establish originality, and are not an independent human audit. The proof in `RESULT.md` supplies the infinite-family argument. The open-access references listed there allow comparison with the previously known nilpotent and random-Krylov special cases.
