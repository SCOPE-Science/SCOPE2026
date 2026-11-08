---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The two symmetric weighted 4x4 adjacency matrices have exact characteristic-polynomial difference P_A(x,t)-P_B(x,t)=-tx[(alpha^2-beta^2)tx+2b(a alpha-c beta)]. Deleting row/column 3 of A gives principal spectrum {a,0,-a}, so by interlacing its second eigenvalue is <=a; the B Perron eigenvalue is >a. Thus evaluating the A polynomial at lambda_B has exactly the sign of lambda_B-lambda_A. The sign rule follows for every positive parameter. Since lambda_B(t) strictly increases and t lambda_B(t) runs from zero to infinity, there is exactly one positive crossing iff (alpha^2-beta^2)(a alpha-c beta)<0; all ties and fixed-sign boundaries follow. Independent SymPy checks verified the determinant identity and algebraic sample crossing; numerical tests do not replace the Perron-interlacing proof.

## originality

PASS

The source and reviewed literature already give metapopulation capacity as Perron eigenvalue and differential spectral edge sensitivity. The exact two-edge-choice all-effort Perron sign law and unique global crossover for weighted four-vertex path are additional to the inspected local perturbation theorems, though older exact graph-comparison results might imply them.

## value

PASS

A minimal but naturally motivated connectivity restoration decision has a mathematically sharp threshold at which first-order preference reverses under finite investment. The universal all-positive-parameter sign rule is more useful than isolated four-vertex numerical rankings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
