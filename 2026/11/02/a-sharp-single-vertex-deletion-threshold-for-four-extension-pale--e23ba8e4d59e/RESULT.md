# A sharp single-vertex deletion threshold for four-extension Paley graphs

## Finding

Let \(q\ge5\) be an odd prime power with \(q\equiv1\pmod4\). The Paley graph \(P_q\) has vertex set \(\mathbb F_q\), with distinct \(u,v\) adjacent if and only if \(u-v\) is a nonzero square. Let \(\mathcal R\) be the countable random (Rado) graph, and let \(\equiv_5\) denote agreement on all ordinary first-order sentences of quantifier rank at most five in the language of undirected adjacency and equality, with no counting quantifiers. Then

\[
\boxed{\quad (\forall v\in V(P_q))\;P_q-v\equiv_5\mathcal R\quad\Longleftrightarrow\quad q\ge89\ \text{and}\ q\ne125.\quad}
\]

Equivalently, every choice of four distinct vertices and a prescribed adjacency/nonadjacency relation to those four has **at least two distinct witnesses** exactly for the indicated orders. This includes all prime-power fields, not only prime fields. The exception at \(q=125\) is genuine: the graph satisfies all four-point extension requirements with one witness, but a particular pattern has precisely one witness and fails after its deletion. Thus the robust property is not monotone in field order across the eligible family.

## Assumptions and scope

For disjoint subsets \(A,B\subseteq V(G)\), a witness is a vertex \(x\notin A\cup B\) adjacent to all of \(A\) and none of \(B\). Define \(P(m,n,k)\) to require at least \(k\) witnesses for every disjoint \(A,B\) with \(|A|=m\) and \(|B|=n\). Define the four-point two-witness property by requiring \(P(m,4-m,2)\) for all integers \(0\le m\le4\). We work throughout with simple undirected graphs and odd prime powers congruent to one modulo four; in this case minus one is a square and adjacency is symmetric.

The countable random graph has the extension property for every finite disjoint pair of vertex sets. A finite graph is four-existentially closed (four-e.c.) when every four-point pattern has at least one witness. The four-point two-witness property automatically implies the same property on any smaller number of anchors by extending the anchor set to four and prescribing arbitrary extra relations. This is possible because the orders in the asserted positive range exceed four.

## Proof

**Step 1: logical equivalence and deletion.** For a finite graph \(G\) with more than five vertices, the following are equivalent: (i) every vertex-deleted graph \(G-v\) agrees with \(\mathcal R\) through quantifier rank five; (ii) every four-vertex pattern of \(G\) has at least two different witnesses. Indeed, the usual five-round Ehrenfeucht–Fraïssé back-and-forth strategy matches equality and adjacency among previously selected vertices; when a new vertex is chosen, at most four vertices have been selected and the corresponding pattern has a witness. This proves rank-five agreement for a four-e.c. graph. Conversely, for each fixed four-vertex adjacency prescription the rank-five sentence

\[
\forall x_1\forall x_2\forall x_3\forall x_4\Bigl(\bigwedge_{i<j}x_i\ne x_j\ \longrightarrow\ \exists y\,\bigl[\bigwedge_{i=1}^4 y\ne x_i\ \land\ \bigwedge_{i=1}^4 L_i(y,x_i)\bigr]\Bigr)
\]

is true in \(\mathcal R\), where each \(L_i(y,x_i)\) is the fixed literal \(E(y,x_i)\) or \(\neg E(y,x_i)\) prescribed for that index. Thus agreement at rank five forces each four-vertex pattern to have a witness. If two witnesses exist in \(G\), deletion of any vertex leaves at least one; if a pattern has at most one witness, deleting that witness (or any other vertex if there are none) leaves an unsatisfied pattern. In the latter case choose the deletion outside the four anchors; the Paley graphs considered have enough vertices. This proves the claimed equivalence with two-witness positivity.

**Step 2: an analytic bound.** Write \(\chi\) for the nontrivial quadratic multiplicative character on \(\mathbb F_q\), extended by \(\chi(0)=0\). For four distinct anchors \(a_1,\ldots,a_4\) and chosen signs \(\epsilon_i\in\{-1,1\}\), the number \(N\) of vertices outside the anchors satisfying \(\chi(x-a_i)=\epsilon_i\) for each \(i\) obeys

\[
16N=\sum_{x\notin\{a_1,a_2,a_3,a_4\}}\prod_{i=1}^{4}(1+\epsilon_i\chi(x-a_i)).
\]

Extend the sum to all \(x\). The empty product contributes \(q\). The four singleton character sums vanish. Each of the six sums for a product of two distinct linear factors equals \(-1\) and therefore contributes in absolute value at most one. The four squarefree cubic sums have absolute value at most \(2\sqrt q\) each, and the squarefree quartic sum at most \(3\sqrt q\), by the standard Weil quadratic-character estimate \( |\sum_x\chi(f(x))|\le(\deg f-1)\sqrt q\) for a squarefree nonconstant product of linear factors. At an excluded anchor, one factor equals one and the remaining three factors each have absolute value at most two; hence each excluded term has absolute value at most eight. Consequently

\[
\boxed{\quad N\ \ge\ \frac{q-38-11\sqrt q}{16}.\quad}
\]

The right side exceeds two at \(q=241\) and increases for all \(q\ge241\) (its derivative is positive there). Therefore every admissible Paley graph of order at least \(241\) has the four-point two-witness property. This is a sufficient tail bound, not an asserted optimum character-sum estimate.

