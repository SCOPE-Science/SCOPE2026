---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For X>=6epsilon, g(z)=cos z-cos X-epsilon(X+z) is strictly decreasing; g(X)<0 and g(0)>0 by 1-cos X>=2X²/pi², ensuring a unique next root z in (0,X). Let Delta=X-z and m=(X+z)/2. Energy identity integral_z^X sin t dt=2epsilon m, whereas F(X)-F(z) with F prime=sin t/(2t) differs from epsilon by a symmetric Taylor defect whose linear term integrates to zero; the smooth kernel sin t/(2t) extends with bounded derivatives to zero and yields |e|<=C Delta³. Uniform Delta²<=C epsilon, all Delta disjoint and sum Delta<=pi, so total defect <=C epsilon. For small X<=pi/2, Delta<=pi epsilon and X>=6epsilon imply Delta<=m, so no singularity is introduced. The terminal F(X_K)<3epsilon. Telescoping gives D=K epsilon+O(epsilon) and therefore a bounded absolute error. Independent high-precision evaluation of D=0.9259685259912329 and six recursively solved parameter values epsilon=.02,...,.0005 produced K=44,90,183,460,923,1849 with bounded K-D/epsilon about -2.30 to -2.98; this diagnostic is not the proof.

## originality

PASS

PASS, qualified: Ovseevich arXiv:1311.5729 explicitly derives the same recurrence (2.16) and its leading limit epsilon N_epsilon(u)->D, so no novelty is attributed to the recurrence, control choice or leading constant. The source theorem and surrounding exact equation do not state a uniform O(1) error for this stop convention; the symmetric defect summation is a genuinely stronger quantitative statement. Full Reshmin 2009 text was unavailable and quantitative pendulum estimates could exist elsewhere.

## value

PASS

A bounded absolute correction to an existing epsilon^{-1} switching count is a meaningful finite-parameter improvement for an explicitly controlled nonlinear dissipation map, rather than simply a reparameterization of the leading asymptotic. It quantifies the accumulation of local quadrature defects and separates half-swing counts from the unproved globally optimal policy count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
