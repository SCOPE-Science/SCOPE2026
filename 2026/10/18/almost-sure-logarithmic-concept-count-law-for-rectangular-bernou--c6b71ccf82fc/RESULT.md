# Almost-sure logarithmic concept-count law for rectangular Bernoulli contexts

## Finding

For a fixed incidence probability \(p\in(0,1)\), let \(\lambda=-\log p\). Consider random formal contexts with \(r_n=n^{\alpha+o(1)}\) objects and \(m_n=n^{\beta+o(1)}\) attributes, where \(\alpha,\beta>0\), and with mutually independent Bernoulli-\(p\) incidences within each context. Write \(C_n\) for the number of formal concepts, including any concepts with empty extent or intent. **There is no assumption that the contexts at different indices are independent.** Then, for every joint construction of the contexts,

\[
\lim_{n\to\infty}\frac{\log C_n}{(\log n)^2}
=\frac{\alpha\beta}{-\log p}\qquad\text{almost surely.}
\]

The same coefficient governs the expectation:

\[
\lim_{n\to\infty}\frac{\log\mathbb E C_n}{(\log n)^2}
=\frac{\alpha\beta}{-\log p}.
\]

A stronger structural lower-bound statement holds: for each fixed \(\varepsilon\in(0,1)\), set
\[
k_n=\left\lfloor\frac{(1-\varepsilon)\log r_n}{-\log p}\right\rfloor.
\]
With probability one, **every** \(k_n\)-element attribute subset is an intent for all sufficiently large \(n\), and hence
\[
C_n\geq\binom{m_n}{k_n}\qquad\text{eventually almost surely.}
\]

For the balanced case \(r_n=m_n=n\) and \(p=1/2\), this reads \(\log C_n\sim(\log n)^2/\log 2\) almost surely. In graph terminology, \(C_n\) is the number of inclusion-maximal complete bipartite subgraphs of the associated bipartite graph, allowing the canonical empty-side cases.

## Assumptions and scope

