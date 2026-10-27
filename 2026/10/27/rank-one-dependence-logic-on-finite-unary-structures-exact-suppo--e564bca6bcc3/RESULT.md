# Rank-one dependence logic on finite unary structures: exact support-fibre classification

## Finding
Fix a finite relational signature \(\sigma=\{P_1,\ldots,P_q\}\) of unary predicates, with equality and without constants, function symbols, or positive-arity relations other than these unary predicates. Use standard lax-team dependence logic, including constancy atoms \(\mathrm{dep}(x)\), and restrict to **nonempty finite** structures. Let \(\mathcal T=\{0,1\}^q\) be the finite set of complete unary colours. Associate to each structure its multiplicity vector \(\mathbf n=(n_t)_{t\in\mathcal T}\), with \(n_t\) the number of elements of colour \(t\), and its realised-colour support \(S(\mathbf n)=\{t:n_t>0\}\).

**Classification theorem.** A class \(\mathcal K\) of nonempty finite \(\sigma\)-structures is definable by a sentence of dependence-logic quantifier rank at most \(1\) if and only if it is invariant under isomorphism and has the following property: whenever \(\mathbf n\) represents a member of \(\mathcal K\), and \(\mathbf m\) is a nonzero multiplicity vector such that
\[
 S(\mathbf m)=S(\mathbf n),\qquad 1\le m_t\le n_t\quad(t\in S(\mathbf n)),
\]
then \(\mathbf m\) also represents a member of \(\mathcal K\). Thus there is **no bound on the finite thresholds** that quantifier rank \(1\) can detect, but it cannot distinguish a larger positive multiplicity from a smaller one in the direction forbidden by this property.

More constructively, for every support \(S\ne\varnothing\), the excluded multiplicity vectors in the positive orthant \(\mathbb N_{\ge1}^S\) admit a finite set \(B_S\) of minimal forbidden vectors. A rank-one sentence defining the class is obtained from these finitely many bases using the explicit colour-bound and support-guard formulas given below.

**Sharp pure-equality corollary.** When \(q=0\), the exact spectra of quantifier-rank-at-most-one sentences on nonempty finite pure sets are \(\varnothing\), all positive integers, and \(\{1,\ldots,k\}\) for arbitrary \(k\ge1\). Any such sentence defining \(\{1,\ldots,k\}\) must contain at least \(k\) occurrences of constancy atoms, and \(k\) occurrences suffice.

## Assumptions and scope
A dependence atom \(\mathrm{dep}(y_1,\ldots,y_s)\) asserts that any two assignments agreeing on \(y_1,\ldots,y_{s-1}\) also agree on \(y_s\). In particular \(\mathrm{dep}(x)\) asserts constancy of \(x\). The language uses first-order literals, conjunction, lax splitting disjunction, and the usual team interpretations of existential supplementation and universal duplication. Negation is allowed on first-order atoms only. The quantifier rank of a formula is its maximal number of nested quantifiers, not its total number of quantifiers or dependence atoms. All statements concern nonempty finite domains; the classification makes no claim about infinite structures, empty domains, or signatures with binary relations or functions.

For \(t\in\mathcal T\), write \(\chi_t(x)\) for the conjunction of the unary literals prescribing colour \(t\), and \(\overline\chi_t(x)\) for its negation put into first-order negation-normal form. If \(q=0\), take \(\chi_t(x)\) to be \(x=x\) and \(\overline\chi_t(x)\) to be \(x\ne x\). Empty finite conjunctions and disjunctions below denote ordinary truth and falsity, respectively.

## Proof
**1. Preservation within support fibres.** Every dependence-logic formula is downward closed in its evaluation team. Moreover, a quantifier-free formula with just the possible free variable \(x\) is evaluated identically on a one-variable team in a unary substructure and in the ambient structure, provided the pointwise unary colours agree. Consider a closed sentence of rank at most \(1\). Every quantified subformula has the form \(\exists x\,\theta(x)\) or \(\forall x\,\theta(x)\), where \(\theta\) is quantifier-free and there are no other free variables. (Vacuously quantified variables and renamings cause no difference.) All the remaining sentence-level conjunctions and splitting disjunctions are Boolean conjunctions and disjunctions when evaluated on the initial singleton empty assignment: the empty-team property makes a split of this singleton a choice of which side receives that assignment.

