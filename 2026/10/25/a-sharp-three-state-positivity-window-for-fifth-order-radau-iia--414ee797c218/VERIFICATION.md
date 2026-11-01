---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The completed fifth-order three-stage Radau IIA step is R(hQ) for R(z)=(60+24z+3z²)/(60-36z+9z²-z³). For every 2-state generator Q=[[-a,a],[b,-b]], Q²=-(a+b)Q and R(-x)=3((x-4)²+4)/(x³+9x²+36x+60) lies in (0,1]; hence every h>=0 gives an entrywise nonnegative matrix, including a+b=0. In the 3-state pure-birth Jordan block the only potentially negative entry is hR'(−h)=3hp(h)/D(h)² with p=h⁴−16h³−48h²+240h+1200, D=h³+9h²+36h+60. Exact signs at 4,5,17,18 and Descartes give exactly two positive roots, so positivity holds on [0,alpha] union [beta,infinity) and fails between. Independent exact rational reconstruction confirmed (T_Q0(5))_12=-105/13924 and the irreducible reversible epsilon=1/1000 witness negative entry -4448823545303000/676819275720209897. Hurwitz cubic locates the denominator poles in Re z>0, excluding undefined generator steps. Distinct from internal-stage positivity and arbitrary 3-state phase classification.

## originality

PASS

The non-monotone three-state *completed* Radau IIA [2/3] phase window with recovered positivity and the reversible irreducible witness is distinct from classical scalar absolute monotonicity/SSP radii and known endpoint counterexamples for other rational integrators. Do not attribute the Runge–Kutta rational function or generic nonnegativity obstructions as new.

## value

PASS

The minimum state dimension and complete reentrant step-size positivity window are natural stability-versus-positivity invariants for a standard stiff ODE integrator. Reversible irreducible counterexample rules out a modelling assumption that might otherwise seem to protect Markov transition probabilities. Both exact thresholds and recovery distinguish the result from a routine SSP-radius restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
