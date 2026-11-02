# Exact covariance resonance and fluctuation-optimal tuning in a Markov skew tent family

## Finding

For every real parameter \(0<t<1\), define the continuous interval map
\[
T_t(x)=\begin{cases}t+(1-t)x/t,&0\le x\le t,\\(1-x)/(1-t),&t<x\le1.\end{cases}
\]
It is the \(a=b=t,c=0\) Markov subfamily of the tunable-mean piecewise-affine maps of Moysis, Lawnik, Volos, Baptista, and Goudos (2023). Write \(\nu_t\) for its absolutely continuous invariant probability and \(\mu_t=\int x\,d\nu_t\). For stationary \(X_0\sim\nu_t\) and \(X_n=T_t^n(X_0)\), define
\[
C_n(t)=\mathbb E[(X_0-\mu_t)(X_n-\mu_t)],\qquad G_t(z)=\sum_{n\ge0}C_n(t)z^n.
\]
The complete autocovariance generating function is rational:
\[
G_t(z)=\frac{(t^2-t+1)\bigl[t^2+3t+1+(t^4+2t^3-2t^2+t)z+(t^5+t^4+t^3)z^2\bigr]}{12(1+t)^2(1+tz)\bigl[1+(1-t)^2z+t^2z^2\bigr]}.
\]
The absolutely convergent Green--Kubo variance, and hence the variance of the stationary central limit theorem, is
\[
\sigma_t^2=C_0(t)+2\sum_{n\ge1}C_n(t)
=\frac{t(1-t)(t^2-t+1)}{12(1+t)^3}>0.
\]
Thus \(n^{-1/2}\sum_{j=0}^{n-1}(X_j-\mu_t)\) converges in distribution under \(\nu_t\) to a centered normal law of variance \(\sigma_t^2\).

There is a genuine correlation-spectrum transition at \(t_*=2-\sqrt3\). If \(0<t<t_*\), a simple negative real decay mode uniquely dominates the asymptotic covariance. At \(t=t_*\), the generating function has an **uncancelled third-order pole** at \(z=-1/t_*\), and
\[
\lim_{n\to\infty}\frac{C_n(t_*)}{n^2(-t_*)^n}
=\frac{t_*(t_*^2-t_*+1)}{4(1+t_*)^2}
=\frac14-\frac{\sqrt3}{8}>0.
\]
For \(t_*<t<1\), its three nontrivial spectral roots have common modulus \(t\), consisting of one negative real root and a nonreal conjugate pair; the complex pair is not canceled by the observable.

The asymptotic variance has its unique global maximum at the root \(t_{\mathrm{var}}\in(0,1)\) of
\[
t^4+4t^3-8t^2+6t-1=0,
\qquad t_{\mathrm{var}}\approx0.227260049622555.
\]
By contrast the metric entropy of \(\nu_t\) is uniquely maximized at \(t_{\mathrm{ent}}=(3-\sqrt5)/2\approx0.38196601125\). The three distinguished parameters are strictly ordered:
\[
0<t_{\mathrm{var}}<t_*<t_{\mathrm{ent}}<1.
\]
This separates a fluctuation optimum, a correlation-resonance transition, and the entropy optimum along one natural tunable-mean family.

## Assumptions and scope

The domain is the full unit interval with \(0<t<1\); endpoint branch conventions have no effect on the absolutely continuous probability or covariance. The Markov partition consists of \(A=[0,t]\) and \(B=[t,1]\) up to the common endpoint. The branch itinerary is \(A\to B\) and \(B\to A\cup B\), with critical orbit \(0\to t\to1\to0\). Every branch of \(T_t^2\) has derivative magnitude either \(1/t\) or \(1/(1-t)^2\), both strictly greater than one. The transition matrix \(\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\) is primitive, so standard piecewise-expanding Markov theory gives a unique mixing absolutely continuous invariant probability and a spectral gap for bounded-variation densities. There may be other, singular invariant measures; the asserted CLT and uniqueness concern \(\nu_t\).

