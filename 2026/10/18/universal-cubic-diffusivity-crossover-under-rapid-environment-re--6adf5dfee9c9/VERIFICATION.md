---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Regeneration gives independent pairs (L,Z_L), E L=1/p and centered-block CLT σ²=p²Σ_m r^{m−1}E[(Z_m−mv)^2], v=p²Σ_m r^{m−1}E Z_m. Enumerating all 2+4+8+16=30 static histories needs only mean a and second site moment b. I independently implemented symbolic enumeration from departure-count products and confirmed exactly all eight E Z_m and E Z_m² formulas for m≤4; series substitution yields coefficients (1−δ²,0,12δ²s,−8s²), verified independently in SymPy, output ALL_INDEPENDENT_CHECKS_PASS. On |r|≤1/2, bounded increments |Z_m|≤m yield |v|≤9 and |Σ|≤2700, so Cauchy estimates |Σ_k|≤2700·2^k and geometric summation yields 86400r⁴ on [0,1/4]. Comparing signal 12ηs²r³ against error proves both strict sign windows if r<ην²/7200, and taking δ/√r→κ,s→s0 yields sharp 4s0(3κ²−2s0). Assumptions apply to arbitrary site laws including atoms at 0,1; CLT is annealed regenerative, not quenched.

## originality

PASS

Martin–Nagel 2026 supplies regenerative variance expression and shows first p-derivative zero and second derivative positive when drift≠0 (their Theorem 2.4 and Lemma 3.3). Their inspected statements do not settle the degeneracy δ=0, its negative third-order coefficient or a law-uniform transition when δ varies with r. These quantified conclusions are new relative to the primary source as read; cooling-environment papers use deterministic refresh schedules rather than geometric regeneration.

## value

PASS

Determining the previously degenerate centered random environment response resolves the local maximum/minimum reversal in an established stochastic homogenization model. Uniform order-r³ asymptotics and sharp δ²~sr sign boundary supply a natural physically meaningful crossover not inferable from known first two derivatives alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
