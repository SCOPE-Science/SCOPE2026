---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For every nonzero pivot of a nonsingular 2×2 input the rank-one cross residual has sole nonzero magnitude |det A|/|a_ij|, giving Z=s1/|a_ij|. Exact squared-entry sampling yields E Z²=N s1²/(s1²+s2²)≤4. For b>2 the Gaussian regression identity gives E[X_i/X_j]=(b−2ρ²)/(b−2)≤b/(b−2), and Cauchy–Schwarz bounds every sketch-pivot probability by that factor times a_ij²/||A||F², proving E Z_b²≤4b/(b−2). On D_e, the independent χ²_b ratio implies exactly E Z_1²=1/e, E Z_2²=−2 log(e)/(1−e²), and limit 1+b/(b−2) for b≥3. For H_h symmetric SPD, row-exchange invariance makes sketch and exact pivot distributions identical; off-diagonal probability h²/(1+h²) yields exact E Z^p=(1+h)^p(1+h^(2−p))/(1+h²), diverging as h→0 for every p>2 even though κ≤2. The strict tail envelope follows by maximizing increasing off-pivot probability over h<1/(T−1). Independently checked several rational h moment identities and b=2 integral expressions.

## originality

PASS

The primary Gaussian-sketch LU article establishes sufficient b≥3 pivot-probability domination, not necessity of b≥3 under the exact two-by-two mean-square normalization. The diagonal chi-square-ratio formulas at b=1,2 and the uniformly-conditioned higher-moment/tail obstruction are distinct further conclusions. Earlier squared-entry RPLU analyses give the baseline but not the sharp moment threshold and explicit counterexample laws.

## value

PASS

Sharp necessity of three sketch columns for uniform normalized mean-square one-step LU accuracy and a separate universal higher-moment/tail obstruction quantify concrete stability properties of a published randomized algorithm. The diagonal and uniformly conditioned counterexample regimes are distinct, operationally meaningful boundaries, not arbitrary tiny test cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
