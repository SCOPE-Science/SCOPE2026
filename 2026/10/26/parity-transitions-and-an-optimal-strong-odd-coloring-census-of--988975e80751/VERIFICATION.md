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

# Verification of gear-graph strong odd coloring

The source of the standalone reproducibility program is `verify.py`. Run `python3 verify.py`; it requires Python 3.9 or later and no third-party modules. Its output from a completed run is included as `verification_output.txt`.

The program independently constructs all graph edges in direct tests for \(3\le n\le7\). It directly evaluates properness and, for every graph vertex, the occurrence counts of the colors on its open neighborhood. This is compared with a dynamic program enumerating closed walks of the two explicitly defined state graphs while tracking each rim color's parity. Direct resulting named optimal-coloring counts at lengths \(3,4,5,6,7\) are \(48,360,49680,6,168\), respectively. A separate equality-subset inclusion-exclusion enumeration verifies the \(68\) nonhub subdivision assignments on the five-rim exceptional case.

The parity dynamic program agrees with the odd-length recurrence for every odd \(3\le n\le39\), excluding the separately analyzed exceptional order five, and checks the minimum palette and smaller palettes for all \(3\le n\le12\). It also computes named optimum counts \(37920\) for \(n=8\) and \(10670760\) for \(n=12\), with further larger cases shown in its output. These finite computations are reproducibility tests, not a replacement for the structural proof of the infinite result.

Independent scientific validation and external certification have not been performed.
