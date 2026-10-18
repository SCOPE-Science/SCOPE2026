# Coarsening can destroy concavity of an unconstrained log-concave density fit

## Finding
Consider the weighted observations at the five sites \(0,1,2,3,4\). Define the continuous piecewise-affine function \(h\) with respective nodal heights
\[
(0,3,3,11/4,9/4),
\]
and let \(\phi_i\) denote the standard hat function at site \(i\) on this five-node grid. Define **exact**, strictly positive observation weights
\[
w_i=\frac{\int_0^4\phi_i(t)e^{h(t)}\,dt}{\int_0^4e^{h(t)}\,dt},\qquad 0\le i\le4.
\]
The unique log-concave maximum-likelihood estimate has log-density \(h-\log\int_0^4e^h\), supported on \([0,4]\), and has all four fine-grid segments as maximal linear pieces.

Merge the first two segments of this optimal subdivision: constrain the unnormalized log-density to be affine on \([0,2]\), \([2,3]\), and \([3,4]\), but do **not** impose concavity on this reduced piecewise-exponential family. Its unique unrestricted maximum-likelihood estimate has **strictly increasing** slopes at the last interior knot \(3\). In particular, a subdivision coarser than the log-concave optimum need not yield a concave unrestricted fit.

This is a counterexample, within weighted one-dimensional density estimation, to the general coarsening implication posed as an open question in the 2023 article *Exact solutions in log-concave maximum likelihood estimation* [1, Section 2, discussion following its subdivision examples].

## Assumptions and scope
Weights may be arbitrary positive real numbers summing to one, as in the weighted log-concave maximum-likelihood problem. The weights above are defined by convergent elementary definite integrals; their numerical values are only illustrative:
\[
(w_0,w_1,w_2,w_3,w_4)\approx
(0.031617194143,0.258582060168,0.341391243051,0.268564591086,0.099844911553).
\]
The reduced family consists of probability densities supported on \([0,4]\) proportional to \(e^g\), where \(g(0)=0\) and \(g\) is affine between its nodes \(0,2,3,4\). The support restriction, positivity of weights, dimension one, and absence of concavity constraints in the reduced maximization are essential to the precise statement. The result does not claim that the concavity-constrained estimate on the coarse model is nonconcave (which is impossible by definition).

## Proof
**1. Exact optimal fine-grid likelihood.** The slopes of \(h\) on its four unit segments are \(3,0,-1/4,-1/2\), strictly decreasing. Hence its logarithm is concave and has precisely the stated optimal subdivision. For an arbitrary vector of fine nodal heights \(v\), write \(h_v=\sum_{i=0}^4v_i\phi_i\) and
\[
F_{\rm fine}(v)=\log\int_0^4e^{h_v(t)}\,dt-\sum_{i=0}^4w_i v_i.
\]
Its gradient at the prescribed heights vanishes componentwise by the defining integrals for the weights. Its Hessian is the covariance matrix of the hat functions under the strictly positive density proportional to \(e^{h_v}\). It is positive definite modulo adding the same constant to all heights: a linear combination of all the hats has zero variance exactly when it is constant. Thus \(h\) is the unique optimum modulo normalization among fine piecewise-affine log-densities. Moreover, any other log-concave density supported on the data convex hull has likelihood no better than its least concave nodal tent: for fixed nodal values, the tent has no greater integral than the log-concave interpoland, so replacing the latter by the tent and renormalizing cannot decrease likelihood. Therefore this fine optimum is also the log-concave MLE over the unrestricted log-concave class, by the standard tent-envelope principle [1,2].

**2. The coarse score and certified trial.** Write \(\psi_1,\psi_2,\psi_3\) for the hats at coarse knots \(2,3,4\), and \(g_u=u_1\psi_1+u_2\psi_2+u_3\psi_3\). The reduced objective is
\[
F(u)=\log\int_0^4e^{g_u(t)}\,dt-\sum_{i=0}^4w_i g_u(i).
\]
Because each coarse hat is affine on every fine-grid segment, \(\sum_iw_i\psi_j(i)=\int_0^4\psi_j e^h/\int_0^4e^h\). Consequently its score is the difference of expectation vectors of the coarse hats under the coarse and fine normalized exponential densities.

Choose the **rational** trial point
\[
u=\left(\frac{17027588}{10000000},\frac{11063547}{10000000},\frac{7452502}{10000000}\right).
\]
The companion `certificate_knots.py` evaluates 24th-degree Taylor-polynomial integrals using exact rational arithmetic. For each score coordinate it proves an interval contained in \((-10^{-6},10^{-6})\); hence
\[
\|\nabla F(u)\|_2<2\times10^{-6}.
\]
The Taylor remainder bound employed is \(e^3 3^{25}/25!<27\,3^{25}/25!\), valid because all trial and fine heights lie in \([0,3]\); positivity of the remainder yields exact rational ratio enclosures.

