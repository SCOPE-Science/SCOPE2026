# Local tournament cycles sharpen the posterior score balance

## Finding

Fix an integer \(n\ge3\). Independently orient each edge of the complete graph on \(n\) labeled vertices in either direction with probability \(1/2\). Fix a vertex \(v\), let \(D\) be its outdegree, and let \(T\) count directed cyclic triangles containing \(v\), counting each three-vertex set once. Put \(N=n-1\), \(m=\lfloor N/2\rfloor\), \(B=\min(D,N-D)\), and \(q_b=b(N-b)\) for \(0\le b\le m\). Then, for all \(0\le d\le N\) and \(0\le t\le d(N-d)\),
\[
\Pr(D=d,T=t)=\binom Nd2^{-N}\binom{d(N-d)}t2^{-d(N-d)}.
\]
Define \(h_b=2\) except \(h_m=1\) when \(N\) is even. For every integer \(0\le t\le q_m\), the exact posterior is
\[
\Pr(B=b\mid T=t)=\frac{w_{b,t}}{\sum_{c=0}^{m}w_{c,t}},\qquad
w_{b,t}=h_b\binom Nb\binom{q_b}t2^{-q_b},
\]
with \(\binom{q_b}t=0\) when \(t>q_b\).

**Conditional likelihood-ratio and variance law.** For consecutive attainable counts, \(B\mid T=t+1\) dominates \(B\mid T=t\) in monotone likelihood-ratio order, hence in stochastic order. The stochastic comparison is strict for each \(0\le t\le q_{m-1}\); for \(q_{m-1}<t<q_m\) both distributions equal the point mass at \(m\). Consequently, the conditional variance \(\operatorname{Var}(D\mid T=t)\) decreases strictly across the same transitions and is constant only at those final transitions. There is exactly one constant final transition when \(n\) is even, and none when \(n\) is odd.

For every \(0\le t\le q_m\),
\[
\mathbb E[D\mid T=t]=\frac N2,
\qquad\operatorname{Var}(D\mid T=t)
=\frac{\sum_{b=0}^{m}(N/2-b)^2w_{b,t}}{\sum_{b=0}^{m}w_{b,t}}.
\]
Thus \(D\) and \(T\) are uncorrelated but not independent. More precisely,
\[
\operatorname{Cov}(D,T)=0,\qquad
\operatorname{Cov}\bigl((D-N/2)^2,T\bigr)=-\frac{N(N-1)}{16}.
\]
At the largest possible cycle count the conditional variance is \(0\) for odd \(n\) and \(1/4\) for even \(n\).

## Assumptions and scope

Only the uniform independent-edge orientation model is considered. The score \(D\) concerns a single **fixed** labeled vertex, not the highest score in the tournament. The count \(T\) includes cyclic triples through that vertex only; it is not the total number of cyclic triples in the tournament. The posterior is conditioned on \(T=t\), an event having positive probability for every integer \(t\in[0,q_m]\). Likelihood-ratio order is understood in the cross-product sense: distributions \(P,Q\) on \(\{0,\ldots,m\}\) satisfy \(P\le_{\rm lr}Q\) when \(P(b)Q(c)\ge Q(b)P(c)\) for all \(b<c\), allowing zero masses.

## Proof

Condition on the orientations of the \(N\) edges incident to \(v\). If \(D=d\), write \(O\) and \(I\) for its sets of outneighbors and inneighbors, of cardinalities \(d\) and \(N-d\). A triple containing \(v\) is cyclic precisely when it consists of \(v\), a vertex \(x\in O\), and \(y\in I\) with the edge \(x\to y\). The \(d(N-d)\) crossing edges are distinct and independently oriented, each favorable with probability \(1/2\). Thus \(T\mid D=d\sim\operatorname{Bin}(d(N-d),1/2)\). Since \(D\sim\operatorname{Bin}(N,1/2)\), multiplication gives the joint law. The posterior expression follows by grouping the symmetric possibilities \(d=b\) and \(d=N-b\).

For fixed \(t<q_m\) and any \(b\) having positive mass at \(t\), the ratio of the unnormalized posterior weights is
\[
\frac{w_{b,t+1}}{w_{b,t}}=\frac{q_b-t}{t+1},
\]
interpreted as zero when \(q_b=t\). The map \(b\mapsto q_b\) is strictly increasing for \(0\le b\le m\), since \(q_{b+1}-q_b=N-2b-1>0\) for \(b<m\). Hence the likelihood ratios increase in \(b\), with the correct zero-mass convention; this is the claimed monotone likelihood-ratio order. It entails first-order stochastic domination. The support at level \(t\) includes a noncentral \(b<m\) exactly when \(t\le q_{m-1}\). In this case \(w_{m-1,t}>0\) and \(w_{m,t}>0\), and strict tilting makes the posterior mass at \(m\) increase. Thus the stochastic comparison is strict. If \(t>q_{m-1}\), only \(b=m\) remains. As \(q_m-q_{m-1}=1\) for even \(N\) and \(2\) for odd \(N\), the constant-transition description follows.

