# An exact correlation law and a beta limit for competing zealots on complete bipartite voter networks

## Finding

Let \(K_{a,b}\) have vertex parts \(A,B\), each with at least two vertices. Fix one vertex in \(A\) permanently at opinion \(1\), and one vertex in \(B\) permanently at opinion \(0\). Other vertices have binary opinions and, at independent rate-one Poisson times, copy the opinion of a uniformly chosen neighbor. At the unique stationary law, let \(I\) and \(J\) be the numbers of opinion-\(1\) *flexible* vertices in \(A\) and \(B\), respectively.

Write \(N=a+b\), \(m=a-1\), and \(n=b-1\). For each flexible vertex in \(A\) and \(B\), respectively, the stationary probabilities of opinion \(1\) are
\[
 x=\frac{b-1}{N-1},\qquad y=\frac{b}{N-1}.
\]
For any distinct flexible vertices belonging to the indicated parts, their joint probability of both holding opinion \(1\) is
\[
\begin{aligned}
 p_{AB}&=\frac{b(a+3b-4)}{(N-1)(3N-4)},\\
 p_{AA}&=\frac{(b-1)(a+3b-4)}{(N-1)(3N-4)},\\
 p_{BB}&=\frac{b(a+3b-2)}{(N-1)(3N-4)}.
\end{aligned}
\]
The same-part formulas require at least two flexible vertices in that part, so \(p_{AA}\) is stated for \(a\ge3\) and \(p_{BB}\) for \(b\ge3\). Subtracting products of means gives
\[
\begin{aligned}
 \operatorname{Cov}_{AB}&=\frac{ab(N-2)}{(N-1)^2(3N-4)},\\
 \operatorname{Cov}_{AA}&=\frac{a(b-1)(N-2)}{(N-1)^2(3N-4)},\\
 \operatorname{Cov}_{BB}&=\frac{b(a-1)(N-2)}{(N-1)^2(3N-4)}.
\end{aligned}
\]

More substantially, along **every** sequence \(a,b\to\infty\) for which \(a/(a+b)\to\rho\in(0,1)\), the two flexible opinion shares converge jointly:
\[
 \left(\frac{I}{a-1},\frac{J}{b-1}\right)
 \Longrightarrow (Z,Z),\qquad
 Z\sim\operatorname{Beta}(2(1-\rho),2\rho).
\]
Hence also \((I+J)/(N-2)\Longrightarrow Z\). In particular, when the parts are asymptotically balanced, the opinion-\(1\) fraction converges to the **uniform law on \([0,1]\)**, not to a deterministic consensus fraction. In that case the limiting probability that at least three quarters of flexible vertices choose opinion \(1\) is \(1/4\). At general fixed \(\rho\), the limiting variance is \(\rho(1-\rho)/3>0\).

## Assumptions and scope

The graph is the undirected, unweighted complete bipartite graph \(K_{a,b}\). The two opposite zealots are included in all their respective neighbors' sampling pools but never change opinions. Every other vertex has a unit-rate independent Poisson update clock and copies one uniformly chosen neighbor; there is **no** intrinsic mutation, majority rule, confidence threshold, or asynchronous update of the zealots. The formulas describe the unique invariant probability for each finite \(a,b\ge2\), not the outcome at a fixed finite time. The limiting assertion requires both parts to grow proportionally, with the fraction \(\rho\) bounded away from zero and one. The same-side joint-probability formulas apply only when the indicated pair of distinct flexible vertices exists.

The primary mathematical domain is stochastic opinion dynamics on social networks (MSC2020 91D30).

## Proof

**1. A unique stationary law and its count generator.** Set \(m=a-1\), \(n=b-1\). From a state with \(i\) flexible ones in \(A\) and \(j\) in \(B\), the only nonzero state-changing count rates are
\[
\begin{array}{ll}
 (i,j)\to(i+1,j): &(m-i)j/b,\\
 (i,j)\to(i-1,j): &i(b-j)/b,\\
 (i,j)\to(i,j+1): &(n-j)(i+1)/a,\\
 (i,j)\to(i,j-1): &j(a-1-i)/a.
\end{array}
\]
These rates follow by counting flexible vertices of each opinion and the proportion of opposite-part neighbors supplying the other opinion. The count state \((0,0)\) can be reached from every state: first each flexible \(A\) vertex with opinion \(1\) copies the fixed opinion-\(0\) neighbor, then each flexible \(B\) vertex with opinion \(1\) copies a flexible \(A\) vertex with opinion \(0\). Every required transition has positive rate. Thus there is only one closed communicating class, which gives a unique invariant law for this finite-state chain. The full labeled chain has a unique invariant law by the same accessibility argument, and its permutation symmetry within flexible vertices makes the formulas below valid for individual agents as well as counts. We do **not** claim that every count state is recurrent.

