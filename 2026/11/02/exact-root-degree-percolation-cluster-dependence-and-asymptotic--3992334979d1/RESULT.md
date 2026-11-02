# Exact root-degree–percolation-cluster dependence and asymptotic decoupling in recursive trees

## Finding

Fix a real retention parameter \(0<p<1\). Grow a uniform random recursive tree \(T_n\) on vertices \(1,\ldots,n\): each vertex \(j\ge2\) independently chooses its parent uniformly from \(1,\ldots,j-1\). Independently retain each new edge with probability \(p\). Let \(R_n\) be the number of vertices in the retained-edge component of root \(1\), and let \(K_n\) be the number of children of root \(1\) **in the original, unpercolated tree**. Set

\[
 a_n=\prod_{j=1}^{n-1}\left(1+\frac pj\right)
 =\frac{\Gamma(n+p)}{\Gamma(1+p)\Gamma(n)},\qquad
 H_{n-1}=\sum_{j=1}^{n-1}\frac1j.
\]

**Theorem.** For every integer \(n\ge1\), the following identity describes the complete joint generating polynomial:

\[
 \boxed{\sum_{n\ge1}\mathbb E[u^{R_n}z^{K_n}]x^{n-1}
 =u(1-x)^{-z(1-p)}\bigl(1-u+u(1-x)^p\bigr)^{-z}.}
\]

All coefficient identities are formal at \(x=0\), with real parameters \(u,z\), and the displayed series is valid analytically for sufficiently small \(|x|\). Moreover,

\[
 \boxed{\operatorname{Cov}(R_n,K_n)
 =a_n\left[1-\sum_{j=1}^{n-1}\left(\frac1j-\frac1{j+p}\right)\right]-1.}
\]

In particular, the covariance is strictly positive for \(n\ge3\), while it vanishes for \(n=1,2\). Define

\[
 c_p=1-\sum_{j=1}^{\infty}\left(\frac1j-\frac1{j+p}\right)
 =1-\gamma-\psi(1+p)>0,
\]

where \(\psi\) is the logarithmic derivative of the gamma function and \(\gamma\) is Euler's constant. Then

\[
 \boxed{\operatorname{Cov}(R_n,K_n)\sim
 \frac{c_p}{\Gamma(1+p)}n^p.}
\]

Nevertheless, a Gaussian fluctuation of the original root degree is asymptotically independent of the percolated root-cluster limit:

\[
 \boxed{\left(\frac{R_n}{n^p},\frac{K_n-H_{n-1}}{\sqrt{\log n}}\right)
 \xrightarrow{d}(W_p,Z),\qquad W_p\perp Z,\quad Z\sim N(0,1).}
\]

Here \(W_p\) is the known Mittag–Leffler limit of the root-cluster size, with \(\mathbb E[W_p^r]=r!/\Gamma(1+rp)\) for positive integers \(r\). The exact positive covariance and the independent joint limit refer to different normalizations, so they are compatible.

## Assumptions and scope

The parent choices are mutually independent uniform choices, the edge-retention indicators are mutually independent Bernoulli variables of fixed parameter \(p\), and the two families are independent. The degree \(K_n\) counts **all** original children of root \(1\), including children joined by deleted edges. The size \(R_n\) counts only the retained-edge connected component containing the root. Statements concerning finite \(n\) hold for every integer \(n\ge1\); the strict covariance statement requires \(n\ge3\); the limit statements require fixed \(0<p<1\) and \(n\to\infty\). At boundary \(p=0\), \(R_n=1\); at \(p=1\), \(R_n=n\), so the covariance is zero at either boundary. The positive asymptotic coefficient is not asserted uniformly as \(p\downarrow0\) or \(p\uparrow1\).

## Proof

**1. Complete finite joint transform.** Let

\[
 F(x;u,z)=\sum_{n\ge1}\frac{x^n}{n}\mathbb E[u^{R_n}z^{K_n}],
 \qquad B(x)=-\log(1-x).
\]

There are \((n-1)!\) increasing rooted trees of order \(n\), explaining the weight \(1/n\) in this exponential generating function. A root contributes \(u\). Its children form an unordered set of independently weighted increasing subtrees. Each root child contributes \(z\); if its incident edge is deleted (probability \(1-p\)), its subtree contributes \(B(x)\), while if the edge is retained (probability \(p\)), the subtree contributes the cluster-marked marginal \(F(x;u,1)\). Therefore the standard increasing-tree root decomposition yields

