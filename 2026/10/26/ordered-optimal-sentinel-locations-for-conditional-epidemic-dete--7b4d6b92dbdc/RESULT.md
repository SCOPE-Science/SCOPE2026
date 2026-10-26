# Ordered optimal sentinel locations for conditional epidemic detection on paths

## Finding

Consider one observed sentinel in a path-shaped contact network. An infection starts uniformly at one of the other vertices, and each contact transmits independently with probability \(p\) in one discrete time step. Conditional on eventual sentinel infection, the optimal site for minimizing expected detection time moves monotonically **from the vertices next to an endpoint toward the center**, visiting every intermediate position on a nonempty transmission-probability interval. Each successive change occurs at exactly one threshold, and these thresholds are strictly increasing. In contrast, maximizing the probability of detection always selects a central site. The first possible probability-dependent optimal conditional-detection site occurs on a five-vertex path, at \(p=\sqrt{2}-1\).

More precisely, let \(P_n\) have labeled vertices \(1,\ldots,n\), with \(n\ge3\). Place one sentinel at \(j\) and choose the initial infection uniformly from the other \(n-1\) vertices. Every infected vertex attempts to transmit to each as-yet-uninfected neighbor in the following step, each undirected edge supporting transmission independently with probability \(p\in(0,1)\); successfully traversed edges transmit in exactly one step and no edge is retried. Let \(D_j\) be the time the sentinel is infected, with \(D_j=\infty\) if it never is. Define \(\mu_j(p)=\mathbb E[D_j\mid D_j<\infty]\).

Write \(k=\lfloor(n+1)/2\rfloor\). For \(n=3,4\), the optimal positions are the central vertex or central pair for all \(p\). For every \(n\ge5\), there are uniquely determined thresholds
\[
0<\tau_2<\tau_3<\cdots<\tau_{k-1}<1,
\]
such that on \((0,\tau_2)\) precisely the mirrored positions \(2,n-1\) minimize \(\mu_j\); on \((\tau_{r-1},\tau_r)\), with \(3\le r<k\), precisely \(r,n+1-r\) minimize it; and on \((\tau_{k-1},1)\) precisely the central position(s) minimize it. At \(p=\tau_r\), precisely the adjacent mirrored position classes \(r,r+1\) are tied for the minimum. Repeated or coincident positions are understood as a set. Each threshold is the unique solution of
\[
\frac{\sum_{d=1}^{r-1} d p^d+\sum_{d=1}^{n-r}d p^d}{\sum_{d=1}^{r-1}p^d+\sum_{d=1}^{n-r}p^d}
= r-\frac{(n-2r)p^{n-2r}}{1-p^{n-2r}},\qquad 2\le r<k.
\]
For \(n=5\), \(\tau_2=\sqrt{2}-1\). For every \(n\ge3\) and every \(p\in(0,1)\), the central site(s) uniquely maximize \(\Pr(D_j<\infty)\), up to reflection.

## Assumptions and scope

The result assumes a finite simple path, a single sentinel, a uniformly sampled initial infection among *nonsentinel* vertices, static independent homogeneous edge-transmission outcomes, and deterministic one-step transmission along successful edges. A contagion travels along the unique path from its seed to the sentinel if and only if every edge on that path succeeds. No competing seed, repeated transmission, latent time, stochastic edge-travel duration, or recovery-delay distribution is modeled. Time is a number of successful edge traversals. All statements quantify over integers \(n\ge3\) and probabilities \(0<p<1\), with the two-vertex case trivial by symmetry.

The conditional objective discards outbreaks that fail to reach the sentinel; it must not be confused with expected time to *either* discovery or epidemic extinction, or with a population-level mean detection delay that assigns a penalty to undetected outbreaks. A favorable conditional mean can accompany a lower overall probability of ever detecting the outbreak.

## Proof

