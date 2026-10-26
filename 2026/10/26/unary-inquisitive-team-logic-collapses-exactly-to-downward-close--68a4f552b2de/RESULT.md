# Unary inquisitive team logic collapses exactly to downward-closed first-order properties
## Finding

Let \(D\) be any nonempty set, finite or infinite, and let \(X\) be a team on exactly one free variable \(x\), identified with its unary relation \(R_X\subseteq D\). Consider inquisitive team logic \(\mathsf{InqBT}\) in the **pure equality signature**, with standard team support, inquisitive disjunction, intuitionistic implication and the two **uniform-value** quantifiers \(\forall^{1}\) and \(\exists^{1}\), but **without** a range-generating quantifier.

**Classification theorem.** A class \(\mathcal K\) of pairs \((D,R_X)\), with \(D\ne\varnothing\), is defined by an \(\mathsf{InqBT}\) formula with free variables contained in \(\{x\}\) if and only if:

1. \(\mathcal K\) is defined by a first-order sentence in the signature \(\{=,R\}\), with \(R\) unary;
2. it is downward closed in the team: \((D,X)\in\mathcal K\) and \(Y\subseteq X\) imply \((D,Y)\in\mathcal K\); and
3. for every nonempty \(D\), \((D,\varnothing)\in\mathcal K\).

The first condition is the substantive **unary collapse**: no one-free-variable \(\mathsf{InqBT}\) formula can express a non-first-order property of the team in pure equality. An earlier expressiveness theorem for a different logic already implies the converse direction; it is included here to give an exact classification and explicit normal form.

**Eventual cardinality normal form.** For each such property there exists a finite integer \(N\ge1\), a finite cutoff \(k_n\in\{0,\dots,n\}\) for every \(1\le n<N\), and precisely one of the following alternatives on **nonempty teams** over every domain of size at least \(N\), including infinite domains:

- \(|X|\le k\), for some fixed integer \(k\ge0\); or
- \(|D\setminus X|\ge d\), for some fixed integer \(d\ge0\).

The first alternative includes the property that only the empty team is accepted; the second includes universal acceptance. The finite-domain exceptions are exactly \(|X|\le k_n\). All these cases have effective \(\mathsf{InqBT}\) defining formulas. At two free variables the analogous first-order collapse fails, by the already published binary counterexample of Kontinen and Ciardelli (Theorem 3.6). Thus free-variable arity one is the exact pure-equality boundary for universal first-order translatability.

## Assumptions and scope

The structure has no nonlogical symbols other than equality. The universe is nonempty, and teams may be empty or infinite. Team support uses the clauses in Kontinen and Ciardelli, Definition 2.1: \(\bot\) holds exactly on the empty team; inquisitive \(\sqcup\) is whole-team Boolean choice; \(\phi\to\psi\) checks **all** subteams; \(\forall^{1}y\) and \(\exists^{1}y\) respectively check every or some **constant** \(y\)-value across the team. Here \(\sqcup\) is merely notation for the primitive inquisitive disjunction. Classical \(\lor\), \(\neg\), and \(\exists\) inside ordinary first-order formulas are the standard derived, flat fragment, not inquisitive operators. Bound variables are alpha-renamed to avoid capturing \(x\).

The normal form describes the restriction to nonempty teams because all \(\mathsf{InqBT}\) formulas accept the empty team, even when their classical first-order guards are false. It makes no claim for multiple free variables, added unary or binary predicates, functions, or the stronger logic with range-generating quantification.

## Proof

**1. Translation into monadic second-order logic.** Fix any formula \(\phi\) with free variables contained in \(\{x\}\). After alpha-renaming bound variables, every team reached from the initial unary team by uniform-value quantifiers and subteam restriction has the form
\[
T(S;\vec a)=\{s_u:u\in S,\ s_u(x)=u,\ s_u(y_j)=a_j\},\qquad S\subseteq D.
\]
Here the current additional variable values \(\vec a\) are fixed across all assignments, even when \(S=\varnothing\). Define recursively a monadic second-order formula \(\tau_\phi(S;\vec a)\), using one unary set variable \(S\) for the current team and individual variables for the constant parameters. Atomic equality translates to \(\forall u(S(u)\to \mathrm{Eq}(u,\vec a))\), and \(\bot\) translates to \(\neg\exists uS(u)\). Conjunction and inquisitive disjunction translate to Boolean conjunction and disjunction. Implication translates to
\[
\forall U\bigl[(\forall u(U(u)\to S(u)))\to(\tau_\alpha(U;\vec a)\to\tau_\beta(U;\vec a))\bigr].
\]
Finally uniform \(\forall^{1}y\) and \(\exists^{1}y\) translate to ordinary first-order \(\forall a_y\) and \(\exists a_y\), respectively, with the chosen individual adjoined to \(\vec a\). Induction on formulas proves the equivalence of each translation with direct team support. All second-order quantified variables are **unary sets** because no semantic operation creates another varying assignment coordinate. In particular \(\tau_\phi(R)\) is a monadic second-order sentence over one unary predicate \(R\) and equality.

