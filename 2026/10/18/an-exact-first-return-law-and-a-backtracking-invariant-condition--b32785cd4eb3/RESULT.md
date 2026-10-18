# An exact first-return law and a backtracking-invariant conditional mean on regular trees

## Finding
For the positive-backtracking node2vec walk on the infinite \(d\)-regular tree, \(d\ge3\), let the backtracking weight be \(\alpha>0\) and the ordinary-forward weight \(\gamma>0\). (The triangle weight is irrelevant because trees contain no triangles.) Put
\[
q=\frac{\alpha}{\alpha+(d-1)\gamma},\qquad
r=\frac{\gamma}{\alpha+(d-1)\gamma}.
\]
Start the walk at a root, choose its first neighbor arbitrarily, and let \(T\ge2\) be the first return time to the root, with \(T=\infty\) on escape. The defective generating function of the remaining steps, \(H(z)=\mathbb E[z^{T-1};T<\infty]\), satisfies
\[
z(1-r)H(z)^2-[1+(q-r)z^2]H(z)+qz=0.
\]
It is the unique solution analytic at the origin with \(H(0)=0\). Defining
\[
\Delta(z)=[1+(q-r)z^2]^2-4q(1-r)z^2,
\]
we have the exact expression
\[
H(z)=\frac{1+(q-r)z^2-\sqrt{\Delta(z)}}{2z(1-r)}
\]
for \(0<z\le1\), with its removable value \(H(0)=0\). In particular,
\[
\mathbb P(T<\infty)=\frac{q}{1-r}=\frac{\alpha}{\alpha+(d-2)\gamma},\qquad
\boxed{\mathbb E[T\mid T<\infty]=\frac{2(d-1)}{d-2}}.
\]
The conditional mean is **independent of the backtracking weight** for every finite positive \(\alpha,\gamma\), even though the probability of ever returning ranges strictly between zero and one. The expected total number of root visits, including time zero, equals \(1+\alpha/[(d-2)\gamma]\).

The entire first-return tail is also explicit. Put
\[
\lambda=\sqrt{q(1-r)}+\sqrt{r(1-q)},\qquad
\eta=\left|\sqrt{q(1-r)}-\sqrt{r(1-q)}\right|.
\]
Then \(0\le\eta<\lambda<1\), and, as integers \(m\to\infty\),
\[
\mathbb P(T=2m)\sim
\frac{\sqrt{1-(\eta/\lambda)^2}}{4\sqrt\pi(1-r)}\;
\frac{\lambda^{2m}}{m^{3/2}}.
\]
The decay base \(\lambda=[1-q+\sqrt{q(q+d-2)}]/\sqrt{d-1}\) is strictly increasing in \(q\in(0,1)\). Therefore a stronger backtracking preference slows the exponential tail, despite leaving the return-conditioned mean exactly unchanged.

## Assumptions and scope
The graph is an infinite homogeneous unrooted \(d\)-regular tree, \(d\ge3\). The walk remembers exactly one previous vertex and moves to the previous vertex with relative weight \(\alpha>0\) or to each other neighbor with relative weight \(\gamma>0\). The first move from the root is to an arbitrary neighbor. Each step consumes one unit of discrete time. No claim is made for nonregular graphs, or for the excluded singular endpoints \(\alpha=0\) or \(\gamma=0\). Although the zero-backtracking walk never returns on a tree, the conditional mean above is not defined at that endpoint; at zero forward weight the walk returns deterministically in two steps, so the conditional-mean identity does not extend to that endpoint.

## Proof
Let \(H(z)\) denote the generating function for hitting the predecessor vertex, starting immediately after traversing an oriented edge away from that predecessor. Tree homogeneity makes the same \(H\) apply after every such outward move. Let \(B(z)\) be the generating function of hitting a designated parent of the current vertex when the last step arrived from one of its children. Both series count the **future** steps and assign no mass to escape.

From an outward state, the next step immediately backtracks with probability \(q\); otherwise it moves one generation further with probability \(1-q\). In the latter case it must complete an excursion back to the present vertex (generating function \(H\)) and then return to its parent from an inward state (generating function \(B\)). The strong Markov property for the directed-edge chain and the fact that the underlying graph is a tree give
\[
H=zq+z(1-q)HB.
\]
From the inward state, the parent is selected with probability \(r\), since it is not the vertex just visited. All other neighbors have combined probability \(1-r\); choosing any one of them initiates an outward excursion with generating function \(H\), after which the process is again in an inward state with the same target. Thus
\[
B=zr+z(1-r)HB,\qquad B=\frac{zr}{1-z(1-r)H}.
\]
Substitution and rearrangement yield the stated quadratic. Since its coefficient of \(H\) at \((z,H)=(0,0)\) is \(-1\), the analytic solution at the origin is unique; the negative square-root branch has expansion \(H=qz+O(z^3)\) and hence is the required probability generating function. All strong Markov decompositions remain valid on the event of eventual return because escape contributes zero.

