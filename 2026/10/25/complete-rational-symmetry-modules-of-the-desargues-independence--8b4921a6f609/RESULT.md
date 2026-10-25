# Complete rational symmetry modules of the Desargues independence complex

## Finding

Let \(D=H(5,2)\) be the twenty-vertex bipartite Kneser graph: its vertices are the two-element and three-element subsets of \([5]\), adjacent precisely when one contains the other. Let \(X=\operatorname{Ind}(D)\) be the ordinary independence complex. The group \(S_5\times C_2\) acts on \(X\): permutations relabel \([5]\), and the generator \(c\) of \(C_2\) complements each subset in \([5]\).

Write \(\varepsilon\) for the nontrivial one-dimensional representation of \(C_2\), \(\operatorname{sgn}\) for the sign representation of \(S_5\), and \(\mathbb Q^{[5]}\) for the five-dimensional permutation representation. Then, as rational \(S_5\times C_2\)-modules,

\[
\widetilde H_4(X;\mathbb Q)\cong\operatorname{sgn}\boxtimes\varepsilon,
\qquad
\widetilde H_5(X;\mathbb Q)\cong\mathbb Q^{[5]}\boxtimes\varepsilon.
\]

All other reduced rational homology groups vanish. In particular, both nonzero homology groups are *anti-invariant* under complement. For \(\sigma\in S_5\) and \(t\in\{0,1\}\), the complete characters are

\[
\chi_4(\sigma,c^t)=(-1)^t\operatorname{sgn}(\sigma),
\qquad
\chi_5(\sigma,c^t)=(-1)^t\#\operatorname{Fix}_{[5]}(\sigma).
\]

Consequently, the quotient \(X/S_5\) has one-dimensional reduced rational homology in degree five and none elsewhere, whereas \(X/(S_5\times C_2)\) is rationally acyclic. These are rational homology statements, not assertions of contractibility.

## Assumptions and scope

All graphs are simple. The vertices of \(D\) are indexed first by lexicographically ordered two-subsets and then by lexicographically ordered three-subsets of \([5]\). A face is a set of graph vertices with no incidence edge. A face of cardinality \(k+1\) has dimension \(k\); its integral orientation is the increasing index order. A permutation \(\sigma\) acts by applying \(\sigma\) to the members of each subset; complement takes a subset \(A\) to \([5]\setminus A\). These operations commute, preserve graph adjacency, and induce simplicial actions.

This is a finite, rational representation theorem for this exact graph. The previously published *nonequivariant* integral homotopy equivalence \(X\simeq S^4\vee\bigvee^5 S^5\) is used as context and credited below; it is **not** the claimed new discovery.

## Proof

**1. Full simplex and boundary construction.** Enumerating all independent sets from the stated incidence relation yields the numbers of faces of cardinalities \(0,1,\ldots,10\):

```
1, 20, 160, 660, 1510, 1924, 1320, 480, 115, 20, 2
```

The enumeration comprises exactly 6,212 augmented faces, 6,211 nonempty. Exact boundary reduction over \(\mathbb F_2\), for differentials from simplicial dimensions \(1,\ldots,9\) to the dimension below, gives ranks

```
19, 141, 519, 991, 932, 383, 97, 18, 2
```

Thus reduced mod-two homology is one-dimensional in degree four and five-dimensional in degree five, and zero otherwise. All rational Betti numbers are at most the corresponding mod-two numbers: an integer boundary minor nonzero modulo two is nonzero over \(\mathbb Q\). The reduced Euler characteristic is \(-4\).

**2. A nonzero sign-isotypic rational fourth class.** For each simplex \(F\), let \([F]\) denote the oriented chain, and define its antisymmetrization under \(S_5\) by

\[
A[F]=\sum_{\sigma\in S_5}\operatorname{sgn}(\sigma)\,\sigma[F].
\]

For each simplex orbit, either this chain vanishes or it gives one sign-isotypic chain basis vector, unique up to nonzero scaling. With integral normalization to orbit coefficients in \(\{\pm1\}\), the nonzero sign-chain dimensions in degrees \(2,3,4,5,8,9\) are respectively

```
4, 20, 26, 9, 2, 2
```

All other sign-chain groups are zero. The exact *rational* boundary ranks in degrees \(3,4,5,9\) are \(4,16,9,2\) respectively. These ranks follow by Gaussian elimination on the actual signed boundary matrices, verifying every orbit coefficient; they are not inferred from characteristic-two ranks. Hence sign-isotypic homology is exactly one-dimensional in degree four and zero in every other degree.

The mod-two bounds from Step 1 give rational homology only possibly in degrees four and five, with dimensions at most one and five respectively. The sign submodule forces \(\beta_4=1\); the reduced Euler characteristic \(\beta_4-\beta_5=-4\) forces \(\beta_5=5\). Because \(\widetilde H_4\) is one-dimensional and contains the sign representation, it **is** the sign representation of \(S_5\).

