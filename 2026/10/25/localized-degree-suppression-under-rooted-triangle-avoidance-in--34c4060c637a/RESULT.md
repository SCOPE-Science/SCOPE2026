# Localized degree suppression under rooted triangle avoidance in sparse random graphs

## Finding
Let \(G_n\sim G(n,p_n)\) with \(p_n=c n^{-\alpha}\), where \(c>0\), \(0<\alpha<1\) are fixed and \(n\) is sufficiently large that \(0<p_n<1\). Fix one vertex \(v\), let \(D_n=\deg(v)\), and let \(S_n\) be the event that no triangle contains \(v\). Let \(W\) denote the positive Lambert inverse defined by \(W(t)e^{W(t)}=t\), and put
\[
 u_n=\frac{W((n-1)p_n^2)}{p_n}.
\]
Then, conditional on \(S_n\), \(D_n/u_n\to1\) in probability. Equivalently,
\[
 D_n\sim_{\Pr(\cdot\mid S_n)}
 \begin{cases}
 \dfrac{1-2\alpha}{c}n^{\alpha}\log n,&0<\alpha<1/2,\\[2mm]
 \dfrac{W(c^2)}c\sqrt n,&\alpha=1/2,\\[2mm]
 c n^{1-\alpha},&1/2<\alpha<1.
 \end{cases}
\]
Here the displayed equivalence means that the ratio of the random variable to the deterministic expression converges to one in conditional probability; it does **not** assert almost-sure equivalence. The rarity of the conditioning event obeys
\[
 -\log\Pr(S_n)\sim
 \begin{cases}
 c n^{1-\alpha},&0<\alpha<1/2,\\
 \Psi(c)\sqrt n,&\alpha=1/2,\\
 \frac{c^3}{2}n^{2-3\alpha},&1/2<\alpha<1,
 \end{cases}
\]
where, writing \(x_c=W(c^2)/c\),
\[
 \Psi(c)=c-x_c-\frac c2 x_c^2>0.
\]
The third equivalence includes \(\alpha>2/3\), where both sides tend to zero: in that regime \(\Pr(S_n)\to1\).

At criticality \(\alpha=1/2\), conditional on \(S_n\), the variables \(D_n/\sqrt n\) satisfy a full large-deviation principle with speed \(\sqrt n\) and good rate function
\[
 I_c(x)=x\log(x/c)-x+c+\frac c2 x^2-\Psi(c),\qquad x\ge0,
\]
with \(0\log0=0\) and \(I_c(x)=+\infty\) for \(x<0\). Its sole zero is \(x_c\). At this critical scale the root's normalized degree falls by the strict factor \(W(c^2)/c^2<1\).

The defect is localized: in **each** of the three regimes, conditional on \(S_n\),
\[
 \max_{u\ne v}\left|\frac{\deg(u)}{(n-1)p_n}-1\right|\xrightarrow{\Pr}0.
\]
Thus the other vertices retain their ordinary asymptotic degrees, despite the possibly large change at the distinguished root.

## Assumptions and scope
All graphs are simple, undirected, and labeled. Edges are mutually independent before conditioning; the selected root is deterministic. \(c\) and \(\alpha\) are fixed independent of \(n\). The event \(S_n\) says exactly that the *open neighborhood* of \(v\) induces no edges; it does not require the entire graph to be triangle-free. Every asymptotic statement is for \(n\to\infty\), conditional on the positive-probability event \(S_n\).

## Proof
**1. Exact law.** The unconditioned degree \(D_n\) is \(\operatorname{Bin}(n-1,p_n)\). Given its neighbor set of size \(d\), the \(\binom d2\) edges among the neighbors are independent Bernoulli variables, hence
\[
 w_{n,d}:=\Pr(D_n=d,S_n)=\binom{n-1}{d}p_n^d(1-p_n)^{n-1-d+\binom d2},\quad0\le d\le n-1.
\]
Consequently \(\Pr(D_n=d\mid S_n)=w_{n,d}/\sum_jw_{n,j}\). Writing \(p=p_n\), \(q=1-p\), successive weights have the exact ratio
\[
 \rho_d=\frac{w_{n,d+1}}{w_{n,d}}=\frac{(n-1-d)p}{d+1}\,q^{d-1},\qquad0\le d\le n-2.
\]
These ratios decrease strictly with \(d\), so the conditional degree law is strictly log-concave across its support.

