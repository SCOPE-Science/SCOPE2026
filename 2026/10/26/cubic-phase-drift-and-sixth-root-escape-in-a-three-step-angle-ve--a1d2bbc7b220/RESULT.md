# Cubic phase drift and sixth-root escape in a three-step angle–velocity map

## Finding

Fix a nonzero real parameter \(P\). Consider the positive-root realization of the angle–velocity map of Khandelwal and Mukherjee at angular step \(2\pi/3\):
\[
\theta_{j+1}=\theta_j+2\pi/3\pmod{2\pi},\qquad
\omega_{j+1}-\omega_j=P\sin\theta_j\left(\frac1{\omega_j}+\frac1{\omega_{j+1}}\right),\qquad \omega_j>0.
\]
There exists an absolute constant \(C>0\) such that, whenever \(y=\omega_0^2>C|P|\), the first three steps use the unique positive branch near the identity, and the three-step return \(\mathcal R_P(\theta,y)=\omega_3^2\) satisfies
\[
\mathcal R_P(\theta,y)-y=-\frac{3P^3}{y^2}\sin(3\theta)
\left(1+O\!\left(\frac{|P|}{y}\right)\right).
\tag{1}
\]
The relative error in (1) is uniform for every real \(\theta\), including arbitrarily close to its six zeros. At those zeros the left-hand side vanishes **exactly** for every \(y>C|P|\). In particular, the phase fibers \(\theta\equiv j\pi/3\pmod{2\pi}\), \(j=0,\ldots,5\), are precisely the period-three fibers in this high-energy region. On each other fiber, the sign of the three-step change in squared speed is exactly \(-\operatorname{sgn}(P^3\sin3\theta)\).

More precisely, keep an initial phase \(\theta\) fixed under the three-step return and write \(y_m=\omega_{3m}^2\). If \(-P^3\sin3\theta>0\) and \(y_0>C|P|\), the positive-root solution exists at every future step, \(y_m\to\infty\), and
\[
\lim_{m\to\infty}\frac{\omega_{3m}^{6}}{m}=-9P^3\sin(3\theta)>0.
\tag{2}
\]
If \(-P^3\sin3\theta<0\), the first return below any fixed chosen threshold \(Y>C|P|\), from initial squared speed \(y_0\to\infty\), occurs after \(N_Y(y_0)\) three-step blocks, where
\[
N_Y(y_0)\sim\frac{y_0^3}{9|P|^3|\sin(3\theta)|}
=\frac{\omega_0^6}{9|P|^3|\sin(3\theta)|}.
\tag{3}
\]
Statement (3) concerns first passage out of the high-energy region; it does not claim that the map ceases to exist afterward.

## Assumptions and scope

The angle lies in \(\mathbb R/(2\pi\mathbb Z)\); speed is strictly positive; \(P\ne0\); and the angular increment is exactly \(2\pi/3\), the smallest admissible nontrivial rotation period in the source model. The source allows \(P\) to have either sign. All assertions concern the positive square-root branch given by its equation (11), not any other algebraic root of the implicit relation. The universal threshold constant need not be optimized. Equalities at \(\theta=j\pi/3\) require only a high-enough initial speed; the asymptotic time laws require \(\sin3\theta\ne0\) fixed while the corresponding limits are taken. Period three means exactly three steps, since the angle component has least period three.

## Proof

