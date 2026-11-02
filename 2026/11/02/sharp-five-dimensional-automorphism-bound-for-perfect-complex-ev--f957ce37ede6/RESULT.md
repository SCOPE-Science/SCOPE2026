# Sharp five-dimensional automorphism bound for perfect complex evolution algebras

## Finding

**Theorem.** Let \(E\) be any five-dimensional evolution algebra over \(\mathbb C\), with \(E^2=E\). Then
\[
 |\operatorname{Aut}_{\mathbb C}(E)|\le 155.
\]
Equality holds if and only if \(E\) is isomorphic to the cyclic evolution algebra \(C_5\) with natural basis \(e_0,\ldots,e_4\) satisfying \(e_i e_j=0\) for \(i\ne j\) and \(e_i^2=e_{i+1\bmod5}\). In this case
\[
 \operatorname{Aut}(C_5)\cong C_{31}\rtimes C_5,
 \qquad |\operatorname{Aut}(C_5)|=155.
\]
Moreover, every other such algebra satisfies the **sharp second bound** \(|\operatorname{Aut}(E)|\le126\). Equality \(126\) holds precisely for the direct sum \(C_2\oplus C_3\) of the corresponding directed-cycle evolution algebras. Thus the first two possible maximal automorphism-group orders are \(155\) and \(126\), each realized by a unique complex-algebra isomorphism class.

This proves the dimension-five case of the conjectured maximum in Kaygorodov–Martín González–Viruel (2026, Conjecture 3), and the corresponding dimension-five case of their simple-algebra Conjecture 4. It does not prove either conjecture in arbitrary dimension.

## Assumptions and scope

An **evolution algebra** has a natural basis \(e_0,\ldots,e_{n-1}\) such that mixed basis products vanish and \(e_i^2=\sum_j a_{ij}e_j\). It is **perfect** if \(E^2=E\), equivalently \(A=(a_{ij})\) is nonsingular. Its directed support graph \(\Gamma\) has edge \(i\to j\) exactly when \(a_{ij}\ne0\); loops are permitted. For a loopless directed \(r\)-cycle, \(C_r\) denotes the evolution algebra with a coefficient \(1\) on each cycle edge; \(C_2\oplus C_3\) has dimension five. All automorphisms here are ordinary complex-linear algebra automorphisms, not group-scheme points over arbitrary rings. The field is \(\mathbb C\), so roots of unity of all orders are available and have their usual cardinalities.

## Proof

**1. Reduction to a graph-and-diagonal bound.** Invertibility of the structure matrix implies a nonzero determinant summand, hence at least one permutation \(\sigma\in S_5\) with \(a_{i,\sigma(i)}\ne0\) for all \(i\); this is a directed cycle cover of \(\Gamma\). Every automorphism of a perfect evolution algebra is monomial in any natural basis (Elduque–Labra; also Sriwongsa–Zou). Its permutation part belongs to \(\operatorname{Aut}(\Gamma)\). A diagonal map \(e_i\mapsto z_i e_i\) is an automorphism exactly when
\[
 z_j=z_i^2\quad\hbox{for every edge }i\to j\text{ of }\Gamma.
\]
Let \(D(\Gamma)\) denote this solution group. The kernel/image formula therefore gives
\[
 |\operatorname{Aut}(E)|\le |D(\Gamma)|\,|\operatorname{Aut}(\Gamma)|.\tag{1}
\]
Neither factor depends on the nonzero numerical edge weights. The right-hand side may overestimate the actual automorphism group, because not every graph permutation necessarily lifts.

**2. Exact finite representation of \(D(\Gamma)\).** Choose any cycle cover \(\sigma\). Suppose its cycle lengths are \(\ell_1,\ldots,\ell_s\), summing to five. On a cycle of length \(\ell\), the edge equations force a freely chosen initial \(t\) to satisfy \(t^{2^\ell-1}=1\); the successive vertex labels are \(t,t^2,t^4,\ldots,t^{2^{\ell-1}}\). Thus all diagonal solutions can be found by enumerating exactly
\[
 U(\sigma)=\prod_{c=1}^s(2^{\ell_c}-1)\le31
\]
root tuples and imposing the remaining edge equations. In particular, for any cycle cover this produces **every** solution exactly once. To use only integer arithmetic, put \(L=\operatorname{lcm}_c(2^{\ell_c}-1)\) and identify the roots on the \(c\)-th cycle with integer exponents
\[
 (L/(2^{\ell_c}-1))\,2^j u_c\pmod L,
 \quad 0\le u_c<2^{\ell_c}-1.
\]
An additional edge \(i\to j\) is satisfied exactly when the corresponding integer exponents obey \(b_j\equiv2b_i\pmod L\). The count of valid tuples is therefore \(|D(\Gamma)|\), with no numerical tolerance or approximation.

**3. Exhaustive five-vertex graph inequality.** Encode a directed graph with loops on the ordered vertices \(0,\ldots,4\) as a \(25\)-bit integer
\[
 m=\sum_{i,j=0}^4 [i\to j]2^{5i+j}\quad (0\le m<2^{25}).
\]
The supplied self-contained C++17 checker `verify.cpp` traverses every one of these \(33{,}554{,}432\) masks. It partitions them into orbits under all \(120\) simultaneous row-and-column vertex relabelings by marking every relabeling of each first unseen mask. For each orbit representative it enumerates all \(120\) candidate cycle covers, skipping those with none; it determines \(\operatorname{Aut}(\Gamma)\) by testing all \(120\) relabelings, and determines \(D(\Gamma)\) by the complete modular enumeration of Step 2 using the smallest available tuple set. The executable returns

