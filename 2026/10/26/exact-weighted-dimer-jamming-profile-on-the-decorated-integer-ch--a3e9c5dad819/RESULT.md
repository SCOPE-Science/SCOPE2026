# Exact weighted dimer jamming profile on the decorated integer chain

## Finding

Let \(C_L\) be the graph with spine vertices \(s_1,\ldots,s_L\), consecutive edges \(s_js_{j+1}\), and a distinct pendant vertex \(p_j\) joined to each \(s_j\). Every spine edge has an independent Poisson dimer-attempt process of rate \(\alpha>0\), and every pendant edge has one of rate \(\beta>0\). Attempts occupy both endpoints only if both are still vacant; occupation is irreversible. Write \(P_{L,i}(\alpha,\beta)\) for the final probability that the pendant edge \(s_ip_i\) is occupied. Define
\[
a=\frac{\beta}{\alpha+\beta},\qquad g=\frac{\alpha}{\alpha+\beta},\qquad E_n(z)=\sum_{j=0}^n\frac{z^j}{j!}.
\]
For every \(L\ge1\) and \(1\le i\le L\),
\[
\boxed{P_{L,i}=\sum_{j=0}^{i-1}\sum_{k=0}^{L-i}
\frac{(-g)^{j+k}(j+k)!}{j!k!\prod_{h=1}^{j+k}(a+h)}.}
\]
The empty product equals one. The finite formula holds for all strictly positive real rates, with no rationality assumption. For sites receding from both endpoints, the common limiting pendant-bond occupation probability is
\[
\boxed{P_\infty(a,g)=a\int_0^1(1-u)^{a-1}e^{-2gu}\,du
=e^{-2g}{}_1F_1(a;a+1;2g).}
\]
Moreover, the finite-volume error obeys the explicit superfactorial estimate
\[
\boxed{\big|P_{L,i}-P_\infty\big|\leq
\frac{g^i}{i!}+\frac{g^{L-i+1}}{(L-i+1)!}.}
\]
As a function of the rate ratio \(b=\beta/\alpha>0\), \(P_\infty(b)\) is strictly increasing, with the singular weak-pendant limit and strong-pendant law
\[
\boxed{\lim_{b\downarrow0}P_\infty(b)=e^{-2},\qquad
P_\infty(b)=1-\frac1b+O(b^{-2})\quad(b\to\infty).}
\]
At the exactly absent-pendant rate \(\beta=0\), no pendant edge can occupy, so its occupation probability is instead zero. If \(\beta\downarrow0\) and observation time \(t=u/\beta\), for any fixed \(u\ge0\), the infinite-chain fraction of occupied pendant edges at time \(t\) converges to \(e^{-2}(1-e^{-u})\). Thus the nonzero weak-rate limit is produced by a late adsorption stage on the scale \(\beta^{-1}\), not by any positive-time discontinuity.

## Assumptions and scope

The graph \(C_L\) is an open decorated path (sometimes called a finite comb); it has \(2L\) vertices and \(2L-1\) edges. The infinite decorated chain has spine indexed by \(\mathbb Z\) and one pendant leaf per spine vertex. For each edge, only its first Poisson attempt matters: once either endpoint is occupied, the edge can never subsequently become admissible. Independent exponential first-arrival clocks are therefore an exactly equivalent construction. All probability statements average these clocks; no mean-field approximation is used. The infinite process is well defined as the local limit of finite intervals because its influence paths have strictly descending independent continuous clocks, and on a bounded-degree graph the chance of an influence path of length \(n\) decreases faster than geometrically for each fixed pair of rates.

## Proof

**Independent branch competition.** Fix a vacant root \(s_i\) and cut an incident spine edge. If that edge first attempts at time \(t\), it succeeds at the root exactly when the opposite spine endpoint is still vacant in the detached branch. If the root stays unoccupied until that first attempt, it has no effect on the detached branch. Consequently, competing edges from distinct branches are independent after the root is removed.

Let \(F_\ell(t)\) denote the probability that a one-sided branch of \(\ell\) spine vertices does *not* supply a successful match to its external root by time \(t\). Set \(F_0(t)=1\). The first edge of the branch attempts with density \(\alpha e^{-\alpha t}\); its opposite spine endpoint is still vacant when its own pendant edge has not arrived (probability \(e^{-\beta t}\)) and its remaining \(\ell-1\) spine branch has not supplied a match (probability \(F_{\ell-1}(t)\)). Therefore, for \(\ell\ge1\),
\[
F_\ell(t)=1-\alpha\int_0^t e^{-(\alpha+\beta)s}F_{\ell-1}(s)\,ds.
\]
With \(x(t)=g(1-e^{-(\alpha+\beta)t})\), the recurrence is \(dF_\ell/dx=-F_{\ell-1}\), and \(F_\ell(0)=1\). Induction gives the *exact* finite expression
\[
F_\ell(t)=E_\ell(-x(t)).
\]
For the pendant edge at \(i\), the pendant first-arrival density is \(\beta e^{-\beta t}\). Both separated spine branches must have failed before that attempt. Hence its occupation probability *by time* \(T\) is
\[
P_{L,i}(T)=\beta\int_0^T e^{-\beta t}F_{i-1}(t)F_{L-i}(t)\,dt.
\]
Substitute \(u=1-e^{-(\alpha+\beta)t}\) and send \(T\to\infty\). The integral becomes
\[
P_{L,i}=a\int_0^1 (1-u)^{a-1}E_{i-1}(-gu)E_{L-i}(-gu)\,du.
\]
Termwise integration and \(aB(n+1,a)=n!/\prod_{h=1}^n(a+h)\) yield the displayed rational-factor finite sum.

