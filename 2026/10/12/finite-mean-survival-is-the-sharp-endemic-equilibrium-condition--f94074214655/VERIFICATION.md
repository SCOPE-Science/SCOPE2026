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

# Verification and limits

The theorem is checked at the level of exact stationary transport and infinite-age integrability, as detailed in `RESULT.md`. Reproduction steps:

1. Derive \(S'(a)=-s(a)S(a)\) and integrate to obtain \(\sigma=1-S(\infty)\).
2. Substitute \(i_*=J_*S\), \(A_*=cV_*/p\), and \(L_*=rA_*/(\eta+\mu)\) into every equilibrium equation; obtain \(\mathcal R_0\) and unique positive coordinates.
3. Check integrability on the infinite interval, not on a truncated age grid: \(\|i_*\|_1=J_*\int_0^\infty S(a)\,da\).
4. For source-admissible \(s(a)=(\log2)e^{-a}\), \(S(\infty)=1/2\) and no positive formal profile is in \(L^1\). For \(s(a)=k/(1+a)\), evaluate the improper integral exactly and find the \(k=1\) cutoff.
5. Integrate the characteristic formula to get the convolution for total age mass. The limit when \(J(t)\to j>0\) follows from a fixed-early-time/late-time split; it is conditional and not a claim that incidence must converge.
6. Run `python3 verify.py` with Python 3 standard library to check algebraic source-parameter examples and exact closed-form identities. Expected output: `VERIFY_OK`.

The Python check is finite and algebraic, not a computer proof of convergence over an infinite age interval. No global stability, persistence or generic incidence limit is established. No external audit or independent validation is asserted.
