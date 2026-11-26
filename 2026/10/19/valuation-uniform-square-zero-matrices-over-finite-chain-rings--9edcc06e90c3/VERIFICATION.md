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

A primitive square-zero B over a length-k quotient has nonzero square-zero reduction, hence the image and kernel of the reduction are the same line. Choose v outside that line modulo the maximal ideal; (Bv,v) is a basis and exhibits B as a conjugate of the single Jordan block. Its stabilizer in GL_2 consists of equal unit diagonal entries and an arbitrary upper entry, giving (q−1)q^(2k−1). Reduction of GL_2 is surjective with q^(4k−4) lifts per invertible reduction, yielding P_k=(q²−1)q^(2k−2). For valuation c with 2c<n, multiplication by π^c identifies the matrix ideal with matrices over length n−c as sets; A²=0 is then exactly the condition on the primitive image over length n−2c, with q^(4c) lifts. The powers of q cancel the c-dependence. If 2c≥n all products vanish, so ideal-shell subtraction and the unique zero exhaust the rest. The high shells including zero contribute q^(4 floor(n/2)), and adding ceil(n/2) copies of the low count gives the stated total, including the field case q². For x=q²T, use Σ floor(n/2)x^n=x²/((1−x)^2(1+x)); the stated generating numerator 1−q²T² results. Direct entry-square enumeration independently verified Z/4, Z/8, Z/16, Z/9 and F_4[t]/(t²), with respective totals 28,112,640,153,496 and all valuation strata matching.

## originality

PASS

The arbitrary-ring-length valuation count in dimension two is distinct on the inspected evidence. An earlier indexed Smith-stratified result already supplies the whole length-two case and must be credited. Two later indexed image-length results have exact substantial overlap, including the constant low-valuation count and total, but the inspections supply no evidence of their prior coverage or a dependency link. The finding is not new on the previously covered length-two slice.

## value

PASS

Square-zero 2×2 matrices are a natural first nilpotency-index-bounded counting problem over nonreduced rings. The entry-valuation census separates constraints on primitive quotients from the automatic square-zero ideal range. The equal counts across genuinely different low strata, valid in mixed as well as equal characteristic and for every length, provide useful uniform local counting data beyond the already-known length-two slice or a total alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
