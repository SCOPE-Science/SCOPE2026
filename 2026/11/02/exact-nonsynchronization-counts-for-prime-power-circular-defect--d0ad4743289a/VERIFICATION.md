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

The defect-one primitivity step can also be checked directly here. For a nonsynchronizing automaton, form the simple graph with an edge between each pair that no word merges. This graph has an edge because a minimum-rank image is a clique of size at least two; a acts transitively by graph automorphisms, so it is regular, of degree d. The letter b is an endomorphism. Its two colliders u,v are nonadjacent, and b is injective on the union of their neighborhoods. Both neighborhoods of size d map into the same neighborhood of size d, so N(u)=N(v). The only duplicated edges under b are the d pairs of edges incident to u,v and a common neighbor. Hence b maps the edge set onto the edges of the induced graph obtained by deleting the unique omitted state e, since that graph has exactly |E|-d edges. It follows for every x that N(bx) minus e equals b(N(x)), using equality of the two preimage neighborhoods at the duplicate image. Degree d then specifies whether e must be added back. Thus b, like a, preserves the equivalence of identical neighborhoods, a nontrivial proper congruence. Translation-invariant congruences are subgroup coset partitions and the nontrivial ones at p^k are exactly residues modulo p^j. The converse holds because missing even one quotient fiber would mean rank ≤n-2, so every preserved quotient operates by permutations. For selected levels J, each parent fiber contributes an independent child permutation, giving G_p(J); distinct targets at the finest level force just one defective fiber. Choose it in L ways, then choose the missing image, unordered kernel doubleton and bijection from the kernel classes inside it, giving m! binom(m,2) there and m! in every other fiber. Inclusion–exclusion gives the formula without disjointness assumptions. The unrestricted count is n! binom(n,2) by the same kernel argument; any rotational stabilizer fixes the single missing image and is trivial. Independent enumeration over collision pairs and injections plus pair reachability gave 16/144 and 14848/1128960 at n=4 and 8, including matching mod-2 and mod-4 counts at 8. An independent integer calculation checked the five displayed orders and small nested quotient permutation counts. No frozen code was executed.

## originality

PASS

Credit the previously established defect-one synchronization theorem and the exact n=8 normalized census, including its two-residue intersection. The distinct contribution is the exact labeled count for every prime power, specifically the arbitrary-depth nested-chain intersection correction and its assembled all-order count, with a free cyclic quotient. The checked structural and finite results do not supply these general intersections.

## value

PASS

Conditioning on the smallest nonzero rank defect is natural in synchronization theory. The chain of modular obstructions at prime powers produces genuinely overlapping events beyond the two levels of the initial census. The exact probability and class count quantify those overlaps for all levels and give an interpretable benchmark for random circular automata, not just another finite table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
