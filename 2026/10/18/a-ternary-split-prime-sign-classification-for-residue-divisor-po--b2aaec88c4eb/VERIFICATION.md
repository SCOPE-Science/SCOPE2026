---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Splitting d|3^t m by 3-adic exponent gives exact D_s=(T_t-1/2)S_s-C_s/2. For negative s, each p≡2 mod3 Euler character factor is strictly positive and smaller than the ordinary factor, hence 0<C_s(m)<=S_s(m), with equality precisely if no p≡2 occurs. The geometric sum T_t gives uniform negativity for s<=-1 and sharp mixed signs for -1<s<0 by divergence of sum_{p≡2 mod3}p^s; multiplying by p≡1 creates infinitely many same-fibre examples. Successors coprime to 3 are always negative, yielding adjacent reversals. For s>=0 direct inequalities settle signs including s=0 boundary. Summing over divisors, the absolutely convergent coefficient c_s=1/2((3^s-1)ζ(1-s)-L(1-s,χ3))<0 follows for s<0 with stated error estimates. Independently compared direct divisor sums against character factorization for 249 n and 4 integer exponents; the analytic divergence and convergence are the infinite proof.

## originality

PASS

The 2021 primary Problem 15 poses class-resolved divisor-power sign questions but does not answer modulus 3. Published parity/modulus-2 finding shares threshold -1 and summatory-bias phenomenon, but depends only on v2 and does not imply modulus-3 same-valuation opposite signs or nontrivial χ3 L correction. Pongsriiam–Vaughan 2015 concerns divisor function on arithmetic progressions of n, not individual divisors d|n. No full or weaker cited theorem implies this sharp ternary partition.

## value

PASS

Modulus 3 is the first residue unit group with a nontrivial real character and exhibits a genuinely new mixed-sign phenomenon at fixed v3 compared with parity. The exact sharp exponent threshold plus counterintuitive negative asymptotic mean despite infinite adjacent reversals addresses an explicitly published mathematical problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
