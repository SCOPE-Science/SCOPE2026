---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For the positive mass-action system x'=x(ax-by), y'=y(bx-cy), reconstruct r=y/x and D(r)=(b-a)+(b-c)r, giving r'=xrD(r) and d log x/dr=(a-br)/(rD). In the wedge b>=max(a,c), b>min(a,c), D>0; the explicitly integrated profiles x=K Phi(r), y=rK Phi(r) vanish as r tends to 0 and infinity, remain bounded and exclude finite-time blowup, proving every positive orbit is a complete two-sided homoclinic. Reciprocal derivatives (1/x)'=-a+br and (1/y)'=c-b/r yield the original-time universal 1/(a|t|) and 1/(ct) dominant tails. Ratio asymptotics yield minority powers |t|^{-b/a}, t^{-b/c}, while b=a>c and b=c>a yield the precise 1/(t log t) logarithmic constants. Outside the wedge, invariant small/large-r cones make x or y blow up quadratically in finite forward/backward time; a=b=c has positive diagonal equilibria. Independently verified all three rational quadratures symbolically and a source example; finite algebra checks do not prove the global time assertions.

## originality

PASS

The specific a=c=1,b=3 homoclinic is already in Yeung–Erban 2026. The 2018 quadratic Lotka–Volterra integrability theory and classical sector classifications are prior technique. What survives is the three-rate all-positive initial-condition iff region and equality-face original-time logarithmic constants; no exact covering statement was located in examined primary accessible text or Resultary. Yeung–Erban full primary could not be read in this run, so this is a qualified best-of-knowledge judgment rather than absolute priority.

## value

PASS

The iff homoclinic region and singular logarithmic transitions distinguish global kinetic behavior of an explicitly motivated three-reaction network under changes of physical rate parameters; these are not simply a normalization or re-derivation of one known orbit. Quantified extinction rates matter for degenerate reaction equilibria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
