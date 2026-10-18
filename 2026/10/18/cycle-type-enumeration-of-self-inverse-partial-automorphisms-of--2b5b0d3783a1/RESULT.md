# Cycle-type enumeration of self-inverse partial automorphisms of finite fences

## Finding

Let \(F_n\) be the alternating fence on \([n]=\{1,\ldots,n\}\), with \(1\prec2\succ3\prec4\succ\cdots\), and let \(\mathcal I(F_n)\) be its inverse monoid of partial automorphisms: bijections between induced subposets that preserve and reflect order. An element \(\alpha\) is **self-inverse** if \(\alpha=\alpha^{-1}\). Write \(f(\alpha)\) for its number of fixed points and \(t(\alpha)\) for its number of two-cycles on its domain; its rank is \(f(\alpha)+2t(\alpha)\).

For \(S\subseteq[n]\), partition \(S\) into maximal runs of consecutive integers. Give each run a **type** \(\tau\): a run of length one has type \((1,*)\); a run of even length \(\ell\ge2\) has type \((\ell,*)\); and a run of odd length \(\ell\ge3\) has type \((\ell,\mathrm{min})\) if its initial vertex is odd and type \((\ell,\mathrm{max})\) if its initial vertex is even. Let \(m_\tau(S)\) be the multiplicity of type \(\tau\), and let \(\ell_\tau\) be its length. Put

\[
g_\tau=\begin{cases}2,&\ell_\tau\ge3\text{ odd},\\1,&\text{otherwise},\end{cases}\qquad
B_\tau(U,V)=\begin{cases}U^{\ell_\tau}+UV^{(\ell_\tau-1)/2},&g_\tau=2,\\U^{\ell_\tau},&g_\tau=1.\end{cases}
\]

Define for every integer \(m\ge0\)
\[
W_{\tau,m}(U,V)=\sum_{j=0}^{\lfloor m/2\rfloor}
\frac{m!\,g_\tau^j}{2^j j!(m-2j)!}\,
V^{\ell_\tau j}\,B_\tau(U,V)^{m-2j}.
\]

**Theorem (all \(n\ge1\)).** The complete cycle-type polynomial of the self-inverse elements is
\[
\boxed{\mathscr I_n(U,V)=
\sum_{S\subseteq[n]}\prod_{\tau:m_\tau(S)>0}
W_{\tau,m_\tau(S)}(U,V).}
\]
Here \([U^aV^b]\mathscr I_n\) is *exactly* the number of self-inverse partial automorphisms with \(a\) fixed points and \(b\) two-cycles. In particular, \(\mathscr I_n(Z,Z^2)\) is the rank enumerator, and \(\mathscr I_n(1,1)\) is the total count. The theorem involves no unknown automorphism-group orders, and applies uniformly to both parities of \(n\).

A closed high-rank consequence is
\[
[Z^{n-1}]\mathscr I_n(Z,Z^2)=
\begin{cases}
2n-2,&n\ge2\text{ even},\\
(5n-9)/2,&n\ge5,\ n\equiv1\pmod4,\\
(5n-7)/2,&n\ge3,\ n\equiv3\pmod4.
\end{cases}
\]
The full-rank contribution is \(U^n\) when \(n\) is even, and \(U^n+UV^{(n-1)/2}\) when \(n\ge3\) is odd. At rank two, for all \(n\ge2\), exactly \((n-1)^2\) self-inverse elements occur.

For illustration, the rank vectors (coefficients in ascending powers) at \(n=7,8,9\) are respectively
\[
(1,7,36,70,74,42,14,2),\quad
(1,8,49,122,175,132,59,14,1),\quad
(1,9,64,196,366,356,216,84,18,2).
\]
Their totals are \(246\), \(561\), and \(1312\).

## Assumptions and scope

No field or characteristic is involved. The fence is the poset with precisely the strict relations between consecutive integers, pointing from odd to even indices; the dual fence has the same self-inverse enumeration. A *partial automorphism* is an order isomorphism of the induced subposets on its domain and image, not merely an order-preserving injection. The empty partial map is included and contributes \(1\). The polynomial counts self-inverse elements, including partial identities, not only elements of exact order two in the ambient monoid. The displayed coefficient formulas are valid under their explicitly stated ranges.

## Proof

**1. Self-inverses are involutive automorphisms of induced subposets.** If \(\alpha=\alpha^{-1}\) as partial bijections, equality of domains implies \(\operatorname{dom}\alpha=\operatorname{im}\alpha=:S\), and \(\alpha^2=\operatorname{id}_S\). Conversely any order automorphism of \(F_n[S]\) whose square is the identity defines such an element. Thus it suffices to count involutions in \(\operatorname{Aut}(F_n[S])\), independently for every subset \(S\).

**2. The component-type lemma.** Comparable distinct points of \(F_n\) are consecutive, so the comparability graph of \(F_n[S]\) has as connected components exactly the maximal selected integer runs. A connected component of size \(\ell\ge2\) is an alternatingly oriented path. Any automorphism of such a component induces either the identity or reversal of the underlying path. If \(\ell\) is even, reversal interchanges the two height levels and is not an automorphism; components with opposite starting height are nevertheless order-isomorphic via reversal between them. If \(\ell\ge3\) is odd, the reversal preserves height and is a nontrivial automorphism; two odd components are isomorphic exactly when their starting heights agree, as their respective numbers of minima differ. Every singleton is one abstract type with trivial automorphism group. Therefore components are classified by the stated types and a component of type \(\tau\) has exactly \(g_\tau\) automorphisms, with \(g_\tau=2\) precisely for odd runs of length at least three.

