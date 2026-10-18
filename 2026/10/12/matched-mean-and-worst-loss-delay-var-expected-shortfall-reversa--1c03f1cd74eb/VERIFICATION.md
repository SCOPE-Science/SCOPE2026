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

Set r=n(1-alpha). When r<1 VaR and integrated-quantile ES equal the sample maximum; at r=1 this formula transitions correctly. For 1<=r<2 VaR=L_(n-1) and ES=((r-1)L_(n-1)+L_n)/r; at fixed maximum ES is nondecreasing in VaR (strict for r>1), so strict opposite rankings are impossible. At the first feasible integer n*=ceil(2/(1-alpha)), 2<=r<3 and VaR is third-largest; witnesses A=(0,...,0,1,3,4), B=(0,...,0,2,2,4) share total 8 and max 4 while VaR(A)=1<2=VaR(B) but ES(A)-ES(B)=(3-r)/r>0. Own exact rational computations verify representative alpha including 0.95,0.975; algebra proves arbitrary alpha.

## originality

PASS

Best-of-knowledge statement-level novelty of the surviving claim after crediting overlap in actual primary texts; not a universal priority certificate. Exact quantile and ES definitions are established; the minimal n with matched mean and maximum and reversed rank is not stated in inspected paper. The proof is an elementary consequence of broad quantile formulas only after isolating the matched-maximum constraint; routine-derivation prior overlap is a real value/originality risk, but the sharp constrained boundary is an independently useful exact fact. Definition-level formulas alone do not explicitly classify minimal scenario support under the stated matched moments, though the deduction is short and residual significance/priority risks remain.

## value

PASS

The sharp minimum number of empirical scenarios where two widely used, non-equivalent tail measures can disagree even at matched mean and worst-case risk is a motivated structural risk-measure boundary. It emphasizes quantile atom conventions and supplies explicit portfolio comparison witnesses, not merely a generic statement that VaR and ES differ.

The dated certificate retains the supplied scientific assessment, sources and limitations.
