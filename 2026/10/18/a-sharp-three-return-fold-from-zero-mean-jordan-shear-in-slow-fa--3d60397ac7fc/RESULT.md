# A sharp three-return fold from zero-mean Jordan shear in slow-fast passage

## Finding

Consider the triangular slow-fast flow
\[
\dot y=\varepsilon,\qquad
\dot v=yv,\qquad
\dot u=yu+\kappa\left(y^2-\frac13\right)v,
\]
with arbitrary \(\varepsilon>0\), \(\kappa\geq0\), and initial data
\(y(0)=-1\), \(u(0)=0\), \(v(0)=\delta\ne0\). A **positive return** means a value \(y>0\) at which the Euclidean fast-state norm returns to its initial magnitude:
\(\sqrt{u^2+v^2}=|\delta|\). The shear \(y^2-1/3\) is, up to scale, the lowest-degree nonconstant even polynomial with zero integral over \([-1,1]\).

For \(0<t<1/\varepsilon\), put
\[
K_\varepsilon(t)=3\sqrt{\frac{e^t-1}{(1-\varepsilon t)t^2}},\quad
\kappa_\varepsilon=\min_{0<t<1/\varepsilon}K_\varepsilon(t).
\]
There is exactly one minimizer \(t_\varepsilon\), and the count of **distinct positive norm returns** is exactly
\[
\begin{array}{c|ccc}
 &0\leq\kappa<\kappa_\varepsilon&\kappa=\kappa_\varepsilon&\kappa>\kappa_\varepsilon\\\hline
\#\text{ positive returns}&1&2&3.
\end{array}
\]
One return is always \(y=1\). At equality the other return is a quadratic tangency at \(y=\sqrt{1-\varepsilon t_\varepsilon}\). Above equality there are two simple returns strictly between \(0\) and \(1\), created by an ordinary square-root saddle-node; no further positive returns exist. In particular the nilpotent shear can generate multiple delayed norm returns **even though its accumulated shear cancels exactly at the spectral-balance point**.

The singular small-\(\varepsilon\) threshold is explicit. Let \(t_0\) be the unique number in \((1,2)\) satisfying \((2-t_0)e^{t_0}=2\), and define
\[
\kappa_0=\frac{3\sqrt{e^{t_0}-1}}{t_0}
=\frac3{\sqrt{t_0(2-t_0)}}
=3.7279012689900775\ldots.
\]
Then
\[
\kappa_\varepsilon=\kappa_0\left(1+\frac{t_0}{2}\varepsilon+O(\varepsilon^2)\right)
\quad(\varepsilon\downarrow0).
\]
For instance, at \(\varepsilon=1/100\), \(\kappa=4\), the three positive returns are approximately \(0.987980246290060\), \(0.995262315755519\), and exactly \(1\).

## Assumptions and scope

The result is exact for every real \(\varepsilon>0\), \(\kappa\geq0\), and nonzero real \(\delta\). Time is the original time, with \(y(t)=-1+\varepsilon t\). The norm is the unweighted Euclidean norm in the fast coordinates \((u,v)\); changing the fast norm is a different question. Returns at the initial slow coordinate \(y=-1\), or possible additional returns for \(y<0\), are deliberately excluded from the positive-return count. The theorem does not claim that every norm return is a dynamical return of the full state, nor that the linear fast variables form a periodic orbit.

The instantaneous fast matrix has two equal real eigenvalues \(y\) for every \(y\). Its off-diagonal Jordan coefficient changes with \(y\), and is not the constant nonzero nilpotent term of the motivating source. The eigenvalue is negative for \(y<0\) and positive for \(y>0\).

## Proof

**1. Exact propagator.** Since \(dy/dt=\varepsilon\), the second equation gives
\[
v(y)=\delta\exp\!\left(\frac{y^2-1}{2\varepsilon}\right).
\]
Dividing the first fast equation by \(v\) and using the scalar equation for \(v\),
\[
\frac{d}{dy}\left(\frac uv\right)
=\frac\kappa\varepsilon\left(y^2-\frac13\right),\qquad
\frac{u(y)}{v(y)}=\frac{\kappa}{3\varepsilon}(y^3-y),
\]
because the primitive vanishes at \(y=-1\). Thus the normalized squared norm is **exactly**
\[
R_\varepsilon(y)^2:=\frac{u(y)^2+v(y)^2}{\delta^2}
=\exp\!\left(\frac{y^2-1}{\varepsilon}\right)
\left[1+\frac{\kappa^2}{9\varepsilon^2}
 y^2(y^2-1)^2\right].\tag{1}
\]
At \(y=1\), both the logarithmic scalar growth and the accumulated off-diagonal shear vanish, so \(R_\varepsilon(1)=1\) identically. At \(y=0\), \(R_\varepsilon(0)^2=e^{-1/\varepsilon}<1\). For \(y>1\), the exponential is strictly larger than one and the bracket is at least one, so no returns occur there.

**2. Exact interior reduction.** Set \(t=(1-y^2)/\varepsilon\) for \(0<y<1\). This bijects that interval onto \((0,1/\varepsilon)\), reversing order, and (1) becomes
\[
R_\varepsilon(y)^2=e^{-t}
\left[1+\frac{\kappa^2}{9}(1-\varepsilon t)t^2\right].\tag{2}
\]
Consequently \(R_\varepsilon(y)=1\) is equivalent to \(\kappa=K_\varepsilon(t)\), with \(\kappa\geq0\). The function \(K_\varepsilon\) diverges at both endpoints.

