---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Each positive leaf (a_i=+1) strictly improves by joining the hub unless already present; each negative leaf (a_i=-1) strictly improves by leaving the hub if included. The hub coalition therefore consists precisely of the positive leaves, with utility U=sum_{a=+1}b_i. Remaining outsider blocks B of negative leaves are Nash-safe exactly when U>=0 and sum_{i∈B}b_i<=U; existence iff U>0 or (U=0 and R=sum_{a=-1}b_i<=0). The admissible outsider block exponential formula counts all such unlabeled partitions. In the independent correlated-sign model E[b 1_{a=+1}]=rho-1/2 and variance=1/2-(rho-1/2)^2; Hoeffding controls off-critical mistakes and a triangular CLT yields P_n(1/2+c/sqrt(n))->Phi(sqrt(2)c). At rho=1/2 sign reversal gives P=1/2+1/2 Pr(U=R=0), with parity and Vandermonde giving exact even correction 1/2*binom(n,n/2)^2/4^n. Independent enumeration of all 4^n signed profiles and original Nash inequalities over unlabeled partitions for n=1..4 confirmed existence criterion and exact critical counts 2/4,10/16,32/64,146/256. Proof valid for all n>=1 (not relying on exhaustive small cases).

## originality

PASS

Best-of-knowledge priority comparison on the exact final statement, allowing explicit inaccessible-primary-source risks; known related first-moment, connectivity, single-class and one/two-factor theorems are acknowledged as prior, not claimed new.

## value

PASS

Complete existence and equilibrium-count spectrum for an economically meaningful, sparse signed star with strict unilateral deviations, together with a sharp reciprocity/noise threshold and Gaussian critical window including exact finite-n parity. Provides a solvable baseline beyond either generic hardness or symmetric-valuation existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
