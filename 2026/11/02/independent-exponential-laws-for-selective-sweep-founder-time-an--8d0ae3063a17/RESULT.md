# Independent exponential laws for selective-sweep founder time and minority-mass decay

## Finding

Consider the discrete-time independent-founder geometric branching model specified below. At population time \(n\), let \(J_n\) be the birth time of a genotype with largest population (the smallest index is chosen if there is a tie), and let
\[
P_n=\frac{\max_{1\le i\le n}G_n(i)}{\sum_{j=1}^{n}G_n(j)}
\]
be the dominant genotype's population fraction. Then
\[
\boxed{\left(\frac{J_n\log n}{n},\ -\frac{\log(1-P_n)}{n}\right)\ \Rightarrow\ (E,F),}
\]
where \(E\) and \(F\) are **independent standard exponential** random variables. In particular, for all fixed \(a,b\ge0\),
\[
\lim_{n\to\infty}\Pr\left(\frac{J_n\log n}{n}>a,\ -\frac{\log(1-P_n)}{n}>b\right)=e^{-a-b}.
\]
The result gives the exact random exponential rate at which the aggregate minority fraction decays, jointly with the mesoscopic emergence time of the dominant genotype. No finite-\(n\) claim of exact exponential distributions is made.

## Assumptions and scope

At each integer birth time \(i\ge1\), a new genotype starts with one individual. Draw \(p_i\) independently and uniformly from \((0,1)\), and conditional on \(p_i\), give every individual of that genotype an independent offspring count distributed as
\[
\Pr(Y_i=k\mid p_i)=p_i(1-p_i)^{k-1},\qquad k=1,2,\ldots.
\]
Every genotype reproduces in every subsequent discrete generation; its descendants form an independent Galton--Watson process with this geometric offspring law. Write \(G_n(i)\) for the size of genotype \(i\) at time \(n\), so that \(G_i(i)=1\). Thus for \(i\le n\), conditional on the fitness parameters,
\[
G_n(i)\sim\operatorname{Geom}\bigl(p_i^{n-i}\bigr),
\qquad\Pr(\operatorname{Geom}(q)=k)=q(1-q)^{k-1}\quad(k\ge1).
\]
There are \(n\) positive populations, so \(0<1-P_n<1\) for \(n\ge2\). The limiting claim concerns the unconditional joint law as \(n\to\infty\), with no independence assumed between the two finite-time statistics.

The primary mathematical subject is branching processes (MSC2020 60J80). Its publicly available motivating model and qualitative dominance result are due to Fontes and Schinazi (2026); they are not presented as new here.

## Proof

**Step 1: exact conditional population scaling.** Set \(\tau_i=-\log p_i\). These are independent rate-one exponential random variables. The probability generating function of the geometric offspring law is \(ps/(1-(1-p)s)\); iterating it \(k\) times gives the geometric generating function with parameter \(p^k\), proving the distribution above. Define
\[
T_{n,i}=(n-i)\tau_i,\qquad V_{n,i}=e^{-T_{n,i}}G_n(i).
\]
For every \(r\in(0,1)\), \(R>1\), and every realized \(p_i\), the geometric distribution gives
\[
\Pr(V_{n,i}<r\mid p_i)\le r,
\qquad \Pr(V_{n,i}>R\mid p_i)\le R^{-1}.
\]
Indeed, with \(q=e^{-T_{n,i}}\), the first event is \(qG<r\); if it is nonempty, it contains at most \(r/q\) positive integers, each contributing at most \(q\) by a union bound. The second inequality follows from \(\mathbb E(qG\mid q)=1\) and Markov's inequality. A union bound therefore yields, for every \(\epsilon>0\),
\[
\Pr\left(\max_{1\le i\le n}\left|\log G_n(i)-T_{n,i}\right|>\epsilon n\right)
\le2ne^{-\epsilon n}\longrightarrow0.\tag{1}
\]
This estimate simultaneously controls every competing family; it requires no separate approximation of the branching noise for high-fitness founders.

