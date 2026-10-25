---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The frozen RESULT.md fixes the normal fan of S_n in the integral off-diagonal lattice Z^{n choose 2}, not the Ehrhart ring. Every active coordinate facet yields an e_ij row and each zero diagonal a negative star row. Eliminating unit rows reduces the toric divisor exact sequence to unsigned incidence blocks: singleton none, paired component 2x1 with free cokernel Z, odd support cycle with Smith invariant 2. Thus Cl(U_v)=Z^{t(v)}+(Z/2)^{c(v)}, Q-factorial iff t=0, smooth iff t=c=0 (identity). Solving canonical all-ones ray equations sets off-support m_ij=1, pair edges =-(n-1), odd cycle edges =-(n-2)/2; local index 2 iff n odd and c>0 and 1 otherwise, Q-Gorenstein always. Exponential formula counts singleton/pair/odd undirected cycles and gives exp(z+uz²/2+(q/2)sum_{j>=1}z^{2j+1}/(2j+1)). Independently calculated support count 5,14,58,238 at n3..6; inspected actual SymPy Smith-normal-form checker, including BFS vertex confirmation n3,4. Arbitrary-characteristic assertion concerns lattices, not quotient group-scheme étaleness.

## originality

PASS

Katz and Brualdi–Cao already classify extreme support components, and Davis already proves even-n Gorenstein phenomena for associated Ehrhart rings. These are credited, not asserted new. The current claim instead supplies each normal-fan affine chart class group, Cartier index, exact local smoothness/Q-factorial boundaries, and bivariate distribution. Direct inspection of the two accessible primary papers found neither the per-chart class group formula nor its joint generating function. Full Katz 1970 text inaccessible; legacy equivalent localization remains a risk.

## value

PASS

Local Weil divisor groups and Gorenstein/Cartier indices control singularity and divisor theory of a natural infinite toric family. The pair/odd-cycle Smith decomposition and parity transition are complete structural invariants, not merely known vertex enumeration; the bivariate enumerator makes singularity types quantitatively accessible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