**1. Analytic one-step transformation.** Put \(a=P\sin\theta\), \(y=\omega^2\), and \(t=a/y\). Dividing the implicit recurrence by \(\omega\), and writing \(r=\omega'/\omega\), gives
\[
r^2-(1+t)r-t=0,\qquad
r(t)=\frac{1+t+\sqrt{1+6t+t^2}}2.
\]
This is the branch with \(r(0)=1\). The map on squared speeds is \(G_a(y)=yr(a/y)^2\). For sufficiently small \(|t|\) this is positive and real analytic, with the convergent Taylor expansion
\[
r(t)^2=1+4t+0t^2+4t^3-16t^4+O(t^5),
\qquad G_a(y)=y+4a+\frac{4a^3}{y^2}+O\!\left(\frac{|a|^4}{y^3}\right).
\tag{4}
\]
The error in (4) and its derivatives in any smooth bounded angular parameter have uniform bounds on any sufficiently small fixed parameter disk. These bounds follow directly from analyticity of the displayed square root around zero.

**2. Three-step cancellation and cubic residue.** Let \(a_j=P\sin(\theta+2\pi j/3)\) for \(j=0,1,2\). Then \(\sum_j a_j=0\) and, by \(\sin^3 u=(3\sin u-\sin3u)/4\),
\[
\sum_{j=0}^2a_j^3=-\frac{3P^3}{4}\sin(3\theta).
\]
Starting from \(y\gg|P|\), each intermediate squared speed is \(y+O(|P|)\). Summing (4) over the three updates therefore gives
\[
\mathcal R_P(\theta,y)-y
=\frac4{y^2}\sum_{j=0}^2a_j^3+O\!\left(\frac{|P|^4}{y^3}\right)
=-\frac{3P^3\sin3\theta}{y^2}+O\!\left(\frac{|P|^4}{y^3}\right).
\tag{5}
\]
The remainder in (5), differentiated once with respect to \(\theta\), remains \(O(|P|^4/y^3)\), uniformly in phase. To see this without relying on a formal asymptotic expansion, set \(\rho=P/y\) and write the normalized three-step map by iterating \(Y\mapsto Y r(\rho\sin\theta_j/Y)^2\), starting from \(Y=1\). On a fixed neighborhood of \(\rho=0\), all three successive iterates are jointly real analytic in \(\rho\) and \(\theta\), and the Taylor remainder and its first angular derivative have the advertised uniform order.

**3. Exact return on the six grid phases.** At every \(\theta\equiv j\pi/3\), the ordered three forcing values are a permutation of \((0,A,-A)\), with the two nonzero entries occupying the remaining consecutive steps after the identity step is ignored. Interchanging the incoming and outgoing positive speeds in the defining implicit equation changes \(a\) to \(-a\). Thus the near-identity branches obey \(G_{-A}\circ G_A=G_A\circ G_{-A}=\operatorname{id}\) whenever the intermediate squared speeds remain high. Consequently \(\mathcal R_P(\theta,y)=y\) exactly on all six grid phases for sufficiently large \(y/|P|\).

**4. Uniform sign all the way to the grid.** Define the normalized remainder
\[
E(\rho,\theta)=\frac{\mathcal R_P(\theta,y)-y}{y}+3\rho^3\sin3\theta,
\qquad \rho=P/y.
\]
By Step 2, both \(E\) and \(\partial_\theta E\) are bounded by \(K|\rho|^4\) for a universal \(K\), and Step 3 shows \(E(\rho,j\pi/3)=0\) exactly. If \(d\) is the circular distance from \(\theta\) to \((\pi/3)\mathbb Z\), then \(0\le d\le\pi/6\) and the mean-value theorem gives \(|E|\le K|\rho|^4d\). On this interval \(|\sin3\theta|=\sin(3d)\ge6d/\pi\). Hence \(|E|\le K'|\rho|^4|\sin3\theta|\). For \(|\rho|\) below a universal positive threshold, the cubic term dominates at every non-grid phase; (1) and the sign classification follow without excluding any thin angular neighborhoods.

**5. Escape and descent in original iteration time.** For fixed phase \(\theta\) outside the grid, write \(c=-3P^3\sin3\theta\ne0\). The three-step recurrence has the uniform tail form
\[
y_{m+1}-y_m=\frac c{y_m^2}+O\!\left(\frac{|P|^4}{y_m^3}\right).
\tag{6}
\]
If \(c>0\), sufficiently high states increase forever, and cannot converge to a finite limit because the return increment is positive and continuous throughout the high-energy region. Hence \(y_m\to\infty\). Expanding the difference of cubes in (6) gives \(y_{m+1}^3-y_m^3=3c+o(1)\), so Cesàro averaging yields \(y_m^3/m\to3c\), proving (2). All intermediate speeds remain real and positive because they stay within the same high-energy branch domain.

If \(c<0\), every high-energy iterate decreases strictly. Were infinitely many iterates to stay above the fixed threshold, their monotone limit would contradict strict negativity of the increment; consequently the threshold is crossed in finitely many returns. For any large auxiliary level \(B\), while \(y_m\ge B\) the cube increment equals \(3c+O(|P|^4/B)\) and is uniformly close to \(3c<0\). The number of additional steps between \(B\) and the fixed threshold is bounded independently of the starting speed, by strict negativity and compactness. First let \(y_0\to\infty\), then \(B\to\infty\). This yields the first-passage asymptotic (3).

## Verification

The standalone `verify.py` recomputes the positive-root branch directly, tests the limiting cubic coefficient for two signs of \(P\) and three off-grid phases at large squared speed, checks exact cancellation for three possible placements of the zero forcing step using high-precision decimal arithmetic, and evaluates the sixth-root growth diagnostic over 500000 three-step blocks. The captured output is `VERIFY_RUN.txt`, ending in `CHECKS_PASS`. These are finite checks of formulas and implementation, not proofs of uniform angular sign or asymptotic limits; those are proved in Steps 1–5. The numerical approach to the limit can be slow because the initial squared speed contributes an additive constant to its cube.

## Relationship to prior work

Khandelwal and Mukherjee, *A Two-Dimensional Map of Arbitrary Period*, arXiv:2412.15002v1 (first public date 2024-12-19), introduce exactly this positive-root map. Their Theorem 3.5 establishes period-\(N\) orbit families at the half-step angular grid; Section 4 derives a local series and an approximate energy integral; Section 5.1 observes numerical drift off that grid. For \(N=3\), the result here gives the missing high-energy *converse* to the period-three construction, a signed cubic return term uniform even near the exact-return phases, and quantitative long-time escape/first-passage laws. The source's one-step series alone does not establish the three-step cancellation, the near-grid uniform sign, or the accumulated sixth-power law.

## Limitations

The classification is confined to the three-step rational-angle case and to squared speeds above a universal multiple of \(|P|\). It does not classify low-speed three-cycles, higher-period angle increments, arbitrary irrational angles, or the continuation of descending trajectories after they leave the controlled high-energy region. No optimal universal threshold is asserted. Priority searches cannot exclude unpublished or differently indexed equivalent treatments; independent scientific and literature review has not been performed.

## References

1. Aakash Khandelwal and Ranjan Mukherjee, *A Two-Dimensional Map of Arbitrary Period*, arXiv:2412.15002v1 (2024-12-19), https://arxiv.org/abs/2412.15002 . Relevant material: equations (1)–(2), (6), (9), (11); Theorem 3.5; Sections 4 and 5.1.
