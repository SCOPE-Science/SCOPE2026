# Five conditional-mean equilibria from two strongly convex NGN losses: a sharp parameter frontier

## Finding

Consider the non-negative Gauss–Newton (NGN) stochastic-gradient rule of Orvieto and Xiao with constant regularization parameter \(\sigma>0\). There exist just two equally weighted, strictly positive, unit-curvature scalar quadratic losses for which its exact **conditional-mean one-step map** has five real fixed points, three locally attracting, despite the population objective having a unique minimizer. The following theorem gives the exact threshold at which this five-root phenomenon becomes possible in the natural symmetric family.

Write \(A=1+\sigma\) and choose any \(d>0\), with
\[
f_+(x)=\tfrac12((x-1)^2+d),\qquad f_-(x)=\tfrac12((x+1)^2+d),\qquad \bar f(x)=\tfrac12(x^2+1+d).
\]
At state \(x\), independently sample a sign with equal probability and take one NGN step, using the sampled loss and its exact derivative. Its conditional expectation is the deterministic map
\[
T_{\sigma,d}(x)=\mathbb E[X_{k+1}\mid X_k=x]
=x-\sigma F_{A,d}(x),
\quad F_{A,d}(x)=\frac{h_{A,d}(x-1)+h_{A,d}(x+1)}2,
\quad h_{A,d}(y)=\frac{y(y^2+d)}{Ay^2+d}.
\]
The fixed points of \(T_{\sigma,d}\) satisfy an exact even-quartic equation described below. For some \(d>0\), this map has **five distinct real fixed points if and only if**
\[
\boxed{\sigma>4+4\sqrt2.}
\]
An exact witness is \(\sigma=11\) and \(d=8/5\). Its five fixed points are
\[
\boxed{x=0,\quad x=\pm 1/\sqrt{15},\quad x=\pm 1/\sqrt5.}
\]
For the deterministic iteration \(x_{n+1}=T_{11,8/5}(x_n)\), the fixed points \(0\) and \(\pm1/\sqrt5\) are locally attracting, whereas \(\pm1/\sqrt{15}\) are repelling. The outer attractors have a population objective excess of exactly \(1/10\).

## Assumptions and scope

