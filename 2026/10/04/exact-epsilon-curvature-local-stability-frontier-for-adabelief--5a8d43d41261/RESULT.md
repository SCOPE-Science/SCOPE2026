# Exact epsilon-curvature local stability frontier for AdaBelief
## Finding

Consider the deterministic scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,\qquad \lambda>0,
\]
and unrectified AdaBelief with the update convention in its defining paper:
\[
g_t=\lambda x_{t-1},
\]
\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\]
\[
s_t=\beta_2s_{t-1}+(1-\beta_2)(g_t-m_t)^2+\varepsilon.
\]
The bias-corrected implementation uses
\[
\widehat m_t=\frac{m_t}{1-\beta_1^t},\qquad
\widehat s_t=\frac{s_t}{1-\beta_2^t},
\]
and
\[
x_t=x_{t-1}-\alpha\frac{\widehat m_t}{\sqrt{\widehat s_t}+\varepsilon}.
\]

Assume
\[
0\le\beta_1,\beta_2<1,\qquad \alpha>0,\qquad \varepsilon>0.
\]
The defining paper explicitly omits bias correction in its theoretical analysis. For that autonomous recurrence, the optimum fixed point is
\[
(x_\star,m_\star,s_\star)
=
\left(0,0,\frac{\varepsilon}{1-\beta_2}\right).
\]
Define
\[
D_\varepsilon
=
\sqrt{\frac{\varepsilon}{1-\beta_2}}+\varepsilon,
\qquad
\chi=\frac{\alpha\lambda}{D_\varepsilon}.
\]
Then the fixed point is locally exponentially stable exactly when
\[
0<\chi<
\frac{2(1+\beta_1)}{1-\beta_1}.
\]
Equivalently,
\[
\lambda<
\lambda_c
=
\frac{2(1+\beta_1)}{1-\beta_1}
\frac{\sqrt{\varepsilon/(1-\beta_2)}+\varepsilon}{\alpha}.
\]

The local eigenvalues are \(\beta_2\) and the two roots of
\[
r^2-
\left[1+\beta_1-(1-\beta_1)\chi\right]r
+\beta_1=0.
\]
At the upper stability boundary these roots are
\[
-1\quad\text{and}\quad-\beta_1,
\]
so the boundary is sharp.

For \(0<\beta_1<1\), the optimization roots form a complex-conjugate pair precisely for
\[
\frac{1-\sqrt{\beta_1}}{1+\sqrt{\beta_1}}
<
\chi
<
\frac{1+\sqrt{\beta_1}}{1-\sqrt{\beta_1}}.
\]
Throughout this interval their common modulus is exactly
\[
\sqrt{\beta_1}.
\]
Thus there is a broad local rate plateau: changing curvature, learning rate, or epsilon changes the oscillation angle while leaving the optimization-block contraction modulus fixed.

The source's bias-corrected algorithm has the same strict asymptotic local frontier. Along the optimum reference orbit, starting from \(s_0=0\),
\[
s_t=\frac{\varepsilon(1-\beta_2^t)}{1-\beta_2},
\]
and therefore
\[
\widehat s_t=\frac{\varepsilon}{1-\beta_2}
\]
for every positive \(t\). The time-dependent local Jacobian differs from the autonomous one only through the first-moment factor \(1-\beta_1^t\), so it converges exponentially to the same limiting Jacobian.

For the common paper settings
\[
\beta_1=0.9,\qquad
\beta_2=0.999,\qquad
\alpha=10^{-3},
\]
the exact curvature ceiling is approximately
\[
120.166931
\]
at
\[
\varepsilon=10^{-8},
\]
but only
\[
0.012016655
\]
at
\[
\varepsilon=10^{-16}.
\]
The source placement of epsilon therefore makes it a genuine local curvature-stability parameter, not merely a divide-by-zero safeguard.

## Assumptions and scope

The theorem uses the paper-form AdaBelief recurrence in which epsilon is accumulated in the second-moment state and is also added after the square root. No AMSGrad maximum, rectification, weight decay, projection, or stochastic gradient noise is included.

The exact fixed-point statement concerns the autonomous recurrence used in the paper's theory. The debiased algorithm is nonautonomous, so its statement here is the strict asymptotic local exponential-stability frontier inherited from the limiting Jacobian.

This is a local scalar theorem. It does not classify nonlinear attractors after loss of local stability, and it does not automatically extend to rotated multidimensional Hessians with coordinatewise preconditioning.

## Proof

Omitting de-biasing, the state map is
\[
m^+=\beta_1m+(1-\beta_1)\lambda x,
\]
\[
s^+=\beta_2s+(1-\beta_2)(\lambda x-m^+)^2+\varepsilon,
\]
\[
x^+=x-\alpha\frac{m^+}{\sqrt{s^+}+\varepsilon}.
\]
At \(x=m=0\), the second-moment equation gives
\[
s_\star=\frac{\varepsilon}{1-\beta_2}.
\]

