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

Minimality on a Cantor space makes T aperiodic. The only candidate S-preimages of T^b x are x (if p(x)=b) and T^d x (if p(T^d x)=a). Exactly one exists iff membership in {p=b} is the same at x and T^d x; this gives both directions using bijectivity on the T-orbit and compactness for the inverse. On the integer orbit each increasing S-orbit crosses the cut at 0 exactly once. There are a guaranteed crossings plus k positions of jump b in the next block of length d; periodicity makes the count T-invariant and minimality makes it constant. Translates of a T^d-minimal set are equal or disjoint and their union is X; the number of clopen components divides d. For the upper bound, conjugation of T^2 by the swap of disjoint clopen levels A and TA realizes p=3,1,2 on A,TA,T^2A respectively and only positive jumps 1 through 3 elsewhere; T^2 is minimal by total minimality. Independently replayed 48,960 cyclic assignments and 6 conjugation proxies, without executing verify.py. Finite cycles corroborate the bounded classification/construction only, not the Cantor or universal minimality assertions.

## originality

PASS

Credit prior constant orbit number, coboundary formula, standard cyclic decomposition, and prior explicit minimal three-jump example. The supported distinct result is the fixed-pair necessary and sufficient criterion and the universal sharp construction conjugate to T^2 on every totally minimal Cantor system.

## value

PASS

The admissibility test can be applied to any prescribed pair without solving a general speedup-equivalence problem. The sharp bound distinguishes failure of a nontrivial small alphabet from failure of nonconstant positive realizations: the first possible alphabet is achieved by a minimal speedup with explicit conjugacy on every totally minimal Cantor system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
