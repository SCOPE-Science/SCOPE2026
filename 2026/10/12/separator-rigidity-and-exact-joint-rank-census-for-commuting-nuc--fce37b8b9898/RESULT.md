# Separator rigidity and exact joint-rank census for commuting nuclei of finite Gödel chains

## Finding
For every integer \(n\ge1\), consider the finite Gödel (linearly ordered Heyting) algebra \(C_n=\{0<1<\cdots<n-1\}\). A **nucleus** means a monotone, inflationary, idempotent unary operation preserving finite meets. For a subset \(S\subseteq C_n\) containing the greatest element, put
\[
j_S(x)=\min\{s\in S:s\ge x\}.
\]
Every nucleus is uniquely of this form. Given two nuclei, let \(B=S\cap T\). List its elements as \(b_1<\cdots<b_k=n-1\), and put \(b_0=-1\). For each \(i=1,\ldots,k\), form the open integer interval \(I_i=\{b_{i-1}+1,\ldots,b_i-1\}\). Then the following are equivalent:

1. \(j_S\circ j_T=j_T\circ j_S\).
2. For every \(i\), either \(I_i\cap(S\setminus T)=\varnothing\) or \(I_i\cap(T\setminus S)=\varnothing\).
3. \(j_S\circ j_T=j_T\circ j_S=j_B\).

Let \(R_{n,k}\) denote the number of **ordered** pairs satisfying these conditions for which the common composition has exactly \(k\) fixed points. For \(1\le k\le n\), the exact joint-image-rank profile is
\[
R_{n,k}=[z^{n-k}]\frac1{(1-z)^k(1-2z)^k}
=\sum_{a=0}^{n-k}\binom{k+a-1}{a}\binom{n-a-1}{n-k-a}2^{n-k-a}.
\]
It is zero outside this range. Consequently, the number of ordered commuting pairs is
\[
c_n=\sum_{k=1}^n R_{n,k}
=\frac{(2+\sqrt2)^n-(2-\sqrt2)^n}{2\sqrt2}.
\]
In particular \(c_1=1\), \(c_2=4\), \(c_3=14\), \(c_4=48\), and \(c_n=4c_{n-1}-2c_{n-2}\) for \(n\ge3\). If nuclei are selected independently uniformly from the \(2^{n-1}\) possibilities, their commutation probability is \(c_n/4^{n-1}\), asymptotic to \(\sqrt2((2+\sqrt2)/4)^n\).

For a nonempty finite direct product \(A=\prod_{i=1}^d C_{n_i}\), every nucleus is coordinatewise. Thus the number of ordered commuting nucleus pairs on \(A\) is \(\prod_{i=1}^d c_{n_i}\). More precisely, the generating polynomial recording the cardinality of the image of their composite is
\[
\sum_{k_1=1}^{n_1}\cdots\sum_{k_d=1}^{n_d}\left(\prod_{i=1}^d R_{n_i,k_i}\right)t^{\prod_{i=1}^d k_i}.
\]

## Assumptions and scope
All chains and products are finite and nonempty. A nucleus is a meet-preserving closure operator, not necessarily a Heyting-algebra homomorphism and not required to preserve bottom. The chain implication is \(x\to y=n-1\) when \(x\le y\) and \(x\to y=y\) otherwise. The composite image cardinality is the number of fixed points of its nucleus when the pair commutes. This work makes no assertion about arbitrary finite Heyting algebras, noncommuting compositions, or infinite chains. The parameter \(n\) denotes the number of elements, including bottom and top; there is no empty-chain case.

## Proof
**All nuclei are fixed-point ceil maps.** Any isotone map on a chain preserves binary meets, since the minimum of two arguments is one of them. For an inflationary isotone idempotent map \(j\), the set \(S=\{x:j(x)=x\}\) contains the top, and \(j(x)\) is the least \(j\)-fixed point above \(x\): \(j(x)\) is fixed, and \(j(x)\le s\) for any fixed \(s\ge x\) by monotonicity. Conversely, the displayed ceil map has all the required properties. Hence the parameterization by \(S\) is bijective and has \(2^{n-1}\) choices.

**Commutation is equivalent to separator purity.** Fix consecutive common fixed points \(b_{i-1},b_i\), allowing \(b_0=-1\). If \(I_i\) contains private points of at most one kind, then for every \(x\) with \(b_{i-1}<x\le b_i\) the operator lacking private fixed points in that interval sends \(x\) directly to \(b_i\); the other sends \(x\) to a point at most \(b_i\). Either order of composition therefore sends \(x\) to \(b_i\). This proves both commutation and equality with \(j_B\) when all intervals are pure.

Conversely suppose some \(I_i\) contains both private kinds. Let \(u\) be the least point of \(I_i\cap((S\setminus T)\cup(T\setminus S))\). After interchanging \(S\) and \(T\) if necessary, assume \(u\in S\setminus T\). Let \(v\) be the least point of \(I_i\cap(T\setminus S)\) above \(u\); such a point exists by minimality of \(u\) and the two kinds being present. There is no \(T\)-fixed point between \(u\) and \(v\), so \(j_T(u)=v\), while \(j_S(u)=u\) and \(j_S(v)>v\). Hence \(j_S(j_T(u))>j_T(j_S(u))\), proving failure of commutation. Finally, if two closures commute, their common composite has image in \(S\cap T\), by viewing it in both orders; it is inflationary and bounded above by every common fixed point above its argument, hence equals \(j_B\). This independently yields the implication from commutation to the explicit composite identity.

