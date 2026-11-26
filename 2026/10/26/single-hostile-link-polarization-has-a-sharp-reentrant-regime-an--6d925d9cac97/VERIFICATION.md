---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the signed Laplacian convention at issue a hostile edge contributes t(e_i+e_j)(e_i+e_j)^T. Write G=H^{-1}, v=Gu and z_0=Gs. The positive connected base gives G>0 entrywise: factor H as D−A with D equal to one plus friendly weighted degree, then sum the Neumann series for D^{-1}A, whose row sums are below one and whose positive paths reach all vertices. Thus c=u^Tz_0, d=v^Tz_0, r=u^Tv and e=v^Tv are positive for the nonzero nonnegative s. Sherman–Morrison gives z=z_0−tcv/(1+tr). Differentiating the neutral-zero squared norm divided by n gives 2c[t(ce−rd)−d]/[n(1+tr)^3]. Its affine numerator starts negative and crosses once exactly when ce−rd>0; equality of ce and rd still gives strict decrease at every finite strength. Independent exact symbolic elimination reproduced the determinant 3ab+2a+2b+1 and the weighted three-path coefficients (−Δ,−2B,Δ) divided by its square, with Δ=(a−b)(2ab−1) and B=a²b+ab²+4ab+a+b. At a=b=1 this is −s_1/4. A connected simple graph on two vertices has no eligible link, and the only eligible three-vertex shape is a path. Independently solving the concrete matrices gives z_3=(3−5t,4−2t,11+5t)/[2(9+13t)] and z_4=(24+11t,8−t,4−11t,4−4t)/(40+51t). Their squared norms reproduce both derivatives, turning strengths 23 and 944/13, minima 7/264 and 173/6952, zero-strength values 73/486 and 21/200, and limits 9/338 and 259/10404. The four-vertex example has four unit friendly links and one variable-strength hostile link, not five unit links at the minimizing strength. Scaling s extends the sign result beyond the explicit [0,1] normalization to nonzero s≥0. The bundled checker and recorded output were inspected; the submitted checker was not executed.

## originality

PASS

Best of current knowledge: the distinctive result is the one-hostile-nonedge strength classification with the explicit weighted three-path regime and sharp boundary of four vertices for unit friendly weights. The FJ model, neutral-zero polarization convention and rank-one inverse technique are prior ingredients.

## value

PASS

For a standard signed equilibrium measure, knowing the initial slope is insufficient to predict the large-strength response. The exact weighted path criterion, explicit witnesses and sharp friendly-unit order distinguish the effect of unequal weights from the minimal graph size in the unit base. The finding is useful as a boundary and counterexample to universal monotonicity, without attributing novelty to the standard rank-one calculation or claiming an equilibrium bifurcation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
