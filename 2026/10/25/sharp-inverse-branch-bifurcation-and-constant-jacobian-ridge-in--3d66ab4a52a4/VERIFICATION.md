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

In log-odds y=log(x/(1−x)), the given two-state map reduces every extended-strip inverse fiber exactly to Φ_A(x)=H, Φ_A=logit(x)−Ax and A=a(1−ckp₁/(1−k)). Differentiating gives Φ'_A=1/[x(1−x)]−A: strictly positive for A<4, a single cubic zero at x=1/2 for A=4, and two folds at x±=(1±sqrt(1−4/A))/2 for A>4. The domain-end limits ±infinity imply global 1/3 inverse counts with two roots on caustics; Φ_4(1/2+u)=−2+(16/3)u³+O(u^5). The difference of fold values is Ar−4 artanh(r), r=sqrt(1−4/A), with cubic-cusp onset (A−4)^(3/2)/3. For A>4, s=kp₁/(1−k)<1/c<1 permits Q*=(1−k)/2+k(p₀+p₁/2) and three real roots all having q=1/2+s(1/2−x) in (0,1); hence physical triple preimages genuinely occur. The exact log-odds determinant is (1−k)[1−A x(1−x)]; it is spatially constant iff A=0, k=1/(1+cp₁), equal to 1−k. Injectivity and change of variables yield zero area for compact *fully* invariant interior sets, while the compactly supported invariant-law Lyapunov sum is log(1−k). Checked the symbolic determinant, critical expansion, and the constructive physical witness against the actual package checker source. None of these statements asserts global chaos or a complete physical inverse census.

## originality

PASS

Metaxas and Sapsis define this population-game map and analyze its equilibria and numerical bifurcation dynamics. Their relevant full text was materially read; its model and parameter conventions are identical, but those sections do not state the exact global 1/3 inverse counts, sharp fold width and physical triple-preimage construction, or unique constant-Jacobian memory rate. General planar endomorphism fold/cusp normal forms are standard and acknowledged; their abstract local classification does not by itself calculate this map's global inverse branches and physical feasibility. Available Resultary hits address other dynamical systems. The object-specific inverse and contraction formulas survive those comparisons. An alternate coordinate conjugacy or earlier map-specific derivation could still cover part of the claim.

## value

PASS

Inverse multiplicity determines whether observed new population and belief states reconstruct prior risk states uniquely. The explicit parameter threshold, exact caustic geometry and nonempty physical triple-preimage region give a structural global classification rather than a generic local cusp observation. The separate memory ridge provides an exact invariant-measure Lyapunov budget and area obstruction that is independent of learning intensity. These are meaningful dynamics and observability facts, with physical and invariance restrictions made explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