**3. Local strong convexity bounds the unknown optimizer.** Put \(r=1/100\). For all \(v\) with \(\|v-u\|_2\le r\), one has \(-r\le g_v(t)\le 2\). Using \(e^2<9\) and \(e^{-r}>99/100\), the normalized density \(e^{g_v}/\int_0^4e^{g_v}\) is bounded below by \(1/40\) on \([0,4]\). Hence the Hessian covariance obeys, for all \(a\in\mathbb R^3\),
\[
a^\top\nabla^2F(v)a\ \ge\ \frac1{40}a^\top H a,
\]
where \(H\) is the *centered Lebesgue Gram matrix* of the three nonconstant coarse hats:
\[
H=\begin{pmatrix}7/16&-5/24&-3/16\\-5/24&5/12&1/24\\-3/16&1/24&13/48\end{pmatrix}.
\]
Sylvester's criterion establishes \(H-(1/10)I\succ0\): its three leading principal minors equal respectively \(27/80\), \(457/7200\), and \(257/108000\). Therefore \(\nabla^2F(v)\succ I/400\) throughout this ball. On its boundary, Taylor's formula gives
\[
F(v)-F(u)>-2\cdot10^{-6}r+\frac{r^2}{800}>0.
\]
By convexity along rays, no global minimizer lies outside the ball; its minimum is attained inside. The covariance is strictly positive definite globally because the three coarse hats are independent modulo constants, so the global minimizer \(u_*\) is unique and \(\|u_*-u\|_2<r\).

**4. Positive jump in the coarse log-density slope.** The signed jump at knot \(3\) is
\[
J(u_*)=(u_*)_3-2(u_*)_2+(u_*)_1.
\]
At the rational trial point its exact value is
\[
J(u)=\frac{588249}{2500000}=0.2352996.
\]
The ball bound implies \(|J(u_*)-J(u)|\le4r=0.04\), so \(J(u_*)>0.1952996>0\). This strictly *upward* jump contradicts concavity of the unrestricted coarse optimum. The coarse partition is obtained by deleting the first interior fine knot, so it is genuinely coarser than the optimal log-concave subdivision. This completes the counterexample.

## Verification
Run `python3 certificate_knots.py` with a standard Python interpreter. The script has no third-party dependencies and independently builds the fine/coarse integrals as rational polynomials, certifies each score interval, checks strict positive-definiteness of the centered Gram matrix, and verifies the final slope-jump inequality. Its output includes `CERTIFIED: unique coarse critical point lies within radius 1/100; its final slope jump is positive.` The Python checks are finite *exact arithmetic* certificates for the explicit inequalities; the global proof rests on the analytic convexity argument above.

## Relationship to prior work
Grosdos, Heaton, Kubjas, Kuznetsova, Scholten and Sorea [1] formulate the unconstrained optimizer on a prescribed subdivision and explicitly ask whether every subdivision coarser than the optimal log-concave subdivision necessarily gives a concave fit. Their examples of incompatible subdivisions do not refute the particular coarsening assertion. The five-point weighted example above supplies a counterexample to precisely that assertion. Robeva, Sturmfels and Uhler [2] prove that every regular subdivision can be realized as the actual optimal log-concave subdivision for some sample weights; that changes the sample weights and does not imply any statement about unconstrained fits after coarsening *fixed* weights. No claim is made that every coarse subdivision fails concavity.

## Limitations
Weights are exactly defined but generally nonrational. Numerical knot values alone do not prove the claim; the rational enclosure certificate supplies the necessary rigorous control. The assertion concerns weighted samples, not an example with equal integer multiplicities, and dimension one only. Published literature searches cannot rule out unindexed or inaccessible prior counterexamples. A subsequent corrigendum to [1] addresses another portion of the source work according to available revision metadata; its complete text was not independently inspected, so any unlocated discussion of the coarsening question remains an originality risk. Independent mathematical review has not been performed.

## References
[1] A. Grosdos, A. Heaton, K. Kubjas, O. Kuznetsova, G. Scholten and M.-Ş. Sorea, *Exact solutions in log-concave maximum likelihood estimation*, arXiv:2003.04840 (first publicly available 2020-03-10), *Advances in Applied Mathematics* **143** (2023), article 102448. DOI: 10.1016/j.aam.2022.102448. Full open text: https://d-nb.info/1303792095/34.

[2] E. Robeva, B. Sturmfels and C. Uhler, *Geometry of log-concave density estimation*, arXiv:1704.01910 (first available 2017-04-06), *Discrete & Computational Geometry* **61** (2019), 136–160. DOI: 10.1007/s00454-018-0024-y. Full HTML: https://arxiv.org/html/1704.01910.

[3] A. Grosdos et al., *Corrigendum to “Exact solutions in log-concave maximum likelihood estimation”*, *Advances in Applied Mathematics* **162** (2025), article 102777. DOI: 10.1016/j.aam.2024.102777 (bibliographic metadata inspected; full text not read).
