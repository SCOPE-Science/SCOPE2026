# Arithmetic lag trichotomy for positive-polynomial Hardy shift averages

## Finding

Let \(S\) be the unilateral shift \((Sf)(z)=zf(z)\) on complex \(H^2(\mathbb D)\), and let
\[
P(z)=\sum_{k\in F}p_kz^k,\qquad p_k>0,\quad \sum_{k\in F}p_k=1,
\]
where \(F\subset\mathbb N_0\) is finite and contains at least two distinct integers. Set \(T=P(S)\). Put
\[
k_0=\min F,\quad d=\gcd\{k-k_0:k\in F\},\quad q=\frac d{\gcd(d,k_0)},\quad Q_h=\frac q{\gcd(q,h)},
\]
for a fixed positive integer lag \(h\), and set
\[
\mu=\sum_{k\in F}kp_k,\qquad v=\sum_{k\in F}(k-\mu)^2p_k.
\]
The hypotheses imply \(\mu>0\), \(v>0\), and \(d,q,Q_h\) are positive integers. For \(D_{n,h}=\|T^{n+h}-T^n\|\) and \(n\to\infty\), precisely the following occur.

**(i) Resonant lag, \(Q_h=1\).**
\[
D_{n,h}=\frac{h\mu}{\sqrt{ev}}\,n^{-1/2}+O_{P,h}(n^{-3/2}).
\]

**(ii) Even peripheral order, \(Q_h\) even.** Exactly for every integer \(n\ge0\),
\[
D_{n,h}=2.
\]

**(iii) Odd peripheral order, \(Q_h\ge3\) odd.** Writing \(B_Q=2\cos(\pi/(2Q))\),
\[
D_{n,h}=B_{Q_h}+\frac{h^2\mu^2\sin^2(\pi/Q_h)}{2B_{Q_h}^{3}v}\,n^{-1}+O_{P,h}(n^{-2}).
\]
In particular, the odd-order limit is approached strictly **from above** for all sufficiently large \(n\).

Thus \(D_{n,h}\to0\) if and only if \(q\mid h\). Nevertheless \(T^nf\to0\) strongly for every \(f\in H^2\), while \(\|T^n\|=1\) for every \(n\ge0\). No positive power of \(T\) is Ritt.

## Assumptions and scope

The operator acts on the complex, unweighted Hardy space on the disk; the underlying shift has multiplicity one. All coefficients of the nonconstant polynomial \(P\) are strictly positive **real** and sum to one. Every asymptotic is for one fixed polynomial and one fixed positive integer \(h\) as \(n\to\infty\), not uniformly in coefficient vectors or growing lags. The gcd of positive differences is ordinary integer gcd; \(\gcd(d,0)=d\). The real variance \(v\) is strictly positive because the support has at least two points. Define the Ritt condition as power boundedness together with \(\sup_{n\ge1}n\|A^{n+1}-A^n\|<\infty\).

## Proof

**1. Exact Hardy multiplier norm.** Since \(T=M_P\), \(T^{n+h}-T^n=M_{P^n(P^h-1)}\). The norm of multiplication by a polynomial \(G\) on \(H^2\) equals its boundary supremum: the upper bound follows from the Hardy boundary integral and the reverse bound from normalized reproducing kernels tending radially to each boundary point. Hence
\[
D_{n,h}=\max_{-\pi\le t\le\pi}|P(e^{it})|^n\,|1-P(e^{it})^h|.\tag{1}
\]
The maximum-modulus principle and positivity give \(\|T^n\|=\|P^n\|_\infty=P(1)^n=1\).

**2. The exact peripheral arithmetic.** For a convex combination of unit complex numbers to have modulus one, all summands must have one common phase. Thus \(|P(e^{it})|=1\) if and only if \(e^{i(k-\ell)t}=1\) for every \(k,\ell\in F\), which is equivalent to \(t=2\pi j/d\) modulo \(2\pi\) for \(0\le j<d\). At such a contact point,
\[
P(e^{2\pi i j/d})=e^{2\pi i j k_0/d}.
\]
These values traverse each \(q\)-th root of unity exactly \(d/q\) times; their \(h\)-th powers traverse all \(Q_h\)-th roots. For any fixed disjoint small arcs around the finitely many contacts, strict convexity yields \(|P|\le\rho<1\) on the complement, so its contribution to (1) is at most \(2\rho^n\).

**3. Uniform local form.** Around any contact write \(t=2\pi j/d+s\) and \(\omega_j=e^{2\pi i j k_0/d}\). Because every exponent is congruent to \(k_0\) modulo \(d\), exactly
\[
P(e^{it})=\omega_jP(e^{is}).
\]
For \(s\) small, the nonvanishing analytic logarithm satisfies the characteristic-function expansion
\[
\log P(e^{is})=i\mu s-\tfrac12vs^2+O(s^3),\quad
\log|P(e^{is})|=-\tfrac12vs^2+O(s^4).
\tag{2}
\]
The second remainder is even and real analytic because \(P\) has real coefficients, hence its odd Taylor coefficients vanish. In particular there are \(a,A,\varepsilon>0\) such that \(e^{-As^2}\le|P(e^{is})|\le e^{-as^2}\) for \(|s|<\varepsilon\).

