---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a nonempty face F the union has size in [k,n-k]; applying common neighbors twice closes F to the family of all k-subsets of that union. This closure is equivariant and restricts the duality to set complementation. Rank-selection shellability gives concentration in degree r, also with reduced H_0 when r=0. The ribbon formula is the augmented alternating character normalized by (-1)^r to give the top character. An explicit check of its Schur expansion uses standard tableaux with descent set {k,k+1,...,k+r}: entries through k are in row one, and the next r+1 entries start successive lower rows. The remaining row indices cannot increase, so no row below the second can be extended (it would require a prior extension of a higher row). Filling j-1 further boxes of row two and then finishing row one gives one tableau for every j=1,...,k, of the claimed shape. For the mixed trace, a setwise fixed chain is reversed and each vertex is sigma^2-invariant. For even chain size its lower half must end at A strictly contained in complement(sigma A), equivalent to A disjoint from sigma A and |A|<n/2; this gives exactly the weighted signed parity orbits. For odd chain size the middle set chooses one parity half of every cycle, possible exactly when every cycle is even, and the lower chain is a chain of subsets of these halves. The reversal sign (-1)^(t(t-1)/2), simplex Euler sign (-1)^(t-1) and augmented -1 give the stated bracket; the top-degree sign is (-1)^r. For n=2k only middle sets can contribute, as required for a discrete complex. Direct bounded chain checks give traces 1 for (n,k,sigma)=(4,1,(12)) and 3 for (4,2,(12)(34)). The frozen checker was inspected, not executed; neither the case checks nor its recorded test plan are used as an infinite proof.

## originality

PASS

The distinct contribution is the explicit mixed character for all permutations and parameters, not the known Boolean model, the duality construction, or the ordinary character via a ribbon. The strongest same-day indexed match gives exactly part of the ordinary character (k=2), not the character on cosets involving duality. The inspected general topological sources give the action or its underlying homotopy model without evaluating these mixed traces. No claim about priority of the ordinary specialization is made.

## value

PASS

This identifies the action of a natural involution jointly with all coordinate symmetries. It reduces a trace calculation on potentially enormous neighborhood complexes to weighted configurations from even cycles and resolves both duality eigenspace representations at once. The sign and middle-rank case are essential; this is more than a dimension calculation or a computation of the already understood ordinary action.

The dated certificate retains the supplied scientific assessment, sources and limitations.
