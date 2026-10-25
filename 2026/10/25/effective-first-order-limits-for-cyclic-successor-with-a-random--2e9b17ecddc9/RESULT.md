# Effective first-order limits for cyclic successor with a random perfect matching

## Finding

Let \(N\) range through the positive even integers. On \(V_N=\{0,\ldots,N-1\}\), fix the successor function \(S_N(i)=i+1\pmod N\), and choose \(M_N\) uniformly from all fixed-point-free involutions of \(V_N\), independently of the fixed successor. Consider the first-order structures \(\mathcal A_N=(V_N,S_N,M_N)\) in the language of two unary functions.

**Theorem.** Every first-order sentence \(\varphi\) has an effectively computable limit \(\lim_{N\to\infty,\ 2\mid N}\Pr(\mathcal A_N\models\varphi)\). Its value is the probability of a finite Boolean combination of threshold events \(Z_H\ge t\), where \((Z_H)_H\) are mutually independent Poisson random variables indexed by the finite admissible coloured cycle cores \(H\) defined below, with means
\[
\mathbb E Z_H=\frac{1}{|\operatorname{Aut}(H)|}.
\]
Conversely, every finite Boolean combination of these threshold events is the limit event of a first-order sentence. Thus this construction is a complete description of the attainable first-order limit spectrum. Each limit lies in \(\mathbb Q[e^{-1/D}]\) for an effectively computable positive integer \(D\) depending on the sentence, and the spectrum is dense in \([0,1]\).

In particular, for any fixed distinct positive integers \(\ell_1,\ldots,\ell_m\), the counts
\[
X_{N,\ell}=\#\{i\in V_N:M_N(i)=S_N^{\ell}(i)\}
\]
converge jointly to independent \(\operatorname{Poisson}(1)\) variables. For any finite nonempty set \(F\) of positive integers,
\[
\Pr\bigl(\forall\ell\in F\ \exists i\ M_N(i)=S_N^{\ell}(i)\bigr)
\longrightarrow (1-e^{-1})^{|F|}.
\]
(The distinct-index definition of \(X_{N,\ell}\) is unambiguous for all sufficiently large \(N>2\ell\).)

## Assumptions and scope

A coloured cycle core is a finite connected multigraph \(H\) of cyclomatic number one, with edges of two distinct kinds: directed \(S\)-edges and undirected \(M\)-edges. Every vertex has degree two counting both edge kinds with multiplicity; the \(S\)-edges form a disjoint union of nonempty directed paths, with at most one incoming and one outgoing \(S\)-edge at any vertex; the \(M\)-edges form a matching; and there are no loops. Parallel \(S\)- and \(M\)-edges are permitted, giving a coloured two-edge cycle. Isomorphisms and automorphisms preserve both edge kinds and the direction of each \(S\)-edge.

Every such core consists of \(k\ge1\) directed \(S\)-path segments with their \(2k\) endpoints paired cyclically by exactly \(k\) matching edges. For each core \(H\), let \(C_N(H)\) be the number of submultigraphs in \(\mathcal A_N\) isomorphic to \(H\), using all the specified \(S\)- and \(M\)-edges but not requiring inducedness. These are unlabelled occurrences, i.e. embeddings divided by \(|\operatorname{Aut}(H)|\). The theorem asserts joint convergence of all finite subfamilies of \(C_N(H)\) to \(Z_H\).

The underlying cyclic successor is named but the choice of a starting point is not. The language does not contain a full linear or cyclic *order* relation, an arbitrary crossing relation on chords, second-order quantification, or a constant naming a vertex. First-order terms of arbitrary fixed depth are allowed.

## Proof

### 1. Matching probability and expected core counts

For any \(b\) prescribed disjoint unordered pairs on \(V_N\), uniform matching gives the exact probability
\[
p_N(b)=\prod_{j=0}^{b-1}\frac{1}{N-(2j+1)}.
\]
Indeed, condition on each specified pair successively, leaving a uniform matching on the unused vertices. If the proposed pairs share an endpoint, their simultaneous probability is zero unless they are identical.

