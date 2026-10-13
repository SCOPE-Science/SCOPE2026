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
# Reproduction and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses no third-party libraries. Its finite fields are \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). Each tested incidence algebra is built from an explicit full list of comparable pairs, including transitively comparable pairs. It enumerates every algebra element, filters all idempotents by direct multiplication, then checks commutation for every ordered tuple. It tabulates the observed count **separately for each diagonal coloring** and compares with \(q^{m(c)}\). Independently, it constructs the Jacobian matrices of the full idempotence and pairwise-commutation system at all diagonal colorings and checks that the tangent dimension equals \(m(c)\).

The exact successful outputs for the tested cases are: edge over \(\mathbb F_2\), three idempotents, 120 tuples; edge over \(\mathbb F_3\), two idempotents, 40 tuples; edge over \(\mathbb F_4\), two idempotents, 52 tuples; three-chain over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), two idempotents, respectively 340, 976, and 2116 tuples; three-point fork over \(\mathbb F_3\), two idempotents, 400 tuples; four-point diamond over \(\mathbb F_2\), two idempotents, 4132 tuples. Every test checks all color fibers and tangent dimensions, followed by `VERIFY_OK`.

These are finite, exhaustive tests **only for the named small algebras**. They do not computationally prove the theorem for every finite poset, any larger tuple, any other finite field, or arbitrary infinite fields. Those quantifiers are established by the explicit conjugator, stabilizer computation, and tangent-space proof in `RESULT.md`. The Tutte recovery follows symbolically from the exact edge expansion. Independent audit remains unperformed.
