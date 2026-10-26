# Scientific review: fundamental–adjoint sixth moment on \(SU(3)\)

## Correctness — PASS

The statement uses probability Haar measure and unnormalized irreducible characters \(w=\operatorname{tr}(g)\), \(h=|w|^2-1\), orthonormal in \(L^2\). The Weyl constant-term formula specified in `RESULT.md` yields exact moments \(\int h^6=145\), \(\int|w|^2h^4=40\), \(\int|w|^4h^2=13\), \(\int|w|^6=6\), and \(\int w^3h^3=22\). Cubic-center symmetry forbids all other mixed phases in the sixth moment. Subtraction from \(145(|a|^2+|b|^2)^3\) gives an exact deficit. It reduces to the rational function \(R(u)\), whose derivative numerator is an explicitly signed cubic with exactly two positive roots. The first critical point is its unique global minimum, including the boundary limit \(139\); its positive value proves that the only nonzero sharp moment maximizers are pure adjoint. Optimality of stability follows from the explicitly admissible phase-aligned mixed equality family. The second-variation coefficient \(75\) is greater than its globally sharp value. The checker reconstructs all Weyl integrals and polynomial identities by exact arithmetic and tests 600 additional complex pairs. Finite tests are not used to establish the universal theorem.

## Originality — PASS, best-knowledge comparison

Agarwal and Nahmgoong, *Singlets in the tensor product of an arbitrary number of Adjoint representations of SU(3)*, arXiv:2001.10826 (first public 2020-01-23), §3, establish the adjoint tensor-power singlet recurrence and display the known multiplicity \(145\) in degree six. The primary paper was inspected through its publicly accessible full HTML, including the Weyl-integration setup and multiplicity table; its stated theorems and main results do not provide a sharp norm or global quadratic stability coefficient on the mixed two-character space. The present claim explicitly attributes \(145\) to that source. Published-record searches for the specific fundamental–adjoint mixture, mixed sixth moments, adjoint tensors, and sharp \(L^6/L^2\) character inequalities located related abelian character-packet and higher-weight estimates, not statements implying this exact \(SU(3)\) stability inequality or its nontrivial equality family. Generic character identities are background, not a novelty claim. Residual risk: a prior equivalent inequality could be hidden in older representation-theoretic norm literature; independent priority audit has not been performed.

## Value — PASS

The known scalar moment \(145\) by itself does not yield the sharp two-character concentration inequality. The exact mixed sixth moment settles whether introducing the fundamental character can improve concentration, and exhibits an optimal *global* stability correction whose equality occurs at a nonzero mixing ratio. The strict inequality \(\kappa<75\) shows that local Hessian analysis at the maximizer misses the worst perturbation; phase alignment yields a rigid three-direction mixed family. This is a natural sharp stability and representation-interaction fact, not a free parameter substitution or a recomputation of an isolated known table entry.

## Scope and remaining risk

Only the two-character space and one exponent are settled; the constant for the larger fundamental–antifundamental–adjoint span is not asserted. No independent scientific priority determination or external validation has occurred.

Self-review: passed. Independent audit: not yet performed.
