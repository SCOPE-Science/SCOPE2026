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

The exact proof is symbolic. The bundled checker supplies a finite replay using positive rational parameters and the source's reduced carrying capacity
\[
K=300.
\]

For an initial state with
\[
x=3,\qquad y=10,\qquad z=10,
\]
it computes the six published transition rates along the event sequence consisting first of immune-death jumps and then tumor-birth jumps. It verifies that every selected event has positive rate and positive conditional probability.

After the immune count reaches zero, the checker verifies at each state that
\[
r_2=r_3=r_4=r_5=0
\]
and
\[
r_1>0
\]
until \(x=K\). Therefore no tumor-death jump is available along the second stage.

The checker also evaluates
\[
1-0.05^{1/10000}
\]
at high precision and obtains
\[
0.00029952835977661200928\ldots.
\]

The finite replay does not prove the theorem by enumeration. General validity follows from the symbolic positivity and zero-factor identities in `RESULT.md`.
