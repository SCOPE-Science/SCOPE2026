# Sharp \(1/\log n\) Poisson defect for geometric-lifetime frogs on complete graphs

## Finding

**Theorem (sharp rare-extinction correction).** Fix any real constant \(c\). For each sufficiently large integer \(n\), put \(\mu_n=\log n+c>0\) and \(p_n=\mu_n/(1+\mu_n)\). Start a frog process on the loopless complete graph \(K_n\) with exactly one frog at each vertex: only the root frog is initially active. At each action, an active frog dies with probability \(1-p_n\), or otherwise jumps to a uniformly selected different vertex, activating the resident frog on first visit. All decisions are independent. Let \(N_n\) be the number of vertices never visited when the process terminates, and let \(\Pi_c\) be Poisson with mean \(\lambda=e^{-c}\). Then, with \(q_n=1/(1+\mu_n)\),

\[
 d_{\mathrm{TV}}\bigl(\mathcal L(N_n),\; (1-q_n)\Pi_c+q_n\delta_{n-1}\bigr)
 =O_c(\mu_n^{-2}),
\]

and, in particular,

\[
\boxed{\quad d_{\mathrm{TV}}\bigl(\mathcal L(N_n),\Pi_c\bigr)
=q_n+O_c(\mu_n^{-2}),\qquad
\Pr(N_n=0)=(1-q_n)e^{-\lambda}+O_c(\mu_n^{-2}).\quad}
\]

Thus \(\lim_{n\to\infty}(\log n)d_{\mathrm{TV}}(\mathcal L(N_n),\Pi_c)=1\). The precise first correction is a disappearing mass \(q_n\) at the macroscopic failure state \(N_n=n-1\), not a change in the Poisson mean. For the conventional critical choice \(p_n=1-1/\log n\), one has \(\mu_n=\log n-1\) and hence \(\Pr(N_n=0)=e^{-e}(1-1/\log n)+O((\log n)^{-2})\).

## Assumptions and scope

All logarithms are natural. The graph has \(n\ge2\) vertices and no self-loops. Exactly one frog starts on every vertex, with only the frog at a designated root awake. A frog takes a geometrically distributed number of transitions (support \(\{0,1,2,\ldots\}\), mean \(\mu_n\)); its own sequence of moves and its lifetime are independent of other frogs. Serializing active-frog actions does not change the terminal visited set, because each frog's entire potential trajectory can be sampled in advance. Total variation is \(d_{\mathrm{TV}}(P,Q)=\sup_A|P(A)-Q(A)|\). All asymptotic constants may depend on fixed \(c\) but not on \(n\).

## Proof

**1. Independent trajectories and isolated vertices.** Preassign independent, finite killed random-walk trajectories to every frog, including those that never awaken. Create an arc \(i\to j\) exactly when frog \(i\)'s trajectory visits the different vertex \(j\). The set of awakened vertices is precisely the set reachable from the root in this directed graph. If a forbidden set \(S\) has \(s\) vertices and a frog starts outside \(S\), each surviving transition hits \(S\) with probability \(s/(n-1)\) before the first hit. Hence the exact probability of avoiding \(S\) for its entire life is

\[
Q_s=\frac{1-p_n}{1-p_n+p_ns/(n-1)}
=\left(1+\frac{\mu_n s}{n-1}\right)^{-1}.
\]

Let \(Z_n^0\) count the nonroot vertices which have no incoming arc from **any nonroot frog other than themselves**, i.e., discard all arcs emitted by the root. Define \(Z_n\) similarly with the root's arcs retained. For each \(1\le k\le n-1\), independent trajectories give exact factorial moments

\[
\begin{aligned}
\mathbb E(Z_n^0)_k&=(n-1)_kQ_{k-1}^{k}Q_k^{n-k-1},\\
\mathbb E(Z_n)_k&=(n-1)_kQ_{k-1}^{k}Q_k^{n-k},
\end{aligned}
\]

where \(Q_0=1\), \((x)_k=x(x-1)\cdots(x-k+1)\), and the zeroth moments equal one. Indeed, every frog whose home lies in a prescribed \(k\)-set must avoid the other \(k-1\) sites, while every frog outside it must avoid all \(k\) sites; remove the root factor in the first formula. By elementary logarithmic expansions, uniformly over \(0\le k\le 3K_n\), for \(K_n=\lceil\mu_n^{1/3}\rceil\),

