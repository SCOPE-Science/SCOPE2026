---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Through round k, vertices beyond distance k stay homogeneous by regularity and locality of the root marker. Independent coordinate reflections and permutations preserve every histogram fibre. To split the newly reached shell, let N be the multiplicity sum of inward neighbours; summing their histograms gives B_r=(N-2)m_r and B_j=(N-1)m_j+w_{j+1}m_{j+1} for 1≤j<r with w_r=2 and other positive weights one. Inversion works for N≥3. If N=1, one nonzero coordinate is determined by the shell; at N=2 one antipodal coordinate can collide only with two nonantipodal coordinates summing to r, and for r≥3 decreasing one of those coordinates of size at least two leaves two positive coordinates, distinguishing the predecessor multisets. This proves the induction without a higher-round assumption. The final antipodal shell is a singleton, but it is combined with the penultimate shell one round earlier. The histogram orbit sizes follow from coordinate position choices and signs, and their distance enumerator is the partition rectangle Gaussian polynomial. For r=2 the graph is a hypercube: all vertices in a shell have the same inward and outward degrees, and each successive shell separates when first reached until only the singleton antipode remains unseen. Exact direct refinement on eight independent test cases, including C_6^5 and C_4^5, matched every partition and the least stable round. The frozen verifier's recorded 21 full-graph configurations include six supplemental r=1 cases with duplicated cyclic neighbour moves, outside the theorem; these checks are not evidence about simple C_2 factors.

## originality

PASS

The supported distinct core is the exact all-round profile in arbitrary powers of even cycles of length at least six. The stable d=2 case and the hypercube comparison are covered, and the odd-cycle analogue has essentially the same conclusions but a different inward-neighbour hypothesis. The frozen work does not claim novelty for the hypercube shell partition; its role here is to identify the exceptional boundary. The finding does not obtain the main scope by parameter substitution into the inspected material.

## value

PASS

A roundwise description gives strictly more than orbit-exactness or a depth bound. It resolves when coordinate structure becomes visible and why the extra antipodal neighbour multiplicity destroys it only for the four-cycle factors. The low-multiplicity collision analysis is useful in deciding when shell-by-shell refinement proofs transfer to other products.

The dated certificate retains the supplied scientific assessment, sources and limitations.
