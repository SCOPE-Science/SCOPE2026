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

Reassessed /workspace/repairs/5/RESULT.md. The frozen counts are correct, but the frozen Finding's last sentence overstates what the preceding summaries determine: for n=3 there are two 3-cycles and three fixed points, and the nonzero leaf counts 6 and 3 both occur on the cycle (6,15,24). Moving the size-6 leaf set to the other 3-cycle (3,12,21), without changing any cycle, yields the same cycle and leaf histograms but a nonisomorphic graph (two decorated 3-cycles instead of one). The repaired Finding gives the pointwise criterion, using the original square-root rule and the unique depth-one antecedent of each cycle vertex. For the mathematical reassessment, residue routing is 1→2→0 and Hensel's lemma bijects classes 0 and 2 separately onto class 0. For valuation t≥1, the base iterate displaces by x², and when G=F^(3^k) displaces by u of valuation s≥2, three iterates displace by u(1+G′+G′²)+O(u²), where the factor in parentheses has valuation 1 and 2s>s+1. Thus periods are 3^max(n−2t,0), the valuation-t balls have full compatible cycles and hence are odometers, and only 0 is periodic at infinite precision. Fixed points, cycle counts and zeta follow by counting each shell and dividing by its orbit length. At each periodic x the antecedent in class 2 is (w−1)/2 for the unique root of 1+4x congruent to 2. The next root problem has discriminant A≡0 mod 3. A=0 has 3^floor(n/2) roots; exact valuation 2r<n with unit part 1 modulo 3 has two simple unit roots each with 3^r free lifts; all other nonzero A have none. This puts the correct rooted star at each vertex and yields the histogram by counting A. At n=1 the rule gives a fixed point with a two-edge chain. The finite replay checks the pointwise rule, not just the aggregate counts, and is corroboration rather than the all-level proof.

## originality

PASS

For the repaired claim, credit known odd-prime lifting, odometer criteria, and modular square-root counts. The supported distinct content is the explicit all-level ternary graph tying the cycles to the nonuniform critical preimage trees, not a new general theory of cycles or square roots. The closest inspected exact example for the same polynomial is at prime 2; the closest graph with pointwise branch incidence uses x²−2 at prime 5. Bounded comparisons do not certify universal priority.

## value

PASS

The parabolic quadratic at the smallest odd prime is a concrete test case that exhibits both odometer growth on the invariant class and singular unbounded branching in the transient classes. The repaired result identifies where those trees sit on every finite cycle, and not merely how many there are, which is what a researcher comparing graph isomorphism types or finite quotient dynamics needs. The graph and zeta formulas are all-level, not an arbitrary short census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