**Step 2: the marked extremal point process.** Let \(b_n\) be the unique positive solution of \(b_ne^{b_n}=n\). Then \(b_n\to\infty\) and \(b_n/\log n\to1\). Define birth-time marks and centered fitness-growth scores by
\[
x_{n,i}=b_ni/n,\qquad z_{n,i}=T_{n,i}/n-b_n,
\qquad\Xi_n=\sum_{i=1}^{n}\delta_{(x_{n,i},z_{n,i})}.
\]
For bounded \(x_{n,i}\to x\ge0\) and fixed \(z\in\mathbb R\), when \(i<n\),
\[
\begin{aligned}
\Pr(z_{n,i}>z)
&=\exp\left[-\frac{b_n+z}{1-i/n}\right]\\
&=\frac{b_n}{n}\exp(-x-z+o(1)).
\end{aligned}\tag{2}
\]
The error is uniform on compact \(x\)-intervals and bounded \(z\)-intervals. Independent rare-event convergence, obtained by taking products of Laplace transforms over disjoint rectangles, gives vague convergence on \([0,\infty)\times\mathbb R\) to a Poisson point process \(\Xi\) with intensity
\[
\boxed{e^{-x-z}\,dx\,dz.}\tag{3}
\]
There is no loss of upper extremal mass at arbitrarily late birth indices. For each fixed \(z\), using \((1-u)^{-1}\ge1+u\) and summing a geometric series,
\[
\sum_{i>Kn/b_n}\Pr(z_{n,i}>z)
\le e^{-b_n-z}\sum_{i>Kn/b_n}e^{-(b_n+z)i/n}
\le C_z e^{-K/2}
\]
for all large \(n\) and any \(K>0\). Likewise the expected number of scores above a large level \(M\) is bounded by \(C e^{-M}\); and the Poisson limit has arbitrarily many points above \(-M\) with probability tending to one as \(M\to\infty\). These truncations justify convergence of the two largest scores and the birth-time mark of the largest score.

**Step 3: independent location and score gap.** Integrating intensity (3) over \(x\ge0\) gives \(e^{-z}dz\). The marking theorem says that, conditional on all unmarked scores, their \(x\)-marks are independent with density \(e^{-x}\) on \([0,\infty)\). Let \(Z_1>Z_2\) be the largest two scores of \(\Xi\) and \(X_1\) the birth-time mark of the largest. Under \(u=e^{-z}\), the unmarked Poisson process becomes a unit-rate homogeneous Poisson process on \((0,\infty)\). Hence if \(A,B\) are independent standard exponentials, the top scores satisfy
\[
Z_1=-\log A,\qquad Z_2=-\log(A+B),
\qquad Z_1-Z_2=\log\frac{A+B}{A}.
\]
Since \(A/(A+B)\) is uniform on \((0,1)\), \(Z_1-Z_2\) is standard exponential. The mark \(X_1\) is independently standard exponential. Consequently, if \(I_n^*\) denotes the maximizing index of the deterministic scores \(T_{n,i}\), and \(T_{n,(1)}\ge T_{n,(2)}\) their top two order statistics,
\[
\left(\frac{b_nI_n^*}{n},\frac{T_{n,(1)}-T_{n,(2)}}{n}\right)
\Rightarrow(E,F),
\quad E\perp F,\quad E,F\sim\operatorname{Exp}(1).\tag{4}
\]

**Step 4: replacing growth scores by actual family sizes.** Let \(W_{n,i}=\log G_n(i)\), and let \(W_{n,(1)}\ge W_{n,(2)}\) be its largest two order statistics. Order statistics are 1-Lipschitz for the supremum norm, so by (1)
\[
\max_{k=1,2}|W_{n,(k)}-T_{n,(k)}|=o_{\Pr}(n).
\]
Because the limiting normalized growth-score gap in (4) is almost surely positive, (1) also implies \(\Pr(J_n=I_n^*)\to1\): a discrepancy requires either a score gap at most \(2\epsilon n\) or a uniform perturbation greater than \(\epsilon n\), and then \(\epsilon\downarrow0\). Therefore,
\[
\left(\frac{b_nJ_n}{n},\frac{W_{n,(1)}-W_{n,(2)}}{n}\right)\Rightarrow(E,F).
\tag{5}
\]