A finite formal context \(K=(G,M,I)\) consists of finite object and attribute sets and a relation \(I\subseteq G\times M\). For \(B\subseteq M\), let \(B'\subseteq G\) be the objects incident with every attribute in \(B\). Let \(B''\subseteq M\) be the attributes shared by all objects in \(B'\). Empty intersections use their respective full universes. An **intent** is a fixed point \(B''=B\); each intent determines one and only one concept \((B',B)\). Thus \(C_n\) counts intents.

For each positive integer \(n\), the incidence indicators on \(G_n\times M_n\) are mutually independent with common success probability \(p\), with \(|G_n|=r_n\) and \(|M_n|=m_n\). The sequences \(r_n,m_n\) are deterministic positive integers satisfying \(\log r_n/\log n\to\alpha>0\) and \(\log m_n/\log n\to\beta>0\). No independence or exchangeability across different values of \(n\) is used. All logarithms are natural. The assertions concern fixed \(p\); they do not cover \(p=p_n\) approaching either endpoint.

## Proof

**1. Uniform closure of moderately small attribute sets.** Fix \(\varepsilon\in(0,1)\) and abbreviate \(r=r_n\), \(m=m_n\), \(k=k_n\). For a fixed \(B\subseteq M\) of size \(k\), the random size \(X_B=|B'|\) is binomial with parameters \(r\) and \(p^k\), hence has mean \(\mu=rp^k\geq r^\varepsilon\). The standard multiplicative binomial lower-tail inequality gives
\[
\Pr(X_B<\mu/2)\leq\exp(-\mu/8).
\]
Conditional on all incidences in the columns belonging to \(B\), and hence on the set \(B'\), incidence indicators in every other column remain independent. If \(X_B=s\), any specific attribute outside \(B\) lies in \(B''\) with probability exactly \(p^s\). By a union bound,
\[
\Pr(B''\ne B)\leq e^{-\mu/8}+m p^{\mu/2}
\leq e^{-r^\varepsilon/8}+m e^{-\lambda r^\varepsilon/2}.
\]
There are at most \(m^k\) possible choices of \(B\), and \(\log(m^k)=O((\log n)^2)\). Since \(r^\varepsilon=n^{\alpha\varepsilon+o(1)}\), the bound on the probability that **any** \(k\)-element subset is nonclosed is summable over \(n\). The first Borel–Cantelli lemma, without any independence assumption across indices, implies that eventually every such \(B\) is closed. Their corresponding concepts are distinct. Finally, using \(k=O(\log n)\) and \(m=n^{\beta+o(1)}\),
\[
\log\binom{m}{k}
=k\log m-O(k\log(k+1))
=\frac{1-\varepsilon}{\lambda}(\log r)(\log m)+o((\log n)^2).
\]
This proves the almost-sure lower limiting bound with coefficient \((1-\varepsilon)\alpha\beta/\lambda\).

**2. Reduction of large concepts to all-one rectangles.** Fix again \(\varepsilon\in(0,1)\). Put
\[
A=\left\lceil\frac{(1+\varepsilon)\log m}{\lambda}\right\rceil,
\qquad B=\left\lceil\frac{(1+\varepsilon)\log r}{\lambda}\right\rceil.
\]
Concepts with fewer than \(A\) objects are at most \(\sum_{a<A}\binom ra\), because a concept is determined uniquely by its extent; those with fewer than \(B\) attributes are at most \(\sum_{b<B}\binom mb\), because it is also determined uniquely by its intent. These two deterministic contributions satisfy
\[
\log\left(1+\sum_{a<A}\binom ra+\sum_{b<B}\binom mb\right)
\leq\frac{1+\varepsilon}{\lambda}(\log r)(\log m)+o((\log n)^2).
\]
For the remaining concepts the extent has at least \(A\) objects and the intent at least \(B\) attributes. Each such concept determines a distinct all-one rectangle. If \(R\) is the total number of all-one rectangles of sizes \(a\geq A\), \(b\geq B\), then
\[
\mathbb E R=\sum_{a=A}^r\sum_{b=B}^m\binom ra\binom mb p^{ab}
\leq rm\exp\bigl(A\log r+B\log m-\lambda AB\bigr).
\]
Indeed, with \(f(a,b)=a\log r+b\log m-\lambda ab\), its increment in \(a\) is \(\log r-\lambda b\leq-\varepsilon\log r\) and its increment in \(b\) is \(\log m-\lambda a\leq-\varepsilon\log m\); thus \(f\) is maximal at \((A,B)\) throughout the summation region. The displayed upper bound therefore has logarithm at most
\[
\frac{1-\varepsilon^2}{\lambda}(\log r)(\log m)+O(\log r+\log m).
\]
For sufficiently large \(n\), Markov's inequality gives
\[
\Pr\left\{R>\exp\left(\frac{1-\varepsilon^2/2}{\lambda}
 (\log r)(\log m)\right)\right\}
\leq\exp\left(-c_\varepsilon(\log n)^2\right)
\]
for a positive constant \(c_\varepsilon\), because \((\log r)(\log m)\sim\alpha\beta(\log n)^2\). This is summable. Hence almost surely, eventually, the high-high concepts contribute at most the threshold in this inequality. Together with the deterministic small-side bound, this yields
\[
\limsup_{n\to\infty}\frac{\log C_n}{(\log n)^2}
\leq\frac{(1+\varepsilon)\alpha\beta}{\lambda}.
\]

**3. Limits and expectations.** Apply steps 1 and 2 to a countable sequence of positive rational \(\varepsilon\downarrow0\). The intersection of the corresponding probability-one events has probability one; the lower and upper bounds yield the claimed almost-sure limit. For expectations, the lower bound follows from \(\mathbb E C_n\geq\binom{m}{k}\Pr\{\text{all such }k\text{-subsets closed}\}\), whose probability tends to one. The deterministic small-concept bounds and the above first-moment rectangle estimate imply the matching upper bound for \(\mathbb E C_n\). Thus the same logarithmic exponent governs both the typical and expected concept counts. No second-moment hypothesis is needed.

## Verification

The accompanying standalone Python program `verify.py` enumerates all binary incidence tables of sizes \(1\leq r,m\leq4\) with \(rm\leq16\) and checks the number of intents by literal double derivation. It independently evaluates the exact closed-pair expectation identity for incidence probabilities \(1/2\), and additionally \(1/3\) and \(2/3\) for matrices containing at most nine incidence entries. All 42 finite parameter/probability combinations agreed exactly as rational numbers; the program also checks the bijection between extents and intents for further small tables. The sample expected concept counts at probability \(1/2\) are \(39/16\) for \(2\times2\), \(1977/512\) for \(3\times3\), and \(386463/65536\) for \(4\times4\). Running `python3 verify.py` prints `VERIFY_OK` on success. The analytic Chernoff, union-bound, first-moment and Borel–Cantelli proof, not finite enumeration, establishes the infinite-size assertion.

## Relationship to prior work

Kovács's 2018 paper studies independent-incidence formal contexts and derives an explicit exact model for the **mean** number of concepts, alongside computational approximation. The closed-pair summation used in our finite checker is an elementary version of that established expected-value identity; it is not claimed as new. Sakurai's first public preprint, submitted January 26, 2021, supplies a related random split-object/attribute model, an exact expectation formula, and a superpolynomial **expectation lower bound** in the half-density case. Our statement is a distinct sharp almost-sure theorem for fixed polynomially rectangular populations, with a structural simultaneous-closure property and sharp expectation upper bound. The 2020 formal-context null-model study by Felde, Hanika and Stumme identifies the coin-toss setting as a standard probabilistic baseline. The bipartite maximal-biclique interpretation is standard and does not itself establish a typical-count asymptotic.

## Limitations

The result controls the leading \((\log n)^2\) exponent only; it provides neither fluctuations nor second-order corrections, and does not determine the typical concept count up to a multiplicative factor. It assumes independent, equal-probability incidences **within** each context, a fixed \(p\in(0,1)\), and positive polynomial rates for both population sizes. No conclusion is asserted for strongly correlated entries, shrinking incidence probabilities, or non-polynomially scaling populations. The novelty comparison is made against the cited accessible primary literature and mathematical research records; an equivalent formulation in unindexed random-bipartite-graph literature is a residual risk.

## References

- L. Kovács, *Efficient approximation for counting of formal concepts generated from formal context*, Miskolc Mathematical Notes **19** (2018), 983–996. DOI: 10.18514/MMN.2018.2529. Full text: https://real.mtak.hu/92004/1/2529.pdf.
- T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023v1, first public January 26, 2021; subsequently *Information Sciences* **578** (2021), 615–620. https://arxiv.org/abs/2101.11023.
- M. Felde, T. Hanika and G. Stumme, *Null Models for Formal Contexts*, *Information* **11** (2020), article 135. DOI: 10.3390/info11030135.
- B. Ganter and R. Wille, *Formal Concept Analysis: Mathematical Foundations*, Springer, 1999, for fundamental derivation operators and concept definitions.
