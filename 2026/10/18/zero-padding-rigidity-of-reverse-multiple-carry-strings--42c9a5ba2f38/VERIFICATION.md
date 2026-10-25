---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For a genuine (n,b) reverse multiple, b≥3, 2≤n<b, nonzero endpoint digits, the grade-school recurrence b c_(j+1)=n d_(k−j)+c_j−d_j with c_0=c_(k+1)=0 ensures 0≤c_j≤n−1. Eliminating paired reversed digits gives (n²−1)d_j=nb c_(k−j+1)−n c_(k−j)+b c_(j+1)−c_j. At j=k this yields (n²−1)d_k=nb c_1−c_k>0, forcing c_1>0. If c_k=c_(k−1)=0, the j=0,1 identities force D=n²−1 to divide b c_1 and b c_2−c_1. Multiplying the first by c_2 and second by c_1 and subtracting yields D|c_1²; but 0<c_1²≤(n−1)²<D, contradiction. In an outer-zero padded contiguous carry string, c_0=0 and c_1>0 force exactly one lower zero; two-highest-zero exclusion allows at most one upper zero. Only necessary shapes (d_m..d_0,0) and (0,d_m..d_0,0) survive, not asserted realizable. Independently checked modular obstruction for n=2..39, n<b≤59; this supplements exact universal inequality, not a surrogate for proof. Scope excludes internal digit insertions and other derived constructions.

## originality

PASS

Best-of-knowledge PASS specifically for the two-top-zero modular-square obstruction and its *outer-zero contiguous* corollary. Holt 2014 already gives carry bounds, paired-digit identity and c1 positivity. Holt 2016 introduces singly/doubly derived carry encodings and discusses broader open types; the narrow obstruction does not claim those open problems all solved. No source inspected states D|c1² as a universal two-highest-carry exclusion.

## value

PASS

The source and literature motivate a concrete open-ended classification of derived palintiple carry encodings. The new D|c_1² boundary obstruction is a universal structural lemma, ruling out all longer exterior zero-padding of an intact source carry word. Though elementary and deliberately narrow, it gives a principled impossibility boundary for the precisely defined family without claiming to resolve arbitrary third/fourth derivations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