**Step 5: converting the runner-up gap into aggregate minority mass.** Write \(B_1\ge B_2\ge\cdots\ge B_n\) for the ordered genotype populations and \(R=\sum_{j=2}^{n}B_j\). Since \(B_2\le R\le(n-1)B_2\) and \(B_1\le B_1+R\le nB_1\), for every finite population configuration with \(n\ge2\),
\[
\left|-\log(1-P_n)-(\log B_1-\log B_2)\right|\le 2\log n.\tag{6}
\]
Combine (5)--(6) and \(b_n/\log n\to1\) to obtain the claimed joint convergence. The joint survival-function formula follows because the limiting independent exponentials have continuous distributions. \(\square\)

## Verification

A standalone exact-arithmetic program checks the geometric probability-generating-function iteration, the finite-law lower-tail bound used in (1), and finite-\(n\) independent exceedance intensities underlying (2)--(3). The Poisson order-statistic gap and independence are derived analytically in the proof, not certified by the finite checker. The program and its recorded output are supplied alongside this result; the theorem is proved by the arguments above, not by finite computation.

Reproduce with `python3 verify.py`. No nonstandard packages are needed. The analytical proof covers all real thresholds \(a,b\ge0\) and all integers \(n\to\infty\); the verifier is deliberately not an infinite-domain certificate.

## Relationship to prior work

Fontes and Schinazi, *A branching model for selective sweeps* (arXiv:2610.29759v1, first public October 21, 2026), establish eventual dominance of one genotype and derive a Poisson point-process limit for extreme fitness/time marks. Their Proposition 2 supplies a leading Gumbel limit; Lemma 4 supplies a diverging growth-score gap; Section 3 identifies the limiting Poisson envelope of genotype leaders. Those prior results and the exact geometric family law are credited here. The present theorem resolves a different natural statistic: the **full random rate on the \(n\)-scale of the residual non-dominant population mass, jointly and independently with the dominant founder's \(n/\log n\)-scale birth time**. Deriving it requires an ordered-extreme gap limit and simultaneous exponential control of actual branching-family fluctuations.

The standard Poisson mapping and marking theorems are classical; the exponential spacing of the leading two points of an \(e^{-z}dz\) process, considered in isolation, is not claimed as new. Udomchatpitak and Schweinsberg (arXiv:2407.01999) study a fixed-population selection/mutation model with different reproduction and scaling, and do not directly establish the residual-mass law for the independent growing families here. A related published result may subsume the theorem through a general theorem on competing branching families; historical priority remains subject to independent verification.

## Limitations

The conclusion is distributional and does not provide a deterministic exponential rate, tail-error estimates, almost-sure convergence, or a uniform finite-\(n\) approximation. It relies on uniform independent fitness parameters, independent geometric-offspring families, no extinction, and one founder per integer time. It does not automatically extend to fixed-size populations, competition-modified branching, heavy-tailed fitness parameters, or extinction-permitting offspring laws. The independence appears only in the limiting joint law. The limiting statements are self-reviewed but have not undergone an independent mathematical audit.

## References

1. L. R. Fontes and R. B. Schinazi, *A branching model for selective sweeps*, arXiv:2610.29759v1 (October 21, 2026), https://arxiv.org/html/2610.29759v1.
2. N. Udomchatpitak and J. Schweinsberg, *The accumulation of beneficial mutations and convergence to a Poisson process*, arXiv:2407.01999 (2024); *Stochastic Processes and their Applications* 183 (2025), article 104578, https://arxiv.org/abs/2407.01999.
3. S. I. Resnick, *Extreme Values, Regular Variation, and Point Processes*, Springer (1987; reprint 2008), classical point-process convergence and marking principles.
4. MSC2020 classification entry 60J80, *Branching processes (Galton--Watson, birth-and-death, etc.)*, https://msc2020.org/.
