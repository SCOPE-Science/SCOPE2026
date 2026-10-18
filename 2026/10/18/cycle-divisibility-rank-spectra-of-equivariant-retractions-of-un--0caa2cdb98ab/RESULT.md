# Cycle-divisibility rank spectra of equivariant retractions of uniform partitions

## Finding

Let \(n,m\ge2\), let \(X=[m]\times[n]\), and let \(W_{n,m}\) be the monoid of maps \(F:X\to X\) which map every block \(\{i\}\times[n]\) into a single block. Fix \(\sigma\in S_m\); its block permutation \(U_\sigma\) acts by \(U_\sigma(i,x)=(\sigma(i),x)\). If the distinct cycles of \(\sigma\) are indexed by \([t]\) and have lengths \(\ell_1,\ldots,\ell_t\), then the complete image-rank polynomial of idempotents commuting with \(U_\sigma\) is

\[
P_{n,\sigma}(z)=\sum_{\substack{F\in W_{n,m}\\F^2=F,\ FU_\sigma=U_\sigma F}}z^{|\operatorname{im}F|}
=\sum_{\varnothing\ne J\subseteq[t]}\ \sum_{(r_j)_{j\in J}\in[n]^J}
\left(\prod_{j\in J}\binom n{r_j}r_j^{n-r_j}z^{\ell_jr_j}\right)
\prod_{i\notin J}\left(\sum_{\substack{j\in J\\\ell_j\mid\ell_i}}\ell_jr_j^n\right).
\]

An empty inner sum is zero and an empty product is one. In particular, the exact set of attainable positive image ranks consists of the numbers \(\sum_{j\in J}\ell_jr_j\) for nonempty \(J\subseteq[t]\), \(1\le r_j\le n\), such that every \(i\notin J\) admits \(j\in J\) with \(\ell_j\mid\ell_i\).

Write \(c_d\) for the number of cycles of length \(d\), and let \(\mathcal D\) be the set of occurring cycle lengths minimal in the divisibility order. The least attainable image rank and its exact multiplicity are

\[
\rho_{\min}=\sum_{d\in\mathcal D}d,
\qquad
[z^{\rho_{\min}}]P_{n,\sigma}(z)
=n^{|\mathcal D|}
\left(\prod_{d\in\mathcal D}c_d d^{c_d-1}\right)
\left(\prod_{\substack{\ell:c_\ell>0\\\ell\notin\mathcal D}}
\left(\sum_{\substack{d\in\mathcal D\\d\mid\ell}}d\right)^{c_\ell}\right).
\]

For example, when \(n=2\) and the block permutation on three blocks swaps two blocks and fixes one, the rank polynomial is

\[
2z+4z^2+4z^3+2z^4+2z^5+z^6,
\]

so there are exactly \(15\) commuting idempotents, whereas there are \(189\) idempotents without the commuting restriction. If the three blocks instead form one cycle, the polynomial is \(2z^3+z^6\).

## Assumptions and scope

Throughout, \([a]=\{1,\ldots,a\}\). Every element of \(W_{n,m}\) has a unique representation

\[
F(i,x)=(g(i),f_i(x)),\qquad
 g:[m]\to[m],\quad f_i:[n]\to[n].
\]

Here \(F^2\) and \(FU_\sigma\) denote compositions of maps. The exponent in \(P_{n,\sigma}\) is the cardinality of the image in \(X\), not the rank of the induced map \(g\) on blocks. All finite sets and their blocks are labeled. The specified block action \(U_\sigma\) permutes the blocks without changing the within-block coordinates. No assertion is made about units that also permute coordinates within individual blocks.

## Proof

**1. Symmetry reduction.** Direct comparison of the two compositions gives

\[
FU_\sigma=U_\sigma F
\quad\Longleftrightarrow\quad
 g\sigma=\sigma g\quad\text{and}\quad f_{\sigma(i)}=f_i\ (i\in[m]).
\]

Thus each orbit \(C_i\) of \(\sigma\) supports exactly one local map. Applying the idempotence equation to \((i,x)\) gives

\[
F^2=F\quad\Longleftrightarrow\quad
g^2=g\quad\text{and}\quad f_{g(i)}\circ f_i=f_i\ (i\in[m]).
\]

**2. Which cycles can be retained?** Let \(J\) index the cycles of \(\sigma\) pointwise fixed by \(g\). Since \(g^2=g\), \(\operatorname{im}(g)=\operatorname{Fix}(g)\), hence \(J\ne\varnothing\). Commutation with \(\sigma\) forces the fixed set to be a union of complete cycles. Each omitted source cycle \(C_i\) is sent equivariantly into a retained cycle \(C_j\), which is possible exactly when \(\ell_j\mid\ell_i\). After choosing starting points in the source cycle, the map has exactly \(\ell_j\) possible phases, and these determine distinct functions. Choices on different omitted cycles are independent.

**3. Local idempotents and their tails.** For \(j\in J\), the shared local map \(h_j=f_i\) on \(C_j\) satisfies \(h_j^2=h_j\). If its image \(S_j\subseteq[n]\) has cardinality \(r_j\), it is the identity on \(S_j\) and sends every other element of \([n]\) to an arbitrary point of \(S_j\). Its number of choices is therefore \(\binom n{r_j}r_j^{n-r_j}\). For an omitted cycle \(C_i\) whose block map targets \(C_j\), its shared local map has to satisfy \(h_j\circ f_i=f_i\), equivalently \(\operatorname{im}(f_i)\subseteq S_j\); there are \(r_j^n\) possibilities. A retained cycle contributes exactly \(\ell_jr_j\) points to \(\operatorname{im}(F)\), and omitted cycles contribute no new points. Hence its image size is \(\sum_{j\in J}\ell_jr_j\).

