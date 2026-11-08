---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

At ab=2/5 the Zibulski–Zeevi matrix has 2 rows and 5 columns. Explicit even/odd Laurent Zak terms for Q2 and neighboring sample values x,x+2/5,x+4/5 yield two exact cubic determinants in t=z². Independently expanded both: left–left h(-t³+2t²+2epsilon t+1) and left–central -h t(t-1)²+(epsilon-u)(A+Bt). Both exclude ±1 unit roots by signs and nonreal unit pairs by cubic coefficient/root-product constraints. Reflection gives right-hand pairs; four position cases for epsilon>1/10 cover x∈[0,1/5], so a continuous compact torus full-row-rank argument implies uniform positive frame bound. For epsilon≤1/10, at x=epsilon,z=-1 all five wrapped samples lie in the central Zak-zero interval so a row vanishes, preventing a frame. Used the quoted rational-density Zibulski–Zeevi equivalence, not finite samples, to conclude iff b>21/10.

## originality

PASS

The sharp 2/5 rational-density converse occupies the first non-unit numerator case left open by Stangl–Frederick. The known obstruction b≤2+1/(2q) with q=5 is fully credited, and no novelty is claimed for p=1 integer oversampling or the ZZ criterion.

## value

PASS

The published general necessary obstruction is explicitly left without a p>1 converse. Proving the complete first natural non-integer rational slice p=2,q=5 and matching threshold provides an independent substantive frame theorem, not merely a sample rank calculation. Exact zero-free minor patterns are mathematically reusable for other rational Zak sampling problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
