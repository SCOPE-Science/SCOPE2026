# Four Gauss–Legendre Nodes Are the Minimal Resonance-Free Quadrature for a Planar Controllability Gramian

## Finding

Consider the finite-time controllability Gramian of a rank-one forced planar rotation, optionally with scalar damping. **Among the one-, two-, three-, and four-node standard Gauss–Legendre quadratures, four nodes are the first that guarantee a strictly positive-definite approximation for every positive step length.** The lower-node rules have infinite explicit sets of singular step lengths, despite the exact Gramian being positive definite for every positive step. The four-node rule avoids exact singularity but, for zero damping, has arbitrarily poorly conditioned normalized Gramians at a sequence of large steps: their least eigenvalue is bounded above by an explicit inverse-square sequence, while the normalized exact Gramian converges to half the identity.

More precisely, let \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), \(A=-\gamma I+\omega J\), \(b=(1,0)^{\mathsf T}\), where \(\gamma\ge0\) and \(\omega\in\mathbb R\setminus\{0\}\). For \(h>0\), define
\[
W(h)=\int_0^h e^{tA}bb^{\mathsf T}e^{tA^{\mathsf T}}\,dt,
\qquad
G_s(h)=h\sum_{j=1}^s w_{s,j}e^{h c_{s,j}A}bb^{\mathsf T}e^{h c_{s,j}A^{\mathsf T}},
\]
where \(c_{s,j}\in(0,1)\) and \(w_{s,j}>0\) are the usual Gauss–Legendre nodes and weights scaled to \([0,1]\) (thus their weights sum to one). Then \(W(h)\succ0\) for all \(h>0\), whereas
\[
\begin{aligned}
\operatorname{rank}G_1(h)&=1,\\
G_2(h)\text{ is singular}&\iff |\omega|h\in\pi\sqrt3\,\mathbb N,\\
G_3(h)\text{ is singular}&\iff |\omega|h\in\frac{10\pi}{\sqrt{15}}\,\mathbb N,\\
G_4(h)&\succ0\qquad\text{for every }h>0.
\end{aligned}
\]
Here \(\mathbb N=\{1,2,3,\ldots\}\). These statements hold for every allowed damping parameter.

For \(\gamma=0\), put
\[
a=\sqrt{\frac{15+2\sqrt{30}}{35}},\quad
b_0=\sqrt{\frac{15-2\sqrt{30}}{35}},\quad
\alpha=\frac{a}{b_0}.
\]
There are infinitely many coprime positive integers \((p_k,q_k)\) with \(q_k\to\infty\) and \(|q_k\alpha-p_k|<1/q_k\). At the steps
\[
h_k=\frac{2\pi q_k}{|\omega|b_0},
\]
the four-node quadrature satisfies
\[
0<\lambda_{\min}\!\left(\frac{G_4(h_k)}{h_k}\right)
\le\frac{\pi^2}{q_k^2},
\qquad
\kappa_2\!\left(\frac{G_4(h_k)}{h_k}\right)
\ge\frac{q_k^2}{2\pi^2},
\]
and
\[
\lim_{k\to\infty}
\left\|\frac{G_4(h_k)}{h_k}-\frac{W(h_k)}{h_k}\right\|_2
=\frac12.
\]
Thus exact strict positivity does not imply uniform coercivity or accuracy on unbounded oscillation intervals.

## Assumptions and scope

All matrices are real and all statements concern exact arithmetic. The quadrature is applied directly to the **variation-of-constants integral**, not an implicit Gauss–Legendre Runge–Kutta discretization of the matrix differential equation. The initial Lyapunov state is zero, the forcing covariance is the fixed rank-one matrix \(bb^{\mathsf T}\), the angular frequency is nonzero, and the scalar damping is nonnegative. The inverse-square estimate and normalized-error limit are stated only at zero damping. No assertion about arbitrary stable matrices, higher dimensions, other quadrature families, or finite precision is made.

## Proof

**1. Exact Gramian and a rank criterion.** Since \(J^{\mathsf T}=-J\), write
\[
v(\phi)=(\cos\phi,\sin\phi)^{\mathsf T}.
\]
The integrand is \(e^{-2\gamma t}v(\omega t)v(\omega t)^{\mathsf T}\). If a real vector \(z\ne0\) satisfied \(z^{\mathsf T}W(h)z=0\), continuity and nonnegativity would give \(z^{\mathsf T}v(\omega t)=0\) at every \(t\in[0,h]\). At \(t=0\) and at any sufficiently small \(t>0\) with \(\sin(\omega t)\ne0\), these vectors span the plane, a contradiction. Hence \(W(h)\succ0\).

For a positive-weight quadrature, define \(\theta=\omega h\). The Cauchy–Binet determinant identity is
\[
\boxed{\quad
\frac{\det G_s(h)}{h^2}=
\sum_{1\le i<j\le s}
 w_{s,i}w_{s,j}e^{-2\gamma h(c_{s,i}+c_{s,j})}
 \sin^2\!\big(\theta(c_{s,j}-c_{s,i})\big).
\quad}
\]
Every summand is nonnegative, and every coefficient is strictly positive. Consequently \(G_s(h)\) is singular precisely when the sampled angles \(\theta c_{s,j}\) all coincide modulo \(\pi\). This is a projective rank condition rather than ordinary quadrature polynomial exactness.

**2. Sharp node threshold.** The first Gauss–Legendre node set is a singleton, so its Gramian has rank one. For order two, the nodes are \(\frac12\pm\frac1{2\sqrt3}\), whose only difference is \(1/\sqrt3\); hence the stated singular times. For order three, the nodes are \(\frac12\) and \(\frac12\pm\sqrt{15}/10\). All angles agree modulo \(\pi\) exactly when \(|\theta|\sqrt{15}/10\) is an integer multiple of \(\pi\).