**2. Exact first and second moments.** By stationarity of a single flexible opinion indicator, if \(x\) and \(y\) are its means in the two parts, then
\[
 x=\frac{(b-1)y}{b},\qquad
 y=\frac{1+(a-1)x}{a}.
\]
Their unique solution is \(x=(b-1)/(N-1)\), \(y=b/(N-1)\). Exchangeability and stationarity of products of two distinct opinion indicators yield the three equations
\[
\begin{aligned}
 p_{AA}&=\frac{b-1}{b}p_{AB},\\
 p_{BB}&=\frac{y+(a-1)p_{AB}}a,\\
 2p_{AB}&=\frac{y+(b-2)p_{BB}}b
              +\frac{2x+(a-2)p_{AA}}a.
\end{aligned}
\]
When a same-part pair does not exist, its coefficient in the last equation is zero and the corresponding unused equation is omitted; the stated cross-pair formula still follows directly. Solving gives the three expressions in the Finding section. Explicit subtraction of \(xy\), \(x^2\), or \(y^2\), as applicable, yields the covariance identities. This calculation uses no independence assumption between agents.

**3. The two opinion shares synchronize in the large-population limit.** Write \(U=I/m\) and \(V=J/n\). For \(m\ge2\),
\[
 \operatorname{Var}(U)=\frac{x(1-x)}m
              +\frac{m-1}{m}\operatorname{Cov}_{AA},
\]
with the second term defined as zero when \(m=1\); analogously for \(V\). Since \(\operatorname{Cov}(U,V)=\operatorname{Cov}_{AB}\), and all three pair covariances tend to \(\rho(1-\rho)/3\), the exact formulas imply
\[
 \mathbb E[(U-V)^2]\longrightarrow0.
\]
In particular, this is convergence in probability of the two empirical fractions to one another at stationarity. The limit of their individual variances is nonzero, so it is not a law of large numbers to a fixed value.

**4. Stationary diffusion limit and identification of the law.** Put
\[
 H=bm+an=2ab-a-b,
 \qquad Z_N=\frac{bI+aJ}{H}.
\]
This is a convex combination of \(U\) and \(V\), and therefore \(|Z_N-U|\le|U-V|\). The same inequality holds between \(Z_N\) and the unweighted fraction \((I+J)/(m+n)\). Let \(\mathcal L_N\) denote the exact count-chain generator. Directly from the four rates,
\[
 \mathcal L_N Z_N=\frac{n-I-J}{H}.
\]
Its quadratic-variation rate is
\[
 \mathcal L_N Z_N^2-2Z_N\mathcal L_N Z_N
 =\frac{b(mJ+bI-2IJ)+a(n(I+1)+aJ-2J(I+1))}{H^2}.
\]
Multiply the generator by \(H/N\), which changes only the speed, not the invariant law. For each fixed \(f\in C^3([0,1])\), Taylor's theorem, the last two identities, and \(U-V\to0\) in stationary probability imply
\[
 \frac{H}{N}\mathcal L_N f(Z_N)
 -\left((1-\rho-Z_N)f'(Z_N)
    +\frac12 Z_N(1-Z_N)f''(Z_N)\right)
 \longrightarrow0
\]
in stationary \(L^1\). Here the jumps are \(b/H\) or \(a/H\), both \(O(N^{-1})\), the jump-rate sum is \(O(N)\), and the rescaled third-order remainder is \(O(N^{-1})\). The drift and quadratic coefficients converge as claimed because \(a/N\to\rho\) and \(U-V\to0\).

