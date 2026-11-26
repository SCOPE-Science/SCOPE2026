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

The finite permutation transition monoid is a group, and the DFA on that group accepts exactly when the induced permutation squared sends the initial point into the final set. For n≤2 the squares are identities, and feasible minimal input sizes 1 and 2 exist (a unary swap with one final state has size 2). The cycle and adjacent transposition generate S_n, and its action with one final point separates the original n states. For the root final set T={g:g²(0)=0}, a right stabilizer element d lies in T because the identity lies there. If d is nonidentity and fixes 0, left multiplication by the transposition t=(0 a) for a point a moved by d yields t∈T but (td)²(0)=d(a)≠0. If d moves 0 to x, then d(x)=0, and t=(0 a) with a outside {0,x} gives (td)²(0)=a≠0. Triviality of the right stabilizer separates g and h by a left continuation t g^(-1) for d=g^(-1)h; every such continuation is a positive word because the generators have finite order. Unary squaring simply changes the generator to its square on the original n states, so cannot attain n! for n≥3. Frozen artifacts/check_square_root.py and its stored output were inspected without execution; their finite n≤6 verification is corroboration, not the proof.

## originality

PASS

The transformation-state construction, the generators and related operation results are existing tools. The distinctive claim is the exact deterministic permutation-class maximum and binary witness, including a proof that bijective continuations alone separate all n! states. Neither the unrestricted result nor the inspected near catalogue claims give this separation.

## value

PASS

The permutation restriction forbids the general witness's noninjective transition and continuation. Identifying exactly when the natural group construction pays its full factorial cost, with the smallest possible alphabet, closes a natural worst-case question. The stabilizer witness resolves a distinction the trivial transition-count upper bound alone cannot address.

The dated certificate retains the supplied scientific assessment, sources and limitations.
