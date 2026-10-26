# Rigidity and orbit growth for power semigroups of finite matrix units

## Finding

For every integer \(n\geq 2\), let \(I=\{1,\ldots,n\}\) and let \(B_n^0=\{0\}\sqcup(I\times I)\) be the semigroup of matrix units, with \(0\) absorbing and
\[
(i,j)(k,l)=\begin{cases}(i,l),&j=k,\\0,&j\ne k.\end{cases}
\]
Let \(\mathcal P_+(B_n^0)\) denote all **nonempty** subsets, multiplied setwise. Every automorphism of \(\mathcal P_+(B_n^0)\) is induced by one and only one permutation \(\sigma\in S_n\), acting on all its subsets by
\[
0\longmapsto0,\qquad (i,j)\longmapsto(\sigma(i),\sigma(j)).
\]
Thus \(\operatorname{Aut}(\mathcal P_+(B_n^0))\cong S_n\), of order \(n!\). The same proof applies to arbitrary index sets with at least two elements, giving their full symmetric groups.

For a permutation \(\sigma\in S_n\), let \(\lambda(\sigma)\) be the multiset of its cycle lengths and put
\[
c(\sigma)=\sum_{a,b\in\lambda(\sigma)}\gcd(a,b),
\]
where this is a sum over ordered pairs of cycles, including repeated cycle lengths as distinct entries. The exact number of automorphism orbits on the elements of the power semigroup is
\[
\boxed{\mathcal O_n=\frac{2}{n!}\sum_{\sigma\in S_n}2^{c(\sigma)}-1}.
\]
In particular,
\[
\mathcal O_2=19,\quad \mathcal O_3=207,\quad \mathcal O_4=6087,\quad
\mathcal O_5=583935,\quad \mathcal O_6=193857983.
\]
As \(n\to\infty\),
\[
\boxed{\mathcal O_n\sim \frac{2^{n^2+1}}{n!}}.
\]

## Assumptions and scope

All sets in the base semigroup are finite because \(n\) is finite; the empty subset is **not** an element of the power semigroup. The element \(0\) is a genuine absorbing element of the base semigroup, not the empty relation. No additional union operation is required or preserved by the automorphisms. We work with semigroup automorphisms under setwise multiplication alone, not automorphisms of power graphs or Boolean relation algebras. The structural group conclusion holds for any index set \(I\) with \(|I|\ge2\), with the same argument and all subsets, but the finite orbit formula and asymptotic require finite \(n\).

## Proof

**1. A characteristic copy of the full binary-relation semigroup.** Put
\[
E=\{0\}\cup\{(i,i):i\in I\}\in\mathcal P_+(B_I^0).
\]
For any nonempty \(X\subseteq B_I^0\), elementary matrix-unit multiplication gives
\[
EX=XE=X\cup\{0\}.
\]
In particular, \(E^2=E\), and \(E\) is central in the power semigroup. The singleton \(\{0\}\) is an absorbing central idempotent.

These are the **only central idempotents** for \(|I|\ge2\). Indeed, let \(C\) be central. If \((u,v)\in C\) with \(u\ne v\), multiplying \(C\) by the singleton \(\{(x,u)\}\) on either side gives a contradiction: the left product contains \((x,v)\), whereas every nonzero element of the right product has second coordinate \(u\). Hence \(C\subseteq\{0\}\cup\{(i,i):i\in I\}\). Let \(K\subseteq I\) be the diagonal support of \(C\). Commuting with every singleton \(\{(i,j)\}\) forces \(i\in K\) if and only if \(j\in K\), so \(K\) is empty or all of \(I\). With empty support, nonemptiness forces \(C=\{0\}\). With full support, \(C\) is either \(E\) or the diagonal set \(D=E\setminus\{0\}\). But \(D^2=E\ne D\) when \(|I|\ge2\). This proves the assertion.

The absorbing singleton \(\{0\}\) is fixed by every automorphism. Since \(E\) is the unique other central idempotent, it is also fixed. Therefore its image under left multiplication,
\[
\mathscr Z=E\mathcal P_+(B_I^0)
=\{X\subseteq B_I^0:0\in X\},
\]
is characteristic. Removing the zero symbol identifies \(\mathscr Z\) with the **full semigroup of binary relations** \(\mathscr R(I)=\mathcal P(I\times I)\), including the empty relation. Under this identification, setwise multiplication becomes ordinary relation composition, \(\{0\}\) becomes the empty relation, and \(E\) becomes the identity diagonal relation.

