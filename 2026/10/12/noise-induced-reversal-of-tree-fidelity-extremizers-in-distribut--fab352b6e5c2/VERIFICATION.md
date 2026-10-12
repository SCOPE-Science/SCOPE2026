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

The all-size proof is in `RESULT.md`. It assumes exactly the source's independent noisy-resource-channel formulas, with ideal gates, data qubits and readout.

For \(0<q<1\), the second derivative
\[
\frac{d^2}{ds^2}\log(1+q^s)=\frac{(\log q)^2q^s}{(1+q^s)^2}>0
\]
combines with integer degree majorization to give the sharp path/star bounds.

For \(q=-r\), \(0<r\le1/3\), the key negative-regime inequality is
\[
(1-r)(1+r+r^2)^2-(1+r^2)=r(1+r)(1-r-r^3)>0.
\]
It proves that two independent positive degree-excess contributions exceed the largest possible single contribution; the full path maximality uses the separate bound on the number of positive excess coordinates.

For maximum-degree-three trees,
\[
(1+q)(1+q^3)-(1+q^2)^2=q(1-q)^2
\]
controls the exact branching ratio.

The bundled standalone Python checker enumerates all \(18,244\) labeled Prüfer words for \(4\le n\le7\), uses exact rational arithmetic for both positive and negative parameters, verifies the equality degree types and the entire subcubic formula on those cases, and replays the two key polynomial inequalities at representative rational points. It printed `VERIFY_OK 18244 labelled tree sequences` in direct execution. This finite computation is not used to infer universal quantifiers; the proof above covers every \(n\ge4\) and the full physical parameter intervals.

The theorem does not assert hardware-native embeddability or experimental noise robustness. The physical high-noise boundary \(p=3/4\) corresponds to a vanishing channel contraction, not a phase transition in many-body thermodynamics.
