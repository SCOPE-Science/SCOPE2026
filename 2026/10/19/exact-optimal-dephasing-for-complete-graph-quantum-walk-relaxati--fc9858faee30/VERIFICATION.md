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

Independent full-spectrum derivation: let K=−i[H,·], z=λ+γ, and ω=nJ. The two cross-block spaces for the uniform-vector projector P and I−P give eigenvalues ±iω, each n−1 times; the two diagonal blocks give zero n²−2n+2 times. The dephasing is −γI plus γ times the projection to the site diagonal. Compress (zI−K)^{-1} to that diagonal: its constant direction has resolvent 1/z, and any traceless diagonal direction puts squared norm fractions 1/n in each cross-block (PDP=0 and ||PD||²_F=||D||²_F/n). Polarization gives the scalar compression (1−2/n)/z+(2/n)z/(z²+ω²) on the traceless diagonal. The finite-rank determinant lemma now gives λ(λ+γ)^((n−1)(n−2)) times the stated cubic to the power n−1, by rational identity and polynomial continuation. Its constant term is positive, zero is simple, and the cubic is stable by Hurwitz. A negative real cubic root −r exists for every γ>0; regarding its equation as quadratic in γ gives discriminant 4nJ²[nJ²−(n−2)r²]. Since g≤r, equality with the bound forces the repeated solution γ=(n−1)r. At that γ the factor λ+r has r=J√(n/(n−2)), the other two cubic roots have real part −(n−3/2)r and negative quadratic discriminant, and −γ also decays faster for every n≥3. This checks global attainment and uniqueness without a dominant-root assumption away from the optimum. The supplied spot-check code and recorded evidence were read, not executed.

## originality

PASS

There is demonstrable prior overlap in the exact reduced cubic. Credit the indexed hub-return result for this reduction at J=1, and Bressanini et al. for studying the same open-system model. The distinct supported finding is the full-matrix characteristic polynomial with multiplicities and the unique optimizer of the spectral gap. Neither a launch-restricted cubic nor an optimum for an integrated return signal settles those claims. The strongest inspected primary source statements also do not establish them.

## value

PASS

The complete graph is a natural test case for separating dephasing-induced relaxation from strong-dephasing slowdown. The exact spectrum with multiplicities permits direct benchmarks in every size, and the exact optimizer and maximum give a non-asymptotic target rather than a finite-time proxy or a scaling guess. No new value is assigned to recovering the previously known launch cubic alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
