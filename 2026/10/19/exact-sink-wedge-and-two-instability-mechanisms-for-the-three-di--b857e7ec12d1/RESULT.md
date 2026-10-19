# Exact sink wedge and two instability mechanisms for the three-dimensional Hénon two-cycle

## Finding

Consider the quadratic diffeomorphism \(F_{\alpha,\sigma,\delta}:\mathbb R^3\to\mathbb R^3\),
\[
F_{\alpha,\sigma,\delta}(x,y,z)=(\delta z+\alpha-\sigma y+x^2,\ x,\ y),
\qquad 0<\delta<1,\quad \alpha,\sigma\in\mathbb R.
\]
Put
\[
Q=1+\sigma+\delta,\qquad
\alpha_*= -\frac{(1+\sigma+\delta)(3+3\sigma-\delta)}4,
\qquad E=\sigma^2+2\delta Q,
\]
and for \(\alpha<\alpha_*\) put \(h=\alpha_*-\alpha>0\). Every primitive real period-two orbit is counted once, modulo exchange of its two states.

**Complete orbit count.** There are no primitive period-two orbits if \(\alpha\ge\alpha_*\). If \(\alpha<\alpha_*\), there is precisely one primitive orbit, with states
\[
(u,v,u)\longleftrightarrow(v,u,v),\qquad
u=-\frac Q2+\sqrt h,\quad v=-\frac Q2-\sqrt h.
\]

**Sharp attracting region.** Define
\[
W_{\rm flip}=\frac{1+E}{2},\qquad
W_{\rm NS}=\frac{(1-\delta^2)(1+\sigma)(1-\sigma-2\delta)}{4\delta^2}.
\]
The primitive two-cycle is locally exponentially attracting *if and only if*
\[
-1<\sigma<1-2\delta,
\qquad 0<h<\min\{W_{\rm flip},W_{\rm NS}\}.
\]
In particular, no choice of \(\alpha\) produces an attracting primitive two-cycle when \(\sigma\notin(-1,1-2\delta)\).

**Exact exit mechanism.** Fix \(0<\delta<1\) and \(-1<\sigma<1-2\delta\); decrease \(\alpha\) from its existence threshold, so \(h\) increases. If \(E<1-2\delta^2\), the first loss of linear stability is through a simple two-step multiplier \(-1\) at \(h=W_{\rm flip}\). If \(E>1-2\delta^2\), it is through a nonreal conjugate pair on the unit circle at \(h=W_{\rm NS}\). At equality, \(h=1-\delta^2\) and the two-step multipliers are \((-1,-1,\delta^2)\). These descriptions concern the *linear spectrum*, not the nonlinear critical normal forms.

There is a sharp contraction dichotomy: for \(0<\delta<1/3\), the two mechanism boundaries within the sink strip are
\[
\sigma_\pm(\delta)=-\delta\pm\sqrt{(1-3\delta)(1+\delta)}.
\]
The exit is by a \(-1\) multiplier for \(\sigma_-<\sigma<\sigma_+\) and by a complex unit pair in the two remaining portions of the sink strip. For \(\delta>1/3\) all sink branches exit through a nonreal unit pair. At \(\delta=1/3\), this remains true except for the unique double-\(-1\) point \(\sigma=-1/3\).

## Assumptions and scope

All three phase-space coordinates are arbitrary real numbers. There are no positivity or boundedness restrictions on initial states. The map is a diffeomorphism because its Jacobian determinant is the fixed nonzero number \(\delta\). The main classification concerns *primitive period exactly two*, not fixed points, longer periods, global basins, or existence of an invariant circle after the spectral crossing. Local exponential attraction means all three eigenvalues of the second-return derivative have modulus strictly less than one.

## Proof

