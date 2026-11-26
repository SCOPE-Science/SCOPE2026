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

For an existing partial function, s≤r is exactly the condition for a surjective completion. If s<r, any color can be placed at a chosen blank and there are still enough positions for the remaining missing colors; if s=r≥2, the missing colors can be permuted. Only r=s=1 forces a new atom in a feasible premise. For an infeasible partial function, deletion of a singleton color preserves s−r, whereas deletion from a repeated color reduces it by one. This gives the stated minimal shortages; conflict pairs give the other inconsistent stems. Here stem means inclusion-minimal for a fixed conclusion atom, as specified in proof §3. In a full minimal shortage, one can take an unasserted value of a different already-used color at some input: there are at least two used colors, and no proper subset forces any color but the initially missing one. This justifies the lower bound even when a proper subset has a different nontrivial conclusion. Any direct basis must fire a rule with the exact stem to produce its witness atom; the displayed rules suffice on the original input in all cases. The three counts follow by choosing blanks, colors and ordinary or restricted partitions. The restricted recurrence distinguishes the block of the last element having size two from having larger size. For q=3 the only infeasible partial assignments are full functions missing a color and one-blank monochromatic assignments; removing those and the feasible one-blank forces and adding top yields the lattice formula.

## originality

PASS

The distinct result is the explicit classification and enumeration for all onto assignments with n>q≥3. The general optimality theorem for stems is prior work; the strongest retrieved indexed analogues treat one prescribed histogram or permutations. Neither yields the displayed shortage family or the onto-assignment counts.

## value

PASS

A surjective assignment is a natural global constraint. The classification gives an exact one-round representation and its unavoidable rule cost, separating local clashes from genuinely global shortages. The scope distinction makes the count useful for direct evaluation rather than claiming a generic Horn minimization result. The three-color counts provide an explicit boundary and first examples of the general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
