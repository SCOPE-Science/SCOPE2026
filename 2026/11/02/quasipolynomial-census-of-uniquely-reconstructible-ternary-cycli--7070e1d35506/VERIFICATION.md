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

A matrix is realizable exactly when its positive-degree directed support is Eulerian and connected. BEST with indistinguishable parallel ordered transitions gives W(K)=n τ prod_i(d_i-1)! /prod_ij K_ij!, so Q(K)=W(K)/n is a lower bound on rotation classes and is exactly one class when Q=1 and gcd of edge multiplicities is one; repeated simple directed cycles with Q<1 are handled explicitly. Three-symbol circulation is uniquely expressible via t plus reciprocal counts a,b,c, loops at each vertex, and opposite orientation. The arborescence τ=ab+ac+bc+t(a+b+c)+t² yields loop multiplication by prod binom(l_i+s_i-1,s_i-1). Exhaustive nonloop cases and monotonicity under increments of reciprocal pairs reduce all eligible singleton profiles to the disjoint families in RESULT.md. Independently symbolically expanding the critical monotonicity ratio after nonnegative-variable substitution produces 55 nonnegative monomials in the t>=1 two-reciprocal case and 17 in the t=0 two-reciprocal case; thus the all-size inequalities do not rely only on sample data. Direct indexed ternary word enumeration with necklace rotation quotient independently reproduced U1..U12 = 3,6,11,24,45,64,93,114,139,168,201,226, agreeing with the period-six quasipolynomial.

## originality

PASS

Jacquet–Knessl–Szpankowski determine counts/asymptotics of all balanced ternary Markov types and cite Whittle type-class counting, but uniqueness among rotation classes is a sharply different restricted property. Grisales et al count loopless edge-distinguished unique Eulerian-tour digraphs as vertex number changes; Obscura Acosta–Tomescu provide a general edge-distinguished Euler circuit uniqueness/safety criterion, not the count of 3-labeled profiles with loops and identical parallel transitions. The exact singleton-profile quasipolynomial and classification are not contained in the inspected primary theorems.

## value

PASS

Cyclic Markov counts are natural sufficient statistics for circular symbolic data. Knowing which matrices uniquely reconstruct the word up to rotation is a meaningful identifiability invariant. The complete finite-alphabet support classification and explicit all-length degree-two period-six count distinguish this property from the much larger set of all Markov types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
