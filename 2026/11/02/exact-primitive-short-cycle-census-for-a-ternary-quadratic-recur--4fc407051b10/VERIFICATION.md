---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For every k>=2, the recurrence T_k(w)=(w1,...,w{k-1},w0+w{k-1}^2) over F3 is bijective. For each d|k the T_k^(4d)-fixed bi-infinite recurrence divides into d columns and four rows. Even reduced delay k/d modulo 4 forces no nonzero indicator. Odd reduced delay forces exactly one zero per column (or all-zero word), with two possible zero-row increments and a cyclic boundary shift. This yields the exact residue-class binomial expressions F_k(d); counting zeros per orbit forces every nonzero least short period to be 4d, and Mobius inversion gives C_k(4d)=(4d)^(-1) sum_{e|d} mu(d/e)(F_k(e)-1). The fourth-root-of-unity filter gives 2^k all-minimum period 4k for k a power of 2 at least 4. Independent *direct* state iteration over every 3^k state for k=2..10 (not reuse of verifier) reproduced each divisor fixed-count formula and counts k=9: one 12-cycle, thirteen 36-cycles; k=10: one 8-cycle, twenty-seven 40-cycles. Source C++ verifier inspected separately. Finite experiments do not prove all k; all-k argument is the row/column proof.

## originality

PASS

Best-of-knowledge PASS: Steven Finch arXiv:2610.34300 studies the same recurrence and the aggregate states fixed by 4k. Its public abstract and source's precise Proposition 7/Theorem 8 comparisons do not establish the divisor-resolved F_k(d) for both reduced-ratio residue classes and primitive periods obtained by Mobius inversion. A full independent read of Finch's paper could not be completed: direct arXiv HTML/PDF attempts failed; authorized institutional full-text access returned vpn_disconnected. The prior paper could conceal an implication, explicitly recorded as risk. Published Resultary semantic matches did not establish exact same census.

## value

PASS

Nontrivial complete primitive-period census for a canonical quadratic permutation's distinguished short-period sector, revealing primitive periods 8,12,36,40 and rigid 2-power delays; motivated by prior aggregate period counts, not an arbitrary finite table. It explicitly does not classify longer periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
