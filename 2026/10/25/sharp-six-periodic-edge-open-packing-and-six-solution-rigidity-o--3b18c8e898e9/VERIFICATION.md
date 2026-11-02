---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For M_(2n) on vertices Z/(2n), n≥3, with cycle edges and antipodal rungs, each edge-open packing is an induced disjoint union of stars on the endpoints of its edges. Each selected edge contributes a leaf with two exterior incident edges in this cubic graph; these counted edges are distinct, so 3|P|≤3n and |P|≤n. Equality forces induced full K_(1,3) stars with no remaining improper edges and hence graph bipartiteness. The cycle-and-antipode graph is bipartite iff n odd, and equality requires n divisible by 3 via |B|=3|A|, so n≡3 mod6. The six explicit residue-class constructions have n edges in the equality residue, n−1 otherwise: I independently reconstructed their edge sets and tested all n=3..70 (68 values) by induced-edge equality, disjoint-star structure and exact stated size, including q=0 and wraparound cases. Equality centers in one parity satisfy x_j+x_(j+1)+x_(j+h)=1 with h=(n+1)/2; shifting h and using 2h≡1 (mod n) forces x_j=x_(j+h+1), with gcd(n,h+1)=3. Hence one of three phases in each of two parity sides, exactly six labeled maximizers. Finite tests support but do not replace the infinite edge-accounting and recurrence proof.

## originality

PASS

Brešar and Samadi already prove the general |E|/δ upper bound and an equality-structure theorem for edge open packing; they therefore cover the n upper bound and bipartite necessity, which are not new. Pandey–Santra give general characterization and Das–Santra algorithms for other graph classes, without an explicit all-residue Möbius-ladder value or count in inspected material. The separate untwisted prism C_n□K₂ belongs to a different graph family and has the shifted equality phase 6|n; it does not imply the twisted result via parameter renaming. The surviving contributions are the all-n six-residue lower constructions, exact n or n−1 dichotomy, and exactly-six optimizer rigidity. An unindexed generalized-Petersen/efficient-star-packing source could cover these specific formulas, retained as priority risk.

## value

PASS

Möbius ladders are canonical cubic graph families; edge-open packing is a natural induced-star invariant. The Möbius twist changes the divisibility phase relative to circular prisms, and the global formula plus classification of every maximum configuration at equality is a useful structural classification rather than a tiny numerical gain. The mathematical reason is the exact obstruction from bipartiteness and periodic star-center tilings, with constructive matching bounds on every residue class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
