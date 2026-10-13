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

The proof uses two cited infinite results and several elementary structural steps. Gvozdevsky supplies isotypy of \(A\times\mathbb Z\) for arbitrary infinite \(A,B\) and reflection of isomorphism by the finite-distance quotient. Friedman--Stanley supplies Borel completeness of countable linear orders.

The remaining steps were replayed symbolically in the self-review: the finite-distance classes of an order in \(\mathcal I\) are convex copies of \(\mathbb Z\), their quotient is an infinite linear order, isotypy forces both the local \(\mathbb Z\)-pattern and arbitrarily many mutually infinite-distance coordinates, and the coding map \(A\mapsto A\times\mathbb Z\) is coordinatewise continuous.

Run `python3 artifacts/verify.py`. The script enumerates every labeled finite linear order through size seven, forms a finite window of its lexicographic product, checks that the zero slice recovers the input relation exactly, and checks every coded comparison against the lexicographic formula. It prints `VERIFY_OK 7184502 exact assertions`.

The finite script is not evidence for the infinite isotypy or Borel-completeness theorems; those are source-backed mathematical inputs. Its purpose is to catch coding-direction or lexicographic-formula errors.