Fix an admissible core \(H\) having \(k\) matching edges and therefore \(k\) directed successor-path components. To embed its \(S\)-subgraph in the deterministic successor cycle, choose a starting position for each path; there are \(N^k+O_H(N^{k-1})\) injective edge-preserving maps, because each overlap or coincident placement imposes at least one bounded modular difference between starts. Each chosen \(M\)-edge then has probability \(p_N(k)=N^{-k}(1+O_H(N^{-1}))\). Dividing by the automorphism order gives
\[
\mathbb E C_N(H)=\frac{1}{|\operatorname{Aut}(H)|}+O_H(N^{-1}).
\]
These bounds also apply when a core has parallel differently coloured edges. The argument does not use a heuristic independence assumption.

### 2. Joint Poisson convergence

Fix finitely many nonisomorphic admissible cores and finitely many factorial-moment exponents. Expand the joint factorial moment into ordered selections of pairwise distinct copies. The selections with disjoint vertex sets have asymptotic contribution equal to the product of the corresponding powers of \(1/|\operatorname{Aut}(H)|\), by the same path-placement and matching probability formulas.

For an overlapping selection of distinct simple coloured cycles, each connected component of its edge union containing more than one selected cycle has at least two independent cycles. For any fixed union pattern \(U\), write \(s(U)\) for its number of directed successor-path components and \(b(U)\) for its distinct matching edges. Its expected embedding count is \(O_U(N^{s(U)-b(U)})\). As the successor-edge graph consists of paths, its vertex count equals its successor-edge count plus \(s(U)\). Hence for a connected union of at least two different cycles, \(b(U)-s(U)\ge1\). Such overlap contributions are \(O(N^{-1})\). An incompatible selection has probability zero. All factorial moments therefore converge to those of mutually independent Poisson variables of the asserted means. The method of moments for nonnegative integer vectors gives the claimed joint weak convergence.

The same excess calculation shows that, for any fixed \(L\), with probability tending to one no two different coloured cycles of at most \(L\) edges lie at graph distance at most \(L\). Indeed, two such cycles joined by a path of length at most \(L\) produce a finite graph of excess at least one; there are finitely many types of bounded size. The number of vertices whose fixed-radius neighbourhood contains a cycle is consequently tight, while the remaining \(N-O_{\Pr}(1)\) vertices have the same rooted bounded-radius tree neighbourhood.

### 3. Effective first-order reduction

Replace function terms by their fixed-length edge-path relational translations. The effective bounded-degree Hanf locality theorem gives, for any prescribed sentence, a computable radius \(r\) and counting threshold \(t\) such that truth depends only on counts of isomorphism types of rooted \(r\)-balls, each truncated at \(t\). The Gaifman graph here has maximum degree three.

Outside an event of probability tending to zero, each non-tree rooted \(r\)-ball is attributable to exactly one short coloured cycle core; its finite tree extensions are uniquely forced, to depth \(r\), by the one outgoing and one incoming successor edges and the matching involution. Only finitely many core types of bounded size can contribute such balls. Conversely, all cycle-free rooted ball types that can occur agree with the unique directed coloured regular tree ball and occur more than \(t\) times with probability tending to one. The truncated rooted-ball counts are therefore computable deterministic functions of finitely many truncated core counts, establishing that the sentence has a limit given by a finite Boolean combination of events \(Z_H\ge j\).

For effectivity, enumerate the finite bounded-radius core types and their rational Poisson means. Each logically possible finite truncated core profile has strictly positive limiting probability by joint Poisson convergence, so a finite matching realizing that profile and the requisite abundance of tree balls can be found by exhaustive search. Evaluate the original sentence on these witnesses and combine the resulting finite Poisson probabilities. This is a terminating (not necessarily efficient) algorithm.

For the converse, any finite assertion \(C_N(H)\ge j\) can be written using \(j\) pairwise vertex-disjoint tuples satisfying the finite edge diagram of \(H\). On the probability-one limiting event of separated short cycles, this coincides with the desired count threshold. Negations and Boolean combinations therefore realize every event stated in the theorem.

### 4. Arithmetic and density

For a finite family of core means, choose a common positive denominator \(D\) of the rational numbers \(1/|\operatorname{Aut}(H)|\). Each finite Boolean combination of Poisson thresholds has probability in \(\mathbb Q[e^{-1/D}]\), since each finite Poisson lower tail is a rational polynomial in \(e^{-1/D}\). Hence all first-order limits have the asserted arithmetic form.

