# Exact self-influence staircase for continuous-time weighted-median opinion dynamics

## Finding
Consider the continuous-time weighted-median opinion dynamics on a homogeneous complete network with \(n\ge 2\) agents. Each agent assigns weight \(a\in[0,1)\) to its own opinion and equal weight \(b=(1-a)/(n-1)\) to each other agent. Resolve nonunique weighted medians by selecting the median closest to the focal agent's own opinion. For arbitrary real initial opinions, let \(z_1\le\cdots\le z_n\) be their order statistics. Define
\[
q=\min\!\left\{n-1,\left\lfloor\frac{n-1}{2(1-a)}\right\rfloor\right\},\quad L=n-q,\quad R=q+1.
\]
For every \(t\ge0\), the ordered opinions are given by the following exact formulas.

**Stationary-core regime (\(L\le R\)).** For each rank \(i\), write \(j=\max\{L,\min\{i,R\}\}\). Then
\[
x_{(i)}(t)=z_j+(z_i-z_j)e^{-t}.
\]
Thus the agents of ranks \(L,\ldots,R\) stay fixed, all lower ranks converge to \(z_L\), and all upper ranks converge to \(z_R\). For pairwise-distinct initial opinions, the limiting configuration has exactly \(R-L+1=2q+2-n\) distinct opinion values.

**Interacting-central-pair regime (\(L>R\)).** Necessarily \(n=2m\), \(a<1/n\), and \(L=m+1\), \(R=m\). Put \(c=(z_m+z_{m+1})/2\), \(d=(z_{m+1}-z_m)/2\). Then
\[
x_{(i)}(t)=\begin{cases}
c+(z_i-c+d)e^{-t}-d e^{-2t},&1\le i\le m,\\
c+(z_i-c-d)e^{-t}+d e^{-2t},&m+1\le i\le2m.
\end{cases}
\]
In particular all opinions converge to \(c\), and the central gap is exactly \(2d e^{-2t}\).

It follows that the model reaches consensus from **every** initial opinion vector precisely when
\[
0\le a<\begin{cases}1/n,&n\text{ even},\\ 2/(n+1),&n\text{ odd}.\end{cases}
\]
When \(n\) is odd the consensus equals the initial middle order statistic; when \(n\) is even and \(a<1/n\), it equals the arithmetic mean of the two central order statistics. At each weight threshold \(a=1-(n-1)/(2k)\) at which \(q\) increases to \(k\), the generic limiting cluster count increases by two (the first even transition is from one to two), creating a finite, explicit staircase of polarization as self-influence rises.

## Assumptions and scope
The full, fixed influence matrix has entries \(w_{ii}=a\), \(w_{ij}=b\) for \(i\ne j\). An admissible weighted median \(v\) is one of the current opinion values with total weight strictly below \(v\) at most \(1/2\), and total weight strictly above \(v\) at most \(1/2\). The chosen median minimizes its distance from the focal opinion among such admissible values. The differential equation is \(\dot x_i(t)=\operatorname{Med}_i(x(t);W)-x_i(t)\). Time has the unit relaxation rate specified in this equation. The result holds for every integer \(n\ge2\), every \(0\le a<1\), every initial vector in \(\mathbb R^n\), including repeated opinions, and all real \(t\ge0\). Statements about an exact number of distinct limiting values assume pairwise distinct initial opinions.

## Proof
**1. Median-rank calculation.** First suppose \(x_1<\cdots<x_n\). For a fixed focal rank \(i\), the focal value has weight \(a\) and every other rank has weight \(b\). If a candidate rank \(j\) lies below \(i\), its weight strictly above is \(a+(n-j-1)b\) and strictly below is \((j-1)b\); if it lies above \(i\), its weight strictly below is \(a+(j-2)b\) and strictly above is \((n-j)b\). If \(j=i\), these two weights are \((i-1)b\) and \((n-i)b\). An admissible candidate has both weights at most \(1/2\). Since \(q=\min\{n-1,\lfloor1/(2b)\rfloor\}\), a focal rank in the nonempty interval \([L,R]\) has its own opinion admissible. Below \(L\), all its admissible medians lie weakly above rank \(L\), and rank \(L\) is admissible; above \(R\), the symmetric assertion holds. Nearest-own tie-breaking therefore gives
\[
\operatorname{Med}_{(i)}(x;W)=x_{(\max\{L,\min\{i,R\}\})}\qquad(L\le R).
\]
If \(L>R\), the integer definitions force \(n=2m\), \(q=m-1\); exactly the two central ranks straddle the half-weight balance. Directly applying the same two half-weight tests shows
\[
\operatorname{Med}_{(i)}(x;W)=\begin{cases}x_{(m+1)},&i\le m,\\x_{(m)},&i\ge m+1.\end{cases}
\]
These statements include equality at the weight boundaries, because candidates are admissible with half-weight on either side and the focal value wins whenever admissible.

