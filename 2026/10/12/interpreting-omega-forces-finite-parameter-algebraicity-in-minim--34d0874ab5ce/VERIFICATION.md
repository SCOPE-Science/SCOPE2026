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

The primary full text was checked at Proposition 5.2, which reduces any finite-dimensional interpretation of an infinite linear order to dimension \(1\) and preserves order type \(\omega\) when the original interpreted order is \((\omega,<)\). Definition 2.9 and the surrounding discussion were also checked: in a minimal structure the levels of a dimension-one \(\omega\)-interpretation are finite.

For completeness, the algebraicity step was replayed directly. Fix the finite parameter set \(A\) used to define the dimension-one quotient. For each fixed \(n<\omega\), the \(n\)-th point of \((\omega,<)\) is first-order definable from the order alone, so its pullback \(L_n\) is \(A\)-definable. The \(L_n\) are nonempty, pairwise disjoint, and cover \(M\). If one were infinite, minimality would make it cofinite, leaving only finitely many points for infinitely many other nonempty levels. Hence every \(L_n\) is finite. Every \(a\in M\) therefore lies in a finite \(A\)-definable set and belongs to \(\operatorname{acl}(A)\).

The locally finite algebraic-closure corollary is a contradiction argument: if \(\operatorname{acl}(A)\cap M\) is finite for every finite \(A\), the inclusion \(M\subseteq\operatorname{acl}(A)\) is impossible for infinite \(M\).

No computation or experimental evidence is used. The statement does not claim a converse and does not extend the algebraicity conclusion to arbitrary interpreted infinite linear orders.
