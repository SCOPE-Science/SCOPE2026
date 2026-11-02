# Exact rare-seed fixation and Moran comparison for the media-driven q-voter process

## Finding
Fix integers \(q\ge 2\), \(N\ge q+1\), and a media-response probability \(0<p\le1\). On a complete population of \(N\) binary-opinion agents, choose a focal voter uniformly, then choose \(q\) *distinct other agents* uniformly as its influence panel. A unanimous panel sets the focal opinion to its own; a mixed panel sets it to the media-favored opinion \(+\) with probability \(p\) and otherwise leaves the focal opinion unchanged. The all-minus and all-plus configurations are absorbing. Let \(\rho_{N,q,p}(m)\) be the probability of ultimate all-plus consensus from exactly \(m\) plus opinions, for \(1\le m<N\).

**Theorem (finite-population comparison and rare-seed limit).** If \(pq>1\), then, for every permitted \(N,m\),
\[
\rho_{N,q,p}(m)\ge\frac{1-(pq)^{-m}}{1-(pq)^{-N}}.
\]
For each fixed integer \(m\ge1\), holding \(q,p,m\) fixed while \(N\to\infty\) through integers \(N\ge\max(q+1,m+1)\),
\[
\lim_{N\to\infty}\rho_{N,q,p}(m)=
\begin{cases}
0,&0<p\le 1/q,\\
1-(pq)^{-m},&1/q<p\le1.
\end{cases}
\]
The first inequality is a finite-population Moran-style lower bound with effective advantage \(pq\), and its right-hand side is asymptotically sharp for each fixed seed count. At maximal media response \(p=1\), a single seed consequently has limiting consensus probability \(1-1/q\), not one.

## Assumptions and scope
The panel is sampled *without replacement* from the \(N-1\) nonfocal agents; opinions are updated asynchronously, one focal voter per step. In a mixed panel media influence favors plus only; there is no spontaneous change to minus. Panel size \(q\) is fixed as \(N\to\infty\). The number \(m\) of initial plus agents is fixed and does not scale with population size. The full state is exchangeable, so the number of plus opinions \(X_t\in\{0,1,\dots,N\}\) is a Markov chain with nearest-neighbor jumps or holding. The theorem does not concern other panel sampling conventions, heterogeneous networks, or time-varying media.

## Proof
Define \((a)_q=a(a-1)\cdots(a-q+1)\) if \(a\ge q\) and \((a)_q=0\) otherwise. At state \(X_t=k\), set \(n=N-k\), \(T=(N-1)_q\). Direct enumeration of focal opinions and ordered distinct panels gives upward and downward transition probabilities
\[
U_k=\frac{n}{NT}\left[(k)_q+p\big(T-(k)_q-(n-1)_q\big)\right],\qquad
D_k=\frac{k(n)_q}{NT}.
\]
In particular, \(U_k>0\) for \(0<p\le1\) and every \(1\le k<N\), and \(D_1=1/N\), \(U_1=pq/N\). The chain absorbs almost surely in either \(0\) or \(N\).

**Mixed-panel injection.** For a minus focal voter, the mixed ordered panels include all panels containing *exactly one plus*: there are \(qk(n-1)_{q-1}\) such panels. Thus
\[
T-(k)_q-(n-1)_q\ge qk(n-1)_{q-1},
\]
and, using \(n(n-1)_{q-1}=(n)_q\),
\[
U_k\ge\frac{p n}{NT}qk(n-1)_{q-1}=pq\,D_k.
\]
This remains valid when \(n<q\), where both terms on the right of the panel-count inequality vanish. The constant \(pq\) is sharp in the one-step comparison because equality holds at \(k=1\).

For \(s=pq>1\), the process \(s^{-X_t}\) is a bounded supermartingale: conditional on \(X_t=k\), its expected increment equals
\[
s^{-k}(1-s^{-1})(sD_k-U_k)\le0.
\]
At the almost-sure finite absorption time, optional stopping gives \(1-\rho_{N,q,p}(m)+s^{-N}\rho_{N,q,p}(m)\le s^{-m}\). Rearrangement establishes the stated finite-population comparison.

