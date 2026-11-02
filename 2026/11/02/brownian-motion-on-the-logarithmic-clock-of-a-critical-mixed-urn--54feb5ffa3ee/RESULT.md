# Brownian motion on the logarithmic clock of a critical mixed urn

## Finding
For the two-colour Friedman–Pólya randomly mixed urn described below, suppose the exact critical relation
\[
4bp=\mu:=p(a+b)+(1-p)c.
\]
For each integer \(N\ge2\), define the càdlàg random process on \([0,1]\)
\[
X_N(t)=\frac{U_{\lfloor N^t\rfloor}}{\sqrt{\lfloor N^t\rfloor\log N}},\qquad U_n=Y_n^1-Y_n^2.
\]
Then \(X_N\Rightarrow\sqrt q\,B\) in the Skorokhod \(J_1\) topology on \(D([0,1])\), where \(B\) is standard Brownian motion and
\[
q=p(a-b)^2+(1-p)c^2>0.
\]
In particular, for \(0\le s\le t\le1\), the limiting covariance is \(q s\), and the limiting increments on disjoint logarithmic-time intervals are independent. The result includes the marginal critical normal law at \(t=1\) but is stronger: it resolves dependence between polynomially separated observation times.

## Assumptions and scope
Let \(Y_0^1,Y_0^2\) be any strictly positive integers, and let \(a,b,c\) be strictly positive integers and \(p\in(0,1)\). Independently at each integer step, draw a colour proportionally to its existing count and return the selected ball. Independently of that draw and all previous steps, select the Friedman rule with probability \(p\), adding \(a\) balls of the drawn colour and \(b\) of the opposite colour, or the Pólya rule with probability \(1-p\), adding \(c\) balls of the drawn colour. The total \(T_n=Y_n^1+Y_n^2\) may be random. The critical relation \(4bp=\mu\) is feasible in the stated range precisely when \(a<3b\), where it fixes \(p=c/(3b-a+c)\). No integer-valued or Gaussian approximation to the individual counts is assumed. The initial counts are fixed as \(N\to\infty\).

## Proof
Write \(\varepsilon_k=1\) for a colour-1 draw and \(-1\) for a colour-2 draw. Set \(H_k=a-b\) and \(L_k=a+b\) under the Friedman rule, and \(H_k=L_k=c\) under the Pólya rule. The pairs \((H_k,L_k)\) are independent and identically distributed, independent of the draw conditional on the urn history. Define
\[
\mu=\mathbb E L_k,\quad h=\mathbb E H_k=\mu-2bp=\mu/2,\quad q=\mathbb E H_k^2.
\]
We have \(T_n=T_0+\sum_{k=1}^nL_k\), \(U_k=U_{k-1}+H_k\varepsilon_k\), and \(\mathbb E(\varepsilon_k\mid\mathcal F_{k-1})=U_{k-1}/T_{k-1}\). Consequently
\[
\zeta_k=H_k\varepsilon_k-h\frac{U_{k-1}}{T_{k-1}}
\]
is a bounded martingale difference, with exact predictable conditional variance
\[
\mathbb E(\zeta_k^2\mid\mathcal F_{k-1})
=q-h^2\left(\frac{U_{k-1}}{T_{k-1}}\right)^2.
\]
In particular, the second-moment identity \(\mathbb E(U_k^2\mid\mathcal F_{k-1})=(1+2h/T_{k-1})U_{k-1}^2+q\) also holds.

