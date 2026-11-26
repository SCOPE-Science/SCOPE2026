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

D_n is the Birkhoff face attained at zero diagonal. The positive off-diagonal feasible point and connected bipartite constraint graph give dimension n(n-1)-(2n-1). The minimal face containing two matchings is supported on their union: common edges are fixed and each alternating cycle in their symmetric difference contributes one segment. Thus adjacency is exactly one nontrivial cycle c=sigma^{-1}tau on changed support. The derangement condition excludes i->sigma^{-1}(i) on this support. Proper subsets of forbidden arcs have h directed runs on v=s+h vertices. Marking a run and counting positive compositions of its selected lengths and intervening gaps gives the stated l/h factor. After contracting the h paths there are (h+m-1)! cyclic orders on the blocks for each choice of m extra vertices; this includes a single contracted path whose ends close up in the ambient candidate cycle. If a selection contains an entire forbidden directed cycle it can only extend to that cycle and no additional arcs or vertices, giving the separate signed correction. This proves the refined polynomial, including h=v=0 and all q>=2. Independent exact enumeration of every type for n=3..6 compared all coefficients by enumerating derangements tau and testing c. For n=4 the spectra are 2T^2+4T^3+T^4 and 4T^2+2T^4; for n=5 the two degrees are 33 and 31. A smooth fixed point has exactly d invariant curves. Both n=4 and 5 pass the strict excess test and for n>=6 the transposition and three-cycle union bounds already exceed d: the excess starts at 6 for n=6 and its successive difference is n^2-4n+2>0. Thus each normal cone is nonsimplicial, independently of lattice or characteristic. The one-dimensional n=3 case gives P^1. Conjugacy type class sizes and division by two correctly count all edges. The frozen checker.py beside RESULT.md was inspected, not executed; the separate finite comparison corroborates the proof only on the stated range.

## originality

PASS

Pass for the local support-size generating polynomial stratified by endpoint cycle type and its proved consequences. The adjacency criterion, basic toric correspondence and edge-length interpretation are not originality claims. There is meaningful aggregate overlap with a later-indexed derangement edge-length census; on the available evidence it does not furnish the per-type invariant, and no priority conclusion rests on date alone.

## value

PASS

A local curve-degree count is a natural invariant of these matching-polytope toric charts. Refining by changed support reveals differences invisible in global histograms or in the bare adjacency rule, including two different local distributions at the same n. The explicit cycle-type formula also controls the unrefined degree, while a separate uniform bound shows that no torus-fixed chart is smooth once n>=4. Neither the counting claim nor the geometric interpretation requires a wider assertion about the entire singular locus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
