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

The universal proof is symbolic. Its critical externally sourced lemma is the distinct-powers characterization from arXiv:2002.02731: a digit sum \(t\) is attained by a multiple of \(n\) exactly when \(t\) distinct powers of the base can sum to a multiple of \(n\). For \(n=b^2+b+1\), the identity \(b^3\equiv1\pmod n\) reduces this to a three-coordinate residue condition.

The proof checks the exact domain \(b\ge2\), \(b\not\equiv1\pmod3\), and uses \(\gcd(b-1,n)=1\) only to place the family in the cofinite regime posed by the source question. Coverage above the boundary is established from the explicit attainable lengths \(3\), \(b+2\), and \(2b+1\). The nonattainment of \(2b-2\) is proved by a contradiction after subtracting the minimum count and reducing to two residue classes.

`verify.py` was replayed from the packaged artifact directory and produced the exact contents of `verify_output.txt`:

`VERIFY_OK bases=66 post_frobenius_checks=924 generator_witnesses=198`

The replay enumerates admissible bases through \(100\), checks the predicted gap and a post-boundary window, and verifies the three explicit integer witnesses. These finite checks are regression evidence only; they do not certify the infinite quantifiers.
