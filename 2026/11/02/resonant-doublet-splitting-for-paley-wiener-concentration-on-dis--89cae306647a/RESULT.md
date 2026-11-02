# Resonant doublet splitting for Paley–Wiener concentration on distant intervals

## Finding

Let \(a>0\), let \(J=[-a/2,a/2]\), and set \(k(u)=\sin(\pi u)/(\pi u)\), continuously extended by \(k(0)=1\). Let \(K_a\) be the compact, positive, self-adjoint integral operator on \(L^2(J)\) with kernel \(k(x-y)\). Write \(\lambda_0(a)>\lambda_1(a)\) for its two largest eigenvalues. Fix the real, even, \(L^2(J)\)-normalized eigenfunction \(\psi_a\) corresponding to the simple top eigenvalue \(\lambda_0(a)\). Define

\[
 c_a=\int_J\psi_a(x)\cos(\pi x)\,dx,\qquad
 d_a=\int_J x\psi_a(x)\sin(\pi x)\,dx,
\]
\[
 C_a=c_a^2,\qquad Q_a=\frac{c_a d_a}{\pi}.
\]

Both \(C_a\) and \(Q_a\) are **strictly positive for every** \(a>0\).

For \(R>a\), define two intervals separated by their center distance,
\[
 E_R=(J-R/2)\cup(J+R/2).
\]
Let \(\Lambda_+(R)\ge\Lambda_-(R)\) be the two largest eigenvalues of the integral operator on \(L^2(E_R)\) with kernel \(k(x-y)\). Then, as \(R\to\infty\),
\[
 \boxed{\Lambda_\pm(R)=\lambda_0(a)
 \pm\frac{C_a|\sin(\pi R)|}{\pi R}+O_a(R^{-2}).}
\]
Here the symbol \(\pm\) indicates the upper and lower signs, respectively; the error estimate is uniform in all sufficiently large real \(R\).

There is a finer, **resonant** two-eigenvalue law. For every fixed \(T>0\), uniformly for real \(|t|\le T\) and positive integers \(m\to\infty\),
\[
 \boxed{
 \Lambda_\pm(m+t/m)=\lambda_0(a)
 +\frac{Q_a\pm|C_a t-2Q_a|}{m^2}
 +O_{a,T}(m^{-3}).
 }
\]
In particular,
\[
 \Lambda_+(m)=\lambda_0(a)+\frac{3Q_a}{m^2}+O_a(m^{-3}),
 \qquad
 \Lambda_-(m)=\lambda_0(a)-\frac{Q_a}{m^2}+O_a(m^{-3}).
\]
At the strictly positive detuning \(t_a^*=2Q_a/C_a\), the leading \(m^{-2}\) splitting cancels:
\[
 0\le\Lambda_+(m+t_a^*/m)-\Lambda_-(m+t_a^*/m)=O_a(m^{-3}).
\]
This is a **leading-order cancellation**, not a claim of exact eigenvalue multiplicity. No claim is made that these coefficients are elementary functions of \(a\).

With the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx\), the largest eigenvalue \(\Lambda_+(R)\) is exactly the optimal concentration fraction
\[
 \sup_{\substack{0\ne f\in L^2(\mathbb R)\\
 \operatorname{supp}\widehat f\subseteq[-1/2,1/2]}}
 \frac{\int_{E_R}|f(x)|^2\,dx}{\int_{\mathbb R}|f(x)|^2\,dx}.
\]
Thus the theorem gives a quantitative high-separation law for optimal bandlimited concentration, including its two-dimensional top spectral cluster.

## Assumptions and scope

All sets, operators and parameters are real one-dimensional objects; \(a>0\) is fixed throughout each limit. The two intervals have equal fixed length \(a\). The center distance is \(R>a\). The normalized frequency band has width one. The constants implicit in \(O_a\) and \(O_{a,T}\) may depend on the indicated fixed parameters, and the resonant formula makes no statement for detunings growing with \(m\). A classical prolate-spheroidal fact used here is that \(K_a\) has a simple largest eigenvalue with an even real eigenfunction, separated from the rest of its spectrum [1, 3].

## Proof

