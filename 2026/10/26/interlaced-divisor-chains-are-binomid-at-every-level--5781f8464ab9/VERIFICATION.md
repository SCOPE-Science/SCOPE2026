---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For each prime p, let a_n=v_p(f_n). Hypotheses f_1|f_2 and f_n|f_{n+2} give a_1<=a_2 and monotonicity separately along parity classes. Verified the shifted-interval lemma by pairing equal-parity positions, with the exceptional even-start odd-length final even term compared to a_1 using a_{s+2h}>=a_2>=a_1. It gives each ordinary generalized binomial valuation >=0. For width j the column valuation b_n=sum_{i=n}^{n+j-1}a_i-sum_{i=1}^j a_i has b_1=0, b_2=a_{j+1}-a_1>=0 and b_{n+2}>=b_n; the same lemma proves every generalized binomial coefficient in every column integral for every N,K,j,p. This handles all unbounded quantifiers, not just initial terms. Verified semigroup examples H_q=<2,2q+1> are ComboSum by closure under addition, not ordinary chains because f_2=p and f_3=1; the factor at 2r for odd prime r>=2q+1 gives 1/p and rules out Shapiro divisor-product form. Checked periodic valuations (0,1,1) yield a three-step analogue failing in column two with B_{C2}(4,2)=1/2. Independently generated 500 random parity-monotone finite valuation sequences and checked every available column, confirming the finite consequences but not replacing the interval proof.

## originality

PASS

Shapiro (2023) proves divisor chains and divisor-product sequences binomid at every level, and explicitly asks whether all ComboSum sequences are. The current two-step parity-divisibility sufficient condition is a distinct implication, because its natural semigroup examples fail both stated sufficient conditions. It supplies a rigorously identified proper ComboSum subclass, not a resolution of the unrestricted question. The Caalim–Tanaka finite-index extension problem addresses a different object. Priority uncertainty remains for stronger interval-majorization sufficient criteria not found by exact/general searches.

## value

PASS

The binomid-pyramid all-level integrality problem is explicitly motivated by an open sufficient-condition/ComboSum question. A concise but genuinely nontrivial valuation lemma handles infinitely many column widths, and the semigroup family demonstrates coverage beyond familiar sufficient hypotheses. The three-step counterexample isolates a meaningful structural boundary rather than an arbitrary finite case. No claim of complete characterization or solution to the full ComboSum question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
