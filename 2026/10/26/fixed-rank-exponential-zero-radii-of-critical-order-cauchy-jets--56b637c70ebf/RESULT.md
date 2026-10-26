# Fixed-rank exponential zero radii of critical-order Cauchy jets on regular polygons

## Finding
For each integer \(N\ge3\), set \(U_N=\{\zeta\in\mathbb C:\zeta^N=1\}\) and consider the rational Cauchy jet
\[
F_N(z)=\sum_{\zeta\in U_N}(z-\zeta)^{-N}.
\]
Its zeros consist of \(N-1\) distinct regular \(N\)-gons, on rays \(\arg z=(2h+1)\pi/N\) for \(0\le h<N\). All zeros are simple and lie on distinct circles. In particular, for even \(N\) exactly one polygon lies on the unit circle; otherwise none does.

Order the distinct radii below one as \(0<R_{N,1}<R_{N,2}<\cdots\). Define \(\beta_0=1\), \(\beta_j=(j+1)^{j+1}/j^j\) for \(j\ge1\), and \(c_k=\beta_{k-1}/\beta_k\). For each fixed positive integer \(k\), as \(N\to\infty\) through \(N\ge2k+1\),
\[
R_{N,k}=c_k\exp\left(\frac{\gamma_k(N)+o(1)}{N}\right),
\quad \gamma_1(N)=\tfrac12\log N+\log(2\sqrt\pi),\quad
\gamma_k(N)=\tfrac12\log\frac{k+1}{k-1}\ (k\ge2).
\]
Thus the first three persistent radii are \(c_1=1/4\), \(c_2=16/27\), and \(c_3=729/1024\). More precisely, the \(N\)-th powers of the radii obey \(R_{N,1}^{N}\sim2\sqrt{\pi N}\,4^{-N}\) and \(R_{N,k}^{N}\sim\sqrt{(k+1)/(k-1)}\,c_k^N\) for fixed \(k\ge2\).

## Assumptions and scope
All results concern the canonical uniform measure on the \(N\)-th roots of unity and derivative order exactly \(N-1\) of its Cauchy transform, equivalent up to a nonzero factor to the displayed \(N\)-th power-pole sum. The limit is \(N\to\infty\) with the ring index \(k\) fixed. No uniformity in growing \(k\) is claimed. The rational function is considered off its poles \(U_N\).

## Proof
**Exact reduction.** For \(|z|<1\), expand each pole as a power series, use roots-of-unity orthogonality, and obtain
\[
F_N(z)=(-1)^N N\sum_{j\ge0}\binom{(j+1)N-1}{N-1}z^{jN}=(-1)^NN\frac{P_N(z^N)}{(1-z^N)^N},
\]
where
\[
P_N(w)=\sum_{j=0}^{N-1}a_{N,j}w^j,\qquad
 a_{N,j}=[t^{Nj}](1+t+\cdots+t^{N-1})^N
=\sum_{h=0}^j(-1)^h\binom Nh\binom{(j-h+1)N-1}{N-1}.
\]
The last equality follows by expanding \((1-t^N)^N/(1-t)^N\); rational continuation proves the identity away from the poles. Complementing every exponent in the coefficient extraction shows \(a_{N,j}=a_{N,N-1-j}\), so \(P_N\) is monic reciprocal.

