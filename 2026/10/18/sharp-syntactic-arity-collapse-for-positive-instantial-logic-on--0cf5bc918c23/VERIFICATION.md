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

On the stated persistent frames all argument truth sets are upsets, since box families increase and diamond families decrease along the order. For a box witness U, choose one point of U intersecting each argument, then assign each index to a maximal sampled point above its chosen point. Maximal sampled points are an antichain of size at most w and still belong to U; the upset property places each in all arguments of its block. Conversely a witness of the block meets hits every original argument. For a diamond failure choose points of U outside the arguments, keep minimal sampled points, and assign downwards; each retained point lies outside all arguments of its block and hence outside their union. Failure of one grouped diamond implies original failure since every original argument is contained in its block union. Existential and universal interchange with the corresponding finite disjunction and conjunction; different neighborhoods do not invalidate either equivalence. The finite samples, not the whole carrier, need extrema. Recursive substitution preserves depth because the same argument subformulas occur within one enclosing modality under only lattice connectives. For sharpness let S be the upset of a maximum antichain E and compare constant diamond families of proper subupsets of S with and without S. If S refutes a k<w test, the upset of k chosen counter-witnesses in S still refutes it and omits an element of E: a chosen point can force e in E only by being e. This works also for the empty generator set at k=0. Thus all lower-arity operations agree on every upside-closed argument tuple and induction handles all nesting. At arity w the arguments S minus one antichain point each are upsets; every proper subupset satisfies one, whereas S satisfies none, with empty scope. An independent exhaustive test on the seven naturally labelled three-world orders (`python3 /workspace/branches/independent_checks.py 5`) gave 584,730 bounded comparisons, including both local clauses and lower-arity pairs. The proof covers infinite carriers as well; the check does not.

## originality

PASS

There is material overlap with the same-day finite width signature result in precisely the same semantics, not a new observation that width suffices for finite-carrier observational determination. The supported distinction is explicit positive term elimination for both modalities on all finite-width posets, even without global extrema, plus sharpness on each fixed carrier by a co-witness pair. No priority ordering is inferred from same-day dating.

## value

PASS

A width-indexed reduction of the positive vocabulary matters for expressivity: it translates an actual nested formula without requiring named worlds or neighborhood information. The matching obstruction on each carrier shows that arbitrary nesting cannot compensate for fewer instance positions; the bound is not merely a discrete worst case or an observational recovery theorem. It applies even to infinite chains or other finite-width orders lacking global extrema. It is not a claim of efficient formula size or sharpness under stronger neighborhood restrictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
