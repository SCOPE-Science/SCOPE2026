# Balanced Kemeny optima versus star mixing optima in edge-resampled bipartite walks

## Finding

**Theorem (all orders and edge availabilities).** Let \(n\ge4\), \(1\le a\le b\), \(a+b=n\), and \(0<p<1\). At every discrete time, independently retain each possible edge of \(K_{a,b}\) with probability \(p\). A walker chooses uniformly among presently available neighbors, or stays when none are available. Put \(r=1-p\) and \(q_k=1-r^k\).

The walker has Kemeny's constant (stationary-target mean first-hitting time)
\[
\mathcal K_{a,b}(p)=\frac{a-1}{q_b}+\frac{b-1}{q_a}+\frac{1}{q_a+q_b},
\]
which, at any fixed \(n\) and \(p\), is **strictly minimized by the balanced bipartition**, \(a=\lfloor n/2\rfloor\), \(b=\lceil n/2\rceil\).

The absolute nontrivial eigenvalue radius, by contrast, is
\[
\rho_{a,b}(p)=\max\{r^a,\,1-r^a-r^b\}.
\]
Writing \(m=\lfloor n/2\rfloor\), it is minimized at \(a=m\) if \(2r^m+r^{n-m}\ge1\), and at \(a=1\) if \(2r+r^{n-1}\le1\). Otherwise, the only possible integer minimizers are the two integers adjacent to the unique \(a_*\in(1,m)\) satisfying \(2r^{a_*}+r^{n-a_*}=1\), and their displayed exact radii decide which wins (both may tie).

In particular, when \(p=1/2\) and \(n\ge5\), the **star uniquely minimizes the spectral radius**, although the balanced graph uniquely minimizes Kemeny's constant. For \(n=2m\) with \(m\ge3\), the standard worst-start total-variation mixing time obeys
\[
 t_{\mathrm{mix}}^{K_{m,m}}(1/4)\ge
 \frac{\log2}{-\log(1-2^{1-m})}\sim (\log2)\,2^{m-1},
 \qquad
 t_{\mathrm{mix}}^{K_{1,2m-1}}(1/4)\le3.
\]
At the same time, \(\mathcal K_{m,m}(1/2)\sim 2m\) while \(\mathcal K_{1,2m-1}(1/2)\sim4m\). Thus the Kemeny-optimal bipartition has exponentially slower worst-case mixing than the spectral-optimal star while its stationary-target mean hitting time is asymptotically half as large.

## Assumptions and scope

The underlying graph is the fixed finite undirected complete bipartite graph \(K_{a,b}\). Edge states are mutually independent both across edges and across time; a fresh snapshot is drawn immediately before each move. Edges are chosen **after** the current snapshot is revealed. No neighbor being available means one time step of holding in place. Walks start from any prescribed vertex. Kemeny's constant is \(\sum_y\pi(y)\mathbb E_x[T_y]\), where \(T_x=0\) if the starting vertex is already the target, and does not depend on \(x\). The mixing time is the smallest integer \(t\) for which every starting vertex has total-variation distance at most \(1/4\) from stationarity.

The positivity restriction \(0<p<1\) is essential to irreducibility and aperiodicity. At \(p=0\) the chain is reducible; at \(p=1\) it is periodic, all bipartitions have \(\mathcal K=n-3/2\), and the strict optimization and finite mixing-time statements above are not asserted. The spectral-radius optimizer is understood up to exchanging part names.

## Proof

**Step 1: collapse the independent edge snapshots.** If the current vertex has \(d\) possible neighbors, each neighbor is selected with the same unconditional probability, and a move occurs iff at least one of its \(d\) edges is present. Consequently each specified neighbor is chosen with probability \((1-r^d)/d\), while the holding probability is \(r^d\). With \(A\) the part of size \(a\), and \(B\) the part of size \(b\), the transition matrix in block form is
\[
P=\begin{pmatrix}
 r^b I_a & (q_b/b)J_{a\times b}\\
 (q_a/a)J_{b\times a} & r^a I_b
\end{pmatrix}.
\]
Here \(J\) is an all-ones rectangular matrix. Detailed balance across each possible edge shows that stationary total masses on \(A,B\) are \(q_a/(q_a+q_b)\) and \(q_b/(q_a+q_b)\), respectively, with uniform mass within each part.

**Step 2: exact spectrum and stationary-target hitting time.** On the zero-sum subspace supported on \(A\), the eigenvalue is \(r^b\), with multiplicity \(a-1\); analogously \(r^a\) has multiplicity \(b-1\). On part-constant vectors the remaining eigenvalues are \(1\) and \(r^a+r^b-1\). Since the chain is finite, irreducible and aperiodic, the standard spectral identity for Kemeny's constant, \(\mathcal K=\sum_{\lambda\ne1}(1-\lambda)^{-1}\), gives the displayed formula. As \(a\le b\), the absolute nontrivial eigenvalue radius is \(\max\{r^a,1-r^a-r^b\}\), with no omitted eigenvalue because \(b\ge2\). This also confirms the stationary distribution and correct multiplicities at \(a=1\).

