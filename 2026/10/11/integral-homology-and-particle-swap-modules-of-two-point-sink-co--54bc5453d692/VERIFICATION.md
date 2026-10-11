---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible calculations and boundaries

Run `python3 verify.py` using a standard Python 3 interpreter. No additional packages or downloaded data are needed.

The checker constructs each cubical chain complex by listing all ordered vertex pairs, edge--vertex and vertex--edge cells, and ordered **distinct** edge pairs. Oriented differentials are built directly from the graph's edges. It tests that every two-cell has zero second boundary and computes both boundary ranks modulo the primes \(2,3,5,7\). It separately constructs a signed rectangle basis of the graph cycle lattice and ranks all its coordinatewise cycle products modulo the same primes. It enumerates the side-preserving graph permutations and label-swap choices, computes signed fixed-cell Lefschetz numbers, and checks the proposed rational-character identity elementwise.

The verified graph sizes are \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)\). Their chain-group sizes \((\operatorname{rank}C_0,\operatorname{rank}C_1,\operatorname{rank}C_2)\) are respectively \((16,32,12),(25,60,30),(36,96,56),(49,140,90),(36,108,72),(49,168,132),(64,256,240)\). Their Betti vectors are respectively \((1,5,0),(1,7,1),(1,10,5),(1,13,11),(1,8,7),(1,12,24),(1,18,65)\). In total the character identity is checked for \(2120\) combined permutations; the program terminates with `VERIFY_OK` when all its assertions hold.

These checks do not show integral torsion-freeness or prove a statement for untested \((m,n)\). Those claims require the explicit primitive-image proof and relative sequence in `RESULT.md`. The checker verifies rational characters through finite Lefschetz traces, not a claimed universal computational certification.