\[
\mathbb E(Z_n^0)_k=\lambda^k\bigl(1+O_c(\mu_n^2K_n^2/n)\bigr),
\quad
\mathbb E(Z_n)_k=\lambda^k\bigl(1+O_c(\mu_n^2K_n^2/n)\bigr).
\]

Truncated inclusion–exclusion for \(\Pr(Z_n^0=j)\) and \(\Pr(Z_n=j)\), with truncation length \(K_n\), has Bonferroni remainders bounded by corresponding factorial moments divided by \(K_n!\). The tail beyond \(K_n\) is bounded by \(\mathbb E(Z_n^0)_{K_n+1}/(K_n+1)!\), and similarly for \(Z_n\). Summing the absolute errors over \(j\le K_n\) gives

\[
d_{\mathrm{TV}}(\mathcal L(Z_n^0),\Pi_c)
+d_{\mathrm{TV}}(\mathcal L(Z_n),\Pi_c)
=O_c\!\left(\frac{\mu_n^2K_n^2}{n}
+\frac{C_c^{2K_n+2}}{K_n!}\right)=o(\mu_n^{-2}).
\]

**2. Rare early extinction.** Write \(B_n\) for the event that the root frog dies before its first jump. Its probability is **exactly** \(q_n=1-p_n\), and \(B_n\) is independent of \(Z_n^0\). On \(B_n\), clearly \(N_n=n-1\). On \(B_n^c\), the first jump necessarily discovers a new vertex, so the number of active frogs becomes two. In an asynchronous serialization let \(a\) count living frogs and \(v\) visited vertices. Before \(v\) reaches \(\lceil n/2\rceil\), each action changes \(a\) by \(+1,-1,0\), respectively, with probabilities \(b=p_n(n-v)/(n-1)\ge p_n/2\), \(d=1-p_n\), and \(1-b-d\). For sufficiently large \(n\), \(\rho=2d/p_n<1\), and \(\rho^a\) is a nonnegative supermartingale until extinction or the halfway discovery boundary: the drift is \(\rho^a[b(\rho-1)+d(\rho^{-1}-1)]\le0\). Optional stopping from \(a=2\) yields

\[
\Pr(\text{extinction before visiting half the graph}\mid B_n^c)
\le \rho^2=O_c(\mu_n^{-2}).
\]

**3. No hidden unreachable clusters after macroscopic growth.** An unvisited vertex set \(S\) has no incoming arcs from outside \(S\), because every frog outside \(S\) has awakened and completed its preassigned path. If \(S\) also has no arc joining two different vertices of \(S\), each member is an indegree-zero vertex, so \(N_n=Z_n\). For a fixed nonroot \(S\) of size \(s\), the absence of outside incoming arcs has probability \(Q_s^{n-s}\); the trajectories of the \(s\) frogs inside \(S\) are independent of this event. A union bound over steps made by those frogs bounds the chance of an internal arc by \(\min\{1,\mu_ns^2/(n-1)\}\). Therefore the probability of a nonempty unreachable set of size \(2\le s\le n/2\) with any internal arc is at most

\[
R_n=\sum_{s=2}^{\lfloor n/2\rfloor}
\binom{n-1}{s}Q_s^{n-s}
\min\left\{1,\frac{\mu_ns^2}{n-1}\right\}.
\]

We show \(R_n=O_c(\mu_n/n)\). For \(s\le n^{1/3}\), the first two factors are uniformly \((1+o(1))e^{-cs}/s!\), giving \(O_c(\mu_n/n)\) after summation. For \(n^{1/3}<s\le n/\mu_n^2\), use \(\log(1+x)\ge x-x^2/2\) and \(\binom ns\le(en/s)^s\) to get \(\binom{n-1}sQ_s^{n-s}\le \exp(-s\log n/4)\) for large \(n\). For \(n/\mu_n^2<s\le n/\sqrt{\mu_n}\), use \(\log(1+x)\ge x/(1+x)\) to get an exponential bound \(\exp(-\Omega(s\sqrt{\mu_n}))\). Finally, for \(n/\sqrt{\mu_n}<s\le n/2\), bound the binomial coefficient by \(2^n\) and the avoiding probability by \((1+\sqrt{\mu_n})^{-n/2}\), yielding \(\exp(-\Omega(n\log\mu_n))\). The three latter ranges sum to \(o_c(\mu_n/n)\). Consequently, conditional on \(B_n^c\), the chance \(N_n\ne Z_n\) is \(O_c(\mu_n^{-2}+\mu_n/n)\).

