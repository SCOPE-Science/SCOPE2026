# All-order moment dominance under polarisation in random \(k\)-SAT

## Finding
Let \(Z_p\) be the number of satisfying assignments of the polarised random \(k\)-SAT formula specified below. For integers \(n\ge k\ge2\), \(m\ge2\), \(r\ge1\), and real \(0\le p<q\le1/2\),
\[
\mathbb E[Z_p^r]>\mathbb E[Z_q^r].
\]
The family of falling-factorial moments is ordered too:
\[
\mathbb E[(Z_p)_r]\ge\mathbb E[(Z_q)_r],\qquad r\ge1,
\]
where \((z)_r=z(z-1)\cdots(z-r+1)\) counts ordered distinct choices. The factorial-moment inequality is not asserted to be strict for all orders. For a single clause, every formula has exactly \(2^n-2^{n-k}\) satisfying assignments, and equality holds. For \(k=1\), the model is independent of \(p\).

## Assumptions and scope
There are \(n\) Boolean variables. A clause selects uniformly a \(k\)-element variable set, flips an independent fair common sign coin, then independently flips each of its \(k\) signs with probability \(p\). All clause selections, common coins and within-clause flips are independent across the \(m\) clauses. The case \(p=1/2\) is classical random \(k\)-SAT and \(p=0\) uses a fair choice between the two all-equal sign patterns. Repeated clauses are permitted. The result concerns finite \(n,k,m,r\); there is no limit theorem or restriction to clauses below the satisfiability threshold.

## Proof
Write \(\mathcal X=\{0,1\}^n\), with coordinatewise XOR denoted \(\oplus\). For an ordered \(r\)-tuple \(\boldsymbol\sigma=(\sigma_1,\ldots,\sigma_r)\in\mathcal X^r\), define
\[
a_p(\boldsymbol\sigma)=\Pr\{\text{one polarised clause at }p\text{ is satisfied by every }\sigma_i\}.
\]
Clause independence gives the **exact moment identity**
\[
\mathbb E[Z_p^r]=\sum_{\boldsymbol\sigma\in\mathcal X^r}a_p(\boldsymbol\sigma)^m.\tag{1}
\]

Fix \(p<q\le1/2\), and put \(\varepsilon=(q-p)/(1-2p)\), so \(0<\varepsilon\le1/2\). A sign generated as a fair common coin times independent \(p\)-flips and subsequently changed by an independent \(\varepsilon\)-flip has the polarised \(q\)-law, because \(p(1-\varepsilon)+(1-p)\varepsilon=q\). Let \(U\in\mathcal X\) have independent \(\operatorname{Bernoulli}(\varepsilon)\) coordinates. Conditioning on the uniformly chosen variable set shows that the restriction of \(U\) to that clause gives exactly the required independent sign flips. Flipping clause signs is equivalent to XOR-shifting every test assignment on the same variables. Therefore
\[
a_q(\boldsymbol\sigma)=\mathbb E_U\,a_p(\sigma_1\oplus U,\ldots,\sigma_r\oplus U).\tag{2}
\]
For integer \(m\ge1\), Jensen's inequality for \(t\mapsto t^m\) and (2) give
\[
a_q(\boldsymbol\sigma)^m\le\mathbb E_U\,a_p(\boldsymbol\sigma\oplus U)^m.
\]
Summing over all ordered tuples, the map \(\boldsymbol\sigma\mapsto\boldsymbol\sigma\oplus U\) permutes \(\mathcal X^r\) for each \(U\). Equation (1) proves \(\mathbb E[Z_q^r]\le\mathbb E[Z_p^r]\). Restricting both sums to tuples of pairwise distinct assignments proves the factorial-moment inequality, because this subset is invariant under simultaneous XOR.

For strictness of the ordinary moments when \(m\ge2\), choose a diagonal tuple \(\boldsymbol\sigma=(0^n,\ldots,0^n)\). If \(\tau\) has exactly one coordinate equal to \(1\), the probability \(h_p(x)\) that one clause fails assignment \(x\) satisfies
\[
h_p(0^n)-h_p(\tau)
=\frac{k}{2n}(1-2p)\big((1-p)^{k-1}-p^{k-1}\big)>0.
\]
Indeed, a clause omitting the changed coordinate has identical failure probability, while a clause containing it contributes the positive difference; the probability of inclusion is \(k/n\). Thus \(a_p\) on diagonal tuples changes between common shifts \(U=0^n\) and \(U=\tau\), both of positive probability since \(0<\varepsilon\le1/2\). The function \(t^m\) is strictly convex on positive \(t\) for \(m\ge2\), and these one-clause probabilities are positive. Jensen is strict for this tuple. Every other tuple contributes a nonnegative difference, proving the strict raw-moment claim. For \(m=1\), any single \(k\)-clause excludes exactly \(2^{n-k}\) assignments. For \(k=1\), the fair common coin makes each literal sign fair independently of \(p\), proving the stated boundaries.

## Verification
The accompanying `verification/check.py` enumerates all possible clauses using exact rational probabilities, independently evaluates simultaneous clause-satisfaction probabilities, and sums finite moments. It checks \(n\in\{2,3\}\), \(k\in\{2,3\}\) with \(k\le n\), \(m\in\{1,2,3\}\), \(r\in\{1,2,3\}\) and \(p\in\{0,1/4,1/2\}\). It additionally tests the entire two-assignment noise-smoothing identity at \(n=3,k=2\). The program recorded 218 passed exact rational assertions. Those finite assertions are corroboration, not a proof for arbitrary parameter sizes.

## Relationship to prior work
Danielsson and Markström (2022 preprint; 2023 journal) defined precisely this polarised random \(k\)-SAT model and proved an asymptotic comparison of the probability that the formula admits at least one satisfying assignment. They also gave the expected-solution-count expression used in an upper-threshold argument. The present statement concerns **all exact finite-sample positive integer moments of the number of satisfying assignments**, plus its falling-factorial moments, and is not the same as the asymptotic satisfiability-event comparison. The 2021 work on *biased* random \(k\)-SAT concerns a different sign mechanism, without the balancing fair common coin.

## Limitations
The result does **not** imply a stochastic ordering of \(Z_p\), a finite-sample ordering of \(\Pr(Z_p>0)\), a variance ordering, or a sharp satisfiability threshold. Factorial moments need not be strictly ordered at high orders (for instance, the event that all \(2^n\) assignments satisfy a nonempty formula is impossible). Earlier equivalent statements in broad probabilistic or Boolean-noise literature remain a historical-priority risk; independent mathematical audit has not been performed.

## References
1. J. Larsson Danielsson and K. Markström, *Polarised random k-SAT*, arXiv:2204.06615, first public version 2022-04-13; *Combinatorics, Probability and Computing* 32 (2023), 885–899, doi:10.1017/S0963548323000226.
2. J. Larsson and K. Markström, *Biased random k-SAT*, *Random Structures & Algorithms* 59 (2021), 238–266, doi:10.1002/rsa.20996. Different sign model; cited for contextual comparison.
