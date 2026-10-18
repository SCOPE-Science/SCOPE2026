---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For SPD B, nonzero s, y=Bs and guarded Case I of Li et al s^Ty>=xi||y||², the quadratic descent form of -g^Td reduces in span{s,Bs} to Q=[[1/b,-||h||/(2b)],[-||h||/(2b),1]], with e=s/||s||, b=e^TBe>0, h=(I-ee^T)Be and guard b>=xi(b²+||h||²). Positivity of Q-(1-1/(4xi))I from principal minors proves universal lower bound; SPD B_b with b->0 attains sharp limit. For xi=1/4 each fixed guarded pair strictly descends but no positive uniform coefficient; xi<1/4 yields negative eigenvalue. Fully rational reachable example A=[[99/100,3],[3,999/100]] SPD, initial g0=(-1,-300/251), accepted alpha0=2/25 and projection s0=(2/25,0), guard xi=1/100 margin 18/3125, next direction has g1^T d1=86467011299/98439062500>0, making monotone-affine line-search rejection for all positive steps. Independent exact fractions verify this witness; no claim about Cases II/III or all algorithm runs.

## originality

PASS

Original Li et al 2026 paper specifies identical Case-I direction, guard and claimed sufficient-descent lemma for all positive xi, but its proof neglects how s/y secant cross terms can defeat descent. The exact minimax coefficient, sharp xi=1/4 threshold and reachable projected affine counterexample contradict that stronger original claim below threshold. Prior 2025 Tang et al subspace CG has different direction, so cannot supply same exact source-specific bound. Relevant Resultary numerical algorithm counterexamples are to different methods.

## value

PASS

The theorem establishes a mathematically sharp missing hypothesis in a published convergence argument, supplies explicit strong-monotonicity reachable ascent trajectory, and identifies a repairable safeguard threshold for the specific branch; this is substantive theorem validation, not a cheap type check or isolated numerical observation. It explicitly does not establish full algorithm global convergence when xi>1/4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
