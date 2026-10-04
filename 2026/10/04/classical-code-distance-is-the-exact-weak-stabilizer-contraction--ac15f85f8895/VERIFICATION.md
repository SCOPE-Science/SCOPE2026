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

The general statement is proved analytically in `RESULT.md`. The only nonstandard external lemma used is the single-stabilizer isotypical action from Dominy et al., arXiv:1207.5880, Lemma 5. The expanded source was inspected directly in open full text; its equation (30) states the factor \(\zeta^{\sigma_S(g)}\), while Lemmas 6 and 7 provide the full-group and generator-only endpoint checks.

The bundled `verify.py` independently checks the finite algebra used for examples. It enumerates binary characters, verifies that the generator schedule has minimum exponent \(1\), verifies that the full nonidentity schedule has constant exponent \(2^{r-1}\) for \(1\le r\le6\), checks the \(r=3\), \(L=4\) intermediate schedule has minimum exponent \(2\), and exhausts all distinct nonidentity-column schedules for \(r=3\), yielding optimal distances \(1,2,2,3,4\) at \(L=3,4,5,6,7\).

Finite enumeration is not used as evidence for the infinite family. The proof for arbitrary \(r\) and \(L\) is the character-product identity followed by the definition of the row-generated binary code and orthogonality of the source's isotypical decomposition.

The statement deliberately does not assert an exact trace-distance bound for evolution interleaved with a Hamiltonian. The source's endpoint recurrence analysis would need to be generalized before making such a dynamical claim.
