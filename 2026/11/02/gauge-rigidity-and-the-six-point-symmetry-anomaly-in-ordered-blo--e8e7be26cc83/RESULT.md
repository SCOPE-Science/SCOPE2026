# Gauge rigidity and the six-point symmetry anomaly in ordered-block inverse monoids

## Finding

Fix integers \(k,m\geq2\). Let \(\Omega\) be partitioned into \(k\) linearly ordered blocks \(B_1<\cdots<B_k\), each containing \(m\) points. Write \(M_{k,m}\) for the inverse monoid of partial bijections of \(\Omega\) whose domain and image are unions of complete blocks, which map each selected block bijectively onto a selected block, and whose induced partial injection on the block indices is increasing. This is the ordered-uniform-partition monoid studied in [1].

Choose identifications of each block with \(\{1,\ldots,m\}\), and let \(G=S_m\). Each nonzero element \(f\) is uniquely specified by increasing sequences \(i_1<\cdots<i_r\), \(j_1<\cdots<j_r\) and labels \(g_t\in G\), interpreted as the bijections \(B_{i_t}\to B_{j_t}\). The empty map has \(r=0\).

**Theorem.** Every monoid automorphism of \(M_{k,m}\) is given, uniquely, by the following data:

\[
\tau\in\{\mathrm{id},\rho\},\qquad \rho(i)=k+1-i,\qquad
\varphi\in\operatorname{Aut}(G),\qquad
(a_1,\ldots,a_k)\in G^k,\quad a_1=1.
\]

For every labeled arrow \((i,j,g)\) of an element, replace it by

\[
\bigl(\tau(i),\tau(j),\;a_{\tau(j)}\,\varphi(g)\,a_{\tau(i)}^{-1}\bigr),
\]

and sort the arrows by their new source indices. Multiplication of permutation labels is function composition, with the rightmost function acting first. The resulting transformation is a monoid automorphism, and all automorphisms occur exactly once in this form.

In particular,

\[
\bigl|\operatorname{Aut}(M_{k,m})\bigr|
=2(m!)^{k-1}\bigl|\operatorname{Aut}(S_m)\bigr|
=\begin{cases}
2^k,&m=2,\\
4(6!)^k,&m=6,\\
2(m!)^k,&m\geq3,\ m\neq6.
\end{cases}
\]

Call an automorphism *spatial* if it is induced by conjugation by a permutation of \(\Omega\). An automorphism in the displayed normal form is spatial precisely when \(\varphi\) is inner. Therefore **every automorphism is spatial when \(m\neq6\)**, while **exactly half are non-spatial when \(m=6\)**. The exceptional half comes from the unique nontrivial class in \(\operatorname{Out}(S_6)\) [3].

## Assumptions and scope

No characteristic, field, or asymptotic assumptions are involved. Both \(k\) and \(m\) are arbitrary integers at least two. A block is treated as an indivisible domain and image unit: individual points cannot be omitted from a selected block. A partial bijection need not fix its selected block indices. The relative block order is preserved, but its internal permutations are unrestricted. The theorem classifies abstract monoid automorphisms, rather than only conjugations by permutations of the underlying points.

The same arrow-groupoid argument identifies automorphisms for arbitrary finite group labels \(G\), with parameter count \(2|G|^{k-1}|\operatorname{Aut}(G)|\); the displayed theorem and six-point consequence concern the concrete transformation monoids with \(G=S_m\). The exceptional outer-automorphism classification of symmetric groups is a classical theorem [3], not part of the new proof.

## Proof

**1. Idempotents and atom permutations.** For each subset \(A\subseteq\{1,\ldots,k\}\), let \(e_A\) be the identity on the union of the blocks indexed by \(A\). These are exactly the idempotents, since an idempotent partial bijection is an identity on its domain. Their multiplication is \(e_Ae_C=e_{A\cap C}\), so the intrinsic idempotent semilattice is a Boolean lattice with \(k\) atoms \(e_{\{i\}}\). Every monoid automorphism consequently permutes these atoms, say via \(\tau\in S_k\).

