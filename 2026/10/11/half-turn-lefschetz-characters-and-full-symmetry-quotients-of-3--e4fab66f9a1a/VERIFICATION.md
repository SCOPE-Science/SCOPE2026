---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

A g-invariant matching M with k edges in s permutation edge orbits acts on oriented (k−1)-simplex with sign (-1)^{k-s}; multiplying chain sign (-1)^{k-1} and adding the empty simplex gives reduced Lefschetz -sum_{gM=M}(-1)^s. Folding the P3×Pn half-turn gives odd center-column seam masks (0,1,4) with vector u_o, and even between-column seam masks (0,2,5,7) with minus signs for paired upper/lower seam orbit; these exhaust edge-orbit conflicts. The explicit 8×8 signed transfer T_{A,B}=(-1)^|B|(1−1_{upper-free}−1_{lower-free}) for disjoint masks yields s_m=e0^T T^m u. Independently recomputed both first 9 sequences, verified the order-six denominator recurrence for 14 indices and used Cayley–Hamilton order≤8 to extend the vanishing sequence to all m, establishing the exact rational generating functions. The identity and two reflection traces average to quotient reduced Euler; independent exact transfer gives F17=320,F8=94,b8(o)=-22,a17=0, hence (-320+94+22)/4=-51. Independently counted actual edge-orbit matchings for n=2..6, including orientation signs for R,C,RC, which agreed. Finite orbit checks corroborate only, not prove recurrence.

## originality

PASS

The same-family 2026 Chauhan–Sharma–Shukla primary preprint establishes nonequivariant homology/connectivity and conjectures a wedge; it does not calculate the rotation Lefschetz character. Published related mathematical finding on the two coordinate-reflection characters is direct prior input, but it cannot determine the product involution: a nonzero virtual K-four character can vanish on identity,R,C yet change J. The new odd/even folded signed edge-orbit constraints yield the additional character and thus full quotient Euler. Unindexed signed matching transfer series could still encode it; precise residual risk noted.

## value

PASS

The half-turn is a natural missing group element in the full Klein-four automorphism action of a difficult infinite family of matching complexes. Center seam edge-orbit constraints distinguish it from either single reflection; exact all-width rational characters and quotient Euler values, including -51 at width17, are intrinsic equivariant-topology invariants. They are independent of nonequivariant homology tables and do not need a full homotopy classification to matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
