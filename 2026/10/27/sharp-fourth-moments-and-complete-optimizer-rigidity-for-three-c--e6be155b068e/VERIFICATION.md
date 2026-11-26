---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For ordinary SU(2) characters and Haar probability, Clebsch–Gordan and orthogonality give the displayed |f²|² sum; its repeated even term disappears at n=0 while its odd |b(a+c)|² term persists. Positivity reduces to coefficient moduli. For c>0, writing u=|b/c|², the u-derivative has a strictly positive fixed factor times u_n(t)−u; u_n(t)>0 since 4t²−t+3 is positive and all other numerator terms are nonnegative. Independent symbolic expansion checked reduction to R_n and the derivative identity; H_n(0)<0<H_n(1) and one sign change for each n give the unique interior maximizer, strictly above R_n(0) and its limit at infinity. At c=0 and a≠0, continuity and t→∞ bound the quotient by the latter limit; the pure-b quotient n+2 is strictly below the interior u-optimum at any fixed t. Equality in |a²+b²+c²| and |b(a+c)| then forces exactly a common complex scalar with a free middle sign. The positive root tends to 1 and the expansion gives t_n=1−1/(2n)+O(n⁻²) and u_n=4/5+8/(25n)+O(n⁻²). For K_n the leading rational term has zero derivative at t=1, hence the constant correction is the same as from evaluating at 1: (128n²+314n+197)/(28n+38)=32n/7+491/98+O(n⁻¹). The independent bounded reproduction at branches/f69c1132-ca0c-4731-a89d-4680338628e2/independent_reproduction.py also compares exact semicircle-moment and character calculations on 24 complex samples and checks the sample root values. It does not by itself prove the all-weight statement. The supplied script was inspected, not executed.

## originality

PASS

The known high-weight result already covers the leading slope and limiting optimizer, and the general product rule is classical. The inspected sources do not cover the exact all-weight sharp value, positive-cubic-root characterization, finite-weight phase rigidity, or next asymptotic term of this triple. This is a bounded assessment of the distinct finite-weight theorem, not a claim of exhaustive priority.

## value

PASS

Consecutive central triples give a natural first packet beyond all two-mode problems. The exact, uniform-in-weight interior optimizer and its phase rigidity decide how parity mixing occurs at finite weight, not just its asymptotic pattern. The finite-weight formula and first correction are useful even when the leading slope is already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
