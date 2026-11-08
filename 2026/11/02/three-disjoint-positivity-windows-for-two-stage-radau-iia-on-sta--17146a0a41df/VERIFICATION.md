---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS: Spectral projectors for L(K1,m) at eigenvalues 0,1,m+1 yield four rational entry forms. Offdiagonals equal h[(m+1)h+6]/Db and h²[(m+1)h²+(6m+12)h+18]/(Da Db), so positive for all h>0. The only obstructions are hub quadratic H_m and leaf quartic F_m. Exact minimum R(x)>-(3 sqrt 3-5)/2 and delta<1/10 establish diagonal positivity for 2<=m<=10. For m>=11 hub discriminant 4(m²-10m-2) gives two roots below 2; F_m positive on [0,3], negative at 8, eventually positive, while Descartes allows at most two positive roots: exactly two simple leaf crossings >3. The two disjoint bad intervals yield three closed safe windows. Independent SymPy identities, rational isolations at m=10,11,12,20,100 and exact large-m asymptotic coefficient checks support, but do not prove, the all-m result.

## originality

PASS

PASS: Best-of-knowledge supported by direct statement/implication comparisons, not claimed absolute priority. A method-level radius does not determine the exact sequence of diagonal sign changes for this star, so these are not equivalent results. No inspected general theorem implies the two disjoint negative intervals in a uniform star for the exact [1/2] Radau map; similar positivity loss/recovery alone is weaker. The prior facts provide a setting for positivity loss, but cannot substitute for exact hub and leaf sign polynomials. A specialized, not yet indexed star result could still be prior.

## value

PASS

PASS: The nonmonotone endpoint-positivity region of a standard stiff integrator is a meaningful obstruction for graph diffusion and positivity-preserving timesteps. Two distinct diagonal obstructions produce a sharp smallest graph (12 states) and three disconnected feasible windows, including a finite [2,3] central window and a late O(m) recovery. This cannot be read off graph-independent absolute-monotonicity radii.

The dated certificate retains the supplied scientific assessment, sources and limitations.
