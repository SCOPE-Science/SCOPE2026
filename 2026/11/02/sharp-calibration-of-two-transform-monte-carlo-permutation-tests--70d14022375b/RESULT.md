# Sharp calibration of two-transform Monte Carlo permutation tests

## Finding

The ordinary fixed-identity, plus-one Monte Carlo permutation p-value can remain exactly valid under some *biased* transformation draws, but the valid region depends on the number of resamples. Here is an exact, sharp, finite-sample description.

Let \(\Omega\) be finite and let \(g\) permute \(\Omega\), with longest cycle length \(L\ge2\). Let \(X\) have any \(g\)-invariant distribution and let \(T:\Omega\to\mathbb R\) be any score (ties allowed). Independently of \(X\), draw \(G_1,\ldots,G_M\) independently, each equal to the identity with probability \(a\in[0,1]\) and to \(g\) with probability \(1-a\). Use the unmodified fixed-origin statistic

\[
P_M=\frac{1+\sum_{i=1}^{M}\mathbf 1\{T(G_iX)\ge T(X)\}}{M+1},\qquad M\ge1.
\]

Write \(\delta_L=1-1/L\) and \(F_{M,a}(j)=\Pr\{\operatorname{Bin}(M,a)\le j\}\). Then for every integer \(1\le k\le M\),

\[
\Pr\!\left(P_M\le\frac{k}{M+1}\right)
=\Pr\{T(gX)<T(X)\}\,F_{M,a}(k-1)
\le\delta_L F_{M,a}(k-1).
\]

The upper bound is attained **simultaneously at all thresholds** by taking \(X\) uniform on a maximal cycle and assigning scores that decrease along all but one directed edge of that cycle. Thus the exact worst-case rejection probability at each nominal support threshold is \(\delta_L F_{M,a}(k-1)\). It follows that \(P_M\) is a valid (superuniform) null p-value for *every* invariant law and score exactly when

\[
\boxed{\ \delta_L\sum_{j=0}^{k-1}\binom Mj a^j(1-a)^{M-j}\le\frac{k}{M+1}\quad\text{for all }1\le k\le M.\ }
\]

The set of safe identity masses is the interval \([a_{M,L},1]\), where \(a_{M,L}\) is characterized by these explicit finite binomial inequalities. For every finite \(M\), \(0\le a_{M,L}<\delta_L\), but

\[
\lim_{M\to\infty}a_{M,L}=\delta_L.
\]

A concrete budget reversal occurs at \(L=3\) and \(a=27/100\): for \(M=1\) the worst rejection rate at level \(1/2\) is \(\tfrac23\cdot\tfrac{73}{100}=73/150<1/2\); for \(M=2\) the worst rejection rate at level \(1/3\) is \(\tfrac23(73/100)^2=5329/15000>1/3\). The exact minimal safe mass is \(a_{1,3}=1/4\) for one resample and \(a_{2,3}=1-1/\sqrt 2\) for two.

## Assumptions and scope

The sample space \(\Omega\) is finite; \(g\) is a bijection; the null satisfies \(X\overset d=gX\); and the transformation draws are independent of each other and of \(X\). The p-value **does not draw a random reference transformation or re-center by its inverse**. The comparison uses \(\ge\), so equality is always treated conservatively. The integers \(L\ge2\), \(M\ge1\), \(1\le k\le M\), and identity mass \(a\in[0,1]\) are unrestricted otherwise. For \(g\) equal to the identity, the p-value equals one identically and the statement has the trivial separate boundary case. Exchangeable coordinate data with a fixed coordinate permutation are a standard instance of the \(g\)-invariance assumption.

## Proof

**1. Exact rejection identity.** Set \(D=\{T(gX)<T(X)\}\). On \(D^c\), both the identity and \(g\) yield a score at least \(T(X)\), hence \(P_M=1\). On \(D\), a transformed score reaches or exceeds \(T(X)\) exactly when the sampled transformation is the identity. Conditional on \(X\in D\), the number of such draws is \(B\sim\operatorname{Bin}(M,a)\), with its distribution independent of \(X\). Thus \(P_M=(1+B)/(M+1)\) on \(D\), proving the exact displayed rejection identity.

**2. Sharp cycle bound.** Since \(g\) preserves the null law, conditional on any positive-mass \(g\)-cycle of length \(\ell\), the position of \(X\) is uniform on that cycle. Around a directed cycle, it is impossible to have a strict score decrease on every edge: that would give \(T(x)>T(gx)>\cdots>T(g^\ell x)=T(x)\). Hence at most \(\ell-1\) of its \(\ell\) directed edges satisfy \(T(gx)<T(x)\). Their fraction is at most \(1-1/\ell\le 1-1/L=\delta_L\). Mixtures across cycles preserve this bound. On a cycle of length \(L\), assign \(L\) distinct scores strictly decreasing along the first \(L-1\) steps and returning upward on the final edge; the uniform null then has \(\Pr(D)=\delta_L\). This single construction attains the rejection bound for every \(k\) and \(a\).

