# A fourth-moment contamination frontier and a sharp five-node robustness cost for Gaussian-mixture quadrature

## Finding
Let \(L>1\), \(0<\varepsilon_L<1\), and define the centered Gaussian variance mixture
\[
\mu_L=(1-\varepsilon_L)\,\mathcal N(0,1)+\varepsilon_L\,\mathcal N(0,L^2).
\]
Denote by \(G_L\) its unique three-node Gaussian quadrature, exact on every polynomial of degree at most five. Put
\[
m_2=1+\varepsilon_L(L^2-1),\qquad
m_4=3[1+\varepsilon_L(L^4-1)].
\]
Its nodes are \(0,\pm a_L\), where \(a_L^2=m_4/m_2\), with center weight \(w_0=1-m_2^2/m_4\) and each outer weight \(w_\pm=m_2^2/(2m_4)\). All three weights are strictly positive.

**Complete weak-limit classification.** Assume \(L\to\infty\) and \(\varepsilon_L\to0\), and write \(\theta_L=\varepsilon_L L^4\). If \(\theta_L\to c<\infty\), \(G_L\) converges weakly to the three-atom probability measure
\[
G_c=\left(1-\frac{1}{3(1+c)}\right)\delta_0+
\frac{1}{6(1+c)}\left(\delta_{-\sqrt{3(1+c)}}+\delta_{\sqrt{3(1+c)}}\right).
\]
If \(\theta_L\to\infty\), then \(G_L\Rightarrow\delta_0\). In particular, \(G_L\Rightarrow G_0\), the standard-normal three-node Gauss-Hermite law, **if and only if** \(\varepsilon_L L^4\to0\). The fourth-moment scale, rather than the variance scale, is the exact transition for weak stability of this moment-fitted quadrature.

**Sharp positive-node cost.** Whenever \(\varepsilon_L\to0\) and \(\varepsilon_L L^4\to\infty\), there is no sequence of positive quadrature rules with at most four nodes, all exactly integrating degrees zero through five for \(\mu_L\), which converges weakly to \(G_0\). Conversely, the positive rule
\[
C_L=\frac23\delta_0+
\frac{1-\varepsilon_L}{6}(\delta_{-\sqrt3}+\delta_{\sqrt3})+
\frac{\varepsilon_L}{6}(\delta_{-L\sqrt3}+\delta_{L\sqrt3})
\]
has exactly five distinct nodes, integrates every polynomial through degree five, and satisfies \(C_L\Rightarrow G_0\) whenever \(\varepsilon_L\to0\). Therefore five is the **smallest possible** positive node count for this precise notion of weak stability while retaining degree-five exactness in the diverging-fourth-moment regime.

As a concrete loss of bounded-test accuracy, for \(\varepsilon_L=L^{-3}\),
\[
\mu_L\Rightarrow\mathcal N(0,1),\quad G_L\Rightarrow\delta_0,\quad
G_L(e^{-x^2})\longrightarrow 1,\quad
\int e^{-x^2}\,d\mu_L\longrightarrow 1/\sqrt3.
\]
Thus the quadrature error on a smooth bounded nonnegative integrand tends to \(1-1/\sqrt3\), even though the underlying mixture approaches the normal law in total variation at a rate at most \(L^{-3}\).

## Assumptions and scope
The integrands are real functions for which the expressions exist; the exactness and lower-bound assertions refer to all real polynomials of degree at most five. A positive \(K\)-node rule is a probability measure supported on at most \(K\) real points with nonnegative weights, exactly matching these moments. Coincident nodes may be consolidated. Weak convergence is against bounded continuous real test functions. The large-\(L\) statements assume both \(L\to\infty\) and \(\varepsilon_L\to0\), with no unstated relation between their rates. The node-minimum statement compares convergence specifically to the **uncontaminated three-node Gauss-Hermite rule** \(G_0\), not convergence to the continuous normal distribution itself.

## Proof
**1. Explicit uniqueness and positivity.** The mixture is symmetric, so odd moments one, three, and five vanish. Its second and fourth moments are precisely \(m_2,m_4\). The monic polynomial \(P_3(x)=x^3-(m_4/m_2)x\) is orthogonal to \(1,x,x^2\): parity covers the even degrees and the inner product with \(x\) is \(m_4-(m_4/m_2)m_2=0\). Its distinct zeros \(0,\pm\sqrt{m_4/m_2}\) are the unique Gaussian quadrature nodes. By symmetry and degree-four exactness, the only possible weights are \(w_\pm=m_2^2/(2m_4)\) and \(w_0=1-2w_\pm\). This directly matches all moments through degree five. Writing \(V\) for the random Gaussian-component variance, \(m_2=\mathbb E[V]\) and \(m_4=3\mathbb E[V^2]\), hence \(m_4\ge3m_2^2\). Therefore \(w_0\ge2/3\) and \(w_\pm>0\).

**2. Sharp weak limits.** If \(\theta_L=\varepsilon_L L^4\to c<\infty\), then \(\varepsilon_L L^2=\theta_L/L^2\to0\), so \(m_2\to1\), \(m_4\to3(1+c)\), and substitution into the node and weight formula gives \(G_c\). If \(\theta_L\to\infty\), then \(m_4\to\infty\), while
\[
0\le\frac{m_2^2}{m_4}
\le \frac{(1+\varepsilon_L L^2)^2}{3\varepsilon_L L^4}
=\frac{1}{3\varepsilon_L L^4}+\frac{2}{3L^2}+\frac{\varepsilon_L}{3}\to0.
\]
It follows that the total weight on the two outer nodes tends to zero, so \(G_L\Rightarrow\delta_0\), irrespective of their locations. The only way for \(G_L\Rightarrow G_0\) is \(\theta_L\to0\): otherwise a subsequence has \(\theta_L\) bounded away from zero and a further subsequence converges to either \(c>0\) or infinity. The corresponding \(G_c\) or \(\delta_0\) is not \(G_0\).