The choices of \(J\), the local idempotents, and each omitted cycle's target, phase, and local function are unique and mutually independent. Multiplying their counts and summing over all admissible choices proves the asserted polynomial and its exact support.

**4. Least image and leading coefficient at that end.** Let \(\mathcal D\) be the distinct lengths that have no strictly smaller occurring divisor. For a cycle of any \(d\in\mathcal D\), the absence of a smaller target forces at least one entire cycle of that length into the fixed set of \(g\). Therefore \(\operatorname{rank}(F)\ge\sum_{d\in\mathcal D}d\). Conversely, select one representative cycle for each minimal length, map every other cycle to a selected representative of a length dividing its own, and take rank-one local idempotents on the retained cycles. Such a divisor exists by finite descent in the divisibility order. This realizes the bound.

Attaining equality forces exactly one fixed cycle for each minimal length, every fixed local idempotent of rank one, and no other fixed cycles. For each \(d\in\mathcal D\) there are \(c_d\) choices of that cycle, \(n\) choices of its constant image, and \(d\) possible phases for every one of its other \(c_d-1\) cycles. Each cycle of any other occurring length \(\ell\) has \(\sum_{d\in\mathcal D,\ d\mid\ell}d\) choices of target and phase; all its local functions are forced once the target's singleton image is chosen. Multiplication gives the displayed minimum-rank coefficient.

## Verification

The companion source `check.py` enumerates actual full transformations of \(X\) without assuming the structure used in the proof. It directly tests \(F^2=F\), the relation \(FU_\sigma=U_\sigma F\), and the image size, and compares every coefficient with an independent implementation of the closed polynomial. It also checks the least attainable rank and its coefficient against a separate divisor-poset formula. The tests cover \(15\) finite cases with \(n\in\{2,3\}\), \(m\le4\), and representative cycle types including fixed points, transpositions, double transpositions, and full cycles. The output terminates with `ALL_EXACT_CHECKS_PASSED 15`.

These finite tests check the implementation and boundary cases. The unrestricted theorem for arbitrary \(n,m\) follows from the combinatorial proof above, not from finite enumeration.

## Relationship to prior work

Dolinka and East, Proposition 3.1 and Proposition 3.2, give the idempotent criterion and total number in the uniform-partition endomorphism monoid without a centralizing-permutation restriction. Al-Aadhami's deposited thesis, Section 4.3.2 and Theorem 4.3.4, gives the general total-idempotent census for monoid wreath products. Konieczny's Theorem 1 characterizes maps commuting with a permutation in a full transformation monoid via divisibility of source and target cycle lengths. These are important pre-existing ingredients and are not claimed as discoveries here.

The assertion assessed here is the **complete cardinality-of-image generating polynomial** for the *intersection* of the uniform-partition endomorphism monoid's idempotents with the centralizer of a specified coordinate-preserving block permutation, together with its exact least-rank coefficient. Neither the unsymmetrized enumeration, the full-transformation centralizer description, nor the abstract idempotent criterion by itself states this two-layer rank-weighted enumeration. Bernhardt and collaborators' centralizer theorem concerns wreath products of groups, not this noninvertible transformation wreath monoid. The case of singleton blocks reduces to classical permutation-equivariant transformations and is not presented as a new classification.

## Limitations

The result concerns a fixed, coordinate-preserving permutation of blocks, not arbitrary elements of the wreath-product unit group. It gives ranks and multiplicities, not the Green-class structure or a complete description of multiplication in the centralizer. The proof is self-contained conditional on the standard finite-set model. An equivalent enumerator under different terminology in older centralizer or semigroup literature has not been excluded by an exhaustive bibliographic search. The historical characterization of equivariant cycle maps and the unweighted total-idempotent formula are explicitly acknowledged as prior coverage. No independent mathematical audit has been performed.

## References

1. A. D. H. Al-Aadhami, *Combinatorial Questions for a Wreath Product of a Semigroup with a Full Transformation Monoid*, University of York PhD thesis (2017), publicly deposited 2018-02-26; especially Section 4.3.2 and Theorem 4.3.4. https://etheses.whiterose.ac.uk/id/eprint/19494/
2. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312, especially Propositions 3.1–3.2. https://arxiv.org/html/1407.3312v2
3. J. Konieczny, *Regular, inverse, and completely regular centralizers of permutations*, Mathematica Bohemica 128 (2003), 179–186, especially Theorem 1. https://emis.dsd.sztaki.hu/journals/MB/128.2/mb128_2_6.pdf
4. J. Araújo and J. Konieczny, *Centralizers in the Full Transformation Semigroup*, general centralizer structure. https://repositorioaberto.uab.pt/server/api/core/bitstreams/e1505ef6-df71-4791-a964-cd83058b4fc9/content
5. F. Bernhardt, A. C. Niemeyer, M. Rober, and L. Wollenhaupt, *Conjugacy classes and centralisers in wreath products*, arXiv:2107.04645, group-wreath-product setting. https://arxiv.org/html/2107.04645v2
