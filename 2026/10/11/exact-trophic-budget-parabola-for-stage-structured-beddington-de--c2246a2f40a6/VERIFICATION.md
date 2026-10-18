---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Set predation F=axz/(1+bx+cz) and Φ=x+y/k1+(α+d1)z/(α k1). Substitution cancels -F +F and -(α+d1)y/k1+(α+d1)y/k1 exactly, leaving dΦ/dt = r x(1−x/k) − C z, C=(α+d1)d2/(α k1). For any compactly supported invariant probability in the nonnegative octant, boundedness of the generator on its support justifies ∫dΦ/dt dμ=0. Completing square yields ∫(x−k/2)²+(kC/r)mean z=k²/4 and equivalent Var x + (kC/r)mean z = mean x(k−mean x). Since z≥0, max mean z=rk/(4C); equality puts invariant support inside plane x=k/2. Tangency x′=0 on that plane fixes z uniquely by strict monotonicity of F in z≥0, then invariance and z′=0 fixes y, proving support consists of one equilibrium. Consequently every non-equilibrium invariant ergodic recurrent state has strict inequality. Independent SymPy cancellation and exact parameter values checked: C=9/10, kC/r=27/4, ceiling=100/3. No existence or stability of periodic states assumed.

## originality

PASS

The full original Feng–Jiang model paper investigates bifurcations and periodic-orbit multiplicity, while Khajanchi 2014 uses S=k1 x+y+z for dissipative bounds. The latter cancellation retains juvenile/mature mortality terms and gives no exact stationary parabola. The tuned Φ cancels the juvenile term as well and, after invariant-measure integration, establishes a response-independent mature predator ceiling and equality rigidity. Related mean-variance laws in different ecological systems have no implication for the exact nine-parameter stage-structured system.

## value

PASS

Feng–Jiang study coexisting limit cycles where orbit averages are mathematically meaningful but nonlinear period computation is difficult. A universally exact, response-independent relation between prey fluctuation variance and mature-predator mean, plus its sharp algebraic cap and rigid equality case, constrains every possible compact recurrent state without solving bifurcation dynamics. The weighted trophic content is physically motivated by cancellation of within-population transfers; its exact budget is an independently useful stationary law, even though deriving it uses elementary algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
