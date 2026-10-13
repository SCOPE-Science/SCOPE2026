# Embedded monogenic inverse submonoids of finite symmetric inverse monoids

## Finding

Let \(I_n\) be the symmetric inverse monoid of partial bijections on \([n]=\{1,\ldots,n\}\), with global identity \(1_n\). For \(\alpha\in I_n\), put \(H_\alpha=\langle1_n,\alpha,\alpha^{-1}\rangle\). Count **distinct embedded subsets** \(H_\alpha\subseteq I_n\), not isomorphism classes. In the directed graph of \(\alpha\), let \(a(\alpha)\) be the largest number of vertices in a directed-chain component (a singleton with no incident edge counts as a one-vertex chain); if no chains exist put \(a(\alpha)=1\). Let \(k(\alpha)\) be the least common multiple of lengths of its directed-cycle components, with empty least common multiple equal to one. These parameters depend only on \(H_\alpha\).

For every \(n\ge1\), \(1\le a\le n\), and integer \(k\ge1\), let \(E_n(a,k)\) count the distinct embedded inverse submonoids \(H_\alpha\) with \((a(\alpha),k(\alpha))=(a,k)\). Define formal series

\[
 C_d(z)=\exp\left(\sum_{j\mid d}\frac{z^j}{j}\right),\qquad
 P_a(z)=\exp\left(\sum_{j=1}^{a}z^j\right),\quad P_0(z)=1,
 \qquad Q_k(z)=\sum_{d\mid k}\mu(k/d)C_d(z).
\]

Here \(\mu\) is the arithmetic Möbius function; coefficients are interpreted formally over \(\mathbb Q\). Then the **complete joint longest-chain/cycle-order profile** is

\[
\boxed{
 E_n(a,k)=\begin{cases}
 \displaystyle\frac{n!}{\varphi(k)}[z^n]e^zQ_k(z),&a=1,\\[2mm]
 \displaystyle\frac{n!}{2}[z^n]\bigl(P_a(z)-P_{a-1}(z)\bigr)Q_k(z),&a\ge2.
\end{cases}}
\]

Every coefficient in the display is an integer. For chain-bearing generators the embedded inverse submonoid has **exactly two generators**, the given partial bijection and its inverse; for cycle-only generators it has exactly \(\varphi(k)\) generators. This rigidity is the reason for the two different denominators.

Writing \(M_n=\sum_{a,k}E_n(a,k)\), an alternative finite formula is

\[
 M_n=\frac12\left(\sum_{r=0}^n\binom nr^2r!-\sum_{s=0}^n\binom ns s!\right)
 +\sum_{s=0}^n\binom ns\sum_{\lambda\vdash s}
 \frac{s!}{z_\lambda\,\varphi(\operatorname{lcm}(\lambda))},
 \qquad z_\lambda=\prod_{j\ge1}j^{m_j}m_j!.
\]

The empty partition has \(z_\varnothing=1\) and \(\operatorname{lcm}(\varnothing)=1\). The first term counts the chain-bearing inverse submonoids; the second counts cycle-only ones, indexed by a support set and a cyclic subgroup of its symmetric group. In particular

\[
 (M_1,M_2,M_3,M_4,M_5,M_6)=(2,6,24,126,838,6841).
\]

The proportion of embedded monogenic inverse submonoids with a chain-bearing generator tends to one: if \(R_n=\sum_{s=0}^n\binom ns s!\), then \(R_n\le e\,n!\), whereas \(|I_n|\ge(n+1)n!\), so the cycle-only fraction is \(O(1/n)\).

## Assumptions and scope

Only finite sets \([n]\) with \(n\ge1\) are considered. Composition is the ordinary composition of partial bijections, and \(H_\alpha\) contains the global identity even when \(\alpha\) is supported on a proper subset. Directed chains and cycles are vertex-disjoint and exhaust \([n]\); an inactive vertex is a chain of one vertex. The cyclic order \(k\) comes **only** from cycle components, not from chain lengths. The finding enumerates literal embedded submonoids, not abstract isomorphism types and not subsemigroups formed without the global identity. The lead 2023 source is in primary MSC2020 \(20M20\).

## Proof

**1. Unique-generator lemma for chains.** Every partial bijection is a disjoint union of oriented paths and directed cycles. A word \(w\) in \(\alpha\) and \(\alpha^{-1}\) has an exponent sum \(t\in\mathbb Z\). On a directed chain of \(v\) vertices the word is a restriction of translation by \(t\), hence has rank at most \(\max(v-|t|,0)\); on a cycle of length \(j\) it is the total permutation \(\alpha^t\). The rank of a product of partial bijections never exceeds the rank of either factor.

Assume \(a(\alpha)\ge2\), and \(\beta\in H_\alpha\) also generates \(H_\alpha\). Since \(\alpha\) and \(\beta\) are words in one another and inverse, rank monotonicity forces \(\operatorname{rank}\beta=\operatorname{rank}\alpha\). A word with exponent sum zero is a partial identity (on every component) and cannot generate the non-idempotent chain map \(\alpha\). For \(|t|\ge2\), the rank on each chain is at most its corresponding rank under \(\alpha\), and is strictly smaller on at least one chain with two or more vertices; its rank on every cycle remains unchanged. Thus \(|t|=1\). Equality of ranks now forces translation by \(+1\), or respectively \(-1\), to be defined on every possible chain edge, so \(\beta=\alpha\), or respectively \(\beta=\alpha^{-1}\). Both generate and are different. Hence every chain-bearing embedded submonoid has exactly two generating elements.

