---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The numerical and analytic reconstruction agrees exactly with the assigned proof. Solving the printed equilibrium relation gives u0=3.880786577827112 and v0=8.836967740350953. Fresh differentiation gives f_u=-0.5291880158707808, f_v=-0.397557495697221, g_u=0.09330903285810652, and g_v=0.02033146852557073. The zero-mode trace is negative and determinant positive. With d1=0.01,d2=10, d2 f_u+d1 g_v=-5.291676844022552, so the modal trace stays negative and the modal determinant is positive for every nonnegative Laplacian mode. At k squared 0.83 the determinant is 4.48731831647893, not the plotted negative value.

## originality

PASS

Originality passes. The open primary PDF prints the reaction terms, reverses the labels g_u and g_v in the displayed Jacobian assignment, and presents Figure 3 as the unstable case for d1=0.01 and d2=10 with a negative determinant near k squared equal to 0.83. Direct differentiation of the printed equations gives a completely stable modal polynomial instead. Generic Turing theory is prior art but does not state this parameter-specific contradiction, and the bounded searches found no correction.

## value

PASS

Figure 3 is the source's showcased unstable double-Allee case and underpins its claimed diffusion-driven transition as prey diffusion changes. Showing that every linear spatial mode is stable for the printed equations removes that interpretation and separates possible finite-amplitude spatial structure from genuine Turing instability. This is a substantive correction of a central numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
