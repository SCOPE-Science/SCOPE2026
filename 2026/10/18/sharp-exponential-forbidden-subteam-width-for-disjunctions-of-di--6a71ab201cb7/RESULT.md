# Sharp exponential forbidden-subteam width for disjunctions of distinct constancy atoms

## Finding
For every integer \(n\ge 1\), let
\[
\Phi_n=\operatorname{dep}(x_1)\vee\cdots\vee\operatorname{dep}(x_n),
\]
where the \(n\) variables are pairwise distinct, \(\operatorname{dep}(x_i)\) means that the value of \(x_i\) is constant on the team, and disjunction is evaluated with ordinary lax team semantics.

**Sharp forbidden-subteam theorem.** For every structure with arbitrary domain and every team \(T\) whose assignment domain contains these variables,
\[
T\models\Phi_n
\quad\Longleftrightarrow\quad
(\forall U\subseteq T)(|U|\le 2^n\Longrightarrow U\models\Phi_n).
\]
The upper bound \(2^n\) is minimal among all bounds holding uniformly over structures and teams: the binary cube \(\{0,1\}^n\) fails the formula, whereas every proper subteam satisfies it. In addition, the size of any finite inclusion-minimal failing team lies between \(n+1\) and \(2^n\), and both endpoints occur.

The term *forbidden-subteam width* here is explicitly defined by **at-most** cardinality. It is independent of any convention that treats \(k\)-coherence as a property of subteams of *exactly* \(k\) elements; these conventions should not be silently interchanged.

## Assumptions and scope
A team is a set, possibly infinite, of assignments with a fixed finite variable domain that includes \(x_1,\ldots,x_n\). The structure may be finite or infinite; no restriction on cardinalities of coordinate value sets is imposed. For each \(i\), the constancy atom holds on a subteam \(S\) exactly when all assignments in \(S\) have the same \(x_i\)-value. In particular, it holds on empty and singleton subteams. Lax disjunction allows a covering union of subteams, with overlaps permitted; in this constancy-only setting, overlaps can equivalently be removed by assigning each tuple to one suitable component.

Project \(T\) to its \(n\) named coordinates, obtaining a set of tuples in \(A_1\times\cdots\times A_n\). Satisfaction depends only on this projection: multiplicities and further variables play no role. Here \(A_i\) can be taken as the value set of coordinate \(i\) in the ambient structure. Call a set of tuples *cross-coverable* when there are values \(a_i\in A_i\), one per coordinate, such that
\[
(\forall t\in T)(\exists i\in\{1,\ldots,n\})\ t_i=a_i.
\]
For the empty team, the cross-covering condition is interpreted as true without requiring the existence of ambient values. When \(T\ne\varnothing\), suitable values can always be sought among those realized in \(T\). The semantic condition \(T\models\Phi_n\) is equivalent to cross-coverability.

## Proof
**Step 1 (semantic reduction).** Suppose \(T=\bigcup_i S_i\) and \(S_i\models\operatorname{dep}(x_i)\). Choose for every nonempty \(S_i\) its fixed value \(a_i\). For empty \(S_i\), choose any value from the nonempty team's ambient coordinate domain; the chosen hyperplanes cover \(T\). Conversely, if values \(a_i\) cover \(T\), put \(S_i=\{t\in T:t_i=a_i\}\); these teams cover \(T\) and each has constant \(i\)-th coordinate. This also handles arbitrarily nested bracketing of the displayed finite disjunction.

**Step 2 (finite character for arbitrarily large teams).** We show by induction on the number \(n\) of coordinates that cross-coverability of all finite subteams implies cross-coverability of \(T\). The empty set is harmless. If \(T\ne\varnothing\), fix \(r\in T\). Every finite subteam \(S\) containing \(r\) has a cross-cover in which at least one of the selected values equals \(r_i\) in its coordinate. There exists one fixed coordinate \(i\) such that *every* finite \(S\) containing \(r\) has a cover with \(a_i=r_i\): otherwise, for each of the finitely many coordinates choose a finite counterexample \(S_i\ni r\), and their union would have no cover, contradicting the hypothesis.

