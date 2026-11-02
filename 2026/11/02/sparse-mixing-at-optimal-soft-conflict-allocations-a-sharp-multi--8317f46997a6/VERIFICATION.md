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
# Reproducibility and verification

From this directory, run `python3 verify.py` with Python 3.8 or newer; the program uses only the standard library and no external data. Its main check enumerates every nonnegative integer part-by-agent occupancy matrix satisfying the exact part sizes and equitable agent quotas for 864 multipartite instances with up to four graph parts, nine goods, and five agents. These are all structurally distinct allocations for the relevant conflict objective: relabeling vertices inside a part does not affect EF1 or the number of violated edges. There are 69,276 checked occupancy matrices. For each parameter tuple, the script finds the true finite minimum and checks that an optimum uses at most \(r-1\) mixed bundles. For complete bipartite instances with equal quotas, it independently checks the residue formula and that every optimum has exactly zero or one mixed bundle as appropriate. Additional assertions verify the sharpness family through nine parts and the odd bipartite specialization for agent counts up to 49.

The source contains the entire finite procedure. The expected terminal line begins with `PASS 864 complete types/agent cases; 69276 occupancy matrices`. The code is a finite stress test, not a substitute for the universal proof. In particular, no assertion about arbitrary large multipartite graphs rests on extrapolating the tested cases. No independent audit or external certification has occurred.
