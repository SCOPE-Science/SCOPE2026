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

A ball move is a zero-sum integer difference of total negative mass at most r, and is lost exactly if some negative component exceeds the center multiplicity at that coordinate. Fixing one or two negative components leaves a positive-sum vector; choosing its strictly negative positions and composing their absolute mass, then weakly composing the positive mass among the rest, gives the displayed K, δ and ω. The strict differences between the δ's are witnessed by the move transferring exactly a+1 objects from the designated coordinate to another; δ_(r−1)>0 by transferring r. The interior volume generating function is (1−t)^(q−1) times the sum of binom(m+q−1,q−1)^2 t^m, by taking the constant term of the q-fold product of (1−t)/((1−tw)(1−w^−1)) and then summing through r; Euler's binomial-series transformation gives the stated H. For a fixed coordinate of size a the marginal is (q−1)/(n+q−1) times the product of (1−a/(n+j)) over j=1,…,q−2, yielding the stated negative n⁻² correction. The two-coordinate probability starts at (q−1)(q−2)/n²; three small coordinates cost O(n⁻³), or are impossible eventually for q≤3. For every fixed k, adding δ_a^k for each small coordinate and correcting each pair by its overlap-aware joint power gives D_n^k exactly through two small coordinates, with bounded error otherwise. This gives L_k and M_k, including q=2 with no pair term. The variance subtracts L_1²/n²; the rare-defect masses come from one-coordinate events, with other events of order n⁻². Independently, for q=3,r=2 the moves at distances 0,1,2 number 1,6,12 (the distance-two patterns are permutations of (2,−2,0),(2,−1,−1),(−2,1,1)). They give δ=(7,3) and ω_00=1 only. Grouping centers by which coordinates are 0 or 1 produces the six stated bins for n≥6; summing deficits and squared deficits gives (60n+36)/((n+1)(n+2)) and (348n+1332)/((n+1)(n+2)). Subtracting the square gives the −3312 correction. The uploaded checker was inspected, not executed; the stored 8964 center checks and 16 spectra are finite consistency evidence.

## originality

PASS

The prior individual-center and mean theorems are credited. The explicit face-overlap n⁻² law for every fixed deficit moment evaluates a statistic not supplied by those prior statements. There is substantial exact overlap with a later Resultary record (rare deficits, leading moments, the entire six-bin table and ternary variance); that record gives a stronger finite-n formula for the first two volume moments, but does not predate the October 27 finding. No preexisting evaluation of the full moment coefficients was established.

## value

PASS

Ball-size variation is a natural missing statistic for a nonhomogeneous coding metric whose interior, minimum and mean are already used. The universal two-face term distinguishes same-center interactions that the mean cannot see; radius two in the ternary simplex is the first case where two simultaneous coordinate violations can overlap, explaining the six classes and giving an interpretable exact example. No improved code size is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
