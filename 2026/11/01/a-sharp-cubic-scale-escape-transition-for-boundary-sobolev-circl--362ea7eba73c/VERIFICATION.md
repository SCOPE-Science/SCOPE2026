---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. Haar orthogonality determines coefficients c_j=-lambda j P'(1) and P'(1)=n/(1+lambda S_n), S_n=sum_{j<n}j², yielding P=z[z^{n-1}-A sum_{j=1}^{n-1}j z^{j-1}] with A=n lambda/(1+lambda S_n). Descartes sign rule or monotonic F_m(r) gives one simple positive root; setting r=1 yields lambda_c exactly. For A<A*, Rouché gives all Q roots inside; at equality only r=1 is on the boundary; for A>A*, the explicit |B_{m,A}(e^{i theta})|²-A²=2(1-cos theta){A[A m(m+1)-2]+2(1-cos theta)[A(m+1)+1]} is strictly positive except at z=1, forbidding another boundary crossing. For n=2, the m=1 edge case follows directly. For lambda_n the monotone inversion of a locally uniform Riemann sum gives H(u) limits for s<=3; a relative O((1+v)²/n) Laplace-sum error for v=O(log n) and equation e^-v v²~tau n^{-(s-3)} gives the s>3 log and loglog expansion with constants. Separate exact symbolic verification of the unit-circle identity and 57 finite root-class cases was performed; inspected pinned CHECK.py. Finite roots do not prove all n, lambda, tau or s.

## originality

PASS

PASS, explicitly best-of-knowledge, with unusually material unresolved priority risk. The rank-one discrete Sobolev perturbation formula is standard. Castillo, Garza and Marcellán (Numerical Algorithms 60, 2012, 669–681), DOI 10.1007/s11075-012-9594-6, is a directly relevant earlier study of zeros for the exact general inner-product form with derivative evaluation at arbitrary alpha and lambda, and may include the special Haar/alpha=1 case. Both arXiv/preprint and lawful OA searches did not yield its full text; authorized Oxford retrieval returned vpn_disconnected. Its accessible abstract states general zero behaviour when n and lambda vary but neither this precise all-degree threshold nor the loglog asymptotic. No whole-paper NOT_COVERING finding is made. The 2026 Majumder–Swaminathan arXiv:2610.31994 studies absolutely continuous derivative measures on the circle rather than the point mass at 1, so its stated hypotheses do not directly cover the result. On the specific full formula and exact asymptotic available to compare, retain PASS with explicit literature priority risk, not an access-based automatic rejection.

## value

PASS

PASS. For a canonical Haar orthogonality perturbed by a boundary derivative atom, the exact transition location of the unique escaping zero across every degree is a natural sharp zero-geometry invariant. The cubic mass scale and three moving-parameter regimes, including a loglog subcritical asymptotic, go well beyond merely restating a rank-one perturbation formula or illustrating small degrees. Such precise quantitative root behaviour can be independently useful for asymptotic Sobolev orthogonal polynomial theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
