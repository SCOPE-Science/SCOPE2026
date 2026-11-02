# Exponential bottleneck hierarchy for flat-weight surviving-label elections

## Finding

Consider a population with \(n\ge3\) labelled candidates, initially all active. At each integer round, each of the \(n\) voters independently chooses uniformly among the currently active candidates; candidates with no new votes cease to be active forever. Let \(K_t\) be the number of active candidates after round \(t\), with \(K_0=n\), and let \(T_n=\inf\{t\ge0:K_t=1\}\). For \(2\le k\le n\), let \(H_{n,k}=\#\{0\le t<T_n:K_t=k\}\), including zero if state \(k\) is skipped.

For every fixed integer \(r\ge2\), as \(n\to\infty\),

\[
\bigl(H_{n,k}/(k/(k-1))^n\bigr)_{k=2}^r
\;\Longrightarrow\; (E_k)_{k=2}^r,
\]

where the \(E_k\) are *independent* exponentials of respective rates \(k\). In particular, \(T_n/2^{n-1}\Longrightarrow\operatorname{Exp}(1)\), while the two largest exponential scales in the expected absorption time satisfy

\[
\boxed{\mathbb E T_n=2^{n-1}+\frac13(3/2)^n+O\bigl(n(4/3)^n\bigr).}
\]

These conclusions jointly describe an ordered hierarchy of rare-candidate extinctions; the secondary \((3/2)^n\) contribution is resolved even though it disappears at the primary \(2^n\) scale.

## Assumptions and scope

The number \(n\) of voters is constant over time, the selections are conditionally independent and uniform over **currently surviving** labels, and extinction is permanent. A candidate with \(m\ge1\) votes has weight one, and a candidate with zero votes has weight zero. This is the *flat-weight boundary variant* of the power-weight voting dynamics studied in the cited conclave paper; that paper assumes a strictly increasing weight function and, specifically, fixed \(\alpha>0\). The case here is separately defined and is not claimed to be covered by that assumption. All distributional limits hold with fixed \(r\) as \(n\to\infty\). The displayed expectation estimate uses an absolute implicit constant for sufficiently large \(n\).

## Proof

**1. Exact occupancy transition.** Conditional on \(K_t=k\), the next votes are \(n\) independent uniform draws among the \(k\) labels. If \(S(n,j)\) denotes a Stirling number of the second kind, then for \(1\le j\le k\),

\[
P_n(k,j)=\Pr(K_{t+1}=j\mid K_t=k)
=\binom{k}{j}\frac{j!S(n,j)}{k^n}.
\]

Thus \(K_t\) is a nonincreasing Markov chain and \(1\) is absorbing. Let \(q_{n,k}=1-P_n(k,k)\), the strictly positive probability of leaving \(k\) on a given round. A fixed active label can be missed, so

\[
q_{n,k}\ge\left(\frac{k-1}{k}\right)^n.
\]

For each *fixed* \(k\), inclusion-exclusion applied to at least one empty label gives

\[
q_{n,k}=\sum_{i=1}^k(-1)^{i+1}\binom{k}{i}\left(\frac{k-i}{k}\right)^n
=k\left(\frac{k-1}{k}\right)^n\bigl(1+o(1)\bigr).
\]

In particular, \(q_{n,2}=2^{1-n}\) and \(q_{n,3}=3(2/3)^n-3(1/3)^n\).

**2. A fixed low state is not skipped.** To jump from \(k\ge j+1\) directly to at most \(j-1\), all \(n\) draws must lie in some set of \(j-1\) labels. The union bound and the preceding lower bound give

\[
\Pr(K_{t+1}\le j-1\mid K_t=k,\ K_{t+1}<k)
\le\binom{k}{j-1}\left(\frac{j-1}{k-1}\right)^n.
\]

There are at most \(n\) strict decreases in the entire path. Consequently, for each fixed \(j\ge2\),

\[
\Pr(\text{state }j\text{ is skipped})
\le n^j\left(\frac{j-1}{j}\right)^n=o(1).
\]

This bound also covers paths that skip several levels at once. For fixed \(r\), a union bound shows that every state \(2,\ldots,r\) is visited with probability tending to one.

**3. Independent exponential clocks.** At state \(k\), the number of rounds before the first strict decrease (counting the departing round) is geometric with success parameter \(q_{n,k}\). Its duration is independent of the destination of that decrease. Because the chain only moves downward, its entire path may be constructed using independent geometric random variables \(G_{n,k}\), one for each state \(k\), and independently sampled departure destinations. On a visit to \(k\), \(H_{n,k}=G_{n,k}\); otherwise \(H_{n,k}=0\). For each fixed \(k\),

\[
q_{n,k}(k/(k-1))^n\longrightarrow k,
\]

so the standard geometric-tail calculation gives \(G_{n,k}/(k/(k-1))^n\Longrightarrow\operatorname{Exp}(k)\). Joint independence holds already for the auxiliary geometric variables, and Step 2 removes the negligible skipped-state discrepancy. This proves the joint limit.

**4. Sharp mean through two distinct exponential scales.** Since visiting \(k\) is independent of \(G_{n,k}\),

\[
\mathbb E T_n=\sum_{k=2}^{n}\frac{\Pr(\text{visit }k)}{q_{n,k}}.
\]

For \(k\ge4\), the lower bound in Step 1 gives \(q_{n,k}^{-1}\le(4/3)^n\), hence their total contribution is at most \(n(4/3)^n\). Step 2 gives \(\Pr(\text{skip }2)\le n^2 2^{-n}\) and \(\Pr(\text{skip }3)\le n^3(2/3)^n\). Therefore, dropping the visit factors in the two smallest states incurs at most \(O(n^3)\) absolute error. Finally,

\[
q_{n,2}^{-1}=2^{n-1},\qquad
q_{n,3}^{-1}=\frac{(3/2)^n}{3(1-2^{-n})}
=\frac13(3/2)^n+O((3/4)^n).
\]

We obtain \(\mathbb E T_n=2^{n-1}+\frac13(3/2)^n+O\bigl(n(4/3)^n+n^3\bigr)\). Since \(n^3=O(n(4/3)^n)\), the claimed remainder follows. For the absorption-time limit, the expected total time spent above state \(2\) is at most \(n(3/2)^n=o(2^n)\). Together with Step 2 and the geometric limit at \(k=2\), this implies \(T_n/2^{n-1}\Longrightarrow\operatorname{Exp}(1)\).

## Verification

The independently runnable Python file `checker.py` computes exact rational one-round transition probabilities from Stirling numbers, checks their normalization, the boundary escape probabilities and their lower bounds, recursively computes finite expected absorption times, and checks finite state-visitation probabilities against the analytic skip estimates. It reports 625 passing exact-rational assertions. Those finite computations corroborate algebraic identities only; the fixed-state asymptotic hierarchy and the infinite-\(n\) bound are proved in Steps 1--4.

## Relationship to prior work

Benjamini, Cai, Chen, Gong and Li (2026) study the power-weight conclave process for \(\alpha>0\). Their Theorem 1.5 gives an exponential lower bound for absorption when \(0<\alpha<1\), but does not address flat weights, the exact multiscale holding-time joint law or the two exponential terms in the mean. The classical occupancy formula (as recorded by Weisstein after Feller) supplies the single-round transition kernel used in Step 1, not a multiround extinction analysis. Cancrini and Posta (2020) study a different repeated-balls-into-bins chain that permits all bins to be refilled and is not a monotone extinction chain. Related published occupancy analyses were compared at the level of these objects and implications.

## Limitations

This is a boundary extension, not a theorem for any *fixed positive* power exponent. It says nothing about crossover as a positive exponent tends to zero with the population size. It establishes fixed-finite-dimensional convergence of low-state holding times, not simultaneous convergence over a growing number of levels. Independent mathematical validation and a definitive exhaustive historical priority determination are not claimed. The finite checker does not prove an asymptotic theorem.

## References

1. I. Benjamini, Z. Cai, G. Chen, S. Gong and Z. Li, *The Conclave Process* (2026), first public 2026-07-24, https://arxiv.org/abs/2607.22324 .
2. E. W. Weisstein, *Classical Occupancy Problem*, MathWorld, https://mathworld.wolfram.com/ClassicalOccupancyProblem.html (including its reference to Feller's 1968 text).
3. N. Cancrini and G. Posta, *Mixing time for the Repeated Balls into Bins dynamics* (2020), https://arxiv.org/abs/2001.11246 .