**Limit and boundary control.** Since \(0<g<1\), the alternating exponential-series remainder satisfies
\[
|E_\ell(-gu)-e^{-gu}|\le\frac{(gu)^{\ell+1}}{(\ell+1)!},
\qquad 0\le u\le1,
\]
while each factor is in \([0,1]\). Apply the product-difference bound under the probability measure \(a(1-u)^{a-1}du\) to get the stated superfactorial estimate. The infinite limit is therefore the integral of \(e^{-2gu}\). Changing variables to \(w=1-u\), or integrating the exponential series, gives its confluent-hypergeometric representation.

**Monotonicity and singular limit.** Put \(b=\beta/\alpha\), and let \(Y\) be unit-rate exponential. The infinite probability is
\[
P_\infty(b)=\mathbb E\exp\left[-\frac{2}{1+b}\left(1-e^{-(1+1/b)Y}\right)\right].
\]
For every \(Y>0\), both positive factors in the exponent's product decrease strictly as \(b\) grows. Thus the integrand increases strictly. Dominated convergence gives the endpoints \(e^{-2}\) and \(1\). For the leading strong-pendant correction, every spine vertex is ultimately matched when \(\beta>0\), and by translation symmetry the probability of a backbone match on a given incident edge is
\[
Q(b)=\alpha\int_0^\infty e^{-(\alpha+2\beta)t}e^{-2x(t)}\,dt,
\qquad 1-P_\infty(b)=2Q(b).
\]
Putting \(z=\beta t\) and using dominated convergence gives \(bQ(b)\to1/2\). Expanding the bounded integrand once more uniformly under \(e^{-2z}\) yields \(Q(b)=1/(2b)+O(b^{-2})\), proving the announced remainder.

**Late-time crossover.** For the infinite comb, the pendant occupation probability at time \(T\) is
\[
P_\infty(T;\alpha,\beta)=\beta\int_0^T e^{-\beta t}
\exp\left[-\frac{2\alpha}{\alpha+\beta}(1-e^{-(\alpha+\beta)t})\right]dt.
\]
Set \(T=u/\beta\) and \(y=\beta t\). For every fixed \(y>0\), the second exponential tends to \(e^{-2}\) as \(\beta\downarrow0\). Its value lies in \([0,1]\), so dominated convergence on \([0,u]\) proves \(e^{-2}(1-e^{-u})\). At \(\beta=0\), the pendant edges never attempt, and their occupation probability is identically zero. This establishes the claimed noncommutation of the weak-rate and infinite-time limits.

## Verification

The accompanying standard-library-only `verification.py` constructs an independent exact-rational first-successful-edge Markov recursion on finite combs, and compares it with the derived finite sum for all sites of lengths one through seven and four pairs of integer rates (112 exact identities). It separately integrates the finite-branch and infinite-branch formulas and tests 54 instances of the proven finite-volume bound, plus numerical weak-/strong-rate and monotonicity examples. Run `python verification.py` from the package directory. Exact rational comparisons are genuine exhaustive finite-state calculations; quadrature and small-parameter tests are corroboration only, not proofs of the infinite-volume statements.

## Relationship to prior work

General dimer adsorption on graphs, its rigorous infinite-volume construction, and exact occupation formulas on *regular* Bethe trees are established in Penrose and Sudbury [1], building on Evans's lattice-adsorption analysis [2,3]. The all-rates decorated-path formula is not their stated regular-tree result: the decorated spine has two different vertex degrees and separately weighted pendant and spine edges. The root-branch method here is related to their shielding/forward-equation techniques. Evans and Nord [4] treat narrow infinite ladders and strips, including homogeneous dimer adsorption on a square ladder; that strip has an additional parallel rail and its published abstract does not resolve the present decorated-path weighted profile. The paper of Gouet and Sudbury [5] concerns finite Cayley trees, and its full text was not accessible for an exact comparison. No claim of discovery of tree cavity methods, classical one-dimensional dimer RSA, or general infinite-graph construction is made. The assessed contribution is the jointly evaluated finite-site and thermodynamic weighted comb law, its factorial boundary error, monotonic response, and singular slow-pendant crossover.

## Limitations

The theorem assumes a one-pendant-per-spine decorated path, identical rates within each edge class, independent arrival clocks, initially vacant sites, and irreversible dimers. The finite expression determines pendant-edge occupation probabilities, not the full joint jamming law or higher correlations. It does not provide a solution on arbitrary nonregular trees or two-dimensional ladder substrates. Stronger unpublished or inaccessible previously derived decorated-chain formulas could affect priority; the all-literature originality conclusion remains qualified by inspected sources 

## References

[1] M. D. Penrose and A. Sudbury, “Exact and approximate results for deposition and annihilation processes on graphs,” *Annals of Applied Probability* 15 (2005), 853–889; publicly available arXiv:math/0503519v1, 24 March 2005. https://arxiv.org/pdf/math/0503519

[2] J. W. Evans, “Exactly solvable irreversible processes on Bethe lattices,” *Journal of Mathematical Physics* 25 (1984), 2527–2532.

[3] J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of Modern Physics* 65 (1993), 1281–1329. https://doi.org/10.1103/RevModPhys.65.1281

[4] J. W. Evans and R. S. Nord, “Random and cooperative sequential adsorption on infinite ladders and strips,” *Journal of Statistical Physics* 69 (1992), 151–162. https://doi.org/10.1007/BF01053787

[5] R. Gouet and A. Sudbury, “Blocking and dimer processes on the Cayley tree,” *Journal of Statistical Physics* 130 (2008), 935–955. https://doi.org/10.1007/s10955-007-9451-5
