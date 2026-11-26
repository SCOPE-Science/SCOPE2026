# The complete designated-entailment order of twenty-four Belnapian essence and accident operators

## Finding

In Petrukhin’s four-valued semantics on nonempty universal-accessibility frames, write \(O\preceq O'\) if \(O(A)\models_D O'(A)\) uniformly for **all** formulas \(A\), using the same argument on both sides. Here \(\models_D\) preserves designated truth at every pointed model. Equivalently, this order can be tested by giving both operators the same propositional letter \(p\). It is not the order for each individually chosen argument formula.

The twenty-four operators are pairwise distinct for this comparison. For the six queries
\[
\mathcal Q=\{\{t\},\{b\},\{n\},\{f\},\{t,b\},\{b,f\}\},
\]
the complete list of strict comparisons is
\[
\begin{aligned}
\bullet_Q\preceq\circ_R &\iff Q\cap R=\varnothing,\\
\bullet_Q\preceq\widetilde\circ_R &\iff Q\subseteq R,\\
\widetilde\bullet_Q\preceq\circ_R &\iff R\subseteq Q.
\end{aligned}
\]
There are respectively \(20,10,10\) comparisons of these forms, all covers. Including the twenty-four identities, sixty-four of the \(576\) directed tests hold. Of the \(512\) failures, \(144\) first have a one-world countermodel, \(340\) first have a two-world countermodel, and \(28\) first have a three-world countermodel. All of these minima can be attained with the atomic argument \(p\).

## Assumptions and semantics

The truth values are \(V=\{t,b,n,f\}\), with designated values \(t,b\). The letters stand for positive evidence only, both kinds of evidence, neither kind, and negative evidence only, respectively. Accessibility is universal. At a pointed world \(w\), put \(a=v(A,w)\) and \(S=\{v(A,u):u\in W\}\). In the notation of the finding, the designated-truth clauses from Petrukhin’s Definition 6 are
\[
\begin{array}{ll}
\bullet_Q: a\in Q\ \wedge\ S\setminus Q\ne\varnothing,&
\circ_Q: \neg(a\in Q\ \wedge\ S\setminus Q\ne\varnothing),\\
\widetilde\bullet_Q: a\notin Q\ \wedge\ S\cap Q\ne\varnothing,&
\widetilde\circ_Q: \neg(a\notin Q\ \wedge\ S\cap Q\ne\varnothing).
\end{array}
\]
The negations in this display are of Boolean predicates of designated truth, not claims about interdefinability by object-language negation.

## Proof

**Profile reduction.** Every model and argument gives a profile \((a,S)\) with \(a\in S\subseteq V\); the truth clauses depend on nothing else. Conversely each of the \(4\cdot 2^3=32\) profiles is realized by the atom \(p\) on exactly \(|S|\) worlds, one for each status in \(S\), with designated point carrying status \(a\) (whether or not \(a\) itself is a designated value). Every realization needs at least \(|S|\) worlds. Thus the profiles decide uniform entailment and the least countermodel orders, including for comparisons quantified over arguments of arbitrary nesting depth.

**A single family of cuts.** Let \(\mathcal K=\mathcal Q\cup\{V\setminus Q:Q\in\mathcal Q\}\), a family of twelve different proper nonempty sets. For \(K\in\mathcal K\) let \(L_K(a,S)\) be \(a\in K\) and \(S\setminus K\ne\varnothing\). The twelve accidents give exactly the \(L_K\), and the twelve essences give their Boolean complements. Indeed, the negative accidents correspond to the cuts \(V\setminus Q\), and each essence is the complement of its corresponding accident at the designated coordinate.

If \(K\not\subseteq L\), choose \(a\in K\setminus L\) and one additional status outside \(K\) to refute \(L_K\Rightarrow L_L\). If \(K\subsetneq L\), choose \(a\in K\) and one additional status from \(L\setminus K\). This also refutes the implication, because the resulting \(S\) lies wholly in \(L\). Therefore accidents entail one another only by identity. By contraposition the same holds among essences. An essence never entails an accident, since in every single-world model all essences are designated and no accident is designated. These facts also separate the twenty-four signatures.