If \(a(\alpha)=1\), \(\alpha\) is a permutation \(g\) on its support \(S\), undefined elsewhere. Its generated inverse submonoid equals \(\langle g\rangle\cup\{1_n\}\); all generating elements are precisely the \(\varphi(k)\) generators of the cyclic group \(\langle g\rangle\), where \(k=|g|\). This includes \(k=1\) and \(S=\varnothing\). Consequently the profile \((a,k)\) is constant among all generators of one embedded submonoid, with fiber size two for \(a\ge2\) and \(\varphi(k)\) for \(a=1\).

**2. Labeled component count.** On a chosen \(j\)-element vertex set, there are \(j!\) oriented chains of size \(j\), yielding exponential generating weight \(z^j\), including inactive singleton chains. There are \((j-1)!\) directed cycles of length \(j\), yielding weight \(z^j/j\). By the labeled exponential formula, \(P_a(z)C_d(z)\) counts partial bijections whose chains have size at most \(a\) and whose cycles have lengths dividing \(d\). The order of the cyclic part then divides \(d\). Möbius inversion on the divisor lattice extracts exact cycle-order \(k\) as \(Q_k(z)\). For \(a\ge2\), subtracting \(P_{a-1}Q_k\) requires largest chain size exactly \(a\). For \(a=1\), chains are precisely inactive singletons, giving \(P_1=e^z\). The unique-generator lemma divides each resulting count by two, or by \(\varphi(k)\), proving the profile formula. Since it counts equivalence classes of actual generators, its coefficients are integers.

**3. Total and asymptotics.** There are \(|I_n|=\sum_{r=0}^n\binom nr^2r!\) partial bijections, because one chooses domain, range, and a bijection of rank \(r\). Those with no nontrivial chains are precisely permutations on some support \(S\), numbering \(R_n=\sum_{s=0}^n\binom ns s!\). Therefore the chain-bearing contribution is \((|I_n|-R_n)/2\). For a fixed support of size \(s\), cycle-only submonoids biject with cyclic subgroups of \(S_s\). There are \(s!/z_\lambda\) permutations of cycle type \(\lambda\), and exactly \(\varphi(\operatorname{lcm}(\lambda))\) generators per cyclic subgroup. Summing over types and supports gives the second term. Finally, \(R_n=n!\sum_{j=0}^n1/j!\le e\,n!\); rank-\(n\) and rank-\(n-1\) partial bijections alone give \(|I_n|\ge(n+1)n!\). Thus cycle-only submonoids are \(O(n!)\) out of \(\Omega(n\,n!)\) chain-bearing submonoids, proving the asserted limiting proportion.

## Verification

The standalone `checker.py` uses exact rational formal-series arithmetic and a separate exhaustive algorithm. For every \(1\le n\le6\), it enumerates all partial bijections, explicitly closes each generator under multiplication by itself and its inverse together with the global identity, groups generators by **equal sets** of partial maps, computes both graph parameters, and compares each resulting profile with the symbolic coefficient formula. It also checks that every generating fiber has exactly the predicted size and that the totals equal \(2,6,24,126,838,6841\). Execute `python checker.py` from the directory containing this file. The final output is `VERIFY_OK`. The proof for all \(n\) is algebraic and does not depend on finite enumeration.

For \(n=4\), the nonzero profile values are

\[
\begin{array}{c|rrrrrrrr}
(a,k)&(1,1)&(1,2)&(1,3)&(1,4)&(2,1)&(2,2)&(3,1)&(4,1)\\
E_4(a,k)&16&27&8&3&30&6&24&12
\end{array}.
\]

## Relationship to prior work

Elliott, Levine, and Mitchell (2023), Theorem 1 and Section 4, count monogenic inverse submonoids of finite symmetric inverse monoids **up to isomorphism**, and their Lemmas 8–9 classify which abstract isomorphism types occur. In contrast, this finding determines the multiplicities of **distinct labeled embedded submonoids**, with cycle-order and longest-chain refinements. The generator-fiber rigidity and the exact formulas above do not follow from the statement of their type-count theorem without an additional equality-of-generated-subsets argument and labeled component enumeration. Preston (1986) establishes structural realizations and representation-theoretic classifications of monogenic inverse semigroups; that work supplies fundamental background rather than these embedded counts. The underlying chain–cycle decomposition and exponential formula are classical and not claimed as innovations. Published source and alias searches did not identify the explicit embedded joint-profile formula, but absence of a search hit does not establish absolute novelty.

## Limitations

The answer concerns finite symmetric inverse monoids with the **global identity retained** and says nothing about arbitrary inverse subsemigroups, other ambient monoids, or the complexity of all inverse submonoids. It does not enumerate abstract isomorphism classes; those are addressed by earlier work. The finite checker covers only \(n\le6\); the infinite assertion is established by proof. Independently published embedded counts under alternate terminology remain possible and require external bibliographic assessment. No independent audit has been performed.

## References

1. L. Elliott, A. Levine, and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, 2023, arXiv:2303.12387 (version 1 submitted 22 March 2023), *Communications in Algebra* **51** (2023), 4654–4661. https://arxiv.org/pdf/2303.12387 ; https://doi.org/10.1080/00927872.2023.2214821 .
2. G. B. Preston, *Monogenic inverse semigroups*, *J. Austral. Math. Soc. Ser. A* **40** (1986), 321–342. https://doi.org/10.1017/S1446788700027543 .
