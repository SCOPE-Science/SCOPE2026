# Two independent threshold systems for diagonal subsemigroups of chain semilattices

## Finding

Let \(C_n=\{0,1,\ldots,n-1\}\) with \(a\wedge b=\min(a,b)\), where \(n\ge1\). A diagonal subsemigroup means a subset \(R\subseteq C_n\times C_n\) containing every \((i,i)\) and closed under coordinatewise meet. For each \(i\in C_n\), choose independently two thresholds \(u_i,v_i\in\{i,i+1,\ldots,n-1\}\), and define
\[
R(u,v)=\Delta\cup\{(i,j):i<j\le u_i\}\cup\{(j,i):i<j\le v_i\}.
\]
Every diagonal subsemigroup is exactly one such \(R(u,v)\), and every threshold pair defines a diagonal subsemigroup. Inclusion is equivalent to coordinatewise comparison of all thresholds, so the inclusion lattice is \(\bigl(\prod_{k=1}^{n} C_k\bigr)^2\), where \(C_k\) is a \(k\)-element chain. Consequently
\[
|\operatorname{Diag}(C_n)|=(n!)^2,\qquad
\sum_{R\in\operatorname{Diag}(C_n)}z^{|R|-n}=\prod_{k=1}^{n}(1+z+\cdots+z^{k-1})^2.
\]
Exactly \(n!\) diagonal subsemigroups are symmetric. The congruences are precisely the partitions of \(C_n\) into consecutive intervals, so \(|\operatorname{Cong}(C_n)|=2^{n-1}\). Thus the diagonal-subsemigroup coefficient defined by Barber and Ruškuc obeys
\[
\chi(C_n)=\frac{2^{n-1}}{(n!)^2},\qquad
\frac{\chi(C_{n+1})}{\chi(C_n)}=\frac{2}{(n+1)^2}.
\]
In particular \(\chi(C_n)\to0\), with \(\chi(C_n)\sim (2e^2/n^2)^n/(4\pi n)\).

## Assumptions and scope

The only operation on \(C_n\) is binary meet (the minimum), and \(n\) ranges over all positive integers. Compatibility is closure under coordinatewise minimum, with no symmetry or transitivity assumed. The rank variable \(z\) records the number of off-diagonal ordered pairs in a relation. A congruence is a compatible equivalence relation. The lattice is ordered by ordinary inclusion of subsets of \(C_n^2\); for \(n=1\) the empty threshold products have their usual one-element interpretation.

## Proof

**Necessity of interval thresholds.** Fix a reflexive meet-compatible relation \(R\). If \((i,j)\in R\) with \(i<j\), then for every \(k\) with \(i<k\le j\), compatibility with the diagonal pair \((k,k)\) yields
\[
(i,j)\wedge(k,k)=(i,k)\in R.
\]
The upper off-diagonal entries in row \(i\) therefore form either an empty set or a consecutive interval \(\{i+1,\ldots,u_i\}\). Likewise, \((j,i)\in R\) with \(i<j\), together with \((k,k)\) for \(i<k\le j\), yields \((k,i)\in R\); the lower off-diagonal entries in column \(i\) form \(\{i+1,\ldots,v_i\}\). These thresholds are determined uniquely by \(R\), assigning \(i\) when the corresponding interval is empty.

**Sufficiency and independence.** Conversely fix arbitrary threshold arrays \(u,v\). Reflexivity of \(R(u,v)\) is immediate. For pairs \((a,b),(c,d)\in R(u,v)\), if they are comparable in the product order, their coordinatewise meet equals one of the two pairs. Otherwise, after possibly interchanging the pairs, \(a<c\) and \(b>d\), so their meet is \((a,d)\). If \(a=d\), this is diagonal. If \(a<d\), then \(a<d<b\), and the presence of \((a,b)\) forces \((a,d)\) by the upper interval rule. If \(a>d\), then \(d<a<c\), and the presence of \((c,d)\) forces \((a,d)\) by the lower interval rule. These are exhaustive possibilities. Hence any two independent threshold arrays give a compatible relation; **the two directions impose no hidden cross-constraints**.