For the limit, put \(R_{N,k}=D_k/U_k\), \(P_{N,0}=1\), and \(P_{N,j}=\prod_{k=1}^{j}R_{N,k}\). Solving the one-dimensional harmonic equation for the fixation probability gives the exact identity
\[
\rho_{N,q,p}(m)=\frac{\sum_{j=0}^{m-1}P_{N,j}}{\sum_{j=0}^{N-1}P_{N,j}}.
\]
Indeed the increments of the harmonic function obey \(U_k(h_{k+1}-h_k)=D_k(h_k-h_{k-1})\), with \(h_0=0,h_N=1\). For every *fixed* \(k\ge1\), the explicit transitions yield \(NU_k\to pqk\), \(ND_k\to k\), hence \(R_{N,k}\to r=(pq)^{-1}\) and \(P_{N,j}\to r^j\) for each fixed \(j\).

When \(pq>1\), the injection gives \(0\le P_{N,j}\le r^j\), taking \(P_{N,j}=0\) for \(j\ge N\). Dominated convergence for the summable geometric sequence gives denominator \(\to(1-r)^{-1}\) and numerator \(\to(1-r^m)/(1-r)\), producing \(1-r^m\). When \(0<pq\le1\), for every fixed integer \(J\ge m\), the denominator is at least its first \(J+1\) terms, whose limit is \(\sum_{j=0}^Jr^j\), while the numerator tends to \(\sum_{j=0}^{m-1}r^j\). Letting \(J\to\infty\) forces the fixation probability to zero because \(r\ge1\). This proves all claims.

## Verification
The standalone \`verify_finite_chain.py\` independently enumerates focal voters and unordered distinct committees and compares the resulting rational transition probabilities to the stated closed forms in \(420\) configurations. It checks \(U_k\ge pqD_k\) and equality at one seed and computes exact fixation probabilities from the birth-death product formula. At \(q=5\), \(p=2/5\), and two plus seeds, the exact probabilities at population sizes \(40,200,800\) are approximately \(0.784907778\), \(0.757362400\), and \(0.751865833\), consistent with the proved limit \(3/4\). Such finite computations do not prove the limit; the proof above is analytic. Run with \`python3 verify_finite_chain.py\` (Python standard library only).

## Relationship to prior work
Muslim, Anugraha NQZ and Khalif (arXiv:2305.06053) introduce precisely the media-on-nonunanimity rule and analyze macroscopic drift, approximate media thresholds, and exit probabilities at initial *positive fractions*. Their paper already identifies the scale \(p\approx1/q\); that threshold scale is **not claimed as new here**. Their numerical and diffusion analyses do not state a fixed-finite-seed large-population fixation limit or the exact all-population Moran inequality from a distinct-panel counting argument. Their displayed finite-size transition formulas use a different panel/focal sampling normalization in the media term; our sampling convention is explicitly fixed above, rather than silently equating the two finite chains.

Azhari and Muslim (arXiv:2305.06051) investigate the same five-panel media mechanism numerically, without a fixed-seed fixation law. Doniec, Mullick, Sen and Sznajd-Weron (arXiv:2502.10172) include the media model as a special case of a broader asymmetric process and provide a finite-state Markov-chain approach to exit probabilities; the inspected calculations do not extract this rare-seed limit or an all-\(N\) Moran comparison. Standard birth-death potential formulas and branching-process survival probabilities provide techniques, not a prior theorem establishing the model-specific sharp inequality and limit.

## Limitations
The initial plus count must remain fixed as \(N\) grows. A fixed positive initial proportion is a genuinely different asymptotic regime. The result does not imply certainty of plus consensus for finite populations, even at maximal media influence. For \(p=0\), the rates are degenerate below panel size and the stated harmonic-ratio proof does not apply without modification, so the theorem states \(p>0\). Originality rests on the located literature, not exhaustive coverage of all possible records. No independent audit or validation is claimed.

## References
- R. Muslim, R. Anugraha NQZ and M. A. Khalif, *Mass media and its impact on opinion dynamics of the nonlinear q-voter model*, arXiv:2305.06053, first public version 2023-05-10, https://arxiv.org/abs/2305.06053.
- Azhari and R. Muslim, *The external field effect on the opinion formation based on the majority rule and the q-voter models on the complete graph*, arXiv:2305.06051, first public version 2023-05-10, https://arxiv.org/abs/2305.06051.
- M. Doniec, P. Mullick, P. Sen and K. Sznajd-Weron, *Modeling biases in binary decision-making within the generalized nonlinear q-voter model*, arXiv:2502.10172, first public version 2025-02-14, https://arxiv.org/abs/2502.10172.
- J. Civitarese, *External fields, independence, and disorder in q-voter models*, Phys. Rev. E **103** (2021) 012303, https://doi.org/10.1103/PhysRevE.103.012303 (different skepticism/noise mechanism; abstract inspected).
