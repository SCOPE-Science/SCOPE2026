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

The argument was checked from the stated hypotheses with no computational experiment.

Chen's proof of Theorem 3.3 was inspected at the trace-pairing step: when the finite-flat rank is \(r\) and the distinct geometric-fiber count is \(s\), the trace radical is the nilradical and is locally free of rank \(r-s\); the quotient by it is finite étale of rank \(s\).

For the excess-one case, the remaining checks are elementary and explicit. Locally write the nilradical as \(N=A\varepsilon\). From \(\varepsilon^2=c\varepsilon\) and nilpotence one obtains \(c^n=0\) for some \(n\), hence \(c=0\) because \(A\) is reduced. Therefore \(N^2=0\).

The multiplication representation \(B\to\operatorname{End}_A(N)\cong A\) is an \(A\)-algebra retraction after passing to \(B/N\). Thus the finite étale reduction has a section and splits as \(A\times C\). The complementary idempotent lifts uniquely through \(N\); because the \(C\)-factor acts trivially on \(N\), the lifted component is exactly \(C\), while the other component is \(A\oplus N\) with square-zero multiplication.

The proof establishes a global statement because the nilradical is an invertible sheaf and the lifted idempotent is unique, so the local decompositions glue.

Limits checked: the reduced-base hypothesis is essential to the step from nilpotence of \(c\) to \(c=0\); no positive-characteristic extension is asserted; no claim is made for excess greater than one.