Reversing every edge in the tournament maps \(D\) to \(N-D\) and preserves cyclic triples (equivalently use the exact joint mass). Thus \(\mathbb E[D\mid T=t]=N/2\). Since \(|D-N/2|=N/2-B\), the displayed conditional variance formula follows. The function \(b\mapsto(N/2-b)^2\) is strictly decreasing for \(0\le b\le m\). Therefore the strict conditional stochastic comparisons yield strict decreases in this variance, with equality exactly when both distributions equal \(\delta_m\). The value at \(B=m\) is \(0\) when \(N\) is even and \(1/4\) when \(N\) is odd.

The constant conditional mean gives \(\operatorname{Cov}(D,T)=0\); dependence holds because \(T>0\) forces \(0<D<N\), whereas \(\Pr(D=0)>0\). Put \(X=(D-N/2)^2\). From the binomial law above,
\[
\mathbb E[T\mid D]=\frac{D(N-D)}2=\frac{N^2/4-X}{2}.
\]
Thus \(\operatorname{Cov}(X,T)=-\operatorname{Var}(X)/2\). As \(D-N/2\) is a sum of \(N\) independent centered symmetric \(\pm1/2\) variables, its second and fourth moments are \(N/4\) and \((3N^2-2N)/16\), respectively. Therefore \(\operatorname{Var}(X)=N(N-1)/8\), proving the last identity.

## Verification

The self-contained Python file `verify_tournament.py` independently enumerates **all** tournament edge orientations for \(3\le n\le7\) and computes the pair \((D,T)\) directly from orientations. With exact integer/rational arithmetic, it verifies the full joint law, posterior means, every conditional upper-tail comparison, exact strict/constant transition ranges, and conditional-variance inequalities. The executable passed 681 distinct exact assertion groups over these sizes (including all \(2^{21}=2{,}097{,}152\) orientations for \(n=7\)). This finite replay is not the proof for general \(n\); the proof is the conditional independent-edge argument and exact likelihood-ratio calculation above.

## Relationship to prior work

The literature on tournament scores and directed-cycle counts provides the natural setting. Andersson (1998) studies asymptotic distributions of whole-tournament subgraph counts. Liu (2012, Section 4) studies connectivity among cyclic triangles in **prime deterministic tournaments**; his results concern which cyclic triangles can be linked, not the conditional joint law of one vertex's outdegree and its local cycle count. Sanchez and Kolesnik (2020, Sections 1–3) characterize feasible tournament score and expected score vectors, not finite posterior conditional distributions of triangle counts. The elementary binomial likelihood-ratio principle underlying the proof is a general probabilistic tool and is not claimed as newly discovered. The specifically characterized local score–cycle posterior, its sharp parity-dependent strictness cutoff, and its zero-mean/strict-variance contrast are the claims here.

## Limitations

The theorem requires independent **fair** orientations; correlations between matches or unequal orientation probabilities can invalidate the binomial kernel and the ordering. The result concerns only the rooted local triangle statistic; it neither orders the posterior entire score sequence nor establishes stochastic order for the total number of cyclic triples. The 1998 Andersson article and older triad-count literature could not be inspected in full; an earlier equivalent formulation or implication cannot be ruled out. No independent scientific audit has been performed.

## References

1. P. Andersson, “On the asymptotic distributions of subgraph counts in a random tournament,” *Random Structures & Algorithms* 13 (1998), 249–260. DOI: `10.1002/(SICI)1098-2418(199810/12)13:3/4<249::AID-RSA4>3.0.CO;2-V`; publisher first-public date 1998-12-07.
2. G. Liu, “Various Theorems on Tournaments,” arXiv:1207.0237, 2012-07-01, especially Section 4 on cyclic triangles in prime tournaments. `https://arxiv.org/abs/1207.0237`.
3. M. Sanchez and B. Kolesnik, “The geometry of random tournaments,” arXiv:2009.09322, 2020-09-19. `https://arxiv.org/abs/2009.09322`.
4. K. Nowicki, “Asymptotic normality of triad counts in random digraphs,” *Stochastic Models* (1989), DOI: `10.1080/15326348908807104`.
