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

On the labelled crown graph the open-neighborhood sum at b_i is A-f(a_i), and similarly on the other side. The threshold is therefore exactly the two side-sum inequalities. A negative vertex sees all opposing 2's except a possibly matched one; cases of zero, one, and at least two opposing 2's give exactly the stated cell restrictions. The nine cells partition the n named pairs; their multinomial correctly counts labelings, without dividing by graph automorphisms. With a 2 on both sides each side has weight at least 3; if one side has no 2, it has weight at least 2 and the other side has only positive labels. For n>=5 this gives weight at least 7; for n=3 the no-2 side has odd weight and the only weight-six arrangement of this kind is all ones; for n=4, weight at most six would force the other side to be all ones, leaving no defending 2 on either side and hence all ones. Odd n>=3 attain six with two 2's per side and the indicated 1/-1 counts; even n>=4 attain it with one 2 per side in the same deleted matching pair. G_2 is a matching and its unique minimum is all ones. For n>=4, weight-three side profiles satisfy 3t+2u=n+3. Odd n forces a positive even t, so all pairs of side profiles are compatible. Even n permits a unique 2; each direction of a bad match has U_n D_n possibilities by symmetry and their intersection forces two distinct 2 positions and the binomial product J_n. Inclusion-exclusion proves the claimed minimum count. G_3 separately has nine pairings of two-2 side profiles plus all ones. A separate row-mask enumeration checked every full coefficient for n=2 through 7 against a sorted-multiset enumerator and recovered minima counts 1,10,84,900,3280,44100 (checks/frozen_checks.py argument 1; output checks/1.txt). Those finite checks corroborate rather than establish the universal formula.

## originality

PASS

The full labelled signed-total-Roman polynomial and uniform minimum multiplicities are the supported distinct claim. The closest inspected results either count different Roman labelings on the same graph or count the same signed-total-Roman invariant on other graphs. Known special-case minimum values are not credited as new.

## value

PASS

The crown is a natural perturbation of the complete bipartite graph in this signed total-domination problem. The matching-pair compression replaces exponential enumeration in n with at most binom(n+8,8) cell profiles, and the parity law gives explicit degeneracies of the optimal labelings. These are useful extension data beyond the numerical invariant and comparison examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
