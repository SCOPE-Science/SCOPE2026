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

The symbolic proof uses the published operator ranges and self-selection behavior.

For Definition 5.1, each replacement set is a subset of \(F_\varphi\), and the source states that if
\[
G\in F_\varphi,
\]
then
\[
\mathcal R_a(G,\varphi)=\{G\}.
\]
Therefore a belief subcomplex is fixed exactly when all its facets satisfy \(\varphi\).

For Definition 5.2, every output again lies in \(F_\varphi\). If all current facets satisfy \(\varphi\), then for each input facet the internal same-perspective set is nonempty, lies inside the current belief-facet set, and contains the input facet. The union of these internal sets is therefore exactly the current facet set.

Both operators thus map every model into their own fixed-point class, which proves idempotence. If \(F_\psi\subseteq F_\varphi\), the output of \(\psi\)-revision already belongs to the fixed-point class of \(\varphi\), proving absorption.

The bundled `verify.py` independently implements the intended nearest-facet rule and the Grove-style fallback rule on finite uniquely colored facet systems. It exhaustively checks all two-agent binary-perspective models and sampled three-agent binary-perspective models.

## Limits

The checker is corroborative. The proof is not an extrapolation from finite enumeration. Modal-input revisions and memory-enriched variants are outside the claim.
