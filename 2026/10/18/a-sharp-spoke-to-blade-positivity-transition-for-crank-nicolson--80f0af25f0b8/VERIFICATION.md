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

Reconstructed the completed step T=2R-I and the orthogonal constant, hub contrast, blade contrast and intrablade spaces. With M=rs, N=M+1, the diagonal weights at the hub are (1/N,M/N,0,0), at a leaf (1/N,1/(MN),(r-1)/M,(s-1)/s), with rates (0,Nb,b,b+sa). The positive resolvent for h>0 follows from the irreducible Markov semigroup integral. Thus only the two strictly decreasing diagonals matter; both have unique roots at level 1/2 and the smaller root is included. At z=bh/2=1/(M-1), putting x=a/b, the leaf excess is (M-1)[r(M-1)-(r(s-2)+1)x]/[2M^2(r+x)]. This proves the switch, simultaneous equality and strict decrease in the leaf regime since its last resolvent term decreases strictly in a. For s>=3 the rescaling z=y/x gives limiting leaf level 1/s+(s-1)/(s(1+sy)); at y=1/(s-2) its derivative is nonzero. For s=2 the slow contribution is 1/2-z/2+3z^2/2+O(z^3). With eps=x^(-1/2) and z=eps*y, the rescaled residual is -y/2+1/(4y)+eps*(3y^2/2-1/(8y^2))+O(eps^2). The simple root yields y=1/sqrt(2)+eps/2+O(eps^2), including the claimed 1/a term after converting to h. Analytic checks prove the stated family. The inspected verify.py implements useful direct rational inversions and leading-order asymptotic probes; its 1290 groups are frozen reported evidence, not a new run and not a check of the second triangle coefficient.

## originality

PASS

The reversible resolvent-diagonal criterion and generic graph positivity bounds are covered. The supported distinct contribution is the explicit two-conductance windmill crossover, including its extended hub plateau and the sharp singular scales with coefficients. No equivalent or dominating evaluated classification was established in the closest available sources.

## value

PASS

The switch identifies the actual limiting vertex orbit on a natural hub-and-community diffusion network. It extends the exactly flat step range beyond homogeneous/saturated spokes, and explains why triangles require a different power-law timestep reduction than larger blades. This is an evaluated family law with practical step-selection meaning, not merely the generic resolvent test or a finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
