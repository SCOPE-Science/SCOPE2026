# Exact depth-one semantic quotient for two-agent belief disagreement

## Finding
For every integer \(k\ge 1\), consider the Boolean language on exactly \(k\) propositional letters with the *sole modal connective* \(\mathsf D\), interpreted over arbitrary two-agent \(\mathsf{KD45}\) Kripke models by
\[
\mathsf D\varphi :=(B_1\varphi\land B_2\neg\varphi)\lor(B_2\varphi\land B_1\neg\varphi).
\]
Put \(m=2^k\) and \(H_m=(3^m-2^{m+1}+3)/2\). The depth-at-most-one formulas have exactly \(mH_m\) pointed semantic equivalence classes, and exactly \(2^{mH_m}\) equivalence classes of formulas. An invariant for a pointed model is its current valuation together with either one null marker or an unordered pair of disjoint nonempty supports of its agents' successor valuations. Every invariant is realized and is isolated by a depth-one formula.

If the invariant is a disjoint pair \(\{S,T\}\) of nonempty valuation sets and the current valuation is \(v\), its smallest realizing model has exactly
\[
|S|+|T|+\mathbf 1_{v\notin S\cup T}
\]
worlds. The null invariant has a one-world realization. Thus every satisfiable depth-one formula has a model with at most \(2^k\) worlds, and this is sharp for each \(k\ge 1\).

Modal nesting genuinely increases expressive power already with two worlds: two pointed \(\mathsf{KD45}\) models agree on every depth-one formula but are separated by \(\mathsf D(\mathsf Dp)\). No one-world pair can witness such a separation.

## Assumptions and scope
Fix exactly two agents, an arbitrary nonempty Kripke world set, and \(k\) propositional variables. Each agent's accessibility relation is serial, transitive and Euclidean, without assumptions relating the two agents. The Boolean connectives are unrestricted. Nesting depth counts occurrences of \(\mathsf D\) along any syntax-tree branch, so its depth-one argument is purely propositional. The semantic equivalence of pointed models is agreement on every depth-one formula; formula equivalence is truth agreement at every pointed model in this class. We do *not* assume reflexivity, equality of successor relations, or a finite ambient frame. The finite-model results refer to finite representatives, not a priori finite input frames.

Write \(V=\{0,1\}^k\), so \(|V|=m\). At a pointed model \((M,w)\), let \(v\in V\) be the valuation of \(w\), and let
\[
S_i=\{\operatorname{val}(u):wR_i u\}\subseteq V,\qquad i\in\{1,2\}.
\]
Seriality makes both sets nonempty. For each \(P\subseteq V\), let \(\chi_P\) be the propositional disjunction of exactly the complete valuation minterms belonging to \(P\), with the empty disjunction interpreted as false.

## Proof
**1. Modal truth table.** Directly from the semantics of universal belief,
\[
(M,w)\models\mathsf D\chi_P
\quad\Longleftrightarrow\quad
(S_1\subseteq P\ \&\ S_2\cap P=\varnothing)
\ \lor\
(S_2\subseteq P\ \&\ S_1\cap P=\varnothing).
\tag{1}
\]
If \(S_1\cap S_2\ne\varnothing\), every such test is false, because one common valuation would have to belong simultaneously to \(P\) and its complement. Conversely, if \(S_1\cap S_2=\varnothing\), then \(P=S_1\) and \(P=S_2\) are positive tests. Furthermore, the inclusion-minimal positive tests are *exactly* \(S_1,S_2\): every positive test contains one of them and cannot contain the other. Consequently the complete vector of positive and negative tests distinguishes exactly the null overlap case or the unordered disjoint pair \(\{S_1,S_2\}\). Ordinary propositional minterms additionally distinguish the root valuation \(v\). Any Boolean depth-one formula is a Boolean combination of the root's propositional literals and finitely many tests of the form \(\mathsf D\chi_P\), hence these data determine its truth; conversely the complete test vector defines each data type by a finite conjunction.

