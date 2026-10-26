# Sharp stationary-simplex collapse for forward/inverse circle dynamics

## Finding
Let \(b\ge 2\) be an integer and \(T_b:\mathbb T\to\mathbb T\) be \(T_b(x)=bx\pmod 1\). Write \(F=(T_b)_*\) for push-forward on probability measures, and let \(Q_b\) select uniformly among the \(b\) inverse images of each point. For \(\alpha,\beta,\gamma\ge0\), \(\alpha+\beta+\gamma=1\), and \(\alpha+\beta>0\), consider the stationary Markov operator \(P=\alpha F+\beta Q_b+\gamma I\).

**Complete classification.** If \(\alpha\le\beta\), normalized Haar measure \(m\) is the **unique** stationary probability. If \(\alpha>\beta\), set \(r=\beta/\alpha<1\). The assignment
\[
\rho\longmapsto\nu_{\rho,r}=(1-r)\sum_{j=0}^{\infty}r^jQ_b^j\rho,
\qquad F\rho=\rho,
\]
is an affine homeomorphism from the full simplex of \(T_b\)-invariant probabilities onto the simplex of \(P\)-stationary probabilities. Its inverse is \(\rho=(F\nu-r\nu)/(1-r)=\lim_{n\to\infty}F^n\nu\), with convergence in total variation. Thus the simplex changes from infinitely many extremal stationary laws to a singleton exactly at \(\alpha=\beta\).

**Quantitative boundary phenomenon.** Uniformly over all \(F\)-invariant \(\rho\), with circle geodesic cost and Wasserstein distance \(W_1\),
\[
W_1(\nu_{\rho,r},m)\le\frac{1-r}{4(1-r/b)}.
\]
For the atomic law arising from \(\rho=\delta_0\),
\[
\frac{1-r}{2\pi}\le W_1(\nu_{\delta_0,r},m)
\le\frac{1-r}{4(1-r/b)}.
\]
Every \(\nu_{\delta_0,r}\) with \(0\le r<1\) is purely atomic and has maximal probability-measure total-variation distance \(\sup_E|\nu_{\delta_0,r}(E)-m(E)|=1\). For \(0<r<1\) the atomic support is dense. Hence the uniform collapse to Haar at the transition has the optimal **linear** order in \(1-r\) in Wasserstein distance, but does not occur in total variation along these atomic laws.

## Assumptions and scope
The circle is \(\mathbb T=\mathbb R/\mathbb Z\), equipped with geodesic distance \(d(x,y)=\min_{k\in\mathbb Z}|x-y+k|\). The operator \(Q_b\) acts on probabilities by averaging the inverse image set: when \(x\in[0,1)\),
\[
Q_b\delta_x=\frac1b\sum_{k=0}^{b-1}\delta_{(x+k)/b}.
\]
Individual inverse branches depend on a fundamental-domain choice, but this averaged probability kernel is well-defined and Feller on the circle. The weights include either zero forward or zero backward probability but exclude the pure-holding process \(\alpha=\beta=0\), for which every probability is stationary. The classification is of *all Borel stationary probabilities* for this quotient kernel, not just measures supported on periodic/preperiodic points, and not stationary measures of an arbitrary nonlinear conjugate system without a demonstrated intertwining.

## Proof
**1. Preimage-grid lemma.** The identity \(FQ_b=I\) follows directly by applying \(T_b\) to every inverse image. Iterating \(Q_b\), the conditional law \(Q_b^j\delta_x\) is the equally weighted grid of \(b^j\) preimages \(\{(x+k)/b^j:0\le k<b^j\}\), with the \(j=0\) convention of a single point. For each \(j\), couple this grid to Haar measure by adding an independent displacement uniform on the centered arc of length \(b^{-j}\) about each grid point. The image of the coupling is Haar because the arcs partition the circle; its expected geodesic transport cost is \(1/(4b^j)\). Integrating the coupling in \(x\) yields
\[
W_1(Q_b^j\mu,m)\le\frac1{4b^j}
\]
for every probability \(\mu\), uniformly in \(\mu\) and \(j\). In particular \(Q_b^j\mu\to m\) weakly. Since \(Q_bm=m\), the only probability fixed by \(Q_b\) is \(m\).

**2. A rigid recurrence.** For \(\alpha>0\), put \(r=\beta/\alpha\). Stationarity \(P\nu=\nu\) is exactly
\[
(1+r)\nu=F\nu+rQ_b\nu.
\]
Define \(\mu_n=F^n\nu\) for \(n\ge0\). Applying \(F^n\) for \(n\ge1\), using \(F^nQ_b=F^{n-1}\), gives
\[
\mu_{n+1}-\mu_n=r(\mu_n-\mu_{n-1}),
\qquad\mu_n=\nu+\Big(\sum_{j=0}^{n-1}r^j\Big)(F\nu-\nu).
\]
Every \(\mu_n\) is a probability, so their signed total-variation norms are bounded. If \(r\ge1\), the unbounded partial sums force \(F\nu=\nu\). The stationary equation and \(r>0\) then give \(Q_b\nu=\nu\), whence \(\nu=m\) by Step 1.

