---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed rank-one N=r ell^T with ell^T r=0 and NA^kN=k gamma N. The explicit absolutely convergent eigen-energy V_p(x)=sum_{k>=0}q^k lambda^{-(k+1)}|ell^T A^k x|^p is continuous, p-homogeneous, strictly positive for x!=0 because ell^T and ell^T D are independent when gamma!=0. The defining F_p(lambda)=1 gives exact qV_p(Ax)+(1-q)V_p(Nx)=lambda V_p(x); compactness on unit circle bounds it above/below by Euclidean norm^p, proving all times and initial states, not just renewal times. Two consecutive N steps cause finite absorption a.s. For canonical A=[[2,-1],[1,0]], N=[[0,0],[1,0]], gamma=-1, independent exact multiplication verifies q=1/3 invariant Q=[[6,-3],[-3,2]] positive definite, q1=1/2, q2=1/3 and q=.4 rates 0.889897948557 and 1.113507624413. Geometric K_q stochastic ordering yields unique q_p for all p>0; strict decrease with p is only asserted for |gamma|=1 example.

## originality

PASS

Existing broad packet-loss/delay control theorems cover mean-square and Riccati/input-output stability criteria. The inspected technical statements do not furnish the exact all-real-order moment equation and norm-comparable nonlinear eigenenergy of this nilpotent-unipotent family. The second-moment example could be derivable from general moment theory; only complete all-p explicit classification claimed distinctly. Closest predictor-controller paper is not fully inspected, risk noted.

## value

PASS

The result reveals a meaningful strong/nonuniform stability gap in an elementary packet-loss control family: every trajectory is killed a.s. but high moments can diverge exponentially, with a continuum of exactly characterized thresholds. Its explicit positive p-homogeneous eigenfunction for noninteger p is structurally useful beyond textbook first/second-moment matrix calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
