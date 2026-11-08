---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS: For F_i=H(r x_i(1-x_i-gamma x_(i+1))), 1<r<3 and gamma>1, a positive fixed coordinate lies strictly between 0 and 1 and satisfies x_i+gamma x_(i+1)=h=1-1/r. If a zero exists, a positive block's last element before it equals h; an adjacent earlier positive element would be h-gamma h<0, impossible. Thus all nonzero boundary points are h times independent sets of C_n, whose number is classical Lucas L_n; all-positive recurrence y_i=-gamma y_(i+1) forces the unique p=h/(1+gamma). Every noncheckerboard independent set has adjacent zeros, allowing a one-coordinate positive logistic perturbation with its successor pinned at zero; eventual deviation to h/2 proves Lyapunov instability. Even checkerboards have relative-cube triangular linearization with active multiplier 2-r and vacant one-sided multiplier max(0,r(1-gamma h)), both <1 in modulus, so they attract locally exponentially. At p the Jacobian is I-t(I+gamma S); all Fourier multipliers 1-t(1+gamma exp(2pi ik/n)). The strict Schur inequalities minimize at the least cyclic cosine, -1 for even n (unstable) or -cos(pi/n) for odd n. Solving gives the exact gamma and r thresholds and neutral conjugate pair at upper-r equality; sec(pi/n)-1~pi²/(2n²) follows by Taylor. Independent n=3..24 Lucas counts and five Fourier samples corroborated analytic proof; no global-basin conclusions.

## originality

PASS

Best-of-knowledge originality after comparing exact statements and implications; four structured comparisons and source-inspection limits are included.

## value

PASS

PASS: Strong inhibition selects a natural exactly solvable family whose complete nonlinear fixed-point structure is a Lucas independent-set census, sharply contrasting exponential proliferation of equilibria with at most two attracting fixed points. The parity-specific positive equilibrium Schur window quantifies an O(n^-2) frustration effect. This is a full motivated fixed-point and local-stability classification with explicit structural proof, not merely the textbook Lucas identity or the generic Fourier test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
