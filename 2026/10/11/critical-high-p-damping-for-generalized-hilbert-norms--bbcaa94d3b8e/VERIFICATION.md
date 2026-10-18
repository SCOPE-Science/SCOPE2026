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

Set x=(alpha+2)/p in (0,1/2]. The exact cited operator identity yields xN=Gamma(1+x)Gamma(b+1-x)/Gamma(b+1). Taylor of both logarithms gives log(xN)=-x(gamma+psi(b+1))+O(x²). The trigamma remainder has argument >=1/2 and is bounded by pi²/2 uniformly b>=0, so uniformity is genuine even for moving superexponential b. For b→infinity, psi(b+1)=log b+O(1/b) yields N≈(p/(alpha+2)) exp(-(alpha+2)log b/p). Hence at log b=[p/(alpha+2)](log p+s+o(1)), N→e^-s/(alpha+2); moving s to ±infinity forces zero or infinity. Independent mpmath beta/gamma evaluations with p=200,400 and b=0,1,exp(2),exp(20) gave absolute log-remainders of order x² with bounded ratios. Numerical probes are supplementary.

## originality

PASS

The lead Li–Li–Pan–Wulan–Zhou paper gives the exact beta-function norm on the stated p range; that input is prior and cannot be republished as novel. Earlier Bergman and Hilbert essential-norm results do not state the simultaneous high-p, high-b uniform asymptotic or superexponential balancing threshold. These statements follow by additional uniform special-function analysis, but no checked indexed result explicitly covers the double-scaling phase.

## value

PASS

The generalized parameter b changes the weighted-Bergman Hilbert operator and naturally asks how growth in b offsets its high-p norm blow-up. Ordinary polynomial and exponential b do not stabilize the norm; an unexpectedly superexponential scale b≈p^{p/(alpha+2)} sharply separates blow-up and decay. The all-b uniformity and finite critical window are a useful natural two-parameter norm phase result, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
