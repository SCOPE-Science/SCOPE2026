---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Use the original synchronous nearest-to-own-opinion weighted-median convention: when leaves a<b, hub selects M=clip(x,[a,b]), not nearest endpoint. With d=(b−a)/2>0, m=(a+b)/2, z=(x−m)/d, the gap satisfies d_next=(1−s)d. If |z|<=1 the interior projection leaves x fixed and interior stays invariant. Outside, z_next=((1−2s)z+s sgn z)/(1−s); for s>1/2 put lambda=(2s−1)/(1−s), B=s/(1−s), so successive exterior side changes give R_next=lambda R−B. When s<=2/3, lambda<=1 and switching cannot continue indefinitely; when s>2/3, R0>B/(lambda−1)=s/(3s−2) generates strict unbounded normalized alternating exterior region. The aggregate dynamics contracts enough for consensus at every s in (0,1); on alternating orbits x_next+m_next=x+m+s sigma d, so summing gives c=(x0+m0)/2+s sigma0 d0/[2(2−s)]. New exact Fraction calculation confirms s=3/4 witness z path 4,−5,7,−11,19,−35, c=73/100. The infinite result follows by induction, not the finite prefix.

## originality

PASS

Best-of-knowledge PASS: the original Mohr–Hjorth–Porter model fixes median tie/interval convention and examines long-/short-time opinion distributions; Cheng–Mei (2026) proves convergent opinions and structural consensus but does not assert finite stabilization of the chosen selector. Indeed persistent selector switching is compatible with their conclusion. Asynchronous and continuous-time frameworks are not statement-equivalent. Prior switching-system analogues are a residual risk.

## value

PASS

The smallest symmetric network with a nontrivial median interval has an exact robust transition between convergent opinions with eventually stable selector and convergent opinions with perpetual strict branch alternation. This sharp dynamical boundary separates discrete influence choice from continuous consensus and is not merely a single simulated cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
