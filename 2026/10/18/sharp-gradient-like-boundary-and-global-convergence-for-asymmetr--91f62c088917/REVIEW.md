# Self-review

## Correctness — PASS

The map is precisely a weighted gradient ascent \(X\mapsto X+D\nabla V(X)\) with \(D=\operatorname{diag}(1-c,1)\), which becomes unit-step Euclidean gradient ascent after the diagonal coordinate transform. Direct trigonometric differentiation proves the identity and the global Hessian lower bound \(\nabla^2W\succeq-[a+(2-c)b]I\). The integral second-order Taylor formula then gives strict increase for parameters below the closed threshold; at equality the only possible Hessian-bound saturation would be at a half-integer diagonal fixed point where the gradient is zero, so the inequality remains strict at every nonfixed state. The fixed-point equations reduce to a cosine law and yield four or six points per cell, with exact strict inequalities for the additional pair. Compactness, strict ascent and connectedness of the omega limit set imply convergence of every torus orbit to one fixed point; small limiting step sizes make the lifted real-plane orbit converge to a single fixed lift. The counterdirection after the potential threshold uses the exact Hessian eigenvalue \(-[a+(2-c)b]\) at the half-integer diagonal point; it proves only failure of this potential's ascent property. The packaged symbolic checker reproduced three identities and 7,656 seeded finite diagnostics passed. The universal assertions rest on proof, not numerics.

## Originality — PASS with residual risk

The accessible complete author-upload text of Soula, Taha, Fournier-Prunaret and Hamri (2022, DOI 10.11648/j.acm.20221101.12) defines the same three-parameter map and studies local bifurcation, period-two phenomena, synchronization, basins and numerical diagrams, rather than a global all-initial-state gradient-like boundary, its neutral endpoint, or a complete finite fixed-set classification derived from that boundary. Hamri and Soula (2010) treat a symmetric predecessor's critical curves and basins but do not provide the claimed asymmetric theorem. Maistrenko, Maistrenko and Mosekilde (2005, DOI 10.1142/S0218127405013320) is an important related same-family paper; only its abstract/publisher preview was accessible, so it cannot be declared not covering the theorem. Actual targeted published-record and semantic mathematical-result searches returned no statement logically implying the complete global claim. The gradient ascent/descent-lemma principle is established prior theory, so only its specific application and exact global region are asserted here. Residual priority risk includes unexamined sections of the inaccessible 2005 source and potentially unindexed equivalences.

## Mathematical value — PASS

The motivating paper's parameter diagrams and bifurcations leave a natural global question: on what explicit region is complex recurrence impossible from every starting state? The answer gives a closed parameter region and a rigorous monotonicity obstruction to cycles or chaotic recurrence. The half-integer neutral boundary is included rather than omitted, and an exact four-versus-six fixed-point census describes the finite possible limiting set. The boundary is quantitatively sharp for the displayed natural weighted-gradient potential. These are model-specific structural facts, not merely computational correctness or an arbitrary numerical slice.

## Limitations and closest literature

The convergence conclusion is not asserted for all parameters beyond the potential threshold; no basin-size formula or convergence-rate theorem is established. The 2005 predecessor was not available in complete full text and is a meaningful priority uncertainty. Independent mathematical validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
