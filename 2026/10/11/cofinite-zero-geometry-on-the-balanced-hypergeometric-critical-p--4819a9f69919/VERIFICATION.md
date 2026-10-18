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

On b+c=3a+1/2 with positive a,b,c and neither b-a nor c-a a nonpositive integer, the published sector-uniform asymptotic has exactly matching z^(-2a) powers. After nonzero normalization, G(z)=R+cos(z-πa)+(d/2z)sin(z-πa)+O((1+exp|Im z|)/|z|²) on the closed right half-plane away from a compact disk. For |R|≠1, the model roots form two separated simple 2π-periodic strings. Away from fixed disjoint root disks the model has a uniform lower bound c exp|Im z| (from periodicity on bounded-height strips and exponential growth at large height); the error is smaller for sufficiently large |z|. Rouché on each far-right disk counts exactly one zero, hence simple; no other large right-half-plane zeros occur. A simple-root Taylor expansion yields d/(2w)+O(n^-2). Real coefficients and one root per conjugation-invariant disk give the real-tail case |R|<1; disks disjoint from the real axis yield off-axis height arcosh|R| for |R|>1. Evenness handles the left side; bounded zeros and |R|=1 are excluded. Independently recomputed d=-3/16 at (a,b,c)=(1/4,1/8,9/8); finite parameter probes are not the infinite proof.

## originality

PASS

The leading asymptotic and some a=1 global real-zero regimes are explicitly preexisting. The claim is the additional exhaustive complex zero-location theorem on the equal-exponent boundary, with first shift, multiplicities, limiting heights, and real-zero counting for all allowed positive triples. Source eq. (2.1) contains no zero-by-zero global Rouché exhaustion; Prop. 5.1 treats different strict regions, and Theorem 7.1 is a special a=1 global-Laguerre–Pólya result. No dominating all-parameter critical-plane theorem was found in targeted searches. Best-of-knowledge only; the source asymptotic makes the derived claim comparatively close to prior work.

## value

PASS

The balanced plane is a natural transition where the algebraic and oscillatory terms have equal asymptotic weight. Explicit gamma-amplitude threshold |R|=1 separates ultimately real and nonreal zero strings, including a complete cofinite location and counting law. It resolves a meaningful critical boundary not just a parameter substitution or finite check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
