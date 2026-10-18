# Transitivity and exact analogy counts for finite unary permutations

## Finding

Let \(A\) be a nonempty finite set and let \(f:A\to A\) be a permutation, regarded as a monounary algebra in the language containing only \(f\). Write its disjoint cycles as \(C_1,\ldots,C_r\), with lengths \(n_1,\ldots,n_r\ge1\). Denote by \(\approx\) the four-place analogical-proportion relation defined by Antić's term-justification and directed-maximality semantics [1,2].

**Complete classification.** If \(a,b\) belong to different cycles and \(c,d\) belong to different cycles, then \(a:b::c:d\) holds. If precisely one of the pairs \((a,b)\), \((c,d)\) crosses between cycles, it fails. If \(a,b\in C_i\) and \(c,d\in C_j\), let \(\delta_i(a,b)\in\mathbb Z/n_i\mathbb Z\) be the unique residue satisfying \(b=f^{\delta_i(a,b)}(a)\), and similarly for \(\delta_j(c,d)\). Then
\[
a:b::c:d\quad\Longleftrightarrow\quad
\delta_i(a,b)\equiv\delta_j(c,d)\pmod{\gcd(n_i,n_j)}.
\]

**Exact count.** Put \(N=|A|=\sum_i n_i\) and \(K=N^2-\sum_i n_i^2\). The number of ordered analogical quadruples is
\[
\boxed{\mathcal A(f)=K^2+\sum_{i=1}^r\sum_{j=1}^r\frac{n_i^2n_j^2}{\gcd(n_i,n_j)}.}
\]
Consequently a uniformly sampled quadruple satisfies the proportion with probability \(\mathcal A(f)/N^4\).

**Exact transitivity criterion.** The analogical-proportion relation is transitive as a binary relation on ordered pairs, in the sense
\[
(a:b::c:d)\ \land\ (c:d::e:g)\ \Longrightarrow\ (a:b::e:g),
\]
for all six entries, **if and only if all permutation cycles have equal length**. If there are \(r\) cycles of a common length \(n\), the relation is an equivalence relation on ordered pairs with \(n\) classes of size \(rn\), indexed by within-cycle displacement, and (if \(r>1\)) one additional class of size \(r(r-1)n^2\) consisting of all between-cycle arrows.

In particular, the three-element permutation with cycles of lengths \(1\) and \(2\) is a smallest finite unary-permutation counterexample to proportion transitivity. The classification solves the finite-bijective case of the characterization problem explicitly posed as Problem 7 in [1]; it is not a classification of general monounary algebras.

## Assumptions and scope

