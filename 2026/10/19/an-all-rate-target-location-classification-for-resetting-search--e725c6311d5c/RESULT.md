# An all-rate target-location classification for resetting search on bridge-barbells

## Finding
For integers \(m\ge3\), \(n\ge2\), form a barbell graph from a complete graph on \(m\) vertices and one on \(n\) vertices, with a single edge joining designated bridge vertices. A particle starts at a left nonbridge vertex and, at rate one *along every edge*, jumps to its neighbor. Independently, at Poisson rate \(r\ge0\), it instantly returns to the starting vertex. The process stops on first arrival at a target vertex other than the start.

The expected hitting time \(M_y(r)\), for every target and every reset rate, obeys the following complete target-location classification. Write
\[
D(r)=m+(mn+m+n+1)r+(m+n+2)r^2+r^3.
\]

* **Left bridge endpoint:** \(M_y(r)=1\), independent of \(r\).
* **Another left nonbridge vertex:**
\[
M_y(r)=1+\frac{n+r}{D(r)};\qquad M_y'(r)<0\quad(r\ge0).
\]
* **Right bridge endpoint:** \(M_y(r)=m+1+r\), strictly increasing.
* **A right nonbridge vertex:**
\[
M_y(r)=r^2+(m+3)r+2m-n+4+\frac{(n-2)(n-m)}{n+r};\qquad M_y'(r)>0\quad(r\ge0).
\]
The formulas at \(r=0\) are continuous limits. The source itself is not a target.

In particular, a reset is always beneficial for finding another nonbridge vertex in the starting clique, never beneficial for reaching the other clique, and immaterial for reaching the starting clique's bridge endpoint. The maximal relative time reduction for a same-clique nonbridge target is exactly \(n/(m+n)\), approaching unity with increasing remote-clique size at fixed \(m\). There is no optimal finite positive reset rate for any target class.

## Assumptions and scope
The graph is the union of two disjoint complete simple graphs, joined by exactly one edge. The source is a left nonbridge vertex. Edge *rates*, not total vertex jump rates, are equal to one: at a vertex of degree \(d\), the clock of real moves runs at total rate \(d\). A reset is an independent Poisson event of rate \(r\), directed to the same starting vertex, even when the particle is already there. The target is absorbing on first arrival. No claim is made for normalized degree-one-per-vertex walks, non-Poisson restarts, or barbells having a nontrivial connecting path.

## Proof
Let \(\tau_y\) be the unreset hitting time and set \(\phi_y(s)=\mathbb E[e^{-s\tau_y}]\) for \(s\ge0\). The finite connected walk hits the target almost surely. If \(T_y(r)\) is its first-passage time after instantaneous Poisson resets of rate \(r>0\), renewal over independent attempts gives
\[
M_y(r)=\mathbb E[T_y(r)]=\frac{1-\phi_y(r)}{r\phi_y(r)}.
\]
This follows because the probability of success before an independent exponential reset is \(\phi_y(r)\), and one attempt has mean duration \((1-\phi_y(r))/r\). Both quantities are positive and finite. The limit at \(r=0\) follows analytically.

To compute each Laplace transform, lump vertices by symmetry relative to the target and source. All vertices inside a lump have identical total rates to any other lump, hence the lumped process has exactly the required hitting-time distribution. Internal jumps do not change the lump. If \(Q\) is the transient generator and \(k\) is the vector of rates into the absorbing target, its Laplace vector is \((sI-Q)^{-1}k\), evaluated at the initial lump.

For a *different left nonbridge* target, order the four transient lumps as \(A\) (left nonbridge, not target), \(B\) (left bridge), \(C\) (right bridge), and \(D\) (right nonbridge). Then
\[
Q_{\rm near}=\begin{pmatrix}
-2&1&0&0\\
m-2&-m&1&0\\
0&1&-n&n-1\\
0&0&1&-1
\end{pmatrix},\qquad k_{\rm near}=\begin{pmatrix}1\\1\\0\\0\end{pmatrix}.
\]
For a *right nonbridge* target, use the corresponding four lumps, but with the target omitted on the right:
\[
Q_{\rm far}=\begin{pmatrix}
-1&1&0&0\\
m-1&-m&1&0\\
0&1&-n&n-2\\
0&0&1&-2
\end{pmatrix},\qquad k_{\rm far}=\begin{pmatrix}0\\0\\1\\1\end{pmatrix}.
\]
The upper left entries encode the actual rates to targets as exits; for example the first row of \(Q_{\rm near}\) has a further target-exit rate of one, which is not shown off-diagonally. In both cases the initial lump is \(A\).

Define
\[
\begin{aligned}
H_c(s)&=c+(mn+2m+2n+1)s\\
&\quad +(mn+2m+2n+4)s^2+(m+n+3)s^3+s^4.
\end{aligned}
\]
Direct matrix elimination gives the exact transforms
\[
\phi_{\rm near}(s)=\frac{D(s)}{H_m(s)},\qquad
\phi_{\rm far}(s)=\frac{n+s}{H_n(s)}.
\]
Substitution in the renewal identity and elementary division prove the displayed near and far formulas, including their endpoints.