**2. Monadic set quantification collapses to first order.** We give a uniform finite-rank argument, valid also for infinite sets. Let \(q\) be the monadic-second-order quantifier rank of \(\tau_\phi\), enlarged to at least one. In the usual MSO Ehrenfeucht–Fraïssé game, two structures with a fixed finite family of unary colour predicates are equivalent for \(q\) rounds provided corresponding colour classes have either the same cardinality below \(2^q\), or both cardinalities at least \(2^q\). A point move removes a point from its colour cell and preserves the invariant at rank \(q-1\); a set move splits each cell into its chosen-set and complementary pieces. For a cell of size at least \(2^q\), the duplicator realizes every split whose small pieces are below \(2^{q-1}\) exactly, while leaving all large pieces at least \(2^{q-1}\). For small cells, it copies the split exactly. The invariant closes by induction on remaining rounds. This argument does not distinguish finite-large from infinite-large cells.

With the initial colours \(R\) and \(D\setminus R\), satisfaction is consequently determined by the two truncated cardinalities \(\min(|R|,2^q)\) and \(\min(|D\setminus R|,2^q)\), with infinity treated as above threshold. The finitely many possible truncated profiles are first-order definable by equality, \(R\), and bounded distinct-witness quantifiers. Their finite disjunction gives an effective first-order translation of \(\phi\). This proves the nontrivial forward implication in the classification.

**3. Downward and empty-team restrictions.** The empty-team and persistency properties follow by structural induction on the support clauses, including implication. Thus every definable property has conditions 2 and 3.

**4. Classification of all downward first-order properties.** Let \(\theta(R)\) be any first-order sentence of rank \(q\ge1\) with conditions 2 and 3. The ordinary first-order equality game with one unary predicate shows that its truth depends only on \(\min(|R|,q)\) and \(\min(|D\setminus R|,q)\). For fixed finite \(|D|=n\), isomorphism invariance and downward closure show that accepted nonempty teams have exactly the form \(1\le|R|\le k_n\) for a cutoff \(0\le k_n\le n\).

For all finite \(n\ge2q\) and all infinite \(D\), the central profile \(|R|\ge q\), \(|D\setminus R|\ge q\) has constant truth value. If it is **false**, downward closure makes all profiles with \(|R|\ge q\) false: reduce such a team to exactly \(q\) points, leaving at least \(q\) outside in any large domain, or use the rank-invariant central profile. The accepted small-\(R\) profiles form one fixed initial segment, hence \(|R|\le k\) with \(k<q\). If the central profile is **true**, downward closure accepts all \(|R|<q\) and all teams with \(|D\setminus R|\ge q\). Among the remaining profiles, indexed by complement size \(b<q\), decreasing \(R\) enlarges \(b\); hence the accepted values form a final segment \(b\ge d\), with \(0\le d\le q\). If none of the \(b<q\) profiles is allowed, set \(d=q\). Thus the large-domain rule is \(|D\setminus R|\ge d\). These arguments apply without change to infinite \(D\), since the same truncated profiles are present. Take \(N=\max(2q,2)\), absorbing finitely many smaller domains in their individual cutoffs.

**5. Explicit formulas.** For \(k\ge1\), the following \(\mathsf{InqBT}\) formula expresses \(|X|\le k\) on nonempty teams:
\[
B_k(x):=\exists^{1}y_1\cdots\exists^{1}y_k\,\bigl((x=y_1)\lor\cdots\lor(x=y_k)\bigr).
\]
Here \(\lor\) is derived **classical flat disjunction**, so every value of \(x\) must be one of the \(k\) globally chosen constants. Put \(B_0:=\bot\). For \(d\ge1\), the following formula expresses \(|D\setminus X|\ge d\) on nonempty teams:
\[
E_d(x):=\exists^{1}z_1\cdots\exists^{1}z_d\,\Bigl[\bigwedge_{i<j}z_i\ne z_j\ \land\ \bigwedge_{i=1}^d x\ne z_i\Bigr].
\]
Put \(E_0:=\top\). A classical equality sentence \(F_n\) expresses \(|D|=n\), and a classical sentence \(G_N\) expresses \(|D|\ge N\). Let \(H\) be the applicable large-domain formula \(B_k\) or \(E_d\). Then
\[
\Bigl(\bigsqcup_{1\le n<N}(F_n\land B_{k_n})\Bigr)\ \sqcup\ (G_N\land H)
\]
expresses exactly the desired property on all **nonempty** teams. The outer disjunction is *inquisitive*, i.e. one disjunct must hold for the entire team. Every disjunct accepts the empty team, so the total formula also agrees there. When \(N=1\), omit the finite-case disjunction. This completes both directions.