**Inclusion lattice and enumeration.** For each \(i\), raising \(u_i\) adds exactly one upper ordered pair at each step and raising \(v_i\) adds exactly one lower ordered pair. Thus \(R(u,v)\subseteq R(u',v')\) holds exactly when \(u_i\le u'_i\) and \(v_i\le v'_i\) for all \(i\). The possible numbers of choices for successive thresholds are \(n,n-1,\ldots,1\) for each direction. The product-lattice description and factorial-square count follow. Since \(|R(u,v)|-n=\sum_i[(u_i-i)+(v_i-i)]\), independent multiplication of each geometric polynomial gives the displayed rank generating function. Symmetry means exactly \(u_i=v_i\) for every \(i\), leaving \(n!\) choices.

**Congruences and decay.** Suppose \(\theta\) is a congruence, and \(i<k<j\) with \(i\mathrel{\theta}j\). Meeting both elements with \(k\) gives \(i\mathrel{\theta}k\), and equivalence then puts all three in one block. Hence each block is an interval. Conversely, any partition into consecutive intervals respects minimum: the minimum of two representatives lies in whichever of their two blocks appears earlier in the chain, independently of representatives. There is one binary choice for each of the \(n-1\) gaps, so there are \(2^{n-1}\) congruences. Dividing by \((n!)^2\) yields the exact coefficient and successive ratio. Stirling's asymptotic formula gives the stated decay. The formulas hold at \(n=1\): all counts equal one.

## Verification

The standalone \`verify.py\` enumerates all \(2^{n(n-1)}\) reflexive binary relations for \(1\le n\le4\), tests closure under coordinatewise minimum and independently checks symmetry, transitivity and the size distribution. The observed triples (diagonal, symmetric, congruence) are \((1,1,1)\), \((4,2,2)\), \((36,6,4)\), \((576,24,8)\). Every relation from the threshold construction is checked, and the sets of reconstructed relations agree exactly for these cases. For \(n=5\), all \(14{,}400\) threshold pairs give distinct closed relations and agree with the generating-polynomial total. These finite checks verify examples; the proof covers every \(n\).

## Relationship to prior work

Barber and Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups* (arXiv:2602.17286, first public version 19 February 2026), define \(\chi\), establish results for Rees matrix and Clifford semigroups, and explicitly leave the possible values of \(\chi\) on finite semilattices unresolved in their Section 4. The formula above evaluates this statistic on the natural infinite family of chain semilattices; it does not answer the question for arbitrary semilattices.

Chajda, Nieminen, and Zelinka, *Tolerances and orderings on semilattices* (1983), Theorems 2 and 7, establish substantial preceding one-sided compatible-ordering and symmetric-tolerance structure, including an interval rule for one-sided relations on tree semilattices. That older result is **acknowledged as partial prior coverage**. The independent coupling of both directions for arbitrary reflexive relations, the full two-threshold lattice decomposition, the rank generating polynomial and the explicit DSC coefficient are the additional statements proved here. The 1983 paper does not state these latter full-relation formulas.

## Limitations

The result concerns chain semilattices in the one-operation semigroup signature; adding other operations can change the compatible relations. No conclusion about non-chain semilattices or general Clifford semigroups follows. The one-sided case and tolerances have substantial earlier theory, so equivalent full-relation formulas in unindexed semilattice literature remain a genuine originality risk. Finite computations alone are not a proof of the infinite family. Independent mathematical validation has not been performed.

## References

1. C. Barber and N. Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*, arXiv:2602.17286 (first posted 19 February 2026), https://arxiv.org/abs/2602.17286 . See Sections 1 and 4.
2. I. Chajda, J. Nieminen, and B. Zelinka, *Tolerances and orderings on semilattices*, Archivum Mathematicum 19 (1983), 125–131, https://dml.cz/dmlcz/107165 . See Theorems 2, 6 and 7.
3. C. Barber and N. Ruškuc, *Semigroup congruences and subsemigroups of the direct square*, Bulletin of the Australian Mathematical Society 113 (2026), 123–134; first publicly posted as arXiv:2504.02428 in April 2025. This earlier work introduces the qualitative DSC property.
