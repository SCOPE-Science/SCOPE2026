---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The 12 vertices (i,j), i≠j in {1,2,3,4}, form four triangles (12 J edges) connected by six opposite-arc K bridges. Triangle J energy J(s²-3)/2 minimizes at s=±1. For h<K, putting all field on bridge pairs gives H>=-4J-6K; equality orientations of abstract K4 must have every indegree 1 or 2, exactly 24. For h≥K, split field K onto each bridge and h-K on triangles: Kxy-K(x+y) minimizes at unlike or ++ bridge pairs and triangle F(s) favors s=1 until h=K+2J, ties s=1,3 there, and s=3 above. Equality constraints simultaneously feasible. At h=K triangle sums ±1 and each bridge not --; 114 configurations with magnetizations (0:24,2:60,4:30). In K<h<K+2J, one negative per triangle and no reciprocal negative bridge gives 3^4-6·3²+3=30 with magnetization4. At h=K+2J, 0 or 1 negative per triangle gives 1+12+48+72+30=163 in magnetizations12,10,8,6,4. Above, unique all-positive state. Thus exact energies -4J-6K, -4J-2K-4h, 12J+6K-12h for the three field bands (continuous at endpoints). Independently constructed all 12 triangles/6 bridges, enumerated all 4096 spin configurations, checked energies and magnetization counts at h=0,K,K+J,K+2J,K+2J+J for (J,K)=(1,1),(3,5),(10,2); these finite checks corroborate all-real coupling proof. Model classical ±1 spins, not vector/quantum or thermodynamic limit.

## originality

PASS

Coffey–Trugman 1992 studies the *same* truncated-tetrahedral graph with two bond orbits, but its spin Hamiltonian is quantum/classical vector Heisenberg rather than collinear Ising, so its field response and degeneracies do not entail these combinatorial Ising counts. Strečka–Karľová–Madaras study Ising plateaus on five Platonic (not Archimedean truncated tetrahedral) graphs; planar triangular nanoclusters and square-lattice truncated-tetrahedral spin-direction models are different objects. Thus the exact uniform two-coupling Ising phase/critical count is best-of-knowledge original; possibility of a specialized unindexed earlier Ising computation remains.

## value

PASS

A finite frustrated molecular-magnet cluster has two natural edge-orbit exchange parameters. Exact all-(J,K>0) field thresholds, magnetization sectors and residual ground-state entropies provide a complete physically meaningful phase diagram, including unusually high 114/163 critical degeneracy and a robust 1/3 plateau. Finite systems can support valuable exact structural classifications; no thermodynamic phase transition or quantum prediction is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
