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

The universal statement is proved analytically by identifying \(\mathbf H_2(\mathbb C)\) with Pauli coordinates \((t,r)\) and the rank-one positive semidefinite matrices with the future null cone \(t>0\), \(t^2=\|r\|^2\).

For a rank-three measurement operator, let its kernel generator have coordinates \((\tau,w)\), and put
\[
q=\tau^2-\|w\|^2=4\det H.
\]
For an input cone point \((t,tn)\), \(t>0\), \(\|n\|=1\), the fiber line meets the null cone where
\[
s\Bigl(2t(\tau-n\cdot w)+sq\Bigr)=0.
\]
When \(q\ne0\), the time coordinate of the only possible second intersection is
\[
t_*=-\frac{t\,\|\tau n-w\|^2}{q}.
\]
Thus \(q>0\) places the second algebraic point on the past cone, while \(q<0\) places it on the future cone except at the tangent set \(\tau=n\cdot w\). When \(q=0\), the equation is linear in \(s\) after the known root is factored out, and a second intersection is possible only in the unique null direction of the kernel generator.

The bundled `verify.py` uses exact rational arithmetic to replay these identities on rational unit Bloch directions and checks canonical kernel representatives of all three signs. A successful run prints

`VERIFY_OK regimes=3 rational_directions=25`

The checker is supplementary. Finite samples are not used to establish the all-triples theorem, and the theorem makes no assertion about higher dimensions or about additional positivity constraints on the measurement matrices.
