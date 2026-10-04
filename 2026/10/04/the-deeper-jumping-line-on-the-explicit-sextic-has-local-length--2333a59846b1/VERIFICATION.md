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

The verifier reconstructs the explicit sextic
\[
F_0=\prod_{i=0}^{5}(x_0-i x_1)+x_2^2\bigl(x_0^4+x_1^4+x_2^4+x_0x_1x_2(x_0+x_1+x_2)\bigr)
\]
and the \(7\times6\) coefficient matrix obtained from the six binary sextics
\[
x\,\partial_iF_0|_{\ell_{u,v}},
\qquad
y\,\partial_iF_0|_{\ell_{u,v}},
\]
for \(i=0,1,2\) and
\[
\ell_{u,v}=\{x_2-u x_0-v x_1=0\}.
\]

At \((u,v)=(0,0)\) it checks exact rank \(4\) and the invertible \(4\times4\) minor
\[
-23520.
\]
It then computes exact bases for the two-dimensional kernel and three-dimensional cokernel and forms the induced first-order normal map.

The three \(2\times2\) minors of that \(3\times2\) linear map are quadratic forms in \(u,v\). Their coefficient matrix in the basis
\[
u^2,\ uv,\ v^2
\]
has determinant
\[
\frac{2655279064360000}{2401}\neq0.
\]
Therefore the quadratic initial minors span \(\mathfrak m^2/\mathfrak m^3\). The local block-reduction and Nakayama argument in `RESULT.md` then proves that the full local jumping ideal is exactly \(\mathfrak m^2\), so the local length is \(3\).

The replay output ends in `VERIFY_OK`.
