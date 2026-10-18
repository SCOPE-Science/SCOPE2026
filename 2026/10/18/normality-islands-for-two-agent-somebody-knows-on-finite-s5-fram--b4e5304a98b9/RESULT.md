# Normality islands for two-agent somebody-knows on finite S5 frames

## Finding

On an arbitrary finite nonempty set of worlds \(W\), let \(E\) and \(F\) be two equivalence relations. Write \(E[w]\) and \(F[w]\) for the equivalence classes of \(w\), and define the *somebody-knows* operation on propositions \(A\subseteq W\) by
\[
B(A)=\{w\in W:E[w]\subseteq A\text{ or }F[w]\subseteq A\}.
\]
The following conditions are equivalent:

1. The bundled operator preserves binary intersections for all propositions: \(B(A\cap D)=B(A)\cap B(D)\) for every \(A,D\subseteq W\). Equivalently, it validates the normal modal distribution axiom \(B(p\to q)\to(Bp\to Bq)\) under all propositional valuations.
2. At every world, the information cells are comparable: \(E[w]\subseteq F[w]\) or \(F[w]\subseteq E[w]\).
3. The bipartite incidence graph with vertices the \(E\)-classes and \(F\)-classes, and an edge for each nonempty intersection, is a disjoint union of stars (a single edge is allowed).
4. The bundled operator coincides on every proposition with distributed knowledge: \(B(A)=K_{E\cap F}(A)\), where \(K_R(A)=\{w:R[w]\subseteq A\}\).

Let \(c_n\) count **ordered pairs** of equivalence relations \((E,F)\) on a fixed labelled \(n\)-world set satisfying these conditions, with \(c_0=1\) as an enumerative convention. If \(\mathsf{Bell}(j)\) denotes the number of set partitions of a \(j\)-element set, then
\[
\boxed{\displaystyle \sum_{n\geq0}c_n\frac{z^n}{n!}
=\exp\!\left(2\bigl(\exp(\exp(z)-1)-1\bigr)-(\exp(z)-1)\right).}
\]
Equivalently, for every \(n\geq1\),
\[
\boxed{\displaystyle c_n=\sum_{j=1}^n\binom{n-1}{j-1}\bigl(2\mathsf{Bell}(j)-1\bigr)c_{n-j}.}
\]
The values for \(n=1,\ldots,7\) are \(1,4,19,111,774,6229,56529\).

## Assumptions and scope

The set \(W\) is finite and nonempty for the counting statement; its elements are labelled, so relabellings are not identified. Both agents have standard S5 accessibility, meaning that \(E\) and \(F\) are equivalence relations. All subsets of \(W\) are admissible propositional valuations. The operator \(B\) is the disjunction of the two ordinary knowledge operators, not common knowledge or the union of accessibility relations. The incidence graph is a *simple* bipartite graph on the two distinguished families of blocks, and has an edge precisely for a nonempty block intersection. The enumeration counts underlying ordered frame pairs, not distinct unary operators.

## Proof

**Failure under crossing cells.** Suppose some \(w\) has incomparable classes \(U=E[w]\) and \(V=F[w]\). Put \(A=U\) and \(D=V\). Then \(w\in B(A)\cap B(D)\). But neither \(U\) nor \(V\) lies in \(U\cap V\), so \(w\notin B(A\cap D)\). Hence intersection preservation implies condition 2.

**Sufficiency and identification with distributed knowledge.** If the two classes at \(w\) are comparable, their smaller member is exactly \((E\cap F)[w]=E[w]\cap F[w]\). Thus, for any \(A\subseteq W\), \(E[w]\subseteq A\) or \(F[w]\subseteq A\) holds exactly when \((E\cap F)[w]\subseteq A\). This proves condition 4 from condition 2. Every relational box preserves finite intersections, so condition 4 implies condition 1. The operation always sends \(W\) to \(W\) and is monotone; for such Boolean operators, preservation of binary intersections is equivalent to the modal distribution axiom. Indeed, distribution follows by applying meet preservation to \(A\) and \((W\setminus A)\cup D\). Conversely, from distribution and monotonicity, \(B(A)\cap B(D)\subseteq B(A)\cap B((W\setminus A)\cup D)\subseteq B(A\cap D)\); monotonicity supplies the reverse inclusion.

