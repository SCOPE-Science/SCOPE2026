---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Thaddeus §2.2 describes rank-u complete collineations as Vainsencher iterated smooth blowups of P Hom(S_V,W) over Gr_u(V). For each lower rank r, the transformed center records the u-plane, (u-r)-kernel and r-dimensional image, with square complete-collineation fiber C_r; smooth determinantal codimension is (u-r)(w-r). The smooth blowup changes χ by (codim-1)χ(center), giving square recurrence E_n=n²+Σ_{r<n}((n-r)²-1)binom(n,r)²E_r and rank-u recurrence binom(v,u)[uw+Σ_{r<u}((u-r)(w-r)-1)binom(u,r)binom(w,r)(r!)²]. With E_r=(r!)², both sums telescope through (j(j+q)-1)/(j!(q+j)!)=1/((j-1)!(q+j-1)!)-1/(j!(q+j)!), giving χ=binom(v,u)binom(w,u)(u!)² for all v,w and 1≤u≤min(v,w), including u=1 and square full-rank. Independently evaluated exact integer recurrences for (v,w,u)=(3,5,2),(4,4,4),(7,9,5),(10,12,7), checking 120,576,38102400,2414168064000. These finite tuples are only regression evidence; geometry plus telescoping establishes all dimensions.

## originality

PASS

PASS (best of knowledge): the main final all-parameter/complete enumeration is not implied by the inspected relevant prior results. Known general tools and specialized prior fibers/cases are acknowledged, with indexed-query and equivalent-formulation residual risks recorded.

## value

PASS

PASS: The topological Euler characteristic of the canonical complete-collineation compactification is a natural all-rank invariant in algebraic geometry. An explicit uniform factorial closed form, including square wonderful compactifications and rectangular rank-u cases, identifies cell-count growth and a double symmetric-group factorial phenomenon. It is a useful invariant in studying blowup models, even without claiming a new full cohomology ring or Chow motive; nontrivial content is the uniform geometric center factorization and recurrence evaluation, not an arbitrary finite number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