**2. Universal degree saddle and concentration.** Define \(u=u_n=W((n-1)p^2)/p\). It solves exactly \(u e^{pu}=(n-1)p\). Since \(0<\alpha<1\), we have \(u\to\infty\), \(u=o(n)\), and \(p^2u\to0\). For each fixed \(a>0\) and \(d=\lfloor au\rfloor\), elementary expansion of the exact ratio yields
\[
 \log\rho_d=-\log a+(1-a)pu+o(1).
\]
The error is uniform for \(a\) in compact subsets of \((0,\infty)\). Hence the ratio is bounded above one at \(a<1\) and below one at \(a>1\), with bounds away from one (possibly improving as \(pu\to\infty\)). By monotonicity of \(\rho_d\), the mode lies between \((1-\varepsilon)u\) and \((1+\varepsilon)u\) for all large \(n\). Applying the bounded-away-from-one ratios over a positive fraction of \(u\) indices and then summing the remaining geometric tails shows
\[
 \Pr(|D_n/u-1|>\varepsilon\mid S_n)\le C_\varepsilon e^{-b_\varepsilon u}\to0.
\]
The constants can be fixed for each \(\varepsilon\in(0,1)\). Now \(W(t)\sim t\) as \(t\downarrow0\), \(W(t)\sim\log t\) as \(t\to\infty\), and \(W(c^2)\) is fixed at the middle scale. Substituting \((n-1)p^2\sim c^2n^{1-2\alpha}\) gives the three stated degree regimes.

**3. Probability below criticality.** For \(0<\alpha<1/2\), factor \(\Pr(S_n)=q^{n-1}B_n\), where
\[
 B_n=\sum_{d=0}^{n-1}\binom{n-1}{d}(p/q)^d q^{\binom d2}\ge1.
\]
For \(d\ge1\), \(\binom{n-1}{d}\le(e(n-1)/d)^d\). Using \(\log q\le-p\), and discarding the nonpositive term \(-d\log d\), we obtain
\[
 \log B_n\le\log n+\frac{(\log(e(n-1)p/q)+p/2)^2}{2p}
 =O(n^\alpha\log^2n)=o(np).
\]
Together with \(B_n\ge1\) and \(-\log q^{n-1}\sim np\), this gives \(-\log\Pr(S_n)\sim np\sim c n^{1-\alpha}\).

