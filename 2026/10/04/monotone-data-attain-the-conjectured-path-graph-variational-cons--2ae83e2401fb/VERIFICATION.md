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

The proof is analytic. The packaged checker is supplementary and uses exact rational arithmetic.

It enumerates all nondecreasing integer sequences with values in \(\{0,1,2,3\}\) for path lengths \(3\) through \(8\). For each sequence it computes the centered graph maximal function exactly, checks
\[
\operatorname{Var}(M_{P_n}f)
=
f(n)-\frac1n\sum_{j=1}^n f(j),
\]
checks the sharp bound
\[
\operatorname{Var}(M_{P_n}f)
\le
\left(1-\frac1n\right)\operatorname{Var}(f),
\]
and checks the equality classification for nonconstant inputs. It repeats the same tests after reflection for nonincreasing inputs.

Finite enumeration is not an infinite proof and is reported only as a reproducibility check.
