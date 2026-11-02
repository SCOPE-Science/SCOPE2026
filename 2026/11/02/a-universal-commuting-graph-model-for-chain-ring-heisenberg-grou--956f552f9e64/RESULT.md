# A universal commuting-graph model for chain-ring Heisenberg groups and a class-two counterexample

## Finding

Let \(R\) and \(S\) range over finite **commutative chain rings with identity** (nonzero finite local principal-ideal rings). Write \(q_R=|R/\mathfrak m_R|\) and let \(\ell_R\ge1\) be the least integer with \(\mathfrak m_R^{\ell_R}=0\). Form the group \(H(R)=UT_3(R)\), and let \(\Gamma(H(R))\) be the **full simple commuting graph**, with all group elements as vertices and edges joining distinct commuting pairs.

**Classification theorem.** For any two such rings,
\[
\boxed{\Gamma(H(R))\cong\Gamma(H(S))\quad\Longleftrightarrow\quad (q_R,\ell_R)=(q_S,\ell_S).}
\]
In particular the graph is independent of ring characteristic and of the isomorphism type of the additive group. The proof gives an explicit, purely combinatorial model \(\mathcal G_{q,\ell}\) of every graph in the class.

**A class-two non-isoclinism collision.** The two groups
\[
\boxed{UT_3(\mathbb Z/8\mathbb Z)\quad\text{and}\quad UT_3(\mathbb F_2[t]/(t^3))}
\]
have order \(512\), have isomorphic full commuting graphs, and are both nonabelian of nilpotency class exactly two. They are **not isoclinic**: their central quotients are respectively \(C_8^2\) and \(C_2^6\), and their derived subgroups are respectively \(C_8\) and \(C_2^3\). This supplies a counterexample to the general class-two isoclinism question posed in Arvind--Cameron (2022); a two-generator positive theorem remains fully consistent with the example.

**Explicit model.** For integers \(q\ge2\) that are prime powers and \(\ell\ge1\), take a rooted forest with \(q+1\) roots at level \(1\), and \(q\) children at each node through level \(\ell\). Introduce a bag \(B_{s,u}\) for each \(0\le s<\ell\) and every node \(u\) at level \(\ell-s\), with
\[
|B_{s,u}|=q^\ell(q-1)q^{\ell-s-1}.
\]
Introduce a set of \(q^\ell\) universal vertices. Each bag is a clique. Two vertices of distinct bags \(B_{s,u}\) and \(B_{t,v}\) are adjacent precisely when either \(s+t\ge\ell\), or \(s+t<\ell\) and the ancestors of \(u,v\) at level \(\ell-s-t\) are equal. All universal vertices are adjacent to all other vertices. This specifies \(\mathcal G_{q,\ell}\) without reference to any ring.

**Degree distribution.** The central \(q^\ell\) vertices have degree \(q^{3\ell}-1\). For every \(0\le s<\ell\), exactly
\[
q^\ell\bigl(q^{2(\ell-s)}-q^{2(\ell-s-1)}\bigr)
\]
noncentral vertices have degree \(q^{2\ell+s}-1\). Thus the number of distinct noncentral degrees is exactly \(\ell\); the graph itself recovers \(\ell\) and, from its order \(q^{3\ell}\), recovers \(q\).

As an enumerative corollary, the number of ordered pairwise-commuting \(k\)-tuples in \(H(R)\), for any \(k\ge1\), is \(q^{\ell k}M_{\ell,k}(q)\), where
\[
M_{\ell,k}(q)=q^{2k\lfloor\ell/2\rfloor}+\sum_{s=0}^{\lfloor(\ell-1)/2\rfloor}q^{2ks}\left(q^{\ell-2s}+q^{\ell-2s-1}\right)\left(q^{k(\ell-2s)}-q^{k(\ell-2s-1)}\right).
\]
This last count is a consequence of the graph model, not the basis of the novelty claim; more general finite-chain-ring matrix enumeration is part of prior literature.

## Assumptions and scope

The rings are finite, nonzero, commutative, local principal ideal rings with a unique chain \(R\supsetneq\mathfrak m\supsetneq\cdots\supsetneq\mathfrak m^{\ell-1}\supsetneq0\). Set \(\mathfrak m=(\pi)\), and \(q=|R/\mathfrak m|\). Each ideal quotient \(\mathfrak m^j/\mathfrak m^{j+1}\) has size \(q\), so \(|R/\mathfrak m^j|=q^j\). The field case \(\ell=1\) is included. No restriction on the characteristic or on the nilpotence index is imposed. The graph includes central vertices; deleting them preserves the forward isomorphism statement, but the recovery argument here is formulated for full graphs.

Identify group elements with triples \((a,b,c)\in R^3\), with multiplication
\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab').
\]
The commutation condition is \(ab'-a'b=0\), independent of both central coordinates. The full graph is simple: no loops are counted, even though an element commutes with itself.

## Proof

