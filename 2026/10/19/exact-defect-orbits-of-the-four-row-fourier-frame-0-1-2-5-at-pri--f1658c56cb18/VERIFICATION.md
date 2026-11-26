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

For four distinct nodes, the remainder of X⁵ modulo their monic quartic has X³ coefficient e₁²−e₂=h₂. Row elimination thus gives the Vandermonde times h₂; the first three rows force rank at least three. The pair-sum polynomial has value 10 at 1, and divisibility by the prime-power cyclotomic polynomial forces p=2 or 5. In the binary case divide away common parity until both parities occur. The odd part must vanish; a 1+3 split is impossible by the odd term count, and the 2+2 split makes the odd part the product of two pair sums, forcing an antipodal pair. Writing the roots as u,−u,v,w reduces the equation to u²+v²+vw+w²=0; its modulus constraint gives v/w=−1 or ±i and hence the two stated shapes. The first is a subgroup coset; the second has one antipodal pair and cannot be fixed by the half-turn, so the stabilizers have orders four and one. For p=5 each residue class of pair sums must have a count divisible by 5. The 3+1 and 2+2 patterns give (6,3,1) and (3,4,3). In 2+1+1, the repeated residue contributes three pairs, the mixed pairs with the two singletons add two each at distinct different residues, and the three singleton pair sums are distinct; the maximum is four. For four distinct residues, deleting the missing residue from all five subtracts one pair per sum from three, leaving two each. Thus all four residues coincide, and iterating yields the order-five coset. Its converse follows from the reciprocal product (1−αt)/(1−t⁵). Independent exact replay checked all 625 residue tuples and all 915,337 four-sets at N=7,8,16,25,27,32,49,64 with zero mismatches; singular counts were 0,10,20,25,0,40,0,80.

## originality

PASS

Full-spark existence for this row set at prime-power orders follows from Alexeev–Cahill–Mixon. The preceding same-row semiprime record also explicitly establishes the order-five pattern at N=15 and the h₂ identity that proves sufficiency at any multiple of five. What survives is necessity for all prime-power orders, especially the binary two-orbit classification and the proof that no larger fifth-power configurations arise. The inspected results do not give these or their counts.

## value

PASS

The first quadratic Schur case after the consecutive and linear cases is a motivated four-row sample-reconstruction problem. The enumeration supplies exactly which samples fail and how many, explains the distinct fourth-, eighth- and fifth-root mechanisms, and replaces the binary full-spark answer with an all-size classification. This is useful beyond repeating the known existence dichotomy or the earlier fifth-root witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
