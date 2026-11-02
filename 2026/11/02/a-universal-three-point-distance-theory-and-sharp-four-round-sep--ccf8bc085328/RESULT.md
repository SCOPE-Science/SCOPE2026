# A universal three-point distance theory and sharp four-round separation of Hamming, Johnson, and Grassmann schemes

## Finding

Fix an integer \(k\ge2\). Work in the finite relational vocabulary \(L_k=\{R_0,R_1,\ldots,R_k\}\), where \(R_i(x,y)\) means distance \(i\), and \(R_0\) is equality. Let \(H(k,a)\) be the Hamming distance scheme of words of length \(k\) on an alphabet of size \(a\); let \(J(n,k)\) be the Johnson distance scheme of all \(k\)-subsets of an \(n\)-element set, with distance \(k-|A\cap B|\); and let \(G_s(N,k)\) be the Grassmann distance scheme of all \(k\)-subspaces of \(\mathbb F_s^N\), with distance \(k-\dim(U\cap V)\), where \(s\) is a prime power.

**Theorem.** For all \(a\ge3\), \(n\ge3k\), prime powers \(s\ge2\), and \(N\ge2k\), these three structures agree on every first-order sentence of quantifier rank at most three:

\[H(k,a)\equiv_3 J(n,k)\equiv_3 G_s(N,k).\]

The thresholds \(a\ge3\), \(n\ge3k\), \(N\ge2k\) are individually sharp for this common three-round theory. Yet the rank-three agreement is optimal: for every such choice of parameters, \(H(k,a)\) is **not** rank-four equivalent to either \(J(n,k)\) or \(G_s(N,k)\).

The essential structural conclusion is that, in all three families, an ordered triple of vertices with pairwise distances \((u,v,w)\) exists if and only if the integers lie in \([0,k]\) and satisfy the triangle inequalities. In particular, their three-point metric spectra agree even though their graph-theoretic local neighborhoods already have different four-point configurations.

## Assumptions and scope

All quantifiers range over vertices (words, subsets, or subspaces), not over ambient coordinates. All distance relations, not merely adjacency \(R_1\), are individually named. The language depends on the fixed diameter \(k\); the theorem compares structures using the same \(L_k\). A first-order sentence has quantifier rank equal to its maximum quantifier-nesting depth. Repeated chosen vertices are permitted in the Ehrenfeucht–Fraïssé game. No claim is made about rank-four equivalence between Johnson and Grassmann schemes, or about other languages or values \(k=1\).

## Proof

**Lemma 1 (all metric triangles occur in a ternary Hamming cube).** Let \(0\le u,v,w\le k\) be integers satisfying the triangle inequalities. Set \(S=u+v+w\) and
\[t=\begin{cases}S\bmod 2,&S\le2k,\\S-2k,&S>2k.\end{cases}\]
Put \(b=(v+w-u-t)/2\), \(c=(u+w-v-t)/2\), \(d=(u+v-w-t)/2\), and \(h=k-t-b-c-d\). All five counts are nonnegative integers. Indeed, parity is automatic. If \(S\le2k\), an odd \(S\) makes each of the three nonnegative triangle slacks odd and hence at least one; if \(S>2k\), the upper bound for \(t\) by every triangle slack follows from \(u,v,w\le k\). In either case \(t+b+c+d\le k\).

Use \(t\) coordinates where three words have three distinct symbols; \(b\) where the first two agree, \(c\) where the first and third agree, \(d\) where the second and third agree, and \(h\) where all agree. The resulting distances are precisely \(u,v,w\). Necessity of these inequalities is the metric triangle inequality.

**Lemma 2 (a common explicit isometric skeleton).** The ternary Hamming space \(H(k,3)\) embeds isometrically into \(J(3k,k)\): split a \(3k\)-element ground set into \(k\) labeled triples, and select in block \(i\) the single symbol prescribed by coordinate \(i\). The intersection size of the resulting \(k\)-sets equals the number of matching coordinates.

It also embeds isometrically into \(G_s(2k,k)\) for every finite field size \(s\ge2\). Split the vector space into \(k\) mutually independent two-dimensional summands. Choose three distinct one-dimensional subspaces in each summand (possible because a projective line over \(\mathbb F_s\) has \(s+1\ge3\) points). Map a word to the direct sum of its \(k\) chosen lines. Two resulting \(k\)-subspaces intersect in precisely the common-coordinate lines. These embeddings extend to all larger ambient set sizes or dimensions by unused coordinates. Both Johnson and Grassmann distances are metrics bounded by \(k\); Lemma 1 and these embeddings therefore prove identical three-point distance spectra for all three families.

**Lemma 3 (three-round back-and-forth).** After one move, all three schemes have the same unary atomic type. After two moves, the chosen ordered pair is classified atomically by its unique distance \(i\in\{0,\ldots,k\}\), and every distance occurs in all three schemes. After the third move, the existence of a vertex having any prescribed two distances to the chosen pair depends only on the feasibility of the associated metric triangle, established in Lemmas 1–2. Therefore Duplicator can maintain the complete atomic diagram through all three moves, including equality, and the Ehrenfeucht–Fraïssé criterion yields the claimed \(\equiv_3\) equivalences.

