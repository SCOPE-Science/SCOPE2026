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

## Exact analytic checks
The forced inverse probability-generating polynomial is
\[
Q_\tau(z)=\mathbb E[1-W/\tau+(W/\tau)z]^n.
\]
The coefficient at \(n-1\) is
\[
q_{n-1}(\tau)=n\tau^{-n}(\tau\mathbb E W^{n-1}-\mathbb E W^n),
\]
which proves the lower-bound obstruction independently of numerical tests. At \(\tau=r_n\), the terminating Gauss equation and coefficient comparison provide the descending recurrence (3) in `RESULT.md`. Its positivity and \(Q(1)=1\) prove existence. The proof includes all real \(a,b>0\) and every integer \(n\ge1\).

## Exact finite replay
Use `python3 verify.py`. The script has no third-party dependencies and checks 162 rational beta-shape/size combinations, comparing two algebraically independent parent-coefficient calculations with the original beta-binomial probabilities after ordinary thinning. It also checks a strictly smaller proposed retention rate gives a negative penultimate coefficient. The special concrete example is
\[
(a,b,n,r_n)=(2,3,4,5/8),\qquad
(q_0,q_1,q_2,q_3,q_4)=(471,704,1152,0,2048)/4375.
\]
Expected successful line:
`VERIFY_OK exact_cases=162 beta23_n4_threshold=5/8 hole=0 support=4`

Finite checks are demonstrations of the equations in selected parameter cases, not a proof of the universal real-parameter statement. That statement rests on the finite polynomial identity and strict coefficient induction.
