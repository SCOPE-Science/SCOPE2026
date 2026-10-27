# Rare terminal vertices produce a linear cover-time penalty on biased cycles

## Finding

Let a nearest-neighbor walk start at vertex \(0\) of the labeled cycle \(C_n\), for integer \(n\ge4\). Independently at each step it moves clockwise with fixed probability \(p\in(1/2,1)\), counterclockwise with probability \(q=1-p\). Write \(T\) for its first time visiting all \(n\) vertices and \(J\) for the last vertex discovered. Put \(d=p-q\), \(r=q/p\), and \(C_m=(1+r^m)/(1-r^m)\) for positive integers \(m\).

For every \(2\le j\le n-2\), set \(N=n-2\), \(i=n-j-1\), and
\[
\beta_{n,j}=\frac{r^{j-1}(1-r^i)}{1-r^N},
\qquad H_y=\frac{1-r^y}{1-r^n}.
\]
Define five exact conditional passage-time components
\[
\begin{aligned}
A_1&=\frac{NC_N-(j-1)C_{j-1}}{d},
&B_1&=\frac{NC_N-iC_i}{d},\\
U&=\frac{(N+1)C_{N+1}-C_1}{d},
&V_+&=\frac{nH_{n-1}-(n-1)}{d},\\
&&V_-&=\frac{nH_1-1}{d}.
\end{aligned}
\]
Then the complete conditional first moment is
\[
\boxed{\mathbb E_0[T\mid J=j]
=(1-\beta_{n,j})(A_1+U+V_+)
+\beta_{n,j}(B_1+U+V_-).}
\]
The corresponding terminal-site law is
\[
\Pr_0(J=j)=\frac{(1-r)r^{n-1-j}}{1-r^{n-1}},
\qquad 1\le j\le n-1.
\]

The principal new asymptotic consequence is **uniform** over integers \(2\le j\le n-2\):
\[
\boxed{\mathbb E_0[T\mid J=j]
=\frac{2n-j-1}{d}-\frac1{d^2}
+O_p(nr^{j-1}).}
\]
In particular, for every \(x\in(0,1)\) and every integer sequence \(j_n/n\to x\),
\[
\boxed{\frac1n\mathbb E_0[T\mid J=j_n]
\longrightarrow\frac{2-x}{2p-1}.}
\]
On the other hand, \(\mathbb E_0 T/n\to 1/(2p-1)\). Thus conditioning on the exponentially unlikely event that the final vertex lies near proportion \(x\) of the clockwise circuit multiplies the first-order mean coverage time by \(2-x\). Its terminal probability has exponential rate
\[
\frac1n\log\Pr_0(J=j_n)\longrightarrow (1-x)\log r<0.
\]

## Assumptions and scope

The walk is discrete-time, nearest-neighbor, spatially homogeneous, with independent increments and fixed clockwise bias strictly greater than one half. The cycle is labeled \(0,1,\dots,n-1\) clockwise and the starting vertex is \(0\). The conditional expectation is defined only at events with positive probability, which holds for all \(1\le j\le n-1\). The displayed finite moment formula is stated for interior terminal labels \(2\le j\le n-2\); endpoint formulas follow from deleting whichever branch has zero probability. All error constants in \(O_p\) may depend on fixed \(p\), but not on \(n,j\). No assertion of uniformity is made as \(p\downarrow1/2\).

## Proof

**Step 1: two possible discovery orders.** Fix \(j\). Delete \(j\) from the cycle and index the remaining path \(0,1,\ldots,N\) clockwise, with path coordinate \(0\) representing original vertex \(j+1\), path coordinate \(N\) representing original vertex \(j-1\), and the walk starting at coordinate \(i=n-j-1\). Both missing exterior neighbors \(-1\) and \(N+1\) represent original vertex \(j\). Since the path is traversed by nearest-neighbor steps, \(j\) is last exactly when both endpoints of this path are visited before an exterior exit. The successful path must visit endpoint \(0\) then endpoint \(N\) while avoiding \(-1\), or endpoint \(N\) then endpoint \(0\) while avoiding \(N+1\). Once both endpoints have been visited, all other cycle vertices have been visited, and the cover time ends at the next hit of \(j\).

**Step 2: splitting probabilities.** For a right-drifting nearest-neighbor walk on the integer interval \([0,L]\) absorbed at its endpoints, gambler's ruin gives
\[
h_L(y):=\Pr_y(\text{hit }L\text{ before }0)
=\frac{1-r^y}{1-r^L},\qquad 0\le y\le L.
\]
The weights of the two successful endpoint orders are therefore
\[
\begin{aligned}
w_A&=\frac{r^i-r^N}{1-r^N}\,\frac{1-r}{1-r^{N+1}},\\
w_B&=\frac{1-r^i}{1-r^N}\,\frac{r^N(1-r)}{1-r^{N+1}}.
\end{aligned}
\]
Their sum telescopes to
\[
w_A+w_B=\frac{(1-r)r^i}{1-r^{N+1}},
\qquad \frac{w_B}{w_A+w_B}
=\frac{r^{N-i}(1-r^i)}{1-r^N}=\beta_{n,j}.
\]
As \(N+1=n-1\) and \(i=n-1-j\), the terminal-site formula follows. It agrees with the published biased last-coverage marginal law and is not itself asserted as a new result.