**4. Resonance and the Gaussian flank.** If \(Q_h=1\), then \(\omega_j^h=1\) at every contact. The analytic expansion and conjugate symmetry imply
\[
|1-P(e^{is})^h|=h\mu|s|\bigl(1+O(s^2)\bigr).
\]
The maximum of the local expression occurs at \(|s|=O(n^{-1/2})\); indeed the Gaussian envelope bounds values outside fixed multiples of this scale, and a nonzero comparison value at \(s=n^{-1/2}/\sqrt v\) excludes smaller scales. For \(u=s\sqrt{nv}\), bounded \(u\),
\[
|P(e^{is})|^n|1-P(e^{is})^h|
=\frac{h\mu}{\sqrt{nv}}|u|e^{-u^2/2}\bigl(1+O_{P,h}(n^{-1})\bigr).
\]
Here the error is uniform on any fixed bounded window; a larger fixed window excludes the rest by Gaussian decay. Since \(\max_{u\in\mathbb R}|u|e^{-u^2/2}=e^{-1/2}\), the first formula follows, including its absolute \(O(n^{-3/2})\) remainder.

**5. Even order is exact.** If \(Q_h\) is even, one contact satisfies \(P(e^{it})^h=-1\). Formula (1) then gives the value \(2\); the triangle inequality yields the upper bound \(|P|^n|1-P^h|\le2\) for every boundary point and every \(n\ge0\).

**6. Odd order and the curvature-induced positive correction.** If \(Q=Q_h\ge3\) is odd, the largest of \(|1-\zeta|\) over \(\zeta^Q=1\) is attained at \(\zeta_\pm=e^{\pm i(\pi-\pi/Q)}\); its value is \(B=2\cos(\pi/(2Q))\). Other contacts have a fixed smaller value, so they cannot give the maximum for all sufficiently large \(n\). At a maximal contact let \(\zeta=\omega_j^h\). By (2), the log of the local objective equals
\[
\begin{aligned}
L_n(s)&=n\log|P(e^{is})|+\log|1-\zeta P(e^{is})^h|\\
&=\log B+a_\zeta s-\tfrac12nv s^2+O(s^2+ns^4),
\end{aligned}\tag{3}
\]
where direct differentiation of the squared modulus yields
\[
a_\zeta=\left.\frac{d}{ds}\log|1-\zeta P(e^{is})^h|\right|_{s=0}
=\frac{h\mu\,\operatorname{Im}\zeta}{B^2}.
\]
The maximum lies at \(s=O(n^{-1})\): away from such a window the negative quadratic in (3) dominates the linear term; within the window \(L_n''=-nv+O(1)\), and solving \(L_n'(s)=0\) gives
\[
s_n=\frac{a_\zeta}{nv}+O_{P,h}(n^{-2}),\qquad
L_n(s_n)=\log B+\frac{a_\zeta^2}{2nv}+O_{P,h}(n^{-2}).
\]
Both maximal contacts have \(|\operatorname{Im}\zeta|=\sin(\pi/Q)\), so exponentiating produces
\[
\max e^{L_n(s)}=B+\frac{B}{2nv}\frac{h^2\mu^2\sin^2(\pi/Q)}{B^4}+O(n^{-2}),
\]
which is precisely the coefficient in part (iii). The correction is strictly positive.

**7. Strong convergence and failure of Ritt.** For boundary-almost every \(t\), \(|P(e^{it})|<1\); by dominated convergence the Hardy boundary norm of \(P^nf\) tends to zero for each fixed \(f\). But \(\|T^n\|=1\). For any positive \(h\), the three regimes show that \(nD_{n,h}\to\infty\). In particular, for every positive integer \(r\), apply the theorem with \(h=r\) and \(n=rm\) to obtain \(m\|T^{r(m+1)}-T^{rm}\|\to\infty\); thus \(T^r\) is not Ritt. This concludes the proof.

## Verification

All statements are analytic and do not rely on finite enumeration. An accompanying executable `checker.py` numerically maximizes (1), verifies contact points, tests exact even-order behavior, and checks the two asymptotic constants for explicit finite positive polynomials and lags. It uses Python 3, NumPy, and SciPy and prints its diagnostic count. These finite tests cannot verify the universal asymptotics or the originality claim.

## Relationship to prior work

Borichev, Gomilko and Tomilov (2026), Section 8, establish that positive convex combinations of powers **preserve** the Ritt property when the input operator is already Ritt. Here the input is the unilateral shift, which is not Ritt; the present result instead classifies the precise failure of asymptotic regularity and all fixed integer lagged differences, including their optimal corrections. Diaconis and Saloff-Coste (2012) analyze the Fourier and local-limit behavior of convolution powers and motivate the characteristic-function expansion, but their local limit and coefficientwise estimates do not state the present exact Hardy multiplier operator-norm trichotomy. Standard unitary spectral and Fourier arguments explain why support differences and peripheral phases matter, but not the sharp constants and \(n^{-1}\) upward correction exhibited here.

## Limitations

The formula requires positive real coefficients, finitely supported integer exponents, and fixed lags. It does not cover signed coefficients, infinite tails, multivariate shifts, arbitrary contractions, or coefficient distributions varying with \(n\). Even though its proof is self-contained, historical equivalences under ergodic, numerical-analysis, or random-walk terminology may exist; the literature comparison is not a proof of global publication priority. Independent expert review has not been performed.

## References

- A. Borichev, A. Gomilko, Yu. Tomilov, *Beurling--Kato theory, Hardy--Sobolev calculus and Ritt operators*, arXiv:2607.10507 (first public version 2026-07-11), especially Sections 7--8.
- P. Diaconis, L. Saloff-Coste, *Convolution powers of complex functions on Z*, arXiv:1205.6490 (2012), especially the Fourier-asymptotic analysis.
