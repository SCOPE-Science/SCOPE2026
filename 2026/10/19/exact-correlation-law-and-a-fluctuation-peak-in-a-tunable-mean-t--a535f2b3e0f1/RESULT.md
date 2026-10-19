# Exact correlation law and a fluctuation peak in a tunable-mean tent family

## Finding

Fix a real parameter \(0<b<1/2\). For the endpoint-tunable piecewise-linear family of Moysis, Lawnik, Volos, Baptista and Goudos, restrict the endpoint parameters to \(a=b\) and \(c=0\), so that the interval map becomes
\[
T_b(x)=\begin{cases}
b+\dfrac{1-b}{b}x,&0\le x\le b,\\[3pt]
\dfrac{1-x}{1-b},&b<x\le1.
\end{cases}
\]
This map has one mixing, physical, absolutely continuous invariant probability \(\mu_b\), with density
\[
\rho_b(x)=\begin{cases}
(1+b)^{-1},&0<x<b,\\
(1-b^2)^{-1},&b<x<1.
\end{cases}
\]
Its exact stationary mean is \(m_b=(1+b+b^2)/(2(1+b))\), increasing strictly from \(1/2\) toward \(7/12\).

Let \(f_b(x)=x-m_b\), and define the stationary covariance at lag \(n\ge0\) by
\[
C_n(b)=\int_0^1 f_b(x)f_b(T_b^n x)\,\rho_b(x)\,dx.
\]
All of these covariances are encoded by the following **exact rational function**:
\[
\boxed{\displaystyle
\sum_{n=0}^{\infty}C_n(b)z^n=
\frac{(b^2-b+1)\bigl[(b^2+3b+1)+(b^4+2b^3-2b^2+b)z+b^3(b^2+b+1)z^2\bigr]}
{12(1+b)^2(1+bz)\bigl(1+(1-b)^2z+b^2z^2\bigr)}.}
\]
The series converges at \(z=1\). Under stationary sampling \(X\sim\mu_b\), the normalized centered orbit sum obeys
\[
\frac1{\sqrt n}\sum_{j=0}^{n-1}(T_b^jX-m_b)
\ \Longrightarrow\ \mathcal N(0,\sigma_b^2),
\qquad
\boxed{\displaystyle \sigma_b^2=
\frac{b(1-b)(b^2-b+1)}{12(1+b)^3}.}
\]
The variance \(\sigma_b^2\) is strictly positive and, although the mean is strictly increasing, is **strictly increasing then strictly decreasing**: its unique maximizer on \((0,1/2)\) is the root \(b_*\approx0.227260049622555\) of
\[
\boxed{\ b^4+4b^3-8b^2+6b-1=0.\ }
\]
At the distinct parameter \(b_{\mathrm{res}}=2-\sqrt3\), the three nontrivial transfer eigenvalues coalesce at \(-b_{\mathrm{res}}\), producing a genuine third-order pole of the covariance generating function. Thus at resonance the all-lag covariance is a quadratic polynomial in the lag times \((-b_{\mathrm{res}})^n\). As \(b\downarrow0\), \(\sigma_b^2\sim b/12\) although the one-time stationary variance tends to \(1/12\).

## Assumptions and scope

The state space is the closed interval \([0,1]\), with the continuous convention at the branch point given above. Every assertion holds for each fixed real \(b\) with \(0<b<1/2\), not uniformly in the singular limit \(b=0\). The two Markov intervals are \(I_0=[0,b]\) and \(I_1=[b,1]\); endpoint choices do not affect the invariant density or the distributional assertion. The central limit theorem uses an initial point drawn from the stationary law \(\mu_b\). Mixing and the physical-measure conclusion imply the almost-everywhere time-average assertions for Lebesgue initial points, but do not assert Gaussian limits for every deterministic point.

## Proof

