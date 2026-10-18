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

The standalone `verify.py` requires Python 3 standard library only. Run `python3 verify.py` in a directory containing the file. The expected final line is `VERIFY_OK`.

It constructs each specified finite-field arithmetic table, the literal companion matrix, the two alternating bracket rows, and computes every adjoint rank directly by checking all two-row minors. Tested polynomial/field configurations are: the irreducible quadratic over \(\mathbb F_2\), its split base extension \(\mathbb F_4\); a split quadratic over \(\mathbb F_3\); an irreducible quadratic over \(\mathbb F_3\), its split base extension \(\mathbb F_9\); a split quadratic over \(\mathbb F_5\); and an irreducible cubic over \(\mathbb F_2\), whose roots split in \(\mathbb F_8\). These test both characteristic two and odd characteristic, split and nonsplit Frobenius eigenplane orbits, and two distinct dimensions.

For each case the program checks the root count, all \(q^{2m}\) noncentral-coordinate ranks, the rank counts including the two central coordinates and the resulting commuting-pair total. The geometric radical-ideal assertion and infinite extension sequence are established by the mathematical argument, not exhaustive software tests. No independent audit or external certification is claimed.
