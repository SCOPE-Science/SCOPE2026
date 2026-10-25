# Scientific review: characteristic-three Igusa cone and nodal K3 zeta

## Correctness — PASS
The six-coordinate quartic translation invariance follows from the characteristic-three power-sum identities. Its complete geometric singular locus is obtained by solving the cubic gradient condition, not by finite-field sampling. The resulting fifteen three-pair directions give all nodes of the quartic base; the Hessian form has radical only in the projective radial direction, so each has ordinary-double-point type in characteristic three. This also proves geometric integrality and normality. The crepant resolution is K3. Exact enumerations of every projective point over \(\mathbb F_3\) and \(\mathbb F_9\) give \(25\) and \(145\) base points. Replacing fifteen rational nodes with exceptional conics gives resolution counts \(70\) and \(280\). The Weil bound plus equality for the squared eigenvalues establishes the zeta function for every extension degree. The executable finite checker is `check_igusa.py`.

## Originality — PASS, subject to historical coverage risk
Hulek--Sankaran, arXiv:math/9810153, Section IV.1, give the complex symmetric Igusa quartic and fifteen singular lines. Rito, arXiv:1310.4071, Section 2, explicitly gives the five-coordinate fifteen-nodal quartic over \(\mathbb C\). Neither published description states the characteristic-three cone degeneration or the resolved characteristic-three K3 Frobenius eigenvalues. The finite-field zeta claim is not implied by classical nodal counts. Searches included characteristic-three Igusa cone, fifteen-node reduction, arithmetic point counts, duality, and known K3 supersingularity. Similar surface singularity classifications in other classical models have no implication for this explicit zeta calculation. The residual risk is an earlier equivalent modular/K3 calculation under another model or coordinate normalization.

## Mathematical value — PASS
The theorem gives a complete and arithmetically explicit exceptional-prime degeneration of a classical modular quartic threefold: the singular boundary becomes a star over a fifteen-nodal K3 model, and its minimal resolution has a maximally constrained Frobenius spectrum. Unlike merely recounting known singular lines, the exact zeta function governs the point counts over **every** finite extension and determines supersingularity. The result is mathematically natural and can inform comparisons of models, reductions and arithmetic K3 geometry.

## Limitations and prior comparisons
No claim is made about the characteristic-three modular interpretation, the full nonreduced Jacobian scheme at the vertex, or the Artin invariant. The completed original literature survey may omit modular descriptions under alternative coordinates; no independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
