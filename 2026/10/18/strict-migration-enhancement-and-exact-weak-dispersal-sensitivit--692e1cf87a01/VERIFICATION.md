---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Exponentiating one season gives scalar e^(bh) times the block with favorable factor s=e^((a−b)h) and symmetric unfavorable diagonal p=(1+e^(−2mh))/2. With P advancing the favorable patch, E_3 E_2 E_1=(P^(−1)E_1)^3 follows by expanding the product and using P^3=I. Thus in the co-moving frame Λ=b+h^(−1) log R. Expansion of det(λI−B) gives f=λ³+(p−1)λ²+(p−1)sλ+(1−2p)s. The three directed cycle edges are positive for the entire parameter range. The positive Perron root is simple even at p=1, where the frame matrix is imprimitive; no simplicity of the full monodromy at zero is assumed. Its polynomial derivative is positive (other real roots are smaller; complex roots pair to a positive factor). With x=s^(1/3)>1, f(x,p)=x²(p−1)(x−1)²≤0; continuity to positive infinity gives R≥x, with equality only when p=1. Then f_p=R²+sR−2s≥x²(x−1)²>0. Implicit differentiation and p′=−h e^(−2mh) give the displayed positive derivative at all finite positive m and from the right at zero. At p=1, f_λ=3x², reducing the derivative to (x−1)²/(3x) with h=T/3. At a=b, scalar growth times column-stochastic migration gives Λ=a, including m=0; at m>0 the period product is positive since the three pair links all occur and the season matrices have positive diagonal. Independent replay `python3 /workspace/review_reproduction.py 4` computes the season exponentials and spectrum of the full period product without using the cubic. Three parameter sets corroborated strict finite comparisons and endpoint slopes (e.g. 0.0133778366 observed versus 0.0133778371 predicted); the equal-growth case also agreed. The replay is numerical and bounded; the algebra above proves the full quantifiers.

## originality

PASS

The distinct contribution is a proof of strict migration-intensity monotonicity for the exact model and all a>b, with its explicit weak-dispersal response. The rotating model, plotted trend, earlier upper bound, endpoint values and Perron–Frobenius tools are not the contribution. The motivating text illustrates the trend in a particular source–sink regime but does not prove it for all growth-rate contrasts or give the one-sided slope in the inspected passages.

## value

PASS

The rate derivative solves a concrete qualitative gap explicitly suggested by the source's figures in a motivated rotating network, where the effect of migration intensity need not follow fixed-network intuition. The sharp initial coefficient gives a usable sensitivity without repeatedly simulating period maps and quantifies exactly the vanishing response as the growth-rate contrast tends to zero. This is not merely reevaluation of the known ceiling or endpoint growth, and makes no claim about monotonicity in the period or other season graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
