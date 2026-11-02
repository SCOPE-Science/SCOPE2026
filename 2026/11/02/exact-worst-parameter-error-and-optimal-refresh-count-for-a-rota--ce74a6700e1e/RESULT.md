# Exact worst-parameter error and optimal refresh count for a rotating Gaussian range sketch

## Finding

Fix \(0<\varepsilon<1\), let \(R_\theta\) be planar counterclockwise rotation, and put
\[
A_\theta=R_\theta\begin{pmatrix}1&0\\0&\varepsilon\end{pmatrix}R_\theta^{\mathsf T},\qquad 0\le\theta\le\Theta.
\]
Choose a single real standard Gaussian vector \(g\in\mathbb R^2\), use it for every parameter value, and form the rank-one randomized range approximation
\[
\widehat A_\theta=P_{A_\theta g}A_\theta,
\qquad P_v=vv^{\mathsf T}/(v^{\mathsf T}v).
\]
The best rank-one squared Frobenius error is \(\varepsilon^2\) for every \(\theta\). Define the random worst-parameter relative squared error
\[
Z_\Theta=\sup_{0\le\theta\le\Theta}
\frac{\|A_\theta-\widehat A_\theta\|_F^2}{\varepsilon^2}.
\]
For every \(1\le x<\varepsilon^{-2}\), set
\[
q_\varepsilon(x)=\frac2\pi\arccos\sqrt{\frac{x^{-1}-\varepsilon^2}{1-\varepsilon^2}}.
\]
Then the **exact distribution** is
\[
\Pr\{Z_\Theta\le x\}=\left(q_\varepsilon(x)-\frac{\Theta}{\pi}\right)_+,
\quad 1\le x<\varepsilon^{-2},
\]
with probability zero below \(1\), probability one at or above \(\varepsilon^{-2}\), and an atom of mass \(\min\{\Theta/\pi,1\}\) at \(\varepsilon^{-2}\). Here \((u)_+=\max\{u,0\}\). For \(0\le\Theta\le\pi\), the **exact expected worst-parameter error factor** is
\[
\boxed{\mathbb E Z_\Theta=\frac{\Theta}{\pi\varepsilon^2}
+\frac{2}{\pi\varepsilon}\arctan\!\left(\frac{\tan((\pi-\Theta)/2)}{\varepsilon}\right)},
\]
with the arctangent evaluated by its endpoint limit at \(\Theta=0\); equivalently \(\mathbb EZ_0=\varepsilon^{-1}\). For \(\Theta\ge\pi\), \(Z_\Theta=\varepsilon^{-2}\) almost surely. In particular, for fixed \(0<\Theta<\pi\),
\[
\mathbb E Z_\Theta=\frac{\Theta}{\pi\varepsilon^2}+\frac1\varepsilon+O_\Theta(1)
\quad\text{as }\varepsilon\downarrow0,
\]
whereas the expectation at any **one fixed parameter** is exactly \(\varepsilon^{-1}\).

There is also a sharp **preassigned independent-sketch refresh law**. Partition the angular interval into \(K\ge1\) positive-length consecutive intervals of lengths \(\ell_1,\ldots,\ell_K\) summing to \(\Theta>0\). Draw an independent isotropic nonzero direction on each interval, keeping that direction fixed within its interval. For \(1<x<\varepsilon^{-2}\), write \(q=q_\varepsilon(x)\) and \(t=\Theta/\pi\). The probability that the squared relative error is at most \(x\) **simultaneously at every parameter** is exactly
\[
\prod_{j=1}^K\left(q-\frac{\ell_j}{\pi}\right)_+.
\]
At fixed \(K\), its maximum over deterministic partitions equals
\[
\boxed{S_K(x,\Theta)=\left(q-\frac{t}{K}\right)_+^K};
\]
when this maximum is positive, equality holds only for equal angular lengths. The best finite integer number of sketches is specified as follows. Let
\[
z_q=-W_{-1}(-q/e)>1,\qquad
k_c=\frac{t z_q}{q(z_q-1)},
\]
where \(W_{-1}\) is the lower real Lambert-\(W\) branch. The maximizing integer \(K\) is among the admissible integers bracketing \(k_c\), after imposing \(K\ge1\) and \(K>t/q\). There is a unique positive maximizing **real** value \(k_c\), while adjacent integers may tie. In particular, repeated refreshing indefinitely is suboptimal. When \(t\to\infty\) at fixed \(q\in(0,1)\),
\[
\max_{K\ge1} S_K=\exp\left(-\frac{tz_q}{q}+O_q(t^{-1})\right).
\]
Thus the optimal count grows linearly with angular excursion, with an explicit tolerance-dependent density. For two equal segments compared with one unrefreshed sketch, in the range \(0<t<q\) two segments succeed more often precisely when
\[
t>2\big(\sqrt{1-q}-(1-q)\big).
\]

