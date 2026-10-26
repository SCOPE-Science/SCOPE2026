# Distribution-free Gödel-modal trichotomy and independent extreme scales

## Finding
Consider one root of a finite, unrestricted fuzzy Gödel–Kripke model with \(n\geq1\) designated successor targets. Write \(r_i\) for the accessibility degree to target \(i\), and \(p_i\) for the atomic truth degree there. All other outgoing edges, if any, have degree zero. Put
\[
B=\min_{1\leq i\leq n}(r_i\Rightarrow p_i),\qquad
D=\max_{1\leq i\leq n}\min(r_i,p_i),
\]
where the Gödel residuum is \(a\Rightarrow b=1\) for \(a\leq b\), and \(a\Rightarrow b=b\) otherwise. These are precisely the truth degrees of \(\Box p\) and \(\Diamond p\) at the root.

**Theorem, distribution-free part.** Suppose the pairs \((r_i,p_i)\) are independent, each pair has an exchangeable law (interchanging its entries does not change the law), and almost surely there are no within-pair ties and the \(n\) local minima \(m_i=\min(r_i,p_i)\) are distinct. The pairs need not be identically distributed. Then
\[
\Pr(B>D)=2^{-n},\qquad
\Pr(B=D)=2^{-n},\qquad
\Pr(B<D)=1-2^{1-n}.
\]
The three-way comparison category is independent of the complete collection of unordered pairs \(\{r_i,p_i\}\), and hence independent of \(D\). In particular, even with atomless inputs, the two modal truth degrees coincide with positive probability.

**Theorem, complete joint law.** Suppose additionally that all \(2n\) inputs are independent and have the same atomless continuous distribution function \(F\) on \([0,1]\). Set \(U=F(B)\), \(V=F(D)\), and \(h(t)=t-t^2/2\). Then, for \(0\leq u<1\) and \(0\leq v\leq1\),
\[
\Pr(U>u,V\leq v)=\bigl(h(v)+[h(v)-h(u)]_+\bigr)^n,
\quad [z]_+=\max(z,0).
\]
The two singular components of this joint distribution have matching cumulative masses:
\[
\Pr(U=1,V\leq v)=\Pr(U=V,V\leq v)=h(v)^n.
\]
On the open wedge \(0<u<v<1\), the remaining probability measure has density
\[
f_{U,V}(u,v)=2n(n-1)(1-u)(1-v)
\bigl(2h(v)-h(u)\bigr)^{n-2}
\]
for \(n\geq2\), with total mass \(1-2^{1-n}\). For \(n=1\), this open-wedge mass is zero.

**Theorem, distinct extreme scales.** As \(n\to\infty\),
\[
\bigl(nU,\sqrt n(1-V)\bigr)
\xrightarrow{d}(E,T),
\]
where \(E\) and \(T\) are independent, \(\Pr(E>s)=e^{-s}\) and \(\Pr(T>t)=e^{-t^2}\) for \(s,t\geq0\). The first coordinate is exponential and the second has a Rayleigh-type distribution. This theorem concerns semantic truth degrees, not the probability connective of a probabilistic modal logic.

## Assumptions and scope
The probabilistic distribution is placed on a finite row of a fuzzy accessibility relation and on an independently sampled atomic valuation. No reflexivity, transitivity, or other frame condition is assumed. Every finite Gödel–Kripke model is witnessed. Zero-weight edges outside the designated row do not affect the displayed modal evaluations. For the distribution-free part, the unordered values of different pairs are independent and their conditional orientation is fair; no common marginal distribution is needed. Distinct local minima and absence of within-pair ties are used to characterize modal equality. For the explicit joint law and scaling limit, all inputs share one continuous atomless \(F\), but \(F\) need not be uniform. We use \(F(1)=1\), and transform all input values by \(F\) using the probability-integral transform.

## Proof
For each \(i\), put \(m_i=\min(r_i,p_i)\) and \(M_i=\max(r_i,p_i)\). Let \(\varepsilon_i=1\) when \(r_i>p_i\) and \(\varepsilon_i=0\) when \(r_i<p_i\). The local diamond contribution always equals \(m_i\); the local box contribution equals \(m_i\) if \(\varepsilon_i=1\), and equals \(1\) if \(\varepsilon_i=0\). Therefore
\[
D=\max_i m_i,
\quad
B=\begin{cases}1,&\{i:\varepsilon_i=1\}=\varnothing,\\
\min_{\varepsilon_i=1}m_i,&\text{otherwise.}
\end{cases}
\]

By within-pair exchangeability and the absence of ties, conditional on the unordered pair \(\{r_i,p_i\}\), its orientation \(\varepsilon_i\) is a fair binary coin. Independence across pairs makes these coins mutually independent even after conditioning on every unordered pair. Because the \(m_i\) are distinct, there is one maximizing index \(j\). All-zero orientations give \(B=1>D\). Exactly the orientation with \(\varepsilon_j=1\) and all other orientations zero gives \(B=D=m_j\). Every other orientation has some reversed pair below the maximal minimum, giving \(B<D\). Each of the first two patterns has conditional probability \(2^{-n}\), uniformly over the unordered data. This proves the trichotomy and independence assertion, including the boundary \(n=1\).

