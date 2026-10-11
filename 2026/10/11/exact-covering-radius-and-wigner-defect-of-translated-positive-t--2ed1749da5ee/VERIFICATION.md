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

The final theorem was checked directly from the definitions of the trace metric, covering radius, and Wigner comparison class. The critical identity is the exact projection formula

\[
\operatorname{dist}_1(B,P+\mathcal C)=\operatorname{Tr}(B-P)_-.
\]

For the lower bound, the support projection of the negative part is a trace-dual witness against every positive correction. For the upper bound, the positive part \((B-P)_+\) is an admissible correction and attains equality. The variational formula for the negative part gives the uniform upper bound \(\operatorname{Tr}P\), while the target \(B=0\) attains it.

The Wigner comparison is independently exact: evaluating at \(A=0\) forces error at least \(\operatorname{Tr}P\) for every Wigner symmetry, and the original conjugation \(U\) attains that value for every \(A\).

No numerical calculation, finite enumeration, or asymptotic passage is used. No assertion is made for the Bures metric or for arbitrary nonstandard isometries.
