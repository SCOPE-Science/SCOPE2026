# The domain-rank involution polynomial of the dihedral inverse monoid

## Finding
For each integer \(n\ge3\), let \(\Omega=\mathbb Z/n\mathbb Z\) and let \(\mathcal D_n\) be the inverse monoid of all restrictions \(g|_A\) of permutations \(g\in D_{2n}\) to subsets \(A\subseteq\Omega\), with the empty restriction included. A partial permutation is an **involution** here if \(\alpha=\alpha^{-1}\), equivalently \(\alpha^2=\operatorname{id}_{\operatorname{dom}\alpha}\); this includes all partial identities. Define its domain-rank polynomial
\[
P_n(z)=\sum_{\substack{\alpha\in\mathcal D_n\\\alpha=\alpha^{-1}}}z^{|\operatorname{dom}\alpha|}.
\]
For odd \(n\),
\[
\boxed{P_n(z)=(1+z)^n+n(1+z)\left((1+z^2)^{(n-1)/2}-1\right).}
\]
For even \(n=2h\),
\[
\boxed{P_{2h}(z)=(1+z)^{2h}+h(1+z)^2\left((1+z^2)^{h-1}-1\right)+(h+1)\left((1+z^2)^h-1\right)-hz^2.}
\]
In both cases, the coefficients of \(z^0,z^1,z^2\) are exactly \(1,n,n(n-1)\). The last term of the even formula removes precisely \(h\) double-counted nonidentity rank-two restrictions.

At \(z=1\), the counts are
\[
P_n(1)=\begin{cases}
2^n+n2^{(n+1)/2}-2n,& n\text{ odd},\\
2^n+(3n/2+1)2^{n/2}-3n-1,&n\text{ even}.
\end{cases}
\]
For fixed \(n\), all counts are integer; as \(n\to\infty\), the fraction of these involutions that are idempotents tends to \(1\), with error \(O(n2^{-n/2})\). Their domain-rank law is within \(O(n2^{-n/2})\) in total variation of \(\operatorname{Binomial}(n,1/2)\).

## Assumptions and scope
The result holds for every integer \(n\ge3\). Write rotations as \(r_a(i)=i+a\) and reflections as \(s_a(i)=a-i\), with indices modulo \(n\). The monoid elements are **distinct partial maps**, not pairs \((g,A)\); distinct global isometries may have the same restriction. No abstract group algebra or field is involved. The rank is the domain cardinality, not the minimum number of semigroup generators.

## Proof
**1. Classification of possible involutions.** If \(\alpha=g|_A\) satisfies \(\alpha=\alpha^{-1}\), then \(g(A)=A\) and \(g^2(i)=i\) for all \(i\in A\). Every nonidentity rotation of order greater than two acts freely, as does its square, so no nonempty such \(A\) occurs. Thus every nonempty self-inverse restriction extends either the identity, a reflection, or (only if \(n\) is even) the half-turn. Conversely, restriction of any of these global involutions to an invariant subset is self-inverse.

**2. Restriction polynomials before coincidences.** A permutation with \(f\) fixed points and \(t\) transposed pairs has invariant-subset polynomial \((1+z)^f(1+z^2)^t\). The identity contributes \((1+z)^n\). For odd \(n\), each of the \(n\) reflections has one fixed vertex and \((n-1)/2\) transpositions. Its restrictions consisting only of fixed vertices (empty or its fixed singleton) are already partial identities, so its genuinely nonidentity contribution is \((1+z)((1+z^2)^{(n-1)/2}-1)\). For \(n=2h\), precisely \(h\) reflections fix two vertices, contributing \((1+z)^2((1+z^2)^{h-1}-1)\) each after subtracting fixed-only restrictions; the other \(h\) reflections have no fixed vertex, contributing \((1+z^2)^h-1\) each. The half-turn has no fixed vertex and contributes a further \((1+z^2)^h-1\).

**3. Exact coincidence audit.** If two distinct reflections coincide on a vertex, their quotient is a nontrivial rotation fixing that vertex, impossible. Thus nonidentity restrictions of different reflections are disjoint. For odd \(n\) there is no half-turn. For even \(n=2h\), let \(\tau(i)=i+h\). A reflection \(s_a\) and \(\tau\) agree exactly at solutions of \(2i\equiv a-h\pmod{2h}\), hence either nowhere or at exactly two antipodal vertices \(\{i,i+h\}\). On this pair they both swap the vertices. Any nonempty \(\tau\)-invariant subset contained in the agreement set is the full two-point pair. Every one of the \(h\) antipodal pairs determines exactly one such reflection, giving precisely \(h\) doubly represented nonidentity rank-two maps. Subtracting \(hz^2\) finishes the formulas. No higher-rank coincidences are possible, since two distinct dihedral permutations agree on at most two vertices.

**4. Low coefficients, total counts and asymptotic law.** Expanding the two polynomials gives \([z^0]P_n=1\), \([z^1]P_n=n\), and \([z^2]P_n=n(n-1)\) for either parity. Setting \(z=1\) gives the displayed formulas. Exactly \(2^n\) involutions are partial identities, and the number of additional involutions is \(O(n2^{n/2})\). Therefore their relative mass is \(O(n2^{-n/2})\). Conditioned on being a partial identity, the domain is uniformly distributed among all subsets, with binomial rank law; mixture bounds imply the total-variation claim.

## Verification
Run `python verify.py` (Python standard library only). The checker independently constructs every distinct restriction of the \(2n\) dihedral permutations for \(3\le n\le10\), computes their partial inverses as maps, and compares the complete domain-rank census with each formula. For \(n=3,4,5,6\), the exact involution totals are \(14,31,62,125\), respectively; the corresponding full monoid cardinalities are \(34,97,286,703\). All eight checked sizes pass. The exhaustive computations are finite corroboration; the proof above handles every \(n\ge3\).

## Relationship to prior work
Dimitrova, Fernandes, Koppitz, and Quinteiro (arXiv:2301.01519, first posted January 4, 2023) study the dihedral inverse monoid and its orientation-, monotonicity-, and order-preserving submonoids, calculating cardinalities, Green's relations, ranks and presentations. Their description of dihedral restrictions is used as the algebraic setting, not claimed as new. Fernandes and Paulista's 2022 preprint (arXiv:2205.02196, first posted May 4, 2022) establishes the same cycle partial-isometry monoid and its cardinality, rank and presentation; importantly, Lemma 1.1 already identifies the antipodal rank-two nonunique extension phenomenon, used in the proof above. The statement proved here concerns instead the **complete domain-rank distribution of self-inverse elements**. The relevant accessible sections of the cited papers do not state this distribution, and a broader general theorem on restriction-monoid torsion enumeration may provide an alternative derivation.

## Limitations
The formulas concern the inverse monoid of **global dihedral restrictions**, not all partial induced-subgraph automorphisms of a cycle, which is a different monoid. The asymptotic takes \(n\to\infty\); no claim of a novel general-purpose group-action counting theorem is made. Publication priority is provisional: some broader inverse-semigroup literature may imply the result. Independent verification or audit has not been performed.

## References
1. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On three submonoids of the dihedral inverse monoid on a finite set*, arXiv:2301.01519, v1 January 4, 2023; subsequent v2 November 2023. https://arxiv.org/abs/2301.01519
2. V. H. Fernandes, T. Paulista, *On the monoid of partial isometries of a cycle graph*, first posted May 4, 2022 as arXiv:2205.02196; Turkish Journal of Mathematics 47 (2023), 1746–1760. DOI:10.55730/1300-0098.3460. https://arxiv.org/abs/2205.02196
