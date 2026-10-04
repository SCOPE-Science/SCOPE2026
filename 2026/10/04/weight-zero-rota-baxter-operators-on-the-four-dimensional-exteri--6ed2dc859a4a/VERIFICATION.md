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

The finite search space is exact: a linear map on the four-dimensional \(\mathbb F_2\)-space has four image columns, each chosen from \(16\) vectors, so there are \(16^4=65536\) maps.

For a fixed \(R\), the Rota–Baxter defect is bilinear. Therefore the first pass checks the \(16\) ordered basis pairs and is exhaustive. It finds exactly \(80\) operators. A second multiplication implementation, written in tuple coordinates rather than bit operations, then checks each of these \(80\) operators on all \(256\) ordered pairs of elements of \(A\).

The verifier also exhausts all \(65536\) linear maps to identify invertible unital multiplicative maps. It obtains exactly \(24\) automorphisms. Conjugation by this group gives exactly \(12\) stable orbits of sizes
\[
1,1,3,3,6,6,6,6,6,6,12,24,
\]
whose total is \(80\). It verifies that every Rota–Baxter operator kills \(z\) and that the ranks occur with multiplicities \((1,25,30,24)\) for ranks \((0,1,2,3)\).

Run `python3 artifacts/verify.py`. The supplied `artifacts/verification_output.txt` is the corresponding recorded output and begins with `CHECK_OK`.

Finite exhaustive verification proves only the stated \(\mathbb F_2\), weight-zero theorem. No extrapolation to arbitrary characteristic-two fields is made.
