# Sharp mean-square stability loss for Bernoulli error-feedback sparsification
## Finding

Consider the deterministic scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,\qquad \lambda>0.
\]
Use the memory/error-feedback update from sparsified SGD with memory:
\[
u_t=e_t+\eta \nabla f(x_t)=e_t+s x_t,
\qquad
s=\eta\lambda>0,
\]
\[
g_t=\mathcal C_p(u_t),
\qquad
x_{t+1}=x_t-g_t,
\qquad
e_{t+1}=u_t-g_t,
\]
with
\[
e_0=0.
\]
The scalar compressor is the Bernoulli ultra-sparsifier
\[
\mathcal C_p(u)=B_tu,
\qquad
B_t\sim\operatorname{Bernoulli}(p),
\qquad
0<p\le1,
\]
independently over time. In dimension one this is exactly the random-coordinate ultra-sparsification mechanism of the source paper with expected transmitted-coordinate count \(p\).

The full state \((x_t,e_t)\) is geometrically stable in mean square if and only if
\[
0<s<\frac{2p}{2-p}.
\]
At the boundary
\[
s=\frac{2p}{2-p},
\]
the second-moment operator has eigenvalue \(1\). For larger positive \(s\), even the standard initialization \(e_0=0\), \(x_0\ne0\), fails to converge to zero in mean square.

The same threshold has an exact renewal interpretation. Immediately after a successful transmission, the residual is zero. Let
\[
J\sim\operatorname{Geom}(p)
\]
on \(\{1,2,\ldots\}\) denote the number of iterations until the next successful transmission, including that successful iteration. During the preceding \(J-1\) failed transmissions, \(x\) is unchanged while the residual accumulates the same gradient step. The next successful message therefore applies the bundled update \(Jsx\), giving
\[
x^+=(1-Js)x.
\]
Hence the exact squared contraction factor per successful communication cycle is
\[
q_{\rm cyc}(s)
=
\mathbb E[(1-Js)^2]
=
1-\frac{2s}{p}
+
\frac{2-p}{p^2}s^2.
\]
It satisfies
\[
q_{\rm cyc}(s)<1
\quad\Longleftrightarrow\quad
0<s<\frac{2p}{2-p},
\]
and its unique minimizer is
\[
s_{\rm cyc}^\star=\frac{p}{2-p},
\]
with
\[
q_{\rm cyc}^{\min}
=
\frac{1-p}{2-p}.
\]

The comparison with the same Bernoulli sparsifier without memory is sharp. If one simply uses
\[
x_{t+1}=x_t-B_ts x_t,
\]
then
\[
\mathbb E[x_{t+1}^2\mid x_t]
=
\left(1-2ps+ps^2\right)x_t^2,
\]
so mean-square stability holds exactly for
\[
0<s<2,
\]
independently of \(p\). At
\[
s=1,
\]
the first successful transmission sends the exact scalar gradient step and annihilates the error.

Thus error accumulation changes random omission into a random delay: a rare successful message contains a geometrically distributed number of stale same-sign gradient contributions. On this deterministic scalar benchmark, that bundling creates overshoot and strictly narrows the constant-step mean-square stability window whenever \(p<1\).

## Assumptions and scope

The objective is a one-dimensional deterministic positive quadratic. The compressor independently either transmits the entire scalar update or transmits zero, with success probability \(p\). This is the one-dimensional specialization of the source paper's random-coordinate ultra-sparsification mechanism.

The result concerns the classic memory/error-feedback update in which the unsent part of the step is added to the next message. It does not cover error-feedback variants that alter the point where the gradient is evaluated, damp the residual, clip the accumulated message, or use correlated transmission schedules.

Mean-square stability means geometric decay of the second moments of the full state \((x_t,e_t)\). The theorem does not claim that error feedback is generally harmful. In multidimensional or stochastic settings, memory can preserve information that ordinary compression would otherwise lose, which is precisely the motivation of the original convergence theory.

The no-memory comparison uses the same biased Bernoulli compressor without rescaling. It is included to isolate the dynamical effect of residual accumulation, not as a general replacement recommendation.

## Proof

