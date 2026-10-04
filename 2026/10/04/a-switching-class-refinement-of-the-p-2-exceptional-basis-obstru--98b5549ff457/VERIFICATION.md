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

The verifier constructs the standard Euler Gram matrices for \(\mathbf P^4\) and \(\mathbf P^6\) from
\[
B_{ij}=\binom{p-1+j-i}{p-1}
\]
for \(i\le j\), with zero entries below the diagonal.

For each of \(p=5\) and \(p=7\), it verifies \(B\equiv I\pmod p\), forms
\[
A=\frac{B-B^{\mathsf T}}p\bmod p,
\]
and checks entry-by-entry that
\[
A_{ij}=(j-i)^{-1}
\]
for \(i<j\).

It enumerates all unordered triples and checks the closed formula
\[
(A_{ij}A_{jk}A_{ki})^2=[(j-i)(k-j)(k-i)]^{-2},
\]
obtaining the exact multisets
\[
\Theta_5=\{1^{\times5},4^{\times5}\},
\qquad
\Theta_7=\{1^{\times14},2^{\times21}\}.
\]

The verifier also performs exact right mutations on adjacent pairs of the standard Gram matrix. After every mutation it checks that the new normalized skew residue is the old one conjugated by the corresponding adjacent permutation modulo \(p\). A separate sign-change test checks diagonal switching.

The replay output stored in `verification_output.txt` ends in `VERIFY_OK`.

The finite replay checks representative prime cases and exact algebraic transformations. The theorem for arbitrary odd prime \(p\) is the symbolic basis-change proof in `RESULT.md`.