**3. All solutions when forward steps dominate.** Suppose \(0\le r<1\). The recurrence makes \(\mu_n\) a Cauchy sequence in signed total variation; its limit
\[
\rho=\nu+\frac{F\nu-\nu}{1-r}=\frac{F\nu-r\nu}{1-r}
\]
is a probability, and continuity of \(F\) as a total-variation contraction gives \(F\rho=\rho\). Substituting the stationary equation shows
\[
\rho=\frac{\nu-rQ_b\nu}{1-r},\qquad
\nu=(1-r)\rho+rQ_b\nu.
\]
Iteration yields \(\nu=(1-r)\sum_{j=0}^{N}r^jQ_b^j\rho+r^{N+1}Q_b^{N+1}\nu\). Its last term has mass \(r^{N+1}\), proving the claimed infinite series in total variation. Conversely, if \(F\rho=\rho\), then for the convergent displayed series \(F\nu=(1-r)\rho+r\nu\) and \(\nu=(1-r)\rho+rQ_b\nu\); these two identities give the stationary equation. The explicit inverse proves injectivity and surjectivity. Continuity of \(F,Q_b\) in weak topology and uniform convergence of the geometric series give continuity of the map and its inverse; hence an affine homeomorphism. The collection of invariant measures has infinitely many extreme points because \(T_b\) has infinitely many distinct periodic orbits.

**4. Zero forward probability.** If \(\alpha=0\) then \(\beta>0\), and stationarity reduces to \(Q_b\nu=\nu\), so Step 1 again forces \(\nu=m\). Haar is stationary in all cases because both \(F\) and \(Q_b\) preserve Haar.

**5. Optimal Wasserstein order and total-variation discontinuity.** By Step 1, convexity of \(W_1\) in its first argument and the geometric series,
\[
W_1(\nu_{\rho,r},m)\le(1-r)\sum_{j\ge0}\frac{r^j}{4b^j}
=\frac{1-r}{4(1-r/b)}.
\]
Take \(\rho=\delta_0\), invariant under \(T_b\). The measure \(Q_b^j\delta_0\) is supported on the rational \(b\)-adic grid; its integral of \(\cos(2\pi x)\) vanishes for \(j\ge1\), while the \(j=0\) integral equals one. Therefore \(\int \cos(2\pi x)\,d\nu_{\delta_0,r}=1-r\). The real-valued circle test \(f(x)=\cos(2\pi x)/(2\pi)\) is 1-Lipschitz and Haar-centered. Kantorovich–Rubinstein duality gives \(W_1(\nu_{\delta_0,r},m)\ge(1-r)/(2\pi)\). Every grid measure is finite atomic, so their countable geometric mixture is purely atomic. The union of all grids is dense when \(r>0\), yet countable and Haar-null. Taking this countable union as the event in the probability-measure total-variation definition gives distance one. This completes the proof.

## Verification
An independent exact-fraction finite-truncation diagnostic is supplied as `checks/check.py`, with its output in `checks/output.txt`. It tests 240 combinations of degree, periodic seed, geometric ratio, and truncation level. For every tested case it proves by exact rational arithmetic the nonasymptotic identity
\[
(1+r)\nu_N-F\nu_N-rQ_b\nu_N
=(1-r)r^{N+1}(Q_b^N\rho-Q_b^{N+1}\rho),
\]
where \(\nu_N=(1-r)\sum_{j=0}^N r^jQ_b^j\rho\). It additionally tests uniform-grid identities in 45 finite cases. These computations are not a substitute for the infinite-measure proof in Steps 1–5.

## Relationship to prior work
Goverse and Kleptsyn, arXiv:2607.11421v1, Section 4.3, display the degree-two quotient kernel with forward doubling, holding, and equiprobable inverse branches in equation (4.17). Their Proposition 4.11, equation (4.25), establishes **the forward construction** \(\rho\mapsto(1-r)\sum_jr^jQ^j\rho\) for doubling-invariant \(\rho\) under \(r<1\). That entire construction and the identity \(FQ=I\) are credited here as prior work. The new statement is the **converse exhaustiveness and affine-simplex equivalence**, the unique-stationary collapse at and below balance, and the optimal-order Wasserstein convergence with persistent total-variation singularity. The source also describes uniqueness among dyadic-supported states; this is logically weaker than uniqueness among all Borel probabilities and is not claimed here as new. The present argument treats arbitrary integer degree \(b\).

Homburg and Kalle, arXiv:2207.09987v1, study related expanding/contracting affine random maps and emphasize one-point stationary Haar measure, while their main theorems classify synchronization/intermittency and two-point stationary motions. Those results do not explicitly classify the full *one-point* stationary simplex above. The new claim is deliberately limited to the symmetric inverse-branch kernel; general transfer-operator or renewal methods could yield part of the proof after specialization.

## Limitations
This is a statement about the specified quotient Markov kernel, not a uniqueness theorem for the full nonlinear random system in the motivating paper, not a statement that every stationary law is physical, and not a classification of two-point motions. The quantitative bound uses circle geodesic \(W_1\); it does not imply convergence in total variation. The degree \(b\) must be an integer at least two and the inverse branches must be chosen with exactly equal probability. Earlier general operator-theoretic principles may implicitly subsume portions of the result, so independent priority review remains important.

## References
1. V. Goverse and V. Kleptsyn, *Atomic physical measures for non-invertible random dynamical systems*, arXiv:2607.11421v1 (first public 2026-07-13), especially Section 4.3 and Proposition 4.11. https://arxiv.org/abs/2607.11421
2. A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, arXiv:2207.09987v1 (first public 2022-07-20), particularly Sections 1, 3, and 4.2. https://arxiv.org/abs/2207.09987