Conditioned on the Bernoulli event, the state update is linear. If \(B_t=1\),
\[
\begin{bmatrix}
x_{t+1}\\
e_{t+1}
\end{bmatrix}
=
\begin{bmatrix}
1-s&-1\\
0&0
\end{bmatrix}
\begin{bmatrix}
x_t\\
e_t
\end{bmatrix}.
\]
If \(B_t=0\),
\[
\begin{bmatrix}
x_{t+1}\\
e_{t+1}
\end{bmatrix}
=
\begin{bmatrix}
1&0\\
s&1
\end{bmatrix}
\begin{bmatrix}
x_t\\
e_t
\end{bmatrix}.
\]

Define the second moments
\[
X_t=\mathbb E[x_t^2],
\qquad
Y_t=\mathbb E[x_te_t],
\qquad
Z_t=\mathbb E[e_t^2].
\]
Independence of \(B_t\) gives the exact recursion
\[
\begin{bmatrix}
X_{t+1}\\
Y_{t+1}\\
Z_{t+1}
\end{bmatrix}
=
N
\begin{bmatrix}
X_t\\
Y_t\\
Z_t
\end{bmatrix},
\]
where
\[
N=
\begin{bmatrix}
1-2ps+ps^2&-2p(1-s)&p\\
(1-p)s&1-p&0\\
(1-p)s^2&2(1-p)s&1-p
\end{bmatrix}.
\]

Write the characteristic polynomial as
\[
P(z)=z^3+a_1z^2+a_2z+a_3.
\]
Direct expansion gives
\[
a_1=-ps^2+2ps+2p-3,
\]
\[
a_2=p^2s^2+2p^2s+p^2-ps^2-2ps-4p+3,
\]
and
\[
a_3=-(1-p)^2.
\]

For a real monic cubic, the Jury conditions are
\[
|a_3|<1,
\]
\[
1+a_1+a_2+a_3>0,
\]
\[
1-a_1+a_2-a_3>0,
\]
and
\[
1-a_2+a_1a_3-a_3^2>0.
\]
For \(0<p\le1\), the first condition is automatic. The potentially binding condition factors as
\[
1+a_1+a_2+a_3
=
ps\left[2p-(2-p)s\right].
\]
Hence it is positive exactly for
\[
0<s<\frac{2p}{2-p}.
\]

