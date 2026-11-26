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

An independent direct classification avoids transfer determinants. On these cubic graphs the single-spin change is 2J(3-2a) for a aligned neighbors, so the aligned edges must form a matching. If a rung is parallel, all four rail edges incident to its endpoints must be antialigned, forcing adjacent rungs to be parallel too even at the swapped seam. Thus all rungs are parallel, alternating in sign around the ring, with two labeled assignments for even n and none for odd n, at K=n. Otherwise all rungs are antiparallel. Each rail transition then aligns both legs or neither, including at the seam; the aligned transitions form a nonconsecutive cyclic set of size j contributing K=2j. Their sign product requires (-1)^(n-j)=+1 in the prism and -1 in the twisted ladder, and each admissible set has exactly two global sign assignments. The number of nonconsecutive cyclic j-sets is n/(n-j) times binomial(n-j,j), so parity projection gives both exact polynomials for all n>=3. For even n the sole common value K=n has raw weights 2 and 6 (the two maximum-size alternating cyclic sets yield the extra four); for odd n the supports are disjoint. This implies the stated TV bound. At z=1, the C_n power sum gives Lucas numbers and the conjugate unit phases give the stated cosine. Near z=1 the common dominant analytic root is lambda=(1+sqrt(1+4z^2))/2, with exponentially subdominant contributions. Its logarithmic derivatives z*d/dz give 1-1/sqrt(5) and 4/5^(3/2), and log(lambda(1))/2 gives the claimed entropy. Exact independent sector polynomial and n=3 through 8 enumerations also agree; the supplied verifier was inspected but not executed. The conclusions are about labeled blocked configurations and their energy law, not flip basins.

## originality

PASS

Covered parts include the Möbius ground-state sector, part of its low-energy blocked spectrum, the zero-field unweighted circular-ladder count and entropy, and the gauge-equivalent even periodic baseline. The supported distinct contribution is the full energy-resolved Möbius polynomial and its exact comparison to the periodic closure including parity-separated supports and near-maximal TV. No inspected result supplies or entails the complete weighted comparison; the older inaccessible strip paper remains a named risk.

## value

PASS

Changing a single seam condition provably places essentially all energy probability in opposite parity sectors even though both models have the same exponential state count and first two limiting energy cumulants. The complete polynomial pinpoints the exceptional overlap and shows why unweighted or thermodynamic comparisons miss it. This is a statement about blocked-state distributions, not a claim about dynamical basin selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