**2. A self-contained automorphism lemma for binary relations.** We establish that every semigroup automorphism \(F\) of \(\mathscr R(I)\) is simultaneous relabeling of row and column indices by one permutation. This is also the classical theorem of Magill [2], and the argument below supplies the version needed here.

A nonempty relation is a *rectangle* when it has the form \(A\times B\) with nonempty \(A,B\subseteq I\). If \(e=\{(a,b)\}\) is any one-edge relation, every \(UeV\) is either empty or a rectangle, while each nonempty rectangle can be obtained as such a product. Conversely, every nonempty relation contains some edge \((i,j)\), so sandwiching that relation between suitable one-edge relations yields a one-edge relation. Consequently, the nonempty rectangles form precisely the least nonzero Green \(\mathscr J\)-class of \(\mathscr R(I)\). This class is intrinsic and preserved by \(F\).

For a rectangle \(A\times B\), its principal right ideal consists of the empty relation and all nonempty rectangles with left support \(A\). Its principal left ideal analogously determines \(B\). Green's \(\mathscr R\)- and \(\mathscr L\)-relations therefore imply that \(F\) induces bijections \(f,g\) of the nonempty subsets of \(I\) such that
\[
F(A\times B)=f(A)\times g(B).
\]
The product rule
\[
(A\times B)(C\times D)=
\begin{cases}A\times D,&B\cap C\ne\varnothing,\\\varnothing,&B\cap C=\varnothing\end{cases}
\]
shows that \(B\cap C\ne\varnothing\) exactly when \(g(B)\cap f(C)\ne\varnothing\). On nonempty subsets, inclusion is characterized by intersection neighborhoods: \(C\subseteq D\) precisely when every nonempty set meeting \(C\) also meets \(D\). Thus \(f\) and \(g\) are order automorphisms of the nonempty Boolean subset poset. They must come from permutations \(\sigma,\tau\in\operatorname{Sym}(I)\), because they preserve singleton atoms and their unions. Intersection incidence of singleton sets forces \(\sigma=\tau\).

After composing \(F\) with the inverse of simultaneous index relabeling, assume every rectangle, hence every one-edge relation, is fixed. For any relation \(Q\) and indices \(a,b,i,j\), the sandwich
\[
\{(a,i)\}\,Q\,\{(j,b)\}
=\begin{cases}\{(a,b)\},&(i,j)\in Q,\\\varnothing,&(i,j)\notin Q\end{cases}
\]
recovers membership of each edge of \(Q\). Both possible outputs and both singleton factors are fixed. It follows that \(F(Q)=Q\) for every \(Q\). The lemma follows without an unproved rigidity assumption.

**3. No hidden lift automorphisms.** By Steps 1 and 2, any automorphism \(\Phi\) of the power semigroup acts on \(\mathscr Z\) by one simultaneous index permutation \(\sigma\). That permutation extends to an automorphism of the full power semigroup. Compose \(\Phi\) with its inverse, so that \(\Phi\) fixes \(\mathscr Z\) pointwise.

For each nonempty \(X\), applying \(\Phi\) to \(EX=X\cup\{0\}\) yields
\[
E\Phi(X)=\Phi(EX)=EX.
\]
Hence \(\Phi(X)\cup\{0\}=X\cup\{0\}\). If \(0\in X\), then \(X\in\mathscr Z\) is already fixed. If \(0\notin X\), then \(\Phi(X)\) is either \(X\) or \(X\cup\{0\}\). The latter is itself fixed, so injectivity of \(\Phi\) excludes it. Thus every \(X\) is fixed. Faithfulness of the index action completes the automorphism classification.

**4. Exact orbits.** A permutation \(\sigma\in S_n\) with cycle lengths \(a\) and \(b\) acts diagonally on the corresponding \(a\times b\) block of ordered pairs with exactly \(\gcd(a,b)\) orbits. Thus \(c(\sigma)\) counts its orbits on all \(n^2\) nonzero matrix units. Precisely \(2^{c(\sigma)}\) relations are fixed; independently choosing whether the base zero element belongs to a subset gives twice this number. Removing the empty subset leaves \(2^{c(\sigma)+1}-1\) fixed **nonempty** subsets. Burnside's lemma yields the displayed formula.

