# Sharp individual-witness budgets for paired monadic mention-some questions

## Finding
Fix a nonempty finite set of possible worlds \(W\), with \(|W|=n\). In constant-domain inquisitive first-order semantics with a single varying unary predicate \(P\), ask simultaneously for the state-support families of \(\exists\!\exists x\,P(x)\) and \(\exists\!\exists x\,\neg P(x)\). An ordered pair of nonempty downward-closed families \((K,L)\) of subsets of \(W\) occurs if and only if its maximal faces \(F=\operatorname{Max}(K)\) and \(G=\operatorname{Max}(L)\) satisfy
\[
(\forall A\in F)(\exists B\in G)\ A\cup B=W,
\qquad
(\forall B\in G)(\exists A\in F)\ A\cup B=W.
\]
For any realizable pair, the **exact least number of individuals** in a realizing common domain is
\[
r(K,L)=\left|F\cup\{W\setminus B:B\in G\}\right|.
\]
Across all such pairs on \(n\geq1\) worlds, the largest required domain is exactly
\[
R(n)=\binom{n}{\lfloor n/2\rfloor}+\binom{n}{\lfloor n/2\rfloor+1}.
\]
For \(n=4\), there are \(3937\) distinct realizable ordered pairs, with the following complete distribution of their **least** domain sizes:

| Least individuals | Number of ordered support pairs |
|:--:|--:|
| 1 | 16 |
| 2 | 120 |
| 3 | 450 |
| 4 | 901 |
| 5 | 1110 |
| 6 | 849 |
| 7 | 366 |
| 8 | 103 |
| 9 | 20 |
| 10 | 2 |

The total \(3937\) follows from a previously known count of nonempty convex subsets; the new exact statistic asserted here is the domain-demand distribution and its operational interpretation, together with the paired-support construction. The bound uses the classical two-Sperner inequality and is not claimed as a new extremal combinatorics theorem.

## Assumptions and scope
A model has exactly the labeled worlds \(W\), a **nonempty** constant domain \(D\), rigid identity, and independent interpretations \(P_w\subseteq D\) at each world \(w\). Information states are **all** subsets \(s\subseteq W\), including the empty state. A formula \(\exists\!\exists x\,\alpha(x)\) is supported in \(s\) when there exists a single \(d\in D\) such that \(\alpha(d)\) is true at every \(w\in s\). Classical \(\neg P(x)\) is truth conditional. Support families, and thus ordered pairs, are compared on this same labeled world set, without quotienting by world permutations. The theorem covers no other connectives or nested quantifiers.

For each \(d\in D\) define the *positive footprint* \(T_d=\{w\in W:d\in P_w\}\). The common domain cannot be chosen independently for the two questions: its \(d\)-th negative footprint is exactly \(W\setminus T_d\). Thus
\[
K=\{s\subseteq W:(\exists d\in D)\ s\subseteq T_d\},\qquad
L=\{s\subseteq W:(\exists d\in D)\ s\subseteq W\setminus T_d\}.
\]
Here \(F\), \(G\), and the complement family \(H=\{W\setminus B:B\in G\}\) are nonempty antichains of \(\mathcal P(W)\). A nonempty downward-closed family necessarily contains the empty state.

## Proof
**Necessity of the covering condition.** Each maximal \(A\in F\) is included in some \(T_d\), and \(T_d\in K\); maximality forces \(T_d=A\). Since \(W\setminus T_d\in L\), there exists \(B\in G\) containing \(W\setminus A\). Hence \(A\cup B=W\). The same argument applied to \(B\in G\) yields an \(A\in F\) with \(A\cup B=W\).

**Sufficiency and exact cost.** Set \(H=\{W\setminus B:B\in G\}\). The condition says every \(A\in F\) contains some \(h\in H\), and every \(h\in H\) is contained in some \(A\in F\). Give one distinct individual each footprint in \(T=F\cup H\), interpreting \(P\) at \(w\) by membership of \(w\) in the corresponding footprint. Taking downward closures then gives precisely \(K\) and \(L\): the \(H\)-footprints are already below the \(F\)-footprints, and the complements of the \(F\)-footprints are already below complements of \(H\). Conversely, the maximal-face argument forces **every distinct** footprint in \(F\cup H\) to be realized in any model, so the least domain size equals \(|F\cup H|\).

**Convex dual description.** The family
\[
C=\{S\subseteq W:(\exists h\in H)(\exists A\in F)\ h\subseteq S\subseteq A\}
\]
is the nonempty order-convex set generated between \(H\) and \(F\). Its minima are exactly \(H\), its maxima exactly \(F\), and the original support pair is uniquely recovered by downward closing \(C\) and downward closing the complements of \(C\). Conversely any nonempty order-convex \(C\subseteq\mathcal P(W)\) yields such a pair. Its least realizing domain has \(|\operatorname{Min}(C)\cup\operatorname{Max}(C)|\) elements. When minima and maxima coincide, duplicated footprints are counted only once.

