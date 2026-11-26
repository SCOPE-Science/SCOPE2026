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

The corrected RESULT.md uses only the necessity direction of the classical three-minimal-generator theorem and proves minimality before applying it. The frozen proof quoted a shared-factor equivalence without explicitly imposing minimality or checking it in the odd branch. The unrestricted reading is false: ⟨12,21,2⟩=⟨2,21⟩ is symmetric although 2∉⟨4,7⟩ for d=3. At odd n=2m+1≥5 the middle generator w is odd; the smallest cannot be redundant; and an expression for the largest 32v using 32u and w forces the coefficient of w to be a multiple of 32. It would give v=Au+Bw; w>v forces B=0, impossible since u=m^5>1 and gcd(u,v)=1. The unique gcd pair is therefore the outer pair with gcd 32, and symmetry would imply (2m+1)^5=A m^5+B(m+1)^5. Modulo m and m², B=1+jm with 0≤jm≤30 and j≡5 mod m, excluding m≥7. In the even case there is no common-divisor pair and only the largest could be redundant; the required A≡−1 mod n exceeds ((n+1)/(n−1))^5 for n≥8. Independent replay `python3 /workspace/reproductions/fifth_powers.py` confirms all remaining odd and even candidate remainders and computes F=7501, g=3751 for ⟨32,243⟩. The residue bounds prove the infinite tails; the replay is not an infinite search. The equality/strictness statement then follows by reflecting membership about F/2. The replacement states the same valid Finding but supplies the missing applicability argument; the frozen source and its bounded verifier remain unchanged.

## originality

PASS

The repaired proof establishes the all-index fifth-power classification, including the even indices. Fel's closest prior work gives classical structural criteria, exact results at other exponents, and a bounded higher-power scan. The classification does not follow from those without the fifth-power coefficient exclusions. No inspected result gives the full fifth-power theorem; inaccessible sources and ranked-search limits are recorded separately.

## value

PASS

Exponent five is the first exponent beyond the explicit square/cube/quartic classifications, and the disappearance of the quartic exceptions n=5 and n=7 is not a monotonicity consequence. The symmetry question is a natural sharp boundary for the genus inequality. The proof reduces an infinite fifth-power family to a small explicit set of residues with separate structural reasons for the two parities, replacing prior bounded odd-index evidence with an all-index theorem. It does not claim exact Frobenius or genus values beyond the single symmetric case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