## Assumptions and scope

All matrix computations use exact real arithmetic. The Gaussian probe is independent of the deterministic matrix family. The same laws hold for any nonzero rotationally invariant random vector in \(\mathbb R^2\), since only its uniform projective direction matters. The matrix family has two fixed positive singular values and rotates monotonically through angular length \(\Theta\); its first rank-one target is not oversampled. Refresh intervals and their number are selected before the random probes, and the refreshed probes are mutually independent. The probability target is a specified relative **squared Frobenius** threshold \(x\), not a spectral-error or expected-cost criterion. The Lambert-\(W\) optimization concerns independent preassigned restarts and does not address adaptive refresh policies, probe selection based on observations, or additional columns per sketch.

## Proof

**1. Pointwise algebra.** In the rotating eigenbasis, write \(R_\theta^{\mathsf T}g=(u,v)^{\mathsf T}\), and let \(D=\operatorname{diag}(1,\varepsilon)\). Orthogonal projection onto \(D(u,v)^{\mathsf T}\) yields
\[
\begin{aligned}
\|D-P_{D(u,v)}D\|_F^2
&=1+\varepsilon^2-\frac{u^2+\varepsilon^4v^2}{u^2+\varepsilon^2v^2}\\
&=\varepsilon^2\frac{u^2+v^2}{u^2+\varepsilon^2v^2}.
\end{aligned}
\]
Write \(g=\|g\|(\cos\phi,\sin\phi)^{\mathsf T}\). For any nonzero probe, therefore,
\[
E_\theta(g):=\frac{\|A_\theta-P_{A_\theta g}A_\theta\|_F^2}{\varepsilon^2}
=\frac{1}{\cos^2(\phi-\theta)+\varepsilon^2\sin^2(\phi-\theta)}.
\]
The projective angle \(\phi\bmod\pi\) is uniform on a circle of circumference \(\pi\).

**2. The sharp distribution and its atom.** For \(1\le x<\varepsilon^{-2}\), put
\[
\delta=\sqrt{\frac{x^{-1}-\varepsilon^2}{1-\varepsilon^2}},
\quad \alpha=\arccos\delta\in[0,\pi/2).
\]
The inequality \(E_\theta\le x\) says that \(\phi\bmod\pi\) lies in the closed arc of angular radius \(\alpha\) centered at \(\theta\bmod\pi\). To hold for all \(\theta\) in a continuously traversed arc of length \(\Theta\), the projective angle must belong to the intersection of all these arcs. Its length is exactly \((2\alpha-\Theta)_+\) for \(\Theta<\pi\), and zero for \(\Theta\ge\pi\). Division by \(\pi\) proves the distribution. At \(x=\varepsilon^{-2}\), the pointwise ratio is always no larger than this upper bound. The left limit of the distribution is \((1-\Theta/\pi)_+\); hence the jump has mass \(\min\{\Theta/\pi,1\}\). In particular a halfturn forces the maximal relative error for every nonzero probe.

**3. Exact mean and singular-value limit.** For \(0\le\Theta\le\pi\), the projective angle has probability \(\Theta/\pi\) of hitting a perfectly transverse direction during the sweep. On the complement, its shortest distance \(d\) from the traversed orthogonality arc has density \(2/\pi\) on \((0,(\pi-\Theta)/2)\). Therefore
\[
\mathbb E Z_\Theta
=\frac{\Theta}{\pi\varepsilon^2}
+\frac2\pi\int_0^{(\pi-\Theta)/2}
\frac{\mathrm dd}{\varepsilon^2+(1-\varepsilon^2)\sin^2d}.
\]
Substituting \(u=\tan d\) makes the integrand \(\mathrm du/(\varepsilon^2+u^2)\) and evaluates the integral exactly as stated. At \(\Theta=0\) take the integral's endpoint limit. For fixed \(0<\Theta<\pi\), expanding \(\arctan(\tan((\pi-\Theta)/2)/\varepsilon)\) at \(\varepsilon=0\) yields the displayed two leading orders. A fixed-parameter expectation is the \(\Theta=0\) case, by rotational invariance.

