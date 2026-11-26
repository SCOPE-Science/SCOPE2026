---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Trace preservation on the other sites reduces the computation to two Kraus channels on the undamped two-site marginal. Counting matching strings gives diagonal A,B,B,D and coherence B between 01 and 10. Damping changes the coherence to qB and vacuum/double-excitation populations to a(q) and q²D, so the X-state concurrence is exactly 2q[B−√(Da(q))]₊. The squared comparison F=B²−Da(q) has F(1)=E=k(N−k)/[N²(N−1)]>0, and is strictly increasing for k≥2 since D<k/N. Thus for 0<q≤1 survival throughout occurs when B²≥D, including equality; otherwise the smaller root is the unique crossing in (0,1) and is the displayed q_c. For k=1 the concurrence is 2qB, and q=0 gives zero for every k. At fixed N the positive ratio B²/D for k>1 has log derivative −1/[k(k−1)]−2/(N−k). Writing the ratio as [k/(k−1)](1−k/N)²/(1−1/N) gives 1+(1/c−2c)/√N+o(N⁻¹ᐟ²) when k/√N→c>0. Integer sequences above and below c=1/√2 therefore bracket K_N with arbitrary fixed slack. With ε=1−q one has the exact F=E−2εDB−ε²D²; at k/√N→c its N^(3/2) rescaling tends to c−2εc³, while √N(B+√(Da))→2c. At k/N→α and ε=s/N, NF→α(1−α)(1−2sα²) and B+√(Da)→2α(1−α). Rationalization gives both clipped profiles, including the zero boundary. In the macroscopic regime B²/D→(1−α)²<1, so q_c exists eventually and ε_c=E/[D(√(B²+E)+B)] gives Nε_c→1/(2α²). The supplied verifier was inspected without execution; finite samples are not the proof of either limit.

## originality

PASS

The elementary X-state damping test and the undamped Dicke reduction are known ingredients, and the finite concurrence formula is a specialization. The supported distinct result is the classification in Dicke index and the two finite-size scaling laws and threshold constants for this input family. The closest actual overlaps use the same damping but different observables or a two-qubit pure-input ensemble rather than mixed two-site reductions.

## value

PASS

Independent loss of Dicke excitations is a standard model and two-site concurrence answers a concrete question different from Bell violations. The result tells a researcher how many excitations can be used while preserving pair entanglement at every positive survival probability, and resolves the order and constant of tolerable loss at macroscopic density. The distinct scaled profiles preserve information lost by just noting that undamped concurrence goes to zero with N. This is not merely another finite example of sudden death.

The dated certificate retains the supplied scientific assessment, sources and limitations.
