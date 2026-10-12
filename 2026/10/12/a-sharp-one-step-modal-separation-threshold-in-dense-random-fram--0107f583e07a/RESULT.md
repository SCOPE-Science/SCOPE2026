# A sharp one-step modal separation threshold in dense random frames

## Finding
Fix \(p\in(0,1)\). Let \(G_n\sim G(n,p)\) be a simple undirected graph on \([n]\), and independently give each vertex a uniformly random color from \([q_n]\), where \(q_n\) is a sequence of positive integers satisfying
\[
\frac{q_n\log n}{n}\longrightarrow\alpha\in(0,\infty).
\]
For a vertex \(v\), define its **one-step modal signature**
\[
\sigma_n(v)=\bigl(c(v),\,\{j\in[q_n]:N(v)\cap c^{-1}(j)\ne\varnothing\}\bigr).
\]
Then
\[
\lim_{n\to\infty}\Pr\bigl(\sigma_n\text{ is injective}\bigr)=
\begin{cases}0,&\alpha<p,\\1,&\alpha>p.\end{cases}
\]
In fact, for \(\alpha<p\), with probability tending to one, \(n-o(n)\) vertices have **every** color in their open neighborhoods, and two of those vertices share their own color. The case \(\alpha=p\) is not determined.

For ordinary Kripke semantics on the adjacency relation, give the vertices the Boolean atomic predicates encoding their assigned colors. The Boolean algebra of subsets expressible by formulas of **modal depth at most one** is the full powerset \(\mathcal P([n])\) exactly when \(\sigma_n\) is injective. Thus the theorem identifies the sharp multiplicative threshold \(q_n\sim p n/\log n\) for random depth-one full separation. If \(q_n=2^{r_n}\), one may use uniformly random \(r_n\)-bit propositional valuations; for other \(q_n\), use \(\lceil\log_2 q_n\rceil\) propositions and a fixed injection of the color alphabet into Boolean words, sampling uniformly among these words.

## Assumptions and scope
The graph distribution has independent edges of probability \(p\), where \(p\) is fixed strictly between zero and one. The labels are mutually independent, uniformly distributed over \(q_n\) colors, and independent of edges. Graph adjacency is symmetric, irreflexive, and is interpreted by the ordinary existential modality \(\Diamond U=\{v:N(v)\cap U\ne\varnothing\}\). The finite Boolean algebra has complements and all Boolean combinations. The theorem concerns *modal depth at most one*; it does not assert failure of generation at unrestricted modal depth when \(\alpha<p\).

## Proof
**Logical reduction.** Let \(\chi_j\) be the propositional conjunction specifying color \(j\) (unused Boolean words, if any, do not occur). A depth-zero formula is, on this model, a union of entire color classes. Hence the truth value at \(v\) of every depth-one formula depends only on \(c(v)\) and on the set of colors represented in \(N(v)\). Conversely, all components of \(\sigma_n(v)\) are detected by the depth-zero formulas \(\chi_j\) and depth-one formulas \(\Diamond\chi_j\). Therefore two vertices satisfy the same depth-one formulas if and only if their signatures coincide. On a finite universe, injectivity is equivalent to definability of every singleton by a Boolean conjunction of these component tests; singletons then generate the full powerset.

**Failure below the threshold.** Let \(B_n\) count pairs \((v,j)\in[n]\times[q_n]\) for which no neighbor of \(v\) has color \(j\). For each fixed pair \((v,j)\), independence of the other \(n-1\) labels and incident edges gives
\[
\Pr\bigl(N(v)\cap c^{-1}(j)=\varnothing\bigr)=\left(1-\frac p{q_n}\right)^{n-1}.
\]
Consequently
\[
\frac{\mathbb E B_n}{n}=q_n\left(1-\frac p{q_n}\right)^{n-1}
=\frac{\alpha+o(1)}{\log n}\,n^{1-p/\alpha+o(1)}.
\]
If \(\alpha<p\), this tends to zero. By Markov's inequality, \(B_n=o_{\Pr}(n)\); thus \(n-o_{\Pr}(n)\) vertices see every color. Since \(q_n=o(n)\), with probability tending to one two such vertices have the same own color, so their signatures are equal.

**Separation above the threshold.** Fix different vertices \(v,w\). If their own colors differ, their signatures differ. Condition on the event \(c(v)=c(w)=c\). For each \(j\ne c\), let \(M_j\) be the number of the other \(n-2\) vertices of color \(j\), and put \(a_j=(1-p)^{M_j}\). Conditional on all vertex labels, the two independent incident-edge families make the indicators \(N(v)\cap c^{-1}(j)\ne\varnothing\) and \(N(w)\cap c^{-1}(j)\ne\varnothing\) independent Bernoulli variables with probability \(1-a_j\). The pairs of indicators for distinct \(j\ne c\) are independent. Therefore, with \(Y=\sum_{j\ne c}a_j(1-a_j)\),
\[
\Pr\bigl(\sigma_n(v)=\sigma_n(w)\mid(c(u))_{u\in[n]}\bigr)
\le\prod_{j\ne c}\bigl(1-2a_j(1-a_j)\bigr)
\le e^{-2Y}.
\]
(The excluded common-own-color class can only add distinguishing information.)

