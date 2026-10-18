# Critical-window crossover and Euler correction for alpha-Farey escape

## Finding
Consider the piecewise-linear intermittent alpha-Farey maps with partition tails \(t_k=k^{-\theta}\), \(k\ge1\), where \(\theta>0\), and the Markov hole \([0,t_n]\), \(n\ge2\). Let \(\gamma_n(\theta)\) be their Perron--Frobenius spectral escape rate. The natural transition between the finite-invariant-measure regime \(\theta>1\) and infinite-invariant-measure regime \(\theta\le1\) has a uniform critical window that is absent from fixed-parameter small-hole asymptotics.

**Theorem (moving-exponent crossover).** For every sequence \(\theta_n>0\) with \(\theta_n\to1\), put \(L_n=\log n\), \(c_n=(\theta_n-1)L_n\), and define the continuous positive function
\[
\Phi(c)=\begin{cases}c/(e^c-1),&c\ne0,\\1,&c=0.\end{cases}
\]
Then, without any boundedness assumption on \(c_n\),
\[
\lim_{n\to\infty}\frac{nL_n\gamma_n(\theta_n)}{\Phi(c_n)}=1.
\]
For every fixed \(C>0\), uniformly in \(|c|\le C\), let \(\theta_n=1+c/L_n\) and \(\Psi(c)=(1-e^{-c})/c\), with \(\Psi(0)=1\). Then
\[
nL_n\gamma_n(1+c/L_n)=\Phi(c)\left[1-\frac{\gamma_{\!E}-e^{-c}}{L_n\Psi(c)}+O_C(L_n^{-2})\right],
\]
where \(\gamma_{\!E}\) is Euler's constant. Consequently, \(n\log n\,\gamma_n\to\Phi(c)\) when \(c_n\to c\in\mathbb R\). When \(c_n\to+\infty\), this scaled escape rate tends to zero; when \(c_n\to-\infty\), it diverges like \(-c_n\). These statements concern the escape rate as a spectral observable, not a polynomial survival law for every initial distribution.

## Assumptions and scope
For a given \(\theta>0\) define \(t_k=k^{-\theta}\), \(a_k=t_k-t_{k+1}>0\), \(A_k=(t_{k+1},t_k]\). The alpha-Farey map is
\[
F_\theta(x)=\begin{cases}(1-x)/a_1,&x\in A_1,\\ \frac{a_{k-1}}{a_k}(x-t_{k+1})+t_k,&x\in A_k,\ k\ge2,\\0,&x=0.\end{cases}
\]
The hole is \(H_{n,\theta}=[0,t_n]\), leaving the finite collection of branches \(A_1,\ldots,A_{n-1}\). The escape rate is \(\gamma_n=-\log\lambda_n\), where \(\lambda_n\) is the strictly positive Perron root of the finite open transfer matrix on the branch-constant subspace. The spectral characterization for these Markov holes, and its polynomial identity below, are established in Knight--Munday (2014/2016). The present theorem does **not** assert arbitrary-observable decay or extension to non-Markov holes.

## Proof
**1. Exact root and the first truncated renewal moment.** The known finite-matrix characteristic identity is
\[
1-\sum_{k=1}^{n-1}a_k z^k=0.
\]
Since \(\sum_{k=1}^{n-1}a_k=1-t_n<1\) and every \(a_k>0\), it has a unique real root \(z_n>1\). Monotonicity and Perron theory identify \(z_n=\lambda_n^{-1}\). Thus \(\gamma_n=\log z_n>0\) uniquely solves
\[
\sum_{k=1}^{n-1}a_k(e^{k\gamma_n}-1)=t_n.\tag{1}
\]
Set \(S_n=\sum_{k=1}^{n-1}k a_k\). Summation by parts gives the **exact** identity
\[
S_n=\sum_{j=1}^{n}j^{-\theta}-n^{1-\theta}.\tag{2}
\]
No replacement of this finite sum by the divergent or convergent full zeta function is needed.

**2. Uniform control for every moving exponent approaching one.** Put \(\delta_n=\theta_n-1\), \(c_n=\delta_n\log n\), and
\[
I_n=\int_1^n x^{-1-\delta_n}\,dx=(\log n)\Psi(c_n).
\]
For all sufficiently large \(n\), the integrand is positive decreasing; the sum--integral comparison yields
\[
\sum_{j=1}^n j^{-1-\delta_n}=I_n+O(1),\qquad S_n=I_n-e^{-c_n}+O(1).\tag{3}
\]
The error in (3) is independent of \(n\) and of \(\delta_n\) in a fixed neighbourhood of zero. Elementary examination of \((1-e^{-c_n})/\delta_n\), including the continuous case \(\delta_n=0\), shows \(I_n\to\infty\) and \(e^{-c_n}/I_n\to0\) for every sequence \(\delta_n\to0\). Therefore \(S_n\sim I_n\).

Let \(R_n(g)=\sum_{k=1}^{n-1}a_k(e^{kg}-1)\). By \(e^u-1\ge u\) for \(u\ge0\), (1) gives
\[
0<n\gamma_n\le\frac{nt_n}{S_n}=\frac{e^{-c_n}}{S_n}\longrightarrow0.\tag{4}
\]
With \(M_{2,n}=\sum_{k<n}k^2a_k\le nS_n\) and \(e^u-1-u\le u^2e^u/2\) for \(u\ge0\),
\[
0\le R_n(\gamma_n)-\gamma_nS_n
\le\frac{\gamma_n^2}{2}e^{n\gamma_n}M_{2,n},
\]
so the relative error compared with \(\gamma_nS_n\) is bounded by \(\frac12n\gamma_ne^{n\gamma_n}=o(1)\). Equation (1) now implies \(\gamma_n\sim t_n/S_n\), and since \(t_n=e^{-c_n}/n\),
\[
\frac{n(\log n)\gamma_n}{\Phi(c_n)}
\sim\frac{e^{-c_n}(\log n)}{I_n\Phi(c_n)}=1.
\]
This proves the first statement even when \(|c_n|\to\infty\).

