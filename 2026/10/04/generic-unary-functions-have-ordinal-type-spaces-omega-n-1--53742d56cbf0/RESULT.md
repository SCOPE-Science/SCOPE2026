# Generic unary functions have ordinal type spaces \(\omega^n+1\)

## Finding

Let \(L=\{f\}\) consist of one unary function symbol, and let
\[
T=EC_L
\]
be the model completion of the empty \(L\)-theory. Jeřábek proves that \(EC_L\) eliminates quantifiers, is complete when there are no nullary symbols, is totally transcendental in the one-unary-function case, and has countably many complete \(n\)-types for every finite \(n>0\).

For \(p\in S_n(T)\), consider the directed graph whose vertices are the \(p\)-equivalence classes of the unary terms
\[
f^m(x_i)\qquad(1\le i\le n,\ m<\omega),
\]
with the edge \([t]\to[f(t)]\). Let \(\rho(p)\) be the number of infinite connected components of this graph. Because there are only \(n\) roots, every infinite component contains one eventual forward ray, so \(0\le \rho(p)\le n\).

The exact Cantor--Bendixson stratification is
\[
\boxed{
S_n(T)^{(k)}
=
\{p\in S_n(T):\rho(p)\ge k\}
\qquad(0\le k\le n).
}
\]
Consequently,
\[
\boxed{\operatorname{CB}(p)=\rho(p).}
\]
There is a unique type of rank \(n\), namely
\[
p_{\mathrm{gen}}(x_1,\ldots,x_n)
=
\{f^a(x_i)\ne f^b(x_j):
(i,a)\ne(j,b)\}.
\]
Thus
\[
S_n(T)^{(n)}=\{p_{\mathrm{gen}}\},
\qquad
S_n(T)^{(n+1)}=\varnothing.
\]

Using the elementary classification of countable compact metrizable spaces of finite Cantor--Bendixson height with one top-rank point (a short induction is recalled below), this gives the explicit homeomorphism type
\[
\boxed{S_n(T)\cong\omega^n+1\qquad(n\ge1).}
\]

In particular,
\[
S_1(T)\cong\omega+1,\qquad
S_2(T)\cong\omega^2+1,\qquad
S_3(T)\cong\omega^3+1.
\]
Jeřábek's prior result gives only the cardinal statement \(|S_n(T)|=\aleph_0\); the retained contribution is the full derivative stratification and resulting ordinal topology.

## Assumptions and scope

The type spaces are over the empty set and consist of real finite tuples. The language has exactly one unary function and no constants or relation symbols. Types over nonempty parameter sets are not treated here: even a finite parameter set generates an infinite definable forward orbit, so the same invariant requires an additional relative term-graph analysis.

All Cantor--Bendixson derivatives are taken in the usual Stone topology. The argument uses quantifier elimination for \(EC_L\), not any special presentation of a countable model.

## Proof

Jeřábek's Theorem 3.7 says that \(EC_L\) eliminates quantifiers and that every \(L\)-structure embeds into a model of \(EC_L\). Corollary B.3 makes \(EC_L\) complete when \(L\) has no nullary symbols. Hence a complete \(n\)-type over the empty set is exactly a complete equality diagram of the terms \(f^m(x_i)\), subject only to the congruence rule
\[
t=s\Longrightarrow f(t)=f(s).
\]
Any such coherent term diagram is realized in some unary-function structure and therefore in a model of \(T\).

Write
\[
X_k=\{p\in S_n(T):\rho(p)\ge k\}.
\]
We prove by induction that \(S_n(T)^{(k)}=X_k\).

For \(k=0\) this is tautological. Assume \(S_n(T)^{(k)}=X_k\).

First suppose \(\rho(p)=k\). Every finite component of the term graph is eventually periodic and is therefore completely described by finitely many equalities and inequalities. In each infinite component, finitely many rooted forward paths eventually merge into one ray. Choose a finite depth \(N\) beyond all those mergers and beyond complete descriptions of all finite components. Let \(U\) be the basic clopen neighborhood recording the equality pattern of all terms through depth \(N\), together with the equalities that close the finite components.

If \(q\in U\) and \(q\ne p\), let an equality not belonging to \(p\) occur at the earliest possible depth beyond the recorded part. All equalities already present in \(p\) beyond depth \(N\) are forced by the mergers and cycles recorded in \(U\), so a difference really must first appear by adding such an equality. It has one of three forms: an infinite ray meets itself and creates a cycle, two previously distinct infinite rays merge, or an infinite ray meets one of the already recorded finite components. Every case lowers the number of infinite components. Thus
\[
q\ne p,\ q\in U\quad\Longrightarrow\quad \rho(q)<k,
\]
so \(U\cap X_k=\{p\}\). Hence every \(p\) with \(\rho(p)=k\) is isolated in the \(k\)-th derivative.

