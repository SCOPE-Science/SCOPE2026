# Exact finite-arity type spectrum of the existentially closed projective plane
## Finding
Let \(T_{2,2}\) be the complete theory, in the incidence language \(\{P,L,I\}\), of existentially closed combinatorial projective planes. Then its complete type spaces over the empty set have the exact cardinalities
\[
|S_0(T_{2,2})|=1,\qquad |S_1(T_{2,2})|=2,\qquad |S_2(T_{2,2})|=8,\qquad |S_3(T_{2,2})|=48,
\]
and
\[
|S_n(T_{2,2})|=2^{\aleph_0}\qquad(n\ge 4).
\]
Thus the finite arities have the sharp spectrum
\[
1,2,8,48,2^{\aleph_0},2^{\aleph_0},\ldots .
\]

There is a finer three-variable census. Among the \(28\) injective complete \(3\)-types, algebraic-closure sizes \(3,4,5,6\) occur with multiplicities
\[
6,14,6,2,
\]
respectively.

## Assumptions and scope
The result is for the original two-sorted incidence presentation used by Conant and Kruckman: \(P\) and \(L\) name points and lines, and \(I\) is incidence. In a model of \(T_{2,2}\), every two distinct points determine a unique line and every two distinct lines meet in a unique point.

Two results from Conant--Kruckman are used as inputs. First, algebraic closure is incidence closure, and two tuples have the same complete type over a parameter set exactly when their marked algebraic closures are isomorphic over that parameter set. Second, their Theorem 3.3 constructs continuum many complete \(4\)-types; Remark 3.4 observes that arity \(4\) is the first infinite type space. The new contribution here is the exact enumeration in arities \(1,2,3\), together with the resulting complete all-arity cardinal spectrum and the closure-size refinement for injective triples.

## Proof
Conant--Kruckman Proposition 2.14 identifies \(\operatorname{acl}(A)\) with the closure obtained by repeatedly adjoining the unique connecting line of every pair of points already present and the unique intersection point of every pair of lines already present. Their Corollary 2.15 says that the complete type of a tuple is determined exactly by the isomorphism type of this finite or countable incidence closure with the tuple coordinates marked.

For one variable there are exactly two possibilities: a point or a line. Hence \(|S_1|=2\).

For two variables, first separate equality from inequality. If the variables are equal, there are two types, according to sort. If they are distinct and of the same sort, there is one point--point type and one line--line type. If they have opposite sorts, each of the two ordered sort patterns \((P,L)\) and \((L,P)\) splits into incident and nonincident cases. Therefore
\[
|S_2|=2+1+1+2+2=8.
\]

For three variables, partition by the equality pattern.

If all three coordinates are equal, there are \(2\) types. If exactly two coordinates are equal, choose the repeated pair in \(3\) ways. After collapsing it, the remaining ordered pair must be distinct, and there are \(6\) such two-variable types: point--point, line--line, and the four oriented mixed incidence/nonincidence types. This contributes \(3\cdot6=18\).

Now suppose all three coordinates are distinct. Three points give two types, according as they are collinear or noncollinear; dually, three lines give two types, according as they are concurrent or nonconcurrent. For exactly two points and one line, choose the position of the line in \(3\) ways. Its incidence set on the two marked points can be any of the four subsets of those two points. The case of incidence with both points simply says that the marked line is their unique connecting line. Hence this sort pattern contributes \(3\cdot4=12\) types. The dual case of one point and two lines contributes another \(12\). Consequently the injective contribution is
\[
2+2+12+12=28,
\]
and altogether
\[
|S_3|=2+18+28=48.
\]

The same classification gives the injective closure-size distribution. In the mixed two-point/one-line case, incidence with both points gives closure size \(3\), incidence with exactly one gives size \(4\), and incidence with neither gives size \(5\); the dual cases behave identically. A collinear point triple or concurrent line triple has closure size \(4\), while a noncollinear point triple or nonconcurrent line triple has closure size \(6\). Thus the numbers of injective types of closure sizes \(3,4,5,6\) are \(6,14,6,2\).

Finally, Conant--Kruckman construct an injection from \(2^\omega\) into \(S_4(T_{2,2})\), so \(|S_4|=2^{\aleph_0}\), since the language is countable. For every \(n>4\), repeat the fourth coordinate in all additional positions. This gives an injection \(S_4\hookrightarrow S_n\). Again a countable language has at most continuum many complete finite-arity types, hence \(|S_n|=2^{\aleph_0}\) for all \(n\ge4\).

## Verification
A standalone verifier uses the Fano plane as a finite witness structure for every local configuration needed in arities at most three. It exhausts all ordered \(n\)-tuples for \(n=1,2,3\), computes incidence closure by iterating joins and meets, canonically labels the resulting finite marked incidence structure, and counts distinct canonical forms. It returns exactly
\[
2,8,48.
\]
For injective triples it independently returns \(28\) marked closure types and the closure-size distribution
\[
3^{\times6},\ 4^{\times14},\ 5^{\times6},\ 6^{\times2}.
\]
The captured output ends with `VERIFY_OK`.

The computation is only a finite check of the low-arity classification. The continuum statement for arity four and above rests on the published construction in Theorem 3.3.

## Relationship to prior work
Conant and Kruckman characterize algebraic closure and prove that marked algebraic closure determines complete type. They also prove that \(T_{2,2}\) has continuum many \(4\)-types and explicitly note that arity \(4\) is minimal for infinitude. The inspected article does not give the exact finite values \(2,8,48\), the \(28\)-type injective triple census, or the closure-size distribution above.

A separate earlier result uses the broader \(T_{m,n}\) incidence framework to identify one-line extension polynomials with hypergraph independence polynomials. That result concerns finite one-point extension admissibility and computational complexity, not complete type spaces of \(T_{2,2}\), so it does not imply the present spectrum.

Targeted semantic-database searches for “existentially closed projective planes exact complete 3-type count 48”, “\(T_{2,2}\) \(S_3\) 48 types”, and aliases involving generic projective planes and three-generated algebraic closure produced no equivalent statement. Exact web searches likewise returned the Conant--Kruckman paper and unrelated projective-geometry results, but no published \(2,8,48\) type census.

## Limitations
The finite counts are special to \(m=n=2\). Conant and Kruckman explicitly leave open the analogous minimal-arity/local-finiteness question for general \(T_{m,n}\), so no extension of the \(2,8,48\) formula to arbitrary \(m,n\) is claimed here. The originality assessment is based on targeted searches rather than a proof that the small census has never appeared as folklore or in an unindexed source.

## References
1. Gabriel Conant and Alex Kruckman, *Independence in generic incidence structures*, Journal of Symbolic Logic 84 (2019), 750--780. arXiv:1709.09626. DOI: 10.1017/jsl.2019.8.
2. In particular: Proposition 2.14 (algebraic closure is incidence closure), Corollary 2.15 (types are marked-closure isomorphism types), Theorem 3.3 (continuum many \(4\)-types), and Remark 3.4(3) (arity \(4\) is the first infinite type space).
