# Self-review

## Correctness
PASS. The claim is derived from exact qubit probabilities. The leading-order six-parameter coefficient is reduced to a completed-square identity, and the explicit representative is expanded one order further. The threshold conclusion uses the source's exact one-sided-efficiency formula. The bundled standard-library checker re-evaluates the exact probability expression at decreasing positive \(\theta\), confirms convergence to \(3/7\), and checks the algebraic leading-coefficient identity. No finite scan is used to justify the infinite limit.

## Originality
PASS. The 2007 primary source reports numerical minimization, a weak-entanglement limit of approximately \(43\%\), and explicitly says that it could not find an analytical expression for the optimal settings. The 2009 qudit paper proves a different dimension-dependent construction and describes the nearby qubit \(0.428\) boundary as strong numerical evidence. Exact-fraction, decimal, source-ID, asymptotic-scaling, and analytic-settings searches did not locate the same constructive theorem. The main residual risk is an obscure or poorly indexed later derivation.

## Value
PASS. A closed qubit family with exact limiting threshold \(3/7\) turns a longstanding numerical benchmark into a transparent asymptotic construction. The completed-square classification explains why the constant arises inside the scaling suggested by the numerical optimizer and gives a reusable target for stronger global analysis.

The closest literature and limitations are recorded explicitly: no global qubit optimality, arbitrary-scaling lower bound, noisy-detector extension, or proof of the later dimension-witness conjecture is claimed.

Self-review: passed. Independent audit: not yet performed.
