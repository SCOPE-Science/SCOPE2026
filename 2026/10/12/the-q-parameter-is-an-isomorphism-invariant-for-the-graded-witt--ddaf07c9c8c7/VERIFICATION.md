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

The proof has two logically separate inputs. First, direct subtraction of the displayed products gives the Witt bracket for every admissible \(q\) and \(\lambda\). Second, the published Witt automorphism theorem says every Lie automorphism has the sign-and-scaling form \(W_n\mapsto\varepsilon a^nW_{\varepsilon n}\). After substitution, multiplicativity is an affine polynomial identity in \(m,n\). Comparing its \(m\)-coefficient gives \(q=q'\), and then the constant term gives \(\mu=\varepsilon\lambda\). This is an exact symbolic proof for all integer indices.

`verify.py` is a regression checker, not an infinite certificate. It uses exact rational arithmetic to test the common-commutator identity, the cross-parameter coefficient criterion, the converse isomorphisms, and the automorphism sign condition on a finite grid. The replay result in `verification_output.txt` is `CHECK_OK`.

The verification does not independently re-prove Bavula's complete classification of Witt Lie automorphisms. That published theorem is an explicit premise of the proof. No conclusion is drawn for \(q=0\), \(q=1\), noncomplex ground fields, or ungraded products.
