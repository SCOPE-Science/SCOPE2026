---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For any finite field F_q of characteristic p>5 and all a,b, translation x→x−a/5 sends the two fixed top coefficients to B=b−2a²/5 while bijectively reparametrizing free c,d. Inclusion–exclusion over fibers of quintic degree <=5 reduces the mean image count to q−(q choose 2)/q + ((q choose 3)−K4(B)+K5(B))/q². Four equal evaluations correspond exactly to quadratic Q+s²=-2B; five additionally impose s=0 and Q=-2B. Distinct input constraints are removed by explicit partition-lattice Mobius weights; for p>5 all indicated quadratic forms are nonsingular, so standard Gauss representation formulas give exact B=0/nonzero squareclasses. The squareclass difference is (qχ(5)−χ(-15))/(3q²) !=0. Independent direct enumeration of ALL q² free coefficient pairs for EACH B over F7 and F11 checked each exact rational formula; e.g. F7 q²-scaled totals B=0:229, nonzero squares:225, nonsquares:227. Analytic proof, not finite checks, establishes all extension fields and p>5.

## originality

PASS

Best-of-knowledge PASS: Cesaratto–Matera–Pérez–Privitelli arXiv:1306.1744 gives generic inclusion–exclusion, and Matera–Pérez–Privitelli 1310.3293 primary PDF gives average first-moment asymptotic with O(q^1/2) and geometric interpolation methods; these do not evaluate the exact fixed d=5,s=2 character-split constant. Their explicit main estimate assumptions s<=d-4 exclude (5,2), while generic identities require the nontrivial four-/five-tuple quadratic-form evaluation performed here. Earlier specialized finite-field counting may contain equivalent exact formulas; no definitive full-text exclusion of all historical sources is claimed.

## value

PASS

Natural boundary family of monic quintics with two fixed high coefficients and uniformly random lower coefficients; exact image size detects square/nonsquare invariant B and proves a nonzero arithmetic gap invisible to general big-O averages. This is an exact useful finite-field statistic, not a mere parameter renaming of asymptotic estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