It remains to show that \(Y\) is polynomially large with overwhelmingly high probability. Let \(\lambda=(n-2)/q_n\), take independent Poisson variables \(Z_1,\ldots,Z_{q_n}\) of mean \(\lambda\), and set \(T_j=(1-p)^{Z_j}(1-(1-p)^{Z_j})\). The variables \(T_j\) are independent and lie in \([0,1/4]\). The Poisson probability generating function gives
\[
\mathbb E T_j=e^{-p\lambda}-e^{-p(2-p)\lambda}.
\]
For the sum over \(j\ne c\), write
\[
\mu=(q_n-1)\bigl(e^{-p\lambda}-e^{-p(2-p)\lambda}\bigr)
=\frac{\alpha+o(1)}{\log n}\,n^{1-p/\alpha+o(1)}.
\]
When \(\alpha>p\), \(\mu\) grows as a positive power of \(n\), up to subpolynomial factors. The standard multiplicative Chernoff bound for independent random variables in \([0,1]\), applied to \(4T_j\), gives
\[
\Pr\left(\sum_{j\ne c}T_j<\mu/2\right)\le e^{-\mu/2}.
\]
Conditioning on \(\sum_{j=1}^{q_n}Z_j=n-2\) gives precisely the multinomial occupancy vector of the original \(n-2\) independent colors. The conditioning event has probability \(\Theta(n^{-1/2})\) by Stirling's formula, so in the original model
\[
\Pr(Y<\mu/2)\le O(\sqrt n)e^{-\mu/2}.
\]
Combining this with the preceding conditional signature inequality gives, uniformly for each fixed pair of vertices with the same own color,
\[
\Pr(\sigma_n(v)=\sigma_n(w)\mid c(v)=c(w))
\le O(\sqrt n)e^{-\mu/2}+e^{-\mu}.
\]
The right side is \(o(n^{-2})\). A union bound over at most \(\binom n2\) pairs yields injectivity with probability tending to one.

## Verification
The standalone script `verify.py` exhaustively tests 6,519 graph/color configurations on at most four vertices against an independent enumeration of all depth-zero Boolean color unions and their depth-one diamonds. It also checks the exact finite expectation \(nq(1-p/q)^{n-1}\) for six small \((n,q)\) cases at \(p=1/2\), and produces nine fixed-seed finite random-graph illustrations. Run `python3 verify.py` with standard Python 3; no third-party packages are needed. Its expected final output is `VERIFY_OK`. All asymptotic steps above are mathematical deductions; no finite experiment certifies a limiting probability.

## Relationship to prior work
Alcón, Gutiérrez, Hernando, Mora and Pelayo introduced **neighbor-locating proper colorings** in 2018: equal-colored vertices must see different sets of neighbor colors, *and each color class is independent*. Their Definition 1 and order bounds concern properly colored deterministic graphs, not independent uniformly random (generally nonproper) labels on dense binomial random graphs. Chakraborty, Foucaud, Nandi, Sen and Supraja (first public version 2023) establish extremal and complexity results for the proper-coloring version on sparse graphs, again not this probability threshold. The nonproper color-neighborhood test is the natural depth-one logical counterpart of that graph-theoretic definition. Ten Cate and Koudijs (2022) study finite characterizability of modal formulas; their subject of finite logical separation motivates the modal perspective but does not give a random-frame color-alphabet threshold. Standard occupancy and Poisson concentration tools are used here and not claimed as new. No claim is made that the purely combinatorial signature criterion itself is new.

## Limitations
The critical regime \(q_n\log n/n\to p\) is unresolved. The failure half is for **depth-one** formulas only: later modal refinements may distinguish some or all vertices. The graph is undirected, loopless, dense with fixed edge probability, and vertex colors are sampled independently; proper colorings, sparse graph regimes, nonuniform color probabilities, and optimized (rather than random) valuations are outside this result. A historically equivalent probability theorem under another terminology may exist.

## References
1. L. Alcón, M. Gutiérrez, C. Hernando, M. Mora, and I. M. Pelayo, *Neighbor-Locating Colorings in Graphs*, arXiv:1806.11465v1, first public 2018-06-29, especially Definition 1 and Theorem 1. https://arxiv.org/abs/1806.11465
2. B. ten Cate and R. Koudijs, *Characterising Modal Formulas with Examples*, arXiv:2206.06049v1, first public 2022-06-13, especially Section 3. https://arxiv.org/abs/2206.06049
3. D. Chakraborty, F. Foucaud, S. Nandi, S. Sen, and D. K. Supraja, *On locating and neighbor-locating colorings of sparse graphs*, arXiv:2301.13557v1, first public 2023-01-31, especially the main results and conclusions. https://arxiv.org/abs/2301.13557
