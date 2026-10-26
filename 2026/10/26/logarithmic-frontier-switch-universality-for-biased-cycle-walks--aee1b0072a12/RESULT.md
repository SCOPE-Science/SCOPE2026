# Logarithmic frontier-switch universality for biased cycle walks

## Finding
Let \(n\ge3\) and let a nearest-neighbour random walk start at vertex \(0\) of the labelled cycle \(C_n\). Its clockwise-step probability \(p\in(0,1)\) is constant throughout the walk. List the directions \(Y_1,\ldots,Y_{n-1}\in\{L,R\}\) in which *previously unvisited* vertices are discovered, ignoring steps to already visited sites, and define the frontier-alternation count
\[
K_{n,p}=\sum_{j=1}^{n-2}\mathbf1\{Y_{j+1}\ne Y_j\}.
\]
Put \(\theta=\left|\log\frac{p}{1-p}\right|\), with \(\theta^{-1}=+\infty\) when \(\theta=0\), and
\[
M(n,\theta)=\min\{n-1,\lfloor\theta^{-1}\rfloor\}.
\]
There is a coupling of \(K_{n,p}\) with independent Bernoulli variables \(B_m\), \(m\ge2\), with \(\Pr(B_m=1)=1/(m+1)\), such that for every \(n\ge3\) and every \(p\in(0,1)\),
\[
\boxed{\mathbb E\left|K_{n,p}-\sum_{m=2}^{M(n,\theta)}B_m\right|
\le e+1+\frac{2}{1-e^{-1}}<7.}
\]
An empty sum is zero. At \(p=1/2\), the coupled variables agree almost surely, so the **exact** probability generating function is
\[
\boxed{\mathbb E[z^{K_{n,1/2}}]=\prod_{j=3}^{n}\frac{j-1+z}{j}.}
\]
In particular, for any deterministic triangular sequence \(n\to\infty\) and \(p_n\in(0,1)\) with effective length
\[
\ell_n=\min\left\{n,\left|\log\frac{p_n}{1-p_n}\right|^{-1}\right\}\longrightarrow\infty,
\]
one has
\[
\boxed{\frac{K_{n,p_n}-\log\ell_n}{\sqrt{\log\ell_n}}\ \Longrightarrow\ N(0,1),\qquad
\mathbb E K_{n,p_n}=\log\ell_n+O(1).}
\]
For \(p_n=1/2+c n^{-a}\), where \(c\ne0\) is fixed and \(a>0\), the effective logarithmic length is \(\min\{a,1\}\log n+O(1)\). Thus the Gaussian centering and variance scale are \(\min\{a,1\}\log n\), whereas for any fixed \(p\ne1/2\) the number of alternations converges almost surely to a finite random variable as the cycle grows under a common-walk coupling.

## Assumptions and scope
Only simple nearest-neighbour walks on a cycle are considered; no self-loops, direction persistence between ordinary steps, or time-dependent step probabilities are allowed. The index \(m\) denotes the number of already visited vertices immediately before the next discovery, and runs from \(2\) to \(n-1\) when counting switches. A new discovery may be made at either end of the currently visited arc. Even at the final discovery, where both endpoints neighbor the same unvisited vertex, its label is the *side from which the walk entered that vertex*. The parameters \(p_n\) may depend on the total cycle size but must remain constant in time within each individual walk. All logarithms are natural.

## Proof
**1. Discovery-direction chain.** Before coverage, the visited set is an arc of \(m\) consecutive vertices. Just after a discovery, the walker sits at the newly visited endpoint, so its next exit side depends only on the previous discovery side, not on earlier history. Reflection interchanges \(p\) and \(1-p\) without changing \(K_{n,p}\), so assume \(p\ge1/2\). Write \(r=(1-p)/p=e^{-\theta}\) and \(S_m=1+r+\cdots+r^m\). Place the two as-yet-unvisited exit sites at \(-1\) and \(m\), the visited sites at \(0,\ldots,m-1\), and solve the standard gambler's-ruin Dirichlet problem. For a last discovery at the right end, the probability that the next discovery occurs at the left is \(a_m=r^m/S_m\). For a last discovery at the left end, the probability that the next discovery occurs at the right is \(b_m=1/S_m\). The initial discovery is right with probability \(p\). These formulas are valid with their continuous values at \(r=1\). Notice that \(a_m\) and \(b_m\) depend on \(m\), not on the location of the arc in the cycle.

**2. Coupling and small-range bound.** Let \(U_m\), \(m\ge2\), be independent uniforms, independent also of the first discovery. Generate the next discovery by switching sides when \(U_m\le a_m\) if the current side is right and when \(U_m\le b_m\) if it is left. Set \(B_m=\mathbf1\{U_m\le1/(m+1)\}\). Then all \(B_m\) are independent, each with success probability \(1/(m+1)\). If \(\theta=0\), then \(a_m=b_m=1/(m+1)\), and the coupling has zero error.

For \(\theta>0\) and \(m\theta\le1\), since \(e^{-m\theta}(m+1)\le S_m\le m+1\) and \(1-e^{-j\theta}\le j\theta\),
\[
0\le b_m-\frac1{m+1}\le\frac{e\theta}{2},\qquad
0\le\frac1{m+1}-a_m\le e\theta.
\]
The first inequality follows by bounding \((m+1)-S_m\) by \(\theta m(m+1)/2\); for the second, use \(a_m\le1/(m+1)\) and \(1/(m+1)-a_m\le(1-r^m)b_m\). Thus, for all \(2\le m\le M(n,\theta)\), the mismatch probability between the real switch indicator and \(B_m\) is at most \(e\theta\). Summing these probabilities gives expected early mismatch count at most \(e\).

