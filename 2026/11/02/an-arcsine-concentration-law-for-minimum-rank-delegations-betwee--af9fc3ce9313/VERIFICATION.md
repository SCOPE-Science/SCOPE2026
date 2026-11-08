---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

In the two-terminal path with independent fair rankings, an interior directed left/right edge selection has no directed 2-cycle iff it consists of L^kR^{n-k}, so all feasible branchings are cuts k=0,...,n. For X_i=+1 if right preferred, cost of cut minus n is (#left-preferring voters)+S_k, S_k sum X_i, hence optimum is exactly the set of simple symmetric random-walk minima. Reflection counting splits an earliest minimum at k into a strictly-positive reversed prefix and a weakly nonnegative suffix, giving the stated exact product ballot probability including endpoints k=0,n. Donsker invariance and the almost-sure uniqueness of the Brownian minimum imply all profile-dependent optimal tie rules have the arcsine Beta(1/2,1/2) weak limit. The 3/4 representation event has limiting probability 2/3, whereas BFD splits almost evenly. Reflection for maximum of simple walk plus exact E|S_n| yields optimal expected second-choice cost n/2-n*2^(1-n)*C(n-1,floor((n-1)/2))+(1-p_n)/2 and asymptotic n/2-sqrt(2n/pi)+1/2+O(n^-1/2). Independent direct rank-profile enumeration n=1..10 matched both expectation and earliest-minimum probabilities; the limiting claim relies on standard functional CLT, not finite tests.

## originality

PASS

Brill, Delemazure, George, Lackner and Schmidt-Kraepelin (2022) introduced BordaBranching and documented the tradeoff between preferred ranks and voting-weight concentration, but their investigated instances/algorithms do not state a random independent-preference path law. Utke and Schmidt-Kraepelin (2023) analyze fixed-profile randomized mixed optimal branchings; a mixture across optimal branchings for a fixed ranking is different from iid random ranking preferences followed by any optimal tie-break. The reflection principle and Brownian arcsine distribution are classical; the substantive incremental result is the exact reduction of a delegation optimization to walk minima and hence an explicit sharp concentration-versus-cost tradeoff for an important mechanism. An unlocated specialized random-path delegation paper could already make this reduction.

## value

PASS

Concentration of guru voting weights is a central problem in liquid democracy. The natural minimal two-guru path cleanly isolates global preference-rank optimization versus balanced shortest-path routing, with a nonvanishing 2/3 chance of a three-quarter guru while achieving only order sqrt(n) expected rank-cost savings. It is an interpretable sharp failure mode, with exact finite cost and tie-rule-invariant macroscopic limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