**1. Exact and exhaustive two-cycle reduction.** Every state of a period-two orbit is of the form \(p=(u,v,u)\), with other state \(q=(v,u,v)\), because the second and third coordinates of \(F\) shift the previous first and second coordinates. The two identities \(F(p)=q\) and \(F(q)=p\) are equivalent to
\[
(1+\sigma)v=\delta u+\alpha+u^2,\qquad
(1+\sigma)u=\delta v+\alpha+v^2.
\]
Subtracting shows that \((u-v)(u+v+Q)=0\). For primitive period two \(u\ne v\), so \(u+v=-Q\). Substituting \(u=-Q/2+t\), \(v=-Q/2-t\) into either equation gives exactly \(\alpha=\alpha_*-t^2\). Thus a distinct pair exists precisely when \(h>0\); the two signs of \(t\) are the same orbit with interchanged states. At \(h=0\), the two states coincide, so this is not primitive period two. The reduction involved no divisions by possibly vanishing parameters such as \(1+\sigma\).

**2. Full Floquet polynomial.** Write
\[
J(w)=\begin{pmatrix}2w&-\sigma&\delta\\1&0&0\\0&1&0\end{pmatrix},
\quad M=J(v)J(u).
\]
Direct multiplication gives
\[
M=\begin{pmatrix}
4uv-\sigma&\delta-2\sigma v&2\delta v\\
2u&-\sigma&\delta\\1&0&0
\end{pmatrix},
\]
and, putting \(T=1+E-\delta^2-4h\),
\[
\det(\lambda I-M)=\lambda^3-T\lambda^2+E\lambda-\delta^2.
\]
The determinant is \(\delta^2\), the middle coefficient is \(\sigma^2-2\delta(u+v)=E\), and the trace is \(4uv-2\sigma=T\). In particular, the middle coefficient does not depend on \(\alpha\), while the trace decreases *linearly* in \(h\).

**3. Sharp Schur inequalities.** Since \(0<\delta<1\), a monic real cubic \(P(\lambda)=\lambda^3-T\lambda^2+E\lambda-\delta^2\) is Schur stable if and only if its reciprocal Schur reduction
\[
\frac{P(\lambda)+\delta^2\lambda^3P(1/\lambda)}{\lambda}
=(1-\delta^4)\lambda^2+(-T+\delta^2E)\lambda+(E-\delta^2T)
\]
is Schur stable. For a real quadratic \(A\lambda^2+B\lambda+C\) with \(A>0\), this is equivalent to \(A+B+C>0\), \(A-B+C>0\), and \(A-C>0\) (the last two positive endpoint sums also imply \(A+C>0\)). The three expressions here reduce exactly to
\[
4(1+\delta^2)h,
\qquad4(1-\delta^2)(W_{\rm flip}-h),
\qquad4\delta^2(W_{\rm NS}-h).
\]
Now \(E=(\sigma+\delta)^2+2\delta+\delta^2>0\), so \(W_{\rm flip}>0\). Also \(W_{\rm NS}>0\) is equivalent to \((1+\sigma)(1-\sigma-2\delta)>0\), or \(-1<\sigma<1-2\delta\). This proves the stated necessary and sufficient stability inequalities and excludes any re-entrant sink intervals as \(h\) increases.

**4. Distinct stability-loss boundaries.** The difference between the two permissible widths satisfies
\[
4\delta^2(W_{\rm NS}-W_{\rm flip})
=-(1+\delta^2)(E-1+2\delta^2).
\]
Thus \(W_{\rm flip}<W_{\rm NS}\) exactly when \(E<1-2\delta^2\); \(P(-1)=0\) at that first boundary, and the remaining two multipliers have modulus below one. When \(E>1-2\delta^2\), \(W_{\rm NS}<W_{\rm flip}\); at that boundary
\[
P(\lambda)=(\lambda-\delta^2)(\lambda^2-2c\lambda+1),
\quad c=\frac{E-1}{2\delta^2}.
\]
In the strict sink strip, \(E<1+2\delta^2\), because \(E\) is convex in \(\sigma\) and equals \(1+2\delta^2\) at both strip endpoints. With \(E>1-2\delta^2\) we therefore have \(-1<c<1\), proving a nonreal unit pair. At equality of the widths, \(P(\lambda)=(\lambda+1)^2(\lambda-\delta^2)\) and both widths equal \(1-\delta^2\).