For the iid common-\(F\) part, the probability-integral transform reduces the unordered rank calculations to independent \(\mathrm{Unif}(0,1)\) pairs, without changing their strict order or which branch of the Gödel residuum applies. Write the transformed inputs as \((x_i,y_i)\). For \(u<1\), the event \(U>u,V\leq v\) requires, for every index \(i\), either \(x_i\leq y_i\) and \(x_i\leq v\), or \(x_i>y_i\) and \(u<y_i\leq v\). The first alternative has area
\[
\int_0^v(1-x)\,dx=h(v),
\]
and the second has area \([h(v)-h(u)]_+\). Independence across the \(n\) inputs proves the displayed joint survival–distribution formula.

The maximal local minimum \(V\) has distribution \(\Pr(V\leq v)=(2h(v))^n\). The orientation trichotomy is independent of \(V\), so multiplying its two rare-category probabilities \(2^{-n}\) by \((2h(v))^n\) yields the two claimed singular cumulative masses. The only remaining component is supported on \(0<U<V<1\). On its interior, differentiating \(\Pr(U>u,V\leq v)=(2h(v)-h(u))^n\) first in \(v\) and then with a negative sign in \(u\) yields the stated density. Its mass is the complement \(1-2^{1-n}\).

For any \(s,t\geq0\) and all sufficiently large \(n\), set \(u=s/n\) and \(v=1-t/\sqrt n\), so \(u<v\). The joint formula gives
\[
\Pr(nU>s,\sqrt n(1-V)\geq t)
=\Bigl(2h(1-t/\sqrt n)-h(s/n)\Bigr)^n
=\left(1-\frac{s+t^2}{n}+O(n^{-2})\right)^n
\longrightarrow e^{-s-t^2}.
\]
For fixed \(s,t\), the error estimate follows from \(h(s/n)=s/n-s^2/(2n^2)\), while \(2h(1-t/\sqrt n)=1-t^2/n\) exactly. The one-coordinate survival limits are recovered by taking one threshold zero. Their factorization, with continuous limiting marginals, proves joint convergence to the independent claimed laws.

Both symmetry and atomlessness have a role. For example, if \(n=1\), \(r\) has density \(2r\) on \([0,1]\), and \(p\) is independent uniform, then \(\Pr(B>D)=1/3\), whereas \(\Pr(B=D)=2/3\); the two marginals are not exchangeable. If the pair is deterministically \((1/2,1/2)\), the atomless/no-tie hypothesis fails and only \(B>D\) occurs.

## Verification
Run `python3 checker.py` in the directory containing this document and the included standalone checker. It exhaustively checks every orientation of distinct prescribed local minima for \(1\leq n\leq11\) against the defining modal operations; each case has exactly one orientation with \(B>D\) and one with \(B=D\). It also runs 160,000 reproducibly seeded independent-uniform trials for each of \(n=1,2,3,5,7\), comparing empirical categories and three bivariate probabilities to the exact formula, and checks endpoint normalization. Expected last line: `ALL_CHECKS_OK`. The proof above, not these finite or simulated checks, establishes the general and asymptotic statements.

## Relationship to prior work
Ferrari, Fiorentini, Giardini and Rodriguez (2026) introduce witnessed Gödel modal models, a refutation calculus and the finite-model property. Caicedo and Rodríguez (2011) give the same bimodal algebraic semantics and completeness theory. These sources supply the interpretation of \(\Box\) via Gödel residuation and \(\Diamond\) via minimum, but the inspected material gives no sampled-row trichotomy, joint distribution, or extreme-scale theorem. Li, Yu and Liu (2025) study random fuzzy matrices under iterative max–min transitive closure; their random object and functional differ from the paired box/diamond truth degrees here. Kozhemiachenko and Sedlár (2026) study probabilistic fuzzy modal specifications with Łukasiewicz/Product outer connectives and probability measures on events, not the current random Gödel accessibility-and-valuation construction. Published results on ordinal regradings of finite Gödel frames and earlier finite Gödel modal identities concern validity or definability rather than this joint sampling law.

## Limitations
The theorem does not assert a frame-valid modal equation, and it does not apply to arbitrary correlated accessibility and valuation rows, reflexive rows with imposed diagonal weight, or sampled values with ties. The explicit density is stated in probability-rank coordinates and need not be a Lebesgue density in original truth coordinates when the common law is singular. No theorem on nested formulas or random whole-frame satisfiability follows. An equivalent distribution theorem may exist under order-statistic or random-fuzzy-relation terminology beyond the inspected literature. The computations are finite checks and simulations, not exhaustive evidence for all sizes.

## References
1. M. Ferrari, C. Fiorentini, P. Giardini and R. O. Rodriguez, *A Gödel Modal Logic Over Witnessed Models*, arXiv:2606.31906, first submitted 30 June 2026, https://arxiv.org/abs/2606.31906.
2. X. Caicedo and R. O. Rodríguez, *Bi-modal Gödel logic over [0,1]-valued Kripke frames*, arXiv:1110.2407v1, 11 October 2011, https://arxiv.org/html/1110.2407v1.
3. N. Li, X. Yu and W. Liu, *Max–Min Transitive Closure of Randomly Generated Fuzzy Matrix: Bernoulli and Classical Probabilistic Models*, Axioms 14 (2025), 690, https://doi.org/10.3390/axioms14090690.
4. D. Kozhemiachenko and I. Sedlár, *Reasoning About Probabilities, Actions, and Knowledge in Fuzzy Modal Logic*, KR 2026, pp. 429–440, https://proceedings.kr.org/2026/41/kr2026-0041-kozhemiachenko-et-al.pdf.