**Invariant Markov density.** The slopes are \((1-b)/b>1\) and \(-1/(1-b)<-1\). The first branch maps \(I_0\) onto \(I_1\), and the second maps \(I_1\) onto the whole interval. The corresponding topological transition matrix is \(\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\), whose square is strictly positive. Standard primitive expanding-Markov-map theory therefore gives a unique mixing absolutely continuous invariant probability. The Perron–Frobenius equation on the two constant-density cells is solved by the displayed \(\rho_b\). Directly,
\[
\frac{b}{1+b}+\frac{1-b}{1-b^2}=1,
\quad
\int_0^1 x\rho_b(x)dx=\frac{1+b+b^2}{2(1+b)}.
\]
The density is bounded above and below by positive constants, so ergodic time averages hold for Lebesgue-almost-every initial point: the measure is physical.

**Finite transfer space.** Let \(\mathcal P\) be the four-dimensional space of functions which are affine on each Markov cell. Encode \(q\in\mathcal P\) by \((A_0,B_0,A_1,B_1)^\mathsf T\), meaning \(q(x)=A_j+B_jx\) on \(I_j\). The transfer operator with respect to Lebesgue measure is \((Pq)(x)=\sum_{T_by=x}q(y)/|T_b'(y)|\). Its restriction to \(\mathcal P\) has the exact matrix
\[
M_b=\begin{pmatrix}
0&0&1-b&1-b\\
0&0&0&-(1-b)^2\\
\dfrac b{1-b}&-\dfrac{b^3}{(1-b)^2}&1-b&1-b\\
0&\dfrac{b^2}{(1-b)^2}&0&-(1-b)^2
\end{pmatrix}.
\]
Indeed, a point in \(I_0\) has only the right-branch preimage \(1-(1-b)x\); a point in \(I_1\) has that preimage and the left-branch preimage \(b(x-b)/(1-b)\), yielding the four rows. Its characteristic polynomial factors exactly:
\[
\det(\lambda I-M_b)=(\lambda-1)(\lambda+b)
\bigl(\lambda^2+(1-b)^2\lambda+b^2\bigr).
\]
The nontrivial three eigenvalues have modulus strictly less than \(1\): \(-b\in(-1,0)\), and the quadratic is Schur stable because \(b^2<1\), \(1-(1-b)^2+b^2=2b>0\), and \(1+(1-b)^2+b^2>0\).

**Covariance generating function.** Put \(r_0=(1+b)^{-1}\), \(r_1=(1-b^2)^{-1}\), and encode the centered signed density \(f_b\rho_b\) by
\[
v_b=(-m_br_0,r_0,-m_br_1,r_1)^\mathsf T.
\]
Let \(\ell_b\) be the linear functional integrating \(f_bq\) over \([0,1]\). Transfer duality gives \(C_n(b)=\ell_b M_b^n v_b\). The vector \(v_b\) has zero total integral; hence its cyclic subspace has no eigencomponent corresponding to \(1\). Summing the matrix resolvent yields
\[
\sum_{n\ge0}C_n(b)z^n
=\ell_b(I-zM_b)^{-1}v_b,
\]
and exact rational simplification gives the boxed generating formula. All steps are algebraic over \(\mathbb Q(b,z)\); they are reproduced by the companion symbolic checker, which also independently computes sample correlations by exact piecewise-affine integration.

**Gaussian limit and exact long-run variance.** Define the invariant-measure transfer operator \(\mathcal Lg=\rho_b^{-1}P(\rho_bg)\). Its iterates applied to \(f_b\) decay geometrically in the finite invariant affine space, so
\(h_b=\sum_{n\ge1}\mathcal L^n f_b\) converges uniformly and is bounded. Set \(d_b=f_b+h_b-h_b\circ T_b\). Transfer duality implies \(\mathcal Ld_b=0\). Thus \(d_b\circ T_b^j\) forms a stationary reverse-martingale-difference sequence, and
\[
\sum_{j=0}^{n-1}f_b\circ T_b^j
=\sum_{j=0}^{n-1}d_b\circ T_b^j-h_b+h_b\circ T_b^n.
\]
The remainder is uniformly bounded. The stationary ergodic martingale central limit theorem therefore gives a normal limit with variance \(\int d_b^2d\mu_b\). Geometric covariance decay identifies that variance as the Green–Kubo sum
\[
\sigma_b^2=C_0(b)+2\sum_{n\ge1}C_n(b)
=2G_b(1)-G_b(0),
\]
where \(G_b\) is the boxed generating function. Simplification yields the boxed formula, which is positive for \(0<b<1/2\).

**Unique fluctuation peak and resonance.** Exact differentiation gives
\[
\frac{d\sigma_b^2}{db}=-\frac{Q(b)}{12(1+b)^4},
\quad Q(b)=b^4+4b^3-8b^2+6b-1.
\]
On \([0,1/2]\), \(Q''(b)=12b^2+24b-16\le-1\), so \(Q'\) is decreasing and \(Q'(b)\ge Q'(1/2)=3/2>0\). Because \(Q(0)=-1\) and \(Q(1/2)=9/16\), the root \(b_*\) is unique, with the asserted increase and decrease. At \(b_{\mathrm{res}}=2-\sqrt3\), \((1-b_{\mathrm{res}})^2=2b_{\mathrm{res}}\), so the generating-function denominator is \((1+b_{\mathrm{res}}z)^3\) up to its nonzero constant factor. Its numerator does not vanish at \(z=-1/b_{\mathrm{res}}\) (its unreduced value is \(126-72\sqrt3\ne0\)), establishing a genuine triple pole.

## Verification

Run the standalone `verify.py` with Python 3 and SymPy. It reconstructs the transfer matrix, invariant density, characteristic polynomial, the first three covariance values, the entire rational resolvent, the exact Green–Kubo variance, the derivative and resonance identities. It separately splits inverse branch cylinders into rational subintervals and integrates \(f_b(x)f_b(T_b^n x)\) in exact rational arithmetic for \(b\in\{1/5,1/4,1/3,2/5\}\) and \(0\le n\le8\), producing 36 independently calculated covariance matches. Those finite checks corroborate the proof but are not substituted for the infinite-family algebra and ergodic argument.

## Relationship to prior work

The three-parameter piecewise family and its numerically tunable stationary mean appear in Moysis et al. (2023), extending the earlier MOCAST conference paper. The full later article explicitly identifies theoretical parameter–statistics relationships as future work; it does not state this exact invariant law, rational all-lag covariance, variance peak, or transfer resonance. General Frobenius–Perron/Markov-map methods and central limit theorems are established prior tools, not claimed new here. McDonald, Van Wyk and Cilliers (2025) develop prescribed-density and power-spectrum-pole map-design techniques; that broader design methodology neither specifies these exact constants for the Moysis slice nor states the variance maximum or the coalescent correlation poles. Similarities in technique do not constitute identification of this parameter-specific theorem.

## Limitations

The analysis applies only to the expanding Markov slice \(a=b,c=0,0<b<1/2\), not all endpoint parameters or the nonexpanding boundary. It does not estimate the speed of central-limit convergence or treat finite-precision numerical orbits. A complete four-page version of the originating 2023 conference paper could not be inspected, leaving a priority risk even though the accessible expanded article and related published work were compared in substance. Novelty beyond the inspected corpus is not independently certified. No independent mathematical audit has been performed.

## References

1. L. Moysis, M. Lawnik, M. S. Baptista, S. K. Goudos and C. Volos, *Construction of Piecewise Chaotic Maps With Tunable Statistical Mean*, MOCAST (2023), DOI: 10.1109/MOCAST57943.2023.10176612. Publisher release reported as 17 July 2023; full conference text not accessible in this review.
2. L. Moysis, M. Lawnik, C. Volos, M. S. Baptista and S. K. Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission*, Symmetry **15** (2023), 2138, DOI: 10.3390/sym15122138. Public expanded full article.
3. A. M. McDonald, M. A. Van Wyk and J. É. Cilliers, *The Design of Discrete-Time Systems With Prescribed Probability Distribution and Power Spectrum Poles*, IEEE Access **13** (2025), 65900–65924, DOI: 10.1109/ACCESS.2025.3558799. General map-design methods, publicly accessible full article.
4. M. I. Gordin, *The central limit theorem for stationary processes*, Soviet Math. Dokl. **10** (1969), 1174–1176. Martingale approximation principle.