Its density and mean, included to normalize the covariance calculation but not claimed novel in isolation, are
\[
\frac{d\nu_t}{dx}=\begin{cases}\frac1{1+t},&x\in(0,t),\\\frac1{1-t^2},&x\in(t,1),\end{cases}
\qquad \mu_t=\frac{1+t+t^2}{2(1+t)}.
\]
The topological entropy is \(\log\varphi\), where \(\varphi=(1+\sqrt5)/2\), while
\[
h_{\nu_t}(T_t)=\frac{-t\log t-(1-t)\log(1-t)}{1+t}.
\]

## Proof

**Invariant density.** On \(A\), the right inverse branch is \(y_B=1-(1-t)x\), with inverse-Jacobian \(1-t\). On \(B\), both that branch and \(y_A=t(x-t)/(1-t)\), with inverse-Jacobian \(t/(1-t)\), are present. Their Frobenius--Perron equations show directly that the displayed two-level density is normalized and invariant. The primitive two-state Markov structure and uniform expansion of the second iterate yield the stated mixing and uniqueness among absolutely continuous invariant probabilities.

**Closed transfer subspace.** Represent a density that is affine on each Markov interval by the coefficient column \((c_A,d_A,c_B,d_B)^{\mathsf T}\), meaning \(c_A+d_Ax\) on \(A\) and \(c_B+d_Bx\) on \(B\). The transfer operator leaves this four-dimensional space invariant, with matrix
\[
M_t=\begin{pmatrix}
0&0&1-t&1-t\\
0&0&0&-(1-t)^2\\
t/(1-t)&-t^3/(1-t)^2&1-t&1-t\\
0&t^2/(1-t)^2&0&-(1-t)^2
\end{pmatrix}.
\]
For \(h_A=1/(1+t)\) and \(h_B=1/(1-t^2)\), the coefficient column of \((x-\mu_t)\,d\nu_t/dx\) is \(v_t=(-\mu_t h_A,h_A,-\mu_t h_B,h_B)^{\mathsf T}\). Define a row functional \(J_t\) on coefficient columns by integrating \((x-\mu_t)(c_i+d_ix)\) over the respective two intervals. Then by transfer duality,
\[
C_n(t)=J_tM_t^nv_t,
\qquad G_t(z)=J_t(I-zM_t)^{-1}v_t.
\]
Taking the inverse, integrating the monomials explicitly and canceling the invariant eigenmode gives exactly the displayed rational function. The raw characteristic polynomial is
\[
\det(\lambda I-M_t)=(\lambda-1)(\lambda+t)
[\lambda^2+(1-t)^2\lambda+t^2].
\]
The nontrivial eigenvalues have modulus strictly less than one: the isolated root is \(-t\); a nonreal pair has modulus \(t\); and any real roots of the quadratic are both negative, with absolute values summing to \((1-t)^2<1\). Thus the series for \(G_t(1)\) converges absolutely and the spectral-gap CLT applies. Direct simplification of \(2G_t(1)-G_t(0)\) proves the asserted positive variance.

**Uncancelled resonance.** The discriminant of the quadratic characteristic factor is
\[
(1-t)^4-4t^2=(t^2+1)(t^2-4t+1).
\]
Its sole zero in \((0,1)\) is \(t_*=2-\sqrt3\), at which the quadratic equals \((\lambda+t_*)^2\). Thus the denominator of \(G_{t_*}\) has a third-order factor \((1+t_*z)^3\). Its unmultiplied numerator at \(z=-1/t_*\) equals \(6t_*(t_*^2-t_*+1)\), strictly positive, proving noncancellation. The coefficient transfer formula for a triple pole gives
\(C_n(t_*)\sim[t_*(t_*^2-t_*+1)/(4(1+t_*)^2)]n^2(-t_*)^n\).
For \(t<t_*\), the larger-magnitude negative quadratic root dominates \(-t\); the observable's numerator and quadratic denominator have nonzero resultant \(2t^4(1+t)^2(t^2-t+1)^3\), so this mode does not vanish. For \(t>t_*\), the conjugate roots are nonreal and also not canceled, while all three nontrivial roots have modulus \(t\).

