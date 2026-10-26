# A fractional-order Cesàro commutator trace and a shift-invariant boundary flux

## Finding
For real \(s>0\) and \(\alpha>-1\), define the lower-triangular matrix on \(\ell_2(\mathbb N_0)\)
\[
(T_{s,\alpha})_{nj}=
\begin{cases}
\displaystyle s\frac{\Gamma(n-j+s)}{\Gamma(n-j+1)}
\frac{\Gamma(n+\alpha+1)}{\Gamma(n+\alpha+s+1)},&0\le j\le n,\\
0,&j>n.
\end{cases}
\]
It induces a bounded operator. Write \(P_N\) for projection onto the first \(N+1\) coordinate vectors, and let \(D_{s,\alpha}=T_{s,\alpha}^*T_{s,\alpha}-T_{s,\alpha}T_{s,\alpha}^*\). The **finite-section commutator flux** has an exact limit independent of the shift parameter:
\[
\boxed{\lim_{N\to\infty}\operatorname{tr}(P_ND_{s,\alpha}P_N)
=F(s)}
\]
where \(\psi=\Gamma'/\Gamma\), \(\gamma\) is Euler's constant, and
\[
F(s)=\begin{cases}
\displaystyle\frac{s^2(\psi(2s)+\gamma)}{2s-1},&s\ne\tfrac12,\\
\displaystyle\frac{\pi^2}{24},&s=\tfrac12.
\end{cases}
\]
For \(\alpha=0\), the operator is the Hausdorff matrix with Beta\((1,s)\) representing measure. By the classical subnormality theorem for bounded Hausdorff matrices on \(\ell_2\), \(D_{s,0}\) is positive. Consequently \(D_{s,0}\) belongs to trace class and \(\operatorname{Tr}(D_{s,0})=F(s)\) for **every real** \(s>0\), not just integral orders. For every positive integer \(m\), the formula specializes to \(F(m)=m^2H_{2m-1}/(2m-1)\), as in an already available integer-order result.

## Assumptions and scope
All operators act on complex \(\ell_2(\mathbb N_0)\). Parameters satisfy \(s>0\) and \(\alpha>-1\); no uniformity in either parameter is claimed. The trace of \(P_N D P_N\) is a **finite-dimensional** trace, even when the full self-commutator has not been shown to be trace class. In the shifted case \(\alpha\ne0\), the theorem makes no claim of hyponormality or trace-class membership. The full trace conclusion is specifically for \(\alpha=0\).

The Hausdorff representation at \(\alpha=0\) is exact:
\[
(T_{s,0})_{nj}=\binom nj\int_0^1 t^j(1-t)^{n-j}\,s(1-t)^{s-1}\,dt.
\]
The measure is nonnegative, has total mass one, and yields a bounded operator as proved below.

## Proof
**1. Boundedness.** For fixed \(s>0\) and \(\alpha>-1\), gamma-ratio estimates, including finite indices by increasing the constant, give
\[
0\le(T_{s,\alpha})_{nj}\le C_{s,\alpha}
\frac{(n-j+1)^{s-1}}{(n+1)^s},\qquad 0\le j\le n.
\]
For \(w_k=(k+1)^{-1/2}\), split the elementary sums at the midpoint to obtain
\[
\sum_{j=0}^n\frac{(n-j+1)^{s-1}}{(n+1)^s}w_j\le C_sw_n,
\quad
\sum_{n=j}^\infty\frac{(n-j+1)^{s-1}}{(n+1)^s}w_n\le C_sw_j.
\]
For the first inequality, when \(j\le n/2\), the summand's convolution factor is bounded by a constant times \((n+1)^{s-1}\); for \(j>n/2\), \(w_j\lesssim(n+1)^{-1/2}\) and the sum of \((n-j+1)^{s-1}\) is \(O((n+1)^s)\). For the second inequality split into \(j\le n\le2j+1\) and \(n>2j+1\). The first part reduces to \((j+1)^{-s-1/2}\sum_{k\le j+2}k^{s-1}=O((j+1)^{-1/2})\), and the tail is \(O(\sum_{n>2j+1}(n+1)^{-3/2})\). Schur's test proves boundedness.

**2. Exact finite-section identity.** Lower triangularity, with justified nonnegative column-square sums, gives for every \(N\ge0\)
\[
\operatorname{tr}(P_ND_{s,\alpha}P_N)
=\sum_{n=N+1}^\infty\sum_{j=0}^N |(T_{s,\alpha})_{nj}|^2
=:\Phi_N(s,\alpha).
\]
Indeed, the terms with both row and column at most \(N\) cancel exactly between \(T^*T\) and \(TT^*\). This is an identity, not a positivity assertion about the full operator.

**3. Limiting boundary flux.** Gamma-ratio asymptotics give, uniformly on positive compact intervals away from zero,
\[
\frac{\Gamma(k+s)}{\Gamma(k+1)}=k^{s-1}(1+O_s(k^{-1})),\qquad
\frac{\Gamma(n+\alpha+1)}{\Gamma(n+\alpha+s+1)}=n^{-s}(1+O_{s,\alpha}(n^{-1})).
\]
After writing \(x=n/N\), \(y=j/N\), on every strip \(1+\varepsilon\le x\le R\), \(0\le y\le1\), the summand is uniformly
\[
N^{-2}s^2(x-y)^{2s-2}x^{-2s}(1+o(1)).
\]
Thus the sum on that strip converges to its double integral. For the large-row tail \(n\ge RN\), \(R\ge2\), the gamma bound in step 1 makes the total at most \(C_{s,\alpha}/R\), uniformly in \(N\). For the near-boundary strip \(N<n\le(1+\varepsilon)N\), put \(r=n-N\). The total is at most a constant times
\[
N^{-2s}\sum_{1\le r\le\varepsilon N}\sum_{k=r}^{N+r}(k+1)^{2s-2},
\]
which is \(O_s(\varepsilon^{2s})\) for \(0<s<1/2\), \(O(\varepsilon(1+|\log\varepsilon|))\) for \(s=1/2\), and \(O_s(\varepsilon)\) for \(s>1/2\), uniformly as \(N\to\infty\). Consequently the limits \(\varepsilon\downarrow0\), \(R\to\infty\) establish
\[
\lim_{N\to\infty}\Phi_N(s,\alpha)
=s^2\int_1^\infty\int_0^1(x-y)^{2s-2}x^{-2s}\,dy\,dx.
\]
The limiting integral is independent of \(\alpha\).

**4. Exact evaluation for all positive orders.** Substitute \(u=y/x\) and interchange the nonnegative integrals:
\[
\int_1^\infty\int_0^1(x-y)^{2s-2}x^{-2s}\,dy\,dx
=\int_0^1(1-u)^{2s-2}(-\log u)\,du.
\]
Setting \(t=1-u\) and expanding \(-\log(1-t)\) as a nonnegative series gives
\[
\int_0^1t^{2s-2}(-\log(1-t))\,dt
=\sum_{k=1}^\infty\frac1{k(k+2s-1)}.
\]
For \(2s\ne1\), the digamma series identity evaluates this as \((\psi(2s)+\gamma)/(2s-1)\); when \(2s=1\), it equals \(\zeta(2)=\pi^2/6\). All exchanges are justified by nonnegativity for \(s>0\).

**5. The trace-class consequence.** At \(\alpha=0\) the displayed Beta integral makes \(T_{s,0}\) a bounded Hausdorff operator. Sharma's classical subnormality theorem, stated explicitly in the update to Rhaly (2017, Section 5) and recalled in Ma (2026, Section 1), gives \(D_{s,0}\ge0\) for any real \(s>0\). For a positive bounded operator the canonical trace is the supremum of its finite coordinate diagonal sums. Step 3 proves those sums tend to the finite \(F(s)\), so \(D_{s,0}\) is trace class and its trace is exactly \(F(s)\). Finally \(\psi(2m)+\gamma=H_{2m-1}\) at positive integers.

## Verification
The accompanying `check_fractional_flux.py` uses standard-library arithmetic only. It replays the finite compression identity for small matrices, calculates finite tail-flux approximants from gamma recurrences, and checks their approach to the formula at integer and noninteger orders, including the removable half-order value. Numerical checks support the algebra and asymptotic scales; the infinite assertion relies on the preceding estimates and the cited Hausdorff subnormality theorem.

## Relationship to prior work
Sharma's bounded-Hausdorff subnormality theorem provides the classical positivity input but not the present explicit nonintegral trace profile. Rhaly's 2017 paper identifies the fractional-order Cesàro matrices and quotes Sharma's theorem. Ma's September 18, 2026 preprint studies hyponormality **at positive integer order** for all shifts \(\alpha>-1\), with primary classification 47B20. An available October 2026 result computes exactly \(m^2H_{2m-1}/(2m-1)\) and trace norms at integer \(m\). Those integer statements are not asserted to be new here. The new assertion is the explicit continuous-order profile and, separately, its shift-invariant finite-boundary-flux interpretation for every \(s>0\). A 2024 Hausdorff-factorization paper describes the fractional-order matrix, but no trace profile was identified in accessible text. This is a best-knowledge priority assessment, not a proof of uniqueness.

## Limitations
For shifted \(\alpha\ne0\) the result concerns only the limit of finite-section traces, not the full trace or trace-norm of the self-commutator, which may have both signs. No new proof of Sharma's general subnormality theorem is supplied. The result does not determine the Schatten spectrum, eigenvectors, or optimal bounds of the shifted commutators. The 2024 factorization source was only partially accessible; independent source-complete priority checking remains appropriate.

## References
- Y. Ma, *Hyponormality of generalized Cesàro matrices of every positive integer order*, arXiv:2610.00193v1, September 18, 2026; Theorem 1.1 and introduction. https://arxiv.org/html/2610.00193v1
- H. C. Rhaly Jr., *A conjecture on hyponormality for the Cesàro matrix of positive integer order*, arXiv:1701.00425v2, 2017; Section 5 and its reference to Sharma's theorem. https://arxiv.org/html/1701.00425v2
- N. K. Sharma, *Hausdorff Operators*, Acta Sci. Math. **35** (1973), 165–167; subnormality theorem, as cited by Rhaly.
- *Factorization of Hausdorff Operators*, Axioms **13** (2024), 813; Section 4 (fractional Cesàro matrices). https://www.mdpi.com/2075-1680/13/12/813
- An indexed integer-order result, *A shift-invariant harmonic trace for generalized Cesàro self-commutators* (October 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-shift-invariant-harmonic-trace-for-generalized-ces-ro-self-com--b9745d36b9d7 .
