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

The standard marked-cluster generating function F_w(z,y)=C_w(z,y)/[(1-z(q-1+y))C_w(z,y)+z^m y^{h_w}] is a formal series with invertible denominator. Setting y=1 gives H_w-H_v=z^m(C0_w-C0_v)/(D_w D_v), so equality of all N(n), 0<=n<=2m-1, makes the degree<=m-1 polynomial C0_w-C0_v identically zero. Differentiating the reciprocal at y=1 then makes J_w-J_v proportional to z^m[(h_w-h_v)C0-(C1_w-C1_v)]/C0²; the same coefficient window forces this polynomial zero, its constant gives h_w=h_v and all marked overlap derivatives C1 agree. At each overlapping d, C0 stores the existence indicator and C1 the exact marked-letter suffix count, hence complete weighted border polynomials match, giving every histogram A_w(n,k). The binary witness w_m=0110^(m-3), v_m=10^(m-2)1 for m>=4 has C0=1+z^(m-1), equal h=2, and first J difference coefficient at 2m-1, proving cutoff sharp. Independently enumerated all binary words for m=4, n<=7: w=0110, v=1001, N7=97 each, M7=340 and339; grouped all forbidden words m<=4 against finite jets and complete checked histograms. Two forbidden-set witness {00,11} vs {01,10} has same N,M all n but different spectra at n=2. Finite enumeration corroborates the formal proof only.

## originality

PASS

Bóna–Maga–Richey Fact 2.9 supplies the marked cluster rational function and Corollary 2.11 the forward border-to-spectrum implication. The assessed addition is the inverse finite first-moment coefficient criterion, optimal cutoff and multi-forbidden boundary. No claim that the cluster formula itself is new.

## value

PASS

The exact finite identification threshold converts limited observed avoidance counts and a first marked-letter moment into the complete infinite marked spectrum; its sharpness and failure for two forbidden words show a genuine structural rigidity boundary for symbolic dynamics and combinatorics on words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
