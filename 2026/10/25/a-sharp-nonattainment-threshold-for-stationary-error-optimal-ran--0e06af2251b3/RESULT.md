# A sharp nonattainment threshold for stationary-error-optimal randomized backward Euler

## Finding

The one-component-per-step randomized backward-Euler method for the scalar affine equation
\[
 u'(t)+3u(t)=1
\]
exhibits a sharp transition in optimal positive sampling probabilities. Decompose the drift and forcing as \(A_1u=2u\), \(f_1=1\), \(A_2u=u\), and \(f_2=0\). Independently select component 1 with probability \(p\in(0,1)\), or component 2 with probability \(1-p\), scaling each selected operator and forcing by the reciprocal selection probability. At each fixed step \(h>0\), the resulting affine random recursion has a unique invariant probability law. Let \(V_h(p)\) be its stationary expected squared distance to the exact equilibrium \(u_*=1/3\).

Define the polynomial
\[
P(h)=200h^5+5829h^4-1620h^3+528h^2-1008h-528.
\]
There is exactly one positive root, \(h_* = 0.7166725626567217698\ldots\). The following statements hold without asymptotic qualifications:

1. If \(0<h<h_*\), the function \(V_h(p)\) attains its minimum at at least one admissible probability \(p\in(0,1)\), and the minimum is strictly below \(1/36\).
2. If \(h=h_*\), exactly one admissible probability minimizes \(V_h(p)\), namely \(p_*=0.8029974025247708290\ldots\), and its risk is exactly \(1/36\).
3. If \(h>h_*\), every admissible probability satisfies \(V_h(p)>1/36\), while \(\inf_{0<p<1}V_h(p)=1/36\), approached only in the one-sided limit \(p\uparrow1\). Consequently no admissible probability minimizes the stationary error in this regime.

The endpoint \(p=1\) is **not** an admissible unbiased random splitting (component 2 is never selected); it is used solely as the limiting competitor. The transition concerns infinite-time stationary loss at fixed step size, not finite-horizon convergence or consistency under step refinement. The exact continuous-time equilibrium is independent of \(h\).

## Assumptions and scope

All quantities are real and calculations use exact arithmetic. For each \(h>0\) and \(p\in(0,1)\), independent component indices \(I_n\in\{1,2\}\) have probabilities \(\Pr(I_n=1)=p\), \(\Pr(I_n=2)=1-p\). Given \(U_n\), the numerical update solves
\[
 U_{n+1}+h\frac{A_{I_n}U_{n+1}}{\pi_{I_n}}
 =U_n+h\frac{f_{I_n}}{\pi_{I_n}},
 \qquad \pi_1=p,\quad\pi_2=1-p.
\]
Thus the expected sampled drift and forcing equal those of the full equation, and each iteration evaluates exactly one component. Write \(X_n=U_n-1/3\), \(q=1-p\), and
\[
\begin{aligned}
 X_{n+1}&=r_{I_n}X_n+c_{I_n},\\
 r_1&=\frac{p}{p+2h},&c_1&=\frac{h}{3(p+2h)},\\
 r_2&=\frac{q}{q+h},&c_2&=-\frac{h}{3(q+h)}.
\end{aligned}
\]
For each fixed pair \((h,p)\), both multiplicative coefficients lie strictly between zero and one. Coupling two chains with identical indices therefore contracts their difference geometrically; the bounded affine iterates admit a unique stationary distribution with finite moments. No Gaussian approximation is used.

## Proof

**Exact stationary moments.** Put \(R=pr_1+qr_2\) and \(R_2=pr_1^2+qr_2^2\). By independence of a fresh index from the current state, the stationary mean \(m=\mathbb E X\) satisfies \(m=Rm+pc_1+qc_2\), hence
\[
m=\frac{h(3p-2)}{3(2h+3pq)}.
\]
The two conditional centered images of the stationary mean differ by
\[
\Delta=(r_1-r_2)m+c_1-c_2=\frac{h}{2h+3pq}.
\]
Centering the affine recursion around \(m\), its stationary variance is exactly \(pq\Delta^2/(1-R_2)\). Therefore
\[
\boxed{V_h(p)=\frac{h^2(3p-2)^2}{9(2h+3pq)^2}
+\frac{pqh^2}{(2h+3pq)^2(1-R_2)}.}
\]
As \(p\downarrow0\), this tends to \(1/9\); as \(p\uparrow1\), it tends to \(1/36\). For every fixed \(0<p<1\),
\[
 V_h(p)=\frac{h}{54p(1-p)}+O(h^2)\quad(h\downarrow0).
\]
In particular, the small-step leading constant is minimized at equal sampling, even though the drift coefficients are unequal.

**The exact comparison polynomial.** Set
\[
\begin{aligned}
K(p,h)={}&-4h^3+(-6p^2+16p-8)h^2\\
&+9p^2(1-p)h+6p^2(1-p)^2,\\
T(p,h)={}&\frac{(p+2h)^2(1-p+h)^2}{h}(1-R_2)>0.
\end{aligned}
\]
Direct substitution and cancellation give the *exact* identity
\[
\boxed{V_h(p)-\frac1{36}=-\frac{(p+2h)(1-p)K(p,h)}{12(2h+3p(1-p))T(p,h)}.}
\]
All factors other than \(-K\) are strictly positive. Thus an admissible sampling probability strictly improves upon the limiting stationary loss \(1/36\) if and only if \(K(p,h)>0\).

