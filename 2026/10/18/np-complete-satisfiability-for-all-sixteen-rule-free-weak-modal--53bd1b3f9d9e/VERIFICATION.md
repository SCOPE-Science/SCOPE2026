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

The proof in RESULT.md is the basis of the unrestricted correctness claim. The standalone standard-library program `verify.py` tests all 16 combinations of rules, using two finite methods: explicit conjunction-closure expansion with a bounded term size, and independent enumeration of finite closure-compatible subsets. The seeded result was `WEAK_MODAL_VERIFY_OK direct_bounded_closure=394 independent_horn_enumerations=391`.

The brute-force term expansion deliberately limits conjunction size and cannot prove the infinite finite-support lemma; the lemma is established by the conjunction-tree argument. The enumerations test only small generated inputs. The NP upper bound concerns polynomial verification of guessed one-world certificates; it is not a deterministic polynomial-time procedure for satisfiability. Independent mathematical audit has not been performed.
