---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every integer r>=29, t>0, the cut projection Q_t=W^(1/2) D^T(DWD^T)^+ DW^(1/2) is the Euclidean orthogonal projector on edge coordinates; cycle P=I-Q. The uniform kernel is Q_0[(i,j),(a,b)]=[i=a]/r+[j=b]/r-1/r^2, with exceptional column h=(2r-1)/r^2, sum other absolute values S=3(r-1)^2/r^2. Sherman–Morrison on mean-zero vertex subspace gives exact Q_t entries and denominator H=1+(t-1)h>0. Exceptional column norms equal c_Q=(t+3k sqrt(t))/(t+k), c_P=(k+3k sqrt(t))/(t+k) with k=(r-1)^2/(2r-1). Optimize 2x2 Rayleigh quotients: shared sharp maximum L=(1+sqrt(1+9k))/2, unique weights t_Q=((1+sqrt(1+9k))/3)^2 and t_P=((sqrt(1+9k)-1)/3)^2, product k^2. For every OTHER column and t>0, source triangle bounds give Q norm<5 and P<6, whereas L>6 for r>=29; this proves global rather than exceptional-only optimization and unique column. At t=1 the exact uniform norms are 3-4/r+2/r^2 and 4-8/r+4/r^2; L~(3/(2sqrt2))sqrt r+1/2. Independently calculated exact-rational grounded weighted Laplacian inverses for r=3,4,5,6 and four test t values; exceptional column formulas agreed. Bounds r>=29 are sufficient not optimal.

## originality

PASS

Symmetrized transfer impedance/cut projector is classical and rank-one conductance updates are standard, but the objective here is induced edge-coordinate l1 maximal absolute column sum after optimizing ONE edge weight on Krr. The closest weighted electrical-flow papers bound spectral norm of ENTRYWISE ABS matrix, a different norm and not sharp in this family; unweighted constant-norm biclique results do not imply unbounded sqrt(r) weighted amplification. No inspected equivalent maximum-column theorem or optimal-conductance statement was found. Priority is qualified by standard projector/electrical network literature.

## value

PASS

One-edge conductance variation in a dense Krr graph produces unexpectedly unbounded endpoint projection norms even though the uniform network norms stay bounded. The sharp order-sqrt(r) amplification, two exact distinct optimizing conductances and product duality are meaningful extremal statements about electrical cut/cycle decompositions; optimization over all columns is essential. The object and coordinate norm are explicit; no claim extends to arbitrary projections, multiple varying edges or minimal possible order r.

The dated certificate retains the supplied scientific assessment, sources and limitations.
