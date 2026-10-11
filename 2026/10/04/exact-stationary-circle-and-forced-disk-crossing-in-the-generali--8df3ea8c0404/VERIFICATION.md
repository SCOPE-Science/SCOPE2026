---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For the generalized Sprott O vector field, direct differentiation gives the exact coboundary \(L(xy+z-bx)=x^2+y^2+ax\). Every compact invariant probability therefore satisfies \(\mathbb E[(x+a/2)^2+y^2]=a^2/4\). Stationarity of \(x\) and \(y\) gives \(\mathbb E[y]=0\) and \(\mathbb E[x]=\mathbb E[z]=m\), yielding the variance parabola. Zero variance at either endpoint forces the corresponding equilibrium atom, using the displayed \(L(yz)\) identity. On the boundary circle, \(LF=y(4x-2z+a)\); if a complete trajectory is not an equilibrium, an interval with \(y\ne0\) forces a linear relation between \(z\) and \(x\), and substitution back yields a nonzero quartic vanishing on an interval, a contradiction. Hence only equilibrium mixtures live on the circle, and every other invariant measure has positive mass on both sides. Periodic-orbit crossing follows by continuity. The exact sparse-polynomial verifier checks all algebraic identities.

## originality

PASS

Sprott's original paper gives the canonical O system and its equilibria, while the later dynamic-regions note gives exactly the two-parameter generalized equations used here and maps numerical dynamical regimes. Neither inspected source states the stationary circle, mean-variance parabola, or forced disk crossing. The complete Dimitrova--Yordanov paper studies statistical spectra of generalized Sprott B and N systems rather than O. A particularly relevant 2004 analytical Sprott-flow paper could not be reliably inspected because the authorized DOI retrieval returned mismatched content; it is retained as a residual bibliographic risk and is not used for a noncoverage claim. Targeted Resultary searches returned no implication-equivalent O-system balance law.

## value

PASS

The stationary circle is a parameter-exact geometric constraint on every compact recurrent statistical state of a standard generalized chaotic flow. The theorem also classifies the boundary-supported invariant measures and forces every nonconstant periodic orbit to cross the circle, turning a simple coboundary into a global recurrence statement. This is a natural structural property of the named flow rather than a numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