The squared prediction error has zero first derivative at the fixed point. A denominator perturbation also contributes no linear term to \(x^+\), because its numerator is zero at the fixed point. Hence the Jacobian in \((x,m,s)\) is block triangular:
\[
J=
\begin{bmatrix}
1-h(1-\beta_1)\lambda&-h\beta_1&0\\
(1-\beta_1)\lambda&\beta_1&0\\
0&0&\beta_2
\end{bmatrix},
\qquad
h=\frac{\alpha}{D_\varepsilon}.
\]

The \(2\times2\) block has determinant \(\beta_1\) and trace
\[
T=1+\beta_1-(1-\beta_1)\chi.
\]
Its characteristic polynomial is \(r^2-Tr+\beta_1\). The real second-order Jury conditions are
\[
1-\beta_1>0,
\qquad
1-T+\beta_1>0,
\qquad
1+T+\beta_1>0.
\]
They reduce to
\[
\chi>0
\]
and
\[
2(1+\beta_1)-(1-\beta_1)\chi>0,
\]
which gives the exact stability interval.

At equality in the upper condition,
\[
T=-(1+\beta_1),
\]
so
\[
r^2+(1+\beta_1)r+\beta_1=(r+1)(r+\beta_1).
\]

The optimization roots are nonreal exactly when
\[
T^2<4\beta_1.
\]
Solving this inequality gives the stated plateau interval. Since the product of the two roots is \(\beta_1\), each complex root has modulus \(\sqrt{\beta_1}\).

For the debiased algorithm, the optimum second-moment recursion is
\[
s_t=\beta_2s_{t-1}+\varepsilon.
\]
Its closed form yields constant corrected value \(\widehat s_t=\varepsilon/(1-\beta_2)\). The local \((x,m)\) block replaces \(h\) by
\[
h_t=
\frac{\alpha}{(1-\beta_1^t)D_\varepsilon},
\]
which converges exponentially to \(h\). Strict Schur stability and strict instability are robust under this exponentially vanishing nonautonomous perturbation, giving the same asymptotic frontier away from equality.

## Verification

The accompanying `verify.py` checks the fixed second-moment floor, characteristic polynomial, Jury boundary, complex-root plateau, source-parameter curvature ceilings, and the exact corrected second moment along the debiased optimum reference orbit.

Finite numerical eigenvalue evaluations are transcription guards. The infinite-time local frontier follows from the analytic Jacobian and Jury calculation above.

## Relationship to prior work

Zhuang et al. introduced AdaBelief and place epsilon in two locations: inside the residual second-moment recurrence and after the square root. Their paper states that its theoretical analysis omits de-biasing and proves general convex and nonconvex convergence bounds under lower-bound and monotonicity conditions on the adaptive second moment. The inspected full text does not give an exact deterministic quadratic Schur frontier or the rate plateau above.

The official implementation preserves the accumulated-epsilon convention. Its documentation emphasizes that epsilon plays a materially different role than in Adam and recommends different epsilon values for different task families.

Zhang, Niwa, and Kleijn later isolated AdaBelief's epsilon placement as a mechanism that suppresses the range of adaptive stepsizes and used that observation to motivate Aida. Their analysis reproduces the same recurrence but does not derive the scalar quadratic curvature ceiling, unit-root boundary, or momentum plateau.

FastAdaBelief modifies the schedule to exploit strong convexity and proves improved regret bounds. It does not state the constant-parameter local stability law derived here.

## Limitations

The result is local and deterministic. It does not classify the nonlinear dynamics after local instability.

The epsilon convention in the original AdaBelief paper is not universal across modern libraries; some libraries expose separate second-moment and denominator epsilon parameters.

The numerical comparison between \(\varepsilon=10^{-8}\) and \(\varepsilon=10^{-16}\) holds the other paper-form parameters fixed and excludes optional rectification. It is not a claim that smaller epsilon is globally worse in deep-learning practice.

Inside the complex-root plateau, the full state also has eigenvalue \(\beta_2\); the full local spectral radius is therefore
\[
\max\{\sqrt{\beta_1},\beta_2\}.
\]

## References

1. Juntang Zhuang, Tommy Tang, Yifan Ding, Sekhar Tatikonda, Nicha Dvornek, Xenophon Papademetris, and James S. Duncan, “AdaBelief Optimizer: Adapting Stepsizes by the Belief in Observed Gradients,” arXiv:2010.07468v1, 2020.
2. Official `juntang-zhuang/Adabelief-Optimizer` implementation, `AdaBelief.py`, update-0.2.0 branch.
3. Guoqiang Zhang, Kenta Niwa, and W. Bastiaan Kleijn, “A DNN Optimizer that Improves over AdaBelief by Suppression of the Adaptive Stepsize Range,” arXiv:2203.13273v1, 2022.
4. Yangfan Zhou, Kaizhu Huang, Cheng Cheng, Xuguang Wang, Amir Hussain, and Xin Liu, “FastAdaBelief: Improving Convergence Rate for Belief-based Adaptive Optimizers by Exploiting Strong Convexity,” arXiv:2104.13790v1, 2021.
