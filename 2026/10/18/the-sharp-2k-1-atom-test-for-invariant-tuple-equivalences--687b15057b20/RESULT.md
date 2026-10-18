# The sharp \(2k+1\)-atom test for invariant tuple equivalences

## Finding
For each integer \(k\ge2\), an equivalence relation on ordered \(k\)-tuples that is invariant under every renaming of atoms can be verified on just \(2k+1\) atoms. This is the **least possible** uniform test size, including when the full atom universe is infinite.

Precisely, let \(A\) be any set with at least \(2k+1\) elements (finite or infinite), let \(B\subseteq A\) have \(|B|=2k+1\), and let \(R\subseteq A^k\times A^k\) be invariant under \(\operatorname{Sym}(A)\). Then \(R\) is an equivalence on \(A^k\) if and only if \(R\cap(B^k\times B^k)\) is an equivalence on \(B^k\). For each \(k\ge2\) the number \(2k\) fails in place of \(2k+1\).

## Assumptions and scope
A tuple is ordered and may repeat atoms. Invariance means \((u,v)\in R\iff(\pi u,\pi v)\in R\) for every permutation \(\pi\) of the atom set. The test uses *one fixed* \((2k+1)\)-element set; invariance makes its choice irrelevant. No definability assumption or local finiteness of \(R\) is imposed. The result is not asserted for arbitrary groups other than the full symmetric group, for relations with external distinguished parameters, or for arity zero.

## Proof
We prove a finite symmetric-group normal-form lemma first.

**Lemma (small-supported quotient normal form).** Let \(N\ge2k+1\), \(G=\operatorname{Sym}(N)\), and let \(Q\) be a finite \(G\)-set in which each point is fixed by the pointwise stabilizer of some set of at most \(k\) atoms. Then every transitive component of \(Q\) is of the form \(\operatorname{Inj}_t(N)/H\), with \(0\le t\le k\) and \(H\le\mathfrak S_t\). Here \(\operatorname{Inj}_t(N)\) denotes ordered injective \(t\)-tuples, and the right action of \(H\) permutes their positions.

*Proof of the lemma.* Fix \(q\in Q\) and \(K=\operatorname{Stab}_G(q)\). There is \(X\), \(|X|\le k\), with the pointwise stabilizer \(G_{(X)}\subseteq K\). Whenever \(G_{(S)},G_{(T)}\subseteq K\) and \(|S|,|T|\le k\), the complements \(N\setminus S\) and \(N\setminus T\) intersect (because \(N>2k\)). All transpositions inside either complement belong to \(K\); their union is the edge set of a connected graph on \(N\setminus(S\cap T)\). Therefore these transpositions generate its full symmetric group and \(G_{(S\cap T)}\subseteq K\). Intersecting the finitely many such subsets of \(X\) produces a least \(S\subseteq X\) with \(G_{(S)}\subseteq K\).

For any \(g\in K\), conjugation gives \(G_{(gS)}\subseteq K\). The same transposition argument applies to \(S,gS\); hence \(G_{(S\cap gS)}\subseteq K\). Minimality forces \(S\cap gS=S\), so \(gS=S\). Thus every \(g\in K\) preserves \(S\) setwise, while \(K\) contains all permutations fixing \(S\) pointwise. Its induced action on \(S\) is a subgroup \(H\le\mathfrak S_{|S|}\), and \(G/K\cong\operatorname{Inj}_{|S|}(N)/H\), establishing the lemma. This proof also covers \(S=\varnothing\), when \(K=G\).

**Lifting the finite quotient.** Suppose the restriction \(E=R|_{B^k}\) is an equivalence. The quotient \(Q=B^k/E\) is a finite \(\operatorname{Sym}(B)\)-set. The class of a tuple \(u\) is fixed by every permutation fixing the atoms of \(u\) individually; hence the lemma applies. Decompose \(Q\) into its finitely many transitive components. Assign each a distinct label \(c\), and choose its presentation \(\operatorname{Inj}_{t_c}(B)/H_c\), where \(t_c\le k\).

