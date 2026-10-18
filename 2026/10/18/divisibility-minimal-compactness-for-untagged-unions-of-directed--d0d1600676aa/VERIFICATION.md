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

# Verification and limitations
The evidence is the self-contained \(\mathsf{ZF}\) proof in `RESULT.md` (five numbered steps). Its critical tests are: \(C_m\to C_n\iff n\mid m\); finite connected hulls in each weak component; finite witness amalgamation showing that one cycle length works on all finite subsets; minimal-target pinning of every original vertex; and definable least-target grouping before invoking the component compactness assumptions. These checks are deductive and cover arbitrary set-sized graphs, not only finite sample instances.

No external program, numerical enumeration, formal proof assistant, or independent audit is asserted. The argument does not settle analogous claims for infinitely many template components. Potential older results under different names could overlap with the union formula.
