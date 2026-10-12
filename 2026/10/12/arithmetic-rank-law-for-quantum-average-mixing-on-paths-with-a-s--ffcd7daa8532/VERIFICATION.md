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

# Exact verification and limitations

Execute `python verify_marked_path.py` with a standard Python 3 installation. No package installation, external database, or other file is needed. The checker builds integer powers of each tridiagonal Hamiltonian, extracts diagonal walk moments, and computes rational row ranks without floating-point approximations. A separate symbolic calculation checks the proposed Chebyshev reflection differences coefficient by coefficient.

Expected completed output:

```
VERIFY_OK symbolic_antisymmetric_minor_identities=1014 exact_moment_rank_instances=680 negative_potential_instances=170 site_cases=170 path_orders=2..18
```

The exact rank tests include every site for every order from two through eighteen, for potentials minus two, three-halves, one and three, and the symbolic identities include the central odd-order cases and reflection sign change. Neither finite checks nor execution logs establish the general theorem. The proof in `RESULT.md` supplies the unrestricted argument through spectral simplicity, exact adjugate identities, Chebyshev reflection differences and polynomial gcds. No independent audit has been performed.