**2. The atom permutation must be monotone or antitone.** The inverse of an element is characterized uniquely by the inverse-monoid equations, so every automorphism preserves the inverse operation and the natural order \(s\preceq t\) defined by \(s=et\) for some idempotent \(e\). For each ordered pair of indices \(i,j\) and label \(g\in G\), denote by \([i\to j;g]\) the rank-one-block element that is defined only on \(B_i\) and maps it to \(B_j\) with label \(g\). An automorphism sends it to \([\tau(i)\to\tau(j);g']\) for some \(g'\), because its source and range atomic idempotents are preserved.

Take any \(i<j\) and \(u<v\). The two elements \([i\to u;1]\) and \([j\to v;1]\) have a common upper bound in the natural order: their union is a block-order-preserving partial bijection. The corresponding images can have a common upper bound only if the relative ordering of \(\tau(i),\tau(j)\) agrees with the relative ordering of \(\tau(u),\tau(v)\); they have distinct source blocks and distinct target blocks, so no other compatibility obstruction is possible. Using the fixed source pair \((1,2)\) and varying \(u<v\), the sign of \(\tau(u)-\tau(v)\) must be constant. Thus \(\tau\) is either increasing, hence the identity, or decreasing, hence \(\rho(i)=k+1-i\). Conversely simultaneous reversal of source and target block orders preserves every increasing block bijection, giving a monoid automorphism. Compose an arbitrary automorphism with this reversal to reduce to the case that every atom is fixed.

**3. The rank-one groupoid forces a single label automorphism.** Assume the atoms are fixed. For every \(i,j\), there is a bijection \(F_{ij}:G\to G\) such that

\[
\Phi([i\to j;g])=[i\to j;F_{ij}(g)].
\]

The rank-one multiplication rule is, whenever the intermediate blocks match,

\[
[j\to\ell;h]\circ[i\to j;g]=[i\to\ell;hg].
\]

Therefore \(F_{i\ell}(hg)=F_{j\ell}(h)F_{ij}(g)\) for all indices and labels. In particular \(\varphi=F_{11}\) is a bijective group homomorphism \(G\to G\), hence belongs to \(\operatorname{Aut}(G)\). Set \(a_j=F_{1j}(1)\), so \(a_1=1\). Composing an identity-labeled arrow \(1\to i\) with its inverse forces \(F_{i1}(1)=a_i^{-1}\). Factoring an arbitrary labeled arrow as

\[
[i\to j;g]=[1\to j;1]\circ[1\to1;g]\circ[i\to1;1]
\]

then gives

\[
F_{ij}(g)=a_j\varphi(g)a_i^{-1}.
\]

This also proves uniqueness: \(\tau\) is recovered from atomic idempotents, \(\varphi\) from the maximal subgroup at the first atom after undoing reversal, and each \(a_j\) from the image of the identity-labeled arrow \(1\to j\).

**4. Reconstruction at every rank.** Every element is the least upper bound in the intrinsic natural order of the rank-one-block restrictions of its arrows; such an upper bound exists and is precisely their disjoint union. Hence images of the rank-one restrictions uniquely determine the image of every element. The formula in the theorem is therefore necessary. Conversely, choose any permitted \(\tau,\varphi,a_2,\ldots,a_k\). The formula is invertible, carries increasing disjoint arrow families to increasing disjoint arrow families, respects source/target matching, and preserves the rank-one composition rule by cancellation of \(a_{\tau(j)}^{-1}a_{\tau(j)}\) in each composable pair. General multiplication is the union of these matching rank-one composites. Thus the formula is a multiplicative bijection, so it is an automorphism. Parameter uniqueness proves the cardinality formula.

**5. Spatial criterion and exceptional count.** A permutation of \(\Omega\) inducing a monoid automorphism necessarily sends the supports of the atomic idempotents to such supports, so it permutes the complete blocks. By step 2, its induced block permutation is increasing or decreasing; its internal action on each block is a permutation in \(S_m\). In labeled coordinates such conjugations act as \(g\mapsto b_j g b_i^{-1}\), after block permutation, for suitable \(b_i\in S_m\). In the unique normalized parametrization, this means precisely that \(\varphi\) is inner; conversely any inner \(\varphi\) can be absorbed into the \(b_i\) to realize the automorphism spatially. Since \(S_2\) has trivial automorphism group, \(\operatorname{Aut}(S_m)=\operatorname{Inn}(S_m)\) for all \(m\ge3\), \(m\neq6\), and \(\operatorname{Out}(S_6)\cong C_2\) [3], the last conclusions follow. In particular, \(|\operatorname{Aut}(S_2)|=1\), \(|\operatorname{Aut}(S_6)|=1440\), and \(|\operatorname{Aut}(S_m)|=m!\) for \(m\ge3\), \(m\neq6\).

## Verification

The standalone program `verify.py` enumerates each element as a tuple of increasing labeled arrows, computes the monoid multiplication directly, independently builds all parameterized automorphisms, checks bijectivity and checks the homomorphism equation for **every pair of elements**. It passed all of the following cases:

- \((k,m)=(2,2)\): \(13\) elements, \(4\) distinct automorphisms, \(676\) multiplication equations checked.
- \((k,m)=(3,2)\): \(63\) elements, \(8\) distinct automorphisms, \(31{,}752\) multiplication equations checked.
- \((k,m)=(2,3)\): \(61\) elements, \(72\) distinct automorphisms, \(267{,}912\) multiplication equations checked.

Run `python3 verify.py` with standard Python 3. These checks support the explicit construction in small degrees; the unrestricted completeness and the \(m=6\) claim follow from the proof and the known symmetric-group automorphism theorem, not from finite enumeration.

## Relationship to prior work

Caneco, Fernandes and Quinteiro [1] explicitly define these ordered-uniform-partition inverse monoids and establish their ranks and finite presentations, including the \(2k\) rank formula. Their main results do not identify the abstract automorphism group. The present classification is an independent invariant beyond the published rank/presentation information; those earlier results are not claimed as new.

Araújo, Fernandes, Jesus, Maltcev and Mitchell [2] determine automorphism groups for larger semigroups of partial endomorphisms of equivalence relations, for certain wreath products, and for monoids of order-preserving partial maps on chains. Their broad spatiality theorem assumes that for each underlying point there exists a constant idempotent with that point as image. The present monoids have no such point-valued constants when \(m\ge2\), because every nonempty domain is a union of whole blocks. Moreover, the order-preserving condition is imposed on the block quotient rather than on the individual points. The specific group-labeled classification and non-spatial \(S_6\) exception are not consequences of those stated applications. The \(m=2\) and \(m\ge3\), \(m\neq6\) cases are spatial, agreeing conceptually with the earlier chain and inverse-semigroup rigidity results.

McCammond [3] supplies a proof of the classical exceptional automorphism theorem for symmetric groups; that theorem is invoked here but not re-proved or claimed as original.

## Limitations

This theorem does not classify endomorphisms, general congruences, or automorphisms of monoids with unequal block sizes or order-reversing partial maps adjoined as elements. The proof assumes equal block sizes so that all rank-one labels lie in one group. Literature-wide priority cannot be certified: an unlocated general automorphism theorem for group-labeled rook or Brandt-type inverse semigroups could imply this result. No independent mathematical audit or complete publication-priority search has been performed.

## References

[1] R. Caneco, V. H. Fernandes and T. M. Quinteiro, *Ranks and presentations of some normally ordered inverse semigroups*, arXiv:1905.11489v1 (public 27 May 2019), https://arxiv.org/abs/1905.11489 ; later *Periodica Mathematica Hungarica* 85 (2022), 435–447.

[2] J. Araújo, V. H. Fernandes, M. M. Jesus, V. Maltcev and J. D. Mitchell, *Automorphisms of partial endomorphism semigroups*, *Publicationes Mathematicae Debrecen* 79 (2011), 23–39, https://doi.org/10.5486/PMD.2011.4703 .

[3] J. McCammond, *The exceptional symmetry*, arXiv:1412.1855 (public 4 December 2014), https://arxiv.org/abs/1412.1855 .