**3. Four nodes cannot be weakly stable when the fourth moment diverges.** Suppose a sequence of positive degree-five-exact rules with at most four nodes converges weakly to \(G_0\), which has positive mass at each of the three separated points \(-\sqrt3,0,\sqrt3\). Fix three small disjoint bounded open intervals around these points with boundaries of \(G_0\)-mass zero. For all sufficiently large \(L\), each interval must contain at least one node, leaving at most one additional node. Choose one node in each interval as the bounded core. If no additional node exists, all fourth moments are bounded, contrary to \(m_4\to\infty\). If the extra node is bounded along a subsequence, the same contradiction holds. Consequently it must escape in absolute value along any unbounded-moment subsequence: write its location \(z_L\), with \(|z_L|\to\infty\), and weight \(v_L\ge0\). Exactness of the **fifth** moment, which is zero, gives \(v_Lz_L^5=-\sum_{\mathrm{core}}w_i x_i^5\), a uniformly bounded quantity because core locations are bounded and positive weights sum to one. Hence \(v_Lz_L^4=O(1/|z_L|)\to0\). The core contributes a bounded fourth moment, contradicting \(m_4\to\infty\). Thus at least five nodes are necessary. No symmetry assumption on competing rules was used.

**4. Five-node attainment.** The displayed \(C_L\) has strictly positive weights and distinct nodes for \(L>1\). Its center mass is \(2/3\), and its two symmetric node-pairs carry masses \((1-\varepsilon_L)/6\) and \(\varepsilon_L/6\) at each end. Its total mass is one; odd moments to degree five cancel; its second and fourth moments are \(m_2,m_4\). It is therefore degree-five exact. The two extreme nodes have total mass \(\varepsilon_L/3\to0\), the inner-pair weights converge to \(1/6\), and the center weight remains \(2/3\), proving \(C_L\Rightarrow G_0\).

**5. Bounded-integrand witness.** Since \(\mu_L\) is the stated mixture, its total-variation distance to \(\mathcal N(0,1)\) is at most \(\varepsilon_L\). With \(\varepsilon_L=L^{-3}\), the large-fourth-moment case applies, so \(G_L(e^{-x^2})\to1\). Direct normal integration gives
\[
\int e^{-x^2}\,d\mu_L=
\frac{1-\varepsilon_L}{\sqrt3}+
\frac{\varepsilon_L}{\sqrt{1+2L^2}}\longrightarrow\frac1{\sqrt3}.
\]
This proves the stated nonzero limiting error.

## Verification
The supplied standard-library Python script `verify.py` checks 60 positive parameter pairs using exact rational arithmetic for the degree-five moment identities of both the three-node and componentwise five-node rules. It also evaluates a bounded-integrand witness for four large variance ratios and checks three predicted limits. The run produced: `PASS: 60 exact parameter checks, four bounded-integrand comparisons, three asymptotic checks`. The proofs of the node-minimum and all-rate limit statements above are analytic; finite tests are neither substituted for nor interpreted as exhaustive proofs.

## Relationship to prior work
Kabaila's 2026 tutorial introduces custom Gaussian quadrature through moment determinants and the Stieltjes procedure. Pinkse's 2026 positive-weight Gauss-Hermite construction focuses on node budgets and exactness for standard Gaussian weights, rather than rare high-variance contamination. Shim's 2026 Gaussian-mixture entropy study motivates integration under mixture distributions. The present statement concerns a different comparison: **direct global moment-fitted three-node quadrature versus componentwise degree-five quadrature**, with a complete contamination-scale weak-limit law and a proven minimal positive node count for maintaining the uncontaminated quadrature limit. Classical formulas for three-point Gaussian quadrature and componentwise integration are not claimed as new in themselves. An equivalent treatment in older orthogonal-polynomial perturbation or quadrature-of-moments literature remains a priority risk.

## Limitations
The limiting stability target is the standard-normal *three-node rule*, not exact Gaussian integration for every continuous function; the five-node rule still has finite quadrature error on generic non-polynomials. The lower bound is for nonnegative-weight rules exact through degree five and for a three-atom target; it does not address signed weights, approximate moment matching, adaptive evaluation cost, multivariate mixtures or higher quadrature degrees. The classification does not imply that all moment-fitted Gauss quadrature schemes fail under all contaminations. Existing literature may contain equivalent results; priority has not been independently established.

## References
1. P. Kabaila, *Custom-made Gauss quadrature: an introduction for statisticians*, arXiv:2607.14511, first posted July 16, 2026. https://arxiv.org/abs/2607.14511
2. J. W. Shim, *Gauss--Hermite Quadrature for Gaussian-Mixture Entropy with an Action-Space Hermite Surrogate*, arXiv:2608.21467, first posted August 21, 2026. https://arxiv.org/abs/2608.21467
3. J. Pinkse, *Positive weight Hermite and Legendre quadrature rules*, arXiv:2609.26840, first posted September 2026. https://econbase.org/papers/text/2609.26840.html