The universe is finite and nonempty; \(f\) is bijective; the signature contains a single unary function and no constant or relation symbols. Terms are exactly \(f^u(z)\), \(u\in\mathbb N_0\). For an ordered pair \((a,b)\), its justification set is
\[
J(a,b)=\{(u,v)\in\mathbb N_0^2:\exists x\in A,\ f^u(x)=a,\ f^v(x)=b\}.
\]
A justification is *trivial* if it lies in every arrow-justification set, equivalently if it justifies every possible arrow proportion. The directed proportion \(a\to b:\!\cdot\ c\to d\) holds when either both arrow-justification sets contain only trivial justifications, or their intersection contains a nontrivial justification and is inclusion-maximal among \(J(a,b)\cap J(c,d')\) as \(d'\) ranges over \(A\). The complete proportion \(a:b::c:d\) requires this assertion in the four orientations \((a,b,c,d)\), \((b,a,d,c)\), \((c,d,a,b)\), \((d,c,b,a)\), exactly as defined in [1, Definition 1].

## Proof

**1. Individual arrow justifications.** A unary term is \(f^u(z)\). If \(a,b\) lie in distinct cycles, there is no common term witness and \(J(a,b)=\varnothing\). If both lie in \(C_i\), and \(b=f^{\delta_i(a,b)}(a)\), then
\[
J(a,b)=\{(u,v)\in\mathbb N_0^2:v-u\equiv\delta_i(a,b)\pmod{n_i}\}.
\]
The reverse implication follows by choosing the unique point \(x=f^{-u}(a)\) in \(C_i\) (negative powers are used only to select this witness, not as language terms). This establishes equality of the infinite justification sets, not merely agreement on a finite truncation.

**2. Directed maximality.** Suppose both arrows are internal to cycles \(C_i,C_j\). By the generalized Chinese remainder theorem, their justification intersection is nonempty precisely when their two displacements agree modulo \(g=\gcd(n_i,n_j)\). For a fixed source point \(c\in C_j\), the sets \(J(c,d')\) for distinct \(d'\in C_j\) are disjoint congruence classes of \(v-u\pmod{n_j}\); for \(d'\notin C_j\), they are empty. Thus any nonempty intersection \(J(a,b)\cap J(c,d)\) is maximal against all alternative targets \(d'\), since distinct alternatives yield disjoint intersections. When \(|A|>1\), such a nonempty intersection always contains a nontrivial justification: if there is more than one cycle, cross-cycle arrows have empty justification sets; if there is a single cycle of length greater than one, displacements give disjoint nonempty classes. The singleton algebra is exceptional only in that every justification is trivial; its sole proportion holds by the trivial clause, agreeing with the claimed formula.

If both arrows cross cycles, both sets are empty and the trivial clause holds. If exactly one arrow crosses cycles, its set is empty while the internal arrow has a nontrivial justification, so neither clause applies. Reversing an internal arrow negates its displacement; the compatibility congruence survives this negation and the exchange of the two arrows. All four directed orientations therefore have the same classification as stated.

**3. Counting.** There are \(K\) between-cycle ordered arrows. Every ordered pair of them is analogical, contributing \(K^2\). For fixed cycles \(C_i,C_j\) and \(g=\gcd(n_i,n_j)\), each residue class modulo \(g\) contains exactly \(n_i^2/g\) ordered arrows internal to \(C_i\): \(n_i\) possible origins and \(n_i/g\) permissible destinations per origin. Pairing matching residue classes contributes \(g(n_i^2/g)(n_j^2/g)=n_i^2n_j^2/g\). Summing proves the count and probability formula.

**4. Transitivity.** If every \(n_i=n\), all within-cycle arrows are partitioned by their common displacement in \(\mathbb Z/n\mathbb Z\), and all cross-cycle arrows form one disjoint equivalence class (when any exist). This is an equivalence relation, hence transitive, with the sizes stated above. Conversely, suppose \(n_i>n_j\) and put \(g=\gcd(n_i,n_j)\), so \(0<g<n_i\). Choose \(a\in C_i\), \(c\in C_j\), and \(b=f^g(a)\ne a\). The displacement formula gives \(a:a::c:c\) and \(c:c::a:b\), because \(g\equiv0\pmod g\), but it rules out \(a:a::a:b\), because \(g\not\equiv0\pmod{n_i}\). Thus transitivity fails. This witness works for every unequal pair of cycle lengths.

For minimality, a permutation on one or two points has either one cycle or cycles all of length one; both satisfy transitivity. The \((1,2)\) example has three points and fails.

## Verification

The standalone program `verify.py` evaluates Antić's directed-maximality definition by enumerating term pairs \((u,v)\) modulo the order \(L=\operatorname{lcm}(n_1,\ldots,n_r)\) of the permutation. Periodicity makes these residue pairs an exact finite representation of each infinite justification set. It constructs the sets by independent term-and-witness evaluation rather than by the cycle-displacement formula. It then checks every four-entry proportion, the closed count, equivalence-class multiplicities and transitivity.

Running `python verify.py` completed successfully: `VERIFY_OK compositions=127 tested_quadruples=207541 direct_justifications=YES exact_counts=YES transitivity=YES`. The cases comprise every ordered composition of each positive integer from one to seven. These checks are finite corroboration; the preceding argument proves the result for all finite permutations.

For a two-cycle together with a three-cycle, the formula gives \(251\) satisfying quadruples among \(625\); unequal lengths force failure of transitivity. For two two-cycles, it gives \(96\) satisfying quadruples among \(256\), with a transitive proportion relation.

## Relationship to prior work

Antić [1, Definition 1] supplies the four-direction justification semantics, proves failures of transitivity in general, and explicitly asks for a characterization of monounary algebras enjoying transitivity in Problem 7. The present statement settles that question **within the finite bijective subclass**, not in general, and adds a complete arithmetic proportion test and exact counting formula. The source's difference theorem for the successor algebra \((\mathbb N,S)\) and its two-element cycle comparisons do not imply the multi-cycle gcd rule or the transitivity dichotomy. Antić [2] supplies the general abstract framework but not this finite-permutation classification. Other classifications of monounary algebras by cycle/depth or homomorphism invariants concern different relations and do not imply the present analogical predicate. An undiscovered equivalent characterization remains possible.

## Limitations

The assumption that \(f\) is bijective is essential to the proof: a nonperiodic incoming tree changes the justification sets and can destroy the simple residue-class description. The classification does not resolve the corresponding problem for arbitrary finite or infinite monounary algebras. The count measures ordered element-quadruples, not isomorphism classes. The independent finite verification covers sizes at most seven only. Originality conclusions are based on the identified and inspected sources and do not constitute a priority certificate.

## References

[1] C. Antić, *Analogical proportions in monounary algebras*, Annals of Mathematics and Artificial Intelligence **92** (2024), 1663–1677, DOI: 10.1007/s10472-023-09921-7. Earliest identified public preprint: arXiv:2208.06829, 14 August 2022; see Definition 1 and Problem 7.

[2] C. Antić, *Analogical proportions*, Annals of Mathematics and Artificial Intelligence **90** (2022), 595–644, DOI: 10.1007/s10472-022-09798-y; preprint arXiv:2006.02854. See the abstract justification framework and general nontransitivity results.

[3] D. Jakubíková-Studenovská, *Monounary algebras and their pseudovarieties*, abstract describing cycle-length/depth descriptions of finite monounary pseudovarieties (background on cycle classifications, not on analogical proportions), https://tu-dresden.de/die_tu_dresden/fakultaeten/fakultaet_mathematik_und_naturwissenschaften/fachrichtung_mathematik/institute/algebra/aaaseries/prev/abstracts/abstracts80/21.pdf.
