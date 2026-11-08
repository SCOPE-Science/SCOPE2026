---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The orthogonal spectral projections give ||Re(e^{-iθ}T)||²=M² max(cos²θ,r² cos²(θ−β)); this remains true in arbitrary Hilbert dimension and with a zero complement. The difference is A+R cos(2θ−γ), with A=(1−r²)/2>0 and R²−A²=r² sin²β; integrate its absolute value to derive 1/2+[r sinβ−A atan(r sinβ/A)]/pi. Its derivative wrt s=sinβ is r³s²/[pi(A²+r²s²)]>0. Writing x=r sinβ/A, the ratio (x−atan x)/x³ = integral_0^1 v²/(1+x²v²)dv strictly decreases, giving sharp upper/lower cubic coefficients, equality only at stated endpoints/limits. Taylor gives cubic β turn-on; r=1−ε,β=εt gives the uniform compact crossover. Independent numerical quadrature of four generic parameter pairs matched the analytic formula; source checker tests further finite points. Prior published orthogonal-phase endpoint is not claimed new.

## originality

PASS

Best-of-knowledge distinct claim after comparison with directly relevant primary sources and published mathematical findings. Prior special cases and baseline formulas are explicitly credited. Complete historical originality is not certified.

## value

PASS

The newly introduced integrated Cartesian numerical radius for normal operators has qualitatively different behavior for two unequal-modulus eigenvalues than for fixed-modulus unitaries or rank-one operators. A fully sharp two-parameter dependence, optimal cubic control at fixed r, and singular near-equal-modulus crossover identify a motivated spectral response and equality boundaries rather than a trivial inequality restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
