---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

True order-two polyanalytic Fock space in one variable has simple rotation-character Hermite basis psi_0=bar(z), psi_n=(z^n bar(z)−n z^(n−1))/sqrt(n!), so radial bounded operators are diagonal with bounded coefficients a_n. Coherent-state Berezin evaluation equals e^(−x)[x F''+(1−2x)F'+xF], F=Σ a_n x^n/n!, including x=0. The null equation with F=e^x H reduces to xH''+H'+H=0, recurrence (j+1)² h_{j+1}=−h_j, hence a_n=c L_n(1), a unique compact nonzero bounded null operator. Classical Laguerre Plancherel–Rotach L_n(1)=(e^1/2/sqrt(pi))n^−1/4[cos(2sqrt n−pi/4)+O(n^−1/2)]. Joint equidistribution of n/M and phase 2sqrt n modulo 2pi gives N_D(t)~(3e²/(8pi²))t^−4 because average cos^4=3/8; monotone inversion gives k^1/4 s_k→(3e²/(8pi²))^1/4, S_p threshold p>4 for kernel element, and normalized fourth-power harmonic sum constant 3e²/(8pi²). Independently recalculated Laguerre recurrence through n=250000 and counting estimates t=.10,.07,.05 converging to normalized 0.99982,1.00017,1.00007. This supports but does not prove infinite equidistribution.

## originality

PASS

Fulsche–Hagger 2024 already has full bounded-operator noninjectivity, trace-class injectivity, Weyl/Laguerre zero description and related p=4 symbol Lp cutoff for a DIFFERENT map; the qualitative radial kernel line might follow from radialization. New assessed precision is radial operator-Schatten threshold and explicit ordered Laguerre constant. Symbol integrability and operator Schatten summability are not interchangeable.

## value

PASS

The exact injectivity boundary of a natural Berezin transform on the full radial Schatten scale, together with the ordered singular-value and logarithmic fourth-moment constants, is a nontrivial operator-ideal classification beyond previously known trace-class injectivity and B(H) noninjectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
