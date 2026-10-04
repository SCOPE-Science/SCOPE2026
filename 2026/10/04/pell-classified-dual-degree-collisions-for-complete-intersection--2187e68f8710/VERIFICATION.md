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

The proof has four independently checkable steps: \(\deg(C^\vee)=2\deg(C)+2g(C)-2\) from a general plane pencil and Riemann--Hurwitz; the adjunction identity \(2g(C_{d,e})-2=de(d+e-4)\); the exact equivalence
\[
2m^2=3n(n+1)\quad\Longleftrightarrow\quad (2n+1)^2-24(m/3)^2=1;
\]
and the standard Pell classification of positive solutions by powers of \(5+\sqrt{24}\).

The bundled checker uses exact integer arithmetic. It confirms the dual-degree equality for generated Pell solutions, verifies the induced recurrences, and independently scans all \(2\le m,n\le5000\). It finds exactly four collisions in that box: the trivial reversal \((m,n)=(3,2)\) and the three nontrivial pairs \((30,24)\), \((297,242)\), and \((2940,2400)\). The scan is a regression test and is not used to infer the infinite theorem.

No claim is made that equal dual degrees imply equal dual hypersurfaces. No claim is made about all pairs of complete-intersection bidegrees.
