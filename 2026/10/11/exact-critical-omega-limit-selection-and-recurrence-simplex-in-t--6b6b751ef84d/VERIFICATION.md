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

# Verification and limits

Exact branch identities and the endpoint circle substitution were checked with SymPy 1.14.0 from the packaged `verify_symbolic.py` and `requirements.txt`. The checker finished with:

```
PASS: both smooth branches, two conserved-balance identities, critical factors, exact circles, and their Lyapunov levels
```

The analytic measure proof additionally requires compact support for invariant-generator averaging, a switching-level kinetic-zero lemma, bounded complete trajectories in the invariant support, and uniqueness of invariant probability on a nonconstant periodic circle. None of these infinite-statistical claims is inferred from the symbolic script. The sharp least-period inequality is proved by periodic Wirtinger, with an exact substituted equality case; no finite numerical search is relied on. The original 1999 and 2000 papers were inspected in relevant full-text sections. A separate 2000 no-chaos paper remained available only by abstract; any previously unnoticed critical invariant-measure theorem therein remains a literature risk. Independent audit has not been performed.
