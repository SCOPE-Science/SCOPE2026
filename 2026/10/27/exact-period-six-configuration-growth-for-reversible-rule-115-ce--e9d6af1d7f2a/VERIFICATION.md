---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The stated Boolean rule has truth table 01110011 in descending neighborhood order. From the initially zero pair the uniform background is 001 repeated. On the right, at time 2 mod 3 the center and its right neighbor are one, giving output zero irrespective of the left neighbor, and at the other times a zero center suffices. On the left the sites through -2 obey the same induction; if the halo value at time 0 mod 3 is s, at time 1 mod 3 it is s (left neighbor zero) and at time 2 mod 3 it is s XOR NOT s = 1. Thus only site -1 needs a free temporal column outside the window. The directed edge enforces the recurrence at the middle column modulo p; starting at (-3,-2), adding one halo with initial bits zero, then n interior columns and two terminal background columns checks all nonautomatic sites, also when n=0. Uniqueness of the temporal evolution gives the bijection. An independently implemented temporal bit-constraint generator reproduced core sizes 3 and 27, starts, and all required initial scalar recurrence residuals. Cayley–Hamilton applies to u M^j P(M) v, so those residuals vanish at every index, not just at tested sizes. Separate direct line evolution with fixed background only at distant endpoints agreed for n=0..6. The recurrence plus initial values gives the two rational functions; divisibility of any period by three follows from the shielded background, so only periods three and six can contribute to Fix(F^6). At z=1/rho, (1-z+z^2)=6/rho^2 and (1-delta z)=sqrt(21)/rho, giving the claimed dominant coefficient; other exponential moduli are |delta| and 1. Fibonacci growth of B_n and 4^n possible initial pairs give the stated relative densities.

## originality

PASS

The prior rule-115 results already give the period obstruction, least-period-six examples (including a two-site witness), and even the sizes of the two rooted temporal-column automata. They are not credited as new. The exact all-window path counts, scalar recurrence and explicit spatial growth of the six-period fixed set are distinct on the evidence read.

## value

PASS

The first two admissible temporal-period classes are natural tests of how the unusual finite-support periodicity of rule 115 is distributed over spatial windows. The scalar transfer functions settle their entire labeled-window census, including the least-period-six count and the growth base distinguishing it from the Fibonacci class and from all 4^n pairs. General finite-state rationality or an isolated witness supplies neither the exact frequencies nor that growth base.

The dated certificate retains the supplied scientific assessment, sources and limitations.
