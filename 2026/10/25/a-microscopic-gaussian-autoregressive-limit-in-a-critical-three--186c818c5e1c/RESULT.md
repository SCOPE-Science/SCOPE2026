# A microscopic Gaussian autoregressive limit in a critical three-allele mutant-family Q-process

## Finding
Fix a mutation probability \(r\in(0,1)\). In the three-allele critical neutral-mutation model described below, let \(N_{n,i}\) be the number of allele-\(i\) mutant families in mutant generation \(n\), under the critical size-biased Q-process. Set \(S_n=N_{n,1}+N_{n,2}+N_{n,3}\) and \(D_n=N_{n,1}-N_{n,2}\).

**Theorem (microscopic-window limit).** For every fixed integer \(m\ge0\), as \(n\to\infty\),
\[
\left(\frac{S_n}{n},\frac{D_n}{\sqrt{S_n}},\frac{D_{n+1}}{\sqrt{S_{n+1}}},\ldots,\frac{D_{n+m}}{\sqrt{S_{n+m}}}\right)
\ \Longrightarrow\ (W,Z_0,Z_1,\ldots,Z_m),
\]
where \(W\) and the centered stationary Gaussian process \((Z_j)_{j\ge0}\) are independent, \(W\sim\operatorname{Gamma}(2,\text{scale}=1/(2r))\), and
\[
\operatorname{Cov}(Z_i,Z_j)=\frac{2(1+3r)}{9r}\left(-\frac12\right)^{|i-j|}.
\]
Equivalently, the Gaussian process obeys \(Z_{j+1}=-Z_j/2+\eta_{j+1}\), with independent centered normal innovations of variance \((1+3r)/(6r)\), independent of its stationary initial state. In particular, every fixed nonzero time-lag correlation is \((-1/2)^h\), irrespective of \(r\).

An equivalent unstudentized joint limit is
\[
\left(\frac{S_n}{n},\frac{D_n}{\sqrt n},\ldots,\frac{D_{n+m}}{\sqrt n}\right)
\Longrightarrow (W,\sqrt W Z_0,\ldots,\sqrt W Z_m).
\]
Neither the single-time Gaussian shape alone nor the macroscopic population growth is claimed as new; the result concerns their *joint finite-generation time window*, including the explicit oscillatory dependence and asymptotic independence from population scale.

## Assumptions and scope
Every individual produces \(\operatorname{Poi}(1)\) children independently; each child is a clone with probability \(1-r\), or a mutant with probability \(r\). Clones inherit their mother's allele. Each mutant independently receives one of the **two alleles different from its mother's** with probability \(1/2\) each. Collapse each clone-family into one vertex and connect it to all mutant children produced anywhere in that clone-family. The resulting mutant-family generations form a three-type Galton–Watson process. Start from a single allele-\(1\) family.

Let \(M\) be the total number of mutant children produced by one complete clone-family. The clone descendants form a subcritical Poisson Galton–Watson tree because \(1-r<1\). Hence \(M\) is finite almost surely and has finite moments of every order. Its probability generating function \(F(s)\) satisfies
\[
F(s)=\exp\big((1-r)(F(s)-1)+r(s-1)\big).
\]
The mutant-type matrix is
\[
P=\begin{pmatrix}0&1/2&1/2\\1/2&0&1/2\\1/2&1/2&0\end{pmatrix}.
\]
The mean matrix is \(P\): it is irreducible, aperiodic, and has Perron eigenvalue one, with right eigenvector \((1,1,1)\). The critical Q-process on nonzero population vectors is the Doob transform with harmonic function \(h(N)=S\). For a transition from \(N\) to \(N'\) it assigns the original probability multiplied by \(S'/S\). Thus \(S_n>0\) at every generation under this law. The result does **not** assert an unconditioned or finite-horizon-survival-conditioned microscopic limit.

## Proof
**1. Family offspring moments.** Differentiating the displayed equation for \(F\) at \(s=1\) gives \(\mathbb E M=1\) and \(\mathbb E[M(M-1)]=1/r\), hence
\[
v:=\operatorname{Var}(M)=\frac1r.
\]
The subcritical clone-tree construction and its exponential-moment generating function imply finite third moments. Equivalently, conditioned on \(M\), all mutant daughter types are independent according to the relevant row of \(P\).

