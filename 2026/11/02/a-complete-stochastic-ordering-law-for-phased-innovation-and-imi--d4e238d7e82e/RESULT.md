# A complete stochastic-ordering law for phased innovation and imitation campaigns

## Finding

In the finite stochastic Bass adoption process with \(N\ge2\) potential adopters, a campaign consists of an intrinsic (external) adoption rate \(p>0\), an imitation rate \(q\ge0\), and a strictly positive duration. Consider any prescribed finite multiset of campaigns and start with no adopters. Ordering the campaigns by nonincreasing \(p/q\) (with \(q=0\) interpreted as \(+\infty\)) maximizes the *entire terminal adopter-count distribution in first-order stochastic order*. The reverse order minimizes it. In particular, every terminal tail probability \(\mathbb P(K\ge j)\), \(1\le j\le N\), and every increasing function of the number of adopters are simultaneously optimized. Equality between adjacent campaign orders holds exactly when their innovation-to-imitation cross product vanishes; for two positively long campaigns with strictly different ratios, each tail at \(j=2,\ldots,N\) differs strictly, while the tail at \(j=1\) is exactly unchanged.

The result covers **all finite populations**, all positive campaign durations and all nonnegative imitation parameters. It is a statement about a fixed multiset of externally prescribed campaigns, not an unconstrained advertising-cost optimization.

## Assumptions and scope

Fix an integer \(N\ge2\), a pure-birth count process \(K\in\{0,1,\ldots,N\}\), and a finite list of phases \(i\in\{1,\ldots,m\}\), where each has \(p_i>0\), \(q_i\ge0\), and duration \(t_i>0\). During phase \(i\), the only nonzero jump is from \(k\) to \(k+1\), at rate

\[
\lambda_i(k)=(N-k)\left(p_i+\frac{q_i k}{N-1}\right),\qquad 0\le k<N,
\]

with \(\lambda_i(N)=0\). Adoption is permanent and all coefficients remain constant within each phase. The initial state is \(K=0\) for the stochastic strictness claim; weak dominance holds from each deterministic initial state. The final time is the sum of all durations, independent of the order.

Let \(Q_i\) be the backward generator \((Q_i f)(k)=\lambda_i(k)[f(k+1)-f(k)]\), and \(P_i(t)=\exp(tQ_i)\) its Markov semigroup on bounded observables. Write \(X\succeq_{\mathrm{st}}Y\) when \(\mathbb P(X\ge j)\ge\mathbb P(Y\ge j)\) for every integer threshold \(j\). For nonzero imitation \(q\), the sorting score is \(p/q\); when \(q=0\) it is infinite. Two phases \(A,B\) have the same score exactly when \(p_Aq_B=p_Bq_A\).

## Proof

**1. Exact generator commutator.** Put \(\Delta=p_Aq_B-p_Bq_A\). Expanding both compositions of the two upper-bidiagonal birth generators gives, for each \(0\le k\le N-2\),

\[
([Q_A,Q_B]f)(k)=\frac{(N-k)(N-k-1)}{N-1}\,\Delta\,[f(k+2)-f(k+1)].
\]

For \(k=N-1,N\), the commutator is zero. This follows directly by substituting \(\lambda_A(k)=(N-k)(p_A+q_Ak/(N-1))\) and the corresponding \(B\) rate, canceling their diagonal contributions, and factoring the remaining \(k\)-to-\(k+2\) coefficient. In particular, if \(\Delta\ge0\), the commutator maps every nondecreasing \(f\) to a nonnegative function; if \(\Delta=0\), the two generators commute.

**2. Increasing-function preservation.** Every \(P_i(t)\) preserves nondecreasing functions. Couple two pure-birth chains begun at ordered integer states, using joint jumps when the states agree and independent jumps when they differ. Since jumps are only upward by one, the order cannot be reversed; once the states meet, they stay together. Thus ordered initial states yield stochastically ordered terminal states, giving the preservation claim. Each Markov semigroup also preserves pointwise nonnegativity.

**3. Finite-time swap identity.** For arbitrary \(s,t\ge0\), differentiate the conjugation \(P_A(u)P_B(t)P_A(s-u)\) and insert the analogous integral for \([Q_A,P_B(t)]\). This yields the exact finite-matrix identity

\[
P_A(s)P_B(t)-P_B(t)P_A(s)
=\int_0^s\!\int_0^t
P_A(u)P_B(v)[Q_A,Q_B]P_B(t-v)P_A(s-u)\,dv\,du.
\]

If \(\Delta\ge0\) and \(f\) is nondecreasing, the two semigroups to the right of the commutator keep it nondecreasing, the commutator is pointwise nonnegative by step 1, and the two semigroups on the left preserve nonnegativity. Therefore \(P_A(s)P_B(t)f\ge P_B(t)P_A(s)f\) pointwise. If \(\Delta=0\), equality holds for every \(f\), state, and duration; if \(\Delta<0\), the reverse inequality follows by exchanging phase labels.

**4. Sorting all phases.** Every finite permutation can be transformed into nonincreasing score order by swapping adjacent inverted pairs. The swap comparison survives arbitrary phases before or after the pair: earlier semigroups preserve nonnegativity, and later semigroups preserve nondecreasing functions. Iteration proves that the sorted permutation dominates every other permutation simultaneously for every terminal nondecreasing reward, including all indicator functions \(f_j(k)=\mathbf1_{\{k\ge j\}}\). Reverse sorting minimizes all of them. Equal-score adjacent swaps have identical transitions, so ties are immaterial.

