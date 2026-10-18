---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For each odd N≥3 and distinct slopes, normalized quadratic Gauss sums at difference d=a−c and modulation offset ell have |G_N(d,ell)|²=Ng if g=gcd(d,N) divides ell, otherwise zero; this follows from grouping by g and the invertible (x−y,x+y) transform modulo odd N/g. Precisely N²/g modulation pairs are nonzero, yielding fourth-overlap cross-basis contribution g, while same slope contributes N. Thus Phi_2(A)=rN+2Σ_{unordered pairs}gcd(a−c,N). The classical identity gcd(k,N)=Σ_{m|gcd(k,N)}φ(m) rewrites the objective as a positive weighted sum of residue-binomial collisions modulo every m|N. For fixed r each collision sum is minimized exactly when m residue occupancies differ by ≤1, with C_m(r), and a cyclic consecutive r-interval attains all individual minima simultaneously. Positivity of every φ(m) proves the complete simultaneous balancing equality test and the nonnegative deficit. Full proof holds all odd N and r, including r=1,N; independent exhaustive integer check on all 2723 nonempty subsets for N=3,5,7,9,11 and bounded quadratic Gauss checks corroborated the arithmetic only.

## originality

PASS

Within the natural union-of-quadratic-chirp-bases family, the all-divisor exact fourth-overlap optimum and complete equality classification are not directly supplied by known Gauss magnitudes or general projective-design bounds. Similar published modular-balancing frame results optimize a different primitive-row Fourier kernel and are explicitly considered.

## value

PASS

The second projective frame potential measures the aggregate coherence of a natural, explicitly defined union of chirp orthonormal bases. The exact all-r optimization in every odd cyclic dimension and full equality/deficit characterization are useful design facts beyond maximum-pairwise-coherence benchmarks; their object and invariant are independently motivated and the answer is not implied by generic projective-design bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
