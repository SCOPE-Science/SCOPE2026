# Exact hypergeometric consensus law and Gaussian majority race on odd bicliques

## Finding

An asynchronously updated binary majority process on a complete bipartite graph with **odd-sized parts** has an exact, nonrecursive probability of eventual positive consensus. In the only stochastic regime, initially opposing partwise majorities compete in a race between two sets of independent first-update clocks. The winner probability is a hypergeometric tail. For growing parts, its sharp transition depends on the **sum of the two initial within-part opinion proportions**, not on the size-weighted global opinion proportion; the critical window has an explicit normal limit.

**Theorem (finite network).** Let \(a=2u+1\) and \(b=2v+1\) be positive odd integers. On \(K_{a,b}\), every vertex initially holds a publicly visible opinion \(+\) or \(-\). Vertices have independent rate-one Poisson update clocks; on ringing, a vertex adopts the strict majority opinion of all its neighbors. (There are no ties.) Let \(i\in\{0,\ldots,a\}\) and \(j\in\{0,\ldots,b\}\) denote the initial counts of positive vertices in the two parts. Write \(P_+(a,b;i,j)\) for the probability of eventual all-positive consensus.

Every trajectory almost surely reaches unanimous consensus. If both partwise initial majorities are positive, \(P_+=1\); if both are negative, \(P_+=0\). If the first part has a positive majority and the second a negative majority, set
\[
 k=b-j,\qquad r=i-u,\qquad s=v+1-j,\qquad t=r+s-1.
\]
Then the exact probability is
\[
 \boxed{P_+(a,b;i,j)
 =\frac{\displaystyle\sum_{\ell=s}^{\min(k,t)}\binom{k}{\ell}\binom{i}{t-\ell}}
 {\displaystyle\binom{i+k}{t}}.}
\]
Binomial coefficients with lower arguments outside their natural range are zero. For the other opposing-majority orientation, color exchange gives
\[
 P_+(a,b;i,j)=1-P_+(a,b;a-i,b-j).
\]
The same absorption probabilities hold for discrete-time scheduling that selects one uniformly random vertex per update.

**Theorem (sharp macroscopic threshold and critical window).** Let \(a_N,b_N\to\infty\) be odd, \(N=a_N+b_N\), and \(a_N/N\to\lambda\in(0,1)\). Take initial counts with \(i_N/a_N\to x\in(1/2,1]\) and \(j_N/b_N\to y\in[0,1/2)\). If \(x+y>1\), then \(P_+\to1\); if \(x+y<1\), then \(P_+\to0\). At the critical line \(y=1-x\), assume additionally
\[
 \sqrt N\left(\frac{i_N}{a_N}+\frac{j_N}{b_N}-1\right)\longrightarrow c\in\mathbb R.
\]
Then
\[
 \boxed{P_+(a_N,b_N;i_N,j_N)\longrightarrow
 \Phi\!\left(\frac{c\sqrt{\lambda(1-\lambda)}}{\sqrt{x(2x-1)}}\right),}
\]
where \(\Phi\) is the standard normal cumulative distribution function. This is a statement for the indicated interior, opposing-majority regime; it does not assert the same normal law at \(x=1/2\) or for vanishing part-size ratios.

**Exact symmetry and minority reversal.** If \(a=b=m\) is odd and \(i+j=m\) with the two local majorities opposed, then \(P_+=1/2\) exactly. A global initial minority can nevertheless win with probability approaching one: for \(\lambda=1/10\), \(x=4/5\), \(y=1/4\), the initial positive fraction tends to \(61/200\), while \(x+y=21/20>1\), so positive consensus has asymptotic probability one.

## Assumptions and scope

The graph is finite, simple, undirected and complete bipartite; both part sizes are **odd**, including the possible size-one case. All initial opinions are visible at time zero. Each vertex has a rate-one clock, independent of all other clocks. Updates take the deterministic strict neighborhood-majority opinion, with no private-signal announcement phase, stubborn vertices, noise, exogenous opinion bias, neighbor sampling, or simultaneous rounds. The first theorem treats every admissible initial configuration with no randomness assumed over the initial opinions. All probabilities concern update-clock randomness only.

The asymptotic theorem holds along any sequences meeting the stated limits; it does not require a balanced graph or independent random initial opinions. The critical assumption specifies an \(N^{-1/2}\) perturbation of the sum of local positive fractions, rather than of the global positive fraction.

## Proof

