---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

At each vertex of C5 exactly five balls contain it: its singleton, three radius-one centered neighbor/self/neighbor balls, and all vertices. Independent selection of one averaging row per output vertex linearizes ||M f||² as the maximum of ||Aσ f||² over 5^5=3125 nonnegative matrices; a Perron nonnegative top singular vector justifies exchanging maxima. With B=15A, the condition ||A||²<5/3 is exactly positive definiteness of integer 375I−B^TB. I independently implemented Bareiss fraction-free determinant and verified five leading Sylvester minors for each matrix: 3120 strict and precisely five exceptional rotations. For the representative, sympy exactly verified characteristic polynomial u(u−2)(u³−19u²+62u−36) for H=(3A)^T(3A). Its Perron root λ>5/3 is the unique root of 81λ³−171λ²+62λ−4 in (1.670,1.671), with positive eigenvector (a,1,a,c,c), a=(27λ−2)/D and c=(9λ−2)/D. Independent numerical strict checks for all twenty competing averaging rows confirm this matrix is active; packaged interval inequalities provide rational certification of activity. Simplicity and the strict gap exclude all other equality rays, while independent signs on input are irrelevant. This is a genuinely exhaustive *finite* proof of C5, not a claim for other graphs.

## originality

PASS

The original Soria–Tradacete graph maximal-operator paper defines the *centered* operator and emphasizes p≤1, star and complete graphs. González-Riquelme–Madrid 2020 introduce uncentered notation but their sharp ℓ² theorems concern centered star/complete graph families; their variation theorems are not this norm. A recent five-vertex census treats centered edge variation, not this uncentered C5 strong ℓ² constant. Hence the full cubic constant and all extremizing rays are not dominated by inspected publications. Earlier unindexed finite graph norm computations remain a priority risk.

## value

PASS

The five-cycle is a canonical smallest noncomplete odd cycle and a natural test case for unrestricted ball centers. Determining an exact algebraic strong ℓ² constant and the *complete* equality rays is mathematically meaningful: it exposes the rigid optimal concentration pattern and distinguishes uncentered and centered graph maximal operators. A complete five-vertex exhaustive certificate qualifies as an exact natural invariant, not an arbitrary or failed infinite conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