```
n=5
labeled_graphs=33554432
unlabeled_graphs=291968
unlabeled_cycle_cover_graphs=199957
max_diagonal_times_graph_aut=155
max_representative_mask=1122820
max_representative_aut=5
unlabeled_graphs_attaining_upper_bound=1
second_highest_bound_126_mask=1122448
bound_120_graphs=3
bound_126_graphs=1
bound_155_graphs=1
VERIFY_OK
```

The \(155\)-representative has exactly the edges \(0\to2\to3\to1\to4\to0\), a single directed five-cycle. Its diagonal group has order \(31\) and its graph automorphism group order \(5\). The \(126\)-representative has exactly \(0\leftrightarrow4\) and \(1\to2\to3\to1\), a disjoint two- and three-cycle, with diagonal group order \(21\) and graph automorphism group order \(6\). The finite check proves (1) is at most \(126\) for all other graph supports and at most \(155\) for every admissible support. There is exactly one graph-isomorphism class realizing each of these two highest bounds. Since all \(25\)-bit masks are visited and all root tuples and permutations are enumerated, this is a finite exhaustive certificate rather than a sampled search.

**4. Attainment and uniqueness up to algebra isomorphism.** When all cycle-edge coefficients equal \(1\), every rotation of each directed cycle lifts to an algebra automorphism. Thus the first graph realizes \(31\cdot5=155\) automorphisms and the second realizes \((3\cdot7)(2\cdot3)=126\). Every choice of nonzero coefficients on a disjoint union of directed cycles can be normalized to coefficient \(1\) by rescaling the natural basis: writing \(e_i^2=a_i e_{\sigma(i)}\), choose nonzero \(t_i\) satisfying \(t_{\sigma(i)}=a_i t_i^2\). On each cycle the only compatibility constraint has the form \(t^{2^\ell-1}=c\) for some \(c\ne0\), which is soluble over \(\mathbb C\). Hence every algebra with either extremal support is isomorphic to the corresponding unweighted cycle algebra. Conversely, Step 3 rules out the respective extremal order for any other support. This completes both classifications. The five-cycle is strongly connected and perfect, hence its algebra is simple by the standard graph criterion; the same bound therefore gives the claimed simple-algebra corollary.

## Verification

Compile and execute using a C++17 compiler:

```
g++ -std=c++17 -O3 -DNDEBUG verify.cpp -o verify
./verify
./verify 1122820
./verify 1122448
python crosscheck.py ./verify  # optional; requires SymPy
```

No external database, downloaded paper, external program, or floating-point operation is needed to reproduce the exhaustive certificate. The optional independent `crosscheck.py` uses SymPy to compute integral Hermite-normal-form lattice indices \(|D(\Gamma)|\) on a deterministic sample of \(305\) support graphs, checks graph automorphisms separately, and independently obtains \(291{,}968\) unlabeled directed loop-allowed graphs from Burnside's lemma. It returns `CROSSCHECK_OK`. GNU C++ and Clang produced the same exhaustive result; an address/undefined-behavior sanitizer run also completed normally. The proof of the reduction to finitely many graphs is mathematical; the final small-dimensional inequality relies on the fully enumerating program and its transparent integer-arithmetic logic.

## Relationship to prior work

Kaygorodov, Martín González and Viruel (2026) explicitly conjecture the maximum \(155\) in dimension five and state that their graph-computational bound had been checked only through dimension four (Conjectures 3 and 4). The present claim proves the next dimension, strengthens it to uniqueness and the sharp runner-up \(126\), and supplies a replayable complete certificate. Elduque and Labra (2019) give the monomial graph representation and diagonal/graph exact sequence used in Step 1. Sriwongsa and Zou (2022) classify maximizers of **the diagonal subgroup alone**, showing its maximum is \(2^n-1\), and analyze certain prescribed total automorphism groups. Neither result alone bounds the product \(|D(\Gamma)|\,|\operatorname{Aut}(\Gamma)|\) sharply for arbitrary five-vertex supports; this requires simultaneous finite support classification, performed here. The numerical target \(155\) itself is not claimed as newly conjectured.

## Limitations

The theorem is restricted to complex five-dimensional **perfect** evolution algebras. It is not asserted for non-perfect algebras, other base fields, group-scheme automorphisms, or any higher dimension. The universal inequality is computationally certified at exactly five vertices; an asymptotic bound does not follow. While the searched primary literature does not report this solved fifth-dimensional case, an unindexed or differently formulated earlier exhaustive census could exist. Independent external mathematical audit has not been performed.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15), especially Conjectures 3 and 4. https://arxiv.org/abs/2610.22248
2. A. Elduque, A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191v1 (2019), especially Section 3. https://arxiv.org/abs/1902.02191
3. S. Sriwongsa, Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333v2 (2022), especially Theorem 4.1. https://arxiv.org/abs/2202.01333