**1. The two partwise majorities determine updates.** Every vertex in the size-\(a\) part sees precisely the opinions in the other part, and conversely. Each part has odd size, hence a unique majority opinion at all times. When the two majorities agree, subsequent clock rings can only set either vertex to that shared opinion; the majority in either part cannot change sign. Each vertex rings within finite time almost surely, so all agents eventually adopt the common opinion. In particular, initial agreement of partwise majorities fixes the winning color with probability one.

**2. An opposing-majority conflict is a finite first-update race.** Suppose \(i>u\) and \(j\le v\). So long as the partwise majorities remain opposed, positive vertices in the first part turn negative at their first clock ring and stay negative; negative vertices in the second part turn positive at their first ring and stay positive. Their remaining originally negative/positive counterparts already agree with their prescribed opinion and do not affect either majority. After \(r=i-u\) distinct initially positive first-part vertices have rung, the first-part majority becomes negative, forcing negative consensus. After \(s=v+1-j\) distinct initially negative second-part vertices have rung, the second-part majority becomes positive, forcing positive consensus. These two thresholds cannot occur simultaneously because the clock rings are almost surely at distinct times. Thus the winning event is exactly that the \(s\)-th first ring among the \(k=b-j\) initially negative second-part agents precedes the \(r\)-th first ring among the \(i\) initially positive first-part agents.

All \(i+k\) relevant first-ring times are independent identically distributed exponential random variables, so their rank ordering is uniformly random over all \((i+k)!\) permutations. Among its first \(t=r+s-1\) entries, at least \(s\) must belong to the second part precisely when the second-part threshold occurs first. The number of such unordered index subsets is \(\sum_{\ell=s}^{\min(k,t)}\binom{k}{\ell}\binom{i}{t-\ell}\), out of \(\binom{i+k}{t}\) possible subsets. This proves the exact formula. Exchanging positive with negative gives the other opposing-majority orientation. Uniform single-site scheduling yields the same embedded jump chain, by superposition of equal-rate independent Poisson clocks.

