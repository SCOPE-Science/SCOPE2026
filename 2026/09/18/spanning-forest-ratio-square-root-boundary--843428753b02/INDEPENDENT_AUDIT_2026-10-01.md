# Independent audit — A square-root boundary layer for the consecutive spanning-forest ratio conjecture

Audited: 2026-10-01 UTC

## Correctness — PASS

The complete-graph ratio follows from exact double counting of one-edge extensions, with the average extension deficit \(\overline q_k\). For an arbitrary noncomplete graph, deleting at least one possible edge makes \(\overline q_k<1\) sufficient. The line-graph path count and cycle union bound give this strict deficit in the range \(n\ge3k^2\). For \(k=3\), direct counting yields \(\overline q_3=12(n+4)/(n^2+3n+4)\); independent exact enumeration reproduced this formula for \(5\le n\le15\) and reproduced the two complement-type counts at \(n=5,6\), closing the exceptional cases.

Risks: The all-\(k\) path/cycle estimates were checked algebraically rather than by an exhaustive computation, which would not prove the infinite range in any case.

## Originality — PASS

The Bencs--Csikvári paper states the stronger consecutive-ratio problem but the accessible source material does not supply the square-root boundary theorem or the all-order \(k=3\) case. Published-archive search found a later missing-edge-range result that complements rather than subsumes this boundary theorem.

Equivalent-formulation search: The searches used both edge-count \(k=n-s\) and component-count \(s\) formulations.

Broader-coverage search: Neither result dominates the other parameter range.

Database/table check: The theorem is structural and infinite.

Claim-versus-prior implication: The audited result is a genuine partial theorem toward the stronger consecutive statement.

### Source inspections

- **An inequality for the number of independent sets of matroids with an application to the forest-tree ratio of graphs** — Abstract and bibliographic material; full text was unavailable through attempted arXiv and institutional routes. Assessment: The accessible primary statement proves the aggregate forest/tree ratio, not the audited consecutive boundary theorem.

## Scientific value — PASS

The theorem establishes a growing boundary layer for a new normalized-matching-type conjecture and completely settles the first fixed rank where cycle corrections enter. This is a mathematically motivated infinite regime rather than a finite data point.

## Limitations

The result proves the consecutive-ratio conjecture only in the boundary range \(n\ge 3k^2\) and for the complete fixed case \(k\le3\); it does not resolve deeper ranks and does not optimize the constant 3. The motivating conjecture is very recent, so unindexed parallel work remains a residual originality risk.
