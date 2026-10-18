---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the prescribed continuous-time reversible generator, stationary-mass-weighted Poisson equations telescope and give H_{i,i+1}=P_i/w_i and H_{i+1,i}=(1-P_i)/w_i. Strong Markov additivity makes the maximal ordered-pair hitting expectation the maximum of the two endpoint directional sums. For each lambda in [0,1], a weighted average and Cauchy-Schwarz yield lower bound S(lambda)^2 and force w_i(lambda)=sqrt(a_i(lambda)/c_i)/S(lambda) at equality. S is strictly concave for n>=3 because not all partial masses P_i equal 1/2; its derivative G/2 is strictly decreasing. At the maximizing scalar lambda*, F-B=S G with correct boundary signs, so the sharp Cauchy bound equals the max objective and the equality allocation is uniquely optimal. Reflection/price cancellation at lambda=1/2 and the symmetric three-state threshold 1/3<=c1/c2<=3 follow by direct substitution. The inspected verify.py independently solves rational Poisson systems in finite cases but is not the proof. All domain restrictions (positive pi,c,w, normalized total mass and cost, no discrete-time rate caps) are needed.

## originality

PASS

Classical first-passage and electrical results concern a given chain. Ghosh-Boyd-Saberi minimize summed or maximum undirected effective resistance and different variables/objectives; such symmetric resistance optimization does not imply separately directed worst hitting time with externally prescribed stationary masses and nonuniform prices. Full-text source comparisons and Resultary queries found no dominating all-parameter allocation theorem. Palacios-Tetali 1996 remains plausible inaccessible fixed-chain source; authorized download returned vpn_disconnected, so originality is qualified, not failed automatically.

## value

PASS

A prescribed-stationary reversible path with priced conductances is a natural robust hitting-latency design problem. The proof gives exact optimum for every path length and positive mass/price vector via one monotone scalar balance, including surprising mass-independent allocation and exact three-state price regime breakpoints; this is a complete optimization decision, not merely an evaluated known formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
