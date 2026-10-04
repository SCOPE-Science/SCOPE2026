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

The proof reduces every unit Birkhoff-orthogonal pair in real \(\ell_4^2\) to one scalar \(u\in[0,1]\). The critical computation is the exact identity
\[
(1+9u+6u^2)^2-9(1+2u+9u^2+4u^3)=4(9u^4+18u^3+3u^2-2).
\]
The quartic on the right has derivative \(6u(6u^2+9u+1)>0\) for \(u>0\), so its sign change from \(u=0\) to \(u=1\) gives one and only one critical point. Endpoint objective values vanish, making this critical point the global maximum.

Replay with:

`python3 artifacts/verify.py`

The checker uses exact rational polynomial arithmetic for the displayed identity and high-precision decimal arithmetic only for root isolation and the witness. It checks \(\|x\|_4=\|y\|_4=1\), the Birkhoff support equation, and agreement between the witness objective and \(\sqrt{1/6-u_0^2/2}\). A successful replay prints `VERIFY_OK`.

Unproved limits: no arbitrary-\(p\) formula is asserted, and no independent audit has been performed.