For every fixed positive \(\ell\), the cycle consisting of a directed successor path of length \(\ell\) closed by one matching edge has no nonidentity colour-and-orientation-preserving automorphism. It consequently has Poisson mean one. For distinct \(\ell\) these cycle counts have independent Poisson limits. The indicators of the corresponding zero-count events are therefore independent Bernoulli variables, each with probability \(e^{-1}\). The largest atom of the first \(m\) such indicators has mass at most \(\max(e^{-1},1-e^{-1})^m\). By ordering these finite atoms and taking partial unions, every target in \([0,1]\) can be approximated within the largest atom mass by a finite Boolean combination. Thus the first-order limit spectrum is dense.

## Verification

The accompanying standalone `checker.py` enumerates all perfect matchings on cyclic vertex sets of sizes \(8\), \(10\) and \(12\), totaling \(11{,}445\) matchings. It checks \(33\) exact multivariate falling-factorial moment identities for successor lengths one through three, comparing direct exhaustive matching counts against independent compatible-chord enumeration divided by the exact matching probabilities. It also checks \(6\) two-segment coloured-cycle expected-count identities, for a total of \(39\) exact identities. Run `python checker.py` with Python 3. The observed success signal is `CHORD_SUCCESSOR_MATCHING_EXACT_OK 11445 39`.

For example, both distinct four-vertex core types with two directed successor edges and two matching edges have exact mean \(N/(2(N-1))\) whenever \(N\ge8\); their common limit \(1/2\) agrees with their automorphism orders \(2\). The finite checks are corroboration only; neither joint Poisson convergence nor logical convergence is inferred from finite data.

## Relationship to prior work

Paguyo's *Convergence rates of limit theorems in random chord diagrams* (arXiv:2104.01134, Sections 1.1, 3 and 4.1) proves a quantitative Poisson law for adjacent-endpoint chords and reports Acan's earlier Poisson marginal law for any single fixed chord length. This is included as a special case, not claimed new. Acan's *On a uniformly random chord diagram and its intersection graph* (arXiv:1501.01489, Introduction and Sections 2–6) studies crossing-intersection graph statistics and chord-diagram growth, not a full successor-and-matching first-order spectrum.

Dolan and Lynch's *The logic of ordered random structures* (1993, DOI 10.1002/rsa.3240040404) establishes nonconvergence for random matchings on **fully ordered** points, according to its accessible abstract. Full linear order is a strictly richer observation language than cyclic immediate successor; its nonconvergence therefore does not imply nonconvergence here. The complete text was not accessible for inspection, which remains a priority-comparison risk.

McKay, Wormald and Wysocka's *Short cycles in random regular graphs* (2004, DOI 10.37236/1819, Theorem 1) proves uncoloured cycle Poisson laws under the **uniform regular-graph model**. Its probability measure does not fix a directed Hamilton cycle, and it does not calculate the present colour-refined means or first-order spectrum. Koponen's *A characterization of the finite model property for \(\omega\)-categorical theories* (arXiv:2610.16163, first posted October 12, 2026; Introduction and Remark 2.15) motivates studying convergence laws for random expansions of prescribed finite base structures but does not establish this concrete law.

## Limitations

The result is for the uniform fixed-point-free involution on an even-sized set with a **named directed cyclic successor**, not a full order or chord crossing relation. It establishes limits for fixed first-order sentences, not uniform complexity bounds for sentence families of growing quantifier rank. It does not provide explicit rates for arbitrary sentences. The proof uses standard effective bounded-degree Hanf locality as an external logical theorem; its statement is specialized and its hypotheses checked here. Historical priority may be affected by a stronger unlocated theorem for edge-coloured random configuration models or random chord structures; the inspected comparisons do not eliminate that possibility. No independent audit has been performed.

## References

1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163 (first public version 2026-10-12), https://arxiv.org/abs/2610.16163.
2. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134 (2021), https://arxiv.org/abs/2104.01134.
3. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489 (2015), https://arxiv.org/abs/1501.01489.
4. B. D. McKay, N. C. Wormald and B. Wysocka, *Short cycles in random regular graphs*, Electronic Journal of Combinatorics 11 (2004), R66, DOI 10.37236/1819.
5. P. Dolan and J. F. Lynch, *The logic of ordered random structures*, Random Structures & Algorithms 4 (1993), 429–445, DOI 10.1002/rsa.3240040404.
6. L. Libkin, *Elements of Finite Model Theory*, Springer, 2004 (bounded-degree locality context).
