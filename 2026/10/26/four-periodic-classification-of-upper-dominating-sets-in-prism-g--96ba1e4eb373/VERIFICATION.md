---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For a minimal dominating S in connected d-regular G of N vertices, partition selected vertices into isolated I and nonisolated F; each f in F needs a unique outside private neighbor p(f). With Q private neighbors and R the rest, all d|I| incident edges enter R, giving |I|<=|R| and 2|S|<=N. At equality, d-regularity and connectedness force either F empty, giving an independent bipartition side, or I empty, yielding a perfect matching cut between S and its complement. In the labelled prism any independent side of size n must alternate one vertex per rung (two patterns only when n even). A perfect-matching cut either contains a bichromatic rung, forcing all rungs to have the same orientation (top/bottom layers), or all monochromatic rungs and a binary cyclic color word with runs exactly length two, forcing 0011 repeats (four phases if 4|n). Hence Gamma=n and U_n=2+2*1_{2|n}+4*1_{4|n} for every n>=3. Direct independent exhaustive tests of all n-subsets for n3..9 reproduced the full families and counts [2,8,2,4,2,8,2].

## originality

PASS

Qualified best-of-knowledge: general regular graph upper domination bound and equality framework are prior. Allagan et al. 2026 count MINIMUM-cardinality dominating sets on precisely the same prisms; their modulo-four numbers do not count maximum-cardinality inclusion-minimal dominating sets. The four-periodic exact upper-domination vertex-subset census was not found in inspected sources; full Southey/Henning and Zverovich papers inaccessible, recorded risk.

## value

PASS

The upper domination number Γ and the number U_n of maximum-cardinality minimal dominating sets are natural graph invariants; the exact 2/4/8 periodicity gives a complete structural classification for a canonical all-n prism family, including odd nonbipartite instances. The result is distinct from minimum dominating set counts and develops a useful perfect-matching-cut equality structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
