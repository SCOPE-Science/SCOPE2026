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

Twice apply defining polynomial recursion. For n=4t+1, residue 3 mod 4 is empty; for n=4t+3 residue 2 mod 4 is empty; even n have only even exponents. Therefore no four-term run is possible, while P_5=1+x+x² realizes three. Define I_t=|E_t intersection E_{t+1}| and J_t=#(j in E_t with j+1 in E_{t+1}); parity decomposition yields I_{2u}=I_u, I_{2u+1}=s(u+1), J_{2u}=s(u), J_{2u+1}=J_u. Stern sums give S_k=(3^k-1)/2, U_k=(3^k-1)/2; aggregate adjacent-pair A_r=(3^(r-1)-1)/2 and triple B_r=(3^(r-2)-1)/2; invert C_r-2A_r+B_r etc to exact R1=2h+1,R2=(h+1)/2,R3=(h-1)/2 for all r>=2. Independently generated 4096 polynomial supports and compared them with Lucas parity; all eleven dyadic-prefix run counts and max-3 condition agreed. Finite checks independently corroborate, do not prove the dyadic recurrence.

## originality

PASS

Best-of-knowledge PASS for maximal coefficient-support run length and exact dyadic run-length histogram for the specified Dilcher–Stolarsky (0,1)-polynomials. The family/0-1 coefficient property, coefficient matrix and fixed-exponent sums are established antecedents; no identified source states the within-row consecutive run histogram. The foundational 2007 full article was inaccessible, a meaningful explicit risk.

## value

PASS

Consecutive coefficient runs are a canonical local statistic of the support of a naturally defined automatic-polynomial sequence. A sharp uniform maximum, complete exact run-length distribution at every dyadic scale and universal limiting proportions give reusable local-support information not supplied by coefficient totals or factorization. This is a natural complete classification, not an arbitrary finite slice or known-table reprint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
