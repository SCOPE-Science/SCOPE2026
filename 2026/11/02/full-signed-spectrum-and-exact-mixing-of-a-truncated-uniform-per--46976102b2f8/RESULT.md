# Full signed spectrum and exact mixing of a truncated uniform persistence chain

## Finding

For every fixed \(0<a<1\), consider the Markov chain obtained by conditioning consecutive independent uniform \([-a,1]\) innovations to satisfy \(X_j+X_{j+1}>0\) indefinitely. Let \(P_a\) be its limiting Doob transition kernel. Define \(r=(1-a)/a\) and, for each integer \(k\), let \(t_k\) be the unique real solution of
\[
\cot(t_k+\pi/4)=rt_k,\qquad k\pi-\pi/4<t_k<(k+1)\pi-\pi/4.
\]
The compact killed transfer operator has exactly the following nonzero eigenvalues, all simple:
\[
\lambda_k=\frac{a}{(1+a)t_k},\qquad k\in\mathbb Z.
\]
Its zero eigenspace consists precisely of the functions vanishing almost everywhere on \((-a,a)\) and of integral zero on \((a,1]\). Thus zero also belongs to the spectrum as an eigenvalue of infinite multiplicity.

Define
\[
 h(x)=\begin{cases}
 \cos(t_0x/a)+\sin(t_0x/a),&-a\le x\le a,\\
 \cos t_0+\sin t_0,&a<x\le1,
 \end{cases}
\quad C_a=2a+(1-a)(\cos t_0+\sin t_0)^2.
\]
Then \(h>0\); \(P_a\) is reversible and has unique stationary density \(\pi_a(x)=h(x)^2/C_a\). For every integer \(n\ge1\), its *exact sharp* centered Hilbert-space mixing norm is
\[
\boxed{\|P_a^n-\Pi_a\|_{L^2(\pi_a)\to L^2(\pi_a)}
 =\rho(a)^n,\qquad \rho(a)=\frac{t_0}{|t_{-1}|}.}
\]
Here \(\Pi_a f=\int f\,d\pi_a\). The extremizing mode is \(\phi_{-1}/h\), with eigenvalue \(-\rho(a)\). At the two support boundaries,
\[
\rho(a)\sim \frac{4a}{\pi}\quad(a\downarrow0),\qquad
\rho(a)\longrightarrow\frac13\quad(a\uparrow1).
\]
These are formulas for the strictly truncated regime \(0<a<1\), not claims about all moving-average parameters.

## Assumptions and scope

The innovations \(X_j\) are independent with density \(1/(1+a)\) on \([-a,1]\); the moving average is \(Z_j=X_j+X_{j+1}\), corresponding to coupling \(\theta=-1\) in the convention \(Z_j=X_{j+1}-\theta X_j\). Conditioning on strictly positive consecutive \(Z_j\) yields the one-step killed operator acting on \(L^2([-a,1],dx)\):
\[
(K_af)(x)=\frac1{1+a}\int_{-a}^1\mathbf 1_{\{x+y>0\}}f(y)\,dy.
\]
The established persistence theory identifies the principal positive eigenpair of this operator as the input for the infinite-horizon Doob transform. We analyze the entire signed spectrum and stationary convergence of this explicit transform. All eigenvalue, stationarity, and mixing statements hold for every *real* \(a\in(0,1)\), with fixed \(a\) and no finite-state discretization.

## Proof

