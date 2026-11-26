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

For fixed b and a uniformly sampled fixed cylinder, the avoider generating function gives the dominant root equation a*D_w(a)=h, with a=1-lambda_w and D_w(a)=sum_p chi_p b^-p(1-a)^(n-p-1). Near a=0 and up to 2h the derivative is positive for large n, uniformly in w; the equation brackets the first positive a between h/2 and 2h. The corresponding root is a pole, since the autocorrelation numerator is nonzero there, and there is no larger admissible Perron root. Thus Gamma_n/h=1/(1+S_w)+O_b(nh), where S_w=sum_{p>0}chi_p b^-p and E S_w=(n-1)h, proving the absolute-mean claim. For least period q<=n/2, Fine–Wilf gives exactly a_b(q) words and excludes all nonmultiples p<=n-q. For Z=(1+S_w)^-1-1 this gives Z=-b^-q+O_b(b^(q-n)); multiplying the squared-error difference by a_b(q) and summing costs O_b(sqrt(h)). The omitted tail of C_b has the same bound. For q>n/2, |Z|<=S_w=O_b(sqrt(h)), so E[Z^2; q>n/2]/h=O_b(n sqrt(h)). The root-approximation cross term and the centering term cost O_b(n^2 h) after dividing the standardized variance by h. This proves the positive cubic variance constant and stated error. The exact interpretation is domination by short symbolic periods: the all-(b-1) cylinder comes from the left side of the endpoint 1, not a period-one point inside that half-open cylinder. Its symbolic contribution b^-2 to C_b is already counted. The variance scale is an RMS scale, not a typical-hole fluctuation scale.

## originality

PASS

The exact escape equation, short-period asymptotics, primitive counts and ensemble mean are established tools/results. The distinct supported claim is the second central moment across uniformly sampled fixed cylinders, with explicit nonzero primitive-period constant and a uniform remainder at fixed b. No equivalent coverage of that asymptotic was identified in the inspected material.

## value

PASS

The result distinguishes fixed-placement uncertainty from the already studied mean escape and explains how a population with Gamma_n/h converging to 1 in L1 still has an RMS scale h^(3/2). The explicit nonzero coefficient resolves how much short symbolic periods contribute and the uniform tail estimate rules out a competing contribution from the many typical holes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