**A unique crossing for each probability.** For fixed \(p\in(0,1)\), the cubic \(K(p,h)\), viewed as a polynomial in \(h\), has positive constant term \(6p^2(1-p)^2\), strictly negative leading coefficient, and positive coefficient of \(h\). Its nonzero coefficient sequence, in descending degree, has exactly one sign change irrespective of the sign of the quadratic coefficient. Descartes' rule of signs and continuity therefore give a unique positive *simple* root \(H(p)\), with \(K(p,h)>0\) exactly when \(0<h<H(p)\). Continuity of this root and the endpoint polynomials imply \(H(p)\to0\) as \(p\downarrow0\), and \(H(p)\to1/2\) as \(p\uparrow1\). The exact identity \(K(4/5,7/10)=73/1250>0\) shows \(H(4/5)>7/10\), so \(H\) has a global maximum at an interior probability.

**Algebraic maximum and uniqueness.** At an interior maximizer, both \(K=0\) and \(\partial_pK=0\). Exact polynomial elimination yields
\[
\operatorname{Res}_p(K,\partial_pK)
=-2592h^4(3h+1)^2 P(h).
\]
For \(h\ge0\),
\[
P''(h)=4000h^3+69948h^2-9720h+1056>0,
\]
because the quadratic portion has negative discriminant \(-200981952\) and positive leading coefficient. Since \(P(0)=-528\), \(P'(0)=-1008\), and \(P(h)\to+\infty\), the polynomial \(P\) has exactly one positive root. Exact rational evaluations give \(P(7/10)<0<P(3/4)\). Hence the global maximum of \(H\) equals this root \(h_*\).

For \(7/10<h<3/4\), the quadratic \(\partial_p^2K\) is positive at \(p=0\) and negative at \(p=1\), with positive leading coefficient, so it has exactly one zero on \((0,1)\). Thus \(\partial_pK\) first increases and then decreases. Because \(\partial_pK(0,h)=16h^2>0\) and \(\partial_pK(1,h)=h(4h-9)<0\), it has exactly one zero in \((0,1)\), the unique maximizer \(p_*\) of \(K(\cdot,h_*)\). At this point \(K(p_*,h_*)=0\); at every other interior probability it is negative.

Finally, if \(h<h_*\) some probability has \(K>0\), so \(V_h(p)<1/36\) there; continuity on \([0,1]\) after adjoining the endpoint limits guarantees an attained interior minimum. At \(h=h_*\) only \(p_*\) attains \(1/36\) in the open interval. For \(h>h_*\), \(K<0\) at every interior probability, so all risks exceed \(1/36\), while their limit at \(p=1\) is \(1/36\). This proves the classification.

## Verification

The accompanying `verify.py` independently derives stationary mean and second moment in two forms, checks the rational risk-comparison identity and the exact resultant, checks root-bracketing inequalities, and evaluates 152 rational probability-step pairs using a second moment-recursion implementation. It reports `VERIFY_OK 481 exact/symbolic/numeric assertions` with SymPy installed. The polynomial sign/uniqueness and attainment arguments above, not the finite sample grid or approximate roots, establish the universally quantified theorem. Reproduction command: `python verify.py` (requires SymPy 1.13 or newer).

## Relationship to prior work

Eisenmann and Stillfjord (first preprint public 2022-10-11; published in *Numerische Mathematik* in 2024) introduce the reciprocal-inclusion-probability sampled operator and forcing in their Sect. 3.2 and analyze finite-horizon well-posedness, stability and convergence in their Sects. 4–5. The present scalar affine problem uses that same sampling and implicit Euler update, but asks for the exact infinite-time stationary-error sampling design; neither their finite-horizon estimates nor their numerical experiments imply the stated algebraic threshold or nonattainment classification.

Veldman and Zuazua (2021 preprint; 2022 journal publication) treat randomized time-splitting in linear-quadratic control and, in their Example 3, optimize *operator-variance* sampling (yielding weights proportional to component operator norms in a block-diagonal example). The present stationary loss also depends on split forcing, resolvent nonlinearity and step size; the leading small-step optimum is equal sampling, while the large-step optimum is lost at a sharp threshold. These are different objective functions and one does not imply the other.

The affine recursion moment identities are elementary and not claimed as new. The assessed contribution is the complete stationary sampling/nonattainment threshold for a minimal heterogeneous instance of the published random resolvent method. Specialized exact two-map resolvent calculations might independently yield the same polynomial and are a remaining priority risk.

## Limitations

The theorem concerns one fixed scalar affine decomposition, independent one-component draws, constant step size, and squared distance to the exact continuous equilibrium measured in the stationary law. It does not establish a universal optimal sampling formula, optimal finite-horizon sampling, uniform-in-parameter convergence as \(p\to0\) or \(1\), or the superiority of an inconsistent deterministic endpoint integrator. The optimizing boundary \(p=1\) is excluded because the second component would then never be sampled. The numerical value of \(h_*\) is subordinate to its exact algebraic specification, and originality remains conditional on the surveyed literature rather than independently certified.

## References

1. M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375v1 (2022-10-11); *Numerische Mathematik* **156** (2024), 435–461. https://link.springer.com/article/10.1007/s00211-024-01396-w
2. D. W. M. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798 (2021); *Numerische Mathematik* **151** (2022), 495–549. https://link.springer.com/article/10.1007/s00211-022-01290-3