**3. Uniform late-switch bound.** Consider the discovery stages \(m>M(n,\theta)\) through \(n-1\). Whenever the current side is right, the probability of switching to left is at most \(a_m\). Since these stages satisfy \(m>\theta^{-1}\),
\[
\sum_{m>M(n,\theta)}a_m
\le \frac{1}{1-e^{-1}}\sum_{m>M(n,\theta)}(1-r)r^m
\le\frac1{1-e^{-1}},
\]
where an empty tail is interpreted as zero. In any binary side sequence, successive switches alternate directions. Therefore the number of late \(L\to R\) switches is at most one plus the number of late \(R\to L\) switches, even if the side at the start of the tail is left. The expected total number of late switches is bounded by \(1+2/(1-e^{-1})\). Combining this with step 2, the triangle inequality proves the asserted \(L^1\) coupling bound, uniformly in \(n,p\).

**4. Distributional consequences.** At \(p=1/2\) all the switch indicators equal independent \(B_m\), giving the displayed generating function. For general \(p_n\) with \(\ell_n\to\infty\), write \(M_n=M(n,\theta_n)\) and \(Z_n=\sum_{m=2}^{M_n}B_m\). Then \(M_n\to\infty\), and
\[
\mathbb E Z_n=H_{M_n+1}-H_2=\log\ell_n+O(1),
\]
\[
\operatorname{Var}(Z_n)=\sum_{m=2}^{M_n}\frac{m}{(m+1)^2}
=\log\ell_n+O(1).
\]
The bounded Bernoulli triangular array satisfies Lindeberg's condition, so its variance-normalized sum is asymptotically standard Gaussian. The uniform \(L^1\) estimate makes \((K_{n,p_n}-Z_n)/\sqrt{\log\ell_n}\) converge to zero in probability and shows the stated expectation asymptotics. Slutsky's theorem concludes the central limit theorem.

For fixed \(p\ne1/2\), use the same first-discovery variable and the same \(U_m\) for all cycle sizes. Under this coupling the discovery direction chain extends to arbitrarily large \(m\). Since \(r<1\), \(\sum_{m\ge2}a_m<\infty\). Hence there are almost surely finitely many \(R\to L\) switches, and therefore finitely many \(L\to R\) switches. The count converges almost surely. Finally, when \(p_n=1/2+c n^{-a}\), the expansion \(\theta_n=4|c|n^{-a}+O(n^{-3a})\) gives the stated crossover.

## Verification
The standalone script `verify_frontier.py` independently solves the finite gambler's-ruin difference equations over rational numbers and compares the resulting exact switch-count distributions with the explicit transition formula for \(3\le n\le9\) and four rational step probabilities. It separately propagates the original nearest-neighbour steps using exact rational arithmetic (rather than the discovery transition formula) for \(3\le n\le6\), and bounds the total unabsorbed probability after 400 steps by \(10^{-12}\) in every such test. It also checks the symmetric generating-function coefficients and the elementary small-range inequalities used in the coupling proof. The recorded run passed 2435 finite checks. These are not a computer proof of the asymptotic theorem; the analytic coupling, Borel-Cantelli argument and Lindeberg theorem above supply that proof.

## Relationship to prior work
Idnani and Salem (arXiv:2610.15115, submitted 10 October 2026) established the connected-arc discovery representation and the exact two-state transition probabilities for the last-covered vertex on a cycle. Those transitions are expressly used as the starting point here, not claimed as new. The present contribution is the distinct frontier-*alternation count*, its exact symmetric-law identification, and especially the uniform-in-drift bounded-error Bernoulli coupling, which yields a sharp effective-range Gaussian crossover for all triangular step biases. Standard gambler's ruin and independent Bernoulli-array limit theorems provide the classical supporting ingredients. Record-count studies such as Wergen–Majumdar–Schehr (2012) and Mendonça (2026) count record highs over *time* rather than changes between left- and right-range frontiers indexed by successive discoveries. None of the inspected statements asserts the uniform coupling inequality or its effective-length limit theorem.

## Limitations
The result counts changes of the *discovery frontier*, not changes of the walk's ordinary step direction, and it does not determine the law of cover time or the joint law of cover time and the alternation count. The universal \(L^1\) bound is an absolute bound, not a sharp constant; it does not establish a total-variation or local limit theorem. Historical work on random-walk alternating extrema could potentially contain equivalent statements under different terminology. Independent scientific review has not been performed.

## References
1. K. Idnani and J. Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115v1 (10 October 2026). https://arxiv.org/abs/2610.15115
2. G. Wergen, S. N. Majumdar and G. Schehr, *Record Statistics for Multiple Random Walks*, Physical Review E 86, 011119 (2012), arXiv:1204.5039. https://arxiv.org/abs/1204.5039
3. J. R. G. Mendonça, *Records, drift, and the longest increasing subsequence of biased Gaussian random walks*, arXiv:2605.29185 (27 May 2026). https://arxiv.org/abs/2605.29185
4. W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. I, classical gambler's-ruin formula (reference background).