**3. Complement on the fourth class.** Complement commutes with \(S_5\), and thus restricts to the sign-chain subcomplex. For its normalized orbit basis, the alternating trace of complement on the sign-chain complex is exactly \(-1\), computed by checking which simplex orbits are sent to themselves and tracking their orientation signs. By the Hopf trace formula and Step 2, sign-isotypic homology occurs only in degree four. Therefore complement acts on \(\widetilde H_4\) by the scalar \(-1\).

**4. The full fifth-homology character.** For a simplicial automorphism \(g\), evaluate its reduced Lefschetz number by

\[
\widetilde L(g)=-1+\sum_{\substack{\varnothing\ne F\in X\\gF=F}}
(-1)^{|F|-1}\operatorname{sgn}(g|_F),
\]

where the final sign is the orientation sign on the ordered vertices of \(F\). Direct exact evaluation for representatives of the seven conjugacy classes of \(S_5\), with and without complement, gives

\[
\widetilde L(\sigma,c^t)=(-1)^t\bigl(\operatorname{sgn}(\sigma)-f(\sigma)\bigr),
\]

where \(f(\sigma)=\#\operatorname{Fix}_{[5]}(\sigma)\). Indeed, for partitions of five in the order

```
(1,1,1,1,1), (1,1,1,2), (1,1,3), (1,2,2), (1,4), (2,3), (5)
```

the reduced Lefschetz values with no complement are

```
-4, -4, -1, 0, -2, -1, 1
```

and with complement are their negatives. By the Hopf trace formula, \(\widetilde L(g)=\chi_4(g)-\chi_5(g)\). Inserting Step 3 yields \(\chi_5(\sigma,c^t)=(-1)^t f(\sigma)\). The character \(f\) is exactly that of the permutation module on five letters. Rational representations of finite groups are determined by their character, proving the decomposition.

**5. Quotients.** For a finite simplicial group action, rational homology of the quotient agrees with invariant rational homology (use a barycentric subdivision and rational averaging). The sign representation has no \(S_5\)-invariants, while \(\mathbb Q^{[5]}\) has a unique invariant line. Complement acts by \(-1\) on both nonzero modules, so the full quotient has no reduced rational homology.

## Verification

The fully standalone Python 3 verifier at `verification/verify_desargues_character.py` constructs every graph edge, every independent face, the exact characteristic-two boundary ranks, every nonzero signed antisymmetrized orbit chain, the rational boundary ranks, and the fixed-simplex Lefschetz characters for the fourteen conjugacy-class configurations of \(S_5\times C_2\). It also checks that every purported permutation preserves adjacency, validates all sign-chain boundary coefficients on their entire orbit supports, and checks the complement sign-chain trace. It has no nonstandard Python dependencies. Run from the package root:

```
python3 verification/verify_desargues_character.py
```

Successful completion prints `DESARGUES_EQUIVARIANT_HOMOLOGY_VERIFIED`. This is an exact *finite* computation establishing the particular rational representation; no infinite family theorem is asserted.

## Relationship to prior work

Nilakantan and Shukla [1] classify independence-complex homotopy types of a specifically defined family of cyclic regular bipartite graphs, not the permutation-and-complement representations of the Desargues graph. Kumar, Singh, and Verma [2] study the linear strands and other commutative-algebra invariants of edge ideals of bipartite Kneser graphs, including the same underlying bipartite Kneser family. Their Betti numbers of edge-ideal resolutions are not homology characters of the entire independence complex. Antolín Camarena and Carnero Bravo [3] study nonequivariant independence homotopy types for categorical graph products, a different graph family.

Most importantly, the published calculation [4] already gives the exact nonequivariant homotopy type \(S^4\vee\bigvee^5S^5\) for *this identical graph* (called both the Desargues graph and \(H(5,2)\)). Its written claim and proof explicitly restrict to ordinary nonequivariant equivalences. A wedge of one four-sphere and five five-spheres does **not** determine the graph's group action: distinct one- and five-dimensional representations have the same Betti numbers. The result here is the complete **joint** \(S_5\times C_2\) homology representation, including complement parity and rational symmetry-quotient consequences. No priority claim is made beyond the checked sources.

## Limitations

The result concerns rational homology representations, not integral equivariant homotopy types or integral module lattices. The rationally acyclic full quotient need not be contractible. The finite calculation is exhaustive for this one graph, but does not classify the general bipartite Kneser family. Published work not indexed or inspected here could contain an equivalent computation; the literature check and calculations have not undergone independent mathematical audit.

## References

1. N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789v1 (first public 2017-09-14), https://arxiv.org/abs/1709.04789.
2. A. Kumar, P. Singh, and R. Verma, *Certain Homological Invariants of Bipartite Kneser Graphs*, arXiv:2105.06144v1 (first public 2021-05-13), https://arxiv.org/abs/2105.06144.
3. O. Antolín Camarena and R. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v1 (2023), https://arxiv.org/abs/2307.12401.
4. *The Desargues graph independence complex is \(S^4\vee\bigvee^5S^5\)*, published computational mathematics record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-desargues-graph-independence-complex-is-s-4-vee-bigvee-5-s-5--ca55f3b9deba.
