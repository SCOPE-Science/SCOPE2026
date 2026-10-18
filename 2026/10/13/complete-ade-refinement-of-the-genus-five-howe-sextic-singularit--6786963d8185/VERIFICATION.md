---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

On the affine chart y=0 at a root xi of the quartic difference b=phi1-phi2, distinct branch loci force phi1(xi)=phi2(xi)≠0, so the quadratic coefficient in y is a unit and completed-square/Morse reduction gives V²+unit*b(xi+u)², the A_{2m-1} germ for root multiplicity m. At P∞ on chart Y=1, homogenization yields a unique quadratic s² with critical section s=O(r³) and residual −4r⁴+O(r⁶), so A3 in every stratum (allowed char is not 2). At Q∞ on chart X=1 when d1=0 the v² coefficient is -4 and transverse critical section v=0; D(1,s)=d2*s−d3*s²+d4*s³ yields A1, A3, A5 for leading order 1,2,3. These give I-1/II-1 3A1+A3, I-2/II-2/II-3 A1+2A3, and I-3/II-4 A3+A5, all delta=5 matching sextic genus defect. Independently checked leading coefficients, orders and all seven basket sums exactly using symbolic arithmetic. Formal coordinate reductions, not the finite symbolic check alone, prove the uniform assertion.

## originality

PASS

PASS best-of-knowledge: the exact originating primary paper Kudo Part II (arXiv:2401.00760) gives singularity coordinates and multiplicity two with seven parameter strata, but not the completed local normal forms or ADE types. Part I arXiv:2310.15993 discusses other tacnodes for a different sextic; its results do not determine this Part II analytic basket. A1/A3/A5 and local delta refinements require actual local expansion beyond multiplicity two. Targeted searches returned no equivalent seven-basket refinement; alternative unindexed local analytic classifications remain possible.

## value

PASS

PASS: Node versus tacnode/higher two-branch contact affects local delta, intersection theory and resolution of the natural explicit genus-five Howe plane sextic. The complete seven-row ADE classification corrects an easy misreading of four multiplicity-two points as four nodes, explains the fixed genus defect five, and resolves all singularity analytic types for precisely the published family. This is a motivated singularity refinement, not mere renaming of the published location/count table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
