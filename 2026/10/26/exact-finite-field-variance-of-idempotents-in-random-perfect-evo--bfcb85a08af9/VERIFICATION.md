---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Write Q=q^n. Each x≠0 is an idempotent with probability 1/(Q−1) by transitivity on nonzero vectors. Distinct collinear vectors x and tx cannot both work, since then t²=t with t≠0,1. Among the (Q−1)(Q−q) ordered independent pairs, exactly those with dependent coordinatewise squares must be discarded; each remaining pair has joint probability 1/((Q−1)(Q−q)). With mean one this factorial moment is the variance. In characteristic two, squaring is an automorphism and preserves independence. In odd characteristic, for x with r nonzero coordinates, a proportional squared y has (q−1)/2 possible square ratios and 2^r sign patterns per ratio; exactly two patterns give collinear y. Summing binomially over support sizes gives (q−1)((2q−1)^n−2q^n+1)/2 excluded pairs. The r=2 term gives strict positivity of the defect, its expansion gives (2^(n−1)−1)q^(1−n)+O_n(q^(−n)), and n=1 gives the unique nonzero solution x=M^(-1). Independently looping over determinant-nonzero 2×2 matrices and counting solutions among nonzero pairs gives histograms 0:16, 1:20, 2:8, 3:4 over F3 and 0:60, 1:90, 3:30 over F4 (replay with F2[t]/(t²+t+1)), confirming 5/6 and 1. Inspected frozen verification notes and script without executing the uploaded script; the proof covers the universal claim, not the finite checks.

## originality

PASS

Credit the earlier mean and the earlier full characteristic-two distribution, not those moments as new. The supported distinct content at the frozen record's date is the uniform all-n exact odd-characteristic variance defect. A distinct November 2 Resultary record states the equivalent general formula and is recorded as direct coverage in the current catalog, not precedence over the October 26 finding. The inspected passage in that later record does not point to earlier coverage of the odd-characteristic formula. No earlier equivalent or mechanically stronger odd-characteristic theorem was identified in the checked material.

## value

PASS

The uniform invertible ensemble and the second factorial moment are motivated by an existing fixed-point prediction. The exact finite-field correction isolates an odd-characteristic obstruction due to square-map projective collisions, distinguishes finite from limiting behavior, and gives the size of the discrepancy uniformly in dimension and field size. This is useful independently of a full distribution and is not a recomputation of the known mean or characteristic-two law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
