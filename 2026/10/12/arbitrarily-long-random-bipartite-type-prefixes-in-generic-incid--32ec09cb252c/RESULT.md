# Arbitrarily long random-bipartite type prefixes in generic incidence theories

## Finding
Let \(T_{m,n}\) be Conant and Kruckman's complete theory of existentially closed \(K_{m,n}\)-free incidence structures, with \(m,n\ge 2\). For every arity
\[
0\le r<\min(m,n),
\]
the complete \(r\)-types over the empty set are exactly the equality quotients of finite labeled bipartite incidence patterns. Consequently, if \(a_r\) denotes the number of injective complete \(r\)-types, then
\[
\boxed{a_r=\sum_{p=0}^{r}\binom rp 2^{p(r-p)}}.
\]
Thus \((a_r)_{r\ge0}\) begins
\[
1,2,6,26,162,1442,18306,330626,\ldots,
\]
the classical sequence OEIS A047863 counting labeled graphs whose vertices are already colored by the two sides of a bipartition.

Allowing repeated coordinates, the full type count is the Stirling transform
\[
\boxed{|S_r(T_{m,n})|=b_r=\sum_{k=0}^{r}{r\brace k}a_k}
\qquad(r<\min(m,n)),
\]
where \({r\brace k}\) is a Stirling number of the second kind. The first values are
\[
1,2,8,46,362,3804,52994,981838,\ldots.
\]
Equivalently, for every fixed \(R\), all theories \(T_{m,n}\) with \(m,n>R\) have exactly the same complete type counts as the named-side random bipartite graph in every arity \(r\le R\).

This finite prefix can be arbitrarily long even though the theories are globally far from oligomorphic: Conant and Kruckman prove that \(S_{m+n}(T_{m,n})\) is uncountable for \(m,n\ge2\). Since the language is countable, this means
\[
|S_{m+n}(T_{m,n})|=2^{\aleph_0}.
\]
So the hierarchy contains theories with an arbitrarily long exact random-bipartite type prefix followed, at a later finite arity, by a continuum-sized type space.

## Assumptions and scope
The language is exactly \(\{P,L,I\}\), with unary predicates for points and lines and incidence only between the two sorts. The parameters \(m,n\) are fixed integers at least two, and types are complete types over the empty set in the home sort.

The exact formula is asserted only in the closure-free range \(r<\min(m,n)\). At or beyond that threshold, a tuple can contain enough distinct points or enough distinct lines to force new algebraic elements, so its complete type need not be determined by the induced incidence pattern alone. No formula is claimed here for those higher finite arities.

The integer sequence A047863 itself is prior enumerative data. The new claim is the exact identification of that sequence, and its Stirling transform, with the stabilized low-arity type profile of the generic incidence hierarchy, together with the resulting arbitrarily-long-prefix/continuum-explosion contrast.

## Proof
Fix \(r<\min(m,n)\), a monster model \(\mathbb M\models T_{m,n}\), and an \(r\)-tuple \(\bar a\). Let \(A\) be the set of distinct entries of \(\bar a\). Then \(A\) contains fewer than \(m\) points and fewer than \(n\) lines.

Conant and Kruckman define a set to be \(I\)-closed when it contains every line incident with \(m\) of its distinct points and, dually, every point incident with \(n\) of its distinct lines. Because \(A\) has too few elements of either sort for either trigger to occur, \(A\) is \(I\)-closed vacuously. Their Proposition 2.14 identifies algebraic closure with \(I\)-closure, hence
\[
\operatorname{acl}(\bar a)=A.
\]
Their Corollary 2.15 says that two tuples have the same complete type exactly when their marked algebraic closures are isomorphic. In the present range the marked algebraic closure is just the finite incidence pattern on the distinct tuple entries. Thus complete type is exactly equality data, side data, and cross-incidence data.

Conversely, every such finite pattern is realized. A finite incidence structure on fewer than \(m\) points and fewer than \(n\) lines is automatically \(K_{m,n}\)-free. By the model-companion/extension results in Section 2 of Conant and Kruckman, it embeds in a model of \(T_{m,n}\), hence into the monster. Therefore no finite pattern counted below is spurious.

For an injective ordered \(r\)-tuple, choose the \(p\) coordinates that are points. There are \(\binom rp\) choices. The remaining \(r-p\) coordinates are lines, and each of the \(p(r-p)\) possible point-line incidences can be chosen independently. Hence there are \(2^{p(r-p)}\) patterns for this side assignment, and summing over \(p\) gives
\[
a_r=\sum_{p=0}^{r}\binom rp2^{p(r-p)}.
\]