**5. Sharp strictness and the first-adopter exception.** Take two campaigns of positive duration \(s,t\) and \(\Delta>0\), start from zero, and fix a threshold \(2\le j\le N\). In the integral in step 3, select the commutator state \(k=j-2\). For all interior \(u\in(0,s)\), \(v\in(0,t)\), the prefix \(P_A(u)P_B(v)\) reaches \(j-2\) with positive probability from zero, because all intrinsic rates are positive. The suffix \(P_B(t-v)P_A(s-u)f_j\) takes a strictly larger value at \(j\) than at \(j-1\), since the former is already adopted above threshold and the latter has positive probability of making no jump. Hence the integrand has a strictly positive contribution from state \(j-2\), establishing \(\mathbb P_{AB}(K\ge j)>\mathbb P_{BA}(K\ge j)\). For \(j=1\), the no-adoption probability is exactly

\[
\mathbb P(K=0)=\exp\!\left(-N\sum_{i=1}^m p_i t_i\right),
\]

because the total hazard while in state zero is \(Np_i\), independent of imitation and order. Thus the first tail always ties. Both statements are sharp. For two campaigns with \(\Delta=0\), all tails tie; \(\Delta<0\) reverses every strict inequality from \(j\ge2\).

## Verification

For \(N=2\), let \(A=(p_A,q_A,s)=(2,1,\log2)\) and \(B=(p_B,q_B,t)=(1,2,\log2)\). Both phases have strictly positive duration and \(\Delta=2\cdot2-1\cdot1=3>0\). Direct exact matrix exponentiation gives

\[
\mathbb P_{AB}(K=0,1,2)=(1,3,60)/64,
\qquad
\mathbb P_{BA}(K=0,1,2)=(1,6,57)/64.
\]

Consequently \(\mathbb P_{AB}(K\ge1)=\mathbb P_{BA}(K\ge1)=63/64\), whereas the full-adoption advantage is exactly \(3/64\). The total expected adoption advantage is also \(3/64\).

The accompanying standalone `CHECK.py` constructs the generators independently, verifies the commutator entries exactly for \(N=2,\ldots,10\) and three rational parameter sets (1,503 scalar identities), checks the two-person matrix exponential in exact arithmetic, and exercises 700 random finite campaign lists with matrix exponentials. These yield **45,284 passed checks** overall. They are supporting arithmetic and finite diagnostics; the all-population and all-duration assertions follow from the analytical argument above rather than finite enumeration.

To replay: install Python 3 with NumPy, SciPy, and SymPy, then execute `python CHECK.py` from the directory containing this document and the checker.

## Relationship to prior work

Bass (1969) introduced a deterministic innovation–imitation adoption equation. Niu's stochastic Bass model (working paper publicly posted July 22, 2002; journal article 2002, DOI below) introduced the finite pure-birth birth-rate mechanism used here and proved a large-population convergence result, **not** the phased campaign stochastic-order classification. Fibich, Golan and Schochet (2024) rigorously study Bass adoption with time-varying network parameters, primarily order in network size and infinite-population limits; their results do not assert this finite phase-permutation dominance. Fibich and Golan (2025) analyze time-dependent optimal promotional spending and finite-network master equations, describing a preference for early external influence, but with different unconstrained profit objectives and without this fixed-multiset all-tail rearrangement theorem. Earlier optimal advertising literature likewise emphasizes optimal spending schedules, often in deterministic formulations, rather than an exact ordering of the complete finite terminal probability distribution.

The present claim is specifically the sharp \(p/q\) score, the commutator explanation, simultaneous stochastic ordering across *all* terminal adoption thresholds and finite populations, and the strict first-versus-later threshold distinction. The stochastic model itself, the exponential-semigroup machinery, and the intuition of early external influence are prior art.

## Limitations

No claim is made for general heterogeneous graphs, contagion with abandonment, unlimited or controllable spending budgets, unprescribed duration, endogenous feedback, or discounted profit. Strict dominance concerns two genuinely different phases starting from no adopters and thresholds of at least two; the probability of at least one adoption always ties across all orders. The all-population result is an analytic theorem within the stipulated pure-birth model, not evidence that a particular empirical market obeys that model. The broad historical-priority survey includes several accessible primary texts and related work, but complete coverage of older marketing scheduling literature remains an uncertainty; independent assessment has not been performed.

## References

1. F. M. Bass (1969), *A New Product Growth Model for Consumer Durables*, Management Science 15, 215–227. https://doi.org/10.1287/mnsc.15.5.215
2. S.-C. Niu (2002), *A Stochastic Formulation of the Bass Model of New-Product Diffusion*, Review of Marketing Science Working Paper 544, first posted July 22, 2002. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=319460 ; journal version, *Mathematical Problems in Engineering* 8, 249–263, https://doi.org/10.1080/10241230215285
3. G. Fibich, A. Golan and O. Schochet (2024), *Monotone convergence of spreading processes on networks*, https://arxiv.org/abs/2407.10816
4. G. Fibich and A. Golan (2025), *Optimal promotions of new products on networks*, https://arxiv.org/abs/2504.06967
5. D. Horsky and L. S. Simon (1983), *Advertising and the Diffusion of New Products*, Marketing Science 2, 1–17. https://doi.org/10.1287/mksc.2.1.1
6. S.-C. Niu (2006), *A Piecewise-Diffusion Model of New-Product Demands*, Operations Research 54, 678–695. https://doi.org/10.1287/opre.1060.0287