**Sharp universal bound.** The boundary \(F\cup H\) is the union of two antichains, so no chain of three distinct subsets of \(W\) lies in it. The standard two-Sperner inequality, derived by averaging over all maximal Boolean-lattice chains, says
\[
\sum_{S\in F\cup H}\binom{n}{|S|}^{-1}\le2.
\]
The fractional mass on each fixed rank is at most one. Optimizing the cardinality under these constraints fills the two largest binomial ranks, yielding the stated upper bound. For equality let \(H\) consist of all \(\lfloor n/2\rfloor\)-element subsets and let \(F\) consist of all \((\lfloor n/2\rfloor+1)\)-element subsets. Every lower footprint extends to an upper one, and every upper one contains a lower one. The construction above realizes the pair with exactly \(R(n)\) individuals, proving sharpness even for \(n=1\).

**Four-world exact distribution.** For \(|W|=4\), there are \(16\) possible footprints. Enumerate each nonempty subset \(T\) of the \(16\) footprints (exactly \(65535\) candidates), form the ordered pair of generated support families, and retain the smallest \(|T|\) for each distinct pair. The first standalone checker exhaustively performs this construction and compares each minimum with the closed formula \(|F\cup H|\). Independently, the second checker enumerates every subset of the \(16\)-element Boolean lattice, tests interval convexity via all triples \(A\subseteq S\subseteq B\), and counts \(|\operatorname{Min}(C)\cup\operatorname{Max}(C)|\) for each nonempty convex subset. Both give the displayed distribution; the two algorithms enumerate fundamentally different sample spaces (footprint collections versus convex sets). The finite computation is exhaustive at \(n=4\), while the all-\(n\) claims above rest on proof, not extrapolation.

## Verification
Execute the bundled standalone scripts with standard Python: `python paired_support_checker.py` and `python convex_boundary_checker.py`. Each script contains its own explicit assertions for the distribution for \(n=1,2,3,4\) and for the expected total \(3937\) at \(n=4\). The scripts use integer-bit encodings of world subsets and no external packages. Their independently obtained distribution vectors agree exactly. The formal proof of the universal claims is in the preceding section; exhaustive finite enumeration verifies only the stated finite cases.

## Relationship to prior work
Ciardelli and Kontinen, *Inquisitive first-order logic is neither compact nor recursively axiomatizable* (arXiv:2603.20845, first posted March 21, 2026), give the mention-some support semantics in Example 2.7. They do not give a joint two-question witness-resource classification. Anttila and Knudstorp, *Convex Team Logics* (arXiv:2503.21850, first posted March 27, 2025), establish expressive completeness for convex team meanings but do not assign a common-domain witness budget to opposed unary existential questions. Elder, Lafreniere, McNicholas, Striker and Welch (2024) describe interval-closed sets through boundary antichains; that general combinatorial structure is prior art, as is the two-Sperner inequality. OEIS A369313 supplies \(3938\) as the total number of convex subsets of the four-dimensional Boolean lattice, so the \(3937\) nonempty count is known in equivalent form. The claimed refinement is the ten-cell witness-cost distribution and its paired question semantics, rather than a new enumeration of convex sets without weights.

## Limitations
The world set is finite, the domain is constant and nonempty, and only the two indicated question forms are covered. Results do not settle compactness, axiomatizability, or expressivity for the full monadic inquisitive first-order fragment. The source literature's convex-set results and the classical two-Sperner theorem already imply much of the *combinatorial* structure once the footprint correspondence is supplied. Exhaustive proof of the exact distribution is for four worlds only; no closed formula for the cost distribution at general \(n\) is claimed. Equivalence to an earlier unindexed boundary-statistic census remains a historical-priority risk.

## References
1. Ivano Ciardelli and Juha Kontinen, *Inquisitive first-order logic is neither compact nor recursively axiomatizable*, arXiv:2603.20845, first posted 2026-03-21. https://arxiv.org/abs/2603.20845
2. Aleksi Anttila and Søren Brinck Knudstorp, *Convex Team Logics*, arXiv:2503.21850, first posted 2025-03-27. https://arxiv.org/abs/2503.21850
3. Jennifer Elder, Nadia Lafreniere, Erin McNicholas, Jessica Striker and Amanda Welch, *Toggling, rowmotion, and homomesy on interval-closed sets*, Journal of Combinatorics 15 (2024), 479–528, arXiv:2307.08520. https://arxiv.org/abs/2307.08520
4. OEIS A369313, *Number of interval-closed sets in the Boolean lattice of dimension n*, including the value for four-dimensional Boolean lattices. https://oeis.org/A369313
5. K. Engel, *Sperner Theory*, Cambridge University Press, 1997, for the classical higher-Sperner inequality.
