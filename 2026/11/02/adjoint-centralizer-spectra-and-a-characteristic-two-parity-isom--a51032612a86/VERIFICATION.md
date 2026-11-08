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

A derivation of k[t]/t^N has form D_f=f(t)d/dt with f∈t^ℓk[t]/t^N, ℓ=0 when p|N and ℓ=1 otherwise, because 0=D(t^N)=N t^{N−1}f. For nonzero f=t^v u with u unit and g=u h, [D_f,D_g] corresponds exactly to u²t^(v−1)(t h'−v h), and each distinct j coefficient (j−v)h_j lives at degree j+v−1, so the centralizer basis and c_N(v) follow even at v=j=0 with zero coefficient. Number of f at valuation v is (q−1)q^(N−v−1). Summing q^c yields the complete nullity polynomial and commuting-pair count; for N=kp the residue decomposition v=ap+b produces the closed S_p(q). In char2, bases A_j=D_{t^{2j}},B_j=D_{t^{2j+1}} for N=2r and A'_j=D_{t^{2j+2}},B'_j=D_{t^{2j+1}} for N=2r+1 obey the same [B_i,A_j]=A_{i+j} truncated bracket, giving both Lie isomorphisms with the affine algebra of k[z]/z^r. Image of ad_(a,b) is ideal (a,b) and has rank r−min(v(a),v(b)); this independently yields the full common spectrum and exact pair count. Direct finite field adjoint matrix rank enumeration for primes p=2,3,5, truncations N=2..7 matches the c_N(v) and p|N pair count, corroborating the universal proof.

## originality

PASS

The one-variable N=p Witt algebra centralizer partly appears in Yao–Chang (p>3), and regular derivations of p-truncated multivariate algebras in Premet are established. The claimed all-N finite-field full spectrum and especially characteristic-two consecutive-length explicit Lie isomorphism are separate; no inspected stronger source dominates those statements, though classic modular Lie textbooks are a plausible priority risk.

## value

PASS

Adjoint-centralizer dimension distributions and commuting-pair probabilities are natural finite Lie-algebra invariants. A complete all-length formula together with a characteristic-two parity isomorphism explains a non-obvious structural equality between derivation algebras of different associative rings. It also isolates the known Witt special case rather than recomputing it as the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