**4. Removing the root's arcs and identifying the sharp defect.** For a fixed nonroot vertex, its probability of having no incoming arc from other nonroot frogs is \(Q_1^{n-2}\), and independently its probability of being visited by the root frog is \(1-Q_1\). A union bound therefore yields

\[
\Pr(Z_n\ne Z_n^0)
\le(n-1)(1-Q_1)Q_1^{n-2}=O_c(\mu_n/n).
\]

Couple \(N_n\) to \(Y_n=(n-1)\mathbf1_{B_n}+Z_n^0\mathbf1_{B_n^c}\). The preceding estimates give

\[
 d_{\mathrm{TV}}(\mathcal L(N_n),\mathcal L(Y_n))
=O_c(\mu_n^{-2}),\qquad
\mathcal L(Y_n)=q_n\delta_{n-1}+(1-q_n)\mathcal L(Z_n^0).
\]

Using Step 1 proves the first asserted mixture approximation. Finally, for any probability law \(P\),
\[
d_{\mathrm{TV}}\bigl(q_n\delta_{n-1}+(1-q_n)P,P\bigr)
=q_n(1-P\{n-1\}).\]

For \(P=\Pi_c\), \(\Pi_c\{n-1\}\to0\); the triangle inequality in both directions proves the stated sharp total-variation expansion. Taking the event \(\{0\}\) gives the full-coverage expansion, because \(n-1>0\). This completes the proof.

## Verification

A standalone, standard-library Python checker gives two independent exact finite-population descriptions: an absorbing Markov recursion in living-frog and visited-vertex counts, and a closed-reachable-set recursion based on the probability that all frogs within a candidate reached set remain there. It verifies their equality on a collection of rational parameters, tests the exact first-death mass, and checks factorial-moment inversion for indegree-zero vertices. The checker reports 1,265 exact finite assertions; these finite tests are diagnostics only. The theorem for all large \(n\) follows from the foregoing inequalities and factorial-moment bounds, not from enumeration.

## Relationship to prior work

De Carvalho and Machado [1], first publicly posted October 10, 2022, study the one-frog-per-vertex model and the fixed-parameter coverage ratio. Their later work [2], first publicly posted July 26, 2024, studies high-survival coverage thresholds in a related setup with an additional root population and gives a threshold dichotomy, not the sharp one-root finite-size defect above. Ball and Barbour [3] establish Poisson approximation for survivors of severe random-contact epidemics, including an almost-geometric contact law, with an order \(O(1/\log n)\) total-variation estimate. They expressly discuss early epidemic extinction and suggest mixture approximations. Hence neither Poisson convergence nor an \(O(1/\log n)\) rate is claimed as new here. The asserted additional content is the **exact leading constant one** of the total-variation discrepancy, an explicit mass escaping to \(n-1\), and the corresponding first coverage-probability correction for this fully specified frog model. These do not follow merely from the earlier order bound or qualitative mixture remark without a quantitative coupling.

## Limitations

The coefficient is for one initially active frog, one sleeping frog at each other site, and uniform loopless complete-graph jumps. Adding initial root frogs changes the early-extinction scale; it is not treated. The asymptotic is pointwise for fixed real \(c\), not uniform over a growing critical window. The Poisson approximation and its order were known in broader epidemic theory; potential overlooked sharper epidemic asymptotics are a residual historical-priority risk. The numerical checker supplies no independent proof or independent validation.

## References

[1] G. O. de Carvalho and F. P. Machado, *The coverage ratio of the frog model on complete graphs*, arXiv:2210.04968v1 (first posted 2022-10-10), https://arxiv.org/abs/2210.04968.

[2] G. O. de Carvalho and F. P. Machado, *Critical Conditions for the Coverage of Complete Graphs with the Frog Model*, arXiv:2407.19027v1 (first posted 2024-07-26), https://arxiv.org/abs/2407.19027.

[3] F. Ball and A. D. Barbour, *Poisson Approximation for Some Epidemic Models*, Journal of Applied Probability **27** (1990), 479–490, https://doi.org/10.2307/3214534; open full text: https://sites.math.rutgers.edu/~zeilberg/EM20/epidemics/ball.pdf.
