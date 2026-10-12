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
`artifacts/verify.py` uses only the Python standard library.

It checks that
\[
X^4-X^2-1
\]
has neither a linear nor a quadratic factor over \(\mathbb F_7\), hence is irreducible.

The script implements exact arithmetic in
\[
\mathbb F_7[\omega]/(\omega^4-\omega^2-1)
\]
and verifies
\[
\omega^{16}=-1,\qquad \omega^{32}=1,
\]
with no smaller divisor of \(32\) giving \(1\). It also verifies
\[
(4\omega^2-2)^2=-1.
\]

Every affine point \(t\in\mathbb F_{7^4}\), together with the projective point at infinity, is then evaluated through the source codeword formula. Coordinate-span ranks over \(\mathbb F_7\) are computed exactly. The projective rank spectrum is checked to be
\[
1:1,\qquad2:49,\qquad3:2352.
\]

Multiplying by the \(2400\) nonzero scalar multiples in each projective line gives
\[
1+2400z+117600z^2+5644800z^3.
\]

As an independent combinatorial check, the verifier counts the affine relation incidences and verifies
\[
56=8+48,
\]
where the unique rank-one point contributes all eight projective relation directions and the remaining \(48\) incidences correspond to rank-two affine points.

Successful replay prints `VERIFY_OK`.
