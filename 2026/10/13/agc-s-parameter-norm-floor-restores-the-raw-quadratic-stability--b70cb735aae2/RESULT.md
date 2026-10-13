# AGC's parameter-norm floor restores the raw quadratic stability ceiling
## Finding

Adaptive Gradient Clipping (AGC) clips each unit by comparing its gradient norm with its parameter norm, but replaces a small parameter norm by a positive floor. On a scalar quadratic this produces an exact three-zone map, and the floor has a sharp dynamical consequence.

Let
\[
f(x)=\frac h2x^2,
\qquad
h>\lambda>0,
\]
where \(h\) is the quadratic curvature and \(\lambda\) is the AGC clipping parameter. Let
\[
\epsilon>0
\]
be the parameter-norm floor and let
\[
x^+
=
x-\eta\widetilde g(x),
\qquad
\eta>0.
\]

For one scalar unit, the source rule is
\[
\widetilde g(x)
=
\begin{cases}
\displaystyle
\lambda
\frac{\max\{|x|,\epsilon\}}{|hx|}
hx,
&
\displaystyle
\frac{|hx|}{\max\{|x|,\epsilon\}}>\lambda,
\\[6pt]
hx,
&
\text{otherwise}.
\end{cases}
\]
Define
\[
a=\frac{\lambda\epsilon}{h}.
\]
Because
\[
h>\lambda,
\]
one has
\[
0<a<\epsilon.
\]
The clipped gradient is exactly
\[
\boxed{
\widetilde g(x)
=
\begin{cases}
hx,& |x|\le a,\\
\lambda\epsilon\,\operatorname{sign}(x),& a<|x|<\epsilon,\\
\lambda x,& |x|\ge\epsilon.
\end{cases}
}
\]
The formulas agree at both boundaries.

For every positive floor,
\[
\boxed{
x_t\to0\ \text{for every initial value}
\iff
0<\eta h<2.
}
\]
Thus AGC's outer regime can cap the effective curvature at \(\lambda\), yet the parameter-norm floor restores the raw curvature \(h\) as the exact universal asymptotic stability threshold.

The gap between the two thresholds contains explicit nonconvergent dynamics. For
\[
\frac2h\le\eta\le\frac2\lambda,
\]
put
\[
s=\eta\lambda\epsilon.
\]
Every positive
\[
x\in
I_\eta
:=
\left[
\max\{a,s-\epsilon\},
\,
\min\{\epsilon,s-a\}
\right]
\]
generates the exact period-two orbit
\[
\boxed{
x\longmapsto x-s\longmapsto x.
}
\]
The interval \(I_\eta\) is nonempty exactly throughout the displayed range. At
\[
\eta=\frac2h
\]
it collapses to the single positive phase \(x=a\), and at
\[
\eta=\frac2\lambda
\]
it collapses to \(x=\epsilon\). For
\[
\frac2h<\eta<\frac2\lambda,
\]
it has positive length, so AGC has a continuum of exact bounded two-cycles.

If
\[
\eta>\frac2\lambda,
\]
then every sufficiently large initialization lies in the outer regime and has
\[
|x_{t+1}|
=
|1-\eta\lambda|\,|x_t|,
\]
with multiplier greater than one. Such trajectories diverge geometrically.

There is a singular floor limit. If one formally sets
\[
\epsilon=0
\]
and fixes \(x=0\), then every nonzero point is in the relative-clipping regime:
\[
\widetilde g(x)=\lambda x.
\]
The floorless map is therefore globally convergent exactly when
\[
0<\eta\lambda<2.
\]
Consequently, introducing any positive floor changes the universal scalar stability ceiling discontinuously from
\[
\frac2\lambda
\]
to
\[
\frac2h.
\]

## Assumptions and scope

The result concerns one scalar AGC unit and plain gradient descent after clipping. Momentum, weight decay, minibatch noise, and vector-valued coupling are not included.

The curvature satisfies
\[
h>\lambda.
\]
When
\[
h\le\lambda,
\]
AGC does not clip this scalar quadratic away from the norm-floor transition in the same way, so the stated phase diagram is not the relevant one.

The source uses a positive norm floor to avoid suppressing gradients of zero-initialized parameters. The formal \(\epsilon=0\) rule is used only as a mathematical comparison that isolates the effect of that floor.

The theorem gives universal scalar convergence and explicit period-two orbits. It does not claim that every nonconvergent initial condition in the intermediate regime approaches one of those cycles.

## Proof

For the scalar quadratic,
\[
g(x)=hx.
\]
AGC tests
\[
\frac{h|x|}{\max\{|x|,\epsilon\}}>\lambda.
\]

If
\[
|x|\ge\epsilon,
\]
this ratio is \(h>\lambda\), so clipping is active and
\[
\widetilde g(x)=\lambda x.
\]

If
\[
|x|<\epsilon,
\]
the test becomes
\[
h|x|>\lambda\epsilon,
\]
or equivalently
\[
|x|>a.
\]
Thus the middle band has constant clipped magnitude \(\lambda\epsilon\), while the innermost band uses the raw gradient. This proves the three-zone formula.