**4. Independent refresh and equal partitions.** For each interval the same arc argument, translated to its starting angle, gives success probability \((q-\ell_j/\pi)_+\). Mutual independence gives their product. If \(t\ge Kq\), every partition has at least one factor zero. If \(t<Kq\), the arithmetic-geometric mean inequality yields
\[
\prod_{j=1}^K\left(q-\frac{\ell_j}{\pi}\right)
\le\left(q-\frac{t}{K}\right)^K,
\]
with equality only for equal lengths. A zero factor cannot improve this positive upper bound.

**5. Unique continuous optimum and integer rounding.** For fixed \(q\in(0,1)\), \(t>0\), extend the log-success objective to real \(k>t/q\):
\[
f(k)=k\log(q-t/k).
\]
Put \(u=t/(qk)\). Direct differentiation gives
\[
f'(k)=\log(q(1-u))+\frac{u}{1-u},
\qquad f''(k)=-\frac{u^2}{k(1-u)^2}<0.
\]
The first derivative decreases continuously from \(+\infty\) at the lower domain boundary to \(\log q<0\) at infinity, so it has a unique root. With \(z=(1-u)^{-1}>1\), the root equation becomes \(z e^{-z}=q/e\), whose unique \(z>1\) solution is \(-W_{-1}(-q/e)\). Solving \(u=t/(qk)\) gives \(k_c\). Strict concavity and integer monotonicity on either side prove the rounding characterization. The exact continuous optimum has \(f(k_c)=-tz_q/q\), while the second derivative near \(k_c\) is \(O_q(t^{-1})\). Rounding to a nearby feasible integer therefore changes \(\log S_K\) by \(O_q(t^{-1})\) as \(t\to\infty\). For \(K=1,2\), subtracting \((q-t)\) from \((q-t/2)^2\) and taking its unique positive root gives the stated two-segment threshold.

## Verification

The standalone standard-library script `verify.py` independently assembles the \(2\times2\) matrices and checks the exact projected residual against the scalar formula. It also compares analytic CDFs and expectations with deterministic projective-angle quadrature, checks brute-force maximization over a time mesh, verifies equal-partition dominance across many unequal partitions, and searches over integer refresh counts against the strict-concavity/Lambert-branch prediction. It checks boundary cases including \(\Theta=\pi\), but finite computations are not substitutes for the preceding analytic arguments. Run `python verify.py` after extracting it from the same finding package.

## Relationship to prior work

Kressner and Lam (2023, arXiv:2302.12761) introduce constant Gaussian dimension-reduction matrices for parameter-dependent low-rank approximation and give expectation and uniform-norm upper bounds. Their uniform analysis is for an oversampled regime (in the stated Theorem 12, \(r\ge2\), \(p\ge4\)) and does not imply the present exact one-column angular distribution, its maximal-error atom, or the optimal independent-refreshed partition. Halko, Martinsson and Tropp (2009/2011, arXiv:0909.4061) establish the foundational randomized range-projection algorithm and single-matrix analyses. Epperly and Webber (2026, arXiv:2605.19096) obtain sharp expected-error results for a single matrix and minimax rotation-invariant embeddings, not the joint worst-parameter law for reuse. The fixed-matrix expectation \(\mathbb E\|A-P_{Ag}A\|_F^2=\varepsilon\) is consistent with previously known planar isotropic calculations; the new object here is the random supremum over a continuously rotated family together with the renewal policy.

## Limitations

The exact law uses a real two-dimensional SPD orbit, one sketch vector, fixed singular values, and exact arithmetic. It does not establish a guarantee for larger target rank, oversampling, variable singular values, arbitrary parameter paths, or adaptive or correlated resketching. The integer optimum is allowed to tie between two neighboring integers; the positive equal-width optimum is uniquely attained only when its success probability is nonzero. The analysis is a same-study mathematical result, not independent validation. Specialized published prior work may contain equivalent arc-covering formulas or an earlier application to rotating sketches; any such overlap would limit the originality claim.

## References

1. D. Kressner and H. Y. Lam, *Randomized low-rank approximation of parameter-dependent matrices*, arXiv:2302.12761, first posted 2023-02-24. https://arxiv.org/abs/2302.12761
2. N. Halko, P.-G. Martinsson and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, arXiv:0909.4061, first posted 2009-09-22, SIAM Review 53 (2011). https://arxiv.org/abs/0909.4061
3. E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096, first posted 2026-05-18. https://arxiv.org/abs/2605.19096