**Step 3: strict Kemeny balance.** Extend \(a,b>0\) continuously with \(a+b=n\), and write \(f(x)=1/(1-r^x)\). This function is positive, strictly decreasing and strictly convex. For \(a>b\), the derivative with respect to \(a\) of \((a-1)f(b)+(b-1)f(a)\), with \(b=n-a\), equals
\[
f(b)-f(a)+(a-1)(-f'(b))-(b-1)(-f'(a))>0,
\]
because \(a-1\ge b-1\ge0\) in the region containing all admissible integer partitions, and \(-f'(b)>-f'(a)>0\). The remaining term \(1/(2-r^a-r^b)\) also strictly increases for \(a>b\), as its denominator strictly decreases there. Hence every unit shift away from the most balanced allowed integer partition strictly increases \(\mathcal K\).

**Step 4: spectral minimizer.** For real \(a\in[1,m]\), the first branch \(r^a\) strictly decreases, while the second branch \(1-r^a-r^{n-a}\) strictly increases. Which branch dominates is determined by the strictly decreasing function \(F(a)=2r^a+r^{n-a}-1\). If \(F(m)\ge0\) the first branch dominates throughout and the balanced part is optimal; if \(F(1)\le0\) the second dominates throughout and the star is optimal. Otherwise the real-valued maximum decreases to its unique crossover and increases afterward. An integer minimizer can therefore only be one of the adjacent integers, whose exact radii determine any tie.

**Step 5: opposite mixing performance at half availability.** At \(p=1/2\) and \(n\ge5\), every \(a\ge2\) satisfies
\[
\rho_{a,n-a}\ge 1-2^{-a}-2^{-(n-a)}
\ge 1-\tfrac14-2^{-(n-2)}\ge\tfrac58>\tfrac12,
\]
where the middle inequality uses the increase of the second branch on \(1\le a\le n/2\). The star, however, has radius \(1/2\), proving unique spectral optimality.

For a start in \(A\), the probability to lie in \(A\) at time \(t\) is \(\pi(A)+(1-\pi(A))\lambda^t\), where \(\lambda=r^a+r^b-1\). Therefore
\[
 d_{\mathrm{TV}}(P^t(x,\cdot),\pi)\ge (1-\pi(A))|\lambda|^t.
\]
On a balanced graph \(\pi(A)=1/2\), and at half availability \(\lambda=-(1-2^{1-m})\), yielding the claimed exponential lower bound. Conversely, decomposing the point mass \(\delta_x\) into its uniform-within-part component and its within-part contrast shows, for every starting vertex,
\[
 d_{\mathrm{TV}}(P^t(x,\cdot),\pi)
 \le |\lambda|^t+\max\{r^a,r^b\}^{t}\le2\rho^t.
\]
For the star at \(p=1/2\), \(\rho=1/2\), so at \(t=3\) the distance is at most \(1/4\). Finally the exact Kemeny formula gives
\[
 \mathcal K_{m,m}(1/2)=\frac{2m-3/2}{1-2^{-m}},
 \qquad
 \mathcal K_{1,2m-1}(1/2)=4m-4+\frac{1}{3/2-2^{-(2m-1)}},
\]
and the two stated asymptotics follow.

## Verification

Run `python3 verify.py` from this directory; only the Python standard library is required. The program constructs the full rational transition matrix independently of the spectral formula, solves all finite first-hitting-time linear systems, recomputes the stationary-target expectation from each source, tests eigenmodes and exact time-step distributions, checks the balancing and spectral optimizer rules over a parameter grid, and verifies the half-availability boundary. It reports 12,354 checked exact-rational comparison units. These finite checks are consistency checks, not a substitute for Steps 1–5, which cover all integer graph sizes and all real \(0<p<1\).

## Relationship to prior work

Lamprou, Martin and Spirakis introduced the edge-uniform evolving-graph RWA model and derived the general single-neighbor transition probability \((1-(1-p)^d)/d\) in their Section 4.2; that reduction is credited here. Their work focuses on cover-time bounds rather than a bipartite Kemeny–spectral optimizer conflict. Kemeny's spectral formula is classical. Breen and collaborators study Kemeny's constant for **nonbacktracking** walks on static graphs, including biregular graphs; their walk has a different state space and dynamics. Faught, Kempton and Knudson study Kemeny calculations and Braess edges in static graphs. The claimed contribution here is the exact joint classification of Kemeny and spectral-radius optimizers **for the edge-resampled RWA chain**, together with its exponential-versus-constant mixing separation at a common edge availability.

## Limitations

No claim is made for edge states with temporal memory, unequal edge-retention probabilities, the choose-before-reveal random walk, general multipartite graphs, or minimization of the **exact** total-variation mixing time at all parameters (only the absolute spectral radius is completely optimized). The two metric optimizers need not coincide. The originality analysis is based on the inspected available literature and indexed records; absence of an indexed exact claim cannot certify historical priority. The independent mathematical audit has not been performed.

## References

1. I. Lamprou, R. Martin and P. Spirakis, *Cover Time in Edge-Uniform Stochastically-Evolving Graphs* (2017), arXiv:1702.05412, first public 2017-02-17; full accessible author manuscript: https://livrepository.liverpool.ac.uk/3020375/1/arxiv-may.pdf.
2. J. Breen, N. Faught, C. Glover, M. Kempton, A. Knudson and A. Oveson, *Kemeny's constant for non-backtracking random walks* (2022), arXiv:2203.12049.
3. N. Faught, M. Kempton and A. Knudson, *A 1-Separation Formula for the Graph Kemeny Constant and Braess Edges* (2021), arXiv:2108.01061.
