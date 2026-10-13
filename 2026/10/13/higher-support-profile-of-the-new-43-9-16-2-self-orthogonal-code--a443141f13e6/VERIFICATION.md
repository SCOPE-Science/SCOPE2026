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
`artifacts/verify.c` uses only the C standard library and embeds the exact published \(9\times43\) binary generator matrix.

The verifier reconstructs all \(512\) codewords, checks rank \(9\), verifies
\[
GG^{\mathsf T}=0,
\]
and reproduces the complete ordinary weight distribution.

For every \(1\le r\le9\), it generates each \(r\)-dimensional subspace of \(\mathbb F_2^9\) once in reduced row-echelon form. The dimension-wise counts are
\[
511,\ 43435,\ 788035,\ 3309747,\ 3309747,\ 788035,\ 43435,\ 511,\ 1.
\]
It computes the support of every corresponding subcode and checks every support-frequency entry recorded in `artifacts/certificate.json`. This certifies both the hierarchy and all minimum-support multiplicities.

Finally, it checks that all 43 columns are nonzero and pairwise distinct and exhausts all \(\binom{43}{3}\) triples, recovering exactly seven dependent triples.

Successful replay prints `VERIFY_OK`.