For \(\forall x\,\theta(x)\), shrinking the domain to an induced unary substructure shrinks the resulting full \(x\)-team, so downward closure preserves truth. For \(\exists x\,\theta(x)\), if a nonempty supplemented team satisfies \(\theta\), any singleton subteam satisfies it. Consequently the existential sentence holds exactly when some colour realised in the structure admits a satisfying singleton assignment. This depends only on the set of realised colours. Any two structures with the same nonempty support and componentwise comparable multiplicities can be represented, up to isomorphism, by an induced inclusion of their underlying unary structures. Boolean combinations preserve the two kinds of truth preservation. This proves the necessary support-preserving downward closure.

**2. Exact colour-count bounds.** For any colour \(t\) and integer \(k\ge0\), define the rank-one sentence
\[
 U_{t,k}:=\forall x\bigl(\overline\chi_t(x)\vee\underbrace{\mathrm{dep}(x)\vee\cdots\vee\mathrm{dep}(x)}_{k\ \text{copies}}\bigr),
\]
where the constancy-disjunct part is omitted for \(k=0\). Then
\[
 M\models U_{t,k}\quad\Longleftrightarrow\quad n_t(M)\le k.
\]
Indeed, the assignments outside colour \(t\) may go into the first disjunct, while each constancy disjunct receives at most one assignment of colour \(t\). Conversely any at most \(k\) such assignments can be placed one per constancy disjunct. The lax overlap option does not change this bound.

For each nonempty support \(S\subseteq\mathcal T\), the rank-one guard
\[
 G_S:=\bigwedge_{t\in S}\exists x\,\chi_t(x)\ \land\ \bigwedge_{t\notin S}U_{t,0}
\]
holds exactly for structures with realised-colour support \(S\).

**3. Synthesis from finite forbidden bases.** Fix an arbitrary class with the preservation property. On each nonempty support \(S\), let \(D_S\subseteq\mathbb N_{\ge1}^S\) be its downward-closed set of allowed multiplicity vectors. The complement is upward closed. By Dickson's lemma, it is generated by a finite set \(B_S\) of coordinatewise minimal excluded vectors; this statement includes the cases \(D_S=\varnothing\) and \(D_S=\mathbb N_{\ge1}^S\). For any supported vector \(\mathbf n\), membership in \(D_S\) is equivalent to
\[
 \bigwedge_{\mathbf b\in B_S}\ \bigvee_{t\in S}(n_t<b_t).
\]
Each comparison \(n_t<b_t\) is expressed by \(U_{t,b_t-1}\). Therefore the explicit rank-one sentence
\[
 \bigvee_{\varnothing\ne S\subseteq\mathcal T}
 \left[G_S\land
   \bigwedge_{\mathbf b\in B_S}\ \bigvee_{t\in S}U_{t,b_t-1}\right]
\]
defines exactly \(\mathcal K\). A vacuous forbidden-base conjunction is represented by \(\forall x\,(x=x)\). An empty overall class is represented by \(\exists x\,(x\ne x)\). This proves sufficiency. If \(\mathcal K\) is hereditary under every nonempty induced substructure (including the loss of colours), the same method applied to its globally downward-closed multiplicity set can omit the existential support guards entirely.

**4. Exact pure-set spectrum and optimal constancy cost.** For \(q=0\), a quantifier-free formula \(\theta(x)\) over one variable has an exact *capacity* \(h(\theta)\in\mathbb N_{\ge0}\cup\{\infty\}\): a full \(x\)-team of size \(n\) satisfies \(\theta\) exactly when \(n\le h(\theta)\). Its value is \(\infty\) for true first-order literals and dependence atoms having a nonempty determining tuple (which are tautological with only \(x\)); \(0\) for false literals; and \(1\) for \(\mathrm{dep}(x)\). Conjunction takes the minimum and lax splitting disjunction takes the sum of capacities, with \(\infty\) absorbing in the sum. This is proved by structural induction: teams of sizes up to the respective capacities admit a partition, and larger ones cannot. Hence if \(h(\theta)<\infty\), it is no greater than the number of occurrences of \(\mathrm{dep}(x)\) in \(\theta\).

