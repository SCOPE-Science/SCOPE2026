# A sharp noncommuting regularization–splitting limit for a port-Hamiltonian DAE

## Finding

Let \(r>0\) and \(h>0\) be arbitrary constants. Consider the index-one, unforced port-Hamiltonian differential-algebraic equation (DAE)
\[
E\dot x=(J-R)x,\quad E=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad R=\begin{pmatrix}0&0\\0&r\end{pmatrix},\quad x(0)=\begin{pmatrix}1\\1/r\end{pmatrix}.
\]
Its unique consistent solution is \(x(t)=(e^{-t/r},e^{-t/r}/r)^{\mathsf T}\). For \(\varepsilon>0\), put \(E_\varepsilon=E+\varepsilon I\) and let \(x_\varepsilon(h)\) be the *unsplit exact* flow at time \(h\) of \(E_\varepsilon\dot x=(J-R)x\). Set
\[
S_{\varepsilon,h}=\exp\!\left(\tfrac h2E_\varepsilon^{-1}J\right)\exp\!\left(-hE_\varepsilon^{-1}R\right)\exp\!\left(\tfrac h2E_\varepsilon^{-1}J\right),\qquad y_{\varepsilon,h}=S_{\varepsilon,h}x(0).
\]
**Exact theorem.** Although \(x_\varepsilon(h)\to x(h)\) as \(\varepsilon\downarrow0\), and \(S_{\varepsilon,h}^{\mathsf T}E_\varepsilon S_{\varepsilon,h}\preceq E_\varepsilon\) for *every* \(h,\varepsilon>0\), the set of cluster points of
\[
\big((y_{\varepsilon,h})_1,\sqrt\varepsilon\,(y_{\varepsilon,h})_2\big)
\]
as \(\varepsilon\downarrow0\) is precisely the circle
\[
\left\{(a,b)\in\mathbb R^2:(a-\tfrac12)^2+b^2=\tfrac14\right\}.
\]
In the regularized energy norm \(\|v\|_{E_\varepsilon}=\sqrt{v^{\mathsf T}E_\varepsilon v}\), the *sharp* lower and upper error accumulation limits are
\[
\boxed{\begin{aligned}
\liminf_{\varepsilon\downarrow0}\|y_{\varepsilon,h}-x_\varepsilon(h)\|_{E_\varepsilon}&=\min(e^{-h/r},1-e^{-h/r}),\\
\limsup_{\varepsilon\downarrow0}\|y_{\varepsilon,h}-x_\varepsilon(h)\|_{E_\varepsilon}&=\max(e^{-h/r},1-e^{-h/r}).
\end{aligned}}
\]
The lower limit is strictly positive for every fixed finite \(h>0\). When \(h=r\log2\), the weighted error itself converges to exactly \(1/2\), independent of the fast oscillation phase. These statements concern a *single* exact-subflow Strang step and do not assert failure for coupled choices \(h=h(\varepsilon)\downarrow0\).

## Assumptions and scope

The model is a real two-variable, constant-coefficient, unforced index-one DAE with the consistent initial value shown above. The algebraic constraint is \(x_1-rx_2=0\), whose derivative with respect to the algebraic variable is \(-r\ne0\). All subflows of the \(\varepsilon\)-regularized ordinary differential equation are evaluated *exactly*: the statement therefore isolates splitting from errors in subsolvers. The parameter \(r\) is positive; \(h\) is fixed and positive while \(\varepsilon\downarrow0\). The energy metric is the positive-definite regularized Hamiltonian metric, not the Euclidean metric. The primary subject is numerical approximation of differential-algebraic equations (MSC2020 65L80).

## Proof