**Simple negative roots.** For \(1\le m\le N\), introduce \(P_{N,m}\) by
\[
\sum_{\zeta\in U_N}(z-\zeta)^{-m}=(-1)^mNz^{N-m}P_{N,m}(z^N)/(1-z^N)^m.
\]
Direct differentiation gives the polynomial recurrence
\[
mP_{N,m+1}(w)=((N-m)(1-w)+mNw)P_{N,m}(w)+Nw(1-w)P'_{N,m}(w),\quad P_{N,1}=1.
\]
For \(m<N\), the leading coefficient of \(P_{N,m}\) is \(1\) and its constant is \(\binom{N-1}{m-1}>0\). Assume \(P_{N,m}\) has \(m-1\) simple negative roots. At every such root \(r\), the sign of \(P_{N,m+1}(r)\) is opposite to the sign of \(P'_{N,m}(r)\) because \(Nr(1-r)<0\). The signs alternate on consecutive roots; positivity at \(0\) provides one additional root between the rightmost root and zero. The polynomial \(P_{N,m+1}\) has degree \(m\), and the sign at \(-\infty\) supplies one root to the left of the leftmost root. Hence all \(m\) roots are real, negative, distinct; induction completes the proof. In the base step \(m=1\), the recurrence directly gives \(P_{N,2}(w)=(N-1)+w\). Since the negative roots never equal \(1\), substitution \(w=z^N\) gives \(N(N-1)\) simple zeros in regular polygons. Reciprocity pairs roots by inversion, with one root at \(-1\) exactly when \(N\) is even.

**Dominant coefficients.** For every fixed \(j\ge1\), the inclusion-exclusion expression and Stirling's formula give
\[
a_{N,j}\sim\frac{\beta_j^N}{\sqrt{2\pi j(j+1)N}},
\]
while \(a_{N,0}=1\). Indeed, the \(h=0\) term has that asymptotic. For \(h\ge1\), the ratio of each shifted binomial term to the \(h=0\) term is exponentially small (the \(N\)-power factors \(\binom Nh\) are only polynomial for fixed \(h\)); there are finitely many \(h\le j\). The sequence \(\log\beta_j\) is strictly concave: it equals the discrete increment of the strictly concave function \(x\mapsto x\log x\) after differentiating its second finite increment, or directly by differentiating \(\log c_j\). Thus \(c_1<c_2<\cdots<1\).

**Isolation of fixed-index roots.** Fix \(k\) and choose \(c_k<\rho<c_{k+1}\). On the circle \(|w|=\rho^N\), the \(j=k\) monomial \(a_{N,k}w^k\) has strictly greater exponential rate than all other fixed \(j\), because \(j\mapsto\log\beta_j+j\log\rho\) is uniquely maximized at \(k\). The remaining high-degree tail is uniformly negligible: \(a_{N,j}\le\binom{(j+1)N-1}{N-1}\le (e(j+1))^N\), and for sufficiently large fixed \(J\), the sum over \(j\ge J\) is bounded by a rapidly decaying geometric-exponential tail since \(\rho<1\) and \(j+1\le N\); equivalently, the uniform entropy bound for the unrestricted binomial shows the rate \(\log\beta_j+j\log\rho\to-\infty\). Rouché's theorem gives exactly \(k\) zeros in \(|w|<\rho^N\). Comparing circles on both sides of \(c_k\) proves \(R_{N,k}\to c_k\).

**Sharp prefactors.** Set \(\tau_{N,k}=a_{N,k-1}/a_{N,k}\). On \(w=-\tau_{N,k}u\), in a fixed neighborhood of \(u=1\), dividing \(P_N\) by \(a_{N,k-1}(-\tau_{N,k})^{k-1}\) gives the uniform limit \(u^{k-1}(1-u)\); every other monomial is exponentially smaller by strict rate separation and the same uniform tail estimate. Hurwitz's theorem, or Rouché on a small circle about \(u=1\), gives one simple negative root \(w=-\tau_{N,k}(1+o(1))\). The isolation above identifies it with the \(k\)-th smallest modulus. Finally Stirling implies
\[
\tau_{N,1}\sim2\sqrt{\pi N}\,4^{-N},\qquad
\tau_{N,k}\sim\sqrt{\frac{k+1}{k-1}}c_k^N\quad(k\ge2),
\]
which proves all assertions after taking \(N\)-th roots.

## Verification
The standalone standard-library checker verifies the coefficient extraction against inclusion-exclusion and reciprocity exactly for \(3\le N\le15\), and evaluates 12 high-precision, strictly bracketed negative roots for \(N=24,32,48,64\) and \(k=1,2,3\). The printed radii converge to the predicted constants; convergence is slower for larger fixed \(k\). These numerical tests are not used to establish the all-\(N\) theorem.

## Relationship to prior work
The numerator \(P_N\) is the Veronese numerator (equivalently the Ehrhart \(h^*\)-polynomial of an \(N\)-dilated standard simplex), so its real-rootedness and basic reciprocal symmetry should **not** be regarded as new. Brenti--Welker and Jochemko study Veronese polynomials and establish real-rootedness and fixed-dimension large-dilation limits. The present claim isolates the different coupled scaling in which both Veronese parameter and polynomial order grow together, obtaining fixed-rank exponential root locations with sharp prefactors and their geometric interpretation as complex Cauchy-jet zero rings. Mallet--Waldspurger motivates the importance of Cauchy-type analytic transform zeros but studies a different wavelet setting. Durán's asymptotics concern ordinary Eulerian polynomial zeros, not this coupled Veronese family.

## Limitations
Novelty is conditional on the available published-literature comparisons. An older general asymptotic theorem for diagonally scaled Veronese/Euler--Frobenius polynomials may imply the root-rate conclusion under a different name; specialist historical review remains warranted. The proof does not give a uniform theory when \(k\) grows with \(N\), nor boundary-layer behavior of the outermost roots. The proof assumes the pole order equals the polygon size; it does not classify arbitrary orders or perturbed atomic weights. No independent mathematical audit has been performed.

## References
- F. Brenti and V. Welker, *The Veronese Construction for Formal Power Series and Graded Algebras* (2007), https://arxiv.org/abs/0712.2645 .
- K. Jochemko, *On the real-rootedness of the Veronese construction for rational formal power series* (2016), https://arxiv.org/abs/1602.09139 .
- S. Mallat and I. Waldspurger, *Phase retrieval for the Cauchy wavelet transform* (2014), https://arxiv.org/abs/1404.1183 .
- A. J. Durán, *Asymptotic for the rightmost zeros of Bell and Eulerian polynomials* (2024), https://arxiv.org/abs/2404.03249 .
