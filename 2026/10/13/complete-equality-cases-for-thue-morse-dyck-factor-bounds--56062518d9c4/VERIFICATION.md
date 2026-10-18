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

The proof uses the cited published recurrence d(2m)=2d(m) and three odd-index recurrences for m>=3, the published two-sided inequalities and DFA q(2^a)=2. Independently counted distinct Dyck factors of a 32768-symbol Thue–Morse prefix for 1<=n<29, recovering exactly the base equality lists upper [1,2,3,6,12,24], global lower [4,8,16], odd lower [3,5]. Published bounds make the upper inequality strict at every sufficiently large odd n; doubling propagates upper equality exactly. The global lower has only even equality and doubling reduces to powers of two. Odd lower: 4m+3 requires simultaneously m power of two and q(m)=1, contradicting q(2^a)=2; 8m+1 has a stronger lower bound; 8m+5 equality would make consecutive m,m+1 powers of two. This is a complete infinite induction, not an extrapolation from the finite prefix.

## originality

PASS

The exact 2023/2025 Mol–Rampersad–Shallit paper was read in the relevant full mathematical sections, including Lemma 5.1 and Theorems 5.2–5.3. It establishes sharp inequalities and exhibits infinite extremal families, but its written statements do not assert their uniqueness or list the two isolated upper and two odd lower equality cases as an iff theorem. OEIS A345199 supplies values/recurrences but not a demonstrated if-and-only-if classification. The new argument logically combines source recurrence strictness, finite base, and automatic q behavior; a priority risk remains if the equivalence is known in subsequent commentary.

## value

PASS

For a natural automatic word and a distinguished Dyck-factor complexity function, classifying all equality cases of sharp published extremal bounds is a motivated complete extremizer problem. Showing no other odd or dyadic equality families exist strengthens mere examples and reveals recurrence rigidity, without claiming new bounds or closed forms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
