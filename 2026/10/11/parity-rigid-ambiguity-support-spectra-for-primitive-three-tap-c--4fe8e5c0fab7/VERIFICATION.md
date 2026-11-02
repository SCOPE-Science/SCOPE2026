---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For every N>=5, a unit-step progression reindexes exactly to {0,1,2}; its ordered differences are the five distinct residues -2,-1,0,1,2. Direct substitution into V_ff(x,k) gives two outer monomial rows with N nonzeros, two adjacent two-term rows with synchronized conjugate roots (each loses one grid frequency iff R=-(B conjugate(A))/(C conjugate(B)) lies in mu_N), and the central positive-coefficient quadratic P(z)=|A|^2+|B|^2 z+|C|^2 z^2. Thus S=5N-2e-h. For a unit root z=e^{i theta}, z^{-1}P(z)=r1+(r0+r2)cos(theta)+i(r2-r0)sin(theta). If sin(theta) is nonzero, equality requires r0=r2 and r1=-2r0 cos(theta)>0; conjugacy gives exactly two sampled nonreal roots iff N/4<j<N/2 and r1/r0=-2cos(2pi j/N). At a real sampled root P(1)>0; only z=-1 can vanish, exactly when N is even and r1=r0+r2, counting a repeated root once. This exhausts h=0,1,2. The explicit five/even or three/odd coefficient triples attain every listed size and simultaneously e=1,h=2 for the minimum 5N-4, which characterizes all minimizing triples. No finite verification is used as an infinite proof; direct independent transforms at 90-digit precision check N=5..20 only.

## originality

PASS

Best-of-knowledge PASS for the precise full coefficient-dependent support law, all-order parity spectrum and complete minimizing phase/amplitude criterion. The earlier prime-order numerical lower bound S>=5p-4 is already covered by Krahmer–Pfander–Rashkov Proposition 4.4 and is not counted as new. Nicola classifies only global support=N extremals; three materially read Resultary full results concern two-tap cross-STFT or a single three-point Fourier polynomial. The current assertion is not mathematically implied by those prior results. The closely titled 2007 technical report could not be read because authorized institutional access was disconnected; priority is not certified absolutely.

## value

PASS

The exactly three-tap self-window progression is a natural first phase-sensitive auto-ambiguity model beyond two-point STFT calculations. Its exact all-order profile classifies every attainable cardinality, identifies the parity-forbidden levels 5N-1 and 5N-3 in odd order, and characterizes all minimizing amplitudes and phases rather than reporting a known lower bound alone. The distinction between a synchronized pair of phase-dependent row zeros and the conjugate central roots is mathematically structural and useful for precise finite time-frequency localization benchmarks. It is a motivated complete family classification, albeit algebraically elementary and intentionally not a theorem for arbitrary three-point supports or different windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
