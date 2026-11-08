---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. The embedded affine recurrence Z=aZ+aB_E gives the infinite product, while stationary active/refractory weights produce the exact mixture (shape-independent for finite E[R]); normalization d=D/r and w=r E[R]/(1+r E[R]) checked. Frullani yields the symmetric Lévy density with K(t)=sum_{j>=0} exp[-t/(a^j sqrt d)]-exp[-t/sqrt(wd)]. K is pointwise nonnegative because its j=0 term dominates the subtracted term, with logarithmic near-zero growth and exponential tails; thus Lévy integrability holds. The classical Sato radial-profile monotonicity criterion implies SD iff K is decreasing. At w=a^(2m), the j=m term cancels; at a=1/100,w=a^(2m+1), at s=a^m/10, scaled derivative obstruction has negative term 10/e and positive sum bounded by 100/99+200e^-10<2; hence K prime>0, all m>=1. Exact cumulant formula and odd vanishing consistent. Independent finite check for m=1,2,3 verified the strict bound numerically; it is not the infinite proof. w=0 convention and tau=0 endpoint accounted for.

## originality

PASS

Qualified PASS for the explicit positive Lévy kernel and a self-decomposability/non-self-decomposability phase alternation under arbitrarily small positive refractory occupation. The equilibrium characteristic function, infinite product, and nonrefractory Laplace convolution are old, not claimed as new. Best-of-knowledge comparison of the actual model and implications finds no established earlier occupancy-interlacing result; lack of an exhaustive priority search remains a risk.

## value

PASS

PASS. A stationary stochastic resetting model has a natural divisibility hierarchy relevant to Lévy-driven representations and AR laws. The property of all-occupancy infinite divisibility alongside alternating self-decomposability in arbitrarily small positive occupancy is a sharp, non-obvious qualitative boundary, not just routine cumulant computation. It gives explicit parameter witnesses rather than an unsupported full phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
