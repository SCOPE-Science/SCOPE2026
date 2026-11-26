---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At a=2/5 the four equal cells have full surviving transitions A→C,D; B→B; C→C; D→A,B, modulo endpoints. Each n-arrow cylinder has length 1/(5·2^n), and M^n1=(n+1,1,1,n+1). The n+2 entry categories (start inside, enter at each k=1,…,n, never enter by n) contain exactly two cylinders each. This proves the survivor and conditional entry laws; normalization by 4/5 and successive differences give P(N=n)=n/2^(n+1), whose mean and variance are 3 and 4. The power series sums to (4−z)/(5(1−z/2)^2); the entry limit follows by Riemann sums. For a≤1/3 the only surviving positive-length branches alternate the two outer intervals, with inverse length ratio 1/2; the isolated equality endpoint has zero mass. Independently enumerated by integer forward iteration on the exact preimage mesh: 13 conditional histograms for a=2/5, n=0–12, and 30 survivor counts at a=1/3, 2/7, 3/11, n=0–9, all agree. Replay: /workspace/branches/independent_checks.js. This finite check is not an all-n proof; the frozen verifier was inspected, not executed.

## originality

PASS

Inspected earlier sources cover the location of the period-four change and the symbolic/periodic survivor structure, not the transient path weights or the entry-time law. Two distinct later catalogue records do cover the numerical laws, including the complete conditional law after an index shift; neither establishes prior coverage of the frozen finding. No earlier or same-day equivalent was identified in the searches performed. The supported distinction is the finite-time Lebesgue and conditional-history laws, not the orbit classification or the Markov method.

## value

PASS

The parameter is a previously identified periodic boundary, not a chosen numerical slice. The linear survival prefactor distinguishes the transient reducible dynamics from the geometric phase despite the same exponential rate, and the exact uniform conditioned switching categories explain where that prefactor comes from. This supplies a useful critical-hole benchmark beyond the zeta/periodic information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
