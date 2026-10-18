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

Pure-loss Kraus/binomial thinning acts on photon-number probabilities and gives W_out(0)=(2/pi)sum_j p_j(1-2eta)^j even for coherent density matrices. If eta<=1/2 all summands are nonnegative; if eta=1 the output equals the initially constrained Wigner origin. For r=2eta-1 in (0,1), initial parity >=0 says odd population w<=1/2. Even j<=2m implies r^j>=r^(2m), odd j>=1 implies r^j<=r, whence W_out>=(r^(2m)-r)/pi. Equality requires precisely p_1=p_(2m)=1/2 and all other diagonals zero, with positivity allowing only their mutual coherence. Strict convexity of r^(2m)-r gives unique r_m=(2m)^(-1/(2m-1)), B_K and unique attenuation. Adjacent even/odd plateaus and strict decreasing even steps follow directly; limit is -1/pi. K>=2 scope and origin-vs-global-positivity distinction are essential.

## originality

PASS

Known Wigner parity and binomial pure-loss identities are prior ingredients. Kenfack–Życzkowski optimize/measure integrated Wigner negativity; Genoni et al. bound origin Wigner values for mixtures of Gaussian states at fixed energy and discuss loss. Neither inspected theorem is an optimization over every cutoff state constrained only by initial origin positivity and all attenuations; no published equality classification or staircase covering the final exact problem was found. This is best-of-knowledge O with uninspected specialized lossy Fock-state literature risk.

## value

PASS

The Wigner function at the origin is a directly measurable parity observable and cutoff limits are natural finite-photon resources. How much loss can expose negative origin parity starting with a nonnegative origin is a precise physically meaningful optimization. The exact floor, optimizer, two-step staircase and asymptotic limit answer that constrained question rather than merely reprinting a known thinning formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
