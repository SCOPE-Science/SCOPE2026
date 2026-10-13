# Exact occupancy reduction for dense Markovian supercoupon collection

## Finding

Fix integers \(n\ge2\) and \(1\le s\le n-1\). Consider the Markovian supercoupon collector in which each round displays a subset \(H_t\subseteq[n]\) of size \(n-1\), and every \(s\)-subset of \(H_t\) is collected. From one round to the next, a uniformly chosen member of \(H_t\) is replaced by its unique outside element. The initial displayed subset may be fixed or random.

Let \(x_t\) be the unique missing element of \(H_t\), let \(K_t=|\{x_1,\ldots,x_t\}|\), and let \(U_t\) be the number of \(s\)-subsets still uncollected after round \(t\). **The exact pathwise identity** is

\[
U_t=\begin{cases}
\binom{n-K_t}{s-K_t},&K_t\le s,\\
0,&K_t\ge s+1.
\end{cases}
\]

The entire process \((K_t-1)_{t\ge1}\), not merely any one marginal, has the same finite-dimensional distributions as the number of distinct types seen in \(t-1\) independent uniform draws from an alphabet of size \(n-1\). Consequently, the time \(T_{n,s}\) of first collecting all supercoupons satisfies

\[
T_{n,s}=\inf\{t\ge1:K_t=s+1\},\qquad
T_{n,s}\ \overset{\mathrm d}=\ 1+\sum_{k=1}^{s}G_k,
\]

where the \(G_k\) are **independent**, supported on \(\{1,2,\ldots\}\), and geometric with success probabilities \(p_k=(n-k)/(n-1)\). In particular,

\[
\mathbb E[z^{T_{n,s}}]
=z^{s+1}\prod_{k=1}^{s}
\frac{n-k}{(n-1)-(k-1)z},\qquad |z|\le1,
\]

\[
\mathbb E T_{n,s}
=1+(n-1)\sum_{j=n-s}^{n-1}\frac1j,
\qquad
\operatorname{Var}(T_{n,s})
=(n-1)\sum_{k=1}^{s}\frac{k-1}{(n-k)^2}.
\]

Writing \(\left\{{m\atop j}\right\}\) for the Stirling number of the second kind and \((a)_j=a(a-1)\cdots(a-j+1)\) for the falling factorial, with \((a)_0=1\), the all-time marginal law and cover-time distribution are

\[
\Pr(K_t=k)=\frac{(n-1)_{k-1}}{(n-1)^{t-1}}
\left\{{t-1\atop k-1}\right\}
\quad(1\le k\le n,\ t\ge1),
\]

\[
\Pr(T_{n,s}\le t)=1-\sum_{j=0}^{s-1}
\frac{(n-1)_j}{(n-1)^{t-1}}\left\{{t-1\atop j}\right\}
\quad(t\ge1).
\]

As a scaling consequence within this same exact family, if \(s_n=\lfloor\alpha n\rfloor\) for fixed \(0<\alpha<1\), then

\[
\frac{\mathbb E T_{n,s_n}}n\longrightarrow-\log(1-\alpha),\qquad
\frac{\operatorname{Var}(T_{n,s_n})}n
\longrightarrow v_\alpha:=\frac1{1-\alpha}+\log(1-\alpha)-1>0,
\]

and \((T_{n,s_n}-\mathbb ET_{n,s_n})/\sqrt{n v_\alpha}\) converges in distribution to a standard normal random variable. These are consequences of the exact reduction, not a claim about a fixed-size \(r\) regime.

## Assumptions and scope

The sample space is the complete graph of \((n-1)\)-subsets of \([n]\), with **non-lazy** moves: at each step one of the \(n-1\) currently present elements is uniformly selected for removal, then the unique currently missing element is added. Every round begins with \(t=1\), at which the first display counts. Each possible \(s\)-subset of the full \(n\)-element universe is to be collected. The starting \(H_1\) can be deterministic or have any initial law; permutation symmetry removes its influence on the asserted scalar laws.

The binomial coefficient with lower index outside the allowable range is interpreted as zero. The geometric variables count the *successful trial*, not the number of failures. The results cover every finite \(n\ge2\) and all \(1\le s\le n-1\), including the known complete-graph-cover boundary \(s=n-1\).

## Proof

**Step 1: complement covering identity.** Each \(H_t=[n]\setminus\{x_t\}\). A given \(s\)-set \(S\) is collected in round \(t\) precisely when \(x_t\notin S\). Thus \(S\) remains uncollected after the first \(t\) rounds if and only if \(\{x_1,\ldots,x_t\}\subseteq S\). If there are \(K_t=k\) distinct missing elements, precisely \(\binom{n-k}{s-k}\) such sets exist when \(k\le s\), and none exist when \(k>s\). This proves the pathwise formula and the stopping-time threshold.

