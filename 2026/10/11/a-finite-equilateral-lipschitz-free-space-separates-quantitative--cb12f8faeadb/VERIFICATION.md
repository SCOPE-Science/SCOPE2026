---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed RESULT.md directly from the frozen SHA. For six equilateral sites, KR/Arens–Eells norm is half the l1 norm on total-mass-zero vectors and the unit ball is conv of all 30 oriented e_u-e_v molecules. The proposed x has zero sum and norm 1. A unit molecule m_uv has distance 2-(x_u)^+-(-x_v)^+, because every coordinate of x has magnitude <=1; independent enumeration of all 30 distances found unique nearest m_{a0,b0} at 3/4. Each nonempty polytope slice contains a maximizing vertex, proving dc>=3/4; the vertex m_{a0,b0} is uniquely exposed by potential +1 at a0, -1 at b0, 0 elsewhere (separating score 2 vs at most 1) so arbitrarily thin slices give dc<=3/4. The functional summing a-side coordinates is 1 at x and <=1 on every molecule, forcing any convex molecular representation to use cross-part molecules only. Thus its nonnegative 3x3 coefficient matrix has row marginals (1/2,1/4,1/4) and columns (3/4,1/8,1/8), whence lambda_00>=1/2+3/4-1=1/4 and the molecule-only maximum admissible radius is exactly 3/4. Independently reimplemented all 12 orbit witnesses A,B,C using exact Fraction arithmetic: each has norm 1 and distance 7/8 from x, and weights 2/11, 4/11, 5/11 on four-entry orbit means give barycenter x. The strict affine slice inequality guarantees that a slice containing x contains at least one 7/8 witness, proving Delta c(x)>=7/8. Finite checks establish precisely the finite rational identities; the all-slice conclusion follows analytically. No exact Delta constant, minimality, or classification is asserted.

## originality

PASS

Best-of-knowledge PASS for the concrete intermediate-radius obstruction in a real six-point equilateral Lipschitz-free/root-polytope space: a distinguished nonvertex x is in the convex hull of points 7/8 away but cannot be represented using only molecules strictly farther than 3/4. The general Choi–Jung Proposition 2.3 supplies the arbitrary-ball convex-hull criterion, and Theorem 3.12 supplies the Daugavet/denting criterion, but not the forced transportation-edge and 12-witness strict gap. Abrahamsen et al. Theorem 6.9 is an endpoint (Delta=2) representation theorem; Aliaga–Pernecká–Smith Corollary 3.7 gives molecular decompositions without a distance threshold. Targeted Resultary searches include the audited record itself (not independent prior coverage) and mathematically distinct finite equilateral/free-space invariants. No established broader theorem or table found which computes or implies the specific 7/8 versus 3/4 obstruction. This is not an exhaustive historical-priority certification.

## value

PASS

The natural six-point equilateral metric produces the type-A root-polytope Lipschitz-free ball, a standard finite benchmark. The motivating mathematical issue is whether the general quantitative Delta convex-hull witness can be restricted to distant molecules, as qualitative endpoint Delta-molecule theorems might suggest. The explicit transportation marginal forces a molecule below the chosen radius into every convex molecular representation, yet distant nonvertex witnesses represent x. This is a genuinely motivated finite counterexample establishing a strict 1/8 boundary at an intermediate quantitative Delta radius, not a mere computation of an arbitrary small coefficient: it sharply obstructs a plausible molecular criterion. Its value is the structural failure and exact obstruction, despite lack of a general theorem, minimum-size claim, or exact Delta constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
