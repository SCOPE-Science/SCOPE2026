---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For any finite nonempty poset, an upset U intersects upset A precisely when maximal traces U∩Max(W) and A∩Max(W) intersect, via extension to a maximal point. Thus within a fixed maximal trace an inclusion-smaller box neighbourhood dominates support/hitting, giving minimal trace-class representatives; box necessity follows by supports U and singleton-maximal upset tests using ≤width(W) instances. For universal diamond, inclusion-LARGER same-trace neighbourhoods dominate counterexamples; the test with scope Max(W) minus the trace of U and instance complements of principal downsets of minimal generators of U recovers existence of same-trace supersets and so maximal signature; |Min(U)|≤width(W). Depth-one variable valuations and induction give the exact same-poset all-formula iff. An antichain gives faithful complete recovery, while nonmaximal points yield distinct constant persistent indistinguishable families; an antichain on w elements realizes sharp arity w. On a chain, choices of empty upset and one extremal nonempty upset yield 2(n+1) independent box and diamond signatures and 4(n+1)^2 classes of constant assignments. Independently brute-forced both semantic clauses for ALL neighbourhood families of chain3/chain4, fork3, antichain3 and all upsets arguments of arity≤width: equivalence classes agree exactly with signatures (8,10,24,256 signatures per modality respectively). Finite checks supplement general poset proof.

## originality

PASS

Best-of-knowledge originality of the precise final claim, with prior partial/general coverage credited. Classical Boolean BAIO result establishes recovery of every raw neighbourhood family with sharp n-instance bound using singleton arbitrary subsets; those singleton probes cease to be admissible for nonmaximal elements of ordered posets, so the stronger classical reconstruction cannot transfer. Das–Khanra–Sardar define the exact two-sided positive semantics and duality agenda but do not give maximal-trace signatures or chain count in inspected text. Search failure alone is not proof of novelty, and explicit residual risks remain.

## value

PASS

The exact observational quotient measures the intrinsic information lost when Boolean instantial modalities are interpreted only on the upsets of an ordered intuitionistic frame. It provides canonical fibrewise invariants, sharp optimal formula arity, nonfaithfulness criterion, and a nontrivial exact chain census relevant to completeness, finite model comparison, and duality problems; not a mere relabelling of standard neighbourhood minimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