**2. Solve and retain the ranks.** In the stationary-core regime, ranks \(L,\ldots,R\) have zero derivatives. Each outside rank obeys \(\dot x_{(i)}=z_j-x_{(i)}\) with the fixed \(j\) from the preceding step, giving the first formula. Strict ordering is maintained at each finite time: differences on any exterior side scale by \(e^{-t}\), while each fixed core value retains its place. Therefore the presumed rank-to-median map remains valid for the entire trajectory.

In the central-pair regime, the two central coordinates satisfy \(\dot x_{(m)}=x_{(m+1)}-x_{(m)}\) and \(\dot x_{(m+1)}=x_{(m)}-x_{(m+1)}\), so they equal \(c\mp d e^{-2t}\). The other ranks solve the forced linear equations toward the opposite central coordinate, yielding the displayed two-rate formulas. Differences between adjacent coordinates on the same side scale by \(e^{-t}\), while the central gap equals \((z_{m+1}-z_m)e^{-2t}>0\). Consequently the rank ordering never changes, and the formulas solve the full nonlinear differential equation globally for strictly ordered initial opinions.

**3. Ties and uniqueness.** Perturb any weakly ordered initial tuple into strictly ordered tuples converging to it. The median operator with nearest-own tie-breaking is nonexpansive in supremum norm, as proved for this exact model in Han et al. (Theorem 8 of the later full-text version); hence its vector field is globally Lipschitz, and solutions depend continuously on initial data. Taking the perturbations to zero in the explicit formulas proves the same formulas for arbitrary ties. A particular labeling of equal values makes no difference because their trajectories coincide. Thus no implicit genericity assumption is needed in either formula.

**4. Exact transition boundaries.** A central-pair regime exists exactly for even \(n\) with \(a<1/n\); for odd \(n\), \(L\le R\) always. When \(n=2m+1\), \(q=m\) exactly for \(a<2/(n+1)\), and only rank \(m+1\) is fixed; for larger \(a\), multiple fixed ranks permit distinct limiting opinions. When \(n=2m\), the central-pair regime gives universal consensus if \(a<1/n\), whereas at and above \(1/n\) the stationary core has at least two ranks. Pairwise distinct initial opinions show the necessity of the strict inequalities. Each further increase of \(q\) adds one fixed rank on each side of the core, so the limiting-profile staircase and generic cluster counts follow. The formulas also settle all parameter endpoints in the stated range.

## Verification
The standalone \`verify.py\` script uses Python's exact rational arithmetic, including every tested self-weight, opinion value and test value of \(u=e^{-t}\). It computes the true weighted median independently by enumerating all distinct observed values and checking the two half-weight inequalities. It compares that median minus the proposed opinion against the exact time derivative \(-u\,d x/du\) of the proposed formula, also checking preservation of order. Executing \`python3 verify.py\` passed 1,755 rational initial profiles (both strict and tied) and 56,160 individual median/ODE checks. This finite evidence does not replace the all-parameter proof above.

## Relationship to prior work
Han, Hendrickx, Chen and Mei's continuous-time weighted-median paper (first publicly posted 25 April 2024 under arXiv:2404.16318; inspected full-text revision dated 26 November 2025) introduces precisely the weighted-median differential equation and tie rule, proves existence, equilibria and global convergence, and gives network-structural consensus conditions. Those general results establish that trajectories converge, but they do not specify the rankwise trajectories, the exact limiting choice of central order statistics, the sharp dependence on homogeneous self-weight, or the finite staircase of limiting cluster counts derived here. Earlier work by Mei et al. studies a discrete-time, asynchronous weighted-median process with different trajectories; synchronous self-appraisal median models also use different evolution equations. The result here is a finite-network exact solution of a natural homogeneous specialization, not a claim that weighted-median opinion dynamics or consensus phenomena themselves are new.

## Limitations
The solution requires homogeneous off-diagonal weights and the stated nearest-own median rule; arbitrary network influence matrices need not preserve ranks or admit this explicit solution. Differences at finite times and terminal clusters are mathematical properties of the specified deterministic model, not empirical forecasts. Generic exact cluster counts may merge when initial opinions tie. The cited full texts and targeted mathematical-result searches did not reveal the formulas, but unpublished, unindexed or otherwise unseen equivalent results remain possible. No independent scientific validation has been performed.

## References
1. Y. Han, J. M. Hendrickx, G. Chen, W. Mei, *Modeling, Analysis, and Control of Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318, first version 25 April 2024; full-text revision 26 November 2025. https://arxiv.org/html/2404.16318v3 ; https://arxiv.org/abs/2404.16318
2. W. Mei, J. M. Hendrickx, G. Chen, F. Bullo, F. Dörfler, *Convergence, Consensus and Dissensus in the Weighted-Median Opinion Dynamics*, arXiv:2212.08808, 2022 (discrete-time asynchronous update rule). https://arxiv.org/abs/2212.08808
3. L. Mohr, P. G. Hjorth, M. A. Porter, *A Weighted-Median Model of Opinion Dynamics on Networks*, arXiv:2406.17552, June 2024; later journal title *Long-Time and Short-Time Dynamics in a Weighted-Median Opinion Model on Networks*, 2026. https://arxiv.org/abs/2406.17552
