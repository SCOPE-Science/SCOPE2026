---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Proved F^3=F on undirected loopless graphs from antitonicity and x<=F²(x). For odd n, j->2j permutes sites and z_j=1-x_(2j-1) converts each output constraint to adjacent AND y’_j=z_j z_(j+1). A zero output counts independent cyclic sets Lucas_n; output all ones has one precursor; a single zero between ones is impossible; longer cyclic zero runs of length L have F_(L-1) internal independent-set assignments, which factor across runs. For nonconstant output, product <=F_(n-2); each nontrivial attractor union has at most 2F_(n-2)<Lucas_n+1 precursors. Independently exhausted every input/output for odd n=3..15 (n=15 has 32768 states), verifying all 2^n fiber equations. Infinite theorem rests on combinatorial run reduction, not only finite states.

## originality

PASS

Jen (1988/1989) and Fukś developed periodic CA attractor and preimage transfer methods and Rule-5 update dynamics is known; previous square-conjugate open-NOR findings on bipartite graphs and paths have individual path fibers but do not imply odd-cycle cyclic run counts or unique Lucas-basin ranking. Best-of-knowledge the explicit odd-ring all-fiber evaluation survives.

## value

PASS

The exact predecessor distribution and unique dominant attraction basin on a canonical elementary cellular automaton answers a natural finite-dynamical-systems question at every odd ring size, including sharp exponential basin probability, not a mere generic time-two recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