**1. An exact commutator and positive coefficients.** Put \(\lambda=\lambda_0(a)\) and \(\psi=\psi_a\). Since \(\psi\) is even, \(\int_J\psi(y)\sin(\pi y)\,dy=0\). Using \(\lambda\psi=K_a\psi\), a direct subtraction gives
\[
 \begin{aligned}
 ((\lambda-K_a)(x\psi))(x)
 &=\int_J(x-y)k(x-y)\psi(y)\,dy\\
 &=\frac1\pi\int_J\sin(\pi(x-y))\psi(y)\,dy\\
 &=\frac{c_a}{\pi}\sin(\pi x).
 \end{aligned}
\]
If \(c_a=0\), then \(x\psi\) would be an eigenfunction for \(\lambda\), orthogonal to the even one-dimensional top eigenspace. Simplicity would force \(x\psi=0\), an impossibility. Hence \(C_a>0\). Furthermore,
\[
 Q_a=\langle x\psi,(\lambda-K_a)x\psi\rangle_{L^2(J)}.
\]
The vector \(x\psi\) is nonzero and odd, hence orthogonal to the top eigenvector. The spectral gap \(\lambda-\lambda_1(a)>0\) makes this quadratic form strictly positive. This also proves \(c_a d_a/\pi>0\) without relying on a sign choice for \(\psi\).

**2. Two-window block operator.** Translation by the two interval centers identifies \(L^2(E_R)\) with \(H\oplus H\), where \(H=L^2(J)\). In this representation the concentration operator is
\[
 \mathcal K_R=\begin{pmatrix}K_a&B_R\\B_R^*&K_a\end{pmatrix},
 \qquad B_R(x,y)=k(x-y-R).
\]
The cross operator has norm \(O_a(R^{-1})\), since \(|x-y|\le a\). Thus the two largest eigenvalues of \(\mathcal K_R\) converge to the double isolated eigenvalue \(\lambda\) of \(K_a\oplus K_a\), and the remainder of its spectrum remains separated by the fixed positive prolate gap for all large \(R\).

**3. Ordinary-distance splitting.** Define finite-rank kernels on \(H\) by
\[
 S(x,y)=\sin(\pi(x-y)),\qquad
 C(x,y)=\cos(\pi(x-y)).
\]
Uniformly on \(J^2\),
\[
 B_R=\frac{\sin(\pi R)C-\cos(\pi R)S}{\pi R}
 +O_a(R^{-2})
\]
in operator norm. Since \(S^*=-S\), \(\langle\psi,S\psi\rangle=0\); since \(\psi\) is even, \(\langle\psi,C\psi\rangle=c_a^2=C_a\). Projecting \(\mathcal K_R\) onto its two-dimensional unperturbed top eigenspace therefore gives the matrix with diagonal \(\lambda\) and off-diagonal \(C_a\sin(\pi R)/(\pi R)+O_a(R^{-2})\). The complement contributes only \(O_a(R^{-2})\) through the uniformly bounded reduced resolvent. The ordered eigenvalues are the first boxed expansion, including when \(\sin(\pi R)=0\).

**4. Resonant kernel expansion.** Set \(R=m+t/m\) with integer \(m>0\) and \(|t|\le T\). Define also
\[
 D(x,y)=(x-y)\sin(\pi(x-y)).
\]
Taylor expansion of the numerator and denominator of \(k(x-y-R)\), uniformly for \((x,y,t)\in J^2\times[-T,T]\), yields
\[
 B_R=(-1)^m\left[-\frac{S}{\pi m}
 +\frac{tC-D/\pi}{m^2}\right]
 +O_{a,T}(m^{-3}).
\]
All remainders are bounded in operator norm, because the kernels are uniformly bounded on the fixed finite square \(J^2\).

**5. Effective two-by-two operator.** Write \(\mathcal K_R=A_0+m^{-1}V_1+m^{-2}V_2+O_{a,T}(m^{-3})\), with \(A_0=K_a\oplus K_a\). Let \(P\) project onto the span of \((\psi,0)\) and \((0,\psi)\), and \(P^\perp=I-P\). We have \(PV_1P=0\). The reduced-resolvent/Feshbach expansion at the isolated eigenvalue \(\lambda\) gives the effective matrix through order \(m^{-2}\):
\[
 \lambda I_2+\frac1{m^2}
 \left[PV_2P+PV_1P^\perp
 (\lambda-P^\perp A_0P^\perp)^{-1}
 P^\perp V_1P\right]_{\operatorname{ran}P}
 +O_{a,T}(m^{-3}).
\]
The inverse is bounded by \((\lambda-\lambda_1(a))^{-1}\). Uniformity follows from this fixed gap and the preceding uniform operator remainder.