Assume first that
\[
0<\eta h<2.
\]
Since
\[
\lambda<h,
\]
also
\[
0<\eta\lambda<2.
\]
In the inner regime,
\[
|x^+|
=
|1-\eta h|\,|x|
<
|x|.
\]
In the outer regime,
\[
|x^+|
=
|1-\eta\lambda|\,|x|
<
|x|.
\]
In the middle regime,
\[
x^+=x-s\,\operatorname{sign}(x),
\qquad
s=\eta\lambda\epsilon.
\]
The hypothesis gives
\[
s<2\frac{\lambda\epsilon}{h}=2a<2|x|,
\]
hence again
\[
|x^+|<|x|.
\]
Therefore the magnitude decreases strictly at every nonzero point. The induced magnitude map is continuous, so its decreasing sequence cannot converge to a positive fixed magnitude. Hence
\[
x_t\to0.
\]

Conversely, at
\[
\eta=\frac2h
\]
the boundary point \(a\) satisfies
\[
a\mapsto-a\mapsto a,
\]
so global convergence fails. If
\[
\frac2h<\eta\le\frac2\lambda,
\]
the period-two construction below gives a nonzero orbit. If
\[
\eta>\frac2\lambda,
\]
the outer multiplier has magnitude greater than one, giving divergent initial conditions. This proves the if-and-only-if global threshold.

For the two-cycle family, a positive middle-band phase \(x\) maps to
\[
x-s.
\]
It returns in one more step exactly when the negative phase has magnitude
\[
s-x
\]
in the same closed floor band
\[
[a,\epsilon].
\]
Thus both phases are admissible precisely when
\[
a\le x\le\epsilon
\]
and
\[
a\le s-x\le\epsilon.
\]
Their intersection is exactly
\[
I_\eta
=
[\max\{a,s-\epsilon\},\,\min\{\epsilon,s-a\}].
\]
This interval is nonempty exactly for
\[
2a\le s\le2\epsilon,
\]
equivalent to
\[
\frac2h\le\eta\le\frac2\lambda.
\]
Strict inequalities give positive interval length.

Finally, when
\[
\epsilon=0,
\]
every nonzero point has AGC ratio \(h\), so clipping is always active and
\[
\widetilde g(x)=\lambda x.
\]
The floorless stability statement follows from the scalar linear multiplier
\[
1-\eta\lambda.
\]

## Verification

The accompanying `verify.py` reconstructs the source scalar AGC rule directly.

It checks the exact three-zone formula over randomized parameters, strict magnitude contraction below the raw-curvature threshold, the two-cycle interval throughout the intermediate regime, both endpoint cycles, outer-regime divergence above the clipped-curvature threshold, and the floorless comparison.

The executable checks are transcription guards. The global threshold and cycle interval are proved analytically above.

## Relationship to prior work

Brock, De, Smith, and Simonyan introduce AGC by clipping each unit when the ratio of gradient norm to a floored parameter norm exceeds \(\lambda\). They define the floor
\[
\max\{\|W_i\|,\epsilon\}
\]
with default
\[
\epsilon=10^{-3},
\]
specifically to prevent zero-initialized parameters from having gradients clipped to zero. They motivate AGC by controlling relative parameter updates and report that it enables stable training at larger batch sizes and learning rates.

The defining source interprets AGC as a relaxation of normalized optimizers: it imposes a maximum relative update size without completely discarding gradient magnitude. Its analysis and experiments do not state the scalar three-zone map above, the discontinuous change in the universal stability ceiling caused by a positive norm floor, or the exact intermediate two-cycle band.

General deterministic gradient-clipping theory studies fixed clipping radii and proves convergence under suitable step-size conditions. That theory explains why ordinary clipping eventually becomes inactive near a critical point, but it does not analyze AGC's parameter-relative threshold with a positive parameter-norm floor.

Focused searches for AGC norm-floor stability, scalar quadratic dynamics, period-two behavior, and floor-induced threshold changes did not identify an implication-equivalent published result.

## Limitations

The finding is deliberately scalar and deterministic.

The exact two-cycle band uses the source's parameter-norm floor but not momentum or the complete NFNet training stack.

The formal floorless comparison is not a recommendation to remove the numerical safeguard; it isolates the safeguard's dynamical effect.

The result concerns asymptotic convergence of the scalar iterate, not finite-step neural-network loss stability.

## References

1. Andrew Brock, Soham De, Samuel L. Smith, and Karen Simonyan, “High-Performance Large-Scale Image Recognition Without Normalization,” arXiv:2102.06171v1, 2021.
2. Jingzhao Zhang, Tianxing He, Suvrit Sra, and Ali Jadbabaie, “Why Gradient Clipping Accelerates Training: A Theoretical Justification for Adaptivity,” arXiv:1905.11881v1, 2019.
3. Anastasia Koloskova, Hadrien Hendrikx, and Sebastian U. Stich, “Revisiting Gradient Clipping: Stochastic Bias and Tight Convergence Guarantees,” arXiv:2305.01588v1, 2023.
