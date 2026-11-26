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

Kraft gives the similarity dimension by r^s=1/q, and strong separation gives both Hausdorff dimension and injective coding. If N=q^n>L, a decoder cycle has length p>=N/L>1 because the total positive advance is a multiple of N. Distinct visited positions have distinct cyclic n-factors, so the repeated list of codeword indices is primitive and any common initial complete-codeword prefix has total length at most n-1. At the first different IFS symbol the cylinder gap is at least δ, scaled by the common-prefix ratio r^v, giving δr^{n-1}. The frozen arbitrary-cycle proof leaves out a genuine small-n case: a chosen decoder cycle can be a singleton when N<=L (binary {0,10,11}, n=1), and the ordinary gap of a singleton is undefined. For all N<=L the theorem as stated is proved instead by the alternating repetition of any two different IFS symbols. Its period 2 is at least N/L and its gap is at least δ>=δr^{n-1}. This covers the boundary without changing the claim or defining an empty minimum. An independent manual n=2 check for {0,10,11} parses the de Bruijn circle 0011 as 0,0,11 with p=3 and the required prefix bound. For the full sequence p tends to infinity, and pη^s>=L^{-1}(δ/r)^s by r^s=1/q. The hypotheses of Kong–Wang–Yu Theorem 1.3 are precisely strong separation, growing periods and positive liminf of this product; the weights r_i^s give normalized Hausdorff measure. Their Theorem 1.1 gives finiteness at s. The example's invariant square gives separation at least one; (4,0) is the fixed point of f_10 and (0,0) that of f_0, so (2,0) and (3,0) witness equality. VERIFICATION.md and artifacts/verify_prefix_orbits.py were inspected without executing the frozen code; the recorded finite checker does not establish the theorem.

## originality

PASS

Credit the inhomogeneous complete-prefix-code family and its quantitative decoder construction; homogeneous positivity, Kraft and de Bruijn ingredients, and the measure-convergence consequence are prior. The strongest adjacent positive inhomogeneous result also uses weighted symbolic separation but covers a different length profile.

## value

PASS

Critical positivity was missing beyond particular inhomogeneous cases. The exact winding argument supplies a uniform lower bound on the product of period and critical separation for an infinite natural family, with genuinely inhomogeneous examples. The same construction produces a concrete orbit sequence to which the prior distribution theorem applies. It is not a solution for general ratios.

The dated certificate retains the supplied scientific assessment, sources and limitations.