**6. Explicit matrix entries.** Evenness of \(\psi\) implies
\[
 \langle\psi,D\psi\rangle
 =2c_a\int_Jx\psi(x)\sin(\pi x)\,dx
 =2c_a d_a=2\pi Q_a.
\]
Consequently,
\[
 PV_2P=(-1)^m(C_a t-2Q_a)
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The operator \(V_1\) sends each basis vector of \(\operatorname{ran}P\) to an odd multiple of \(\sin(\pi x)\) in the opposite component. By the commutator identity from step 1, the unique odd solution of \((\lambda-K_a)u=\sin(\pi x)\) is \(u=\pi x\psi/c_a\). Thus the second-order reduced-resolvent term has zero off-diagonal entries and common diagonal
\[
 \frac{c_a^2}{\pi^2}
 \left\langle\sin(\pi x),(\lambda-K_a)^{-1}\sin(\pi x)\right\rangle
 =\frac{c_a d_a}{\pi}=Q_a.
\]
Here the inverse denotes the inverse restricted to the odd subspace; it is well-defined by the spectral gap. The effective matrix equals
\[
 \lambda I_2+\frac1{m^2}
 \left[Q_a I_2+(-1)^m(C_a t-2Q_a)
 \begin{pmatrix}0&1\\1&0\end{pmatrix}\right]
 +O_{a,T}(m^{-3}).
\]
Its two ordered eigenvalues are exactly \(\lambda+[Q_a\pm|C_a t-2Q_a|]/m^2\) up to the stated remainder, even at the absolute-value cusp. Substituting \(t=0\) and \(t=2Q_a/C_a\) proves both corollaries.

**7. Concentration interpretation.** The orthogonal Fourier projection onto \(PW_{[-1/2,1/2]}\) has integral kernel \(k(x-y)\). Multiplying that projection by the indicator of \(E_R\) on both sides yields a compact positive localization operator. The two operators \(1_{E_R}P_{PW}1_{E_R}\) and \(P_{PW}1_{E_R}P_{PW}\) have identical nonzero eigenvalues by the \(A^*A\)/\(AA^*\) principle. Their largest eigenvalue is the displayed optimal \(L^2\) concentration fraction.

## Verification

A standalone numerical supplement is `CHECK.py` (requires NumPy; see `requirements.txt`). It constructs Nyström discretizations of the exact sinc integral operators using Gauss–Legendre quadrature, tests the ground-state commutator, verifies positivity of \(C_a,Q_a\), and compares the two leading spectral values against both expansions at several lengths, integer separations and microscopic detunings. It also checks separation from the remaining eigenvalues. Run `python CHECK.py` in the folder containing the files. An observed successful run printed `CHECK_OK 279`.

These finite tests are **not** used to infer either the uniform asymptotic statements or exact positivity. Those conclusions follow from the exact identities, spectral gap, and operator-norm expansions in the proof. The tests do not determine optimal constants in the error terms.

## Relationship to prior work

The frequency-concentration and simple-top-eigenvalue setting is classical prolate theory [3]. Recent work on global concentration stability [1] treats sets of fixed total measure and the deficit relative to an interval, but does not calculate the far-separated equal-window spectral doublet or its resonant splitting. The global optimality theorem [2] gives a universal bound for arbitrary sets of a fixed measure; it does not determine either asymptotic coefficient. The spectral analysis of a single sinc interval in [4] supplies context, rather than the two-window coupling formula. Multi-interval sine-kernel determinant asymptotics [5, 6] concern a distinct regime in which the bandwidth or interval scale grows; they do not give fixed-window, large-center-distance top eigenvalue asymptotics.

The new content is the **uniform microscopic doublet law** and its exact positive self-energy coefficient \(Q_a\), derived by the prolate commutator. These are more specific than the generic fact that two distant compact operators weakly couple. The possibility of an earlier unindexed equivalent coupling calculation cannot be ruled out by the available searches.

## Limitations

The interval length must remain fixed as the centers separate. The resonant statement is uniform only for detuning \(|t|\le T\) with fixed \(T\). The theorem concerns the top two eigenvalues only and neither classifies every concentration eigenvalue nor characterizes all maximizing bandlimited functions. At the critical detuning it proves cancellation through order \(m^{-2}\), not an exact crossing. The spectral gap and simplicity of the one-interval prolate ground state are standard external facts [1, 3, 4]. Independent mathematical auditing has not been performed.

## References

1. D. Zelent, *Stability of concentration in the Paley-Wiener space* (first public version 2026-10-01), arXiv:2610.01299, https://arxiv.org/abs/2610.01299.
2. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley-Wiener space* (first public version 2026-07-21), arXiv:2607.19192, https://arxiv.org/abs/2607.19192.
3. D. Slepian and H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty—I*, Bell System Technical Journal 40 (1961), 43–63.
4. A. Bonami, P. Jaming and A. Karoui, *Non-Asymptotic behaviour of the spectrum of the Sinc Kernel Operator and Related Applications*, arXiv:1804.01257, https://arxiv.org/abs/1804.01257.
5. H. Widom, *Asymptotics for the Fredholm determinant of the sine kernel on a union of intervals*, Communications in Mathematical Physics 171 (1995), 159–180, arXiv:hep-th/9405010.
6. B. Fahs and I. Krasovsky, *Sine-kernel determinant on two large intervals* (2020), arXiv:2003.08136, https://arxiv.org/abs/2003.08136.