**4. Critical large deviations.** Set \(\alpha=1/2\). Uniformly over \(d/\sqrt n\) in a compact subset of \([0,\infty)\), Stirling's formula (including the \(d=o(\sqrt n)\) boundary estimate) yields
\[
 \frac1{\sqrt n}\log w_{n,d}=-F_c(d/\sqrt n)+o(1),\qquad
 F_c(x)=x\log(x/c)-x+c+\frac c2x^2.
\]
Exponential tightness follows because \(w_{n,d}\le\Pr(\operatorname{Bin}(n-1,p)=d)\) and the binomial Chernoff bound has rate tending to infinity as \(d/\sqrt n\to\infty\). The discrete Laplace principle therefore gives
\[
 \frac1{\sqrt n}\log\Pr(S_n)\to-\min_{x\ge0}F_c(x).
\]
For \(x>0\), \(F'_c(x)=\log(x/c)+cx\) and \(F''_c(x)=1/x+c>0\). Its unique minimizing point is \(x_c=W(c^2)/c\), and \(F_c(x_c)=c-x_c-cx_c^2/2=\Psi(c)\). Normalizing the weights establishes the stated full conditional large-deviation principle by the same compact-interval upper and lower bounds, together with exponential tightness. Because \(F_c(0)=c>0\) and the minimizer is positive, \(\Psi(c)>0\).

**5. Probability above criticality.** If \(1/2<\alpha<1\), let \(B\sim\operatorname{Bin}(n-1,p)\), \(t_n=(n-1)^2p^3/2\), and \(h=-\log q\sim p\). Then \(\Pr(S_n)=\mathbb E e^{-h\binom B2}\). We have \((n-1)p\to\infty\), \((n-1)p^2\to0\), and \(h\binom B2/t_n\to1\) in probability. If \(t_n\to\infty\), binomial Chernoff bounds outside a fixed relative band are \(\exp[-\Omega(np)]\), negligible on the \(t_n\)-logarithmic scale because \(np/t_n\to\infty\); squeezing the expectation inside that band then shrinking the band proves \(-\log\Pr(S_n)\sim t_n\). If \(t_n\to t\in(0,\infty)\), bounded convergence of \(e^{-h\binom B2}\) gives \(\Pr(S_n)\to e^{-t}\). If \(t_n\to0\), the inequality \(0\le y-(1-e^{-y})\le y^2/2\), together with the exact binomial factorial moments, gives
\[
 \mathbb E[h\tbinom B2]\sim t_n,\qquad
 \mathbb E[(h\tbinom B2)^2]=O(t_n^2+t_n(np^2+p))=o(t_n).
\]
Therefore \(1-\Pr(S_n)\sim t_n\), and again \(-\log\Pr(S_n)\sim t_n\). These cases cover all \(\alpha>1/2\).

**6. Localization.** Conditional on \(S_n\) and on the exact neighbor set \(A\) of \(v\), \(|A|=d\), all edges within \(A\) are forced absent and all other edges remain independent Bernoulli variables. For \(u\in A\),
\[
 \deg(u)\stackrel d=1+\operatorname{Bin}(n-1-d,p),
\]
whereas for \(u\notin A\cup\{v\}\), \(\deg(u)\stackrel d=\operatorname{Bin}(n-2,p)\). By Step 2, \(D_n=o(n)\) in conditional probability, and \(np\gg\log n\). Uniform Chernoff bounds plus a union bound over the \(n-1\) remaining vertices give \(\max_{u\ne v}|\deg(u)/((n-1)p)-1|\to0\) in conditional probability. The strict suppression factor at criticality follows from \(W(c^2)<c^2\) for \(c>0\).

## Verification
A standalone stdlib checker, `verify_root_triangle.py`, exactly enumerates every labeled simple graph through six vertices for two rational edge probabilities and compares the resulting joint degree/event masses against the closed formula, also checking all successive ratios and their strict ordering. It additionally numerically checks the Lambert saddle across three exponents and the critical rare-event rate using normalized log weights. It passed 99 assertions. The infinite limit laws follow from the proof, not from those finite tests.

## Relationship to prior work
Janson and Ruciński, arXiv:0905.0972v1 (May 7, 2009), Section 3 and Example 3.3, study **upper tails** for rooted subgraph copy counts, including rooted cliques. Those theorems concern \(\Pr(X\ge t\mathbb EX)\) for \(t>1\), not \(\Pr(X=0)\) or degree conditioning by the absence of a rooted triangle; their upper-tail inequalities do not imply the present exact conditional law or Lambert phase diagram. Fountoulakis, Kang, and McDiarmid, arXiv:1203.0132v1 (March 1, 2012), study *maximal sizes* of globally selected sparse induced vertex sets, rather than the distribution of a specified random neighborhood constrained to be independent. Bloznelis, arXiv:1303.3388v1 (March 14, 2013), studies degree and clustering in random **intersection** graph models, not independent-edge Erdős–Rényi graphs. Jenssen, Perkins, and Potukuchi, arXiv:2312.09202v1 (December 14, 2023), condition the **entire graph** to be triangle-free, rather than requiring no triangle through a single fixed vertex. Earlier general estimates for absence of triangles, including Wormald (1996), concern global avoidance; they remain background and potential implicit-priority leads.

## Limitations
The result does not characterize the entire globally triangle-free random-graph ensemble, does not give a central limit theorem for the conditioned root degree, and does not assert a sharp prefactor for \(\Pr(S_n)\). The proof is an analytic derivation from elementary conditional weights and standard asymptotics; earlier work on exponential tilting or independent-set conditioning could conceivably subsume it in a more general formulation, so historical priority should receive independent review. Finite experiments cannot certify novelty or infinite asymptotics. The stated origin date is the earliest precise first-public date verified among the specifically inspected foundational papers; some earlier publications lack a day-verified first-public record.

## References
- S. Janson and A. Ruciński, *Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs*, arXiv:0905.0972v1, posted 2009-05-07, https://arxiv.org/html/0905.0972v1.
- N. Fountoulakis, R. J. Kang, and C. McDiarmid, *Largest sparse subgraphs of random graphs*, arXiv:1203.0132v1, posted 2012-03-01, https://arxiv.org/pdf/1203.0132.
- M. Bloznelis, *Degree and clustering coefficient in sparse random intersection graphs*, arXiv:1303.3388v1, posted 2013-03-14, https://arxiv.org/html/1303.3388v1.
- M. Jenssen, W. Perkins, and A. Potukuchi, *On the evolution of structure in triangle-free graphs*, arXiv:2312.09202v1, posted 2023-12-14, https://arxiv.org/html/2312.09202v2 (later revised text inspected; original posting date retained).
- N. C. Wormald, *The perturbation method and triangle-free random graphs*, Random Structures & Algorithms 9 (1996), 253–270, doi:10.1002/(SICI)1098-2418(199608/09)9:1/2<253::AID-RSA15>3.0.CO;2-O (abstract and publication description inspected, original full text not verified).