At \(z=1\) the quadratic factors as \((H-1)((1-r)H-q)=0\). As \(q+r<1\) for \(d\ge3\), the probability-generating branch has value \(q/(1-r)<1\). To verify this branch selection without assuming transience, take \(z\uparrow1\) through the explicit root, for which the smaller solution is continuous. Substituting the definitions of \(q,r\) yields the return probability.

Implicit differentiation of the quadratic at \(z=1\), using \(H(1)=q/(1-r)\), gives
\[
\frac{H'(1)}{H(1)}=\frac{1+r-q}{1-r-q}.
\]
Because \(z^{T-1}\) counts steps *after* the first departure, \(\mathbb E[T\mid T<\infty]=1+H'(1)/H(1)=2(1-q)/(1-r-q)\). Finally \(1-q=(d-1)r\) and \(1-q-r=(d-2)r\), proving the invariant conditional mean. After each return, the walk starts another excursion from the root with the same return probability, by tree symmetry and the directed-edge Markov property; the expected number of root visits is the corresponding geometric sum.

For the tail, write \(H(z)=z f(z^2)\). Then \(f(y)=[1+(q-r)y-\sqrt{D(y)}]/[2(1-r)y]\), where
\[
D(y)=(1-\lambda^2 y)(1-\eta^2 y).
\]
The positive square-root singularity of \(f\) occurs at \(y=\lambda^{-2}>1\), with no other singularities on that circle. The square-root coefficient there is \(-\lambda^2\sqrt{1-(\eta/\lambda)^2}/[2(1-r)]\). The standard transfer formula \([y^n](1-y/R)^{1/2}\sim -R^{-n}/(2\sqrt\pi n^{3/2})\) yields the stated asymptotic for \(\mathbb P(T=2m)=[y^{m-1}]f(y)\). The two probability vectors \((q,1-q)\) and \((1-r,r)\) differ because \(q+r<1\); their Hellinger affinity is \(\lambda\), hence \(\lambda<1\). Writing \(r=(1-q)/(d-1)\) gives the alternative formula for \(\lambda\). Its derivative is positive for \(d>2\), since \((2q+d-2)^2>4q(q+d-2)\).

## Verification
The standalone `VERIFY.py` constructs the time-dependent radial directed-edge Markov chain exactly over rational probabilities, with no use of the quadratic formula, and independently compares its first-return coefficients to those obtained by algebraic coefficient recurrence. It also checks the symbolic conditional-mean, return-probability and decay-base identities. Execute with `python VERIFY.py`; it requires only the Python standard library. The run used four degrees and five positive integer weight pairs at 33 nonzero first-return coefficients per case, and reported 720 checks passed. These finite checks corroborate but do not replace the algebraic argument above.

## Relationship to prior work
Avena, Bet, Schroeder and Stegehuis (2026) define the three-weight node2vec walk, prove a recurrence equivalence on regular infinite graphs, and develop directed-edge and directed-wedge representations. Their recurrence criterion decides whether return is certain, but does not supply the first-return distribution or the surprising independence of its conditional mean from \(\alpha\). Tishby, Biham and Katzav (2021) obtain return-time distributions for ordinary simple random walks and discuss the infinite-tree limit; the specialization \(\alpha=\gamma\) is prior mathematics. Arrigo, Higham and Noferini (2021), and Noferini and Quintana (2023), develop backtrack-downweighted walk enumerators and finite-graph generating functions; those results are important broader combinatorial precedents, but the specific infinite-tree probabilistic first-return PGF and its conditional-moment cancellation were not found in the inspected treatments. An unlocated weighted Green-function specialization remains a priority risk.

## Limitations
This proves one-vertex first-return statistics only, not the global mixing behavior, hitting times to arbitrary subsets, or recurrence properties of irregular graphs. The singular limits of the weights do not commute with conditioning and expectation. The first-return generating function could be derivable from more general weighted nonbacktracking resolvent identities; priority has not received independent review. Finite coefficient checks alone do not justify the tail asymptotic, which follows from the proved square-root singularity.

## References
1. L. Avena, G. Bet, L. Schroeder and C. Stegehuis, *node2vec or triangle-biased random walks: stationarity, regularity & recurrence*, arXiv:2604.13681v1 (first publicly submitted 15 April 2026), https://arxiv.org/html/2604.13681v1.
2. I. Tishby, O. Biham and E. Katzav, *Analytical results for the distribution of first return times of random walks on random regular graphs*, arXiv:2106.10449 (2021), https://arxiv.org/abs/2106.10449.
3. F. Arrigo, D. J. Higham and V. Noferini, *A Theory for Backtrack-Downweighted Walks*, SIAM Journal on Matrix Analysis and Applications 42 (2021), 1229–1247, https://doi.org/10.1137/20M1384725.
4. V. Noferini and M. C. Quintana, *Generating functions of non-backtracking walks on weighted digraphs: radius of convergence and Ihara's theorem*, arXiv:2307.14200 (2023), https://arxiv.org/abs/2307.14200.