**Incidence-graph criterion.** Take an incidence edge joining an \(E\)-block \(U\) and an \(F\)-block \(V\), so their intersection contains a world \(w\). The inclusion \(U\subseteq V\) holds exactly when \(U\) has degree one in the bipartite incidence graph: the \(F\)-blocks partition \(W\), and \(U\) meets only \(V\) precisely when it lies wholly in \(V\). Similarly, \(V\subseteq U\) is equivalent to \(V\) having degree one. Hence condition 2 says every graph edge has a degree-one endpoint. A connected graph with this property cannot have two vertices of degree at least two, since a shortest path between such vertices would have an edge with neither endpoint a leaf. Thus each connected component is a star (including the one-edge case), establishing condition 3 and its converse.

**Counting components.** The components of the incidence graph correspond exactly to the blocks of \(E\vee F\), the least equivalence relation containing both relations. On one such component \(U\), the star condition says that one of the two restrictions \(E|_U\) and \(F|_U\) consists of one block; conversely that condition forces the incidence graph on \(U\) to be a star. For \(|U|=j\), there are \(\mathsf{Bell}(j)\) choices with \(E|_U\) indiscrete and another \(\mathsf{Bell}(j)\) with \(F|_U\) indiscrete. The unique pair with both indiscrete has been counted twice. Thus the exact number of possible connected components of size \(j\) is \(a_j=2\mathsf{Bell}(j)-1\). Choosing an unordered set partition of \(W\) into components, independently specifying the two restrictions on every component, and forbidding cross-component equivalences gives a unique admissible ordered pair. The labelled exponential formula therefore yields
\[
\sum_{n\geq0}c_n\frac{z^n}{n!}
=\exp\left(\sum_{j\geq1}a_j\frac{z^j}{j!}\right).
\]
Using \(\sum_{j\geq0}\mathsf{Bell}(j)z^j/j!=\exp(\exp(z)-1)\) gives the displayed expression. Distinguished-component decomposition using the block containing a fixed label gives the displayed recurrence.

**Strictly local rather than global domination.** For example, on \(W=\{1,2,3,4\}\), choose \(E\)-blocks \(\{1,2\},\{3\},\{4\}\) and \(F\)-blocks \(\{1\},\{2\},\{3,4\}\). Neither equivalence relation globally refines the other, yet the local comparability criterion holds. Indeed, \(B\) is the identity on propositions in this example.

## Verification

The accompanying standalone `verify.py` enumerates all set partitions and ordered pairs on worlds of size one through six. It checks the local-comparability criterion against the independent incidence-degree condition; it checks the distributed-knowledge operator equality on every proposition for each normal pair; and it matches the resulting counts against the recurrence. For sizes one through four it additionally checks the full binary-intersection law over every ordered pair of propositions, including non-normal cases. Run `python3 verify.py` from the package directory; expected completion marker: `BUNDLE_NORMALITY_CENSUS_OK`. The exhaustive computation reaches \(41{,}209\) ordered pairs at six worlds. The all-size theorem follows from the proof above rather than the finite verification.

## Relationship to prior work

The somebody-knows modality \(\bigvee_i K_i\) and its general lack of full conjunction closure are established by Ågotnes and Wáng (2021). Ding and Yang (2026) provide a uniform general theory of bundled modalities and complete axiomatizations for someone-knows over S5. These works address unrestricted frame classes; the result here concerns the **precise exceptional finite S5 frames** where two-agent somebody-knows becomes a normal box, including an exact labelled-frame census. Lindqvist, Velázquez-Quesada, and Ågotnes (2025) investigate different group-belief operators and supply related context on relational versus nonrelational group modalities. None of these inspected results supplies the star-incidence or component Bell-number classification. The count is presented as an exact enumeration derived here, not as a claim of priority for a numerical sequence in isolation.

## Limitations

This result concerns two S5 agents and labelled finite frame pairs; it does not classify arbitrary many-agent bundles, KD45 relations, or distinct resulting bundled operators. The structural equivalences require universal quantification over **all** propositional valuations; they need not follow from agreement on a restricted set of valuation atoms. Existing general results on unions of neighbourhood filters or on set partitions under different terminology may subsume parts of the theorem; absolute historical priority is not established. The executable checks cover only finite sizes up to six, with direct meet-law tests up to four; they do not constitute an infinite proof.

## References

- Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268, first version dated 2026-03-27; especially Section 5.1. https://arxiv.org/abs/2603.26268
- Thomas Ågotnes and Yì N. Wáng, *Somebody Knows*, Proceedings of KR 2021, pp. 2–11, DOI:10.24963/kr.2021/1. https://proceedings.kr.org/2021/1/
- John I. Lindqvist, Fernando R. Velázquez-Quesada, and Thomas Ågotnes, *Variations on distributed belief*, Journal of Logic, Language and Information, DOI:10.1007/s10849-025-09446-8. https://link.springer.com/article/10.1007/s10849-025-09446-8