**3. Sharp first finite-size correction in the bounded window.** Fix \(C<\infty\), take \(\delta=c/L_n\) with \(|c|\le C\), and note that the discrepancy between the sum and the integral admits the uniform expansion
\[
\sum_{j=1}^{n}j^{-1-c/L_n}-\int_1^n x^{-1-c/L_n}\,dx
=\gamma_{\!E}+O_C(L_n^{-1}).\tag{5}
\]
For completeness, write the discrepancy as \(\sum_{j=1}^n[j^{-1-\delta}-\int_j^{j+1}x^{-1-\delta}\,dx]\) plus the harmless endpoint integral \(\int_n^{n+1}x^{-1-\delta}\,dx\). The infinite discrepancy series converges absolutely and locally uniformly in \(\delta\) for \(|\delta|<1/2\); termwise differentiation is justified by the summable majorant \(O(j^{-2+|\delta|}\log j)\), so its value is \(\gamma_{\!E}+O(|\delta|)\). The endpoint and tail are \(O_C(1/n^{1-o(1)})\). This proves (5).

Thus (2) sharpens to
\[
S_n=L_n\Psi(c)+\gamma_{\!E}-e^{-c}+O_C(L_n^{-1}).\tag{6}
\]
Moreover \(a_k\le\theta k^{-\theta-1}\) for \(\theta>0\), so \(M_{2,n}\le\theta\sum_{k<n}k^{-c/L_n}=O_C(n)\). From (4), \(\gamma_n=O_C((nL_n)^{-1})\). Hence
\[
R_n(\gamma_n)-\gamma_nS_n=O_C((nL_n^2)^{-1}),
\]
which is a relative \(O_C(L_n^{-2})\) contribution to (1), because \(t_n=e^{-c}/n\asymp_C1/n\). Substituting (6), expanding its reciprocal, and multiplying by \(nL_n\) yields
\[
nL_n\gamma_n=\frac{e^{-c}}{\Psi(c)}
\left[1-\frac{\gamma_{\!E}-e^{-c}}{L_n\Psi(c)}+O_C(L_n^{-2})\right]
\]
as required.

**4. Regimes outside the bounded window.** From the first equivalence, \(c_n\to+\infty\) gives \(\Phi(c_n)\sim c_ne^{-c_n}\to0\), while \(c_n\to-\infty\) gives \(\Phi(c_n)\sim-c_n\to\infty\). The middle case uses continuity of \(\Phi\).

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It verifies the exact harmonic telescoping and first-moment identities with rational arithmetic, numerically solves (1) by bisection for three detunings and three cutoffs, prints both asymptotic predictions, and checks the root residual and orientation of the positive-root bracket. Execute `python3 verify.py` in the extracted package directory; its expected terminal marker is `VERIFY_OK`. These finite checks corroborate the algebra and scaling trend but do not prove the theorem: the proof above supplies uniform estimates over infinitely many cutoffs and moving exponents.

## Relationship to prior work
Knight and Munday (arXiv:1411.3515, initially public 2014-11-13, revised 2016) introduce the identical family and finite open determinant, and separately calculate the fixed-parameter escape regimes \(\theta>1\), \(\theta=1\), and \(\theta<1\) (sections 3--4). They neither state a joint \((n,\theta)\) limit with \((\theta-1)\log n\) fixed or unrestricted, nor its uniform Euler correction. Their exact finite determinant is explicitly used here; obtaining the new statement requires controlling the first moment and exponential remainder uniformly when the parameter varies. Bonanno--Chouari (arXiv:1512.04432) treat smooth Farey-map holes rather than this detuned partition. Bonanno--Tikekar (arXiv:2601.15908, theorem 3.6 and example 3.3) derive fixed-index parabolic/Markov-hole trichotomies, not this simultaneous parameter--hole limit or first finite-size coefficient. General renewal and Tauberian methods offer plausible alternate derivations and therefore remain a historical-priority risk.

## Limitations
The result is restricted to the power-tail alpha-Farey family, Markov holes of the form \([0,n^{-\theta_n}]\), and \(\theta_n\to1\). Uniformity of the **Euler correction** is asserted only for bounded \(c\); the leading equivalence permits unbounded \(c_n\). The theorem does not specify arbitrary initial-condition escape distributions, non-Markov holes, or non-power partition tails. The first coefficient depends on the precise finite-hole convention. The comparative literature assessment cannot exclude unpublished or unindexed equivalent calculations; no independent scientific audit has been carried out.

## References
1. G. Knight and S. Munday, *Escape rate scaling in infinite measure preserving systems*, arXiv:1411.3515 (first public 2014-11-13; revised 2016); especially sections 2--4 and equation (12). https://arxiv.org/abs/1411.3515
2. C. Bonanno and M. Chouari, *Escape rates for the Farey map with approximated holes*, arXiv:1512.04432 (2015). https://arxiv.org/abs/1512.04432
3. C. Bonanno and A. Tikekar, *On the escape rate for intermittent maps with holes shrinking around the indifferent fixed point*, arXiv:2601.15908 (2026), theorem 3.6 and example 3.3. https://arxiv.org/abs/2601.15908