**Rank-profile enumeration.** Encode the position \(x\) by one of four symbols: absent from both sets, private to \(S\), private to \(T\), or common to both. The final position is necessarily common. Between two consecutive common symbols (also before the first), there are \(m\ge0\) noncommon symbols; they may use the alphabet of absent plus only the first private kind, or absent plus only the second private kind. Inclusion-exclusion gives precisely \(2\cdot2^m-1=2^{m+1}-1\) allowed blocks, including the all-absent word just once. The ordinary generating function for a block ending in one common symbol is
\[
A(z)=\sum_{m\ge0}(2^{m+1}-1)z^{m+1}
=\frac{z}{(1-z)(1-2z)}.
\]
An admissible pair with \(k\) common fixed points is uniquely a concatenation of \(k\) blocks; the coefficient of \(z^n\) in \(A(z)^k\) is precisely the stated \(R_{n,k}\). The binomial sum follows from expanding the two negative binomial powers. Summing over all \(k\ge1\) gives
\[
\sum_{n\ge1}c_n z^n=\frac{A(z)}{1-A(z)}=\frac{z}{1-4z+2z^2},
\]
whose partial fraction decomposition gives the closed form and recurrence. Independence of uniform choices gives the probability formula; since \((2-\sqrt2)/(2+\sqrt2)<1\), its displayed asymptotic follows.

**Direct products.** Write the top of each factor as \(\top_i\). Every element of \(A\) is a meet of axis vectors \(e_i(x_i)\), with coordinate \(i\) equal to \(x_i\) and all others at their respective tops. Extensivity forces the image of an axis vector under any nucleus to have top in every off-axis coordinate. Preservation of finite meets therefore yields \(j(x_1,\ldots,x_d)=(j_1(x_1),\ldots,j_d(x_d))\). The nuclear axioms descend to each \(j_i\), and conversely any tuple of chain nuclei defines a nucleus on the product. Two such products commute exactly when they commute coordinatewise, and the image of the composite is the Cartesian product of the coordinate images. Multiplying counts and recording the product of local ranks establishes both product formulas.

## Verification
The dependency-free executable `verify_nuclei.py` independently enumerates all pairs of fixed-set ceiling maps through \(n=10\) and compares literal compositions against the separator criterion, the common-intersection composite, the recurrence, and **every** joint-rank coefficient. This entails exactly 349,525 ordered-pair checks. It independently enumerates every self-map and filters the nucleus axioms on chains through \(n=5\), rather than assuming the fixed-set representation in that oracle. Small products are checked by direct meet-preservation and composition; all extensive self-maps of products \(C_2\times C_2\) and \(C_2\times C_3\) are independently filtered to verify coordinate decomposition. Use `python3 verify_nuclei.py`; expected final line begins `VERIFY_OK ordered_pairs_checked 349525`. Finite checks do not establish the unbounded formulas; the preceding symbolic argument does.

## Relationship to prior work
Jānis Cīrulis, *Modal Hilbert algebras and their triple representation* (author-uploaded public manuscript dated 23 May 2020), §3, develops modal closure operators and **Proposition 3.5** proves that commuting modal operators have a modal composite (their join), conversely that two modal compositions being modal entails commutation. This general criterion gives no chain-fixed-point obstruction or joint-rank enumeration. Marcel Erné, *Nuclear ranges in implicative semilattices*, §3, Lemma 3.6, explicitly explains that nuclei are not generally closed under composition and that commutation is a sufficient condition for the composite to be nuclear; the lemma does not give a chain fixed-point obstruction or joint-rank census. Shallit and Willard, *Kuratowski's Theorem for Two Closure Operators*, §§2–4, study closure/complement-generated monoids and identities for commuting abstract powerset closures, a different ambient algebra and invariant. The numerical sequence \(1,4,14,48,164,\ldots\) already appears in OEIS A007070 for unrelated interpretations, so the numbers themselves and their linear recurrence are **not** claimed as newly discovered. The claim here is the commutation classification and rank-refined realization of this sequence for nuclear modalities, plus the exact product behavior. A historically equivalent formulation may exist; absence in searched sources is not proof of absolute priority.

## Limitations
The theorem is restricted to finite chains and their finite direct products. It counts ordered pairs, not conjugacy classes, since the chains themselves have no nontrivial order automorphisms. Existing universal facts about closure-operator fixed sets and the general implication from commuting nuclei to nuclear composites are acknowledged as prior art. Independent mathematical and literature audits have not been performed, and the first-discovery claim remains subject to broader bibliographic checking. The finite verifier is reproducibility evidence but cannot certify novelty or infinite-parameter correctness.

## References
1. J. Cīrulis, *Modal Hilbert algebras and their triple representation*, public author manuscript uploaded 23 May 2020, https://www.researchgate.net/publication/341600258_Modal_Hilbert_algebras_and_their_triple_representation.
2. M. Erné, *Nuclear ranges in implicative semilattices*, *Algebra universalis* (2022), https://doi.org/10.1007/s00012-022-00768-3.
3. J. Shallit and R. Willard, *Kuratowski's Theorem for Two Closure Operators* (2011), https://arxiv.org/html/1109.1227v1.
4. *The On-Line Encyclopedia of Integer Sequences*, A007070, https://oeis.org/A007070.
