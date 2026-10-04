# Exact mass–particle phase diagram of the Ferretti–Teta stability certificate
## Finding
For the regularized impurity model of Ferretti and Teta, the published lower-boundedness theorem assumes \(\gamma>\gamma_c(N,\varsigma)\), where \(N\ge2\), \(\varsigma>0\) is the impurity-to-boson mass ratio, and
\[
\gamma_c(N,\varsigma)=\frac{2(\varsigma+1)}{\pi}\arcsin\!\frac1{\varsigma+1}-\frac{2\sqrt{\varsigma(\varsigma+2)}}{\pi(N-1)(\varsigma+1)}.
\]
The sufficient criterion has an exact mass–particle phase diagram. The function \(\gamma_c\) is strictly decreasing in \(\varsigma\) and strictly increasing in \(N\). If
\[
L_N=\frac2\pi\frac{N-2}{N-1},
\]
then some finite \(\varsigma\) satisfies the sufficient condition exactly when \(\gamma>L_N\). Therefore, when \(0<\gamma<2/\pi\), the feasible particle numbers are exactly
\[
2\le N\le \left\lceil\frac1{1-\pi\gamma/2}\right\rceil,
\]
while for \(\gamma\ge2/\pi\) every finite \(N\) is feasible after choosing a sufficiently large mass ratio.

There is a second, genuinely uniform threshold. Put \(r=(\varsigma+1)^{-1}\) and
\[
G(\varsigma)=\frac2\pi\frac{\arcsin r}r.
\]
A fixed finite \(\varsigma\) satisfies \(\gamma>\gamma_c(N,\varsigma)\) for every finite \(N\ge2\) if and only if \(\gamma\ge G(\varsigma)\). Hence no finite mass ratio works uniformly in \(N\) for \(\gamma\le2/\pi\); for \(2/\pi<\gamma<1\) there is a unique \(\varsigma_\infty(\gamma)\) such that uniform certification holds exactly for \(\varsigma\ge\varsigma_\infty(\gamma)\); and for \(\gamma\ge1\) every positive mass ratio works.

At the critical coupling \(\gamma=2/\pi\), let \(\varsigma_N\) be the unique solution of \(\gamma_c(N,\varsigma_N)=2/\pi\). Then
\[
\varsigma_N\sim\sqrt{\frac{N-1}6}\qquad(N\to\infty).
\]
Likewise,
\[
\varsigma_\infty(\gamma)\sim\frac1{\sqrt{3\pi(\gamma-2/\pi)}}\qquad(\gamma\downarrow2/\pi).
\]
Thus \(2/\pi\) is the transition between finite-size-only theorem certification and certification that can persist through arbitrarily large finite particle number at one fixed finite mass ratio.

## Assumptions and scope
The object is the three-dimensional system in Ferretti–Teta consisting of \(N\) identical spinless bosons and one impurity, with zero-range boson–impurity interactions and the paper's three-body regularization. The parameter \(\varsigma\) is the impurity-to-boson mass ratio used in that work, and \(\gamma\) is the strength entering its regularizing boundary condition. Only the explicit sufficient hypothesis \(\gamma>\gamma_c(N,\varsigma)\) from the lower-boundedness construction is classified here.

No converse instability theorem is asserted. In particular, the boundary \(\gamma=\gamma_c\) need not be the true sharp physical stability boundary of the Hamiltonian family.

## Proof
Set \(q=N-1\) and \(r=(\varsigma+1)^{-1}\in(0,1)\). The source formula becomes
\[
\gamma_c(N,\varsigma)=\frac2\pi F_q(r),\qquad
F_q(r)=\frac{\arcsin r}r-\frac{\sqrt{1-r^2}}q.
\]
For \(0<r<1\),
\[
\frac{d}{dr}\frac{\arcsin r}r
=\frac{r/\sqrt{1-r^2}-\arcsin r}{r^2}>0.
\]
Indeed, if \(h(r)=r/\sqrt{1-r^2}-\arcsin r\), then \(h(0)=0\) and
\[
h'(r)=\frac{r^2}{(1-r^2)^{3/2}}>0.
\]
Also,
\[
\frac d{dr}\left(-\frac{\sqrt{1-r^2}}q\right)
=\frac r{q\sqrt{1-r^2}}>0.
\]
Thus \(F_q\) is strictly increasing in \(r\), so \(\gamma_c\) is strictly decreasing in \(\varsigma\). For fixed \(\varsigma\), increasing \(q\) makes the negative term less negative, proving strict increase in \(N\).

