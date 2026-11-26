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

The joint post-crossing state is always vacancy at n−1 and gate ON. The strong Markov property gives iid complete intervals, not an ordinary forward waiting time from a stationary observation epoch. The next m ungated jumps form an independent rate-one Erlang traversal S. Put a=(1−p)κ, b=pκ; the two-state killed service generator yields φ_ON=r(s+b)/Q and φ_OFF=rb/Q for Q=s²+(r+κ)s+rb. Weighting by p+(1−p)e^(−κS) and integrating gives exactly Φ. From ΦQ=N, −Φ′(0)=(Q′−N′)/(rb) and Φ″(0)=(N″−2+2μQ′)/(rb), recovering both displayed moments. The extra term in μ is (1−p)/p times the strictly decreasing integral m∫₀¹(1+κv)^(−m−1)dv. Renewal reward and particle conservation give equal current on all bonds; the counting variance rate is Var(τ)/μ³, including the stationary delayed process since the finite phase-type times have exponential moments. At small κ the numerator of the second moment tends to 2r(m+1/r)(1−p)/p and μ→(m+1/r)/p. At large κ the same moment formulas give μ→m+1/(rp) and Var(τ)→m+(rp)^(−2), not merely convergence in distribution. The fast Fano factor is strictly below one, so continuity with the divergent slow end proves existence (not uniqueness) of a finite crossing. Independent exact replay: python3 /workspace/branches/independent_checks.py 1 solves stationary and tilted-generator Poisson equations; it matches the current and Fano factor at three rational instances, from F≈13.114 at κ=1/30 to F≈0.149 at κ=51. The frozen checker was read, not run. Its printed 96 tally counts four categories per parameter point, although the Laplace category has two frequency equality assertions; this bookkeeping does not affect the proof.

## originality

PASS

Pass for the combined one-vacancy current and counting-noise law, including fixed-open-fraction speed monotonicity and the slow Fano prefactor. Gated reaction renewal is prior and even admits a close reduction of the interval law via independent bond attempt times as instantaneous contacts. The closest inspected exclusion formulas and catalogued Fano crossover do not cover this generator and statistic together. Neither a new general renewal method nor priority over all gated-service models is claimed.

## value

PASS

Transmission current alone would suggest throughput remains regular as the gate slows, whereas its asymptotic count variance becomes very large. The positive limiting current, sharp noise coefficient, and forced approach to sub-Poisson noise supply an exact benchmark where effective-rate averaging loses important information. This is useful in the single-vacancy sector and does not claim a general-density law or a unique crossover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
