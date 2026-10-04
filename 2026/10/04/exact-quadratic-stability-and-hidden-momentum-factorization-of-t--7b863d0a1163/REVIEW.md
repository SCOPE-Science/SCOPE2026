# Review

## Correctness

PASS. The printed recurrence produces a four-state linear map on each quadratic eigendirection. Direct determinant expansion factors its characteristic polynomial into \(z(z-\beta)\) and a monic quadratic with root product \(q_\lambda=\beta+(1-\beta)\kappa\lambda\). The complete quadratic Jury conditions reduce exactly to \(\kappa\lambda<1\) and \(0<\eta\lambda<2(1+q_\lambda)\). The spectral-interval reduction is monotone at the top curvature. The optimal scalar factor follows from the active-root product and discriminant, with the passive roots strictly below the resulting \(\sqrt{q_\lambda}\) floor.

The package includes an independent reconstruction of the modal matrix and determinant comparison to guard against transcription errors.

## Originality

PASS. The defining paper supplies the recurrence, control interpretation, tuning heuristic, and qualitative fragility warning, but not the exact discrete SPD-quadratic factorization or Schur region. The later follow-up proposes a different complete PID construction and discusses derivative-noise control, not this exact phase diagram. The source-associated implementation is algebraically different and was therefore not conflated with the paper equation.

Focused semantic searches over PID/ID optimization, gradient-difference momentum, scalar quadratic stability, characteristic polynomials, and derivative-gain boundaries returned adjacent heavy-ball and quadratic-stability results but no statement implying the complete claim. A residual risk remains for equivalent older control-theoretic state coordinates.

## Value

PASS. The source paper motivates derivative feedback as a way to reduce overshoot while also observing fragility when its gain is too large. The factorization gives a sharp structural explanation: derivative feedback can expand the stable stepsize ceiling toward \(4/L\), but the same gain raises \(q_\lambda\) and therefore worsens the best attainable scalar asymptotic factor. The result is a motivated stability-versus-rate law for the published method, not an arbitrary parameter computation.

Same-model review: passed. Independent audit: not yet performed.
