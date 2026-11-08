---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Sobolewski–Ulas Cor. 3.3 yields chi(4n)=chi(n), chi(8n+2)=T_n, chi(8n+6)=0 and the explicit valuation description. Thue–Morse single-sign sums are O(1) and adjacent-sign correlation has dyadic recurrence C(2M)=-M-C(M), yielding pair frequencies 1/6,1/3,1/3,1/6 with O(log M). The four correct 16-site blocks and eight adjacent transitions yield per block frequencies (1/3,1/3,1/12,1/4,1/4,1/12), then dividing by 4/3 events per block gives asserted probabilities. Independent enumeration of 83,333 successive gaps below n=10^6 gave counts 20834,20833,5209,15624,15625,5208, consistent with limiting weights. Note original paper Prop. 3.4 displays T_n case labels opposite to its Cor.3.3(d); this proof uses the direct recurrence and independently verified block patterns, not the inconsistent printed labels.

## originality

PASS

Best-of-knowledge precise frequency vector and logarithmic discrepancy refine Sobolewski–Ulas 2023 Prop. 3.4, which proves only six possible gaps and infinite occurrence; Theorem 6.1 density of exceptional indices does not specify the conditional distribution of gap lengths. This natural statistic requires adjacent Thue–Morse pair correlation beyond set density.

## value

PASS

Exact probability distribution of every naturally occurring gap for an explicit automatic exceptional set, with quantitative discrepancy and moments, closes the natural first-order statistical classification left by the known six-value support theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