\[
 \partial_xF(x;u,z)
 =u\exp\bigl(z[(1-p)B(x)+pF(x;u,1)]\bigr),
 \qquad F(0;u,z)=0.
\]

For \(z=1\), writing \(G=F(x;u,1)\) gives

\[
 \partial_xG=u(1-x)^{p-1}\exp(pG).
\]

Hence \(\partial_x\exp(-pG)=-pu(1-x)^{p-1}\) and, by the initial condition,

\[
 \exp(-pG)=1-u+u(1-x)^p.
\]

Substitution in the differential identity yields

\[
 \partial_xF(x;u,z)=u(1-x)^{-z(1-p)}
 (1-u+u(1-x)^p)^{-z}.
\]

By the definition of \(F\), its derivative is exactly the generating series asserted in the theorem. Setting \(u=1\) gives the independent-root-attachment law \(\mathbb E[z^{K_n}]=(z)_{n-1}/(n-1)!\); setting \(z=1\) recovers the published marginal root-cluster generating function.

**2. Exact covariance.** Let \(\mathcal F_n\) contain all parent choices and retained-edge decisions through time \(n\). Write \(A_{n+1}\) for the indicator that vertex \(n+1\) chooses root \(1\), and \(D_{n+1}=R_{n+1}-R_n\). Then

\[
 \mathbb E[A_{n+1}\mid\mathcal F_n]=\frac1n,
 \quad\mathbb E[D_{n+1}\mid\mathcal F_n]=\frac{pR_n}{n},
 \quad\mathbb E[A_{n+1}D_{n+1}\mid\mathcal F_n]=\frac pn.
\]

Consequently \(\mathbb E[R_n]=a_n\) and, writing \(C_n=\operatorname{Cov}(R_n,K_n)\),

\[
 C_{n+1}=\left(1+\frac pn\right)C_n
 +\frac pn-\frac{p a_n}{n^2},\quad C_1=0.
\]

Since \(a_{n+1}=a_n(1+p/n)\), division by \(a_{n+1}\) gives

\[
 \frac{C_{n+1}}{a_{n+1}}-\frac{C_n}{a_n}
 =\left(\frac1{a_n}-\frac1{a_{n+1}}\right)
 -\left(\frac1n-\frac1{n+p}\right).
\]

Sum this identity for \(n=1,\ldots,N-1\) to obtain the exact covariance formula. When \(0<p<1\), \(a_n<n\) for \(n\ge2\), so the positive additive term \(p(1-a_n/n)/n\) proves by induction that \(C_N>0\) for \(N\ge3\). Finally the summand \(1/j-1/(j+p)\) is positive and strictly increasing with \(p\); at \(p=1\) its infinite sum is exactly \(1\). It follows that \(c_p>0\) for \(0<p<1\). The convergence of the series and \(a_n\sim n^p/\Gamma(1+p)\) establish the stated asymptotic covariance.

**3. Joint asymptotic independence.** Since \(\mathbb E[R_{n+1}\mid\mathcal F_n]=(1+p/n)R_n\), the variables \(M_n=R_n/a_n\) form a nonnegative mean-one martingale. Its second moments are bounded. Indeed, with \(q_n=\mathbb E[R_n^2]\) and \(b_n=\prod_{j=1}^{n-1}(1+2p/j)\), the Bernoulli transition gives

\[
 q_{n+1}=\left(1+\frac{2p}{n}\right)q_n+\frac{p a_n}{n},\qquad
 \frac{q_{n+1}}{b_{n+1}}-\frac{q_n}{b_n}=\frac{p a_n}{n b_{n+1}}.
\]

Here \(a_n=\Theta(n^p)\) and \(b_n=\Theta(n^{2p})\), so the increments on the right are \(O(n^{-1-p})\) and summable. Thus \(\sup_n\mathbb E[M_n^2]<\infty\) and \(M_n\to M_\infty\) in \(L^2\) and almost surely. Since \(a_n/n^p\to1/\Gamma(1+p)\), it follows that \(R_n/n^p\to W_p=M_\infty/\Gamma(1+p)\) in \(L^2\). The established marginal root-cluster theorem identifies its distribution as Mittag–Leffler with the moments shown above.