**1. Center and determinant pairing.** Direct matrix multiplication gives
\[
[(a,b,c),(a',b',c')]=(0,0,ab'-a'b)
\]
for one standard commutator convention (reversing convention changes only the sign). Thus \(Z(H(R))=H(R)'=\{(0,0,c):c\in R\}\). The inclusion \(H(R)'=Z(H(R))\) follows by taking commutators with \((1,0,0)\) and \((0,1,0)\). In particular the group is nonabelian class two.

**2. Valuation and projective directions.** Define \(\nu(0)=\ell\); for nonzero \(a\in R\), define \(\nu(a)=s\) when \(a\in\mathfrak m^s\setminus\mathfrak m^{s+1}\). For \((a,b)\ne(0,0)\), put \(s=\min(\nu(a),\nu(b))\), and write \((a,b)=\pi^s(u,v)\). Its primitive pair \((u,v)\) is well defined modulo \(\pi^{\ell-s}\), and at least one coordinate is a unit in \(R/(\pi^{\ell-s})\). Its projective line \([u:v]\in\mathbb P^1(R/(\pi^{\ell-s}))\) is therefore well defined.

For any commutative local ring \(A\), if \((u,v)\) and \((u',v')\) are primitive, then \(uv'-u'v=0\) in \(A\) if and only if they represent the same point of \(\mathbb P^1(A)\). Indeed, if \(u\) is a unit, the equation forces \(v'=u'(u^{-1}v)\), and primitiveness of the second pair forces \(u'\) to be a unit. If \(u\) is not a unit then \(v\) is a unit and the symmetric argument applies. This proves the critical projective-line criterion without division by a zero divisor.

Consider elements whose vector parts have valuations \(s\) and \(t\). If \(s+t\ge\ell\), then their determinant is zero automatically. Otherwise the determinant vanishes in \(R\) exactly when the primitive directions, reduced to \(\mathbb P^1(R/(\pi^{\ell-s-t}))\), coincide. This follows from \(\operatorname{Ann}(\pi^{s+t})=(\pi^{\ell-s-t})\), followed by the primitive-line criterion.

**3. The projective tree is universal.** For each \(j\ge1\), the projective line over \(R/(\pi^j)\) has exactly \(q^j+q^{j-1}\) points: choose whether the first coordinate is a unit (giving \((1,x)\), \(q^j\) choices) or the second is a unit and the first is a nonunit (giving \((x,1)\), \(q^{j-1}\) choices). Reduction from level \(j\) to \(j-1\) is surjective and has exactly \(q\) lifts per point, as is immediate from these normalized charts. Consequently the tower of projective points is abstractly a forest with \(q+1\) roots and \(q\) children per node, independent of ring operations.

For fixed \(s\), the number of vector pairs of valuation \(s\) is \(q^{2(\ell-s)}-q^{2(\ell-s-1)}\). Dividing by the number \(q^{\ell-s}+q^{\ell-s-1}\) of directions gives \((q-1)q^{\ell-s-1}\) vector pairs per projective direction. Multiplying by the \(q^\ell\) free central coordinates gives the asserted bag size. The zero vector part contributes \(q^\ell\) universal vertices. Step 2 gives exactly the bag adjacency rule, proving \(\Gamma(H(R))\cong\mathcal G_{q,\ell}\). In particular two rings of matching \((q,\ell)\) yield isomorphic full graphs.

**4. Necessity of matching \(q,\ell\).** If the vector part of a noncentral element has valuation \(s\), the linear map \(R^2\to R\), \((a',b')\mapsto ab'-a'b\), has image \((a,b)=(\pi^s)\) of size \(q^{\ell-s}\). Its kernel therefore has size \(q^{\ell+s}\), so the element's group centralizer has size \(q^{2\ell+s}\). Exactly \(q^\ell(q^{2(\ell-s)}-q^{2(\ell-s-1)})\) vertices have this degree. The central vertices have centralizer size \(q^{3\ell}\). Thus the graph has exactly \(\ell\) distinct noncentral degrees, and its order is \(q^{3\ell}\), recovering \(\ell\) and then \(q\). This proves the reverse implication.

**5. Explicit failure of isoclinism.** Both \(\mathbb Z/8\mathbb Z\) and \(\mathbb F_2[t]/(t^3)\) have \((q,\ell)=(2,3)\); their full commuting graphs are thus isomorphic. But \(H(R)/Z(H(R))\cong(R,+)^2\) and \(H(R)'\cong(R,+)\). The first ring's additive group is \(C_8\), whereas the second's is \(C_2^3\). Therefore the central quotients and derived groups are nonisomorphic, which is incompatible with isoclinism. Their common commuting graph has \(512\) vertices and central degree \(511\), with noncentral degrees \(63,127,255\) occurring respectively \(384,96,24\) times. The groups' characteristic discrepancy is real, not a change of presentation.

**6. All-arity counting corollary.** For \(k\) vector pairs \((a_i,b_i)\), let \(s\) be the minimum valuation among all \(2k\) coordinates. If \(s\ge\lceil\ell/2\rceil\), all determinants vanish, contributing \(q^{2k\lfloor\ell/2\rfloor}\). Otherwise put \(L=\ell-2s\). Reduction to the quotient of length \(L\) leaves a primitive \(k\)-tuple of vectors with pairwise zero determinant, hence a unique projective direction. There are \(q^L+q^{L-1}\) choices of this direction and \(q^{Lk}-q^{(L-1)k}\) scalar tuples with some unit; independently lifting the \(2k\) coordinates supplies \(q^{2ks}\) choices. Sum the disjoint minimum-valuation strata and multiply by \(q^{\ell k}\) central-coordinate choices. This proves the displayed formula for all integers \(k\ge1\) without relying on finite experiments.

## Verification

The standalone file `verify.py` constructs the ring multiplication independently in both unequal-characteristic models \(\mathbb Z/p^\ell\mathbb Z\) and \(\mathbb F_p[t]/(t^\ell)\), and also checks small fields of order four. It directly enumerates determinant-zero relations and ordered commuting tuples, then compares them with the formula above.

More importantly, it constructs canonical projective-direction paths by normalizing pairs and recursively numbering children of each projective-line reduction map. It maps every vector in one ring to the unique vector in the second ring carrying the same valuation, canonical path, and multiplicity index. Across five cross-ring cases \((q,\ell)\in\{(2,2),(2,3),(2,4),(3,2),(3,3)\}\), it compares every ordered pair of vector classes. For \((q,\ell)=(2,3)\), it also expands all \(512\) group vertices and directly tests all \(512^2\) ordered group-vertex pairs, not merely degree histograms.

Run `python3 verify.py` in a directory containing the standalone file. The expected terminal line is `VERIFY_OK 11 exact commuting-tuple censuses and 5 exhaustive cross-ring graph-isomorphism maps`.

## Relationship to prior work

Diaconis and Malliaris (2021) explicitly define Heisenberg commuting graphs over fields and analyze their geometry; their motivating treatment specializes to the finite-field case and does not give the classification over nonisomorphic nonreduced chain rings.

Arvind and Cameron, *Recognizing the Commuting Graph of a Finite Group* (2022), Section 8, state the conjecture that nilpotency-class-two groups with isomorphic commuting graphs must be isoclinic; their counterexample concerns class three. The present pair lies precisely in the conjectured class two and has inequivalent central quotients. The later paper *Aspects of the commuting graph* (2023 preprint, 2026 journal) replaces parts of that preprint and studies recognition and forbidden subgraphs; the inspected text does not establish a finite-chain-ring collapse or resolve the above counterexample.

Cameron and Kuzma (2022) show that equally sized isoclinic groups have isomorphic commuting graphs. That sufficient condition cannot imply the present example because the two groups are not isoclinic.

A published classification of commuting graphs for **two-generated** class-two groups reduces those graphs to determinant-zero graphs over a cyclic ring. It includes the \(\mathbb Z/8\mathbb Z\) group but does **not** include \(H(\mathbb F_2[t]/(t^3))\), whose central quotient requires six generators. Thus its positive isoclinism conclusion is not contradicted. The present theorem compares the whole family of arbitrary finite commutative chain rings, including the noncyclic additive cases.

Research on symplectic graphs over finite local rings studies graphs whose vertices are primitive projective lines, often joined when a determinant is a unit. That relation is not the determinant-**zero** relation on all vectors, including all valuation shells, used here. Previously known finite-chain-ring determinant or Smith-normal-form counts similarly do not themselves establish full graph isomorphism of nonisoclinic groups.

## Limitations

The theorem is restricted to commutative **chain** rings, not arbitrary finite local rings or higher-rank Heisenberg groups. The explicit group collision refutes the class-two isoclinism statement, but does not classify every class-two group sharing a commuting graph. The full graph includes central vertices. There is no claim that the groups themselves or their commutator maps are isomorphic; indeed the example proves the contrary. The combinatorial model and proof are infinite-family arguments; the standalone computations are finite corroborations. Independent audit and a complete global literature priority certification have not been performed.

## References

1. P. Diaconis and M. Malliaris, “Complexity and randomness in the Heisenberg groups (and beyond),” arXiv:2107.02923v1, first public 6 July 2021, https://arxiv.org/abs/2107.02923.
2. V. Arvind and P. J. Cameron, “Recognizing the Commuting Graph of a Finite Group,” arXiv:2206.01059v1, first public 2 June 2022, especially Section 8 and its explicit conjecture, https://arxiv.org/abs/2206.01059.
3. P. J. Cameron and B. Kuzma, “Between the enhanced power graph and the commuting graph,” first published online 8 August 2022, DOI 10.1002/jgt.22871.
4. V. Arvind, X. Ma, P. J. Cameron and N. V. Maslova, “Aspects of the commuting graph,” arXiv:2305.07301, first public 12 May 2023, https://arxiv.org/abs/2305.07301.
5. “Two-generated class-two commuting graphs are determinant blow-ups,” public mathematical report (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-two-generated-class-two-commuting-graphs-are-determinant-blow-up--414532e5643a.
6. “Symplectic graphs over finite local rings,” *European Journal of Combinatorics* 34 (2013), 1114--1124, DOI 10.1016/j.ejc.2013.03.003.
7. A. Wang and R. P. Stanley, “The Smith normal form distribution of a random integer matrix,” 2017. Prior enumerative context; not used to establish commuting-graph isomorphism.