A rank-one universal sentence has the corresponding finite initial-interval spectrum or is universally true. A rank-one existential sentence is either true on all nonempty domains or false on all such domains, because its matrix is checked on a nonempty singleton. Sentence-level conjunctions and disjunctions intersect and unite initial intervals, so every rank-one pure-set sentence has one of the claimed spectra. When the resulting finite cutoff is \(k\ge1\), its value must be realised by some universal matrix of capacity \(k\), forcing at least \(k\) constancy occurrences in the original sentence. Conversely \(\forall x\,\bigvee_{j=1}^k\mathrm{dep}(x)\) attains this exact cutoff with \(k\) occurrences.

## Verification
The accompanying standalone standard-library checker `check_rank1_unary.py` independently evaluates lax split semantics and constancy on finite one-variable teams. It checks \(150\) colour-bound instances, \(24\) support-fibre synthesis instances, \(1{,}830\) formula-capacity instances across \(305\) syntactic formulas, and \(2{,}400\) support-thinning implications. It produces `RANK_ONE_MONADIC_CHECK_OK`. These are finite corroborations only; the general proof is the structural-induction/Dickson argument above. Run with `python3 check_rank1_unary.py` from the directory containing this file.

## Relationship to prior work
Puljujärvi and Väänänen (2026) introduce a dependence-logic Ehrenfeucht–Fraïssé game that characterises logical equivalence with bounded quantifier rank, motivating an exact analysis of the first nontrivial rank. Earlier work of Durand and Kontinen studies other dependence-logic hierarchies, including universals and dependence-atom width. Kontinen and Yang explain the expressive setting of elementary team properties, including the sentence-level relationship between first-order logic and first-order logic with constancy atoms. Fröhlich, Kolaitis and Meier study disjunctions of dependence atoms and their coherence; that paper does not by itself provide the support-fibre classification here. The use of Dickson's lemma for finite forbidden bases and the fact that constancy splitting bounds team size are standard mathematical ingredients, not claimed as discoveries. The assessed contribution is their exact, sharp, rank-restricted unary classification and the optimal pure-equality constancy count. No claim of independent validation or absolute historical priority is made.

## Limitations
The equivalence is only for **finite nonempty unary structures** in **standard lax** dependence logic. It does not classify infinite domains or signatures with binary relations, nonunary functions, constants, or additional generalized atoms. The pure-equality lower bound measures syntactic constancy-atom occurrences, not total formula length under special compressed notations. Relevant general syntactic normal forms, potentially subsuming the classification, may exist in older literature; no exhaustive global priority claim is made. The finite checker does not certify the infinite family of syntactic cases.

## References
1. J. Puljujärvi and J. Väänänen, *A New Ehrenfeucht–Fraïssé Game for Dependence Logic*, arXiv:2606.00812, initial public version 30 May 2026. https://arxiv.org/abs/2606.00812
2. A. Durand and J. Kontinen, *Hierarchies in Dependence Logic*, arXiv:1105.3324, 2011. https://arxiv.org/abs/1105.3324
3. J. Kontinen and F. Yang, *Complete Logics for Elementary Team Properties*, Journal of Symbolic Logic 88 (2023). https://helda.helsinki.fi/server/api/core/bitstreams/fe5360e8-ec3a-4d22-a6fa-95bea82377e3/content
4. N. Fröhlich, P. G. Kolaitis, and A. Meier, *Disjunctions of Two Dependence Atoms*, CSL 2026, DOI:10.4230/LIPIcs.CSL.2026.10. https://doi.org/10.4230/LIPIcs.CSL.2026.10
5. Stanford Encyclopedia of Philosophy, *Dependence Logic* (team semantics and downward closure). https://plato.stanford.edu/entries/logic-dependence/