**1. Exact regularized flow.** Writing \(x=(u,v)^{\mathsf T}\) gives
\[
(1+\varepsilon)u'=-v,\qquad \varepsilon v'=u-rv.
\]
At \(\varepsilon=0\), \(v=u/r\) and \(u'=-u/r\). For the regularized system the characteristic polynomial is
\[
\varepsilon(1+\varepsilon)\lambda^2+r(1+\varepsilon)\lambda+1.
\]
For all sufficiently small \(\varepsilon>0\), its roots are real and distinct: the slow root tends to \(-1/r\), while the fast root is asymptotic to \(-r/\varepsilon\). Explicitly, writing \(d_\varepsilon=\sqrt{r^2(1+\varepsilon)^2-4\varepsilon(1+\varepsilon)}\),
\[
\lambda_s=-\frac2{r(1+\varepsilon)+d_\varepsilon},\qquad
\lambda_f=\frac{-r(1+\varepsilon)-d_\varepsilon}{2\varepsilon(1+\varepsilon)}.
\]
Since \(u(0)=1\) and \(u'(0)=-1/[r(1+\varepsilon)]\), the fast-mode coefficient is
\[
B_\varepsilon=\frac{-1/[r(1+\varepsilon)]-\lambda_s}{\lambda_f-\lambda_s}=O(\varepsilon^2).
\]
Thus \(u_\varepsilon(t)=(1-B_\varepsilon)e^{\lambda_s t}+B_\varepsilon e^{\lambda_f t}\), and \(v_\varepsilon(t)=-(1+\varepsilon)u_\varepsilon'(t)\). This proves \(x_\varepsilon(h)\to(e^{-h/r},e^{-h/r}/r)^{\mathsf T}\); indeed the convergence is uniform for \(t\) in each fixed compact interval \([0,T]\).

**2. The exact split propagator.** Introduce
\[
\theta_\varepsilon=\frac h{2\sqrt{\varepsilon(1+\varepsilon)}},\quad
\delta_\varepsilon=\sqrt{\frac\varepsilon{1+\varepsilon}},\quad
q_\varepsilon=e^{-rh/\varepsilon},\quad c=\cos\theta_\varepsilon,\quad s=\sin\theta_\varepsilon.
\]
The conservative half-step and dissipative full-step are respectively
\[
C=\begin{pmatrix}c&-\delta_\varepsilon s\\s/\delta_\varepsilon&c\end{pmatrix},\qquad
D=\begin{pmatrix}1&0\\0&q_\varepsilon\end{pmatrix}.
\]
Direct multiplication gives the identity
\[
S_{\varepsilon,h}=CDC=
\begin{pmatrix}
c^2-q_\varepsilon s^2&-\delta_\varepsilon(1+q_\varepsilon)cs\\
(1+q_\varepsilon)cs/\delta_\varepsilon&q_\varepsilon c^2-s^2
\end{pmatrix}.
\]
For \(x(0)=(1,1/r)^{\mathsf T}\), this yields
\[
\begin{aligned}
(y_{\varepsilon,h})_1&=c^2-q_\varepsilon s^2-\frac{\delta_\varepsilon}{r}(1+q_\varepsilon)cs,\\
\sqrt\varepsilon (y_{\varepsilon,h})_2&=\sqrt{1+\varepsilon}(1+q_\varepsilon)cs+\frac{\sqrt\varepsilon}{r}(q_\varepsilon c^2-s^2).
\end{aligned}
\]
Because \(q_\varepsilon\to0\) exponentially and \(\delta_\varepsilon\to0\), the displayed scaled endpoint is \((c^2,cs)+o(1)\), where the error is uniform in the phase \(\theta_\varepsilon\).

**3. Cluster set and sharp bounds.** As \(\varepsilon\downarrow0\), \(\theta_\varepsilon\) ranges continuously and strictly monotonically through arbitrarily large values. Hence every phase modulo \(2\pi\) is attained along some \(\varepsilon\)-sequence tending to zero. The image \(\theta\mapsto(\cos^2\theta,\cos\theta\sin\theta)\) is exactly the claimed circle, by
\[
(\cos^2\theta-\tfrac12)^2+\cos^2\theta\sin^2\theta=\tfrac14.
\]
Let \(t=e^{-h/r}\in(0,1)\). By step 1, the exact regularized endpoint, after scaling the algebraic coordinate by \(\sqrt\varepsilon\), tends to \((t,0)\). Since \(E_\varepsilon=\operatorname{diag}(1+\varepsilon,\varepsilon)\), the *squared* energy-norm difference differs by \(o(1)\), uniformly in phase, from
\[
(\cos^2\theta-t)^2+\cos^2\theta\sin^2\theta
=t^2+(1-2t)\cos^2\theta.
\]
Its minimum and maximum over \(0\le\cos^2\theta\le1\) are \(\min(t^2,(1-t)^2)\) and \(\max(t^2,(1-t)^2)\), respectively. Every extreme phase recurs as \(\varepsilon\downarrow0\), proving the two *equalities*, not merely inequalities. If \(t=1/2\), the phase-dependent term vanishes identically, proving the claimed ordinary limit \(1/2\).

**4. Energy contraction despite the error.** The conservative generator \(E_\varepsilon^{-1}J\) satisfies \((E_\varepsilon^{-1}J)^{\mathsf T}E_\varepsilon+E_\varepsilon(E_\varepsilon^{-1}J)=0\), so \(C^{\mathsf T}E_\varepsilon C=E_\varepsilon\). The dissipative subflow \(D\) satisfies \(D^{\mathsf T}E_\varepsilon D\preceq E_\varepsilon\) because \(0<q_\varepsilon\le1\). Applying these inequalities in composition proves \(S_{\varepsilon,h}^{\mathsf T}E_\varepsilon S_{\varepsilon,h}\preceq E_\varepsilon\). Thus energy dissipation is fully compatible with the nonvanishing approximation error.

## Verification

The included `verify.py` uses standard Python only. It rederives the \(2\times2\) product by independent matrix multiplication; checks the explicit eigenmode solution and limiting circular geometry for four \((h,r)\) choices, twenty phase/scale combinations each; and tests the two sharp extrema and the phase-independent \(h=r\log2\) boundary. Execution returns:

`VERIFY_OK exact split matrix; regularized-flow eigenvalues; 80 phase tests; sharp energy-norm envelope`

These 80 numerical tests corroborate the exact algebra and asymptotics. The universal theorem depends on the analytic proof above, not on finite sampling.

## Relationship to prior work

Bartel, Diab, Frommer and Günther, *Operator splitting for semi-explicit differential-algebraic equations and port-Hamiltonian DAEs* (arXiv:2308.16736, first available 2023-08-31), formulate \(E_\varepsilon=E+\varepsilon I\), partition the generator into conservative and dissipative parts, and describe the fixed-\(\varepsilon\) Strang approximation and energy structure. Their finite-step convergence considerations do not address uniform accuracy under the singular \(\varepsilon\downarrow0\) limit. The present result supplies an exact, natural minimal-dimension obstruction with a full endpoint cluster set and sharp nonzero error accumulation values.

Frommer, Günther, Liljegren-Sailer and Marheineke (arXiv:2304.01766) analyze geometric splitting for nonsingular port-Hamiltonian ODEs. Bartel, Günther, Jacob and Reis (arXiv:2208.03574) study operator-splitting **dynamic iterations** for descriptor systems. Neither method identifies the present fixed-step singular-mass Strang cluster phenomenon. General stiff-splitting order reduction is known (e.g., Faou, Ostermann and Schratz, 2015), but the exact circle and sharp regularized-energy error for this DAE are not immediate consequences of those results.

## Limitations

The result is for one two-state linear index-one DAE with consistent data, zero input, a positive damping parameter, regularization by \(E+\varepsilon I\), and a **single** exact-conservative/dissipative Strang step at fixed \(h>0\). It makes no claim about the original paper's *other* coupled-DAE decompositions, implicit-midpoint subsolver behavior, alternative regularizations, or accuracy when \(h\) decreases suitably with \(\varepsilon\). Only a best-knowledge literature comparison is available; independent originality and correctness verification have not been performed.

## References

1. A. Bartel, M. Diab, A. Frommer, M. Günther, *Operator splitting for semi-explicit differential-algebraic equations and port-Hamiltonian DAEs*, arXiv:2308.16736 (first public 2023-08-31), https://arxiv.org/abs/2308.16736.
2. A. Frommer, M. Günther, B. Liljegren-Sailer, N. Marheineke, *Operator splitting for port-Hamiltonian systems*, arXiv:2304.01766 (2023), https://arxiv.org/abs/2304.01766.
3. A. Bartel, M. Günther, B. Jacob, T. Reis, *Operator Splitting Based Dynamic Iteration for Linear Port-Hamiltonian Systems*, arXiv:2208.03574 (2022), https://arxiv.org/abs/2208.03574.
4. E. Faou, A. Ostermann, K. Schratz, *Analysis of exponential splitting methods for inhomogeneous parabolic equations*, IMA J. Numer. Anal. 35 (2015), 161–178, https://doi.org/10.1093/imanum/dru002.
