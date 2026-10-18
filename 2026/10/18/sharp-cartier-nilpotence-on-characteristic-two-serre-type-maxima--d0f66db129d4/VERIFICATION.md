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

The proof's global ingredients are the degree-four one-pole different, the complete holomorphic monomial basis, the characteristic-two Cartier identities, the antipodal modular set, and explicit surviving chains. They are written out in `RESULT.md`; the program is corroborative only.

Run `python3 verify.py` with the files in the same directory. It has no third-party dependencies. In the local exact run, it checked the odd exponents \(n=3,5,7,9,11,13,15\), printed for each the dimension and the ranks of the first and penultimate iterates, verified the omitted pair \(\{m,2m\}\), and finished with `VERIFY_OK`.

The observed final nonzero ranks for these seven cases were \(1,2,3,4,5,6,7\), respectively. **No uniform formula for that rank is claimed or inferred from this finite sample**; the paper proves only positivity for every admissible \(n\) and rank at least two for \(n\ge5\). Independent audit has not been performed.
