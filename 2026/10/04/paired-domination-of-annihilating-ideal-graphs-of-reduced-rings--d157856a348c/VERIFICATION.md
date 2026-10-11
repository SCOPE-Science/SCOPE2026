---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Let the distinct minimal primes be \(P_1,\ldots,P_m\) and \(A_i=\prod_{j\ne i}P_j\). Reducedness and minimal-prime incomparability imply \(A_i\ne0\), while \(A_iP_i=0\), so all \(A_i\) are vertices. For \(i\ne k\), \(A_iA_k\) lies in every minimal prime and is therefore zero, so the \(A_i\) form a clique. Every annihilating ideal \(I\) is contained in some \(P_i\): choose nonzero \(x\in\operatorname{Ann}(I)\) and a minimal prime avoiding \(x\), then primality forces \(I\subseteq P_i\). Hence the \(A_i\) totally dominate. The proof that each \(P_i\) is maximal among proper annihilating ideals gives the matching lower bound \(m\) for total domination without relying on the flawed general theorem noted in later literature. Parity yields the paired lower bound, and the clique attains it when \(m\) is even; when \(m\) is odd, adding \(P_1\) and matching it to \(A_1\) attains \(m+1\). A fresh independent support-graph reconstruction for products of two through five copies of \(\mathbb F_2\) returned paired-domination values \(2,4,4,6\), matching the formula.

## originality

PASS

Chelvam and Selvakumar prove the parity formula for commutative Artinian rings in terms of the number of local factors. Nikandish, Maimani, and Kiani later prove that for reduced rings with finitely many minimal primes the ordinary and total domination numbers equal the number of minimal primes, while Badie revisits the total-domination theory and records flaws in an earlier general theorem. No inspected source states paired domination for arbitrary non-Artinian reduced rings with finite minimal spectrum. The audited proof supplies a self-contained maximal-annihilator lower bound and a clique of complementary minimal-prime products, extending the Artinian parity phenomenon to the full reduced finite-minimal-spectrum class. Current Resultary search returned the assigned theorem and narrower product-of-fields/ideal-intersection records, but no prior broader paired theorem.

## value

PASS

The theorem extends an Artinian paired-domination parity formula to all reduced rings with finite minimal spectrum, a substantially broader algebraic class, and supplies a direct proof robust to known issues in older total-domination arguments. The complementary-minimal-prime clique gives a reusable structural description of optimal paired dominating sets rather than merely a numerical extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
