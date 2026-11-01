---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Log Nash objective is concave, and KKT scores G_j≤n with equality for funded projects are necessary and sufficient; every optimum has unique reported utility vector. Reviewed provided exact SymPy enumerator: all 329 anonymous profiles n=1..4 (7+28+84+210), certified optimizers via rational 1/24 lattice KKT and exact sqrt17 algebraic candidates, enumerated full optimal face vertices by exact linear solves and every unilateral ballot change. The program asserts 0,0,0,6 manipulated profiles, 12 changes and two gains. Independently reconstructed representative [B,AB,C,AC]: true p=(0,1/2,1/2), misreport AB→A has Nash q=(3/8,1/4,3/8), both satisfy exact G=[4,4,4], and true gain (5/8)/(1/2)=5/4. Analytical two-project rule reduces to singleton counts a,b and p=(a/(a+b),b/(a+b)). The complete finite census depends on careful inspected certificate, not a newly performed independent full rerun; full checker can be replayed with SymPy 1.14.

## originality

PASS

Best-of-knowledge originality with disclosed antecedents and material access limits. No established equivalence from other incentive concepts to the full four-voter fixed-cell enumeration was found; comparing count vectors, truth utility, all tie allocations matters. Earlier theorems allow the existence of manipulation but neither imply its exact first size nor the finite orbit count, complete gains, and tie-invariant witnesses.

## value

PASS

The exact smallest strategic-vulnerability cell for the established Nash budget rule, complete orbit classification and sharp gain quantify behavior not entailed by asymptotic/global factor-2 bounds. Exact four-voter cell is a natural benchmark with directly interpretable fairness incentives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
