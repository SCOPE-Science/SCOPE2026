# A sharp rank-five Paley–Peisert separation and the first 4-existentially closed Peisert graph

## Finding
Let \(P^*(q)\) be the Peisert graph on \(\mathbb F_q\) for \(q=p^{2e}\) with \(p\equiv3\pmod4\). For a finite simple graph, call the graph \(k\)-existentially closed (\(k\)-e.c.) when every pattern of required adjacency and required nonadjacency to \(k\) distinct vertices has a realization outside those vertices. The first 4-e.c. Peisert graph occurs at exactly \(q=361\):
\[
\min\{q:P^*(q)\text{ is 4-e.c.}\}=361.
\]
Moreover every four-vertex pattern in \(P^*(361)\) has **at least ten** realizations, and some pattern has exactly ten.

At order \(121\), the Paley graph \(P(121)\) is 4-e.c., with at least two realizations of every four-vertex pattern, whereas \(P^*(121)\) is not 4-e.c. Both graphs are 3-e.c. and have the same strongly regular parameters \((121,60,29,30)\). Consequently they are indistinguishable by first-order sentences of quantifier rank at most four, but distinguishable at rank five:
\[
P(121)\equiv_4P^*(121),\qquad P(121)\not\equiv_5P^*(121).
\]
Here the language consists solely of equality and undirected adjacency. This is a sharp logical-depth comparison for these two particular graphs, not a classification of all conference graphs.

## Assumptions and scope
The Peisert construction is defined only for \(q=p^{2e}\), where \(p\) is prime, \(p\equiv3\pmod4\), and \(e\ge1\). With a primitive element \(g\in\mathbb F_q\), put
\[
D_q=\{g^j:j\equiv0\text{ or }1\pmod4\}.
\]
Distinct field elements are adjacent in \(P^*(q)\) precisely when their difference belongs to \(D_q\). Since \(q\equiv1\pmod8\), this is an undirected simple graph. For comparison, distinct elements of \(\mathbb F_{121}\) are adjacent in the Paley graph when their difference is a nonzero square. For all field representatives below, integer labels encode polynomial coefficients in increasing order, as base-\(p\) digits.

The explicit field models (each modulus irreducible, each indicated generator primitive) are

| Order | Modulus | Generator label | 
| --- | --- | ---: |
| \(9\) | \(X^2+1\) over \(\mathbb F_3\) | 4 |
| \(49\) | \(X^2+4\) over \(\mathbb F_7\) | 8 |
| \(81\) | \(X^4+X+2\) over \(\mathbb F_3\) | 3 |
| \(121\) | \(X^2+9\) over \(\mathbb F_{11}\) | 13 |
| \(361\) | \(X^2+17\) over \(\mathbb F_{19}\) | 21 |

For a graph \(G\) and ordered distinct vertices \(v_0,\ldots,v_{k-1}\), define the extension multiplicity of a bit pattern \(b\in\{0,1\}^k\) as the number of vertices \(z\) outside the tuple for which \(E(z,v_i)\) holds precisely at coordinates with \(b_i=1\). A graph is \(k\)-e.c. exactly when all these multiplicities are positive. The scope is finite, ordinary first-order graph logic; no named bipartition, field operations, or order is present in the logical language.

## Proof
**1. Every smaller eligible order fails.** The only eligible Peisert orders not exceeding \(361\) are \(9,49,81,121,361\), by the prime-power and congruence restrictions. For the first four, respectively, the following distinct four-tuples witness a missing pattern:

| Order | Four encoded vertices | Missing extension pattern |
| --- | --- | --- |
| \(9\) | \((0,1,2,3)\) | no vertex nonadjacent to all four |
| \(49\) | \((0,1,2,3)\) | no vertex nonadjacent to all four |
| \(81\) | \((0,1,2,42)\) | no vertex nonadjacent to all four |
| \(121\) | \((0,1,16,17)\) | no common neighbor of all four |

Each zero count follows by exact field arithmetic modulo the displayed irreducible polynomial, using the displayed primitive generator. The complete sixteen-entry extension count vectors for these tuples are computed by the standalone Python verifier. Thus no eligible order below \(361\) has the 4-e.c. property.

**2. A complete positive calculation at order \(361\).** Field translations act by automorphisms on the Peisert graph. Also, multiplication by \(g^{4t}\) acts by an automorphism because it preserves the connection set \(D_q\). For any four distinct vertices, translate one to zero and multiply by an appropriate fourth power to send a second to one of \(1,g,g^2,g^3\). Therefore every four-set extension pattern is equivalent to one checked on a tuple \((0,b,c,d)\), with \(b\in\{1,g,g^2,g^3\}\), \(c,d\ne0,b\), and \(c<d\) in integer encoding. Exactly
\[
4\binom{359}{2}=257044
\]
representative tuples suffice. Exact counts of all sixteen patterns on all such tuples have minimum **ten**, so every possible four-set has at least ten witnesses. On the tuple \((0,1,2,3)\), exactly the ten vertices
\[
41,81,82,95,187,196,269,301,302,323
\]
are nonadjacent to every member; hence the lower bound is attained. The checker separately validates the field and generator, the connection-set adjacency rule, and the exhaustive orbit range. A second implementation builds the graph using finite-field quartic characters rather than discrete-log connection-set enumeration and obtains the identical minimum of ten.

