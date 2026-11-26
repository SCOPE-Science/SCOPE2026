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

The section has a relative interior point x_i=k a_i/A. A feasible point with two free coordinates can move in both directions along their difference, so every vertex has at most one free coordinate; fixing all but at most one coordinate conversely determines a vertex. All vertices are integral, and any n-1 distinct signed coordinate classes are a basis of the quotient lattice N. This gives smoothness for a one-free-coordinate chart. At a box corner, reverse the signs on the upper-cap coordinates in the saturated zero-sum lattice M. The lattice tangent cone becomes the balanced nonnegative exponent monoid: pair units generate it and changing the matching of units by transpositions gives exactly the 2-by-2 minors as relations. This computes the entire normal-fan affine chart, not its completion or just an étale model. When each sign group has at least two elements, the unique dependence equating the sums of the two groups makes all n rays extremal; each proper face omits a ray from each group and the remaining rays extend to a basis of N. Hence the only singular orbits are the full-cone fixed points of these charts. A group of size one instead gives a free monoid. The degree-d Hilbert function in the standard grading counts two weak compositions of d, giving Segre degree and local multiplicity binom(n-2,s-1). The signed primitive rays span N, so the toric divisor sequence yields Cl(U)=Z. The same group is local at the apex: on the blowup, the total space of O(-1,-1) over the Segre product, a line bundle pulled back from the product that becomes principal off the exceptional zero section over a neighborhood of the apex can differ from triviality there only by a multiple of that section. Restricting to the section gives a multiple of O(1,1) in the original Picard group, i.e. zero in the cone's class group. Thus localization at the apex kills nothing. The rational canonical ray heights force m_i=-1 on S and +1 on its complement; they satisfy the zero-sum relation iff s=t, when the character is integral. The normal semigroup ring is Cohen–Macaulay, so Cartier canonical in this case gives Gorenstein. These arguments apply in arbitrary characteristic as stated. The coefficient product counts the allowed subsets by their tagged cardinality (transpose chart types coincide abstractly). Independent enumeration of vertices and their primal edge adjacencies in four examples gave the stated 24 fixed points with basket {2:6,3:1} for the displayed caps (checks/frozen_checks.py argument 5, checks/5.txt); binomial multiplicities are 4 and 6. The finite check is corroborative; the lattice proof establishes exhaustion and the other invariants.

## originality

PASS

Credit the unit-cap result for the same rank-one local charts in that subfamily, and standard toric/GIT and Segre theory for the underlying local mechanisms and invariants. The supported distinct result is the entire arbitrary-cap classification at one fixed level, enumerating every singular orbit and its type by a cap-subset coefficient, including coexistence of balanced and nonbalanced points. The inspected strongest unit-cap, positroid and general-framework comparisons do not supply the arbitrary-cap basket or a stronger theorem that classifies it by specialization alone.

## value

PASS

The varied polarizations of a standard diagonal quotient form a natural family, and the exact classification tells a researcher which walls produce nonsmooth points, how many there are, and which local canonical behavior they have, without building the whole fan. The mixed fivefold example demonstrates behavior impossible in a single fixed-level unit-cap model; its point counts are illustrative rather than the only result. The constituent determinantal calculations are standard, but their exhaustive cap-dependent combination is useful structural data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