Now \(K_n=\sum_{j=2}^n A_j\), where the \(A_j\) are independent Bernoulli variables of parameters \(1/(j-1)\). In particular \(\mathbb E K_n=H_{n-1}\), \(\operatorname{Var}K_n=H_{n-1}-\sum_{j=1}^{n-1}j^{-2}\sim\log n\), and the bounded-increment Lindeberg theorem gives its central limit theorem. Put \(m_n=\lfloor\exp(\sqrt{\log n})\rfloor\). Then \(m_n\to\infty\) and \(\log m_n=o(\log n)\). The centered early contribution \(K_{m_n}-H_{m_n-1}\), divided by \(\sqrt{\log n}\), converges to zero in \(L^2\). The independent late sum

\[
 \sum_{j=m_n+1}^n\left(A_j-\frac1{j-1}\right)/\sqrt{\log n}
\]

converges to a standard normal variable and is independent of \(\mathcal F_{m_n}\), hence independent of \(M_{m_n}\). Meanwhile \(M_{m_n}\to M_\infty\) in \(L^2\) and \(M_n-M_{m_n}\to0\) in \(L^2\). Applying the product characteristic-function identity for the independent pair and then Slutsky's lemma proves the stated joint convergence with independent limits.

## Verification

The standalone script `verify.py` computes exact rational transition probabilities for the joint state \((R_n,K_n)\), independently enumerates all recursive-tree parent sequences and edge-retention bit patterns through size \(6\), expands the proposed analytic bivariate generating series using rational formal power-series arithmetic, and compares covariances with the closed form. It completes 345 exact assertions across \(n=1,\ldots,9\), five rational retention parameters including both deterministic boundaries, and four generating-variable pairs. Execute `python verify.py` using Python 3; it requires only the standard library. The script supplies finite checks, not a replacement for the proofs of the all-size identities or joint limit.

## Relationship to prior work

Desmarais, Holmgren and Wagner (arXiv:2110.15050, first posted October 28, 2021; later published in *Random Structures & Algorithms*, DOI 10.1002/rsa.21142) analyze broadcast colorings and the marginal size of the root percolation cluster. Their Section 4 derives the two-variable generating function in \(x,u\) without marking the original root degree. Existing root-cluster work also establishes the marginal Mittag–Leffler limit; those facts are not claimed as new. The present claim adds the **original-root-degree joint mark**, a positive closed finite covariance and its asymptotic constant, and joint convergence with an independent Gaussian degree fluctuation. The separate marginal laws do not determine this joint dependence. Kürsten (2016, arXiv:1512.05275), Section IV and Appendix B, computes joint distributions involving the root cluster and the **total sizes of first-generation clusters attached across deleted edges**. This latter count is not the original unpercolated root outdegree, which records every original attachment regardless of edge status. In particular, the marked probability generating function and the degree central limit stated here are not obtained from that first-generation cluster-size distribution. Published calculations of root-degree covariances with leaf count or path length concern different observables and do not imply the percolation-cluster statement.

## Limitations

The model is uniform attachment with independent constant-parameter bond percolation, not preferential attachment with general bias, size-dependent retention, or site percolation. The Gaussian independence concerns the degree on its \(\sqrt{\log n}\) scale, and does not mean finite-size stochastic independence: the finite covariance is strictly positive. The displayed covariance constant is for fixed \(p\) and is not uniform at the deterministic endpoints. Search-based historical priority remains provisional, and no independent external validation is claimed.

## References

1. C. Desmarais, C. Holmgren, S. Wagner, *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050v1 (October 28, 2021); *Random Structures & Algorithms* 63 (2023), 364–405, DOI 10.1002/rsa.21142. Relevant material: Section 2.2 and Section 4.
2. L. Addario-Berry, L. Devroye, G. Lugosi, V. Velona, *Broadcasting on random recursive trees*, *Annals of Applied Probability* 32 (2022), 497–528, DOI 10.1214/21-AAP1686. Background on broadcasting and root influence.
3. R. Kürsten, *Random recursive trees and the elephant random walk*, arXiv:1512.05275v1 (December 16, 2015), *Physical Review E* 93 (2016), 032111, DOI 10.1103/PhysRevE.93.032111. Relevant material: Section IV, Appendix B.
4. Classical Lindeberg central limit theorem and square-integrable martingale convergence theorem; used in their usual forms for independent bounded triangular arrays and \(L^2\)-bounded martingales.
