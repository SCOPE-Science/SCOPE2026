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

The universal proof was reconstructed from definitions. The critical checks are:

1. From \(\tau(N)=\prod(e_i+1)\), the condition \(4\nmid\tau(N)\) permits either no odd exponent or exactly one odd exponent; in the latter case that exponent is \(1\pmod4\).
2. For \(N=8n+1\), the unique odd-exponent prime is forced to be \(1\pmod8\).
3. Quadratic reciprocity makes \(2\) a quadratic residue modulo that prime. The norm-Euclidean calculation in \(\mathbb Z[\sqrt2]\) then yields a factor of norm \(p\), and parity refines \(p=A^2-2C^2\) to \(p=A^2-8B^2\).
4. Scaling the norm identity gives \(8n+1=(2m+1)^2-8r^2\), which is algebraically equivalent to \(n=T_m-r^2\).

`artifacts/verify.py` was replayed from the packaged path. It returned `VERIFY_OK` for every \(0\le n\le100000\), checking \(21447\) inputs with \(4\nmid\tau(8n+1)\). The split was \(447\) square cases and \(21000\) unique-odd-exponent cases.

The computation is finite and is not treated as proof of the infinite statement. No independent audit has been performed.
