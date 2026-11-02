# A universal sixth-power loss of three-rate identifiability at a triadic SIS endemic fold

## Finding

In the three-agent homogeneous dyadic-plus-triadic discrete SIS model of Liang--Cui--Liu, the exact three-rate parameter-learning matrix constructed from three successive nonstationary states has a nonzero determinant at every finite observation time, even on the endemic saddle-node. Yet as the observation window moves to late times, its determinant and spectral condition number have exact sharp asymptotics:
\[
\lim_{t\to\infty} t^6\det\Phi_t=\frac{2}{\kappa^3},\qquad
\lim_{t\to\infty}\frac{\operatorname{cond}_2(\Phi_t)}{t^4}=\frac{3\sqrt 2\,\kappa^2 U W}{2hr}>0,
\]
where \(r=(\kappa-\beta)/(2\kappa)\), \(v(z)=h(-z,z(1-z),z^2(1-z))\), \(U=\|v(r)\|_2\), and \(W=\|v(r)\times v'(r)\|_2\). In particular, four noiseless prevalence observations identify all three *unconstrained* rates exactly, whereas the same raw three-parameter regression becomes polynomially ill-conditioned near the attracting semistable endemic state. The determinant constant is independent of the step size, pairwise transmission rate, recovery rate, and initial prevalence.

## Assumptions and scope

Fix \(\kappa>\beta>0\) and let
\[
\delta=\frac{(\beta+\kappa)^2}{4\kappa},\qquad
r=\frac{\kappa-\beta}{2\kappa}\in(0,1/2),\qquad
0<h<\frac1{\delta+\beta+\kappa}.
\]
Use a three-agent complete dyadic network whose two off-diagonal incoming edge weights for each agent are both \(1/2\), and a three-agent directed hypergraph whose two ordered distinct-neighbor triadic weights for each agent are both \(1/2\). Each vertex has intrinsic recovery, pairwise, and triadic rates \(\delta,\beta,\kappa\), respectively. From symmetric initial prevalence \(x_0\in(r,1]\), the diagonal is invariant; its common component follows, for every integer \(t\ge0\),
\[
x_{t+1}=x_t+h x_t[-\delta+(1-x_t)(\beta+\kappa x_t)]
=x_t-h\kappa x_t(x_t-r)^2.
\]
For each \(t\ge0\), let \(\Phi_t\) be the \(3\times3\) design matrix with rows \(v(x_t),v(x_{t+1}),v(x_{t+2})\) in the exact three-rate regression
\[
\begin{pmatrix}x_{t+1}-x_t\\x_{t+2}-x_{t+1}\\x_{t+3}-x_{t+2}\end{pmatrix}
=\Phi_t\begin{pmatrix}\delta\\\beta\\\kappa\end{pmatrix}.
\]
The limits concern the standard Euclidean spectral condition number of this unscaled three-column design, with \(h\) and all sampled prevalence values known exactly. They do **not** claim equivalent conditioning for a reduced two-parameter estimator that imposes the fold relation, nor a statistical confidence interval for data corrupted in the predictors.

## Proof

**Step 1: invariant scalar fold.** The row sums of the dyadic and triadic weights are separately one. Thus the network model reduces on the invariant diagonal to the stated cubic recurrence. The fold identity is algebraic:
\[
-\delta+(1-x)(\beta+\kappa x)=-\kappa(x-r)^2.
\]
Write \(F(x)=x-h\kappa x(x-r)^2\). Its derivative is the concave quadratic \(1+h[(\beta-\delta)+2(\kappa-\beta)x-3\kappa x^2]\); on \([0,1]\) it is bounded below by its endpoint minimum. Both endpoint derivatives are strictly positive, since \(F'(0)=1+h(\beta-\delta)>0\) and \(F'(1)=1-h(\delta+\beta+\kappa)>0\). As \(F(r)=r\) and \(F(x)<x\) for \(x>r\), strict monotonicity yields \(r<x_{t+1}<x_t\) for all \(t\). Thus \(x_t\downarrow r\), since the only fixed point in \([r,1]\) is \(r\).

**Step 2: sharp approach.** Put \(u_t=x_t-r>0\). Then
\[
u_{t+1}=u_t-h\kappa(r+u_t)u_t^2,
\quad
\frac1{u_{t+1}}-\frac1{u_t}
=\frac{h\kappa(r+u_t)}{1-h\kappa(r+u_t)u_t}\longrightarrow h\kappa r.
\]
By Cesàro averaging the reciprocals, \(t u_t\to1/(h\kappa r)\). Define \(d_t=x_t-x_{t+1}=h\kappa x_t(x_t-r)^2\). Consequently
\[
t^2d_t\longrightarrow\frac1{h\kappa r},\qquad\frac{d_{t+1}}{d_t}\longrightarrow1.
\]
All these limits hold for every \(x_0\in(r,1]\).

**Step 3: finite-time identifiability and determinant.** Factoring \(hx\) from each row of \(v(x)\), the remaining three columns are the quadratic polynomials \(-1\), \(1-x\), and \(x(1-x)\), whose coefficient change-of-basis determinant is \(-1\). The Vandermonde determinant therefore gives the exact identity
\[
\det\Phi_t=h^3x_tx_{t+1}x_{t+2}
(x_t-x_{t+1})(x_t-x_{t+2})(x_{t+1}-x_{t+2})>0.
\]
Hence the four consecutive state observations yield a unique solution for \((\delta,\beta,\kappa)\) in the full three-rate linear model. Using \(x_t-x_{t+2}=d_t+d_{t+1}\), Step 2 implies
\[
t^6\det\Phi_t\longrightarrow
h^3r^3\frac2{(h\kappa r)^3}=\frac2{\kappa^3}.
\]
This is not a statement about two noisy streams of automatically dependent observations; it is an exact algebraic property of the ideal-data design matrix.

**Step 4: singular values.** Regard \(v(z)\) as a row vector. Let \(U=\|v(r)\|\) and \(W=\|v(r)\times v'(r)\|\). Since \(r>0\), the vectors are independent: direct expansion gives
\[
v(r)\times v'(r)=h^2r^2((r-1)^2,\,1-2r,\,1)
\]
up to the common orientation sign, so \(W>0\). The three rows of \(\Phi_t\) coalesce at \(v(r)\), proving \(\sigma_1(\Phi_t)\to\sqrt3 U\). Subtracting their mean yields a leading centered row pattern \((d_t,0,-d_t)\,v'(r)\), modulo an error of relative order \(o(d_t)\) in the centered first-order component; after orthogonal projection away from \(v(r)\), its nonzero singular value is asymptotic to \(\sqrt2\,d_t W/U\). Thus
\[
\sigma_2(\Phi_t)\sim\frac{\sqrt2 W}{U h\kappa r}\,t^{-2}.
\]
Finally, the singular-value product equals the positive determinant, whence
\[
\sigma_3(\Phi_t)\sim\frac{2hr}{\sqrt6\,\kappa^2 W}\,t^{-4}
\quad\text{and}\quad
\operatorname{cond}_2(\Phi_t)\sim\frac{3\sqrt2\,\kappa^2 UW}{2hr}\,t^4.
\]
The use of the determinant to obtain \(\sigma_3\) is valid because the other two asymptotics establish their strictly positive leading constants.

## Verification

Run `python3 verification/check.py` with Python 3.10 or later and no third-party packages. It directly checks 119 exact-rational Vandermonde identities, exact recovery of all three rates from four samples in two independent rational fold cases, and the determinant limit numerically over 60,000 iterations using 65-digit decimal arithmetic. The last check is supplementary, not an infinite-time proof. The exact example \(\beta=1,\kappa=4,\delta=25/16,h=1/10,x_0=3/4\) gives \(r=3/8\) and predicted determinant limit \(1/32\); the computed scaled determinant at iteration 60,000 is approximately \(0.03081541705\). The proof above, not this finite experiment, establishes all infinite limits and the singular-value formula.

## Relationship to prior work

Liang--Cui--Liu (arXiv:2408.08602v1, Secs. 2--4, especially Eqs. 6, 12, 13) introduce the discrete higher-order SIS update and linear-in-three-rates regression, explaining uniqueness under a full-column-rank assumption. Their presented analysis does not give this fold-specific universal determinant or the sharp late-window singular-value collapse. Kiss--Simon (arXiv:2208.07543v1) analyze identifiability from growth rates and final sizes in different networked SIR models. Landry--Restrepo (arXiv:2006.15453v2) discuss heterogeneous higher-order contagion and endemic folds, but not discrete-time three-rate observation-design asymptotics. The determinant factorization is a Vandermonde identity; the distinct contribution here is its full coupling to the critical epidemic recurrence and the explicit, parameter-sensitive conditioning rate.

## Limitations

The theorem applies to a *symmetric trajectory* of the three-vertex complete mixed-interaction network, not general heterogeneous directed hypergraphs. Only an endemic fold with \(\kappa>\beta>0\), a step satisfying the strict positivity bound, and initial \(x_0>r\) is analyzed. Data sampled exactly at the equilibrium give rank one, not unique recovery. The conclusions concern exact noiseless observations and the unconstrained three-parameter least-squares design, not errors-in-variables regression or statistically optimal nonlinear estimators. The general Vandermonde component may follow from standard polynomial-interpolation theory; a literature-equivalent critical-conditioning specialization remains possible.

## References

1. L. Liang, S. Cui and F. Liu, *Discrete-time SIS Social Contagion Processes on Hypergraphs*, arXiv:2408.08602v1 (first public 16 August 2024), https://arxiv.org/html/2408.08602v1.
2. I. Z. Kiss and P. L. Simon, *On parameter identifiability in network-based epidemic models*, arXiv:2208.07543v1, https://arxiv.org/html/2208.07543v1.
3. N. Landry and J. G. Restrepo, *The effect of heterogeneity on hypergraph contagion models*, arXiv:2006.15453v2, https://arxiv.org/html/2006.15453v2.