All quantities and iterations are real and in exact arithmetic. The two losses have Hessian identically one and minimum \(d/2>0\), so there are no divisions by zero. The sampled index is uniform and independent at each update. The NGN sampled stepsize is
\[
\gamma_i(x)=\frac{\sigma}{1+\sigma f_i'(x)^2/(2f_i(x))},
\qquad X_{k+1}=X_k-\gamma_{i_k}(X_k)f_{i_k}'(X_k).
\]
The deterministic mean-map iteration is an associated **conditional-expectation dynamical system**; it must not be confused with either a realization of the stochastic recursion or the generally false identity \(\mathbb E[X_{k+1}]=T_{\sigma,d}(\mathbb E[X_k])\).

## Proof

**1. Exact rational form.** For the sampled residual \(y=x\mp1\), one has \(2f_i=y^2+d\), \(f_i'=y\), so the NGN update displacement is \(\sigma y(y^2+d)/(Ay^2+d)\). Taking the average gives \(F_{A,d}\) as claimed. Bringing the two summands over their strictly positive common denominator yields
\[
\begin{aligned}
F_{A,d}(x)&=\frac{xP_{A,d}(x^2)}{[A(x-1)^2+d][A(x+1)^2+d]},\\
P_{A,d}(t)&=At^2+Bt+C,\\
B&=(A+1)d-2A,\\
C&=d^2+(3-A)d+A.
\end{aligned}
\]
Since \(\sigma>0\), all real fixed points are precisely \(x=0\) together with signed square roots of the distinct strictly positive real roots of \(P_{A,d}\). A quadratic with leading coefficient \(A>0\) has two distinct strictly positive real roots if and only if \(B<0\), \(C>0\), and its discriminant \(\Delta>0\).

**2. Sharp existence threshold.** Direct expansion gives
\[
\Delta=B^2-4AC=d[(A-1)^2d-16A].
\]
Because \(d>0\), the necessary conditions \(\Delta>0\) and \(B<0\) require, respectively,
\[
\frac{16A}{(A-1)^2}<d<\frac{2A}{A+1}.
\]
For \(A>1\), this open interval is nonempty exactly when \((A-1)^2>8(A+1)\), or equivalently \(A>5+4\sqrt2\). This proves necessity. To prove sufficiency, take \(A>5+4\sqrt2\) and let \(d_*=16A/(A-1)^2\). At \(d=d_*\), the coefficient \(B<0\), while \(\Delta=0\) forces \(C=B^2/(4A)>0\). Thus all three strict conditions hold for \(d>d_*\) sufficiently close to \(d_*\). This proves the exact threshold in \(\sigma=A-1\). For arbitrary fixed positive parameters there can be at most five real fixed points because the numerator has degree five.

**3. Five-root witness and dynamical character.** Setting \(A=12\) and \(d=8/5\), algebraic reduction gives
\[
F_{12,8/5}(x)=\frac{x(5x^2-1)(15x^2-1)}{4(15x^2-30x+17)(15x^2+30x+17)}.
\]
The two denominator factors are strictly positive (each equals \(15(x\mp1)^2+2\)). The only real roots are exactly the five displayed above. Differentiating \(T(x)=x-11F_{12,8/5}(x)\) yields the *exact* multipliers
\[
T'(0)=\frac{1145}{1156},\qquad
T'(\pm1/\sqrt{15})=\frac{73}{72},\qquad
T'(\pm1/\sqrt5)=\frac{19}{20}.
\]
The one-dimensional strict derivative criterion \(|T'(x_*)|<1\) proves local attraction at the middle and outer roots; \(|T'(x_*)|>1\) proves repulsion at the inner pair. Because \(\bar f(x)-\bar f(0)=x^2/2\), each outer attracting root has objective excess \((1/5)/2=1/10\). This completes the proof.

## Verification

The accompanying `verify_ngn_mean.py` uses exact SymPy arithmetic. From this directory run `python -m pip install -r requirements.txt` if necessary, then `python verify_ngn_mean.py`. It checks the generic rational identity and discriminant, the double-root offset boundary, the explicit five-root factorization, all five exact derivatives, the objective excess, and representative exact threshold comparisons. The exact universal threshold and dynamical conclusions follow from the analytic inequalities above, not from finitely many tested parameters.

## Relationship to prior work

Orvieto and Xiao (2024), arXiv:2407.04358v1, introduce precisely the NGN stepsize used here; their Section 4 establishes bounds for the stochastic process in convex and strongly convex settings and discusses noninterpolating losses. They do **not**, in the inspected Sections 2 and 4 including convergence claims, supply the five-root conditional-mean classification or the sharp threshold above. Their convergence-neighborhood statements address stochastic trajectory moments, not deterministic iteration of the conditional-mean map.

Orvieto, Lacoste-Julien and Loizou (2022), arXiv:2205.04583, analyze stochastic Polyak stepsizes and demonstrate noninterpolation bias; their stepsizes and mean equations differ from fixed-parameter NGN. Loizou et al. (2020), arXiv:2002.10542, introduce stochastic Polyak stepsizes, but do not obtain this NGN bifurcation. The formula for the original NGN update and the broad existence of bias are prior results, not claimed as new.

## Limitations

This theorem concerns the symmetric two-loss unit-curvature family, fixed \(\sigma\), and the *one-step conditional-mean map*. A locally attracting fixed point of that map does **not** show that individual stochastic trajectories converge to that point, that the stochastic Markov chain has a corresponding stationary distribution, or that its expectation follows repeated applications of \(T\). No such claims are made. The arbitrary-parameter five-root classification is an existence statement with variable positive offset \(d\); local stability for all five-root choices is not asserted. The proof gives a precise mean-drift obstruction, not an impossibility theorem for NGN convergence guarantees. An equivalent rational-map classification in unlocated earlier literature is a residual originality risk.

## References

- A. Orvieto and L. Xiao, *An Adaptive Stochastic Gradient Method with Non-negative Gauss-Newton Stepsizes* (first public version July 5, 2024), arXiv:2407.04358v1. https://arxiv.org/html/2407.04358v1
- A. Orvieto, S. Lacoste-Julien and N. Loizou, *Dynamics of SGD with Stochastic Polyak Stepsizes: Truly Adaptive Variants and Convergence to Exact Solution* (2022), arXiv:2205.04583. https://arxiv.org/abs/2205.04583
- N. Loizou et al., *Stochastic Polyak Step-size for SGD: An Adaptive Learning Rate for Fast Convergence* (2020), arXiv:2002.10542. https://arxiv.org/abs/2002.10542
