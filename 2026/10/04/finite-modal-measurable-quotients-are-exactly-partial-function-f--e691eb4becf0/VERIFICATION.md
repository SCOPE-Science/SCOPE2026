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

The proof was reconstructed directly from the definitions.

For a finite measurable algebra, the null ideal has a largest member \(Z\). Closure of the ideal under \(\Diamond\) proves that a non-null atom cannot reach a null atom. If a non-null atom reached two distinct non-null atoms \(Q_0,Q_1\), the measurable sequence
\[
Q_0,\ Q_1,\ X,\ X,\ldots
\]
would have null intersection but its sequence of diamonds would have a non-null common atom, contradicting the defining marked-space condition.

The quotient map sending a measurable set to its surviving Boolean atoms was checked to have kernel exactly \(N\) and to intertwine \(\Diamond\) with inverse image under the induced partial function.

Conversely, inverse images under a partial function preserve arbitrary intersections on their domain, which verifies the marked-space condition with trivial null ideal.

The bundled `verify.py` exhausts all relations and all principal null ideals on one, two, and three atoms. It checks the marked-space condition over every finite family of measurable sets, which is exhaustive in a finite sigma-field, and compares it with the partial-function characterization. It also verifies the explicit smallest branching obstruction. The program prints `VERIFY_OK`.

## Limits

The computation only checks small finite atom sets; the proof establishes the theorem for every finite marked modal measurable space. No finite computation is used to infer the infinite-space claims.