For an arbitrary ordered \(r\)-tuple, first choose its equality partition into \(k\) distinct values. There are \({r\brace k}\) such partitions. Ordering the blocks canonically, the quotient tuple is an injective ordered \(k\)-tuple, with \(a_k\) possible complete types. Since \(k\le r<\min(m,n)\), the preceding argument applies. Summing over \(k\) yields
\[
|S_r(T_{m,n})|=\sum_{k=0}^{r}{r\brace k}a_k.
\]

Finally, Conant and Kruckman's Remark 3.4 states that \(S_{m+n}(T_{m,n})\) is uncountable for every \(m,n\ge2\). A countable first-order language has at most continuum many complete finite-arity types, so the cardinality is exactly \(2^{\aleph_0}\). Choosing \(m,n>R\) proves the arbitrarily-long-prefix statement.

## Verification
The bundled verifier checks the two displayed sequences by exact integer arithmetic through arity seven. It also independently enumerates all colored bipartite incidence signatures, all equality partitions through arity five, and directly tests that every enumerated low-arity signature is \(K_{m,n}\)-free for \(2\le m,n\le6\) whenever \(r<\min(m,n)\).

Its recorded output is:

`a_0..7 = [1, 2, 6, 26, 162, 1442, 18306, 330626]`

`b_0..7 = [1, 2, 8, 46, 362, 3804, 52994, 981838]`

`exact assertions = 2523`

`VERIFY_OK`

The computation is a finite replay of the combinatorial counting step. The theorem for all \(m,n,r\) in the stated range follows from the algebraic-closure and type-by-closure results above, not from finite experimentation.

## Relationship to prior work
Conant and Kruckman prove the model-companion theorem for \(T_{m,n}\), identify algebraic closure with \(I\)-closure, characterize complete tuple types by marked algebraic closures, and prove uncountability of \(S_{m+n}(T_{m,n})\). The inspected paper does not state the low-arity counting formulas, the stabilization in \(m,n\), or the arbitrarily-long random-bipartite prefix consequence.

OEIS A047863 already records
\[
\sum_{p=0}^{r}\binom rp2^{p(r-p)}
\]
as the number of labeled two-colored graphs with edges only between unlike colors. That combinatorial enumeration is therefore treated as prior, not claimed as new. The contribution here is its exact model-theoretic realization throughout the closure-free range of the generic incidence hierarchy and the corresponding Stirling-transformed count when coordinates may repeat.

A targeted semantic-index search found an exact ordered-tuple orbit profile for side-preserving reducts of the random bipartite graph. That is adjacent prior art and supports treating the random-bipartite profile itself as known. It does not give the finite-prefix stabilization for the non-small theories \(T_{m,n}\), nor the contrast with their continuum-sized higher-arity type spaces.

Two adjacent prior calculations concern a one-line extension polynomial for finite \(K_{m,n}\)-free incidence structures and an exact low-arity census for the special projective-plane theory \(T_{2,2}\). The former concerns finite extensions of the universal base theory rather than complete types in the model companion. The latter is complementary: for example \(|S_3(T_{2,2})|=48\), while the closure-free stabilized value is \(b_3=46\) once \(m,n>3\).

## Limitations
The low-arity formulas stop strictly before \(\min(m,n)\). They do not resolve Conant and Kruckman's question about the first arity at which the type space becomes infinite, nor do they classify the intermediate arities between the closure threshold and \(m+n\).

Originality is literature-search based. Because the proof is short once the published algebraic-closure theorem is combined with elementary bipartite enumeration, an unindexed or folklore occurrence remains possible. The exact sequence A047863 and random-bipartite orbit enumeration are explicitly excluded from the novelty claim.

## References
1. Gabriel Conant and Alex Kruckman, *Independence in generic incidence structures*, arXiv:1709.09626; Journal of Symbolic Logic 84 (2019), 750–780, DOI 10.1017/jsl.2019.8. First arXiv submission: 27 September 2017.
2. OEIS Foundation, *A047863: Number of labeled graphs with 2-colored nodes where black nodes are only connected to white nodes and vice versa*.
3. P. J. Cameron, *Sequences realized by oligomorphic permutation groups*, Journal of Integer Sequences 3 (2000), Article 00.1.5.