**3. Independent exponential hitting-time representation.** In the same orientation, let \(T_A\) be the time of the \(r\)-th first update among the \(i\) initially positive first-part agents, and \(T_B\) the time of the \(s\)-th first update among the \(k\) initially negative second-part agents. The exponential order-statistic spacings representation yields, in distribution,
\[
 T_A=\sum_{h=u+1}^{i}\frac{E_h}{h},\qquad
 T_B=\sum_{h=v+1}^{k}\frac{E'_h}{h},
\]
where all \(E_h,E'_h\) are independent unit-rate exponentials. Thus \(P_+=\Pr(T_B<T_A)\). With \(H_n=\sum_{h=1}^n1/h\) and \(H_0=0\),
\[
 \begin{split}
 \mathbb ET_A&=H_i-H_u,&\quad\mathrm{Var}(T_A)&=\sum_{h=u+1}^i h^{-2},\\
 \mathbb ET_B&=H_k-H_v,&\quad\mathrm{Var}(T_B)&=\sum_{h=v+1}^k h^{-2}.
 \end{split}
\]

**4. Threshold away from criticality.** Write \(x_N=i_N/a_N\) and \(y_N=j_N/b_N\). By harmonic-sum estimates,
\[
 \mathbb E(T_A-T_B)=\log\frac{x_N}{1-y_N}+O(a_N^{-1}+b_N^{-1}),
\]
where the two threshold fractions stay away from \(1/2\) along the indicated sequence. Both variances are \(O(N^{-1})\) when \(a_N/N\to\lambda\in(0,1)\). If \(x+y>1\), the mean difference tends to a strictly positive constant; Chebyshev's inequality gives \(\Pr(T_A>T_B)\to1\). If \(x+y<1\), it tends to a negative constant, giving the opposite limit.

**5. Gaussian critical window.** On \(y=1-x\), the additional scaling implies \(x_N+y_N-1=O(N^{-1/2})\), and hence
\[
 \sqrt N\,\mathbb E(T_A-T_B)\longrightarrow\frac{c}{x}.
\]
Integral comparison for the squared reciprocal sums gives
\[
 N\,\mathrm{Var}(T_A-T_B)
 \longrightarrow\frac{2x-1}{x\lambda(1-\lambda)}.
\]
The summands in the centered difference are independent, with maximal variance \(O(N^{-2})\), total variance of order \(N^{-1}\), and third absolute centered moments totaling \(O(N^{-2})\). Therefore Lyapunov's triangular-array central limit theorem applies. There are no ties between the continuous hitting times, so standardizing and comparing with zero yields the displayed \(\Phi\)-limit.

**6. Symmetry and reversal.** When \(a=b=m\) and \(i+j=m\), the initially positive agents in the first part and the initially negative agents in the second each number \(i\), while the required number of first rings to flip each majority is the same; the independent hitting times are identically distributed. Thus their race is fair. In the stated minority-reversal family, the positive global population fraction tends to \((1/10)(4/5)+(9/10)(1/4)=61/200<1/2\), whereas the sum of local fractions is \(4/5+1/4=21/20>1\). The off-critical threshold proves positive takeover with probability tending to one.

## Verification

The standalone Python program `verify_majority.py` verifies the finite hypergeometric formula with exact rational arithmetic against an independently programmed first-step Markov recurrence for 1,764 configurations on 36 odd part-size pairs through eleven vertices per part. It separately enumerates the complete uniform relevant-clock orderings for 144 smaller configurations, and checks 820 exact symmetry cases through odd size 79. If SciPy is present, it also evaluates large hypergeometric tails in approaching and off-critical regimes and compares the Gaussian limit numerically. These are finite checks; the all-size and asymptotic statements are consequences of the proof above, not of those checks.

Reproduce with `python3 verify_majority.py` in the same folder. No data files, external network access, or proprietary solver are needed; optional SciPy only affects the numerical asymptotic demonstrations. The implementation uses exact integer combinations and fractions for the exhaustive small cases.

## Relationship to prior work

Mohan and Prałat, *Asynchronous Majority Dynamics on Binomial Random Graphs* (first public arXiv version September 9, 2023), analyze learning from initially **unannounced private signals** on random \(G(n,p)\) networks. In contrast, the current result assumes fully visible initial opinions, deterministic odd-degree majority, and a fixed complete bipartite graph; its exact conditional winner law and critical local-fraction window do not follow from their consensus asymptotics.

Amir, Baldasso and Beilin, *Majority dynamics and the median process* (2019), study the same classical independent-clock majority rule, and even use \(K_{3,m}\) in Proposition 3.6 to illustrate a nonmonotone **finite-time marginal** under a specified deterministic update sequence. That example does not give the random-schedule eventual-consensus distribution or the all-size hypergeometric formula and Gaussian crossover proved here. Their complete-graph results address a different topology.

Zehmakan, *Random Majority Opinion Diffusion* (2023), considers **simultaneous** updates and analyzes periodicity, winning sets and cycle graphs. Lesfari, Giroire and Pérennes, *Biased Majority Opinion Dynamics* (2022), impose an exogenous positive opinion bias and start with all-negative agents; they analyze domination and convergence times rather than a neutral, mixed initial condition. Damron and Sen (2019) investigate independent-clock majority on an infinite three-regular tree. None of these inspected results implies the complete-bipartite exact absorption law by a stated theorem or a documented reduction. Related findings about synchronous biclique-majority dynamics likewise concern a different transition kernel.

## Limitations

The proof requires **both parts odd**; even-sized parts introduce tie-breaking that changes the dynamics. It assumes a complete biclique and independently identically rated clocks, and addresses eventual consensus probability rather than expected consensus time. The critical normal law excludes the degenerate boundary \(x=1/2\) and vanishing graph-size ratios. A literature search and full-text comparisons cannot establish absolute publication priority: an equivalent result may be present in specialist sources not identified or inaccessible. No independent external mathematical audit has been performed.

## References

1. D. Mohan and P. Prałat, *Asynchronous Majority Dynamics on Binomial Random Graphs*, arXiv:2309.04691 (first public version 2023-09-09). https://arxiv.org/abs/2309.04691
2. G. Amir, R. Baldasso and N. Beilin, *Majority dynamics and the median process: connections, convergence and some new conjectures*, arXiv:1911.08613 (2019). https://arxiv.org/abs/1911.08613
3. A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1 (2023). https://arxiv.org/html/2302.06760v1
4. H. Lesfari, F. Giroire and S. Pérennes, *Biased Majority Opinion Dynamics: Exploiting Graph k-domination*, IJCAI 2022, DOI:10.24963/ijcai.2022/54. https://ijcai.org/proceedings/2022/54
5. M. Damron and A. Sen, *Zero-temperature Glauber dynamics on the 3-regular tree and the median process*, arXiv:1904.11625 (2019). https://arxiv.org/abs/1904.11625
