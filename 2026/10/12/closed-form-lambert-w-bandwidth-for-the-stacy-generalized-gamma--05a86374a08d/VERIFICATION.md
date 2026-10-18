---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For d>1, the logarithmic derivative (d-1)/x-p x^(p-1)/a^p has the unique zero m=a((d-1)/p)^(1/p) and changes sign there. The normalized density at r=(x/m)^p is exp((d-1)/p*(log r-r+1)); setting it to y gives r exp(-r)=e^-1 y^(p/(d-1)). Both branches W0 and W-1 exist exactly for y in (0,1), and x_±=m[-W_{0,-1}(z)]^(1/p) lie on the proper sides of m. Their difference and the ratio yield stated width and octave bandwidth, including p=1 gamma limit. Independently checked 3 nongamma (d,p,a,y) cases with direct density ratios (0.4,0.5,0.73) to near machine precision. All arguments are analytic, not inferred from samples.

## originality

PASS

LoPrete–Burge 2025/2026 derives the ordinary gamma (p=1) Lambert-W width and expressly proposes generalized gamma as future work, even suggesting an impossibility risk. The stated all-p>0 Stacy width as a nonlinear function of two W branches is not stated in that article. It follows with a simple, exact power-level change of variables, which limits depth but gives a genuinely defined wider family usable formula. Searches for Amoroso and powered-gamma width analogues found no exact published formula; equivalence under other nomenclature remains a risk. Do not represent search absence as proof.

## value

PASS

The 2026 motivating paper specifically poses Stacy generalized-gamma bandwidth beyond gamma as an unresolved future calculation and questions feasibility. The exact two-sided width and octave ratio resolve that explicit useful distributional invariant throughout the interior-mode regime. Although the algebra is a short power transformation, it supplies the precise earlier missing function and branch domain, not an arbitrary toy parameter slice or merely a retitling of gamma results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