**1. Eigenvalue reduction.** The kernel is symmetric and square integrable, hence \(K_a\) is compact self-adjoint. If \(K_af=\lambda f\) with \(\lambda\ne0\), then \(f\) has a continuous representative, constant on \([a,1]\), and for almost every \(-a<x<a\), differentiation gives
\[
\lambda f'(x)=\frac{f(-x)}{1+a}.
\]
Put \(\beta=1/((1+a)\lambda)\). It follows that \(f''+\beta^2f=0\) and \(f'(0)=\beta f(0)\), so every nonzero eigenfunction is proportional to
\[
\phi_t(x)=\begin{cases}
\cos(tx/a)+\sin(tx/a),& -a\le x\le a,\\
\cos t+\sin t,&a<x\le1,
\end{cases}
\qquad t=a\beta.
\]
At \(x=-a\), only the plateau \((a,1]\) contributes; the boundary equation is
\[
\lambda\phi_t(-a)=\frac{1-a}{1+a}\phi_t(a).
\]
Substituting \(\lambda=a/((1+a)t)\) and the trigonometric values gives
\[
\cos t-\sin t=\frac{1-a}{a}t(\cos t+\sin t),
\]
which is precisely \(\cot(t+\pi/4)=rt\). Conversely, any real solution gives an exact eigenpair: \(K_a\phi_t-\lambda\phi_t\) has zero derivative on \((-a,a)\), is constant for \(x\ge a\), is continuous at \(a\), and vanishes at \(-a\) by the same boundary equation. No additional eigenvalues are possible.

**2. All roots and the nullspace.** On each interval \((k\pi-\pi/4,(k+1)\pi-\pi/4)\), the function \(t\mapsto\cot(t+\pi/4)-rt\) is strictly decreasing from \(+\infty\) to \(-\infty\). Therefore there is exactly one root \(t_k\), with no repeated nonzero eigenvalues. If \(K_af=0\), differentiating shows \(f=0\) almost everywhere on \((-a,a)\); the remaining constant value of \(K_af\) vanishes precisely when \(\int_a^1 f(y)\,dy=0\). This characterizes the entire nullspace (including its infinite dimension).

**3. Principal eigenpair and reversibility.** The root \(t_0\) lies strictly between \(0\) and \(\pi/4\). Thus \(h=\phi_{t_0}\) is positive everywhere. Direct integration gives \(\int_{-a}^1h^2dx=C_a\), since the odd cross term integrates to zero on \([-a,a]\). The Doob kernel is
\[
P_a(x,dy)=\frac{\mathbf1_{\{x+y>0\}}}{(1+a)\lambda_0}\frac{h(y)}{h(x)}dy.
\]
It is stochastic because \(K_ah=\lambda_0h\). The measure \(\pi_a(x)dx=h(x)^2dx/C_a\) satisfies detailed balance:
\[
\pi_a(x)P_a(x,dy)\,dx
=\frac{\mathbf1_{\{x+y>0\}}h(x)h(y)}{C_a(1+a)\lambda_0}\,dx\,dy,
\]
which is symmetric. The kernel of \(K_a^2\) is strictly positive almost everywhere: for each \(x,y\in[-a,1]\), the allowable intermediate interval extends above \(\max(-x,-y)\le a<1\). Hence the positive top mode is simple and strictly dominant in modulus, and the invariant probability is unique.

**4. Sharp contraction.** Multiplication by \(h/\sqrt{C_a}\) is a unitary map from \(L^2(\pi_a)\) to \(L^2(dx)\), conjugating \(P_a\) to \(K_a/\lambda_0\). Root ordering gives
\[
0<t_0<\pi/4,
\quad -3\pi/4<t_{-1}<-\pi/4,
\quad t_1>3\pi/4,
\]
and all other \(|t_k|\) exceed \(|t_{-1}|\). Therefore the largest modulus among nonprincipal eigenvalues of \(P_a\) is \(|\lambda_{-1}/\lambda_0|=t_0/|t_{-1}|\). The self-adjoint spectral theorem gives the displayed exact operator norm at every integer \(n\ge1\). Equality is attained by the nonconstant normalized eigenmode \(\phi_{t_{-1}}/h\), whose sign alternates between steps.

**5. Boundary scaling.** Write \(r=(1-a)/a\). As \(a\downarrow0\), the equation for the positive root implies \(rt_0\to1\), hence \(t_0/a\to1\). For the first negative root \(t_{-1}\to-\pi/4\), yielding \(\rho(a)/a\to4/\pi\). As \(a\uparrow1\), \(r\to0\); continuity of the roots in their monotonicity intervals gives \(t_0\to\pi/4\) and \(t_{-1}\to-3\pi/4\), and therefore \(\rho(a)\to1/3\). All statements are limits of explicit identities, rather than inferences from finite numerical calculations.

## Verification

The included standalone `checker.py` computes roots by interval bisection and checks the integral eigenvalue equation, normalization, pairwise eigenfunction orthogonality, detailed balance, spectral ordering and endpoint behavior for an explicit set of parameters and spatial grid values. Run `python3 checker.py` with standard Python 3; compare its output to `checker_output.txt`. The recorded run passed 14,206 finite deterministic assertions. These finite diagnostics are not the proof of completeness, absence of other eigenvalues, or infinite-dimensional mixing; those follow from the reduction and spectral argument above.

## Relationship to prior work

Aurzada and Raschel, *Persistence probabilities for MA(1) sequences with uniform innovations* (arXiv:2507.04427, first posted 2025-07-06), provide persistence generating functions in parameter regimes including the present one. Aurzada and Worf, *MA(1) processes with uniform innovations conditioned to stay positive in the non-expanding regime* (arXiv:2606.01832, first posted 2026-06-01), construct the limiting Doob chain and identify the principal eigenfunction and persistence exponent; their Remark 2 describes its invariant density through left and right eigenfunctions. In the symmetric \(\theta=-1\) case this already implies a density proportional to \(h^2\) once normalized, so that observation alone is not claimed as novel. The assessed addition is the **complete nonzero signed spectrum and explicit nullspace for \(0<a<1\)**, with the **exact sharp nontrivial mixing eigenvalue and its truncated-support scaling**. The earlier \(a\ge1\) case is a separate support regime and is not claimed as new. Generic compact self-adjoint spectral theory explains why eigenvalue ratios govern mixing, but does not itself evaluate the particular transcendental roots or their parameter asymptotics.

## Limitations

This theorem addresses \(\theta=-1\), \(0<a<1\), the infinite-horizon conditioned chain, and the centered \(L^2\) operator norm. It makes no statement for other couplings, expanding supports \(a\ge1\), total-variation norms starting from individual points, or sharp constants in unconditioned survival probabilities. It does not establish a historical uniqueness claim across every unindexed spectral or moving-average reference. The existing literature's principal eigenpair and the classical spectral theorem remain essential inputs, not independent contributions of this result.

## References

1. F. Aurzada and K. Raschel, *Persistence probabilities for MA(1) sequences with uniform innovations*, arXiv:2507.04427v1 (2025-07-06), https://arxiv.org/abs/2507.04427.
2. F. Aurzada and V. Worf, *MA(1) processes with uniform innovations conditioned to stay positive in the non-expanding regime*, arXiv:2606.01832v1 (2026-06-01), https://arxiv.org/abs/2606.01832.