For the **right bridge** as target, only the transient left-nonbridge and left-bridge lumps remain. Their subgenerator is
\[
\begin{pmatrix}-1&1\\m-1&-m\end{pmatrix}
\]
with target-exit rates \((0,1)^{\mathsf T}\). Consequently \(\phi(s)=1/[1+(m+1)s+s^2]\), and renewal gives \(M(r)=m+1+r\). For the **left bridge**, from every nonbridge left vertex the hazard of entering this target is precisely one. The resets return to the same nonbridge class and never change this hazard; therefore the hitting time is \(\operatorname{Exp}(1)\) and has expectation one, independently of \(r\).

For strict monotonicity in the near case put \(a=mn+m+n+1\), \(b=m+n+2\). Differentiation yields
\[
D(r)^2 M'_{\rm near}(r)
=m-na-2nb\,r-(b+3n)r^2-2r^3<0.
\]
Indeed \(m-na<0\) under the stated integer bounds and every remaining coefficient is negative. In the far case,
\[
M'_{\rm far}(r)=2r+m+3-\frac{(n-2)(n-m)}{(n+r)^2}>0.
\]
If the numerator in the fraction is nonpositive, positivity is immediate; if it is positive, \(n>m\) and \(0<(n-2)(n-m)<n^2\), so the fraction is less than one. The remaining two classes are immediate.

Finally \(M_{\rm near}(0)=1+n/m\), while \(M_{\rm near}(r)\to1\) as \(r\to\infty\). Their relative difference is \(n/(m+n)\), proving sharpness. For right-nonbridge targets the expectation grows quadratically with the reset rate; for the right bridge it grows linearly. These exhaust all targets other than the starting vertex.

## Verification
The accompanying standalone script `verify.py` checks both rational Laplace transforms against the four-lump generator resolvents symbolically, the two mean-time formulas against the renewal identity, and the bridge transform exactly. It also constructs the **full, un-lumped** graph generator, adds resets, solves the absorbing mean-time equations, and compares all four target classes for \(m\in\{3,\ldots,7\}\), \(n\in\{2,\ldots,6\}\), and six reset rates, a total of 600 comparisons. The checks passed. They supplement, not replace, the all-size proof above.

## Relationship to prior work
Lin, Julaiti, and Zhang (2012) study general-graph deep trapping and identify barbell graphs as extremal for large global hitting times, but use a different discrete-time walk and do not analyze resetting. Riascos, Boyer, Herringer, and Mateos (2019/2020) derive a network resetting spectral framework and display numerical global search times on a barbell with a connecting path; their transition model selects a neighbor at total unit jump rate and their barbell discussion does not give this all-target, all-reset-rate monotonic classification for the independently rate-one edge-clock walk. Huang and Chen (2021) analyze **first-passage-triggered**, rather than independent Poisson, resetting on a barbell with a bridge node. Zelenkovski and colleagues (2023) examine centrality-based, degree-normalized discrete-time resetting and barbell global search. This exact classification does not assert novelty for general renewal formulas, generator resolvents, or the barbell graph itself.

## Limitations
The all-size monotonicity proof is specific to a single-edge bridge, independent rate-one jumps per edge, a nonbridge source, and Poisson restarting to that source. It neither determines other graph families nor proves a general criterion for arbitrary Markov generators. General mathematical formulas for stochastic resetting make related specializations possible, so independently finding an earlier equivalent specialization remains a bibliographic risk. The 2023 paper's relevant indexed barbell exposition was examined, but a complete accessible full text could not be retrieved during the literature check; its distinct discrete-time resetting setup reduces, but does not erase, this uncertainty. Independent audit has not been performed.

## References
1. Y. Lin, A. Julaiti, Z. Zhang, *Mean first-passage time for random walks in general graphs with a deep trap*, arXiv:1209.6165v1 (first posted 2012-09-27), J. Chem. Phys. 137, 124104 (2012). https://arxiv.org/html/1209.6165v1
2. A. P. Riascos, D. Boyer, P. Herringer, J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568v2 (first posted 2019-10-29), Phys. Rev. E 101, 062147 (2020). https://arxiv.org/html/1910.13568v2
3. F. Huang, H. Chen, *Random walks on complex networks with first-passage resetting*, arXiv:2104.09731v3 (first posted 2021-04-20), Phys. Rev. E 103, 062132 (2021). https://arxiv.org/html/2104.09731v3
4. K. Zelenkovski, T. Sandev, R. Metzler, L. Kocarev, L. Basnarkov, *Random Walks on Networks with Centrality-Based Stochastic Resetting*, Entropy 25, 293 (2023), DOI:10.3390/e25020293.