The endpoint limits are
\[
\lim_{\varsigma\downarrow0}\gamma_c(N,\varsigma)=1,
\qquad
\lim_{\varsigma\to\infty}\gamma_c(N,\varsigma)
=\frac2\pi\left(1-\frac1q\right)=L_N.
\]
Because the decrease is strict and the lower endpoint is not attained at finite mass, some finite \(\varsigma\) obeys \(\gamma>\gamma_c\) exactly when \(\gamma>L_N\). If \(0<\gamma<2/\pi\), this inequality is equivalent to
\[
q<\frac1{1-\pi\gamma/2}.
\]
For integer \(q\ge1\), the largest allowed \(N=q+1\) is therefore \(\left\lceil(1-\pi\gamma/2)^{-1}\right\rceil\). If \(\gamma\ge2/\pi\), the inequality holds for every finite \(N\).

For fixed \(\varsigma\), the sequence \(\gamma_c(N,\varsigma)\) increases with \(N\) to
\[
G(\varsigma)=\frac2\pi\frac{\arcsin r}r.
\]
Every finite term is strictly below \(G(\varsigma)\). Hence \(\gamma>\gamma_c(N,\varsigma)\) for every finite \(N\) if and only if \(\gamma\ge G(\varsigma)\). The same derivative argument shows that \(G\) is strictly decreasing in \(\varsigma\), with range \((2/\pi,1)\), which gives the three uniform regimes stated above.

For the critical scaling, the equation \(\gamma_c(N,\varsigma_N)=2/\pi\) is, in terms of \(r_N=(\varsigma_N+1)^{-1}\),
\[
\frac{\arcsin r_N}{r_N}-1=\frac{\sqrt{1-r_N^2}}q.
\]
The right side tends to zero, so strict monotonicity forces \(r_N\to0\). Using
\[
\frac{\arcsin r}r=1+\frac{r^2}6+O(r^4),
\qquad
\sqrt{1-r^2}=1-\frac{r^2}2+O(r^4),
\]
gives \(q r_N^2\to6\), and therefore \(\varsigma_N\sim\sqrt{q/6}\). Finally,
\[
G(\varsigma)-\frac2\pi=\frac{r^2}{3\pi}+O(r^4),
\]
which inverted at \(G(\varsigma_\infty)=\gamma\) yields the stated square-root divergence.

## Verification
The proof is analytic and does not infer any infinite-domain statement from finite sampling. A standalone numerical checker is included only to corroborate representative monotonicity values, the integer particle-count formula, and convergence toward both asymptotic constants. Its output is not used as a proof.

The key nonstandard input is the exact threshold formula from the cited paper. All remaining steps are elementary differentiation, integer inequality handling, and Taylor expansion with the displayed domains and strict inequalities.

## Relationship to prior work
Ferretti and Teta explicitly derive \(\gamma_c(N,\varsigma)\), prove that their main construction works for \(\gamma>\gamma_c\), and record the pointwise infimum and supremum in the mass ratio. They also emphasize uniform boundedness of the threshold in particle number and mass ratio. The inspected source does not classify, for a fixed regularization strength, which particle numbers can be certified, whether one finite mass ratio works for all finite \(N\), or the critical mass scales at \(2/\pi\).

A later Ferretti–Teta paper treats a different model in which the bosons interact with one another by contact interactions and modifies both three- and four-particle coincidence behavior. It does not imply the present impurity-model phase diagram. The closest previously indexed finding concerns a regularized three-boson model with a different threshold and a Mellin-symbol extremum; it is not the same operator or parameter classification.

## Limitations
The result classifies a sufficient hypothesis in one Hamiltonian construction, not the exact physical stability region. The asymptotic statements concern the mass ratio required by that theorem condition. The literature comparison cannot rule out an unindexed equivalent observation; a related doctoral thesis was identifiable but its full text was not accessible during inspection, so that source remains a specific residual originality risk.

## References
1. D. Ferretti and A. Teta, “Regularized Zero-Range Hamiltonian for a Bose Gas with an Impurity,” arXiv:2202.12765v1, first posted 25 February 2022; especially Eq. (2.9), Proposition 2.1, and Theorems 2.2–2.3.
2. D. Ferretti and A. Teta, “Zero-Range Hamiltonian for a Bose Gas with an Impurity,” Complex Analysis and Operator Theory 17, 55 (2023), DOI: 10.1007/s11785-023-01358-4.
3. D. Ferretti and A. Teta, “Hamiltonian for a Bose gas with Contact Interactions,” arXiv:2403.12594, first posted 19 March 2024.