**Step 3: a complete finite check below the tail.** The program `verify_paley.py` enumerates all odd prime powers \(q\equiv1\pmod4\) with \(5\le q<241\). For a prime power \(q=p^e\) with \(e>1\), it represents \(\mathbb F_q\) as \(\mathbb F_p[X]/(f)\) using the listed monic irreducible polynomial, and verifies irreducibility by division against every monic polynomial of degree at most \(\lfloor e/2\rfloor\). For each field it directly constructs the nonzero-square set and exact adjacency bitsets.

Any four distinct field elements \(u,v,w,z\) can be sent by the invertible affine map \(x\mapsto(x-u)/(v-u)\) to \(0,1,a,b\) with \(a,b\notin\{0,1\}\) distinct. If the multiplier is a nonsquare, all adjacency and nonadjacency conditions are interchanged; since all sixteen patterns are checked this makes no difference to their minimum counts. Hence enumerating every set \(\{0,1,a,b\}\) and its sixteen patterns is exhaustive up to a symmetry that preserves the minimum. The program computes every witness set by bitset intersection, removing the four anchors. It also verifies symmetry, absence of loops, and the number of nonzero squares. The output file `verification_output.txt` records the complete minimizing configuration for each order.

The complete census of minima \(\mu(q)\) is:

| Eligible field orders \(q\) | Minimum witness counts \(\mu(q)\) |
|---|---|
| \(5,9,13,17,25,29,37,41,49,53,61,73,81\) | All \(0\) |
| \(89,97,101,109,113,121\) | All \(2\) |
| \(125\) | \(1\) |
| \(137,149,157,169,173,181,193,197,229,233\) | \(3,4,4,4,4,2,6,5,6,6\), respectively |

The input orders are not preselected: the code factors every integer below \(241\) and selects the eligible odd prime powers. Each exact minimum is computed over all normalized four-sets and every one of the sixteen prescribed relation patterns. The separate program `independent_check.py` recomputes the nine crucial orders \(81,89,97,121,125,137,169,181,233\) by a different algorithm based on character exponentiation and direct histograms, agreeing on every minimum.

For a concrete sharp failure, represent \(\mathbb F_{125}=\mathbb F_5[X]/(X^3+X+1)\), encoding polynomials by their base-five coefficients. For the four anchors \(\{0,1,2,3\}\), the pattern adjacent to \(0,3\) and nonadjacent to \(1,2\) has **exactly one witness, \(4\)**. Deleting \(4\) destroys this extension requirement. In contrast, the minimum at \(q=89\) is two; one attaining pattern is adjacency to all of \(\{0,1,2,3\}\), with exactly the witnesses \(11\) and \(81\). Combining the exact finite census with the proved analytic tail yields the stated equivalence for every admissible prime-power order. \(\square\)

## Verification

Run `python3 verify_paley.py > verification_output.txt` and `python3 independent_check.py > independent_output.txt` using Python 3 and its standard library. The stored output files are the literal results of these commands; the two programs were separately executed and their outputs compared byte-for-byte. The main program checks every eligible prime-power order less than \(241\), using all sixteen patterns on all affine-normalized four-sets. The independent program uses direct character-power calculations rather than square-membership bitsets. The analytic tail is established by the written quadratic-character argument and is not derived from finite experiments.

## Relationship to prior work

The adjacency-property terminology \(P(m,n,k)\) is established in W. Ananchuen and L. Caccetta, *On the adjacency properties of Paley graphs* (1993). That paper's accessible abstract gives asymptotic Paley guarantees for arbitrary fixed parameters, but no complete order-by-order threshold is stated in that abstract. Blass, Exoo, and Harary (1981) similarly establish eventual satisfaction of first-order adjacency axioms. Elsawy's thesis (public arXiv version dated 2012-03-07), section 2.2, describes both three-existential closure and sufficient large-order inequalities for \(P(m,n,k)\). Those results overlap the large-field sufficiency conclusion; the distinctive question here is the **exact all-prime-power classification**, especially the isolated single-witness failure at \(125\) after success at \(89\), and the sharp least robust order.

The primary 1993 article was available for this comparison through its bibliographic record and abstract but not accessible in full text. Accordingly its possible more precise internal tables or claims remain a historical-priority risk; absence from an abstract is not evidence of absence from the full paper. This result does not claim a new asymptotic existence theorem or priority over previously established sufficient bounds.

## Limitations

The theorem applies only to odd prime powers congruent to one modulo four and to deletion of exactly one vertex. The logical equivalence concerns quantifier rank at most five, not unrestricted-depth first-order equivalence, counting logic, arbitrary graph families, or deletion of multiple vertices. Finite verification is exhaustive only below the explicitly proved analytic cutoff; the infinite range is justified by the character bound. The source comparison is not a complete priority certification, and independent mathematical validation has not been performed.

## References

1. W. Ananchuen and L. Caccetta, *On the adjacency properties of Paley graphs*, Networks **23** (1993), 227–236. DOI: https://doi.org/10.1002/net.3230230404.
2. A. Blass, G. Exoo and F. Harary, *Paley graphs satisfy all first-order adjacency axioms*, Journal of Graph Theory **5** (1981), 435–439. DOI: https://doi.org/10.1002/jgt.3190050414.
3. A. N. Elsawy, *Paley Graphs and Their Generalizations*, arXiv:1203.1818v1, publicly submitted 2012-03-07, particularly section 2.2. https://arxiv.org/abs/1203.1818.
4. Standard quadratic-character Weil estimate for a squarefree polynomial over a finite field, used only in the explicit \(q\ge241\) tail bound.
