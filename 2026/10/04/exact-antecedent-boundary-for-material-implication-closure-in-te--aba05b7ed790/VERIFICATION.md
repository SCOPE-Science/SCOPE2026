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

The theorem is proved symbolically by reducing the two material conditionals to operations on families of teams:
\[
M(P,Q)=(\mathcal T\setminus P)\cup Q,
\qquad
M^\circ(P,Q)=\{\varnothing\}\cup M(P,Q).
\]

For union closure, every failure of nonempty-downward closure gives a witness
\[
Q=\{T\setminus A\},
\]
while the converse follows because a failed output union would force both nonempty input teams into \(P\) and then into \(Q\).

For strong intersection closure, every failure of proper-upward closure gives a witness
\[
Q=\{T\cup(\Omega\setminus A)\}.
\]
For weak material implication the same witness works whenever \(T\ne\varnothing\), and \(\varnothing\) is the only additional protected intersection because it is inserted into every weak-material truth family.

The bundled `verify.py` exhaustively checks every antecedent \(P\), every union-closed consequent, and every intersection-closed consequent for base sizes \(1,2,3\). It also checks the finite structural corollaries through base size \(4\). It prints `VERIFY_OK`.

## Limits

The finite checker corroborates the proof and is not used to extrapolate it. The convexity-preservation problem and arbitrary conditional operators are outside the claim.