The equivariant quotient map \(q_B:B^k\to Q\) has the following coordinate form on each equality-pattern orbit of \(B^k\): it chooses a fixed list of \(t_c\) **distinct entries** among the entries of its input tuple and returns the list modulo \(H_c\), together with the component label \(c\). To justify this, choose one tuple \(u\) of that equality type, and identify its quotient class with an injective tuple of supporting atoms. These atoms lie among the distinct entries of \(u\) by the lemma; equivariance transports the same coordinate positions to every tuple of that equality type. The ambiguity in the ordering is exactly the prescribed \(H_c\)-action.

The same finite collection of equality-pattern branches, selected input-coordinate positions, labels, and subgroups \(H_c\) defines a map \(q_A:A^k\to\coprod_c\operatorname{Inj}_{t_c}(A)/H_c\). Equality of its outputs is an equivalence relation on \(A^k\). For any two tuples \(u,v\in A^k\), their union of supports has size at most \(2k\), so there is an injective renaming of those atoms into \(B\). Under such a renaming, the equality of the two \(q_A\)-outputs is equivalent to equality of their original \(q_B\)-outputs. Invariance of \(R\) gives the same equivalence for \((u,v)\in R\). Consequently \(R=\ker(q_A)\), proving transitivity as well as symmetry and reflexivity globally. (Alternatively, symmetry and reflexivity follow immediately by transferring pairs from \(A\) to \(B\).)

**Sharpness.** Fix \(k\ge2\). Define \(R\) on tuples over any atom set by making all noninjective tuples singleton classes, and for injective \(u,v\) declaring
\[
 uRv\quad\Longleftrightarrow\quad \operatorname{supp}(u)=\operatorname{supp}(v)\ \text{or}\ \operatorname{supp}(u)\cap\operatorname{supp}(v)=\varnothing.
\]
This relation is invariant. On any exactly \(2k\)-atom carrier, a \(k\)-subset is disjoint from precisely one \(k\)-subset, its complement. Hence the injective tuples form equivalence classes indexed by the unordered complementary pairs of \(k\)-subsets; the noninjective tuples remain singletons. Every smaller restriction is also an equivalence.

On \(2k+1\) atoms, choose \(k\)-sets \(U,V,W\) with \(U\cap V=V\cap W=\varnothing\), but \(0<|U\cap W|<k\): take two disjoint \(k\)-sets \(U,V\), and replace one member of \(U\) with the lone remaining atom to form \(W\). Any injective enumerations \(u,v,w\) satisfy \(uRv\) and \(vRw\), but not \(uRw\). Thus the threshold is sharp. \(\square\)

## Verification
The proof reduces the infinite assertion to a finite group lemma and an explicit quotient presentation. It does not infer an infinite claim from finite enumeration. The group lemma uses only the generation of a symmetric group by transpositions along a connected graph. Every pair of \(k\)-tuples requires at most \(2k\) atoms, explaining why equality of quotient descriptions transfers from the test domain to the full domain. The complementary-support example witnesses optimality for every \(k\ge2\).

## Relationship to prior work
Finite-context semantics supplies the motivation for studying equivariant quotient kernels: the quotient theorem in Ciobanu's 2026 work establishes their natural group action, without giving this sharp finite-test size. Classical nominal-set theory develops least supports and orbit-finite quotients; the small-supported quotient lemma makes those ingredients explicit at a finite uniform carrier size. Standard group-action theory explains why transitive quotients are coset spaces. The contribution assessed here is the uniform necessary-and-sufficient *sharp cutoff* for testing equivariant tuple equivalences, not the general notion of quotient, least support, or coset action.

## Limitations
The novelty of a numerical finite-test cutoff relative to all older equivariant-algebra literature has not been exhaustively established. The result uses the full symmetric group (no nontrivial atom structure); general oligomorphic groups can behave differently. The proof is mathematical rather than machine-certified. The arity-one case has a different cutoff and is excluded.

## References
1. Gabriel Ciobanu, *Finite-Context Semantics in Finitely Supported Structures*, arXiv:2609.31917, first version 25 September 2026, especially §2 and §5.
2. Mikołaj Bojańczyk, Bartek Klin, and Sławomir Lasota, *Nominal Monoids*, Theory of Computing Systems, DOI:10.1007/s00224-013-9464-1, especially §2 and the least-support treatment.
3. Standard symmetric-group facts: transpositions on the edges of a connected graph generate the full symmetric group on its vertices (proved directly above).
