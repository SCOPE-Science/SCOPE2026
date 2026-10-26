# Review

## Correctness — PASS

The exact scalar derivatives determine the branch ratio \((p-1)|x|^{(p-3)/2}\). For \(p=3\), the branch conditions and radius comparison give the stated three exact contraction factors. For \(p>3\), the middle branch is selected, the unconstrained step-to-radius ratio tends to \(4\), and the boundary recurrence yields \(|x_k|^{-s}\sim s k/(4\rho_{\min})\) with \(s=(p-3)/2\). The parameter floor is reached because the first inner-loop trial satisfies the source's acceptance condition locally. The script checks finite examples only; the proof is analytic.

## Originality — PASS

The primary source's Theorem 4.3 establishes quadratic convergence under a non-degenerate local-optimum assumption and does not cover the power minima with \(f_p''(0)=0\). published-finding corpus semantic searches returned nearby analyses of other methods, but no direct match for the Strategy 4.1 branch classification or its \(p>3\) asymptotic constant. The comparison is based on statements and update rules, not title similarity. Search is not exhaustive; an equivalent result may exist in unqueried literature.

## Value — PASS

Degenerate minima are precisely outside the non-degenerate hypothesis behind the source's quadratic local-convergence result. The exact threshold at \(p=3\), including the dependence on the parameter floor, and the polynomial rate for \(p>3\) quantify how the method behaves when that hypothesis fails. The leading constant gives a concrete diagnostic for flat minima rather than a mere numerical observation.

## Closest literature and limitations

The closest primary source is Jiang et al., arXiv:2311.11489v1, Algorithm 3, Strategy 4.1, and Theorem 4.3. Mishchenko's regularized Newton method and Doikov–Nesterov's Bregman-regularized Newton method use different update rules and strong-convexity assumptions; they are adjacent but do not imply the claimed UTR recurrence as stated. The claim is one-dimensional and local, assumes exact subproblem solves, and describes the pre-termination limit as tolerance decreases.

Self-review: passed. Independent audit: not yet performed.
