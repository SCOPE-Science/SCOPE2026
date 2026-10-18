---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

The change \(q=-\log(1-x),\ p=-y\) is invertible for \(x<1\) and preserves physical time, giving \(\dot q=p\), \(\dot p=e^{-q}-1\), and conserved \(H=p^2/2+q+e^{-q}-1\). The coercive strictly convex potential yields a unique closed energy oval. Positive turning point satisfies \(a_E=E+1+o(1)\); negative turning magnitude \(r_E=O(\log E)\). Exact identity \(E-V(a_E-w)=w-e^{-a_E}(e^w-1)\) bounds positive descent uniformly between \(\sqrt{2w}\) and \(\sqrt{2w}/\sqrt{1-\eta_E}\), \(\eta_E=O(E^{-1})\). On the negative branch \(E-V(-r_E+w)=(E+r_E+1)(1-e^{-w})-w\), yielding \(t_-=O(\log E/\sqrt E)\), while \(t_+=\sqrt{2E}(1+O(E^{-1}))\). Thus negative excursion shrinks in normalized phase; positive branch gives the uniform parabolic limit. The energy identity and sign of \(p\) yield the asserted pointwise-off-midpoint and dominated \(L^1\) momentum limit. Since \(x(sT)ds=-(\sqrt{2E}/T)dP_E\), integration by parts transfers the momentum jump to signed measure \(ds-\delta_{1/2}\). For all continuous tests the extension is justified by \(x\le1\), zero mean over an orbit, hence \(\int|x|ds\le2\). Pushforward density is the two-branch inverse derivative of the limiting parabola. The inspected \(check.py\) makes only bounded finite quadrature sanity checks and is not relied on as asymptotic proof.

## originality

PASS

The primary same-Toda oscillator paper contains the energy quadrature, limiting high-energy period behavior and approximate waveforms, all acknowledged. Its sections on undamped solutions, phase, output power and physical interpretation were examined; they do not assert the weak-* signed physical-force measure \(ds-\delta_{1/2}\) or the joint uniform normalized phase and exact time-sampling density. Loud period-criticality results address a different invariant. The signed delta limit adds a precise original-time dynamical singularity rather than presenting the known period asymptotic as new.

## value

PASS

The signed mass-one force impulse in unmodified physical time describes a singular boundary layer of a classic integrable Loud/Toda oscillator and determines an exact phase-statistical law. This supplies qualitative limiting information not obtained from the known period asymptotic, with a motivated dynamical observable and nontrivial weak-* normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
