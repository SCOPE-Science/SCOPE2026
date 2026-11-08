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

# Verification

Run `python3 verify.py` with Python 3 and no dependencies beyond the standard library. The script constructs exact unrestricted partition counts via the pentagonal recurrence and odd-part partition counts via independent unbounded-part dynamic programming. It compares the implied signed-mass fiber histogram to direct enumeration of every partition for all positive \(n\le22\); for every \(1\le n\le200\), the exact product fibers sum to \(p(n)\). It checks normalized moments and central lattice masses for four additional sizes through \(n=1600\). The comparisons use exact integers for identities and floating point for scaling diagnostics. Observed exact checks: `EXACT_FIBERS_OK n=1..200 direct_enumeration=1..22 lattice_cells=10200`; normalized variance values `1.53649587, 1.54349717, 1.54829927, 1.55162124` at \(n=200,400,800,1600\), approaching \(2\sqrt6/\pipprox1.5593936025\); `VERIFY_OK exact_arithmetic=yes independent_partition_enumeration=yes`.

Proof inputs not established by computation: the full Hardy–Ramanujan and distinct-part partition asymptotics, the analytic uniform expansion, the global tail bound, and the infinite local/weak limit. They are justified in `RESULT.md`; a finite output is not an independent proof.
