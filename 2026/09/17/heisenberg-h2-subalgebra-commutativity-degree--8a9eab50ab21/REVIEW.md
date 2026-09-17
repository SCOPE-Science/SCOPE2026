# Review: exact subalgebra commutativity degree of the five-dimensional Heisenberg algebra

## Correctness

**PASS.** The proof reduces the Lie-algebra problem to symplectic incidence geometry in the quotient by the one-dimensional center. The classification used is direct: a subalgebra containing the center is the full inverse image of an arbitrary quotient subspace; a subalgebra disjoint from the center is the graph of a linear functional over a totally isotropic quotient subspace.

For two noncentral graphs, the key equivalence is checked explicitly: the center lies in their vector-space sum exactly when the two functionals disagree on the intersection of their quotient subspaces. If the center is absent from the sum, permutability is therefore equivalent to vanishing of the cross symplectic pairing. This gives the exact functional weight \(q^{r+s-t}\) for a fixed pair of isotropic subspaces.

In dimension four, the subsequent incidence counts are complete: every line is isotropic; the number of lines and Lagrangian planes is \((q+1)(q^2+1)\); a fixed line has \(q^3\) nonorthogonal lines and lies in \(q+1\) Lagrangians; and a fixed Lagrangian has \(q(q+1)\) distinct Lagrangians meeting it in a line and \(q^3\) transverse Lagrangians. Expanding the resulting nonpermutable-pair count gives the stated rational function.

As a separate finite check, `artifacts/verify_h2.py` exhaustively enumerates all subspaces and subalgebras over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\). It returns 158 subalgebras and 18,964 permutable ordered pairs for \(q=2\), and 693 subalgebras and 292,329 permutable ordered pairs for \(q=3\), exactly matching the formula. No division by 2 occurs in the proof, so characteristic two is covered.

## Originality

**PASS, to the best of our knowledge.** Muhie--Otera--Russo, arXiv:2609.19086v1, introduces the subalgebra commutativity degree for finite-dimensional Lie algebras, explicitly asks for values on Heisenberg algebras \(\mathfrak h(m)\), and gives an explicit formula for \(\mathfrak h(1)\) in Theorem 1.2. Inspection of the full v1 text found no \(\mathfrak h(2)\) computation.

Searches using the exact phrase “subalgebra commutativity degree,” rank-two/five-dimensional Heisenberg terminology, “permutable subalgebras,” and adjacent subgroup-commutativity terminology did not locate the displayed \(\mathfrak h(2)\) formula or an evidently stronger theorem implying it. Searches of the current SCOPE archive by Heisenberg terminology and commutativity-degree terminology also found no overlapping result.

Classical symplectic subspace counting and the general relation between Heisenberg algebras and isotropic subspaces are prior art and are not claimed as new. The novelty claim is restricted to the exact rank-two commutativity-degree computation, its explicit graph-pair criterion in this setting, and the prime-power extension of the rank-one expression.

The most relevant source not inspected in full was M. Tărnăuceanu, *The subgroup commutativity degree of finite P-groups*, DOI 10.1017/S0004972715000702. Its accessible title and abstract concern the group-theoretic subgroup commutativity degree and a different family; no exact extraspecial order-\(p^5\) formula is indicated there. It remains a residual originality risk only because class-two Lie algebras and groups are related by Lazard correspondence for suitable odd primes. More broadly, a specialized group-theoretic formula not surfaced by the searches could imply an odd-prime specialization. No concrete evidence of such coverage was found.

The motivating preprint is very recent, so contemporaneous independent work or a later revision remains an additional residual risk.

## Value

**PASS.** This resolves the first uncomputed Heisenberg rank immediately beyond the source paper's rank-one theorem, gives an exact rational function for every finite field rather than only a numerical example, and isolates a reusable symplectic criterion that converts higher-rank instances into finite incidence counts. The result also shows \(\operatorname{sd}(\mathfrak h(2,\mathbb F_q))\sim 3/q\), giving a clean asymptotic feature of the next rank.

Same-model review: passed. Cross-model review: not yet performed.
