---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Read primary source 2026 measles ODE (2.1), SDE drift (2.2), and printed Milstein Section6.1 directly. Printed I step contains an extra -hβSI/N absent from source while E step has +hβSI/N, so cancellation yields H_{n+1}=H_n-h[μE+(μ+γ+φ1)I]. On all nonnegative states N>0, if h≤1/max{β+ψv+μ, μ+φ, μ+γ+φ1+β, μ+κ+ωv, μ+ω, μ}, each Euler coordinate remains nonnegative and S_{n+1}≥hΛ>0; hence geometric H bound holds for every β>0 and every nonnegative initial state. Exact rational arithmetic of frozen verifier confirms at Λ=5,β=20, all other positive rates=1, true endemic state (15/11,15/11,5/11,5/11,5/22,15/22), incidence 30/11, N=50/11; true DFE infected eigenvalues 1,-6 versus printed trace -17 determinant 18, h=1/40 gives H≤(39/40)^nH0. This is a property of the printed zero-noise recurrence, not stochastic almost-sure extinction or actual source implementation.

## originality

PASS

A directly matching earlier published Resultary record already exposed the spurious -βSI/N term and first-order inconsistency, so those premises are NOT original here. Distinct contribution considered is all-positive-parameter invariant-cone geometric eradication of H and explicit exact true-endemic counterexample with threshold reversal, not shown in the visible earlier index synopsis. Full previous package was inaccessible, creating a real equivalence risk; a matching theorem there would defeat the novelty assessment.

## value

PASS

Global forced infection eradication regardless of β in a positivity-preserving published numerical update reverses epidemic-threshold behavior. The universal Lyapunov contraction and exact supercritical endemic witness exhibit substantive qualitative numerical-method failure beyond merely noting a stray term; the known local consistency objection is credited and not presented as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
