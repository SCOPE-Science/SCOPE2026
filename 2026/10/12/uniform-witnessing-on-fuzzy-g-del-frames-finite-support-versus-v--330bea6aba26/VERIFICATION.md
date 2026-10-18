---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

W is nonempty; arbitrary fuzzy row R:W^2->[0,1], unrestricted [0,1]-valued atomic valuations and Gödel implication a->b=1 if a<=b else b. Box inf attained under every valuation at all worlds iff row positive support finite: if finite, all zero-accessibility worlds give 1 and other values a finite set; if infinite, select a countable sequence of positive R values and let a single atom at u_j have strictly positive value min(R(w,u_j)/2,1/(j+1)) tending zero; elsewhere value1. Inf=0 unattained. Diamond sup min(R,v) universally attained iff positive level sets S_w(epsilon) are finite for every epsilon>0: if sup s>0 it equals a maximum on finite nonempty S_w(s/2), and if zero it is everywhere zero. Conversely infinitely many edges >=epsilon let atom values at distinct u_j tend from below to 0<c<epsilon, others zero; sup c unattained. Joint criterion finite support. Strict example R(w,n)=1/(n+1) on N has diamond c0 rows but infinite support. All modal formulas reduce to arbitrary value functions, so one-atom witnesses suffice. Finite exact program checks are supplementary, not proof of infinite cases; countable choice assumed.

## originality

PASS

The witnessed-model primary paper defines the class by attained infima/suprema and provides nonwitnessed models and finite-model proof search. The cited 2025 crisp counterpart studies model-dependent witnessing and decidability, not uniform all-valuations framewise characterization for arbitrary fuzzy R. The known finite branching/crisp phenomenon motivates the box half, while a c0-row condition allowing infinite positive support for diamond is the substantively new asymmetry. Resultary finite Gödel Kripke frame regrading is unrelated to infinite uniform attainment.

## value

PASS

A complete naturally motivated frame-invariant classification of a semantic property used by witnessed Gödel modal logics, distinguishing necessity and possibility on infinite weighted frames. The c0 but non-finitely-supported example supplies a structural separation valuable for selecting semantics without restricting the model universe to finite frames.

The dated certificate retains the supplied scientific assessment, sources and limitations.