**3. Comparison at order \(121\).** Directly exhaust all \(\binom{120}{3}=280840\) four-sets containing vertex zero, which suffice by translation invariance. Every pattern in the Paley graph has at least two witnesses; some have precisely two. For example, with selected vertices \((0,1,2,12)\), the pattern adjacent to the first, third and fourth but not the second is realized exactly by vertices \(44,46\). For Peisert, the tuple \((0,1,16,17)\) lacks a common neighbor, as above. A separate complete calculation over all \(\binom{120}{2}=7140\) three-sets containing zero finds minimum three-pattern multiplicity \(12\) for the Paley graph and \(11\) for Peisert. Thus both are 3-e.c. Exact pairwise common-neighbor counts show the two graphs each have parameters \((121,60,29,30)\).

**4. Sharp logical depth.** In a graph having at least four vertices, the \(k\)-extension property for \(k=3\) gives a winning four-round duplicator strategy against the countable Rado graph: after at most three distinct vertices have been chosen, Duplicator realizes the prescribed adjacency and nonadjacency pattern, padding to a three-tuple if necessary. The Rado graph has the unrestricted extension property. Both order-121 graphs are therefore equivalent through rank four. A rank-five sentence asserts the existence of four distinct vertices without any common neighbor:
\[
\exists x_0\exists x_1\exists x_2\exists x_3\;\left[\bigwedge_{i<j}x_i\ne x_j\;\land\;\forall z\neg\bigwedge_{i=0}^{3}E(z,x_i)\right].
\]
This sentence is true in \(P^*(121)\) by the exhibited tuple and false in \(P(121)\) by its 4-e.c. property. Its quantifier rank is five. Hence rank five is the first rank separating these two graphs.

## Verification
The complete reproducibility package contains `verify_small_and_orbits.py` (Python standard library, explicit polynomial-remainder irreducibility and primitive-element tests) and `independent_peisert.cpp` (C++17, direct quartic-character adjacency). Run

```sh
python3 verify_small_and_orbits.py
c++ -std=c++17 -O3 independent_peisert.cpp -o independent_peisert
./independent_peisert
```

On \(P^*(361)\), the independent programs each check \(257044\) symmetry-reduced four-tuples and obtain a minimum multiplicity of \(10\). The C++ program separately checks all \(280840\) four-tuples containing zero in both order-121 graphs: Paley has minimum \(2\) and no failures, Peisert has \(400\) four-tuples (containing zero) with at least one missing pattern. Both are 3-e.c., with minimum three-pattern counts \(12\) and \(11\), respectively. The two programs use different adjacency calculations and different enumeration methods where indicated. `python_output.txt` and `independent_output.txt` record actual completed runs. The finite exhaustive calculations serve as exact proofs of the bounded cases; no infinite parameter range is extrapolated.

## Relationship to prior work
Peisert's 2001 construction identifies the additional infinite family of self-complementary symmetric graphs. Kisielewicz and Peisert (2004) investigate pseudorandom properties of this family. Mullin's 2009 thesis, especially Chapter 3 and Table 3.1, details the quartic-coset construction and enumerates maximal cliques at several of the same orders, but does not give 4-extension multiplicities or the rank-four/rank-five separation at order \(121\). Classical Rado-graph extension arguments explain how a 3-e.c. versus 4-e.c. discrepancy yields a sharp logical-depth distinction; they do not supply these finite-field counts.

The paper of Kisielewicz and Peisert (2004) could not be inspected beyond accessible bibliographic material and its abstract. No assertion of complete noncoverage by that unread full text is made. The distinction between general pseudorandom or sufficiently-large-order extension theorems and the **sharp first Peisert 4-e.c. order** is important: an asymptotic sufficient bound alone would not establish the exact cutoff or the Paley–Peisert separation at the fixed order \(121\).

## Limitations
This result identifies the first qualifying Peisert order and establishes one exact logical-depth separation. It does **not** assert that every eligible Peisert order greater than or equal to \(361\) is 4-e.c., classify other self-complementary strongly regular graphs, or determine a universal minimum 4-e.c. graph. The finite computations are complete within the stated ranges and symmetry reductions, but no independent human or formal proof audit has been performed. The inaccessible full text of the relevant 2004 pseudorandomness article is a residual historical-priority risk.

## References
1. W. Peisert, *All self-complementary symmetric graphs*, Journal of Algebra **240** (2001), 209–229. DOI: `10.1006/jabr.2000.8714`.
2. A. Kisielewicz and W. Peisert, *Pseudo-random properties of self-complementary symmetric graphs*, Journal of Graph Theory **47** (2004), 310–316. DOI: `10.1002/jgt.20035`.
3. N. E. Mullin, *Self-Complementary Arc-Transitive Graphs and Their Imposters*, University of Waterloo thesis (2009), especially Chapter 3, Sections 3.1 and 3.4. URI: `https://hdl.handle.net/10012/4264`.
4. The classical extension-axiom description of the countable Rado graph and the Ehrenfeucht–Fraïssé game characterization of bounded quantifier rank are used in their standard form; the needed four-round strategy and separating five-round sentence are spelled out above.