**2. Realization and exact counting.** To realize the null type with any prescribed \(v\), take a single reflexive world of valuation \(v\) for both agents. To realize \((v,\{S,T\})\) with \(S,T\) nonempty and disjoint, introduce one world for each valuation in \(S\cup T\), plus one new root world only if \(v\notin S\cup T\). Otherwise choose the world's copy of \(v\) as root. Let \(C_1,C_2\) be the distinct-world sets corresponding to \(S,T\). For each agent \(i\), set \(R_i(u)=C_i\) for every \(u\in C_i\), and also \(R_i(w)=C_i\) for the root. At any other world outside \(C_i\) (excluding the root), set \(R_i(u)=\{u\}\). Each resulting accessibility relation is serial, transitive and Euclidean: whenever \(uR_i u'\), the successor rows of \(u\) and \(u'\) agree. This realizes precisely the desired supports and root valuation.

The number of *ordered* disjoint nonempty pairs \((S,T)\) is \(3^m-2\cdot 2^m+1\): each valuation belongs to \(S\), to \(T\), or to neither, and inclusion-exclusion removes empty sets. Swapping \(S,T\) fixes no such pair, so division by two gives \((3^m-2^{m+1}+1)/2\) unordered pairs. Adding the null marker gives \(H_m=(3^m-2^{m+1}+3)/2\) support types. All \(m\) root valuations are independent and realizable, yielding exactly \(mH_m\) pointed types. Because each of these finitely many types has a defining depth-one formula, arbitrary unions of types are expressible; therefore precisely \(2^{mH_m}\) formula-equivalence classes exist.

**3. Minimal worlds and the uniform sharp bound.** For disjoint supports, no world can simultaneously have a valuation from \(S\) and from \(T\). Thus any representative needs at least \(|S|+|T|\) distinct worlds; if the current valuation \(v\) is outside their union, the root is one further distinct world. The preceding realization attains this bound. The null class is attained on one world. If \(v\in S\cup T\), the minimum is at most \(m\); otherwise \(|S|+|T|\le m-1\), hence the minimum is still at most \(m\). Choose any partition \(V=S\sqcup T\) into two nonempty blocks and take \(v\in S\). The complete depth-one type formula that isolates \((v,\{S,T\})\) can hold only in models with at least \(|S|+|T|=m\) worlds. Such a partition exists for \(k\ge1\), proving sharpness.

**4. The first nesting boundary.** Let worlds be \(a,b\), with \(p(a)\) true and \(p(b)\) false. In both models take \(R_2(a)=R_2(b)=\{b\}\) and \(R_1(a)=\{a\}\). In model \(M\), set \(R_1(b)=\{b\}\); in model \(N\), set \(R_1(b)=\{a\}\). All rows are nonempty, and whenever a row includes a world the included world's row agrees with it, proving \(\mathsf{KD45}\) for both relations. At root \(a\), both models have the same root valuation and successor supports \(\{\operatorname{val}(a)\}\) and \(\{\operatorname{val}(b)\}\), so part 1 gives depth-one equivalence. In \(M\), \(\mathsf Dp\) is true at \(a\) and false at \(b\); in \(N\), it is true at both worlds. Therefore \(M,a\models\mathsf D(\mathsf Dp)\) but \(N,a\not\models\mathsf D(\mathsf Dp)\). On a singleton, the two serial relations are necessarily reflexive, so every \(\mathsf D\varphi\) is false and no depth-two separation of depth-one-equivalent pointed singleton models is possible.

## Verification
Run `python3 checker.py` with Python 3.10 or later. The standalone checker enumerates all ordered nonempty support-set pairs for valuation-set sizes \(m\in\{1,2,3,4,8\}\), compares every one of the \(2^m\) tests in equation (1), confirms the bijection between test signatures and the predicted invariants, and verifies the formula for \(H_m\). It also checks seriality/transitivity/Euclideanity via successor-row equalities on both explicit two-world frames and reproduces the depth-two separation. Its expected final output is `ALL_CHECKS_OK`. These finite tests verify instances of the statements; the proof above establishes every quantified case.

## Relationship to prior work
Ding and Yang's *A General Theory of Propositional Modal Bundled Modalities* (first publicly submitted 27 March 2026, arXiv:2603.26268v1) develops a general bisimulation and axiomatization theory and specifically studies group disagreement on \(\mathsf{KD45}\). The two-agent strong-disagreement operator is older: Chen and Pan studied its logic in 2017. Fan's *A Uniform Approach to Axiomatizing Bundled Operators* (published online 2025) addresses related bundled-operator axiomatizations. Those precedents define the setting and establish broad logical results; the present statement isolates the exact finite-variable *depth-one* quotient, counts all its types and definable properties, gives minimum representative sizes, and locates a sharp two-world depth-two distinction. The general bisimulation and axiomatization results are not claimed as new. Searches for equivalent support signatures and stronger covering statements yielded no confirmed earlier theorem with these exact conclusions, which is not a proof of priority.

## Limitations
This theorem is specific to exactly two agents, this *symmetric* disagreement connective, fixed finite propositional vocabulary, and modal depth at most one except for the explicit depth-two counterexample. It is not a complete classification at depth two or arbitrary depth, and does not establish an optimal decision procedure. The 2017 Chen–Pan full text could not be fully inspected; an equivalent earlier finite-fragment analysis remains a genuine originality risk. An unrestricted general bisimulation characterization may indirectly imply part of the support equivalence, but the exact quotient/cardinality/minimum-size assertions are not independently attributed to it. Numerical enumeration is a regression check, not an infinite proof.

## References
1. Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268, originally posted 27 March 2026; https://arxiv.org/abs/2603.26268 .
2. J. Chen and T. Pan, *Logic for Describing Strong Belief-Disagreement Between Agents*, published online 5 May 2017, DOI:10.1007/s11225-017-9724-1; https://doi.org/10.1007/s11225-017-9724-1 .
3. J. Fan, *A Uniform Approach to Axiomatizing Bundled Operators*, published online 4 November 2025, DOI:10.1017/S1755020325100981; https://doi.org/10.1017/S1755020325100981 .
