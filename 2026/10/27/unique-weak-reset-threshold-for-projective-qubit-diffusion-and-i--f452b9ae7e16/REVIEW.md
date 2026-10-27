# Scientific assessment: unique weak-reset threshold for projective qubit diffusion

## Correctness — PASS

The claim specifies the radial projective diffusion generator, absorbing fidelity cap, initial condition, independent Poisson reset law and complete parameter range. The moment boundary equations \(\mathcal Lm=-1\), \(\mathcal Lq=-2m\) are directly satisfied by the stated logarithm/dilogarithm forms. Renewal gives the derivative \(M'(0+)=[m^2-v]/2\), whose exact sign is a single elementary function \(\Phi_b\). Its derivative is unimodal because \(-\log y/(1-y)-1\) decreases strictly, whereas \(\log[y/(1-b)]\) increases; both endpoints have the required signs. The two expansions follow respectively by analytic implicit-function and a uniform large-logarithm expansion. The reproduction program produced 178 corroborating checks, including an independent hypergeometric Laplace-transform calculation. Those checks are not presented as exhaustive proofs.

## Originality — PASS (best-knowledge)

The 2026 source paper gives projective Brownian diffusion and first-passage observables, not the reset-benefit threshold. The general coefficient-of-variation criterion and generic Jacobi first-passage moment formulas are prior results that imply the weak reset sign **once specialized moments are known**, but do not state the unique projective geometric threshold or derive both endpoint expansions. The nearest bounded-geometry restart comparison concerns diffusion *inside* a Euclidean ball, not on the Bloch sphere; its \(b/3\) local two-dimensional limit is consistent with but does not dominate the full projective curve. Searches of equivalent spherical, Jacobi, qubit, fidelity, renewal and dilogarithmic formulations found no stated complete threshold. Residual risk remains from potentially unlocated spherical-Brownian literature; the available checks do not prove universal priority.

## Value — PASS

The question is motivated by the explicit quantum-state Brownian fidelity first-passage model and by the physical choice whether rare state resets help prepare a high-fidelity target. The precise switching initial fidelity is not just a restatement of a generic renewal formula. A global single-threshold classification and the nonflat high-fidelity limit \(1-e^{-1}\), with a quantified inverse-logarithmic approach, identify two geometrically distinct regimes. This is a nontrivial necessary-and-sufficient weak-reset criterion, not a claim of optimal finite-rate control.

## Closest results and boundaries

Tóth 2026: source diffusion and mean first-passage, no cap-dependent Poisson reset switch. D'Onofrio–Tamborrino–Lansky 2018: general Jacobi moment theory, not the exact projective switching curve. Pal–Reuveni 2017: known generic reset criterion. Chen–Huang 2022: Brownian inside a Euclidean ball, not Brownian on a spherical surface. Possible stronger prior spherical results remain a literature risk. The result applies to the isotropic pure-qubit model and weak-rate sign only.

Self-review: passed. Independent audit: not yet performed.
