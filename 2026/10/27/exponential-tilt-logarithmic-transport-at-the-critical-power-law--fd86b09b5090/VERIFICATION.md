---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The exponent is constant within each row. Integral tail bounds give Φ_a=a^(1−s_N)(1+O(1/a))/((s_N−1)ζ(s_N)); logarithmic summation yields m_N~I_λ log N/ζ(2) and the proposed masses of logarithmic age windows. For n/N→c>0, n^(2−s_N) is bounded and m_n~m_N. The truncated second moment is O(n) from Σ_(a<n)(2a+1)Φ_a. For k~d n/m_N the truncated sum divided by n converges in probability to d, and the omitted-tail probability kΦ_n is O(1/log N). The identity n(1−E exp(−T/n))=n(1−exp(−1/n))Σ exp(−a/n)Φ_a yields m_n+O(1): the lower-window correction is bounded by Σ_(a<n)aΦ_a/n=O(1), and for a≥n the tail sum is bounded by an exponential integral with factor n^(2−s_N). These bounds are row-wise for fixed λ, not uniform for fixed exponents in a neighborhood of two. The resulting exponential envelope on P(S_k≤n) gives Σ_(j≤n)u_j~n/m_N by dominated sums. Local masses genuinely are controlled: the geometric mixture gives log-convex Φ_j, and the increasing ratios Φ_j/Φ_(j−1) inductively make all nonconstant coefficients of 1/(ΣΦ_jz^j) nonpositive. Since U(z) is that reciprocal divided by 1−z, u_j decreases, and macroscopic forward/backward average bounds give u_j~1/m_N uniformly on compact proportional windows. Now P(A_N=a)=u_(N−a)Φ_a gives the stated ν_λ on subintervals of (0,1); its total mass one rules out endpoint mass. For the walk, solving (I+D)v=2Ds_ℓ⟨s_ℓ,v⟩ for D=diag(e^(−ik),1,e^(ik)) gives the unit-eigenvalue direction s_ℓ−i c tan(k/2)χ_A with c=√(2/(ℓ+2)). The cross term integrates to zero by reflection, and the average of 1/(1+c²tan²(k/2)) is 1/(1+c), giving precisely W and the dark and active cases. The dispersive phases have cos ω=−(2+ℓ cos k)/(ℓ+2), with zero group velocity only on a null set. Fourier shifts in the characteristic function of Y_a/a isolate the same-band terms by orthogonality, giving a zero atom of weight W; oscillatory Fourier integrals on the monotone phase arcs vanish at fixed sites, whose flat profile sums to W by Parseval. Thus for every exponent v∈(0,1), the probability of |Y_a|≤a^v tends to W (fixed-site lower bound and zero-velocity upper bound); finite propagation yields the split between exponent zero and one. Conditioning on A_N∈[N^α,N^β] makes the bounded-continuous test-function error uniform by ordinary sequential convergence and uniform continuity; the ages outside those windows have arbitrarily small limiting mass as α↓0, β↑1. This proves the position mixture, not independence of position from age. Supplied numerical diagnostics were not used to justify the asymptotic.

## originality

PASS

The exact flat-band weight, fixed-site localization, underlying ballistic transport and the fixed-exponent threshold are known. The supported distinct claim is the moving-exponent logarithmic position mixture together with the local renewal analysis for the stated interarrival array. A related Resultary theorem gives the same tilt for an age marginal in a different near-critical renewal law, but not the quantum-position conclusion or the exact row-wise law of this claim.

## value

PASS

At the natural divergent-mean threshold, a logarithmic observation scale separates persistent localization from transport over a continuum of scales that a single ballistic rescaling or an MSD misses. The exp(−λu) tilt quantifies how the moving exponent redistributes these scales, while the localization atom is identified separately for every coin. The row-uniform local renewal argument is substantive and explains why the limit is not a fixed-exponent substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