Let \(T_i=\{t\in T:t_i\ne r_i\}\). Every finite \(F\subseteq T_i\) occurs in \(F\cup\{r\}\), which is coverable with the fixed choice \(a_i=r_i\). None of the points in \(F\) is covered by coordinate \(i\), hence \(F\) is coverable using the other \(n-1\) coordinates. By induction, \(T_i\) is coverable with those coordinates. Together with \(a_i=r_i\), these cover the whole of \(T\). The induction's base case of zero coordinates is immediate: only the empty team is coverable, so any nonempty team already has a finite noncoverable subteam. The theorem thus reduces to finite failing teams.

**Step 3 (a tensor-rank bound on minimal obstructions).** Let \(U\) be a finite, inclusion-minimal non-cross-coverable set, and write \(m=|U|\). For every \(u\in U\), the set \(U\setminus\{u\}\) has a cross-cover by values \(a_i^{(u)}\). Since \(U\) itself is not coverable, that cover misses \(u\) in *every* coordinate. Thus
\[
  u_i\ne a_i^{(u)}\quad(1\le i\le n),
\]
while for every \(v\in U\setminus\{u\}\) at least one index \(i\) satisfies \(v_i=a_i^{(u)}\). All values appearing in \(U\) or among the finitely many selected values \(a_i^{(u)}\) form finite coordinate sets. For each coordinate choose an injective labeling \(h_i\) of that finite set by rational numbers.

In the \(2^n\)-dimensional rational vector space \(V=(\mathbb Q^2)^{\otimes n}\), define the vectors and dual covectors
\[
 P(v)=\bigotimes_{i=1}^n(1,h_i(v_i)),
 \qquad
 Q(u)=\bigotimes_{i=1}^n(-h_i(a_i^{(u)}),1).
\]
Their pairings are
\[
 Q(u)(P(v))=\prod_{i=1}^n\big(h_i(v_i)-h_i(a_i^{(u)})\big).
\]
This is zero when \(v\ne u\) because some coordinate matches the associated cover; it is nonzero when \(v=u\) because no coordinate matches. Therefore the \(m\times m\) pairing matrix is diagonal with nonzero diagonal. The \(m\) vectors \(P(v)\) are linearly independent in \(V\), giving \(m\le\dim V=2^n\).

By Step 2, every noncoverable, possibly infinite \(T\) has a finite noncoverable subset. Choose an inclusion-minimal one and apply Step 3. This establishes the asserted uniform obstruction width \(2^n\).

**Step 4 (sharpness).** Take the full Boolean cube \(B=\{0,1\}^n\). Given any candidate selected values \(a_i\), if a selected value is outside \(\{0,1\}\), replace it by either Boolean value without reducing coverage of \(B\). The complementary tuple \(b\in B\) with \(b_i\ne a_i\) for every coordinate is uncovered, so \(B\not\models\Phi_n\). For every proper subset \(W\subsetneq B\), choose a missing Boolean tuple \(b\in B\setminus W\) and set \(a_i=1-b_i\). The only Boolean tuple escaping these hyperplanes is \(b\), so \(W\models\Phi_n\). Hence the bound cannot be reduced.

**Step 5 (smallest possible obstructions).** Any team of at most \(n\) assignments is cross-coverable: assign a different coordinate to each row and select that row's value in its assigned coordinate; assign remaining coordinates arbitrarily. Conversely, with \(n+1\) distinct values \(c_1,\ldots,c_{n+1}\), the diagonal team
\[
 D=\{(c_j,\ldots,c_j):1\le j\le n+1\}
\]
is not cross-coverable, since each coordinate hyperplane meets \(D\) in at most one row. Every proper subteam of \(D\) has at most \(n\) rows, hence is coverable. Thus \(n+1\) and \(2^n\) are both attained among sizes of inclusion-minimal failures. No assertion about attainment of every intervening integer is made.

