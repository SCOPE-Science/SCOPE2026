---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Define t(x)=log log(x+e^e), h1(x)=1/(1+exp(−2t sin t)), h2(x)=1−h1(x). Both are strictly between 0 and 1, extend real analytically around [0,∞), and sum identically to one. Cumulative hazards Ri(x)=∫0^x hi and S_i=exp(−Ri) therefore yield independent min survival S1 S2=e^−x exactly and strictly positive analytic densities fi=hi exp−Ri. Along alternating log-log intervals s∈[7π/6+2πk,11π/6+2πk] and [π/6+2πk,5π/6+2πk], the designated hazard is at most e^−s. Under x=exp(exp s)−e^e the start/end coordinate ratio tends to zero, so each Ri(b_k)/b_k≤a_k/b_k+e^−A_k→0 on a subsequence. On opposite-sign intervals each hi≥1/2 over lengths →∞, hence Ri→∞ and each law is proper. For every λ>0, Ee^(λXi)≥e^(λb_k−Ri(b_k))→∞, proving heavy-tailed. Independently checked exact complement/hazard algebra and scale separation analytically; no finite tail simulation was misused as proof.

## originality

PASS

Best-of-knowledge PASS ONLY for the positive real-analytic hazard/density construction, not for the 2023 discovery that two heavy tails can have light-tailed minimum or the 2025 universality theorem for arbitrary right-unbounded targets. Leipus–Šiaulys–Konstantinides give factorial/piecewise examples, and accessible summaries of Foss–Tarasenko–Krivtsov and Foss–Scheutzow–Tarasenko emphasize alternating cumulative-hazard construction and segmented tails, but do not explicitly document this analytic positive pair. Both later full papers inaccessible through arXiv/OA in this run; institutional retrieval reported VPN disconnected. A hidden smooth/analytic example in these plausible prior papers is the largest retained novelty risk, not grounds for automatic O failure absent decisive coverage.

## value

PASS

Gives an explicit pair of proper, atom-free, everywhere-positive real-analytic-density/heavy-tailed factors with exactly exponential minimum. Earlier examples achieve a light minimum by piecewise alternation/flat hazards; this sharply demonstrates that the required tail segmentation can occur despite strong local regularity and without literal hazard zeros or nonsmooth corners. An exact self-contained regularity witness in a natural minimum-factorization paradox is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