The remaining two Jury expressions never bind. First,
\[
1-a_1+a_2-a_3
=
p^2s^2+2p^2s+2p^2-4ps-8p+8.
\]
As a quadratic in \(s\), its minimum occurs at
\[
s=\frac{2-p}{p}
\]
and equals
\[
(2-p)^2>0.
\]
Second, put
\[
J(s)=1-a_2+a_1a_3-a_3^2.
\]
At \(s=0\),
\[
J(0)=p^3(2-p)>0,
\]
and
\[
J'(s)
=
2p(p-1)\left[ps-p-2s\right].
\]
For \(0<p<1\), both \(p-1\) and \(ps-p-2s=s(p-2)-p\) are negative, so \(J'(s)>0\). For \(p=1\), \(J\) is constant and positive. Thus \(J(s)>0\) for every \(s\ge0\).

This proves Schur stability of the exact second-moment operator precisely on the stated interval. At the upper endpoint,
\[
P(1)=0,
\]
so the moment operator has eigenvalue \(1\).

For necessity under the actual initialization \(e_0=0\), consider successful-transmission epochs. After a success the residual is zero. If the next success occurs after \(J\) iterations, then the first \(J-1\) iterations leave \(x\) unchanged and add \(sx\) to the residual each time. The successful message is therefore \(Jsx\), so
\[
x^+=(1-Js)x.
\]
The geometric law has
\[
\mathbb E[J]=\frac1p,
\qquad
\mathbb E[J^2]=\frac{2-p}{p^2}.
\]
Therefore
\[
\mathbb E[(x^+)^2\mid x]
=
q_{\rm cyc}(s)x^2
\]
with the displayed \(q_{\rm cyc}\). At the upper boundary it equals one, and above the boundary it exceeds one. Thus the standard initialized algorithm cannot converge in mean square there.

Finally,
\[
q_{\rm cyc}'(s)
=
-\frac2p+\frac{2(2-p)}{p^2}s,
\]
so its unique minimizer is \(p/(2-p)\), with minimum \((1-p)/(2-p)\).

For the no-memory iteration,
\[
x_{t+1}=(1-B_ts)x_t,
\]
and the exact one-step second-moment multiplier is
\[
(1-p)+p(1-s)^2
=
1-2ps+ps^2.
\]
It is below one exactly for \(0<s<2\).

## Verification

The accompanying `verify.py` reconstructs both Bernoulli state matrices and the three-moment operator. Using exact rational arithmetic, it checks the moment recursion by explicit branch averaging, verifies the characteristic coefficients, verifies all four factored Jury expressions, checks the geometric-cycle formula and its optimum, and compares the no-memory stability multiplier.

These finite checks are algebra and transcription guards. The infinite-time result follows from the exact second-moment recursion, the complete cubic Jury test, and the renewal argument above.

## Relationship to prior work

Stich, Cordonnier, and Jaggi introduced sparsified SGD with memory for contractive compressors, including random-\(k\) sparsification. Their ultra-sparsification remark explicitly permits transmitting a random coordinate with probability below one, and their algorithm stores suppressed updates in memory and reinjects them later. Their convergence theorem uses carefully chosen time-varying steps and averaged iterates. The inspected paper does not give the constant-step scalar mean-square phase boundary or the geometric-delay overshoot law above.

Karimireddy et al. cast the same residual mechanism as error feedback and prove broad convergence guarantees for arbitrary compression operators. Their inspected algorithm has the same corrected-message and residual update structure. It does not state the Bernoulli-sparsifier scalar second-moment matrix, its sharp stability interval, or the communication-cycle optimum.

Wu et al. analyze a distinct error-compensated quantized SGD scheme on quadratic objectives. Their method uses stochastic quantization together with two additional compensation parameters and derives worst-case error bounds. The inspected quadratic section does not specialize to Bernoulli coordinate omission or imply the threshold \(2p/(2-p)\).

Xu and Huang later study random block-wise sparsification and report that ordinary error feedback can perform poorly for that compressor, motivating detached error feedback. Their theory concerns distributed stochastic training and variance-versus-second-moment bounds rather than the exact scalar stability mechanism here.

Thomsen, Taylor, and Dieuleveut provide a tight modern comparison of classic error feedback, EF21, and compressed gradient descent in a one-node smooth strongly convex setting. Their main exact analysis assumes a deterministic contractive compressor. It concludes that compressed gradient descent can outperform error feedback in that setting, which is qualitatively consistent with the present benchmark, but it does not cover the independent Bernoulli compressor or derive the geometric-cycle law.

## Limitations

The theorem is scalar and deterministic. Multidimensional random-\(k\) sparsification couples coordinate transmission schedules to different curvature modes, and stochastic gradients add another source of noise.

The compressor is independent across iterations. Correlated or periodic communication can change the waiting-time distribution and hence the bundled-step law.

The result studies a constant learning rate. Diminishing steps can suppress the geometric-delay overshoot and are central to the original convergence guarantees.

The no-memory comparison is unusually favorable in one dimension because a successful scalar transmission loses no directional information. Error feedback can be essential in settings where omitted coordinates would otherwise receive persistently biased updates.

A recent tight-analysis paper treats classic error feedback with deterministic contractive compressors and shows a broader regime where compressed gradient descent can dominate. Its assumptions do not settle the present randomized-compressor formula, but it reduces the novelty claim to the exact Bernoulli mean-square frontier and renewal mechanism rather than a general statement that error feedback is detrimental.

## References

1. Sebastian U. Stich, Jean-Baptiste Cordonnier, and Martin Jaggi, “Sparsified SGD with Memory,” arXiv:1809.07599v1, 2018.
2. Sai Praneeth Karimireddy, Quentin Rebjock, Sebastian U. Stich, and Martin Jaggi, “Error Feedback Fixes SignSGD and other Gradient Compression Schemes,” arXiv:1901.09847v1, 2019.
3. Jiaxiang Wu, Weidong Huang, Junzhou Huang, and Tong Zhang, “Error Compensated Quantized SGD and its Applications to Large-scale Distributed Optimization,” ICML 2018, arXiv:1806.08054v1.
4. An Xu and Heng Huang, “Detached Error Feedback for Distributed SGD with Random Sparsification,” arXiv:2004.05298v1, 2020.
5. Daniel Berg Thomsen, Adrien Taylor, and Aymeric Dieuleveut, “Tight analyses of first-order methods with error feedback,” arXiv:2506.05271v1, 2025.