The four-node Gauss rule has Legendre abscissae \(\{\pm a,\pm b_0\}\), with \(a,b_0\) as above; its scaled nodes are \((1\pm a)/2\) and \((1\pm b_0)/2\). If its Gramian were singular, comparing the two outer nodes and then the two inner nodes would imply
\[
\theta a\in\pi\mathbb Z,
\qquad \theta b_0\in\pi\mathbb Z.
\]
Because \(\theta\ne0\), their quotient \(a/b_0\) would have to be rational. However,
\[
\frac{a^2}{b_0^2}
=\frac{23+4\sqrt{30}}7\notin\mathbb Q,
\]
so \(a/b_0\notin\mathbb Q\). This contradiction gives \(G_4(h)\succ0\) for all \(h>0\), independent of damping. The four-node rule is therefore the smallest standard Gauss–Legendre rule with this all-step property.

**3. Arbitrarily small normalized eigenvalues.** Now set \(\gamma=0\). The four-node Gramian has trace \(h\), since its weights sum to one. As \(\alpha=a/b_0\) is irrational, continued fractions provide infinitely many reduced fractions \(p_k/q_k\) satisfying \(|q_k\alpha-p_k|<1/q_k\), with \(q_k\to\infty\). At the specified step \(h_k\), the sampled inner directions have phases
\[
\frac{\omega h_k}2\pm\pi q_k\operatorname{sgn}(\omega),
\]
whereas the outer directions have phases
\[
\frac{\omega h_k}2\pm\pi q_k\alpha\operatorname{sgn}(\omega).
\]
Modulo \(\pi\), all four directions are within angle \(\pi/q_k\) of the common axis \(v(\omega h_k/2)\). Test the normalized Gramian against the unit vector perpendicular to that axis. Its Rayleigh quotient is at most \(\sin^2(\pi/q_k)\le\pi^2/q_k^2\), yielding the claimed bound on its least eigenvalue. Positivity from step 2 is strict. The trace-one property gives its largest eigenvalue at least \(1/2\), hence the condition-number lower bound.

Finally, direct trigonometric integration shows that, for every \(h>0\), the exact undamped Gramian obeys
\[
\operatorname{spec}\!\left(\frac{W(h)}h\right)
=\left\{\frac12\pm\frac{|\sin(\omega h)|}{2|\omega|h}\right\}.
\]
Therefore \(W(h_k)/h_k\to I/2\). Each normalized discrete Gramian is within operator norm \(O(1/q_k)\) of a rank-one orthogonal projector (its axis may rotate with \(k\)). The operator norm of any rank-one projector minus \(I/2\) is exactly \(1/2\), proving the normalized-error limit.

## Verification

The standalone file `verify.py` tests the first four Gauss rules' polynomial moments, node and weight positivity, a direct-matrix versus Cauchy–Binet determinant identity across damping and frequency choices, the exact two- and three-node resonances, the four-node algebraic root-ratio identity, continued-fraction near-resonances, inverse-square eigenvalue bounds, and the continuum eigenvalue identity. It uses only the Python standard library and reports 163 passed assertions. Finite floating-point checks provide reproducibility and numerical diagnostics, not a replacement for the universal arithmetic and matrix proofs above. The near-resonance limit is proved by continued-fraction theory, not inferred from the displayed samples.

## Relationship to prior work

Zhang, Lan, and Jing (2026) study positivity preservation for integrating-factor strong-stability-preserving Runge–Kutta discretizations of differential Lyapunov equations, proving positive **semidefiniteness** and error statements for their specified methods. Their integral representation motivates asking when positive-weight discretization also preserves **strict** positive definiteness of an exactly controllable planar system. The present analysis concerns a distinct direct Gauss–Legendre quadrature of the variation-of-constants integral, not a claim about the original methods.

Fúster-Sabater and Guillén (2010 arXiv version of earlier work), especially their sampled reachability determinant criteria, already establish the general principle that sampled controllability is governed by the rank of sampled modal vectors. That principle is used here, not claimed as new. What is classified here is the **particular Gauss–Legendre node hierarchy**, including exact singular-time sets, the irrational quartic-node obstruction to all exact resonances, and quantified near-singular behavior even though the continuum normalized Gramian approaches a well-conditioned limit. Standard Gaussian quadrature exactness and positive weights were known long before this calculation; neither implies this all-step classification without inspecting the node arithmetic.

## Limitations

The result establishes neither higher-dimensional positivity of a numerical Gramian nor a general step-size stability theorem. At four nodes it gives exact strict positivity but no uniformly positive spectral lower bound as the frequency–step product increases. Its inverse-square upper bound is achieved only on an infinite subsequence; it is not claimed to be a universal two-sided asymptotic law. Earlier sampled-system theory provides substantial conceptual overlap, and broader historical priority for the specific node-arithmetic classification has not been independently established.

## References

1. W. Zhang, R. Lan, and X. Jing, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation*, arXiv:2606.15703v1 (first posted 2026-06-14), https://arxiv.org/abs/2606.15703.
2. A. Fúster-Sabater and J. M. Guillén, *Characterisation of observability and controllability for nonuniformly sampled discrete systems*, arXiv:1006.4288v1 (2010); especially sampled-modal rank criteria, https://arxiv.org/abs/1006.4288.
3. L. N. Trefethen, *Exactness of Quadrature Formulas*, arXiv:2101.09501 (2021), https://arxiv.org/abs/2101.09501.
4. National Institute of Standards and Technology, *Digital Library of Mathematical Functions*, §3.5, Gaussian quadrature, https://dlmf.nist.gov/3.5.
