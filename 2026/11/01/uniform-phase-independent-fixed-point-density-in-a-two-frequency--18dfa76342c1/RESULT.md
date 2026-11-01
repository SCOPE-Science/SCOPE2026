# Uniform phase-independent fixed-point density in a two-frequency sine map

## Finding

For fixed positive frequencies \(\omega _1\ne\omega _2\) with irrational ratio \(\omega _1/\omega _2\), consider the one-dimensional map
\[
T_{A,\varphi}(x)=A\bigl(\sin(\omega _1(x-\varphi))+\sin(\omega _2(x-\varphi))\bigr),\qquad A>0,\quad\varphi\in\mathbb R.
\]
Let \(N_A(\varphi)\) be the number of **distinct real fixed points** and let \(J_A(\varphi)\) be the number of those fixed points satisfying \(|T'_{A,\varphi}(x)|\le1\). All these counts are finite. Then, **uniformly over the entire phase line**,
\[
\lim_{A\to\infty}\sup_{\varphi\in\mathbb R}\left|\frac{N_A(\varphi)}A-\mathcal C(\omega _1,\omega _2)\right|=0,
\qquad
\lim_{A\to\infty}\sup_{\varphi\in\mathbb R}\frac{J_A(\varphi)}A=0,
\]
where the **sharp coefficient** is the explicit torus integral
\[
\mathcal C(\omega _1,\omega _2)=\frac1{(2\pi)^2}\int_0^{2\pi}\int_0^{2\pi}
\left|\omega _1\cos u+\omega _2\cos v\right|\,du\,dv.
\]
It obeys the strict comparative bounds
\[
\frac{2\max(\omega _1,\omega _2)}\pi<\mathcal C(\omega _1,\omega _2)
<\frac{2(\omega _1+\omega _2)}\pi.
\]
Consequently, the number of fixed points increases linearly with amplitude and asymptotically all fixed points are linearly repelling: the proportion with multiplier modulus at most one tends to zero. The leading coefficient is independent of phase, despite the finite-amplitude multistability emphasized in the model's original numerical study.

## Assumptions and scope

The map is considered on all of \(\mathbb R\), not modulo any period. Each fixed point is counted once, regardless of tangency or algebraic multiplicity. Frequencies are fixed, strictly positive, distinct and irrationally related; \(A\to\infty\), and \(\varphi\) may vary arbitrarily with \(A\). The conclusion is not asserted for rationally related frequencies, for amplitude-varying frequencies, or for periodic points of prime period exceeding one. A nonrepelling fixed point means \(|T'|\le1\), including neutral points; no nonlinear attraction statement is inferred from \(|T'|=1\).

## Proof

**1. Reduction and finiteness.** Write
\[
S(u,v)=\sin u+\sin v,\quad D(u,v)=\omega _1\cos u+\omega _2\cos v,\quad f(t)=S(\omega _1t,\omega _2t).
\]
Putting \(t=x-\varphi\), fixed points are exactly the zeros, on \([-2A-\varphi,2A-\varphi]\), of
\[
h_{A,\varphi}(t)=f(t)-(t+\varphi)/A.
\]
No fixed point lies outside \([-2A,2A]\) since the map takes values there. This is a nonzero real-analytic function (its linear term is unbounded whereas \(f\) is bounded); hence it has finitely many zeros on the compact interval. At its zeros the map multiplier is \(A f'(t)=A D(\omega _1t,\omega _2t)\). Set \(M=\omega _1^2+\omega _2^2\); throughout the line, \(|h''_{A,\varphi}|=|f''|\le M\).

**2. Uniform bound on zeros in short cells.** There are constants \(h_0>0\) and \(A_0>0\), depending only on the frequencies, such that for \(A\ge A_0\), every interval of length at most \(h_0\) contains at most three distinct zeros of \(h_{A,\varphi}\), uniformly in its location and in \(\varphi\). To prove this, first note that the three derivatives \(h'\), \(h''\), \(h'''\) cannot vanish simultaneously for all sufficiently large \(A\). Otherwise, along a sequence \(A\to\infty\), compactness of the phase torus would yield
\[
\omega _1\cos u+\omega _2\cos v=0,\quad
\omega _1^2\sin u+\omega _2^2\sin v=0,\quad
\omega _1^3\cos u+\omega _2^3\cos v=0.
\]
The first and third identities force \(\cos u=\cos v=0\) (distinct positive frequencies), while the second would require \(\omega _1^2=\omega _2^2\), a contradiction. The same compactness argument, with \(A^{-1}\) in a sufficiently short closed interval beginning at zero, gives a uniform positive lower bound for the maximum absolute value of those three derivatives. Were there no uniform \(h_0\), a sequence of cells with lengths tending to zero and four zeros would, by three applications of Rolle's theorem and continuity of derivatives, force a common zero of \(h'\), \(h''\), \(h'''\), again a contradiction. Thus the short-cell bound holds. No explicit value of \(h_0\) is needed in the asymptotic argument.

**3. Uniform slow-fast equidistribution.** Select any \(h\in(0,h_0)\) such that the translation
\[
(u,v)\longmapsto(u+\omega _1h,v+\omega _2h)\pmod{2\pi}
\]
is uniquely ergodic on the two-torus. Such \(h\) are all sufficiently small positive numbers except a countable exceptional set: irrationality of \(\omega _1/\omega _2\) makes every nonzero integer combination \(m\omega _1+n\omega _2\) nonzero. For a bounded Riemann-integrable function \(G\) on \(\mathbb T^2\times[-2,2]\), sample the torus at \(\theta_k=(\omega _1(t_0+kh),\omega _2(t_0+kh))\) and let \(s_k=(t_0+kh+\varphi)/A\), with \(t_0\) any point within \(h\) of \(-2A-\varphi\). Fourier approximation in the torus variables, the geometric-sum estimate for each nonzero Fourier mode, and Riemann sums for the slow variable show that
\[
\frac1A\sum_{k:\,s_k\in[-2,2]}G(\theta_k,s_k)
\longrightarrow\frac1h\int_{-2}^{2}\int_{\mathbb T^2}G(\theta,s)\,dm(\theta)\,ds,
\]
uniformly in \(t_0\), hence uniformly in \(\varphi\). Here \(dm=du\,dv/(2\pi)^2\). For indicator functions with boundary of product measure zero, continuous majorants and minorants justify the same limit. The starting grid can be shifted by less than \(h\) to avoid zeros exactly at grid vertices, which is possible because there are only finitely many roots.

**4. Counting sign changes.** Partition the interval in Step 1 into cells of length \(h\), retaining at most two shorter endpoint cells. Let \(Q_A(h,\varphi)\) count strict changes of sign of \(h_{A,\varphi}\) across full cells. Endpoint cells contribute at most six roots by Step 2. By Step 3, because the boundary of the sign-crossing indicator has zero product measure,
\[
\lim_{A\to\infty}\frac{Q_A(h,\varphi)}A
=\frac1h\int_{-2}^{2}\int_{\mathbb T^2}
\mathbf1_{\{(S(\theta)-s)(S(\theta+h\omega)-s)<0\}}\,dm(\theta)\,ds,
\]
uniformly in phase. Since both values of \(S\) lie in \([-2,2]\), integrating the indicator first in \(s\) yields exactly the absolute difference of those values. Thus
\[
\lim_{A\to\infty}\frac{Q_A(h,\varphi)}A
=\frac1h\int_{\mathbb T^2}|S(\theta+h\omega)-S(\theta)|\,dm(\theta).
\tag{1}
\]

**5. Tangencies and multiple crossings cannot change the density.** In a full cell where root count and strict sign-change count differ, there is both a root \(r\) and a point \(t_*\) with \(h'_{A,\varphi}(t_*)=0\): this follows from Rolle when there are two or more distinct roots, and from Fermat's theorem for a single tangential root. The bound \(|h''|\le M\) implies at the left grid point \(\ell\)
\[
|h_{A,\varphi}(\ell)|\le Mh^2,\qquad
|f'(\ell)|\le Mh+A^{-1}.
\]
For fixed \(h\) and large \(A\), such a bad cell therefore has
\[
|S(\theta_\ell)-s_\ell|\le Mh^2,\qquad |D(\theta_\ell)|\le2Mh.
\]
Let \(B_A\) count these cells. Step 3 and Fubini's theorem give
\[
\limsup_{A\to\infty}\sup_\varphi\frac{B_A}A
\le\frac1h\int_{-2}^{2}m\bigl(|S-s|\le Mh^2,\ |D|\le2Mh\bigr)\,ds
\le2Mh\,m(|D|\le2Mh).
\]
The last factor tends to zero with \(h\), since the nonconstant analytic function \(D\) has a zero set of torus measure zero. Each bad cell has at most three roots by Step 2; hence
\[
\limsup_{A\to\infty}\sup_\varphi\frac{|N_A(\varphi)-Q_A(h,\varphi)|}A
\le6Mh\,m(|D|\le2Mh).
\]
Let \(h\downarrow0\) along admissible grid sizes. The right side tends to zero, whereas the right side of (1) converges by dominated convergence to \(\int_{\mathbb T^2}|D|\,dm\). This proves the stated uniform count law, including possible tangencies at exceptional amplitudes.

**6. Nonrepelling roots have zero density.** A fixed point with \(|T'|\le1\) corresponds to a root \(r\) with \(|f'(r)|\le A^{-1}\). Its cell's left endpoint then satisfies, for large \(A\),
\[
|f'(\ell)|\le2Mh,\qquad |h_{A,\varphi}(\ell)|\le3Mh^2,
\]
by the Lipschitz bound on \(f'\). Every cell has at most three roots. Applying Step 3 to the two indicated inequalities shows that
\[
\limsup_{A\to\infty}\sup_\varphi \frac{J_A(\varphi)}A
\le18Mh\,m(|D|\le2Mh).
\]
Letting \(h\downarrow0\) proves the second limit.

**7. Strict coefficient comparisons.** Let \(U,V\) be independent uniform angles. If \(\omega _1\ge\omega _2\), conditional Jensen gives \(\mathbb E_V|\omega _1\cos U+\omega _2\cos V|\ge|\omega _1\cos U|\), with strict inequality for a positive-measure set of \(U\) near a cosine zero. Thus \(\mathcal C>2\omega _1/\pi\); interchange the frequencies if necessary. Strict triangle inequality in expectation gives \(\mathcal C<2(\omega _1+\omega _2)/\pi\), because the cosine terms have opposite signs with positive probability. This completes the proof.

## Verification

The included `check.py` evaluates the torus integral by two independent uniform grids (256 and 512 points per coordinate), checks the strict coefficient bounds, and performs finite sign-change counts for twelve amplitude/phase cases at \((\omega _1,\omega _2)=(1,\sqrt2)\). Execution with Python 3 standard library passed. The numerical estimate is \(\mathcal C(1,\sqrt2)\approx1.01692769\). Finite grids may miss tangential roots and are explicitly **not** an exhaustive proof of the counts. The uniform infinite-asymptotic and negligible-nonrepelling conclusions rest on Steps 2–7, not on numerical experiments.

## Relationship to prior work

Ali et al. (2023), DOI 10.1088/1572-9494/acf307, introduced the two-sine map and studied equilibrium stability, phase variation, multistability and numerical bifurcations. The cited source's inspected equations (4)–(6) and Sections 3–4 do not give a large-amplitude fixed-point census or the torus-integral coefficient. Ramadoss et al. (2023), DOI 10.1088/1402-4896/acb303, study a related two-sine map with a shifting bifurcation parameter and report numerical steady-state behavior; its exact formula/full text could not be established here, so the possibility of an implicit related census there is a priority risk. Classical uniform distribution and zero-crossing methods supply proof ingredients, but neither the usual single-sine root count nor general zeros of random trigonometric polynomials immediately states this phase-uniform deterministic two-frequency fixed-point coefficient. This is an explicit comparison of propositions, not a claim that absence from search results proves novelty.

## Limitations

The result gives only the leading \(o(A)\) error, with no effective rate uniform over all irrational frequency ratios. It does not classify attractors, basins, higher-period cycles, or the exceptional nonrepelling fixed points themselves. The exact coefficient is an elementary two-dimensional integral rather than a claimed elementary closed form. The full text of a plausibly related 2023 paper was not accessible; publication priority and independent validation remain open.

## References

1. A. M. Ali Ali, S. Sriram, H. Natiq, A. Ahmadi, K. Rajagopal, and S. Jafari, “A novel multi-stable sinusoidal chaotic map with spectacular behaviors,” *Communications in Theoretical Physics* **75** (2023), 115001. DOI: 10.1088/1572-9494/acf307. Published 2023-09-29 (publisher PDF cover).
2. J. Ramadoss, H. Natiq, F. Nazarimehr, S. He, K. Rajagopal, and S. Jafari, “A novel chaotic map with a shifting parameter and stair-like bifurcation diagram: dynamical analysis and multistability,” *Physica Scripta* **98** (2023), 025212. DOI: 10.1088/1402-4896/acb303.
3. S. Steinerberger, “Roots of trigonometric polynomials and the Erdős–Turán theorem,” *Mathematika* **66** (2020), 245–254. DOI: 10.1112/mtk.12003 (related but different root-counting setting).