The remaining implications are \(L_K\Rightarrow\neg L_L\). They hold exactly when \(K\cap L=\varnothing\). If the intersection is nonempty, use a local value there and include a witness outside each of \(K,L\); this makes both accidents designated. For two positive cuts, disjointness is precisely the first criterion in the finding. With one complement cut, it is the corresponding inclusion in the second or third criterion. With two complement cuts, disjointness would require \(Q\cup R=V\); this is impossible, since the only size-two queries intersect and no query has more than two elements. Disjointness among the original queries occurs for \(4\cdot3=12\) ordered singleton pairs and eight singleton/doubleton pairs in the two orientations. There are ten ordered inclusions among the queries: six equalities and four singleton-in-doubleton inclusions. The resulting forty strict comparisons go only from accidents to essences, so they are covers.

**Least countermodel sizes.** The twelve essence antecedents and twelve accident consequents account for the \(144\) one-world failures. Failures between distinct accidents require and, by the two-status construction, admit two worlds. The same holds between distinct essences by contraposition. For an invalid \(L_K\Rightarrow\neg L_L\) the local value belongs to \(K\cap L\). The two outside witnesses can share one world precisely when \(V\setminus(K\cup L)\ne\varnothing\). Thus three worlds are required exactly for the ordered cut pairs with \(K\cap L\ne\varnothing\) and \(K\cup L=V\). Taking complements exchanges these with disjoint ordered cut pairs whose union is proper. There are forty disjoint ordered cut pairs by the cover count, and twelve of those are complementary ordered pairs, one for each first cut. Hence \(40-12=28\) failures first occur at size three, leaving \(512-144-28=340\) at size two. For example, \(\widetilde\bullet_{\{t\}}p\not\models_D\widetilde\circ_{\{b\}}p\) is witnessed at the \(n\)-world of a model whose other worlds give \(p\) status \(t\) and \(b\). Those witnesses must be separate and both different from the local status.

## Reproduction and limits

The set arguments above give the full certificate without computer enumeration. As a finite replay, the accompanying `verify.py` can be run with `python3 verify.py` from the scientific package directory containing that script. It checks the source truth clauses against the profile predicates on labeled valuations, then tests the implication criteria and histogram. Its success signal is `BELNAP_24_IMPLICATIONS_OK 24 40 512 144 340 28`. The proof of the profile reduction is what makes these finite tests exhaustive for the uniform comparison.

The order generally changes if the argument is fixed before taking entailment. For instance, in Petrukhin’s propositional semantics \(p\to p\) takes only \(t\) or \(b\): its positive coordinate is always present and its negative coordinate is present only if \(p=b\). Consequently \(\circ_{\{n\}}(p\to p)\) and \(\circ_{\{f\}}(p\to p)\) are both designated everywhere. The result classifies only the uniform same-argument order and only designated truth on universal frames. It asserts neither four-valued equivalence nor derivability, and does not compare different arguments.

## Relationship to prior work

Petrukhin introduces the operators and gives semantic identities, interdefinability and modal translation results. Identities that add an outer negation or change the input argument are not the bare common-argument comparisons classified here. The present classification uses the published truth clauses; it does not claim a new semantics or a general normal form. Fan studies classical, two-valued essence and accident rather than the designated order for the status-indexed four-valued family.

## References

1. Y. Petrukhin, *Essence and Accident Modalities Meet Belnapian Truth Values*, *Studia Logica* (2026), DOI [10.1007/s11225-026-10250-z](https://doi.org/10.1007/s11225-026-10250-z), Definition 6.
2. J. Fan, *Logics of Essence and Accident* (2015), [arXiv:1506.01872](https://arxiv.org/abs/1506.01872).
