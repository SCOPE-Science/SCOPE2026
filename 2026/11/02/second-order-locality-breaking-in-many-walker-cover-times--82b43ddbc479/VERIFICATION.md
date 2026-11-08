---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For finite irreducible continuous-time Markov chains and farthest target distance d>=2, killing Q on a nonempty J subset of farthest targets yields analytic F_J(t)=A_J t^d+B_J t^(d+1)+O(t^(d+2)). Direct first-hit path integration gives A_J=W_d(J)/d! and B_J=[W_(d+1)(J)-L_d(J)]/(d+1)!, with L_d summing exit rates at PRE-hit vertices only. Exact inclusion-exclusion of no-walker-hit events and δ=N^(-1/d) give a two-term exponential expansion; the binomial-log F_J^2 term is O(N^-1)=o(δ) precisely when d>=2. A union bound controls nearer targets at order o(N^(-(m+1)/d)); finite irreducible hitting tails justify integration for any real m>0. Attaching a non-target pendant at a shortest-path vertex changes no d or d+1 first-hit paths, but adds r to one exit rate, changing B by -r W_v/(d+1)!, hence raises K1 strictly for unique farthest target. Independent killed-generator power expansions for the 4- and 5-state tree give (A,B)=(1/2,-2/3) and (1/2,-5/6), matching mean second coefficients 4/3 and 5/3.

## originality

PASS

Kim-Lawley 2024/2026 arXiv:2310.07905v2 provides EXACT leading many-walker cover-time law K0 and shortest geodesic localization using inclusion-exclusion. The assessed result computes K1 from next-jump paths and prehit holding rates and establishes a concrete off-shortest-path perturbation. Lawley 2020 fastest passage gives first-order Weibull moments. Standard second-order extreme-value expansions might imply a SINGLE-J expansion but not the full target inclusion-exclusion/near-target truncation without extra argument.

## value

PASS

The finite-state second-order coefficient separates geodesic products from exit-rate effects and quantifies exactly when/why the leading locality principle breaks. This is a motivated structural asymptotic with explicit counterexample on a tiny non-target pendant edge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