Finally,
\[
E-(1-2\delta^2)=(\sigma+\delta)^2+(3\delta-1)(\delta+1).
\]
For \(\delta>1/3\) this is strictly positive. For \(\delta=1/3\) it vanishes only at \(\sigma=-1/3\). If \(0<\delta<1/3\), its two zeros are precisely the stated \(\sigma_\pm\); both lie within \((-1,1-2\delta)\), since \((1-\delta)^2-(1-3\delta)(1+\delta)=4\delta^2>0\). This proves the sharp mechanism dichotomy. \(\square\)

## Verification

The included `verify.py` uses SymPy to verify both orbit recurrences, the complete two-step characteristic polynomial, the Schur reductions and the exact transition factorization. It also performs 68 additional rational-parameter recurrence, endpoint and finite spectral checks, including both mechanisms and the double-\(-1\) point. Run `python3 verify.py` in an environment with SymPy. The exact symbolic identities are algebraic checks; the finite spectral cases are illustrations rather than proofs of the quantified theorem.

For orientation, at \((\delta,\sigma)=(1/20,-2913/10000)\), the exact formulas give a first period-two threshold approximately \(-0.3937843\) and flip exit approximately \(-0.9741471\). At \((\delta,\sigma)=(7/10,-163/200)\), the threshold is \(0.03208125\) and the Neimark–Sacker spectral exit is approximately \(0.01210408\). They fall in the respective strong- and moderate-contraction regimes discussed in the motivating literature; these examples are not evidence for global attractors.

## Relationship to prior work

Hampton and Meiss [1], §§II–III, derive multiplier geometry and the fixed-point period-doubling locus for a general three-dimensional quadratic map, and §V numerically locates periodic attractors. Their reported strong-contraction example loses its two-cycle through a subsequent doubling, while a moderate-contraction example loses it through a Neimark–Sacker crossing. The present result supplies, for their one-quadratic-term family, the exact *entire-real-space primitive two-cycle census*, the full closed-form sink domain and the sharp transition at \(\delta=1/3\); it does not claim the previously known fixed-point flip locus as new.

Hampton and Meiss [2] prove anti-integrable continuation results and display low-period numerical continuation data, including a known fixed-point flip criterion in alternate parameters. That criterion concerns creation of a cycle, not the all-parameter Schur region or its two distinct loss mechanisms. The older three-dimensional map studied by Zheng et al. [3] squares a lagged coordinate instead of the current coordinate and derives *fixed-point* bifurcation conditions; its theorems do not imply the present two-cycle spectrum. More generally, generic three-dimensional Schur criteria alone require the nontrivial orbit elimination and the parameter-level factorization proved above.

## Limitations

No claim is made about global attraction, uniqueness of all attractors, basins, chaotic behavior, nonlinear resonance normal forms or the appearance of invariant circles/four-cycles beyond a neutral multiplier crossing. Neither computational checks nor literature searching constitute independent proof or priority certification. The structural result is confined to the quadratic map with \(0<\delta<1\), although every \(\alpha,\sigma\in\mathbb R\) is covered within that range.

## References

[1] A. E. Hampton and J. D. Meiss, *Visualizing Attractors of the Three-Dimensional Generalized Hénon Map*, arXiv:2206.07855v1 (first public version 2022-06-16); journal version: *Chaos* 32 (2022), 113127. https://arxiv.org/abs/2206.07855

[2] A. E. Hampton and J. D. Meiss, *Connecting Anti-integrability to Attractors for Three-Dimensional, Quadratic Diffeomorphisms*, arXiv:2305.06302v1 (2023). https://arxiv.org/abs/2305.06302

[3] J. Zheng, Z. Wang, Y. Li and J. Wang, *Bifurcations and chaos in a three-dimensional generalized Hénon map*, *Advances in Difference Equations* 2018, article 185. https://doi.org/10.1186/s13662-018-1622-y