Bounded independent additions and Hoeffding's inequality with Borel–Cantelli give \(T_n=\mu n+O(\sqrt n\log n)\) almost surely; the constant \(T_0\) is absorbed. Define \(W_k=U_k/\sqrt k\) for \(k\ge1\) and
\[
S_n=\sum_{k=1}^n\frac{\zeta_k}{\sqrt k}.
\]
For \(k\ge2\), exact algebra gives
\[
W_k-W_{k-1}=\frac{\zeta_k}{\sqrt k}+\beta_k W_{k-1},\qquad
\beta_k=\sqrt{\frac{k-1}{k}}\left(1+\frac{h}{T_{k-1}}\right)-1.
\]
Using \(h=\mu/2\), the deterministic terms of order \(1/k\) cancel: for an almost-surely finite random constant \(C\) and all sufficiently large \(k\),
\[
|\beta_k|\le C\bigl(k^{-2}+k^{-3/2}\log k\bigr).
\]
The maximal Azuma–Hoeffding inequality applied on dyadic ranges to the bounded differences \(\zeta_k/\sqrt k\), whose squared bounds sum to \(O(\log n)\), yields \(\sup_{j\le n}|S_j|=O((\log n)^2)\) almost surely. The discrete Gronwall inequality and \(\sum_k|\beta_k|<\infty\) therefore imply \(\sup_{j\le n}|W_j|=O((\log n)^2)\) almost surely. Hence
\[
\sum_{k=2}^\infty|\beta_k W_{k-1}|<\infty\quad\text{almost surely},
\]
so \(W_n-S_n\) converges almost surely to a finite random variable. In particular,
\[
\sup_{n\ge1}|W_n-S_n|<\infty\quad\text{almost surely},\qquad
\frac{U_n}{T_n}=O\left(\frac{(\log n)^2}{\sqrt n}\right)\quad\text{almost surely}.
\]
For \(N\to\infty\), consider the triangular martingale process \(S_{\lfloor N^t\rfloor}/\sqrt{\log N}\). Its largest jump has magnitude at most \(C/\sqrt{\log N}\). Its predictable bracket equals
\[
\frac1{\log N}\sum_{k\le\lfloor N^t\rfloor}
\frac{q-h^2(U_{k-1}/T_{k-1})^2}{k}.
\]
The harmonic-number approximation is uniform over \(0\le t\le1\), and the nonnegative correction tends to zero uniformly because \(U_n/T_n\to0\) almost surely (indeed the weighted correction sum is finite). Thus the bracket converges almost surely, uniformly in \(t\), to \(qt\). The bounded jumps give the conditional Lindeberg condition. The martingale functional central limit theorem now gives \(S_{\lfloor N^\cdot\rfloor}/\sqrt{\log N}\Rightarrow\sqrt q\,B\) in \(D([0,1])\) with \(J_1\). The almost-sure boundedness of \(W_n-S_n\), divided by \(\sqrt{\log N}\), transfers the result to \(X_N\), including \(t=0\). This proves the theorem.

## Verification
The accompanying `checker.py` enumerates finite histories with exact rational probabilities under four admissible critical parameter configurations. For every reachable composition through the configured depth it independently computes the one-step transition distribution and confirms normalization, the two martingale identities, the conditional bracket, and total/difference updates. Running `python3 checker.py` reproduces the archived `checker_output.txt`. This finite check does not certify the functional limit; that conclusion is proved by the martingale argument above.

## Relationship to prior work
Shi, Yin and Miao (2026), Sections 2–4, introduce this random-replacement urn, derive the stochastic-approximation recurrence and state a Gaussian central limit theorem for the **strict** parameter region \(4bp>\mu\). The equality case and its logarithmically reparametrized path law are not stated in those main results. Alves and Rosales (2025) establish convergence of the colour proportion to \(1/2\), without this path limit. Fang (2025 preprint, 2026 journal) already derives exactly the same **logarithmic-clock Brownian topology and normalization** for the untrained critical elephant random walk. Therefore the time change, topology, and Brownian shape are prior mathematics, not innovations of this theorem. That elephant walk has a fixed one-unit replacement and its critical martingale differs from a Bernoulli mixture of Friedman and Pólya additions with possibly random total size. The present claimed scope is the direct critical limit and variance parameter for that mixed model, using a summable random-total error. Classical critical-eigenvalue theories of generalized urns, including Janson, may well imply this specialization; their possible broader coverage remains a priority risk.

## Limitations
The theorem is restricted to fixed positive integer additions, independent Bernoulli selection of replacement rules, two colours, fixed starting counts and the exact critical equality. It makes no assertion about uniformity under parameters approaching the critical surface with \(N\), nor about rates of convergence. The finite checker is not an infinite-dimensional proof. The logarithmic-clock Brownian principle was already proved for critical elephant walks by Fang. Broad generalized-urn limit theorems may imply the mixed-model specialization; the full text of Janson (2004) was inaccessible here, and independent validation has not been performed.

## References
- J. Shi, Q. Yin, Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669v1 (first public 2026-05-26). https://arxiv.org/html/2605.26669v1
- R. Alves, R. A. Rosales, *Friedman vs Pólya*, arXiv:2502.16768 (first public 2025-02-24). https://arxiv.org/abs/2502.16768
- Z. Fang, *How long does it take an Elephant Random Walk to forget its training*, arXiv:2509.15049 (first public 2025-09-18); journal version *How Long does it Take to Train an Elephant Random Walk*, Journal of Statistical Physics 193 (2026), article 80. https://link.springer.com/article/10.1007/s10955-026-03646-7
- S. Janson, *Functional limit theorems for multitype branching processes and generalized Pólya urns*, Stochastic Processes and their Applications 110 (2004), 177–245. https://doi.org/10.1016/j.spa.2003.12.002
- R. Pemantle, *A survey of random processes with reinforcement*, Probability Surveys 4 (2007), 1–79. https://doi.org/10.1214/07-PS094