**Separated optima.** Differentiation gives
\[
\frac{d\sigma_t^2}{dt}=-\frac{q(t)}{12(1+t)^4},
\quad q(t)=t^4+4t^3-8t^2+6t-1.
\]
Since \(q'(t)=4t^3+12(t-2/3)^2+2/3>0\), \(q(0)=-1\) and \(q(1)=2\), this has a unique maximizer. Moreover \(q(t_*)=156-90\sqrt3>0\), so that maximizer precedes the spectral transition. Finally
\[
\frac{d}{dt}h_{\nu_t}(T_t)=\frac{\log((1-t)^2/t)}{(1+t)^2},
\]
whose unique zero is \((3-\sqrt5)/2>2-\sqrt3\), completing the strict ordering. The metric entropy formula follows from the branch Lyapunov exponents and the branch masses \(t/(1+t)\) and \(1/(1+t)\); the topological entropy follows from the Perron eigenvalue of the primitive transition matrix.

## Verification

Run `python CHECK.py` with SymPy available. This program reconstructs the Frobenius--Perron matrix from the two inverse branches, verifies normalization and invariance, checks the correlation resolvent and characteristic polynomial as exact symbolic identities, compares the first eleven covariance coefficients, derives the Green--Kubo rational function and its derivative, verifies the noncancelled triple pole and leading constant, and tests three rational parameters. The proof above, rather than finite testing, justifies all-parameter and infinite-time claims. No external verifier or independent mathematical audit has been performed.

## Relationship to prior work

Moysis et al. (2023 conference; 2023 journal) introduced and numerically explored tunable-mean piecewise maps, including the parent three-parameter family. Earlier literature (Billings--Bollt 2001; Ito--Tanaka--Nakada 1979; Alsedà--Misiurewicz--Pérez 2020) treats invariant densities and entropy of skew tent maps. Those familiar ingredients are not proposed as original results here. Papamarkou--Lawrance (2014) derives autocorrelation laws for *fully stretching*, onto-branch maps with a uniform invariant density; here the left branch maps only \([0,t]\) onto \([t,1]\), so that framework does not directly supply this covariance law. Yoshida--Mori--Shigematsu (1983) studies power spectra for standard symmetric tent maps at band transitions, not the specified parameter family. The proposed distinct contribution is the explicit whole-family covariance resolvent, uncancelled cubic resonance, exact Green--Kubo variance, and strict separation of the variance, resonance and entropy parameters. Identified sources do not directly imply these combined statements, but publication priority is not conclusively established.

## Limitations

The theorem is restricted to the diagonal \(a=b\), \(c=0\) slice and the stationary coordinate observable. It does not classify the entire three-parameter parent family, all observables, or invariant measures singular with respect to Lebesgue measure. A strong general finite-state Markov/transfer-operator apparatus makes the method natural and could subsume pieces of the calculation; the exact formulas and critical comparisons have not been independently checked against all possible prior sources. The 1979 invariant-density paper and the conference proceedings were compared via accessible references/abstracts rather than complete primary full text. Analytic proof and in-file checker have self-review only; independent audit not performed.

## References

1. L. Moysis, M. Lawnik, M. Baptista, S. Goudos, C. Volos, *Construction of Piecewise Chaotic Maps With Tunable Statistical Mean*, IEEE MOCAST (first public release July 17, 2023), DOI 10.1109/MOCAST57943.2023.10176612.
2. L. Moysis, M. Lawnik, C. Volos, M. S. Baptista, S. K. Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission*, Symmetry 15 (2023), 2138, DOI 10.3390/sym15122138. Accessible full text: https://www.mdpi.com/2073-8994/15/12/2138.
3. L. Alsedà, M. Misiurewicz, R. A. Pérez, *Flexibility of entropies for piecewise expanding unimodal maps*, arXiv:2004.01813 (2020), https://arxiv.org/pdf/2004.01813.
4. L. Billings, E. M. Bollt, *Probability density functions of some skew tent maps*, Chaos Solitons Fractals 12 (2001), 365–376, DOI 10.1016/S0960-0779(99)00204-0.
5. T. Papamarkou, A. J. Lawrance, *Nonlinear dynamics of trajectories generated by fully-stretching piecewise linear maps*, Int. J. Bifurcation Chaos 24 (2014), 1450071, DOI 10.1142/S0218127414500710.
6. T. Yoshida, H. Mori, H. Shigematsu, *Analytic study of chaos of the tent map: Band structures, power spectra, and critical behaviors*, DOI 10.1007/BF01011583 (1983).
7. S. Ito, S. Tanaka, H. Nakada, *On unimodal linear transformations and chaos II*, DOI 10.3836/tjm/1270216321 (1979).
