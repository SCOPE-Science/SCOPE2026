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

Run `python3 verify.py` beside `certificate.json`.

The verifier checks the exact identities
\[
\Delta(f(a))=d(a),\qquad d(h(a))=d(a),\qquad d(g(a))=d(a)
\]
for all three source letters, where \(d(0)=-1\), \(d(1)=0\), and \(d(2)=1\). It also checks additivity on every ternary word of length at most \(6\), directly iterates the morphisms through level \(12\), and confirms that every level-\(n\) block has the claimed imbalance and minimum-length growth.

These finite checks verify the nonstandard algebraic ingredients and composition order. The theorem itself is infinite: the bundled proof uses the published suffix decomposition for arbitrary \(n\) and the analytic block-bound argument, not the finite replay, to establish the limit.

Independent audit has not been performed.
