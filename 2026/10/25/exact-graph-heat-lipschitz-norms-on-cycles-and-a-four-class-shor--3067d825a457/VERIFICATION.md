---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS — On C_n (n≥5), a graph-Lipschitz potential corresponds exactly to mean-zero edge gradients g_j of magnitude ≤1. ℓ1/ℓ∞ duality makes norm equal min_c Σ|p_t(j)−c|. For t>0, radial heat differences solve irreducible Metzler tridiagonal ODE with positive initial first coordinate, so p_t(0)>p_t(1)>...>p_t(⌊n/2⌋). Counting radial multiplicities proves the same median p_t(k), k=⌊(n+2)/4⌋, for all t. The stated zero-sum gradient g=1,(n−4k)/2,−1 is a simultaneous extremizer. Unique shortest k-walk gives p_t(k)=t^k/k!+O_n(t^(k+1)), hence leading defect (4k+2−n)/k!, positive for each residue class n mod 4. Positivity and semigroup norm submultiplicativity give strict all-time decay; t=0 and fixed-n asymptotic handled. Independently checked 24 LP norms against median and 11 exact Taylor coefficients, not as proof of infinite n.

## originality

PASS

PASS, qualified — Ollivier/Veysseire/Jost–Liu provide transport-curvature and general nonexpansivity/contraction tools, not the sharp all-t norm for every n≥5 nor the median p_t(⌊(n+2)/4⌋) and one time-independent extremizer. General curvature upper estimates need not yield the high-order t^k contraction defect; for large n curvature bounds are too coarse. No covering published finding in Resultary top hits. Prior spectral/cyclic-transport exact calculations under alternate vocabulary remain a risk.

## value

PASS

PASS — Graph heat transport/Lipschitz decay on all finite unweighted cycles is a canonical model. The exact all-time norm, simultaneous maximizing potential, and growing residue-dependent first nonzero contraction derivative quantify regularization not obtainable from mere curvature/nonexpansivity bounds. All-n structural theorem with sharp coefficient has independent geometric meaning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
