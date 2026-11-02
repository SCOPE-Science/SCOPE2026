# The 89-vertex Paley graph is the first Paley model of the five-round random-graph theory

## Finding

For every prime power \(q\equiv1\pmod 4\), let \(P(q)\) denote the undirected Paley graph on \(\mathbb F_q\): distinct \(u,v\) are adjacent exactly when \(u-v\) is a nonzero square. A graph has the **four-extension property**, also called **4-existential closure**, if for every ordered four-tuple of distinct vertices \((a_0,a_1,a_2,a_3)\) and every pattern \(\varepsilon\in\{0,1\}^4\), some other vertex \(z\) satisfies \(z\sim a_i\) exactly when \(\varepsilon_i=1\).

**Theorem (sharp first Paley four-extension threshold).** Among the graphs \(P(q)\) indexed by prime powers \(q\equiv1\pmod4\), the smallest order with the four-extension property is exactly \(q=89\). More precisely, \(P(89)\) has the property, and none of the thirteen eligible smaller orders \(q\in\{5,9,13,17,25,29,37,41,49,53,61,73,81\}\) does.

Let \(R\) denote the countable Rado graph and \(\equiv_5\) agreement on all first-order sentences of quantifier rank at most five in the vocabulary consisting of equality and undirected adjacency. For every finite graph \(G\),
\[
G\equiv_5 R\quad\Longleftrightarrow\quad G\text{ has the four-extension property}.
\]
Thus \(P(89)\), on 89 vertices, is the *first Paley graph* sharing the five-round theory of \(R\). The minimum is **within the Paley family**: no minimum is asserted over all finite graphs or all strongly regular graphs. Neither is an upper stabilization threshold asserted for all larger prime powers.

## Assumptions and scope

Graphs are simple, finite and undirected except for the explicitly identified infinite comparison graph \(R\). The parameter \(q\) ranges over all prime powers, not only primes, with \(q\equiv1\pmod4\). Finite fields of composite order are constructed as quotients by verified irreducible polynomials; treating such fields as integers modulo \(q\) would be incorrect. Quantifier rank is the maximum nested first-order quantifier depth; no orders, colours or distinguished constants are allowed.

## Proof

**Step 1: translation from four-extension to the five-round theory.** In a five-move Ehrenfeucht–Fraïssé game between a graph \(G\) with the four-extension property and \(R\), Duplicator maintains a partial isomorphism. At each move there are at most four previously selected distinct vertices. If the moving player chooses an already selected vertex, Duplicator repeats its partner. Otherwise the new adjacency pattern to those previous vertices can be realized on the other graph: by the extension property of \(R\), or by the four-extension property of \(G\). For fewer than four prior vertices, pad the prescription to four distinct vertices in \(G\); these exist because a four-extension graph necessarily has more than four vertices. Duplicator wins all five rounds, proving \(G\equiv_5R\). Conversely, every four-vertex extension axiom has quantifier rank five, is true in \(R\), and must therefore hold in any \(G\equiv_5R\). This proves the equivalence.

**Step 2: reduce the finite-field test to finitely many normal forms.** Translation and multiplication by a nonzero square are automorphisms of \(P(q)\). For any ordered pair of distinct vertices, an automorphism takes it to either \((0,1)\) or \((0,\nu)\), where \(\nu\) is a fixed nonsquare. Thus, to test every four-tuple and every extension pattern, it suffices to check the two normalized initial pairs and each unordered pair of other vertices. For \(q\ge5\), there are exactly
\[
2\binom{q-2}{2}=(q-2)(q-3)
\]
normal-form tests. Each test partitions the vertices outside the chosen four into all 16 possible adjacency-pattern cells, represented by exact integer bitsets. The 4-extension property holds exactly when all 16 cells are nonempty for every normal-form test. This is an exhaustive symmetry reduction, not a probabilistic sampling argument.

**Step 3: check every eligible order through 89.** Unique prime-power factorization and the elementary primality test enumerate exactly the eligible orders
\[
5,9,13,17,25,29,37,41,49,53,61,73,81,89.
\]
The standalone `verify_paley89.py` constructs each finite field, verifies irreducibility of the chosen defining polynomial by checking every possible monic factor of degree at most half, constructs its Paley adjacency bitsets, and executes Step 2. For every order less than 89 the program returns a four-vertex set and a missing adjacency pattern. The thirteen witness pairs \((q;\text{vertices};\text{missing pattern index})\) are

