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

The proof was replayed from the exact Euclidean proximal subproblem rather than inferred from numerical output. The critical identities checked are:

1. For \(f_\xi(x)=\tfrac a2(x-c\xi)^2\), the proximal minimizer is \(x^+=(x+\alpha a c\xi)/(1+\alpha a)\).
2. With \(t=\alpha a\) and \(r=(1+t)^{-1}\), this is \(x^+=rx+(1-r)c\xi\).
3. The stationary second moment from the geometric series is \(c^2(1-r)/(1+r)=c^2t/(2+t)\), and the stationary objective gap is one half of \(a\) times this quantity.
4. The two first-level support images are \([-c,c(2r-1)]\) and \([c(1-2r),c]\), so their separation, touching, and overlap occur exactly for \(r<1/2\), \(r=1/2\), and \(r>1/2\), equivalently \(\alpha a>1\), \(\alpha a=1\), and \(0<\alpha a<1\).
5. At \(r=1/2\), the stationary random series is the centered fair binary expansion and hence uniform on \([-c,c]\).

`verify_stationary_law.py` checks the closed-form identities at several parameter values and includes a seeded Monte Carlo replay as a non-probative sanity check. The stored run in `verification_output.txt` reports `VERIFY_OK`.

The infinite-time law, uniqueness, and support statements are proved analytically; the finite simulation does not certify them. No claim is made about density or singularity of the stationary measure in the overlapping regime \(r>1/2\).