**Sharp parameter boundaries.** A binary Hamming space cannot contain three vertices that are pairwise at distance one: the unique changed coordinate of an adjacent pair cannot yield a third distinct binary letter. All target Johnson and Grassmann schemes contain such a triple by the common ternary skeleton. Thus the alphabet bound is exact. If \(n<3k\), three pairwise disjoint \(k\)-sets cannot exist, whereas the common metric triangle \((k,k,k)\) exists in \(H(k,3)\), so the Johnson bound is exact. If \(N<2k\), any two \(k\)-subspaces meet nontrivially, so \(R_k\) is empty while it occurs in \(H(k,3)\); this is already visible in two rounds. These arguments also cover shorter distances becoming unavailable below the respective thresholds.

**Rank-four separator.** The four-variable existential sentence
\[\begin{aligned}
\Diamond:=\exists x\,\exists y\,\exists z\,\exists w\;(&R_1(x,y)\wedge R_1(x,z)\wedge R_1(y,z)\\
&\wedge R_1(x,w)\wedge R_1(y,w)\wedge R_2(z,w))
\end{aligned}\]
has quantifier rank four. It asserts that adjacent vertices have two common neighbors at distance two (an induced diamond). In a Hamming graph, two adjacent vertices differ at exactly one coordinate, and every common neighbor differs from them only at that same coordinate; hence their common neighbors are pairwise adjacent, so \(\Diamond\) fails.

In a Johnson scheme, let \(B\) be any fixed \((k-2)\)-set, disjoint from four symbols \(1,2,3,4\). The four sets \(B\cup\{1,2\}\), \(B\cup\{1,3\}\), \(B\cup\{1,4\}\), \(B\cup\{2,3\}\) satisfy \(\Diamond\). In a Grassmann scheme choose a fixed \((k-2)\)-space \(B\) and independent directions \(e_1,e_2,e_3,e_4\) modulo \(B\); use the four \(k\)-spaces \(B+\langle e_1,e_2\rangle\), \(B+\langle e_1,e_3\rangle\), \(B+\langle e_1,e_4\rangle\), \(B+\langle e_2,e_3\rangle\). Here the first five pair-distances in lexicographic order are one, and the last is two. The ambient requirements hold when \(k\ge2\) and \(n\ge3k\), \(N\ge2k\). Thus \(\Diamond\) separates Hamming from either other family at rank four, proving sharpness of the logical depth.

## Verification

Run `python3 verify_universal_triangle.py` without dependencies. The program constructs all feasible integer triangles up to \(k=7\), verifies their ternary Hamming witnesses and both isometric embeddings, independently enumerates ternary Hamming and Johnson triple-distance supports for \(k=2,3\), and checks the exact four-point diamond in Johnson and binary Grassmann coordinates for \(2\le k\le7\). Its reproducible output is supplied as `verification_output.txt`. Finite tests support, but do not replace, the general proofs above.

## Relationship to prior work

Association schemes organize distance-regular structures via their intersection numbers, including the positivity/vanishing pattern for three-point configurations. Kurihara's *Character tables of association schemes based on attenuated spaces* (arXiv:1101.3455, first publicly posted 2011-01-18), §§1–2, treats Grassmann schemes and more general schemes, primarily calculating character tables; it does not state a cross-family first-order three-round equivalence or the exact four-round separator. Kivva's *A characterization of Johnson and Hamming graphs and proof of Babai's conjecture* (arXiv:1912.11427, 2019), §§1 and 2.4, studies characterization by spectral and local-graph conditions, rather than bounded-rank equivalence in the complete distance language. Terwilliger (1987) introduces intersection diagrams and positivity of intersection numbers. The present argument turns the shared positivity criterion into a three-round logical comparison, establishes three simultaneous sharp size conditions through constructive embeddings, and identifies the next-round obstruction by an explicit four-point motif. Standard intersection-number formulas may imply individual feasibility statements by separate calculations; the present theorem does not claim to originate the metric or association-scheme definitions.

## Limitations

The result does not classify four-round Johnson-versus-Grassmann equivalence, nor does it claim independent mathematical certification or exhaustive priority. Previously unindexed descriptions of the same three-point coincidence may exist. The proof uses a distance-coloured relational language: forgetting colours, changing the vocabulary, or introducing function symbols changes the expressive-power problem.

## References

1. H. Kurihara, *Character tables of association schemes based on attenuated spaces*, arXiv:1101.3455v1 (2011-01-18), https://arxiv.org/abs/1101.3455. Sections 1–2, accessible full HTML version https://arxiv.org/html/1101.3455v2.
2. B. Kivva, *A characterization of Johnson and Hamming graphs and proof of Babai's conjecture*, arXiv:1912.11427v1 (2019-12-24), https://arxiv.org/html/1912.11427v1, especially Sections 1 and 2.
3. P. Terwilliger, *A characterization of P- and Q-polynomial association schemes*, Journal of Combinatorial Theory Series A 45 (1987), 8–26, DOI:10.1016/0097-3165(87)90042-2. Comparison limited to publicly available abstract and metadata.