**2. The size-biased Q transition and population scale.** The identity \(\mathbb E[S'\mid N]=S\) makes \(h(N)=S\) harmonic. In a Q-transition, one of the \(S\) parent families is chosen uniformly and given the size-biased law \(\Pr(M^*=k)=k\Pr(M=k)\); all other parents reproduce with the ordinary \(M\)-law. Daughter-type choices retain their conditional probabilities. Consequently the total-size chain depends on the current state only through \(S\), and
\[
\mathbb E^\uparrow[S_{n+1}\mid S_n]=S_n+v,\qquad
\operatorname{Var}^\uparrow(S_{n+1}\mid S_n)=vS_n+O_r(1).
\]
For completeness, the standard critical finite-variance Q-process population limit can be recovered directly from \(F\). With \(F_k\) denoting the \(k\)-fold iterate of \(F\),
\[
\mathbb E^\uparrow[e^{-tS_n/n}]=e^{-t/n}F_n'(e^{-t/n})
\longrightarrow\big(1+vt/2\big)^{-2}\quad(t\ge0).
\]
Indeed \(F(1-y)=1-y+vy^2/2+O_r(y^3)\) implies \(n(1-F_n(e^{-t/n}))\to t/(1+vt/2)\); differentiating the iterated generating-function recurrence yields the indicated derivative limit (uniformly for \(t\) in compact positive intervals, then at zero). Thus \(S_n/n\Rightarrow W\) with Gamma shape two and scale \(v/2=1/(2r)\); in particular \(\Pr(W=0)=0\), and \(\mathbb E^\uparrow S_n=1+vn\).

**3. Contracting allele contrasts.** For \(a=(1,-1,0)\), write \(H_n=a\cdot N_n=D_n\). Since \(Pa=-a/2\), the ordinary one-step conditional mean of \(H_{n+1}\) is \(-H_n/2\). Write \(H_i\) for the signed offspring contribution of one parent of allele \(i\). Its covariance with its total number of mutant children is \(v(Pa)_i=-va_i/2\). Multiplying the original offspring law by total daughters \(S'/S\) therefore gives the **exact** Q-transition identity
\[
\mathbb E^\uparrow[D_{n+1}\mid N_n]
=-\frac12\left(1+\frac v{S_n}\right)D_n.\tag{1}
\]
Under the ordinary transition, the three parent-specific signed offspring variances are respectively
\[
q_1=q_2=\frac{v+1}{4},\qquad q_3=1.
\]
The single size-biased family changes the Q-conditional variance relative to the ordinary sum by a quantity uniformly bounded in \(N\): expanding \(\mathbb E[S'(H_{n+1}-\mathbb EH_{n+1})^2]/S\), independence cancels all terms except parentwise third mixed centered moments divided by \(S\), and the squared mean adjustment is bounded by \(v^2/4\). Hence
\[
\operatorname{Var}^\uparrow(D_{n+1}\mid N_n)
=q_1(N_{n,1}+N_{n,2})+q_3N_{n,3}+O_r(1).\tag{2}
\]
The same contraction (1) holds for the second contrast \((1,1,-2)\), and its conditional variance is bounded by \(C_rS_n+C_r\). Choose \(S_0\) large enough that \((1+v/S_0)^2/4<1\). On \(S_n\ge S_0\), the squared conditional mean contracts; on the complementary event every contrast is bounded by a constant depending on \(S_0\). Using \(\mathbb ES_n=1+vn\), the variance bound, and a geometric recursion proves
\[
\mathbb E^\uparrow D_n^2=O_r(n),\qquad
\mathbb E^\uparrow(N_{n,1}+N_{n,2}-2N_{n,3})^2=O_r(n).
\]
In particular \(N_{n,i}/S_n\to1/3\) in probability for all three \(i\), since \(S_n/n\Rightarrow W>0\).

**4. Gaussian innovations on a fixed window.** Set \(\lambda=-1/2\) and \(\varepsilon_{k+1}=D_{k+1}-\mathbb E^\uparrow[D_{k+1}\mid N_k]\). By (2) and the preceding type proportions,
\[
\frac{\operatorname{Var}^\uparrow(\varepsilon_{k+1}\mid N_k)}{S_k}
\longrightarrow\beta:=\frac{v+3}{6}=\frac{1+3r}{6r}
\quad\text{in probability}.
\]
Fix any finite number \(K\) of generations around time \(n\). Because total-size increments have conditional mean \(v\) and variance \(vS+O_r(1)\), \(S_{n+j}/n-S_n/n\to0\) in probability for each fixed integer \(j\). The conditional Lindeberg condition follows from finite third offspring moments: the ordinary sum contains \(S_{n+j}\to\infty\) independent parent contributions with uniformly bounded third absolute moments, while the one size-biased parent's contribution is \(o_{\Pr}(\sqrt n)\). Iterated conditional characteristic functions now show that the \(K\) recent innovations divided by \(\sqrt n\), **jointly with** \(S_n/n\), converge to \(K\) conditionally independent centered Gaussians of common conditional variance \(\beta W\). Equivalently they converge to \(\sqrt W\) times independent \(N(0,\beta)\) variables which are independent of \(W\).

**5. Forgetting the remote past and studentization.** From (1),
\[
D_{k+1}=\lambda D_k+\varepsilon_{k+1}+\lambda vD_k/S_k.
\]
The final term has absolute value at most \(v/2\). Iterating backward \(K\) steps leaves an error of at most \(v\), plus \(\lambda^K D_{n-K}\). The latter, divided by \(\sqrt n\), has second moment \(O_r(4^{-K})\) by Step 3. First let \(n\to\infty\) at fixed \(K\), then \(K\to\infty\). The limiting weighted innovation series is the centered stationary Gaussian autoregression with innovation variance \(\beta\), autoregressive coefficient \(\lambda\), and covariance
\[
\frac{\beta}{1-\lambda^2}\lambda^{|i-j|}
=\frac{2(v+3)}9\left(-\frac12\right)^{|i-j|}.
\]
The same argument works simultaneously for \(D_n,\ldots,D_{n+m}\). Finally \(S_{n+j}/n\Rightarrow W\) jointly over each fixed window with a common \(W>0\). Division by \(\sqrt{S_{n+j}/n}\) yields the studentized joint limit, independent of \(W\). This proves the theorem.

## Verification
The companion `verify.py` uses exact rational arithmetic to check the mutation-matrix eigenrelations, clone-family moment recursions, all displayed variance constants, and finite-population Q-transform mean identities for a moment-matched auxiliary offspring law. Its output is included in `verification_output.txt`. These finite checks do not prove the limiting theorem; the mathematical proof above supplies its infinite-generation argument.

## Relationship to prior work
Blancas, Fittipaldi and Hernández-Torres (2026, arXiv:2610.20896v1) formulate mother-dependent mutant chains and their Q-processes and provide spine constructions, but the inspected material does not identify the present microscopic-time covariance law. Baake, Cordero, Mellis and Wachtel (2025, arXiv:2504.21714v1, Theorem 3.1) prove a **macroscopic** time-functional limit for the linearly scaled critical Q-process; its limit lies on the Perron ray and erases the \(\sqrt n\)-scale transverse fluctuations studied here. Fleischmann and Vatutin (1998 preprint, 2001 journal article) and Athreya and Ney (1974) address **single-time** transverse Gaussian or Gaussian-mixture deviations under nonextinction, and so the one-time marginal alone is not novel. The claimed new component is the explicit *joint consecutive-generation* Gaussian autoregression under the Q law, including its universal signed lag correlations and independence from the random population scale.

## Limitations
The theorem requires the stated Poisson parent reproduction, all three alleles, equal switching to the other two alleles, and fixed \(r\in(0,1)\). It does not claim a simultaneous growing-length observation window, uniformity as \(r\downarrow0\), path-space convergence on accelerated time, or a Q-to-finite-horizon conditioned transfer at the fine fluctuation scale. The available inspection of the 2026 motivating preprint was incomplete; priority under broader older fluctuation terminology still deserves independent review. No independent validation has been performed.

## References
1. A. Blancas, M. C. Fittipaldi and S. Hernández-Torres, *The Q-process for the general mother-dependent multitype branching process*, arXiv:2610.20896v1 (first public 2026-10-14), https://arxiv.org/abs/2610.20896.
2. E. Baake, F. Cordero, S.-M. Mellis and V. Wachtel, *Critical multitype branching: a functional limit theorem and ancestral processes*, arXiv:2504.21714v1 (2025), https://arxiv.org/abs/2504.21714.
3. K. Fleischmann and V. A. Vatutin, *Deviations from typical type proportions in critical multitype Galton–Watson processes*, WIAS Preprint 455 (1998); Theory of Probability and Its Applications 45 (2001), 23–40, https://webdoc.sub.gwdg.de/ebook/serien/e/wias/1998/1998/wias_preprints_455.pdf.
4. K. B. Athreya and P. Ney, *Functionals of critical multitype branching processes*, Annals of Probability 2 (1974), 339–343, https://doi.org/10.1214/aop/1176996716.
