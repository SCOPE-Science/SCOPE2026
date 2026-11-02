---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Normalized complex Hermite decomposition of full order-two Gaussian Fock space has one scalar angular sector -1 and a 2x2 sector for each j>=1. Direct incomplete gamma integration gives A_x^(j)=I_j(x)I+E_j(x)[[0,sqrt(j)],[sqrt(j),j-1-x]], E_j=e^-x*x^j/j!. Thus [A_x,A_y]^(j)=(x-y)*sqrt(j)*E_j(x)E_j(y)[[0,1],[-1,0]], yielding exactly singular pair s_j=|x-y|sqrt(j)e^-(x+y)(xy)^j/(j!)^2 and one-dimensional kernel, all Schatten orders by factorial decay. Adjacent ratio q/sqrt(j(j+1)^3) gives mode switch. Strict log-concavity of branch objective gives unique x_j,y_j; Robbins factorial remainders imply each maximum M_j < 1/(pi sqrt(2e)), Stirling shows convergence to that sharp but unattained supremum. Independent numeric 18 block commutators, several M_j, and symbolic radial identities corroborated. Only full order2 centered disks, not individual true levels or off-center disks.

## originality

PASS

The relevant 2019 primary paper establishes general radial block representation for polyanalytic Fock operators, a necessary foundation; inspected theorems do not give the explicit two-disk commutator singular spectrum, mode staircase or globally sharp nonattained constant. The Fulsche–Hagger 2024 revision develops essential commutants and Toeplitz framework, not this disk-pair optimization in inspected relevant sections. Best-of-knowledge PASS with possible unindexed operator-ideal formula risk.

## value

PASS

Analytic Fock radial concentration operators commute, so the first bianalytic level where the two disk cutoffs fail to commute is mathematically natural. Full singular spectrum, all Schatten norms, exact mode switching and sharp global nonattained norm are significant quantitative operator invariants useful for localization questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