## Verification
The standalone file `verify.py` directly evaluates the finite cross-cover semantics, enumerates all teams on four small finite Cartesian universes, extracts each inclusion-minimal failing team, and checks the invertible diagonal tensor pairing for each. It also performs reproducible pseudorandom tests over larger alphabets and checks binary-cube obstructions in dimensions \(1\) through \(6\). Its successful output is:

`CONSTANCY_COHERENCE_VERIFY_OK exhaustive_teams=788 failures=337 minimal=54 random_minimal=268 tensor_pairings=30790 cube_levels=1..6`

The experiment uses integer tensor coordinates and tests the actual pairing matrix; it does not purport to enumerate infinite domains, arbitrary teams or arbitrary dimensions. The general statements follow from the proofs above. Reproduce with `python3 verify.py` using the Python standard library.

The theorem also yields an explicit universal first-order condition over the relation of team tuples: one needs to test only \(2^n\) rows at a time, with repetitions of rows permitted in the quantification. For any enumerated sample of \(k\le 2^n\) rows, coverability amounts to a finite disjunction over choices of one of those rows per coordinate, checking that all sampled rows match at least one of the chosen coordinate values. This consequence is *not* a claim that ordinary first-order definability of the underlying constraint is new.

## Relationship to prior work
Fröhlich, Kolaitis and Meier (arXiv:2508.16146; CSL 2026) calculate the bound \(4\) for a disjunction of two constancy atoms (Corollary 23), thereby covering the present \(n=2\) case. Their primary analysis concerns *two* dependence atoms, not the optimal bound for arbitrary numbers of distinct unary constancy disjuncts.

Barlag et al. (arXiv:2605.31269, 2026) prove qualitative links between coherence and first-order rewritability and discuss repeated occurrences of a constancy atom on the *same* variable. The propositional binary setting in their Section 5.1 has the trivial domain-based upper bound \(2^n\) on team size. That does not give a dimension-dependent bound independent of potentially unbounded coordinate alphabets, which is the nontrivial part of the present statement. In particular, repeated copies of one atom and distinct-coordinate atoms are different objects.

The result can equally be read as a sharp finite-character/Helly-type theorem for covering an arbitrary relation by one coordinate fiber in each direction. The tensor proof explicitly controls minimal noncoverable relations. Literature searches did not identify a prior theorem with this exact strength, but absence of a search hit does not establish priority.

## Limitations
The bound is about disjunctions of **distinct constancy atoms**, not general dependence atoms or arbitrary quantifier-free dependence formulas. It uses lax team semantics and an *at-most* witness-size convention. It does not classify all inclusion-minimal obstructions or assert that every size strictly between the two extremal endpoints occurs. The result is self-reviewed, not independently audited. Older database-dependency, transversal-covering, and coherence literature may contain an equivalent result in different terminology; the earlier Kontinen coherence thesis could not be examined completely during this comparison. Finite checker results are corroborative and are not infinite proofs.

## References
- N. Fröhlich, P. G. Kolaitis, A. Meier, *Disjunctions of Two Dependence Atoms*, first public preprint 2025-08-22, arXiv:2508.16146; CSL 2026, DOI 10.4230/LIPIcs.CSL.2026.10. Full conference text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html
- T. Barlag, N. Fröhlich, M. Hannula, P. G. Kolaitis, J. Kontinen, A. Meier, J. Väänänen, *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269 (first public 2026-05-29); full text: https://arxiv.org/html/2605.31269v1
- J. Kontinen, *Coherence and Complexity in Fragments of Dependence Logic*, doctoral thesis, University of Amsterdam, 2010 (historical priority risk; complete text not inspected).
