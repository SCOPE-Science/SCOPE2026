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

For homogeneous absorbing unit-rate N-state pure-birth Q, E_N(h)=2(I−hQ/2)^−2−(I−hQ)^−1 is a rational matrix function of the nilpotent transient shift S; row sums are one. Scalar r(z)=2/(1+z/2)^2−1/(1+z)=(−z²+4z+4)/((z+1)(z+2)^2), and transient superdiagonals a_k=(−h)^k r^(k)(h)/k!. For N≤5, a0≥0 exactly 0≤h≤2+2sqrt2=U, while a1,a2,a3>0 for 0<h≤U via the explicit one-positive-root polynomials and their negative values at U. Absorbing entry in first row for N=5 equals h^4 p(h)/((h+1)^4(h+2)^5), p=h^5+18h^4+52h³+48h²+2h−12, unique positive zero η in (.3959,.3960); for N2,3,4 corresponding absorbing entries are positive for all h>0 until diagonal barrier U. Thus re-entry N5 at {0}∪[η,U]; h>U fails by diagonal. Independently assembled rational resolvent matrices at h=0,1/4,1,4,5 for N2..5 and symbolically factored N5 absorbing term; exact h=1/4 negative absorbing entry −7799/36905625. Finite checks corroborate all-h sign proof.

## originality

PASS

Best-of-knowledge PASS for the complete N2–5 Richardson-backward-Euler stochasticity windows and first N5 re-entrant interval. The general extrapolation method, SSP conditions and scalar positivity cutoff U are prior work. Published Resultary entry “Richardson acceleration creates a sharp positivity barrier for backward Euler” explicitly gives the scalar U but does not mention the nilpotent N5 absorbing-column obstruction or η polynomial. The [2/2] Padé eight-state barrier uses a different rational stability map, and no result mechanically implies the target sign polynomial. Fornberg–Zuev–Lee investigate extrapolation and stability for Maxwell wave equations, not Markov transition positivity. Residual older SSP derivative-coefficient literature acknowledged.

## value

PASS

Exact sharp Markov-positivity classification for a canonical numerical acceleration scheme on natural absorbing birth chains and a nonmonotone small-step pathology: shrinking the timestep can lose positivity, then increasing it restores positivity for a finite interval. Five states is the first state dimension for this homogeneous hierarchy; N4 scalar bound alone does not predict the re-entry. This is a meaningful method-specific boundary, not an arbitrary negative-entry test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
