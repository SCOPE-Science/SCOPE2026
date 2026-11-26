---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Allaart's p_n^* is the frozen p_n and the strict inequality p_n<1/2 holds on the claimed range. At drawdown 0 or 1 the stop reward with k steps left is U_k=P_p(T_2>k); above drawdown 1 it is zero. For downward drift delta=q-p>0 put rho=p/q and nu=1-rho^2. First-hit paths to 2 have likelihood ratio rho^2 under drift reversal and hit almost surely under the up-drifting law, proving U_L-nu=rho^2 P_q(T_2>L). With at least L steps left a winning stop has conditional reward at most U_L; starting from drawdown 2, it additionally needs ever to reach displacement +1, of probability rho. In the last L times a winning stop from i needs displacement at least i-1, so the separate union bounds cover every adapted rule. Hoeffding applies since delta*m>=1 for all these m and for L; T_2>L under the up-drifting law implies S_L<=1. The continuation bound then uses p+q*rho=2p and nu(1-2p)=delta^2/q^2. At delta=sqrt(6 log(n)/n), n>=32 implies 0<delta<1 and delta*floor(n/3)>1. Using L>=n/3-1 and n-L>=2n/3 gives total error <=(exp(3/2)+exp(1)/3)/n<6/n, below delta^2/q^2. Thus U_n>W_n at the test probability; the exact threshold gives the claimed inequality and limsup. No convergence or rate is inferred from the finite checker.

## originality

PASS

The effective bound is distinct from the known qualitative convergence and finite inequalities. It is not claimed to be sharp or the exact critical window.

## value

PASS

This puts a finite sufficient stopping window and an explicit near-critical rate on the exact threshold sequence whose recently proved convergence came without a rate. The constants apply from a stated horizon, not only eventually.

The dated certificate retains the supplied scientific assessment, sources and limitations.
