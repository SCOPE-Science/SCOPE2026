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

Independently derived the rate conversion theta1=kappa1/kappa3, theta2=kappa1²/(kappa2 kappa3), theta3=kappa2/kappa4 and the positive equilibrium coordinates x=theta1(1-alpha)/2, y=theta2 alpha(1-alpha)/4, z=theta3(2-alpha)/alpha. Direct substitution in the mass-action equations vanishes, and any positive equilibrium forces z>theta3 and alpha in (0,1). Symbolically verified f=4alpha(K(alpha)-K), Kprime=2(g-theta3)/alpha² with g=alpha²[(1-2alpha)theta2-2theta1]/8, the unique maximum g(alpha*)=T and all endpoint inequalities. Hence the one/three/two counts are global, including K<=theta3. Exact symbolic checks verify the cusp K* expression, f_alphaalpha=-2(3alpha theta2+2theta1-theta2) on folds, f_alphaalphaalpha=-6theta2, and the unfolding determinant 32. The physical planar Jacobian on x+y+z=K has trace -kappa1-kappa2-4kappa3*x-kappa4*(y+z)<0 and determinant proportional to theta3-g(alpha), so fold/cusp zero eigenvalues are simple in the transverse direction. A sample theta=(1,4,1/1000) produced two ordered folds K≈0.55753958 and 0.56979709; this finite example is corroboration only, not proof.

## originality

PASS

Best-of-knowledge: Banaji--Feliu explicitly derive the identical cubic and the existence of a three-root regime, and note that a Sturm-algebraic description could be obtained but omit it. The independent contribution is a closed global fixed-(theta1,theta2,theta3) diagram with sharp T and ordered fold K-values. General dual-equation theorems and cusp parametrization may cover a portion of the cusp locus, but available material does not prove they establish this complete fixed-parameter classification. A same-network 2026 follow-up is a material unresolved historical-priority risk, because its full text was inaccessible; no claim of exhaustive priority is made.

## value

PASS

The four-reaction example is a named motivating network for multistationarity and cusp methods, where an earlier paper explicitly omitted its full parameter inequalities. Its fixed-theta total-mass phase diagram is a natural and complete exact classification, not an arbitrary parameter slice: the threshold singles out the cusp, locates both folds, and gives the number of equilibria for every positive conserved total, including degeneracies and excluded K region. This is a bounded but reusable exact semialgebraic structural fact for the same network; no general reaction-network theorem or stability classification is claimed. Its mathematical value depends on the explicit missing classification, not the computational effort alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
