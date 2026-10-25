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

# Verification of the sheaf ultraproduct-covering theorem

The proof has no numerical certificates or computational dependencies. It was checked algebraically at each step:

- The reverse-inclusion tail sets on the clopen neighbourhood basis have the finite-intersection property, so the ultrafilter lemma produces an ultrafilter containing every tail.
- For every ultrafilter-large index subset \(J\), point separation by clopens gives \(\bigcap_{U\in J}U=\{x\}\). This step does not need a countable basis.
- The canonical binary comparison has source \(1\amalg1\), since each ultraproduct of terminal objects is terminal. Its target has a global section represented by the product of clopen characteristic sections.
- Filtered colimits commute with stalks. Equality of two product-sheaf germs requires one open neighbourhood on which all coordinate sections agree, which is stronger than coordinatewise equality in the individual stalks.
- A constant-zero germ is excluded because every clopen characteristic section is \(1\) at \(x\). A constant-one germ would force an open neighbourhood into the singleton \(\{x\}\), impossible at a nonisolated point.
- On discrete \(X\), every sheaf operation is pointwise; the ultrafilter two-tag partition principle proves both comparison arrows are pointwise isomorphisms.

Logical scope: the result concerns ultraproduct covering with the epi–mono factorisation. It makes no assertion that all sheaf categories in the statement satisfy further enrichment-base stability hypotheses. The full compact Stone negative case is present in earlier work, and a possibly stronger localic priority result is not excluded.

Independent audit and external validation were not performed.
