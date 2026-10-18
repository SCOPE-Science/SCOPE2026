---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

For each coordinate, four real numbers summing to zero obey ∑_(i<j)(a_i−a_j)^4=4∑a_i^4+3(∑a_i²)²; the assigned verify.py expands this identity symbolically. Summation over coordinates of the admissible centered ℓ4-unit vectors gives ∑_(i<j)||x_i−x_j||₄⁴=16+3T with T=4+2∑_(i<j)∑_k x_i(k)²x_j(k)²≤16 by Cauchy and each unit fourth norm. Six-term Cauchy gives (∑_(i<j)||x_i−x_j||₄²)²≤6×64. The explicit four tetrahedral vectors supported on three coordinates, of signed coordinates ±3^(−1/4) with even sign parity, sum to zero, each have unit fourth norm and all six distances have fourth power 32/3, so equality gives 8√6. Summability of all sums for arbitrary I follows from Hölder and finite four-vector support of the argument; three coordinates suffice for sharpness. The exact published planar ℓ4² value 8(1+√2) is strictly smaller because 6>(1+√2)².

## originality

PASS

The introducing 2021 article defines J_in, proves universal bounds, and computes selected low-dimensional examples without the real ℓ4 three-coordinate value. The published SCOPE planar theorem gives J_in(ℓ4²)=8(1+√2) but explicitly restricts structural collapse to dimension two. Its implications cannot determine the strictly larger value in dimension at least three. The new exact tetrahedral all-dimensional upper bound and witness are not recovered by the planar reduction; no equivalent source was located in the inspected primary material. Resultary index coverage was unavailable and remains an originality risk.

## value

PASS

The inscribed-quadrilateral constant is a standard defined geometric invariant. Computing its sharp value on real ℓ4 in every dimension≥3 and proving a discontinuous dimension-two/three change provides a complete natural benchmark and warns against unjustified planar reduction; the exact value can be directly reused in Banach-space extremal geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
