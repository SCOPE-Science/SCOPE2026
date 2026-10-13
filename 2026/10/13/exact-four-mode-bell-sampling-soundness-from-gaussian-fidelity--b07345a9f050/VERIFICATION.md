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

The analytic proof has two external mathematical inputs: the standard Bell-sampling Gaussianity test defined by the zero eigenspace of the Majorana bridge operator, and the four-mode positive-parity Gaussian-fidelity normal form. Both were checked against their primary literature.

The only new finite-dimensional spectral calculation is replayed by `artifacts/verify.py` using exact rational arithmetic. In the four-cube representation, the zero eigenspace consists of the six Walsh characters indexed by two-element subsets. The endpoint sum has coefficient \(1/2\) in each of those six normalized characters, so its kernel-projection norm squared is exactly \(6/4=3/2\). Since the endpoint sum has norm squared \(2\), the rejecting projection has norm squared \(1/2\).

The script also checks the resulting formula \(r_4=f(1-f)/2\) for representative rational values and the algebraic monotonicity identity
\[
\frac12y(1-y)-\frac12x(1-x)=\frac12(y-x)(1-x-y)
\]
for \(0\le x\le y\le1/2\), which justifies placing the worst case at the distance boundary.

The script is corroborative only. It does not establish the global four-mode normal form, and no finite enumeration is used as evidence for an infinite or continuous classification.