## Verification

The standalone standard-library Python file \(\texttt{proof_checker.py}\) implements two independent finite evaluators for the same semantics: a direct assignment-team evaluator and a compressed evaluator using a unary subset and globally fixed quantifier values. It tests nested implications, uniform quantifiers, inquisitive and classical disjunction, and permutations of the underlying equality structure. It also checks the \(B_k\) and \(E_d\) constructions on every unary team in domains of size at most five. Executing \(\texttt{python3\ proof_checker.py}\) produces \(\texttt{INQUISITIVE_UNARY_CHECK_OK\ 4080}\) after the detailed checks. These finite computations confirm selected semantic identities, not the all-domain MSO collapse, which is proved above.

## Relationship to prior work

Kontinen and Ciardelli, *On the Expressive Power of Inquisitive Team Logic and Inquisitive First-Order Logic* (arXiv:2603.08646; first submitted 2026-03-09), prove a genuinely non-first-order two-free-variable formula in pure equality (Theorem 3.6). Their direct semantic definitions and example motivate isolating the exact one-variable boundary. That paper does **not** state the monadic unary collapse or the eventual team/complement cutoffs.

Kontinen and Yang, *Complete Logics for Elementary Team Properties* (arXiv:1904.08695, Theorems 3.1--3.7), establish that their **different logic** \(\mathsf{FOT}^{\downarrow}\) captures all downward-closed first-order team properties in arbitrary arity; its logical primitives are a fragment expressible in \(\mathsf{InqBT}\). Consequently the **converse expressive-completeness direction here is already covered in substance** by their stronger general theorem, and is not a stand-alone novelty claim. The contribution is the previously unestablished **upper bound on expressive power for one-free-variable \(\mathsf{InqBT}\)**, yielding the exact boundary with the published binary counterexample, plus a concrete cardinality normal form. The translation uses the classical monadic-second-order finite-rank collapse; neither this general collapse nor the published two-variable separation is claimed to be new.

Ciardelli and Conti, *Connecting state-based and team-based inquisitive logic* (DOI 10.1093/logcom/exag032), develop translations between two semantics, not this one-variable monadic-compression classification. Grilletti and Ciardelli, *Games and Cardinalities in Inquisitive First-Order Logic* (DOI 10.1017/S1755020321000198), classify cardinality quantifiers in the **state-based** variant and do not imply a uniform upper bound for the team-based open-formula fragment.

## Limitations

The classification is for one free team coordinate in a pure-equality signature and standard uniform-value \(\mathsf{InqBT}\). It is not a characterization for larger signatures, multiple team coordinates, or the range-generating extension. The MSO quantifier-rank threshold \(2^q\) is a sufficient game bound and is not claimed sharp. The explicit finite cutoff number depends on the chosen classical first-order translation and is not optimized. Searches and inspected sources do not prove absolute historical novelty; a more general historical monadic-team theorem could subsume this particular statement. Independent expert validation has not been carried out.

## References

1. J. Kontinen and I. Ciardelli, *On the Expressive Power of Inquisitive Team Logic and Inquisitive First-Order Logic*, arXiv:2603.08646 (first public 2026-03-09), especially Definition 2.1 and Theorem 3.6, https://arxiv.org/html/2603.08646.
2. J. Kontinen and F. Yang, *Complete Logics for Elementary Team Properties*, arXiv:1904.08695 (2019; revised 2022), especially Section 2 and Theorems 3.1--3.7, https://arxiv.org/pdf/1904.08695.
3. I. Ciardelli and G. Conti, *Connecting state-based and team-based inquisitive logic*, Journal of Logic and Computation (2026), DOI 10.1093/logcom/exag032.
4. G. Grilletti and I. Ciardelli, *Games and Cardinalities in Inquisitive First-Order Logic*, Review of Symbolic Logic (2023), DOI 10.1017/S1755020321000198.
