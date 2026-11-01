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

For SPD S and symmetric planar A the transformed-set Gaussian change-of-variables gives H_epsilon = Var_mu(<ASy,y>) - E_mu(<(A^2 S+ASA)y,y>). For rectangles [-1/epsilon,1/epsilon] x [-epsilon,epsilon] in any orthogonal frame, symmetric transverse integration and a uniform Gaussian majorant bound all relevant normalized second/fourth moments by their Gaussian-line limits with O(epsilon^2) error uniformly over compact unit directions. If alpha=<Su,u>, beta=<ASu,u>, zeta=<(A^2S+ASA)u,u>, then H0=(2 beta^2-alpha zeta)/alpha^2. Orthogonal diagonalization A=diag(a,b) reduces the quartic numerator to -(a-b)^2xy[c(px^2+qy^2)+2pqxy]; with r=c/sqrt(pq), w=2sqrt(pq)xy/(px^2+qy^2)=sin 2phi this equals -(a-b)^2 w(w+r)/(2(1+rw)^2). The exact square identity implies sharp maximum (a-b)^2r^2/[8(1-r^2)] = ||AS-SA||_F^2/(16 det S), realized at w=-r/(2-r^2); for nonzero commutator w lies strictly interior, giving precisely two projective axes. The positivity region w(w+r)<0 has total transformed-angle length arcsin|r|. For r=0 or a=b, maximum zero, with no unsupported uniqueness claim. Independent symbolic expansion verified both polynomial identities. Independent finite checks covered 84 independently generated SPD/symmetric matrix pairs, 125 directions each (maximum residual 4.45e-14), and three direct finite-width Gaussian quadratures approaching the exact 1/6 instance (0.141407,0.155503,0.161696). Finite experiments are not a proof of the uniform error; the Gaussian dominated symmetric-Taylor argument supplies it.

## originality

PASS

Best-of-knowledge PASS for the exact quantitative planar optimization, with explicit dependence on preceding Gaussian second-variation work. Kalantzopoulos (arXiv:2610.07248v1) proves the directionwise sign/commutator equivalence in all dimensions and evaluates one planar example, but does not give the universally optimized commutator quotient, full maximizing-axis set, or transformed-angle measure. Cordero-Erausquin and Rotem (2020) supply a Gaussian strong-(B) failure mechanism. Full text of Putterman (2026) was inaccessible even after same-paper arXiv and lawful-open attempts followed by authorized institutional retrieval; its abstract addresses positive near-equality covariance stability, not the negative-curvature orientation maximum. The maximization is an elementary yet motivated rational optimization of previous explicit formulas, not an independent invention of the derivative method. Search failure cannot prove priority.

## value

PASS

The central question after the qualitative noncommutativity theorem is how large the strongest failure of Gaussian logarithmic curvature can be when rectangle directions vary. The exact invariant ||[A,S]||_F^2/(16 det S), optimal-axis rigidity, sum-of-squares angular deficit and full transformed-angle instability measure answer that natural quantitative problem for every symmetric planar generator and SPD covariance. A future researcher comparing strength of covariance anisotropy, the rate of strong-(B) failure or optimal witness directions can use these precise quantities, which are not mere arbitrary point values. The derivation is short and dependent on previous work, but the exact sharp universal continuous classification is an independently meaningful statement. No assertion of a wider convex-body theorem or paper-sized breakthrough.

The dated certificate retains the supplied scientific assessment, sources and limitations.
