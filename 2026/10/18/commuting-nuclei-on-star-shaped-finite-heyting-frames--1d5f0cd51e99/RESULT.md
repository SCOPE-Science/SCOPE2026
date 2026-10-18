# Commuting nuclei on star-shaped finite Heyting frames

## Finding

For every integer \(n\geq 1\), let \(P_n=\{r\}\sqcup L\) be the finite poset with \(|L|=n\), \(r<\ell\) for all \(\ell\in L\), and no distinct comparable points in \(L\). Its upset lattice \(H_n=\operatorname{Up}(P_n)=2^L\cup\{P_n\}\) is an \((2^n+1)\)-element finite Heyting algebra. A *nucleus* is an extensive, monotone, idempotent, binary-meet-preserving endomap of \(H_n\). Two nuclei *commute* when their two compositions coincide pointwise.

**Classification and spectrum.** Every nucleus has a unique form \(J_{a,A}\), with \(a\in\{0,1\}\) and \(A\subseteq L\), described below. Two such nuclei \(J_{a,A}\) and \(J_{b,B}\) commute exactly when \(a=b\), or \(a=0,b=1,A\subseteq B\), or \(a=1,b=0,B\subseteq A\). All maximal (by inclusion) families of mutually commuting nuclei are
\[
\mathcal F_I=\{J_{0,A}:A\subseteq I\}\;\cup\;\{J_{1,B}:I\subseteq B\subseteq L\},\qquad I\subseteq L.
\]
There are precisely \(2^n\) such families; \(|\mathcal F_I|=2^{|I|}+2^{n-|I|}\). For each integer \(k\geq0\), the number of ordered \(k\)-tuples of pairwise-commuting nuclei (repetitions allowed) is exactly
\[
T_n(k)=\sum_{h=0}^{k}\binom{k}{h}\bigl(2^h+2^{k-h}-1\bigr)^n.
\]
In particular, \(T_n(2)=2\cdot 4^n+2\cdot3^n\), and two independent uniformly chosen nuclei commute with probability
\[
\frac{T_n(2)}{(2^{n+1})^2}=\frac12+\frac12\left(\frac34\right)^n\longrightarrow\frac12.
\]
These are assertions about nuclei on the non-chain Heyting algebras \(H_n\), not about arbitrary monotone closure operators or all finite posets.

## Assumptions and scope

The labels of the \(n\) leaves are fixed. The lattice elements are precisely the arbitrary subsets \(U\subseteq L\) and the additional top upset \(P_n\), containing the root. Meet is set intersection. The Heyting implication is the usual upset implication, although only meet preservation is required of a nucleus. Define \(J_{0,A}(P_n)=J_{1,A}(P_n)=P_n\). For \(U\subseteq L\), put
\[
J_{0,A}(U)=\begin{cases}P_n,&A\subseteq U,\\U\cup(L\setminus A),&A\not\subseteq U,\end{cases}
\qquad
J_{1,A}(U)=U\cup(L\setminus A).
\]
Equivalently, with \(S=A\) for \(a=0\) and \(S=A\cup\{r\}\) for \(a=1\), these are the subset-generated nuclei
\[
J_{a,A}(U)=\{x\in P_n:S\cap\uparrow x\subseteq U\}.
\]
The case \(n=1\) is a three-element chain. For \(n\ge2\), \(H_n\) is nondiscrete, distributive, and not a chain.

## Proof

**1. Exhaustiveness of the normal form.** Fix any nucleus \(j\) on \(H_n\). Let \(A=\{\ell\in L:\ell\notin j(\varnothing)\}\). For each leaf \(\ell\) and leaf subset \(U\subseteq L\), if \(\ell\notin A\), monotonicity forces \(\ell\in j(U)\). If \(\ell\in U\), extensivity forces \(\ell\in j(U)\). Conversely, if \(\ell\in A\setminus U\), then \(U\cap\{\ell\}=\varnothing\); as \(\ell\in j(\{\ell\})\) and \(j\) preserves intersections, \(\ell\in j(U)\) would force \(\ell\in j(\varnothing)\), a contradiction. Thus the leaf part of \(j(U)\) is always \(U\cup(L\setminus A)\).

The set \(F=\{U\in H_n:r\in j(U)\}\) is a nonempty filter of the finite meet-semilattice \(H_n\): it contains \(P_n\), is upward closed, and is closed under finite meets. Hence \(F\) has a unique least element \(W\) and consists of exactly the upsets containing \(W\). If \(W=P_n\), the root is added only to \(P_n\), giving \(J_{1,A}\). Otherwise \(W=K\subseteq L\). Because \(j(K)\) contains the root, it equals \(P_n\); the leaf formula then forces \(A\subseteq K\). If \(A\subsetneq K\), the proper upset \(A\) satisfies \(j(A)=L\) (root absent, all leaves present), but \(j(j(A))=j(L)=P_n\), contradicting idempotence. Thus \(K=A\), yielding \(J_{0,A}\). The leaf membership rule determines \(A\), and whether \(W=P_n\) determines \(a\), so the representation is unique. Conversely the subset formula directly preserves intersections, is extensive and monotone, and is idempotent because it leaves membership on \(S\) unchanged; every displayed map is a nucleus. This proves there are exactly \(2^{n+1}\) nuclei.