**Step 3: weighted exit-time identity.** Let \(\tau\) be the first exit from \((0,L)\) and let \(u(y)=\mathbb E_y[\tau\,\mathbf1_{\{X_\tau=L\}}]\). First-step conditioning gives
\[
u(y)=h_L(y)+p u(y+1)+q u(y-1),\quad
u(0)=u(L)=0.
\]
Solving this difference equation with particular solutions proportional to \(y\) and \(yr^y\) gives
\[
\frac{u(y)}{h_L(y)}
=\frac{LC_L-yC_y}{d}.
\]
The corresponding conditional time for exit on the left is
\[
\mathbb E_y[\tau\mid X_\tau=0]
=\frac{LC_L-(L-y)C_{L-y}}d.
\]
Both formulas hold for integers \(1\le y<L\). Uniqueness follows from the finite killed-chain Dirichlet problem, or directly from the difference equation.

**Step 4: conditional passage times.** Applied to the initial interval \([0,N]\), Step 3 yields \(A_1\) and \(B_1\) for the first endpoint under the two successful orders. Starting at endpoint \(0\), going to \(N\) before \(-1\), or starting at endpoint \(N\), going to \(0\) before \(N+1\), gives the same conditional mean \(U\). Once both path endpoints are visited, the remaining stopping time is the first hit of \(j\) from its left or right neighbor. Cutting the cycle at \(j\) makes this a gambler's-ruin exit on \([0,n]\). Optional stopping for the bounded-interval drift martingale \(X_t-dt\) gives the unconditional endpoint-absorption mean \([n h_n(y)-y]/d\). Choosing \(y=n-1\) or \(y=1\) yields \(V_+\) and \(V_-\), respectively. The strong Markov property and the conditional branch weight \(\beta_{n,j}\) establish the exact formula in the Finding.

**Step 5: uniform remainder.** Since \(C_m=1+2r^m/(1-r^m)\) and \(C_m\le C_1\) for all \(m\ge1\),
\[
A_1=\frac{i}{d}+O_p(nr^{j-1}),
\quad U=\frac{n-1-C_1}{d}+O_p(nr^{n-1}),
\quad V_+=\frac1d+O_p(nr^{n-1}).
\]
Also \(B_1+U+V_-=O_p(n)\) uniformly, and
\[
0\le\beta_{n,j}\le\frac{r^{j-1}}{1-r}.
\]
Substitution gives \(\mathbb E[T\mid J=j]=(i+n-C_1)/d+O_p(nr^{j-1})\). Using \(i=n-j-1\) and \(C_1=1/d\) gives exactly the displayed sharp expansion.

**Step 6: unconditional comparison.** All conditional means are at most \(K_p n\) for a constant \(K_p\), by the same positive finite-interval exit-time formulas, including the endpoint branches. For fixed \(k\ge0\), the formula with \(j=n-1-k\) (with its natural single-branch endpoint convention when \(k=0\)) gives \(\mathbb E[T\mid J=n-1-k]/n\to1/d\). The established terminal law implies \(\Pr(J=n-1-k)\to(1-r)r^k\), and these probabilities have a uniform geometric tail. Dominated summation therefore yields \(\mathbb E T/n\to1/d\). The stated rare-event rate follows by taking logarithms of the terminal law.

## Verification

The standalone standard-library program `verify.py` independently solves the full discrete Markov-chain first-step equations on states (visited subset, current vertex), retaining for every possible terminal label both its probability and its unnormalized cover-time first moment. It compares those independently obtained rational quantities with the formulas above for all terminal labels, cycle sizes \(3\le n\le8\), and clockwise probabilities \(3/5,2/3,3/4\). It also checks finite error ratios for larger cycles; these latter checks are diagnostics only. The accompanying `verification_output.txt` records 252 passing assertions. Reproduction: `python verify.py` (Python standard library, no external dependencies).

## Relationship to prior work

Idnani and Salem (arXiv:2610.15115, submitted 2026-10-10) establish the connected-arc representation and exact **marginal** law of the last-covered vertex for symmetric and biased cycle walks, plus a treatment of time-varying bias. That marginal law is credited above. The separate present claim conditions **elapsed cover time on an exponentially unlikely terminal vertex**, gives its finite first moment, and identifies the macroscopic \((2-x)\) slowdown with an exponentially small bulk error. A 2021 public mathematical discussion derives the symmetric terminal-location uniformity and outlines a conditional mean-time decomposition for the **unbiased** walk; those statements are not claimed as new. Classical gambler's-ruin and cover-time identities are standard proof ingredients. The complete 2026 source manuscript could not be inspected; therefore the priority comparison against unexamined sections is a material limitation.

## Limitations

The theorem has fixed positive clockwise drift and excludes the critical symmetric case and parameter-uniform near-critical scaling. It concerns the first conditional moment and not a conditional limit law for the full cover-time distribution. The asymptotic is nontrivial for last sites with their distance \(j\) tending to infinity (especially \(j/n\to x\in(0,1)\)); near fixed small \(j\), the displayed remainder may be of leading order. Exhaustive finite-state calculations cannot establish the infinite statement. A priority risk remains because the complete recent primary preprint and some historical sources were inaccessible; scientific independence has not been established by external review.

## References

1. Kiyan Idnani and Jad Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115 (first submission 2026-10-10), https://arxiv.org/abs/2610.15115.
2. László Lovász and Peter Winkler, *On the Last New Vertex Visited by a Random Walk*, Journal of Graph Theory **17** (1993), 593–596.
3. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6 (cycle cover times and last vertices), https://www.stat.berkeley.edu/~aldous/RWG/book.html.
4. “Simple random walk on cycle graph (Ending on specific vertex after cover time),” Mathematics Stack Exchange question 4273163, 2021-10-10 (answer 2021-10-18), https://math.stackexchange.com/questions/4273163/.