**3. Exact superuniformity criterion.** The only possible p-values are \(1/(M+1),\ldots,1\). For an arbitrary nominal \(\alpha\in[0,1]\), its rejection event is the event at the largest attained grid point no larger than \(\alpha\). Therefore requiring \(\Pr(P_M\le\alpha)\le\alpha\) for every \(\alpha\) is equivalent to the \(M\) stated inequalities. Sharpness in Step 2 proves necessity as well as sufficiency. Each binomial lower-tail probability \(F_{M,a}(k-1)\) decreases continuously in \(a\), so the safe set is a closed interval ending at one.

**4. The finite and asymptotic identity-mass frontiers.** For \(Y\sim\operatorname{Bin}(M+1,a)\), the binomial size-bias identity gives

\[
(M+1)aF_{M,a}(k-1)=\mathbb E\left[Y\mathbf1\{Y\le k\}\right]\le k.
\]

Thus every \(a\ge\delta_L\) is safe. At \(a=\delta_L\in(0,1)\), the inequality is strict for every \(1\le k\le M\), because \(Y\) is nondegenerate and has positive mass both at zero and above \(k\). Continuity and finiteness of the set of inequalities therefore give \(a_{M,L}<\delta_L\). Conversely fix \(a<\delta_L\), choose \(t\) with \(a<t<\delta_L\), and take \(k_M=\lfloor(M+1)t\rfloor\). The weak law for a binomial random variable gives \(F_{M,a}(k_M-1)\to1\), whereas \(k_M/(M+1)\to t<\delta_L\). Hence this \(a\) fails the finite-grid condition for all sufficiently large \(M\). This proves \(a_{M,L}\to\delta_L\).

**5. Explicit budget reversal.** For \(L=3,M=1\), the only nontrivial inequality is \((2/3)(1-a)\le1/2\), equivalent to \(a\ge1/4\). For \(L=3,M=2\), the \(k=1\) condition gives \((2/3)(1-a)^2\le1/3\), or \(a\ge1-1/\sqrt2\); the \(k=2\) condition is automatic. Substituting \(a=27/100\) yields the two exact rational rejection probabilities stated above.

## Verification

The standalone file `verify_two_transform.py` uses rational arithmetic to enumerate all strict score rankings of cycles with lengths \(2\) through \(6\), all transformation draws with \(1\) through \(4\) resamples, and five rational identity probabilities. It independently compares each exact finite null rejection probability with the theorem's binomial formula and bound, verifies extremal descending profiles and the two-resample budget reversal, and checks a broader finite collection of binomial identities. The completed run reported **78,579 passed deterministic checks**. The proof above, not finite enumeration, establishes the infinite families of assertions.

## Relationship to prior work

Ramdas, Barber, Candès and Tibshirani (2022, Theorem 2) prove validity for arbitrary transformation distributions using a **random reference transformation** and composition with its inverse. Their result covers a stronger range of sampling distributions after this algorithmic correction, but does not imply validity or a sharp calibration criterion for the different, fixed-identity statistic studied here. Their Section 2 explicitly warns that omitting the correction can cause anti-conservatism. Hemerik and Goeman (2018, Theorem 2) justify conventional fixed-identity Monte Carlo permutation p-values with **uniform** draws from a group; that theorem handles the uniform special case but not a sharp admissible interval of *biased* two-point draws. Phipson and Smyth (2010) address correction of randomly drawn permutation p-values, principally under appropriately uniform random sampling. The present contribution is the sharp all-threshold characterization and finite-resample budget dependence for fixed-origin two-transform sampling; it is not a replacement for the generally valid random-reference construction.

## Limitations

The theorem is confined to independent identity/one-fixed-permutation sampling and a finite invariant space. It does not characterize arbitrary nonuniform distributions on more than two transformations, dependent resamples, or noninvariant nulls; neither does it give a power-optimal choice of identity mass. Universal sharpness allows deliberately chosen score functions and null laws, and may overstate miscalibration for a fixed practical statistic. Self-review has been performed; independent mathematical audit has not. A hidden equivalent in earlier general nonuniform-permutation literature remains possible.

## References

1. A. Ramdas, R. F. Barber, E. J. Candès and R. J. Tibshirani, *Permutation tests using arbitrary permutation distributions*, arXiv:2204.13581 (first public 2022-04-28), Theorem 2 and Section 2. https://arxiv.org/abs/2204.13581
2. J. Hemerik and J. Goeman, *Exact testing with random permutations*, TEST 27 (2018), 811–825; online 2017-11-30. https://doi.org/10.1007/s11749-017-0571-1
3. B. Phipson and G. K. Smyth, *Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn*, Statistical Applications in Genetics and Molecular Biology 9 (2010), Article 39. https://arxiv.org/abs/1603.05766
