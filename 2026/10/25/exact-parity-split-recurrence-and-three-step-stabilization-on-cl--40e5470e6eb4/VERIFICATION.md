---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Every private leaf copies its core state at each update. A clique vertex sees S−x_i+y_i ones out of m neighbors. For m=2k this yields three branches x′=0 if S<k, x′=y if S=k, x′=1 if S>k; paired balanced words give c² recurrent states plus 2 homogeneous states. The other first-entry classes partition by whether x is homogeneous and whether the next core is balanced, homogeneous, or intermediate, giving D1=2(2^m−1), D3=c(2^m−c−2). For m=2k+1, borderline outputs are (1−x)∧y at S=k or (1−x)∨y at S=k+1; disjointness/complement-cover forces only recurrent balanced-border pairs, 2c(k+2) plus 2 homogeneous states, and their free leaf-bit multiplicities yield D1 and D3. D2 is the nonnegative complement of the partition. Stirling's central binomial estimate gives even recurrence fraction 2/(πm) and odd 2^(−m)√(2m/π). Fresh independent direct-neighborhood orbit enumeration for m=3..7 (21,824 labelled states) matched exact formulas, including m=3 depth vector (20,32,12,0), m=5 (82,302,400,240), m=6 (402,126,2728,840), and fixed counts. All-order proof comes from the branch partition, not finite checks.

## originality

PASS

A fresh closest-prior comparison finds no accessible theorem or database record implying the final all-parameter conclusion. The exact overlap/special-case antecedents are credited and remaining literature-access or terminology risks are recorded; PASS is a best-of-knowledge judgment, not external historical certification. Exact parity-split recurrence and three-step stabilization on clique coronas: Tie-retaining synchronous binary majority on K_m∘K1 for every m≥3 has exact transient-depth counts D0..D3, fixed and primitive two-cycle counts, sharp depth ≤3 (depth ≤2 at m=3), and sharply different even/odd recurrent-state asymptotics.

## value

PASS

A complete distribution of first entrance into periodic states, including the sharp bounded transient and a dramatic even/odd asymptotic recurrence split, is a natural dynamical invariant for a dense binary majority network with attached one-step-memory leaves. General period≤2 results alone do not give basin-depth populations. The result addresses synchronous unweighted tie-retaining majority only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
