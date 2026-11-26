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

Each row and column sums to zero, so the positive-rate family has the unique uniform invariant law. The limiting weak rate c-t=1-2t is strictly positive for t<1/2; b-t>0 follows from (2-t)^2-h^2=10/3-4t>0, and a-t>0 is evident. The trace is -2(a+b+c), and each principal two-by-two minor is ab+bc+ca+t^2, e.g. (a+c)(a+b)-(a+t)(a-t), so the extra coefficients are 6 and 17/2 using a+b+c=3, ab=5/6+t and c(a+b)=2-t-t^2. The roots are 0,-3±1/sqrt(2), all simple. The phrase 'three nonzero-state modes' is a wording slip: there are two nonzero relaxation modes, as the displayed spectrum and the parenthetical specify. The activity is 2 by the trace, and the exit rates are 2+t, 2-(t+h)/2 and 2+(h-t)/2; the last is at most 2+1/sqrt(6) since h-t decreases. Each oriented stationary edge current equals 2t/3, giving the stated sum of logarithms with unordered-edge normalization. Only c-t vanishes at the excluded endpoint; (2t/3) log(1/(1-2t))=(1/3) log(1/(1-2t))+o(1). Continuity from zero then yields every finite prescribed s>=0 without monotonicity or attainment of infinity. One or two states admit no nonzero steady edge current by conservation. Replay is exact from the cofactor and rate identities; frozen verify.py was inspected, not executed, and its numerical samples do not establish any universal or limiting claim.

## originality

PASS

The supported distinct result is the existence of a strictly positive three-state family spanning every finite nonnegative stationary entropy production with the same entire simple real spectrum, uniform invariant law and fixed activity, and with bounded exits. The general uniform-stationary cycle spectrum and current formulas are not new and are available in the closest catalogue work. Neither that spectral formula nor the checked spectral-thermodynamic inequalities supply the simultaneous isospectral positive-rate trajectory approaching a one-way edge with nonzero current, which is the crucial existence statement here. The conclusion is bounded to the assessed sources, not a claim of chronological priority.

## value

PASS

This gives an exact identifiability boundary for a natural collection of thermodynamic observables, rather than a perturbative discrepancy between two generators. The full set of relaxation rates, stationary populations and overall jump count leave every finite entropy-production value compatible on the smallest possible network, without increasing exit rates. The point is restricted to strictly positive but not uniformly lower-bounded edge rates; observing eigenvectors, edge traffic or full kinetics is a different inverse problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
