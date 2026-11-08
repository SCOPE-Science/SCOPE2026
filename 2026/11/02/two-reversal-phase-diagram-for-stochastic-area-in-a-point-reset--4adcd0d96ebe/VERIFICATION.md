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

Generator moment equations for reset point (a,b) yield (r+1)EX−uEY=ra, −uEX+(r+1)EY=rb, and (r+2)E(X²−Y²)=2(Tx−Ty)+r(a²−b²). The continuous area production is u E(X²−Y²); a reset jump contributes bX−aY, whose Poisson compensator gives r[bEX−aEY]. Summing and simplifying produces J=u/(r+2)[2ΔT+r(1−u²)ΔR/((r+1)²−u²)]. Independent symbolic derivation confirms all coefficients and factorization. When ΔT≠0 set q=−(1−u²)ΔR/(2ΔT); J has sign ΔT times (1−q h(r)), h=r/[(r+1)²−u²], whose unique maximum occurs at s=√(1−u²) and equals 1/[2(1+s)]. This proves zero/tangency/two-simple-zero regimes and root product s²; ΔT=0 gives constant sign ΔR or zero identically. For u=3/5,Tx=2,Ty=1,(a,b)=(0,5/√2), exact J=6(5r−8)(5r−2)/[5(r+2)(5r+2)(5r+8)]. Regeneration and integrable jump rewards justify a.s. long-time area rate. The submitted CHECK.py was inspected for symbolic and quadrature checks; independent algebra checks the central identity. Chord area is an explicitly defined geometric jump observable, not actual transported work.

## originality

PASS

Best-of-knowledge distinct claim after comparison with directly relevant primary sources and published mathematical findings. Prior special cases and baseline formulas are explicitly credited. Complete historical originality is not certified.

## value

PASS

The Brownian gyrator is a fundamental nonequilibrium two-temperature circulation model, and stochastic resetting is a physically motivated intervention. Whether its orientation reverses once or twice is a natural exact dynamical question. The exact phase boundary and reciprocal-root law for a correctly jump-inclusive area observable are useful qualitative predictions within a sharply specified model, not a restatement of unreset circulation or entropy production.

The dated certificate retains the supplied scientific assessment, sources and limitations.