| Order | Four distinct vertices (field-element encoding) | Pattern index |
| ---: | --- | ---: |
| 5 | 0,1,2,3 | 0 |
| 9 | 0,1,2,3 | 0 |
| 13 | 0,1,2,3 | 2 |
| 17 | 0,1,2,3 | 0 |
| 25 | 0,1,2,3 | 0 |
| 29 | 0,1,2,3 | 0 |
| 37 | 0,1,2,7 | 4 |
| 41 | 0,1,2,3 | 15 |
| 49 | 0,1,2,3 | 11 |
| 53 | 0,1,2,3 | 15 |
| 61 | 0,1,3,14 | 1 |
| 73 | 0,1,8,9 | 15 |
| 81 | 0,1,2,42 | 7 |

Here index \(j\in\{0,\ldots,15\}\) means the \(i\)-th bit of \(j\) prescribes adjacency to the \(i\)-th listed vertex. Each entry is independently testable from the embedded code, which also specifies field encoding. For \(q=89\), the normal-form computation exhausts all 7,482 configurations and finds no missing pattern.

**Step 4: independent, non-symmetry-reduced positive certificate.** The separately written C++ program `verify_paley89_direct.cpp` constructs the degree-44 Paley graph over \(\mathbb F_{89}\) using quadratic residues modulo 89 and checks every one of the
\[
\binom{89}{4}=2,441,626
\]
four-element vertex subsets directly, searching all 16 possible extension patterns outside each subset. Every test succeeds. Unlike Step 2, this check does not use graph automorphisms, normal forms, finite-field quotient arithmetic, or the Python bitset construction. Therefore \(P(89)\) has four-extension, and the preceding complete list of counterwitnesses establishes minimality. Combined with Step 1, the theorem follows.

## Verification

Use Python 3.9+ and any C++17 compiler supporting `g++ -std=c++17 -O3`. Run `sh run_checks.sh` from the directory containing the embedded artifacts. The reproducible outputs are provided as `verify_paley89.stdout.txt` and `verify_paley89_direct.stdout.txt`. The Python program reports all thirteen failures and `q=89 ... four_ec=True pair_orbits=7482`. The C++ program reports `PASS exhaustive-89 all-four-subsets=2441626 min-pattern-count=16`. A run-time measurement in the C++ output is informational and platform-dependent. The certificate is a complete finite determination, so it does not infer untested larger orders.

## Relationship to prior work

Blass, Exoo and Harary established that sufficiently large Paley graphs satisfy first-order adjacency axioms. Ananchuen and Caccetta studied Paley adjacency properties; their 1993 Networks article and its relevant thesis treatment were identified, but their complete text could not be examined in this comparison. Bonato, Holzmann and Kharaghani investigated the 3-e.c. property and explicitly discussed Paley graphs as known 4-e.c. examples; their accessible article does not give the first Paley 4-e.c. order. Elsawy's 2012 exposition describes the finite-field Paley construction and n-e.c. literature without an exact 89-order threshold. A later publicly available analysis provides the sufficient *prime-order* bound \(p\ge193\) for 4-e.c. Paley graphs and explicitly says that bound is not sharp. The present result determines the least parameter over **all prime powers** and links it to the exact rank-five theory of the Rado graph. The EF equivalence itself is elementary and is not claimed as a new theorem independently of this classification.

## Limitations

Historical priority has not been conclusively settled, especially for the 1993 Networks article and thesis chapter on Paley adjacency properties, which were not available in complete readable form. The result establishes a family-specific first order, not the minimum size of an arbitrary 4-e.c. graph, and says nothing about 4-e.c. for every larger Paley order. Although exact enumeration gives a finite complete proof, it is not an independent formal proof assistant certification. Independent mathematical audit is not part of this result.

## References

1. A. Blass, G. Exoo, F. Harary, *Paley graphs satisfy all first-order adjacency axioms*, J. Graph Theory **5** (1981), 435–439. https://doi.org/10.1002/jgt.3190050414
2. W. Ananchuen and L. Caccetta, *On the adjacency properties of Paley graphs*, Networks **23** (1993), 227–236. https://doi.org/10.1002/net.3230230404
3. A. Bonato, W. H. Holzmann, H. Kharaghani, *Hadamard matrices and strongly regular graphs with the 3-e.c. adjacency property*, Electron. J. Combin. **8** (2001), R1. https://math.ryerson.ca/~abonato/papers/3echw2.pdf
4. A. Elsawy, *Paley Graphs and Their Generalizations*, arXiv:1203.1818v1, posted 2012-03-07. https://arxiv.org/abs/1203.1818
5. *4-existentially closed graphs are super geometric dominant*, publicly released result (2026), https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-four-existential-closure-super-geometric-dominance--424c9dd4cac4
