---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independent product argument: put A=p^a and m=q-1, so 1<=m<A. The numerator factors of binom(q(A-1),A-1) are mA+j for j=1-m through A-1-m; the denominator factors are 1 through A-1. Their residues mod A cover 0 through A-1 except A-m, each once. A nonzero residue d in this range has valuation <a, so the matching factor has its same valuation and the same unit modulo p after dividing out the p-power. Cancel all such matched factors. The unmatched numerator is mA, the unmatched denominator A-m. Since v_p(A-m)=v_p(m)<a, their valuation difference is a, and the respective normalized units reduce to opposite elements modulo p. The unit ratio is -1, including p=2 and the endpoint cases. The frozen Legendre and Wilson calculation correctly reaches the same result. The gcd is exactly A: the congruence gives divisibility by A, and the order-A finite difference of the degree-(A-1) polynomial f(q)=binom(q(A-1),A-1), with f(0)=0 and f(1)=1, makes the gcd over q=2,...,A divide A. The wording about sharpness is read as the sharp divisibility threshold, not a universal claim about the next digit.

## originality

PASS

Credit the known exact progression gcd and the classical general unit formula. The distinct content is the uniform evaluation of the leading normalized unit at -1 for the entire interval, not the generic availability of an algorithm for an individual binomial coefficient. The sources inspected do not give this family simplification or a theorem directly asserting it.

## value

PASS

The prime-power endpoint is a natural high-divisibility family of an established progression-gcd problem. A term-by-term unit is needed to determine the first nonzero digit rather than the minimum valuation, and the unexpected constancy gives simultaneous residue information for arbitrary linear combinations of the progression. Its proof is a uniform arithmetic cancellation, not a table or a finite search for an isolated value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
