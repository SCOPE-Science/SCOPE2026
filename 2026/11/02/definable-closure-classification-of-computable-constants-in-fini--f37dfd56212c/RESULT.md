# Definable-closure classification of computable constants in finite randomizations

## Finding
Let \(M\) be a nonempty finite structure in a finite relational signature, and let \(R(M)\) be its two-sorted Borel randomization on the unit interval. For any computable presentation \(Q\) of \(R(M)\), let
\[
C(Q)=\{a\in M:\text{the externally specified constant random variable }\bar a\text{ is a }Q\text{-computable point}\}.
\]
The **exact attainable family** is
\[
\boxed{\{C(Q):Q\text{ is computable}\}
=\{S\subseteq M:\operatorname{dcl}_M(S)=S\}
=\{\operatorname{Fix}(H):H\leq\operatorname{Aut}(M)\}.}
\]
Here \(\operatorname{dcl}_M\) denotes ordinary first-order definable closure, \(\operatorname{Fix}(H)\) the common fixed elements of a subgroup, and \(\operatorname{Aut}(M)\) the finite automorphism group. Every displayed subset can be attained by transporting the **standard computable presentation along a fiberwise automorphism** of \(R(M)\); the resulting presentation is computably isomorphic to the standard one. Thus the spectrum concerns which *externally distinguished constants* are computable, not computable-isomorphism types.

For an empty-signature set of size \(q\geq2\), the possible sizes are exactly
\[
\boxed{\{0,1,\ldots,q-2,q\}.}
\]
In particular exactly \(q-1\) computable constants are impossible. In the finite case every constant is computable precisely when the presentation is aware, so all computable presentations of \(R(M)\) are aware if and only if \(M\) is rigid.

## Assumptions and scope
Fix a nonempty finite universe \(M\) and a finite relational language. Finite structures are effectively decidable by their tables. Random variables are Borel functions \(f:[0,1)\to M\), identified modulo almost-everywhere equality. Their metric is \(d(f,g)=\mu\{t:f(t)\neq g(t)\}\). The event sort is the Lebesgue probability algebra. For every ordinary formula \(\varphi\) the randomization includes its formula-event operation \(\llbracket\varphi\rrbracket\). A computable presentation has a computable dense sequence of named random-variable points, uniformly computable metric and formula-event data, and a computable dense event presentation. An element is computable if its metric distance to the named points can be approximated arbitrarily well by an algorithm. The original constant random variables \(\bar a\) are fixed externally and are **not** added to the presentation language as named constants. Awareness has its established meaning as computable enumerability of the finite closed set of these constants.

The statement is about all presentations of this particular completed randomization, and not about arbitrary randomizations of infinite structures or uniformly recovering an arbitrary unknown finite model. No assertion of computability of the transporting automorphism *relative to the fixed standard presentation* is made.

## Proof
**Step 1: necessary closure under definability.** Suppose \(S=C(Q)\), and let \(a\in\operatorname{dcl}_M(S)\). Then a finite tuple \(\vec s\) from \(S\) and an ordinary formula \(\varphi(x,\vec s)\) uniquely define \(a\) in \(M\). Since every \(\bar s\) in this tuple is \(Q\)-computable, the real quantity \(\mu\llbracket\varphi(f,\overline{\vec s})\rrbracket\) is uniformly computable for each named point \(f\). Uniqueness gives the exact identity
\[
\mu\llbracket\varphi(f,\overline{\vec s})\rrbracket
=\mu\{t:f(t)=a\}=1-d(f,\bar a).
\]
For each positive rational \(\epsilon\), search the dense named sequence until the computably approximable left side is certified strictly larger than \(1-\epsilon\). This search terminates by density, and the selected point lies at distance less than \(\epsilon\) from \(\bar a\). Therefore \(a\in C(Q)=S\). Since \(S\subseteq\operatorname{dcl}_M(S)\), it follows that \(S\) is definably closed. The algorithm is permitted to have a different finite formula and tuple of computable parameter names for each fixed \(a\); the theorem asserts individual point computability, not a uniform operator taking arbitrary elements of \(M\) as input.

**Step 2: finite definable closure is a group fixed set.** Put \(G_S=\{g\in\operatorname{Aut}(M):g(s)=s\text{ for all }s\in S\}\). Each definable element is fixed by every member of \(G_S\). Conversely, a singleton orbit under \(G_S\) is definable over \(S\): write the finite atomic diagram of an enumeration of \(M\), assert that its entries are distinct and exhaust the universe, identify the entries that name the finitely many parameters from \(S\), and existentially quantify all entries except the distinguished one. The satisfying distinguished elements are exactly its \(G_S\)-orbit. If that orbit is a singleton, the formula uniquely defines it. Consequently
\[
\operatorname{dcl}_M(S)=\operatorname{Fix}(G_S).
\]
Furthermore \(S=\operatorname{Fix}(H)\) for some subgroup \(H\leq\operatorname{Aut}(M)\) implies \(H\leq G_S\) and hence \(\operatorname{Fix}(G_S)\subseteq\operatorname{Fix}(H)=S\), so these two characterizations of closed subsets coincide.

**Step 3: realize every closed subset.** Fix \(S=\operatorname{dcl}_M(S)\). Begin with the standard presentation \(P\) whose random-variable names are rational-interval simple functions \([0,1)\to M\), and whose event names are finite unions of rational intervals. This is computable, since first-order truth in the finite structure and rational lengths are decidable; every original \(\bar a\) is a special point. Enumerate the nonidentity members \(g_1,\ldots,g_t\) of \(G_S\). If \(t=0\), then \(S=M\), and \(Q=P\) suffices.