The invariant laws of \(Z_N\) are tight on \([0,1]\). Let \(\nu\) be any weak subsequential limit. For each polynomial \(f\), stationary expectation of the exact generator is zero; taking limits gives
\[
 \int_0^1\left[(1-\rho-z)f'(z)
   +\frac12z(1-z)f''(z)\right]\,d\nu(z)=0.
\]
Testing \(f(z)=z^k\), for each integer \(k\ge1\), proves the recurrence
\[
 \mu_k=\frac{k-1+2(1-\rho)}{k+1}\,\mu_{k-1},
 \qquad\mu_0=1,
\]
where \(\mu_k=\int z^k\,d\nu(z)\). These are exactly the moments of \(\operatorname{Beta}(2(1-\rho),2\rho)\). A measure on the compact interval \([0,1]\) is determined by its moments (polynomial approximation), so all subsequential limits coincide. Consequently the full stationary sequence converges to this beta law. The synchronization in step 3 transfers convergence to the claimed joint shares and total flexible share. The mean and variance of the beta law are \(1-\rho\) and \(\rho(1-\rho)/3\). When \(\rho=1/2\), both beta parameters equal one, giving the uniform law and the claimed upper-tail probability.

## Verification

The accompanying executable `verify.py` uses only Python's standard library and exact rational arithmetic. It compares the count jump rates with a separately written vertex-level copying enumeration for all count states when \(2\le a,b\le5\), reconstructs the full rational stationary distribution of the finite count generator for each of those 16 graph sizes, and compares all first/factorial-second/cross moments with the closed formulas. It also checks five independent stationary moment balance equations over all 361 parameter pairs \(2\le a,b\le20\). The resulting replay reports 196 vertex-event rate checks, 16 exact stationary distributions, and 361 moment-system checks. These finite checks corroborate the formulas; the infinite beta convergence is proved analytically in step 4, not inferred from enumeration.

To reproduce, run `python verify.py` from the directory containing the extracted documents. The program prints its PASS counts and raises an assertion on any discrepancy. No external packages, numerical tolerances, or downloaded datasets are required.

## Relationship to prior work

Njougouo, Reina, Tuci and Carletti (arXiv:2401.00114v1, December 30, 2023) investigate heterogeneous-network decisions with zealots using heterogeneous mean-field methods and simulations, including voter updating. The present claim instead derives **exact finite-network pair correlations** and a **stationary weak limit on an explicit bipartite graph family**. Their published heterogeneous mean-field and simulation statements do not imply these formulas or the joint beta limit.

Acemoglu, Como, Fagnani and Ozdaglar develop a general theory of stubborn-agent opinion fluctuations and disagreement; those general results motivate stationary-correlation analysis but do not print the present complete-bipartite formulas or beta limit. Ben-Ari and collaborators analyze quasi-stationary distributions for the voter model on complete bipartite graphs **without two fixed opposing zealots**, a different chain with absorbing consensus. Pickering and Lim analyze the zealot-free bipartite voter model through spectral methods. Braha and de Aguiar obtain exact stationary laws for the well-mixed zealot/Moran model and discuss random or heterogeneous graphs; the **well-mixed complete-graph beta behavior is known**, whereas the degree-asymmetric fixed \(K_{a,b}\) stationary scaling and specific pair correlations here are not consequences of that case. These distinctions concern mathematical assumptions, not merely titles.

## Limitations

The beta limit concerns only the stationary regime and simultaneous proportional growth of the two parts. It does not quantify convergence time, nonstationary initial conditions, other graph classes, more than two zealots, or nonuniform copying. A well-mixed network already has related beta stationary limits; novelty is claimed specifically for this graph-dependent pair-correlation formula and the nontrivial bipartite, degree-asymmetric scaling. Literature priority remains subject to specialist verification. The computations are finite corroboration, not an independent proof of the limiting statement. No independent external audit has been performed.

## References

1. T. Njougouo, A. Reina, E. Tuci, and T. Carletti, *On the role of zealots in a best-of-n problem on a heterogeneous network*, arXiv:2401.00114v1 (first publicly posted 2023-12-30), https://arxiv.org/abs/2401.00114.
2. D. Acemoglu, G. Como, F. Fagnani, and A. Ozdaglar, *Opinion Fluctuations and Disagreement in Social Networks*, Mathematics of Operations Research 38 (2013), https://economics.mit.edu/sites/default/files/publications/Opinion%20Fluctuations%20and%20Disagreement%20in%20Social%20Ne.pdf.
3. I. Ben-Ari, A. Panzo, J. Speegle, and R. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187, https://arxiv.org/abs/2004.10187.
4. W. Pickering and C. Lim, *Solution of the Voter Model by Spectral Analysis*, arXiv:1408.2130, https://arxiv.org/abs/1408.2130.
5. D. Braha and M. A. M. de Aguiar, *The multi-allelic Moran process as a multi-zealot voter model: exact results and consequences for diversity thresholds*, arXiv:2601.09816v1 (2026), https://arxiv.org/abs/2601.09816.