**3. Strict unimodality and complete root count.** Introduce
\[
\varphi_\varepsilon(t)=\log(e^t-1)-\log(1-\varepsilon t)-2\log t.
\]
Its first two derivatives are
\[
\varphi_\varepsilon'(t)=\frac{e^t}{e^t-1}
+\frac{\varepsilon}{1-\varepsilon t}-\frac2t,
\]
\[
\varphi_\varepsilon''(t)=
-\frac1{4\sinh^2(t/2)}
+\frac{\varepsilon^2}{(1-\varepsilon t)^2}
+\frac2{t^2}>0.
\]
The last inequality is strict because \(2\sinh(t/2)>t\) for every \(t>0\). Moreover \(\varphi_\varepsilon'\to-\infty\) at the left endpoint and \(\to+\infty\) at the right endpoint. Therefore the logarithm of \(K_\varepsilon\) is strictly convex and has one minimum. Comparing a horizontal \(\kappa\)-level to that minimum proves exactly zero, one tangent, or two simple interior roots. Adding the always-present return \(y=1\) gives the displayed \(1/2/3\) classification. At the threshold, \(\varphi_\varepsilon''(t_\varepsilon)>0\) and \(\partial_\kappa[R_\varepsilon^2-1]>0\) at the interior contact, so this contact is a nondegenerate fold.

More precisely, when \(\eta=\kappa-\kappa_\varepsilon\downarrow0^+\), its two \(t\)-coordinates are
\[
t_\pm=t_\varepsilon\pm
2\sqrt{\frac{\eta}{\kappa_\varepsilon\varphi_\varepsilon''(t_\varepsilon)}}
+O_\varepsilon(\eta),\tag{3}
\]
and their slow coordinates are \(\sqrt{1-\varepsilon t_\pm}\). This identifies the square-root splitting as well as the root count.

**4. The limiting threshold.** For fixed positive \(t\), \(K_\varepsilon(t)\to3\sqrt{e^t-1}/t\). The limiting logarithmic derivative vanishes precisely when \((2-t)e^t=2\). Apart from the endpoint \(t=0\), it has exactly one root \(t_0\in(1,2)\), by differentiating \((2-t)e^t\). The same strict-convexity argument implies \(t_\varepsilon\to t_0\). The implicit function theorem at the nondegenerate minimizer gives \(t_\varepsilon=t_0+O(\varepsilon)\). Evaluating \(K_\varepsilon\) there, the derivative of the limiting factor in \(t\) vanishes at \(t_0\), so
\[
\frac{\kappa_\varepsilon}{\kappa_0}
=(1-\varepsilon t_0)^{-1/2}+O(\varepsilon^2)
=1+\frac{t_0}{2}\varepsilon+O(\varepsilon^2).
\]
This proves the final asymptotic expansion. For fixed \(\kappa>\kappa_0\) and sufficiently small \(\varepsilon\), the two nontrivial return coordinates differ from \(y=1\) by quantities of order \(\varepsilon\), since their transformed coordinates converge to distinct finite positive roots of \(e^t-1=(\kappa^2/9)t^2\).

## Verification

The standalone \(\texttt{verify.py}\) uses Python's standard library. It runs 336 exact rational identity checks across 96 parameter triples, followed by 95 representative floating-point checks, including nine values of \(\varepsilon\), the three-return sample, and the first-order small-\(\varepsilon\) coefficient. Its current execution reports 431 successful checks. All infinite quantifiers and the uniqueness of the minimizer are justified by the proof above; finite testing is not substituted for them.

## Relationship to prior work

Borsotti's 2026 paper [1], Sections 2–4, establishes logarithmically enhanced entry-exit shifts for a **fixed nonzero** nilpotent block \(N\), and explicitly notes possible extra norm-return points close to initial entry. Here the nilpotent block is instead multiplied by a sign-changing, mean-zero coefficient. The total shear vanishes at \(y=1\), and the new exact phase diagram concerns two additional returns on the **repelling side** \(0<y<1\) close to the delayed spectral-balance point. Neither the constant-block exit formula nor its near-entry caveat gives this finite-\(\varepsilon\) fold threshold.

Kaklamanos, Kuehn, Popović and Sensi [2] analyze dynamic passage through a **unique intersection of two distinct eigenvalue branches**, under explicit hypotheses in their main theorem; in this example the two eigenvalues coincide for every \(y\), so its main theorem does not apply. Classical scalar entry-exit balance [3] predicts the baseline \(y=1\) but cannot count the shear-induced crossings of the two-dimensional Euclidean norm. These distinctions concern exact hypotheses and implications, rather than titles or terminology.

## Limitations

This is a complete result for the stated linear triangular slow-fast family and initial fast direction, not a general theorem for arbitrary variable nilpotent matrices, initial directions, norms, nonlinear perturbations, or stochastic forcing. The threshold depends on the chosen Euclidean norm. The additional norm recrossings are not periodic orbits. No independent audit has been performed; related uncatalogued literature could still contain an equivalent formula. The elementary exact propagator and strict-convexity mechanism, not numerical root finding, establish the conclusions.

## References

[1] Jacopo Borsotti, *The entry-exit function and nilpotent corrections in multidimensional slow-fast systems*, arXiv:2610.15670v1 (first public 2026-10-11), https://arxiv.org/abs/2610.15670 ; full text https://arxiv.org/html/2610.15670v1 .

[2] Panagiotis Kaklamanos, Christian Kuehn, Nikola Popović, Mattia Sensi, *Entry–Exit Functions in Fast–Slow Systems with Intersecting Eigenvalues*, arXiv:2208.11559 (2022), and *Journal of Dynamics and Differential Equations* 37 (2025), 559–576, https://doi.org/10.1007/s10884-023-10266-2 .

[3] Peter De Maesschalck and Stephen Schecter, *The entry–exit function and geometric singular perturbation theory*, *Journal of Differential Equations* 260 (2016), 6697–6715, https://doi.org/10.1016/j.jde.2016.01.008 .