**2. Commutation.** Apply an outer \(J_{a,A}\) after an inner \(J_{b,B}\). For every leaf-subset input \(U\subseteq L\), both composition orders have leaf component \(U\cup(L\setminus(A\cap B))\). In the four ordered flag cases \((a,b)=(0,0),(0,1),(1,0),(1,1)\), respectively, the first composition contains the root exactly under the conditions
\[
A\cap B\subseteq U,\qquad A\cap B\subseteq U,\qquad B\subseteq U,\qquad\text{never}.
\]
The reversed composition interchanges \((a,A)\) and \((b,B)\). Identical flags therefore always commute. In the mixed case \(a=0,b=1\), equality for every input \(U\subseteq L\) is equivalent to equality of the principal inclusion tests \(A\cap B\subseteq U\) and \(A\subseteq U\), which holds exactly when \(A\subseteq B\). The other mixed case is symmetric. Both maps fix \(P_n\), so this proves the claimed iff for all inputs.

**3. Maximal families.** A commuting family contains some of each flag in any maximal instance: otherwise all maps of its existing flag could be inserted, after which a map of the opposite flag also commutes (\(J_{0,\varnothing}\) or \(J_{1,L}\)). For a maximal family let \(\mathcal A\) denote its flag-zero leaf sets and \(\mathcal B\) its flag-one sets. The mixed criterion says \(A\subseteq B\) for every \(A\in\mathcal A\), \(B\in\mathcal B\). Put \(I=\bigcap_{B\in\mathcal B}B\). Maximality forces \(\mathcal A=2^I\), since any omitted subset of \(I\) could be inserted. Its union is \(I\); maximality then forces \(\mathcal B=\{B:I\subseteq B\subseteq L\}\). Conversely this is pairwise commuting and every omitted flag-zero map fails to commute with \(J_{1,I}\), while every omitted flag-one map fails to commute with \(J_{0,I}\). Distinct \(I\)'s give distinct families. Counting their two disjoint layers gives the stated cardinality.

**4. Ordered tuples.** Fix an ordered flag pattern with \(h\) flag-zero entries and \(k-h\) flag-one entries. For each leaf \(\ell\), compatibility prohibits simultaneously a flag-zero set containing \(\ell\) and a flag-one set omitting \(\ell\). Thus either all flag-zero sets omit \(\ell\) (\(2^{k-h}\) choices), or all flag-one sets contain \(\ell\) (\(2^h\) choices), with one assignment counted twice. There are \(2^{k-h}+2^h-1\) choices per leaf, independent across the \(n\) leaves. There are \(\binom{k}{h}\) flag patterns. Summing proves the tuple formula, including \(k=0\). At \(k=2\), simplification yields the pair count and probability.

## Verification

Run `python3 verify.py` with the standard library. The program constructs all maps from the pointwise subset rule (separately from the displayed case formula); verifies extensivity, idempotence, binary-meet preservation, and every pairwise composition for \(1\le n\le4\); compares the commutation predicate with the theorem; enumerates maximal cliques of the commutation graph independently for \(1\le n\le4\); and enumerates pairwise-compatible ordered tuples for \(1\le n\le3\), \(0\le k\le3\). It also exhaustively enumerates *all* self-maps satisfying the nucleus axioms on the complete small lattices for \(n=1,2\), independently confirming completeness there. Its terminal marker is `VERIFY_OK`. These finite checks corroborate the formulas but do not establish the universal quantifiers; the proof above does that.

## Relationship to prior work

Lindenhovius established that nuclei on the downset lattice of an Artinian poset are parametrized by subsets, using Heyting implication. Ochs provided an explicit nucleus-to-subset inverse formula. The corresponding parameterization here, after reversing order, is credited to that work. The present result concerns the *composition compatibility relation* among those nuclei, all maximal commuting families, and the exact full ordered-tuple spectrum on root-star frames. These latter statements are not stated in either inspected source. They do not follow from counting nuclei alone: the root flag produces a nontrivial mixed-layer inclusion obstruction. The \(n=1\) special case is a chain, while the non-chain star lattices with \(n\ge2\) require the mixed-layer subset criterion. General frame-nucleus and Grothendieck-topology results provide context but no identified exact star-family count.

## Limitations

The classification assumes an exact rooted-star order with incomparable leaves, finite \(n\), and meet-preserving idempotent closure operators. It does not count commuting arbitrary closure operators, classify all finite Heyting algebras, or make claims for arbitrary forked or infinite posets. The cited finite-poset parametrization itself is earlier work. Searches cannot certify worldwide novelty, especially against uncatalogued semigroup or locale-theoretic equivalent statements. The conclusions are mathematical assertions supported by the included proof and finite checks.

## References

1. Eduardo Ochs, *On a formula that is not in “Grothendieck Topologies in Posets”*, arXiv:2107.08501v1, publicly submitted 18 July 2021, https://arxiv.org/abs/2107.08501 . Section on the explicit inverse of the nucleus/subset bijection.
2. A. J. Lindenhovius, *Grothendieck topologies on a poset*, arXiv:1405.4408v2 (originally 17 May 2014), https://arxiv.org/abs/1405.4408 . Appendix B and Theorem C.4 on nuclei and subset Grothendieck topologies for Artinian posets.
