---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The companion `artifacts/verify.py` uses only the Python standard library.

It performs four checks:

1. Exhaustive enumeration of labeled triangle-free graphs through six vertices, obtaining \(1,1,2,7,41,388,5789\).
2. Boundary checks for \(K_r\)-free labeled graphs: for \(n<r\), every graph is allowed, while at \(n=r\) only the complete graph is excluded.
3. Explicit construction of every graph/order pair for the triangle-free case through \(n=4\), confirming the finite identity \(a_3(n)=n!f_3(n)\) at the encoding level.
4. Exact rational verification for \(3\le r\le30\) that \(\lambda_r=(r-2)/(2(r-1))\) is strictly increasing and that \(1+1/(1-2\lambda_r)=r\).

The replay prints

`ordered_triangle_free_profile_n1_to_6= [1, 4, 42, 984, 46560, 4168080]`

followed by `VERIFY_OK`.

The finite replay does not verify the Erdős–Kleitman–Rothschild asymptotic theorem or Turán's theorem; those are cited mathematical inputs. It checks the finite combinatorial bridge and the algebraic consequences used here.
