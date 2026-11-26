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

Writing a=δi, b=δj with (i,j)=1 gives f=gcd(δ,i+j) since (ij,i+j)=1. The Jordan divisor identity and δ=dk therefore give exactly the ordered primitive-pair sum (1); the support d²k≤2x follows without approximation. For each e in Möbius inversion on (i,j), the congruence after division by e has modulus d/gcd(d,e); counting one residue of the second variable for each first variable costs O(y/e), uniformly. Extending the density sum costs O(y) since gcd(d,e)≤d. Its Euler factors give V_d(y)=y²[dζ(2)]⁻¹∏_{p|d}p/(p+1)+O(y log(2y)). For a separate truncation check, restrict to d≤D=floor(√x/(log x)²) and all k≤min(floor(2x/d²),floor(x/d)), which ensures y≥1 and omits only zero counts within this d range. The uniform count errors sum to O(xD²(log x)²), by J₂(d)≤d² and the harmonic sum over k. Extending the main k-sum to infinity costs O(xD²), since the per-d k tail is O(d²/x) and the per-d main term is O(x²/d). J₂(d)∏p/(p+1)=dφ(d), and the full sum over k cancels the primitive density factor ζ(2)⁻¹. Harmonic summation of φ(d)/d² gives ζ(2)⁻¹log D+O(1). For d>D, the elementary count V_d(y)≤2y²/d and d≤√(2x) bound the whole tail by O(x² log log x). Hence the factor 1/2 is from log D=½log x−2log log x+O(1), not from unordered pairs, and the constant is 1/(2ζ(2)). All counts work with real upper bounds and integer variables. The frozen rectangle estimates in RESULT.md lines 23–100 are also uniform. Reviewed VERIFICATION.md, verify.py and verify_output.txt as finite identity evidence only; no numerical computation is required for the asymptotic.

## originality

PASS

The closest primary work poses the power-moment asymptotic at t≥2 and proves a theorem only below that boundary. Neither earlier same-map level-set results nor the distinct indexed density theorem gives the second moment. The supported contribution is the ordered t=2 asymptotic with its constant and remainder, not all of the open higher-exponent range.

## value

PASS

The t=2 case is the first excluded exponent of a published problem. Determining the order, constant and lower-order error establishes a genuine transition from finite normalized subcritical moments to logarithmic growth; neither a finite check nor formal substitution at the boundary supplies it. This resolves one precisely posed case without claiming t>2 or an optimal remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