For the asymptotic, let \(\sigma\ne1\) move exactly \(k\ge2\) indices and fix \(f=n-k\). There are at most \(f^2\) orbits of fixed-fixed pairs, at most \(fk\) of fixed-moved and moved-fixed pairs combined, and at most \(k^2/2\) of moved-moved pairs (each such orbit has size at least two). Hence
\[
c(\sigma)\le f^2+fk+k^2/2=n^2-nk+k^2/2\le n^2-nk/2.
\]
At most \(n^k\) permutations move exactly \(k\) indices. Therefore the nonidentity terms, divided by \(2^{n^2}\), are at most
\[
\sum_{k=2}^{n}n^k2^{-nk/2}=o(1).
\]
The identity term dominates the Burnside sum, and the claimed asymptotic follows.

## Verification

The accompanying standalone `verify.py` reconstructs the multiplication of the base semigroup and its power semigroup directly from bitsets. It exhaustively checks central idempotents among all 31 nonempty subsets for \(n=2\) and all 1023 nonempty subsets for \(n=3\), checks the intrinsic zero-adjoining identity on every subset, and verifies the membership sandwiches. It verifies each of the two index permutations on all product pairs when \(n=2\), and tests 2500 reproducibly sampled product pairs for each of the six index permutations when \(n=3\).

Independently, the script computes Burnside sums for \(2\le n\le6\) and directly enumerates permutation orbits on all elements for \(n=2,3\). It reports `VERIFY_OK` and `ORBIT_OK`. The general automorphism theorem and asymptotic are proved above for arbitrary sizes in their stated ranges; the finite checks are corroboration, not substitutes for proof.

## Relationship to prior work

Tringali and Wen [1] investigate automorphisms of large power semigroups of numerical semigroups, establishing rigidity in a very different commutative cancellative setting. The present result determines an automorphism group and full orbit census for a natural noncommutative, noncancellative, inverse zero-simple family. Magill's theorem [2] already classifies automorphisms of the **full semigroup of binary relations**; Step 2 explicitly acknowledges and re-proves it, while the central-idempotent construction in Steps 1 and 3 is the additional issue for the nonempty power semigroup. Tamura [3] studies isomorphisms of power semigroups of general completely zero-simple semigroups, a highly relevant possible source of overlap. Its full text was not available for a decisive comparison; the present automorphism-group identification could conceivably be recoverable from results there. The orbit-counting and asymptotic assertions are also included explicitly for separate comparison. The 2025 work of Yang and collaborators [4] treats **power graphs**, which are different from power semigroups and do not imply this theorem. No absolute novelty claim is made.

## Limitations

The result is restricted to the trivial-group (matrix-unit) Brandt family, with \(n\ge2\). It makes no claim about Brandt semigroups over nontrivial groups or arbitrary Rees zero-matrix semigroups. The orbit asymptotic uses finite indices and has no infinite analogue stated here. Tamura's 1986 treatment is an unresolved bibliographic overlap risk; it should be checked in full before claiming historical priority. The cited Magill relation-semigroup theorem is not novel here.

## References

[1] S. Tringali and K. Wen, *On the automorphisms of the power semigroups of a numerical semigroup*, arXiv:2604.26901, initially posted 2026-04-29; *Trans. London Math. Soc.* 13 (2026), e70030, DOI 10.1112/tlm3.70030.

[2] K. D. Magill Jr., *Automorphisms of the semigroup of all relations on a set*, *Canadian Mathematical Bulletin* 9 (1966), 73–77, DOI 10.4153/CMB-1966-009-7.

[3] T. Tamura, *Isomorphism problem of power semigroups of completely zero-simple semigroups*, *Journal of Algebra* 98 (1986), 319–361, DOI 10.1016/0021-8693(86)90002-5.

[4] B. Yang, Y. Cheng, L. Zeng and Y. Shao, *Power graphs of Brandt semigroups*, *AKCE International Journal of Graphs and Combinatorics* 22 (2025), 350–353, DOI 10.1080/09728600.2025.2553326.
