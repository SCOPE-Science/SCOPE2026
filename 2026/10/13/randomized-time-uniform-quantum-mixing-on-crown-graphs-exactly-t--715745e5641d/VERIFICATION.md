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

For Cr_n, A has bipartite blocks B=J_n-I_n. The orthogonal projection P=J/n diagonalizes B with eigenvalues n-1 and -1, giving explicit cos(tB),sin(tB) and four orbit probabilities p0..p3. Direct expansion gives the exact pointwise identity p1(t)+p3(t)=[2-2cos(nt)]/n^2<=4/n^2. Uniform expected mixing would force E[p1+p3]=1/n, impossible for n>=5 for every Borel probability distribution on nonnegative times. At n=3, exact probabilities at t=0, pi/3, 2pi/3, pi weighted by 1/12,1/2,1/6,1/4 yield each orbit 1/6. At n=4, at t=pi/4 all four equal 1/8. Thus the classification includes *arbitrary* observation distributions, not only Cesaro laws. Independent rational orbit computations and numerical inequality diagnostics reproduced all boundary cases; no infinite inference is drawn from finite sampling.

## originality

PASS

Baptista–Coutinho–Marques introduce general observation-time averaging and analyze several families including complete and complete bipartite graphs; no complete crown classification appears in the material read. Adamczak et al show the six-cycle lacks instantaneous and Cesaro average uniform mixing, which does not preclude the explicit four-atom arbitrary-time mixture. The n=4 hypercube instantaneous case is known and credited; the all-n impossibility and n=3 randomized construction are the assessed contribution.

## value

PASS

For the natural connected crown family obtained by deleting a perfect matching from K_n,n, this is a complete iff classification allowing arbitrary Borel observation-time distributions, a substantially broader averaging mechanism than Cesaro or instantaneous mixing. It gives an explicit nontrivial positive C6 four-atom law, credits the Q3 case, and proves a uniform obstruction for every n>=5 with a single exact orbit functional. This is a motivated all-size spectral classification, not a finite test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
