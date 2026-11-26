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

For the budget counting each undirected edge once, concavity of the Rayleigh minimum on the space orthogonal to constants allows averaging all feasible allocations over the graph automorphism group. With m=n-1, the reduced Laplacian has ordinary zero-sum modes of eigenvalue ma+b, the positive even mode (m+1)b, and the odd block with diagonals mb and 2ma+b and off-diagonal of magnitude sqrt(m)b. Normalizing to unit gap forces mb>1 and a at least the larger of (1-b)/m and ((m+1)b-1)/(2m(mb-1)). The odd-bound budget is minimized at mb=3/2 and meets the internal constraint exactly for m<=6. For m>=7 the difference of the bounds has the sign of 2(mb)^2-(m+1)(mb)+m, positive at mb=1, negative at 3/2, and positive beyond the larger root. The odd budget decreases up to the lower crossing and the internal budget then increases; the far odd branch also increases. This proves the radical branch and the scaling B/D_n. The even and upper odd modes remain above one, so multiplicity changes at n=7, one size before the formula changes. Fresh full-Laplacian checks at n=3,6,7,8 gave multiplicities 1,1,11,13 and respective D_n values 11/2, 7, 15/2, 9-sqrt(2)/2.

## originality

PASS

The supported distinction is the exact continuous-time, budget-normalized solution and its mode collision, not the fastest-mixing framework or the part-size-eight change for the closely related discrete-time problem. No inspected result covers the full continuous-time statement.

## value

PASS

A single forbidden edge is a natural perturbation of a standard network-design benchmark. The solution exposes which modes limit the optimal continuous-time rate, and separates the first multiplicity collision from the change in allocation formula. The optimizer and normalization are usable in this design problem and cannot in general be recovered by scaling the known discrete-time design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
