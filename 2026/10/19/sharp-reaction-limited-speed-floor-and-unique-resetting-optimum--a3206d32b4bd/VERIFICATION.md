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

For generator D∂²−U∂ and the stated occupation-density convention, the rank-one Green function gives q=k exp(−t)/(k+√(U²+4Dr)); resetting renews after min(killing time, reset clock), of mean (1−q)/r and success probability q. Thus T=(1−q)/(rq), with r=(D/L²)t(2M+t). In the dimensionless objective the strictly positive summand (eᵗ−1)/[t(2M+t)] plus η[(M+t)/(2M+t)]eᵗ/t gives the strict floor and the trial t=1 approaches it as M→∞. At fixed M the objective diverges at both endpoints, also at M=0 where its numerator starts at (1+η)t and its denominator at t². For the derivative numerator H, independent expansion gives H=eᵗ[−2MA+2A(M−1)t+(A+η(2M−1))t²+ηt³]+2M+2t, A=1+ηM. Its coefficients match the asserted Qₙ and strictly positive first differences for n≥2. At M>0 the first two coefficients are negative and those from n=3 positive; at M=0 the first negative one is n=2 and the positive tail starts at n=4. Dividing H by the first positive degree leaves a strictly increasing function on (0,∞), tending to opposite signs at the endpoints; its unique zero is simple. Thus the minimizer is nondegenerate and locally analytic in U. Coercivity of eᵗ/t and the trial value force t*→1; expansion of the stationary equation in M⁻¹ gives t*=1−[1/2+1/(ηe)]/M+O(M⁻²). Converting back gives the constant correction −k/(eL) in r* and [(e−1)L+eD/k]/U in T*, with the stated fixed-parameter remainders. Differentiating T first in U at zero and then in r at r₀ gives L/(2Dr₀²)>0, hence r*′(0)<0; continuity and r*→∞ give an interior minimum without proving it unique. The frozen checker was inspected, not executed: contrary to RESULT.md line 90 it does not check the stationary-coefficient identity. Separate `python3 /workspace/checks/frozen_math_checks.py 4` passed for the coefficients through n=8, the symbolic first-difference identity and both expansion coefficients; the all-degree formula and global arguments above are analytic.

## originality

PASS

Credit Mazzolo for the exact drifted MFPT, zero-drift uniqueness, the sign of the first derivative of the optimum at zero drift, and a numerical turnover. The distinct earlier-uncovered part supported here is all-inward-drift uniqueness, the sharp reaction-limited lower bound, the fixed-reactivity strong-inward expansions, and the resulting universal turnover. Later local results explicitly cover uniqueness and the rate expansion (not independently novel relative to those texts); their overlap is material but not prior coverage of this October 19 record.

## value

PASS

The result identifies what arbitrarily fast delivery and optimized resets cannot overcome: finite point reactivity imposes the nonzero sharp time eL/k. The first correction distinguishes finite travel/diffusion from that limit, and uniqueness removes ambiguity in the reset-rate law even though the optimal rate need not increase monotonically with drift. The contributions are meaningful for this reset search model without claiming outward-drift behavior or an optimum for ideal absorption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
