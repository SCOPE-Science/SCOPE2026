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
The standalone `verify.py` is standard-library Python 3 and may be run with `python3 verify.py`. It checks the exact hub subspace, both other active eigenspaces, polynomial trace and discriminant identities at 1,267 rational inputs, finite parity samples, nine rational yes/no cases, and numerical explicit approximation sequences. Expected output starts with `VERIFY_OK`.

The universal impossibility of perfect transfer follows from the parity contradiction \((u_+-s)(u_--s)=-s^2\), where \(u_+,u_-,s\) are odd. The existence statements use rational-independence and Kronecker density, which are mathematical arguments, not consequences of finite software runs. The classification excludes irrational algebraic potentials.
