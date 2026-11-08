---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The planted-subtree two-temporal-state partition function factorizes as H_k(p,s)=A_k(p0,s1)A_k(p1,s0), where A_k equal/different weights satisfy u_{k+1}=u_k(u_k+2v_k), v_{k+1}=u_k². At root degree two, tie retention gives 2u_h² two-step states with fixed root, 2v_h² with flipping root; stationary state count from same one-time recurrence is 2u_h, so Q=2(u²+v²), N=(Q-F)/2=u²+v²-u. r_h=u_h/v_h follows r_{h+1}=1+2/r_h, tends to2, giving 1/(r²+1)=1/5 root flip in primitive two-cycles. The entropy series comes from u_{h+1}=u_h²r_{h+1}, with bounded logs and 2^-j summability. Independently exhaustive synchronous evolution for all states at h=1,2,3 (32904 states) confirmed exact F,Q,N and root flips; recurrence h=4 checked and rho series approximated. Finite checks do not establish arbitrary height; two-layer induction does.

## originality

PASS

After direct mathematical implication comparisons, no inspected prior theorem gives the entire final claim; positive classification is best-of-knowledge, not an absolute historical priority certificate. For synchronous binary neighbor-majority on perfect rooted binary trees with root ties retained, exact recursion counts all fixed and mixed/pure period-two configurations, root-flipping fraction tends to 1/5, and the orbit count has growth constant about 1.53717671718234 per vertex.

## value

PASS

A complete transfer-recursion census including mixed two-cycles, new local root-flip 1/5 limit, and exact periodic-orbit entropy on a natural self-similar family addresses a meaningful dynamical invariant beyond known fixed-point or pure-cycle counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