**Step 2: exact lumping.** Conditional on the current missing element \(x_t\), the next missing element \(x_{t+1}\) is uniform over the other \(n-1\) elements. If \(K_t=k\), exactly \(n-k\) of those \(n-1\) possible next elements have never been missing. Therefore

\[
\Pr(K_{t+1}=k+1\mid K_1,\ldots,K_t)=\frac{n-k}{n-1},\qquad
\Pr(K_{t+1}=k\mid K_1,\ldots,K_t)=\frac{k-1}{n-1}.
\]

The conditioning may include the entire previous omission path: the displayed probabilities depend only on \(k\). With \(K_1=1\), this is the same birth-and-hold transition kernel as the occupancy count plus one after independent uniform draws from \(n-1\) symbols, started with zero occupied symbols. Equality of all finite-dimensional distributions follows by induction on time.

**Step 3: first passage and distribution.** The waiting time to move from \(K=k\) to \(K=k+1\) has geometric parameter \((n-k)/(n-1)\). By the strong Markov property of this one-dimensional chain, these successive waiting times are independent. The initial round contributes one additional unit, yielding the geometric sum and its probability-generating function. Geometric mean and variance give the displayed expressions. For \(t-1\) independent draws from \(n-1\) symbols, the number of words using exactly \(j\) distinct symbols is \((n-1)_j\left\{{t-1\atop j}\right\}\), proving both explicit formulas and, via the pathwise identity, the complete law of the uncollected count.

**Step 4: proportional-size consequence.** For \(s_n=\lfloor\alpha n\rfloor\), the displayed finite sums are Riemann sums with limits

\[
\int_0^\alpha\frac{dx}{1-x}=-\log(1-\alpha),\qquad
\int_0^\alpha\frac{x\,dx}{(1-x)^2}
=\frac1{1-\alpha}+\log(1-\alpha)-1.
\]

The second integral is strictly positive. All geometric parameters in these triangular arrays are bounded below by a positive constant depending only on \(\alpha\), so their centered third absolute moments are uniformly bounded. Total variance grows as \(n v_\alpha\), and Lyapunov's condition follows from a total third-moment bound of order \(n\) divided by a variance-to-the-\(3/2\) power of order \(n^{3/2}\). Hence the stated normal limit.

## Verification

Running `python3 verify.py` with the included standard-library verifier produces:

```
EXACT_PATH_CHECKS_PASS comparisons=510 n=2..6 t=1..6 s=1..n-1
n=2 s=1 mean=2 variance=0
n=3 s=1 mean=2 variance=0
n=4 s=2 mean=7/2 variance=3/4
n=7 s=3 mean=47/10 variance=99/100
n=10 s=9 mean=7409/280 variance=7782021/78400
```

The verifier enumerates every omission path at those finite horizons using exact rational arithmetic and independently checks the Stirling occupancy law, uncollected-count frequencies, and the truncated geometric-convolution cover-time probabilities. It is a finite reproducibility check; Steps 1–4 supply the proof for all admissible parameters.

## Relationship to prior work

Athreya, Mukherjee, and Mukherjee introduce this Markovian supercoupon model and formulate a general asymptotic expectation conjecture (Conjecture 2.4). They prove a cover-time connection and asymptotic for \(r=s\) (Theorem 2.5), and examine the fixed-parameter regime. The present claim concerns the different, maximal nontrivial display size \(r=n-1\) and gives an **exact all-time uncollected-count process and stopping-time distribution** for every \(s\), including the interior \(1\le s<n-1\). The standard iid partial coupon collector provides the law *after* the complement/occupancy equivalence is established; its formulas are not independently claimed as new. The \(s=n-1\) boundary is the known complete-graph cover-time case, rather than a new stand-alone result.

## Limitations

This reduction does not apply without further arguments to display sizes \(r\le n-2\), to different transition rules, or to unequal removal probabilities. It is not a proof of the fixed-\(r,s\) asymptotic conjecture. At the already classical boundary \(s=n-1\), the exact expression specializes to the complete-graph coupon cover time. Older coverage under hypergraph-covering or complete-graph-walk terminology cannot be excluded solely by the searches reported here; priority needs independent bibliographic assessment.

## References

1. S. Athreya, S. Mukherjee, and S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145, initial public version dated 2023-04-03. https://arxiv.org/abs/2304.01145
2. The same authors, *On a Generalisation of the Coupon Collector Problem*, *Journal of Theoretical Probability* 38, article 54 (2025), DOI:10.1007/s10959-025-01417-w. https://doi.org/10.1007/s10959-025-01417-w
