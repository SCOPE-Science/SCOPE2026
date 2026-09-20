# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Direct differentiation gives
\[
\dot A=y^2-bz(z-\rho),\qquad
\dot B=(x^2-bz)^2-2ay^2
\]
for the stated polynomials. Exact symbolic verification reproduces both identities with zero residual. Invariance of a compactly supported probability measure justifies integration of Lie derivatives. Testing functions of z alone yields \(\mathbb E[x^2\mid z]=bz\), so \(z\ge0\) almost surely. The equality case is rigid: zero \(y\)-energy plus the second balance gives \(y=0\) and \(x^2=bz\) almost surely; invariance then forces \(x(\rho-z)=0\), leaving only the three equilibria. Therefore every non-equilibrium invariant measure has strictly positive \(\int z(z-\rho)d\mu\), which can occur with \(z\ge0\) only if positive mass lies above \(z=\rho\). The conditional amplitude law then forces positive mass with \(x^2>b\rho\), giving a second barrier at the nonzero-equilibrium amplitude. The periodic-orbit conclusions follow by applying the invariant-measure theorem to normalized time measure on the orbit.

The proof was stress-tested at all three equilibria, where both dissipative balances vanish, and against the limiting possibility of a measure concentrated in \(0\le z\le\rho\), which the equality classification correctly reduces to equilibrium support. The theorem does not infer pointwise convergence from invariant-measure information.

## Originality

**PASS, to the best of our knowledge.** The original Shimizu–Morioka work concerns limit-cycle bifurcation. Shilnikov's classical treatment develops the bifurcation, homoclinic, periodic-orbit, and Lorenz-attractor structure. Dias–Mello and Liu–Gao study local Hopf cycles in the Rucklidge and Shimizu–Morioka formulations; Messias–Gouveia–Pessoa study compactified dynamics at infinity and special global structures. Rucklidge gives the equivalent double-convection formulation, and later work studies analytic/Darboux/meromorphic integrability and invariant algebraic manifolds. Rigorous and recent literature establishes Lorenz attractors, heteroclinic connections, and detailed attractor-boundary bifurcations.

No checked source states the paired stationary identities, their conditional-variance consequence, the equilibrium-only equality classification, or the resulting invariant-measure barriers requiring non-equilibrium recurrent dynamics to cross both the nonzero-equilibrium height and amplitude. Exact and synonymous searches were also made under the equivalent Rucklidge formulation and under moment, time-average, invariant-measure, and periodic-orbit terminology.

Residual risk remains because the complete theorem-level text of several especially relevant sources was not fully inspected: Shimizu–Morioka (1980), Lima–Llibre–Valls on Rucklidge integrability (2014), Huang–Shi–Li on Shimizu–Morioka integrability (2020), and Demina–Ilyukhin on Rucklidge invariant algebraic manifolds (2023). Their accessible descriptions concern different questions, but a short equivalent balance identity could have appeared without being indexed. The originality claim is therefore deliberately limited to “to the best of our knowledge.”

## Value

**PASS.** The result constrains every compact recurrent statistical state, rather than one numerically observed attractor or one local bifurcation branch. It yields two global geometric obstructions—non-equilibrium recurrence must cross the nonzero-equilibrium height and exceed the nonzero-equilibrium amplitude—together with an exact derivative-energy ratio for every periodic orbit and quantitative stationary fluctuation identities. Retaining \(\rho\) makes the statement apply directly to the standard Rucklidge formulation as well as the normalized Shimizu–Morioka system.

## Scientific limitations

The balances are necessary conditions, not existence or uniqueness results for recurrent sets. They do not determine which parameter values admit periodic or chaotic dynamics. Compact invariant sets that support only equilibrium measures are not classified. The positivity interpretation uses \(a,b,\rho>0\). The conditional law \(\mathbb E[x^2\mid z]=bz\), considered alone, is an elementary consequence of stationarity of the z-equation and is not claimed as a standalone novelty.