For \(t>0\), choose pairwise disjoint rational half-open intervals \(I_1,\ldots,I_t\) of strictly positive rational lengths. Fix any **noncomputable** real \(\alpha\in(0,1)\). Inside each \(I_j\), let \(A_j\) be the initial half-open subinterval of length \(\alpha\mu(I_j)\). It is Borel with noncomputable measure. Define the measurable, pointwise automorphism \(h_u\in\operatorname{Aut}(M)\) to equal \(g_j\) for \(u\in A_j\) and the identity otherwise. The map
\[
(\Theta f)(u)=h_u(f(u))
\]
is an automorphism of the random-variable sort; it fixes every formula event pointwise and acts as identity on the probability algebra, since the automorphisms preserve all ordinary formulas. Transport all random-variable special names of \(P\) by \(\Theta\), leaving the event names unchanged, to form \(Q\). All named metric and predicate values are *exactly the same computable values* as for \(P\), and the name-preserving correspondence \(P\to Q\) and its inverse are computable isomorphisms.

If \(a\in S\), every \(g_j\) fixes \(a\), so \(\Theta^{-1}(\bar a)=\bar a\), and \(\bar a\) is \(Q\)-computable. If \(a\notin S\), choose \(j\) with \(g_j(a)\neq a\), and put \(b=g_j^{-1}(a)\neq a\). The standard-coordinate preimage \(f=\Theta^{-1}(\bar a)\) equals \(b\) exactly on \(A_j\) *within* \(I_j\), and equals \(a\) elsewhere in \(I_j\). Were \(f\) a \(P\)-computable point, the event \(I_j\cap\llbracket f=\bar b\rrbracket=A_j\) would have computable measure: the two random variables \(f,\bar b\) and the rational interval event \(I_j\) are all \(P\)-computable, and their formula event and intersection have effectively computable measures. This would compute \(\alpha=\mu(A_j)/\mu(I_j)\), a contradiction. Hence \(\bar a\) is not \(Q\)-computable, and \(C(Q)=S\).

**Step 4: pure-set cardinalities and awareness.** For a pure set of size \(q\), the pointwise stabilizer of \(S\) permutes its \(q-|S|\) omitted elements. If at least two are omitted it fixes precisely \(S\); if at most one is omitted it fixes all elements. This gives the cardinality spectrum in the finding (the singleton case has spectrum \(\{1\}\)). For any finite \(M\), finitely many individually computable constants can be assembled into a uniformly computable list, so awareness is equivalent to \(C(Q)=M\). If \(\operatorname{Aut}(M)\) is trivial, \(\operatorname{dcl}_M(\varnothing)=M\), forcing every \(C(Q)=M\). If it is nontrivial, the closed proper set \(\operatorname{Fix}(\operatorname{Aut}(M))\) is realizable and yields a nonaware presentation. This proves the final assertion.

## Verification
The accompanying standalone `checker.py` tests the finite-group identities on all pure sets with one through six elements, all 530 labelled directed binary relations on at most three vertices, and all 64 simple graphs on four vertices. It also tests finite event-partition consistency on 490 configurations. It prints `ALL_CHECKS_OK pure_sizes=1..6 directed_binary_models=530 undirected_4_models=64 finite_event_instances=490`. These computations check finite algebraic subclaims only. The completeness of the spectrum and the noncomputability argument follow from Steps 1–4 and are **not** consequences of the finite tests.

## Relationship to prior work
Zhao (2026, arXiv:2610.30569v1), especially Theorem 1.3 and Section 3, already constructs a transported nonaware presentation of the randomization of the two-element pure set in which **neither** constant is computable. That example is prior coverage, not a new special case. Section 4 treats a countably infinite pure set with a different individual-versus-uniform computability phenomenon. Cuervo Ovalle and Goldbring (2025, arXiv:2506.06187) introduce awareness, computability conventions, and criteria for effective recognizability; those results provide conceptual groundwork rather than the exact finite-structure spectrum above. Andrews, Goldbring and Keisler (2013, arXiv:1304.7797v1), in particular Theorem 3.3.6 and the discussion of finite structures in Section 4, describe **model-theoretic definable closure** inside randomized structures, not the attainable sets of **presentation-computable externally named constant random variables**. Their results are consistent with the definability obstruction but do not furnish the effective transported-realization classification. The new assertion is the full Galois-closed family for arbitrary finite structures, including its missing-one-point gap for every pure-set size.

## Limitations
The base structure is finite and given in a finite relational signature. The constructions establish existence, not an effective operator recovering the noncomputable twisting real or the externally distinguished original constants from a transported presentation. The latter absence is essential. The exact finite-structure theorem does not classify computability spectra for infinite structures. The originality assessment is based on inspected papers and semantic database queries, not a formal proof of historical priority; an unlocated equivalent presentation-spectrum classification remains possible. Independent validation has not been performed.

## References
1. Xuanheng Zhao, *Non-Aware Computable Presentations of Randomizations*, arXiv:2610.30569v1 (22 October 2026), https://arxiv.org/html/2610.30569v1 .
2. Nicolás Cuervo Ovalle and Isaac Goldbring, *Computable presentations of randomizations*, arXiv:2506.06187 (6 June 2025), https://arxiv.org/abs/2506.06187 .
3. Uri Andrews, Isaac Goldbring and H. Jerome Keisler, *Definable Closure in Randomizations*, arXiv:1304.7797v1 (29 April 2013), https://arxiv.org/html/1304.7797v1 .