**Step 1: exact detection polynomial.** For fixed \(j\), an initially infected vertex at distance \(d\) reaches the sentinel after precisely \(d\) steps with probability \(p^d\). Set
\[
F_j(p)=\sum_{i\ne j}p^{|i-j|}=\sum_{d=1}^{j-1}p^d+\sum_{d=1}^{n-j}p^d,
\qquad G_j(p)=pF_j'(p).
\]
The initial seed is uniform among \(n-1\) possibilities, hence
\[
\Pr(D_j<\infty)=\frac{F_j(p)}{n-1},\qquad
\mu_j(p)=\frac{G_j(p)}{F_j(p)}=\frac{pF_j'(p)}{F_j(p)}.
\]
Reflection gives \(\mu_j=\mu_{n+1-j}\) and \(F_j=F_{n+1-j}\); it suffices to consider \(1\le j\le k\).

**Step 2: one adjacent comparison.** For \(1\le j<k\) write \(d=n-2j\), so \(d\ge1\). Moving the sentinel one step inward replaces one possible seed distance \(n-j\) by distance \(j\), giving
\[
F_{j+1}-F_j=p^j-p^{n-j}=p^j(1-p^d),
\qquad G_{j+1}-G_j=j p^j-(n-j)p^{n-j}.
\]
Thus \(F_{j+1}>F_j\): detection probability strictly increases toward the center. For conditional time, direct cross-multiplication yields
\[
\mu_{j+1}-\mu_j
=\frac{p^j(1-p^d)}{F_{j+1}}\bigl(M_j(p)-\mu_j(p)\bigr),
\qquad M_j(p)=j-\frac{d p^d}{1-p^d}.
\]
All prefactors outside parentheses are positive. The endpoint is never optimal for \(n\ge3\): when \(j=1\), \(\mu_1(p)>1\) (a seed at distance at least two has positive conditional probability) while \(M_1(p)<1\); thus \(\mu_2<\mu_1\).

**Step 3: unique adjacent thresholds.** Fix \(2\le j<k\). The conditional law of \(d\) among detected cases has weights proportional to \(p^d\). Differentiation with respect to \(\log p\) gives
\[
\frac{d\mu_j}{d\log p}=\operatorname{Var}(D_j\mid D_j<\infty)>0,
\]
since these sites have both distance-one and distance-two possible seeds. Therefore \(\mu_j\) is strictly increasing in \(p\), whereas \(M_j\) is strictly decreasing. As \(p\downarrow0\), \(\mu_j\to1<j=\lim M_j\); as \(p\uparrow1\), \(M_j\to-\infty\) while \(\mu_j\) remains bounded by \(n-1\). Hence each equation \(\mu_j=M_j\) has exactly one solution \(\tau_j\in(0,1)\). By Step 2, \(\mu_{j+1}>\mu_j\) below \(\tau_j\) and \(\mu_{j+1}<\mu_j\) above it.

**Step 4: the thresholds occur in strict order.** Fix \(p\in(0,1)\) and put \(\lambda=-\log p>0\), \(h(x)=x/(e^{\lambda x}-1)\) for real \(x>0\). Then \(M_j=j-h(n-2j)\). The function
\[
h(x)+\frac{x}{2}=\frac{x}{2}\coth\left(\frac{\lambda x}{2}\right)
\]
is strictly increasing in \(x>0\), since after setting \(y=\lambda x/2\) its derivative equals
\[
\frac{\sinh y\cosh y-y}{2\sinh^2 y}>0.
\]
If both \(M_j\) and \(M_{j+1}\) are defined, then \(d=n-2j\ge3\) and therefore
\[
h(d-2)-h(d)<1,\qquad M_{j+1}-M_j=1-h(d-2)+h(d)>0.
\]
At \(p=\tau_j\), Step 2 gives \(\mu_j=\mu_{j+1}=M_j\). Consequently \(\mu_{j+1}<M_{j+1}\) at that parameter. By the strictly decreasing sign change in Step 3, this implies \(\tau_j<\tau_{j+1}\).

**Step 5: global optimality and the first threshold.** For \(p\) below all thresholds, the conditional means strictly increase on positions \(2,3,\ldots,k\); as successive thresholds are crossed, the unique local/global minimum moves inward exactly one position at a time, because all adjacent comparisons have the ordered signs established above. At a threshold only the corresponding two neighboring classes tie. Reflection gives every minimizer. The strict increase of \(F_j\) toward the center, from Step 2, separately proves the detection-probability statement.

For \(n\le4\), only the endpoint-to-next-position comparison is needed, yielding the fixed central optimum. For \(n=5\) the sole interior comparison is between
\[
F_2=2p+p^2+p^3,\qquad F_3=2p+2p^2.
\]
The equality \(\mu_2=\mu_3\) reduces to \(p^2+2p-1=0\); its sole interior root is \(\sqrt2-1\). Thus five vertices are the sharp minimum size at which the conditional-time-optimal monitor changes as transmission varies.

## Verification

A standalone exact-arithmetic script, `verify.py`, enumerates *all* independent edge-open/closed configurations on paths of orders \(2\) through \(9\), testing each sentinel and four rational transmission probabilities. It separately verifies the detection and detected-delay numerator expressions against the distance-polynomial calculation (176 monitor/parameter combinations over 16,384 weighted labeled configurations). It brackets every analytic adjacent threshold for path orders \(5\) through \(24\) using exact rational inequalities and checks their strict order; it also tests 110 independent global-minimizer comparisons. The deterministic output is `certificate.json`. The general all-order theorem rests on the analytical proof, not these finite tests.

Reproduce using Python 3 standard library with `python verify.py` and compare its single output line to `certificate.json` after removing its final newline only if needed; both are included alongside this document.

## Relationship to prior work

Christakis and Fowler (2010) motivated early epidemic detection using centrally situated social sensors and empirical lead time, but did not study the exact conditional delay on all path lengths. Sun et al. (2014) considered sensor performance in a large metropolitan temporal encounter network and used simulations rather than the independent fixed-edge path model.

Ciccolini et al. (2014) optimized sentinel hospitals using movement data and heuristics. Holme (2017, preprint arXiv:1708.06456) explicitly recognized conditional sentinel discovery time, but its principal analysis uses continuous-time Markov SIR with exponential infectious and recovery durations, considers graphs of at most seven vertices, and does not provide this all-length sequence of ordered path thresholds under deterministic unit edge delays. The conditional-detection objective itself is therefore **not claimed as new**; the all-path phase-order theorem is the assessed contribution. Related exact results concerning optimal vaccinated vertices or spreading seed locations use different intervention objectives and do not imply this conditional-latency sequence.

## Limitations

All assertions are for the precisely stated discrete-generation independent-edge path model, not general SIR, real hospital networks, heterogeneous edges, repeated exposures, or graphs with cycles. The conditional metric can reward a sensor that misses many outbreaks. The theorem does not optimize a decision-theoretic combined coverage/latency utility or sampling noise. It has not received independent scientific audit. An equivalent all-path theorem under exponential-tilt or conditioned-distance terminology could exist outside the inspected literature; further bibliographic scrutiny is appropriate.

## References

- N. A. Christakis and J. H. Fowler, *Social Network Sensors for Early Detection of Contagious Outbreaks*, arXiv:1004.4792, initially submitted 27 April 2010; PLOS ONE 5(9):e12948 (2010). https://arxiv.org/abs/1004.4792 ; https://doi.org/10.1371/journal.pone.0012948
- L. Sun, K. W. Axhausen, D.-H. Lee, et al., *Efficient detection of contagious outbreaks in massive metropolitan encounter networks*, Scientific Reports 4, 5099 (2014). https://doi.org/10.1038/srep05099
- M. Ciccolini, T. Donker, H. Grundmann, M. J. M. Bonten, and M. E. J. Woolhouse, *Efficient surveillance for healthcare-associated infections spreading between hospitals*, PNAS 111, 2271–2276 (2014). https://doi.org/10.1073/pnas.1308062111
- P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456 (2017); Physical Review E 96, 062305 (2017). https://arxiv.org/abs/1708.06456