Now suppose \(\rho(p)>k\), and let \(U\) be any basic neighborhood of \(p\). Only finitely many terms occur in the formulas defining \(U\), so choose one infinite ray and a depth \(M\) strictly beyond all mentioned iterates. Modify the term diagram by imposing, farther out,
\[
f^{M+r}(x_i)=f^M(x_i)
\]
for some \(r>0\), with all earlier terms left unchanged. This closes exactly that ray into a cycle, produces a coherent unary-function term diagram, and hence extends to a complete type \(q\in S_n(T)\). We have
\[
q\in U,\qquad q\ne p,\qquad \rho(q)=\rho(p)-1\ge k.
\]
Therefore \(p\) is a limit point of \(X_k\).

We have shown that the isolated points of \(X_k\) are exactly the types with \(\rho=k\), and therefore
\[
X_k'=X_{k+1}.
\]
The induction proves the boxed derivative formula.

Since at most \(n\) infinite components can occur, \(S_n(T)^{(n+1)}=\varnothing\). If \(\rho(p)=n\), no two variable orbits can merge and no orbit can cycle, so every term \(f^a(x_i)\) is distinct from every other term. This specifies exactly one complete type, giving \(|S_n(T)^{(n)}|=1\).

Jeřábek's Proposition B.2 gives \(|S_n(T)|=\aleph_0\). A Stone space of a countable theory is compact metrizable. For completeness, the finite-rank classification needed here can be proved by induction: a countable compact metrizable scattered space whose \(n\)-th derivative is one point and whose \((n+1)\)-st derivative is empty decomposes into a sequence of clopen pieces of derivative height at most \(n\) converging to the unique top point; infinitely many pieces have top height \(n\), and the induction hypothesis identifies those pieces with copies of \(\omega^{n-1}+1\). Absorbing the lower-height pieces and taking the one-point compactification gives
\[
(\omega^{n-1}+1)\cdot\omega+1\cong\omega^n+1.
\]
This proves the stated homeomorphism.

## Verification

The proof is structural rather than numerical. The bundled checker replays the local mechanism used in the induction on a bounded exhaustive family of canonical unary term diagrams. It verifies that closing any chosen free ray strictly beyond an observed prefix preserves the complete equality pattern on that prefix and decreases the number of infinite components by exactly one. It also verifies directly that finite eventually periodic one-variable diagrams are isolated by a finite term diagram.

The recorded run ends with `VERIFY_OK`. These finite checks only guard the term-diagram mechanics; the infinite derivative theorem is established by the proof above.

## Relationship to prior work

Kruckman and Ramsey study the generic \(L\)-structure, explicitly identifying it as the model companion of the empty theory in an arbitrary language. Their paper supplies a modern general context for generic function structures but does not state the present unary Stone-space topology.

Jeřábek gives the decisive unary facts used here. Theorem 3.7 proves quantifier elimination and the model-completion property. Theorem B.1 says that one unary function is exactly one of the totally transcendental cases. Proposition B.2 proves that there are \(\aleph_0\) complete \(n\)-types for each \(0<n<\omega\), and exhibits infinitely many eventually periodic 1-types. None of the inspected passages determines the Cantor--Bendixson derivatives, the rank of an individual type from its forward-orbit graph, or the ordinal homeomorphism \(S_n(T)\cong\omega^n+1\).

Targeted published-finding corpus and web searches under “generic unary function,” “existentially closed unary function,” “Cantor--Bendixson,” “Morley rank,” “complete \(n\)-types,” and the exact ordinal fingerprint \(\omega^n+1\) did not locate an equivalent statement. The nearest published-finding corpus item concerns equality-modal semantics of arbitrary functions rather than first-order type-space topology.

## Limitations

The result is restricted to the empty-parameter type spaces of the single-unary-function model completion. It does not classify types over finite or infinite parameter sets, and it does not treat languages with a second unary function or with additional unary predicates, where Jeřábek's stability classification changes sharply.

The originality risk is not zero. Unary-function theories are classical objects, and an equivalent computation might exist in older stability-theory literature phrased as Morley rank, Cantor--Bendixson degree, or functional-digraph rank rather than as a Stone-space homeomorphism. The searches performed in this run found no such source, so the result is retained with that folklore risk explicitly recorded.

## References

1. Alex Kruckman and Nicholas Ramsey, *Generic expansion and Skolemization in NSOP\(_1\) theories*, arXiv:1706.06616; Annals of Pure and Applied Logic 169 (2018), 755--774.
2. Emil Jeřábek, *Recursive functions and existentially closed structures*, arXiv:1710.09864; Journal of Mathematical Logic 20 (2020), article 2050002.