**3. The involution factors.** An order automorphism of \(F_n[S]\) must permute components only within each type. For \(m\) components of one type \(\tau\), its group is the wreath product of \(m\) copies of the internal component group (trivial or \(C_2\)) by \(S_m\). An involution on these components induces an involution on the set of components, hence has \(j\) transposed component pairs and \(m-2j\) fixed components. The number of choices of the component matching is \(m!/[2^j j!(m-2j)!]\). For each paired component there are \(g_\tau\) possible isomorphisms one way, and the other is forced to be its inverse. All \(\ell_\tau\) vertices in each first component then participate in transpositions, contributing \(V^{\ell_\tau}\) per pair. On each fixed component, the allowed local involutions contribute \(U^{\ell_\tau}\) for the identity, and—only for odd \(\ell_\tau\ge3\)—\(UV^{(\ell_\tau-1)/2}\) for reversal. This proves \(W_{\tau,m}\). Distinct types do not interact. Multiplying and summing over domains \(S\) proves the boxed polynomial and its rank specialization.

**4. Near-full-rank and rank-two consequences.** Rank \(n-1\) means deleting exactly one vertex from the domain. Deleting an endpoint leaves one component of length \(n-1\); deleting an internal vertex leaves two components, and they may be exchanged exactly when their lengths and types agree. Applying the component-type lemma to the \(n\) deletion positions yields \(2n-2\) for even \(n\), \((5n-9)/2\) for \(n\equiv1\pmod4\) with \(n\ge5\), and \((5n-7)/2\) for \(n\equiv3\pmod4\) with \(n\ge3\). For clarity, in the odd case \(n=2m+1\), each of the two endpoint deletions contributes one; the \(m-1\) odd internal deletion positions contribute one apiece, except that the middle one contributes two when \(m\) is even; the \(m\) even positions normally contribute four except the two boundary internal positions contribute two, and the middle one contributes six when \(m\) is odd and \(m\ge3\). The small case \(n=3\) is directly \(4\). This simplifies to the displayed formulas. For rank two, an adjacent pair admits only the identity, whereas each nonadjacent pair admits the identity and its transposition, giving \((n-1)+2[\binom n2-(n-1)]=(n-1)^2\). Finally the entire fence has trivial automorphism group for even \(n\), and a two-element group generated by reversal for odd \(n\ge3\).

## Verification

The standalone `checker.py` implements the run-type expression with exact integer polynomial arithmetic and independently enumerates **all** partial permutations satisfying involutivity and the induced-order test for each \(1\le n\le8\). It compares every joint \((f,t)\) coefficient; this is a full finite check on those sizes, not an infinite proof. It also checks the near-top and rank-two formulas and displays exact rank vectors for \(n\le12\). Run `python3 checker.py` with a standard Python 3 interpreter; success prints `VERIFY_OK`. No external packages, downloads, precomputed tables or network access are used.

## Relationship to prior work

Koppitz and Musunthia (2019, arXiv:1903.10155), and Dimitrova and Koppitz (2021, arXiv:2111.14432), study generating sets, Green relations and ranks of fence partial-automorphism inverse semigroups. In particular, the latter identifies consecutive-run type as a Green-relation invariant. This structural backdrop is **not claimed as new**. The result above instead enumerates *self-inverse elements*, refining their individual cycle types across all ranks, and gives explicit near-full-rank coefficients.

Passararat and Koppitz (2025, DOI:10.12958/adm2353) characterize maximal subsemigroups and i-conjugacy of elements. Their conjugacy characterization is highly relevant but does not supply the displayed joint enumeration or the automorphism-fiber product formula in the inspected sections. General wreath-product involution counting is standard and is used transparently; novelty is claimed only for its exact fence-partial-automorphism specialization, joint enumerator, and coefficient consequences.

## Limitations

This is a finite, explicit subset-sum formula, not a claimed constant-state recurrence or a closed elementary expression for the total at every \(n\). The known Green/J classifications and standard wreath-product theory provide much of its structural infrastructure. The literature search cannot exclude an equivalent enumeration under alternative graph-automorphism, partial-symmetry, or subgroup cycle-index terminology. Independent mathematical validation has not been performed. Exhaustive computation through eight points verifies only those finite cases; the proof supplies the all-\(n\) argument.

## References

1. J. Koppitz and T. Musunthia, “The rank of the inverse semigroup of partial automorphisms on a finite fence,” arXiv:1903.10155, first posted 2019-03-25, https://arxiv.org/abs/1903.10155.
2. I. Dimitrova and J. Koppitz, “On the semigroup of all partial fence-preserving injections on a finite set,” arXiv:2111.14432, first posted 2021-11-29, https://arxiv.org/abs/2111.14432.
3. B. Passararat and J. Koppitz, “The inverse semigroup of all fence-preserving injections and its maximal subsemigroups,” Algebra and Discrete Mathematics 39 (2025), 225–242, DOI:10.12958/adm2353, https://admjournal.luguniv.edu.ua/index.php/adm/article/download/2353/pdf.
