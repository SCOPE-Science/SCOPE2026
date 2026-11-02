# Hamming-cover polynomial counts ordered idempotent generators of finite incidence algebras

## Finding
Let \(P\) be any nonempty finite poset and \(K=\mathbb F_q\) any finite field. For every integer \(k\geq0\), let \(G_{P,k}(q)\) be the number of ordered \(k\)-tuples of idempotents in the incidence algebra \(I(P,K)\) which generate it as a **unital \(K\)-algebra**. Let \(x\lessdot y\) mean that \(y\) covers \(x\), and write \(h_\chi(x,y)\) for the Hamming distance between the two binary words \(\chi(x),\chi(y)\in\{0,1\}^k\). Then

\[
\boxed{G_{P,k}(q)=\sum_{\chi:P\hookrightarrow\{0,1\}^{k}}\;q^{\sum_{x<y,\,x\not\lessdot y}h_\chi(x,y)}\prod_{x\lessdot y}\bigl(q^{h_\chi(x,y)}-q\bigr).}
\]

The sum runs over **all injective maps**, not only order-preserving maps. Empty sums/products follow their usual conventions. In particular, the answer is an explicitly evaluable integer polynomial in the field size \(q\) for each fixed \(P,k\). A summand vanishes if any cover edge joins binary words at Hamming distance one. The assertion also holds for \(k=0\): only the one-point poset admits an empty unital generating tuple.

Writing \(c(d)=|\{(x,y):x<y,\ d(x)\ne d(y)\}|\), the number of all idempotents in \(I(P,K)\) is \(H_P(q)=\sum_{d:P\to\{0,1\}}q^{c(d)}\). Therefore the exact probability that \(k\) independent uniformly selected idempotents generate the algebra is \(G_{P,k}(q)/H_P(q)^k\). The single-idempotent counting identity is a preliminary fact, not asserted to be novel.

Examples: for a two-point chain and \(k=2\), the count is \(4q(q-1)\); for a three-point chain and \(k=3\), it is \(48q^3(q-1)^2(2q+1)\). For an antichain of \(n\) points the count is the falling factorial \((2^k)_n\), independent of \(q\).

## Assumptions and scope
A finite poset \(P\) is regarded as fixed with distinguishable elements. The incidence algebra has basis \(e_{xy}\) indexed by \(x\le y\), with \(e_{xy}e_{uv}=\delta_{yu}e_{xv}\). The Jacobson radical \(J\) consists of elements of zero diagonal; \(U=1+J\) is its unipotent unit group. The number \(q\) is an arbitrary prime power, including characteristic two. The number \(k\) is a nonnegative integer, and tuples are ordered. No restrictions on the height, width, connectedness, or labeling of \(P\) are needed. Generators are taken with scalars and identity adjoined; nonunital generation is not considered.

## Proof
**Step 1: classify idempotents with prescribed diagonal.** Fix a binary diagonal map \(d:P\to\{0,1\}\), also denoting its diagonal idempotent by \(d\). Every idempotent \(E\) with diagonal \(d\) is conjugate to \(d\) under \(U\). Indeed put \(u=Ed+(1-E)(1-d)\); its diagonal entries are all one, so \(u\in U\) and is invertible. The identities \(Eu=Ed=ud\) show \(E=udu^{-1}\). Conversely all these conjugates are idempotents with diagonal \(d\). The stabilizer of \(d\) in \(U\) consists exactly of matrices whose \((x,y)\)-entry vanishes whenever \(x<y\) and \(d(x)\ne d(y)\), since the \((x,y)\)-entry of \(ud-du\) is \((d(y)-d(x))u(x,y)\). Hence the conjugacy orbit contains exactly \(q^{c(d)}\) idempotents.

**Step 2: independent cover coordinates.** If \(x\lessdot y\), the \((x,y)\)-entry in \(E^2=E\) is \((d(x)+d(y))E(x,y)=E(x,y)\). Thus \(E(x,y)=0\) when \(d(x)=d(y)\); when they differ, it is unrestricted. More explicitly, conjugating by \(1+t e_{xy}\) for a cover with differing diagonal bits alters \(E(x,y)\) by \(t(d(y)-d(x))\) and alters no other cover entry (all other possible affected pairs have an intermediate vertex). Varying these elementary conjugations makes all crossing-cover entries jointly arbitrary. Since there are \(q^{c(d)}\) idempotents in the orbit and \(s(d)\) crossing covers, every prescribed tuple of those \(s(d)\) entries has exactly \(q^{c(d)-s(d)}\) realizations. This uniformity does not assert that noncover entries themselves are independent; only the residual fiber cardinality is used.

**Step 3: generation criterion.** The theorem of Longstaff and Rosenthal [1, Main Theorem, pp. 118–120] states that a family of incidence-algebra matrices together with the identity generates the whole algebra if and only if (i) each pair of distinct vertices is separated by at least one diagonal coordinate and (ii) for every cover \(x\lessdot y\), some **linear combination** of the generators has equal diagonal entries at \(x,y\) and a nonzero \((x,y)\)-entry. Condition (i) says precisely that the simultaneous diagonal coloring \(\chi:P\to\{0,1\}^k\) is injective.

For a fixed injective \(\chi\) and a fixed cover, form vectors \(\delta=(d_a(x)-d_a(y))_{a=1}^k\in K^k\) and \(v=(E_a(x,y))_{a=1}^k\in K^k\). The vector \(\delta\) has exactly \(h=h_\chi(x,y)\ge1\) nonzero coordinates, and by Step 2 the vector \(v\) may have nonzero entries only in those coordinates. A linear combination \(\lambda\) as in criterion (ii) exists exactly when \(\lambda\cdot\delta=0\) but \(\lambda\cdot v\ne0\); elementary linear algebra shows this is equivalent to \(v\notin K\delta\). Among the \(q^h\) possible cover vectors, exactly \(q\) lie on the line \(K\delta\), leaving \(q^h-q\).

By the uniform joint distribution of cover coordinates in Step 2, different cover tests impose independent multiplicative fiber factors. The full number of \(k\)-tuples with fixed binary diagonal coloring is \(q^{\sum_{x<y}h_\chi(x,y)}\); replacing the unrestricted \(q^{h}\) factor on each cover by \(q^h-q\) gives
\[
q^{\sum_{x<y,\,x\not\lessdot y}h_\chi(x,y)}\prod_{x\lessdot y}(q^{h_\chi(x,y)}-q).
\]
Summing over the injective colorings proves the formula. Summing Step 1 over all \(d\) proves the probability denominator.

## Verification
The accompanying standalone `verify.py` directly enumerates incidence algebra elements over prime fields, tests idempotence by multiplication, and for each ordered candidate tuple builds the linear span of noncommutative words to check unital generation; it independently evaluates the claimed Hamming-cover polynomial. It reports `VERIFY_OK: 11 exhaustive configurations`, covering two-, three-, and four-point chains, a fork, a diamond, and antichains, over \(\mathbb F_2\) and \(\mathbb F_3\). In particular, over \(\mathbb F_2\) with \(k=3\) it finds \(1920\) generating tuples for the three-point chain and \(768\) for the three-point fork. These are finite checks, not proofs for arbitrary posets or prime powers; Steps 1–3 establish that generality.

## Relationship to prior work
Longstaff and Rosenthal [1] already proved the exact **existence criterion for any generating family**; it is explicitly used in Step 3 and is not new here. Khripchenko and Novikov [2] already showed conjugacy of idempotents to their diagonals; the application and finite orbit count in Step 1 are elementary. Kolegov [3] determined the **minimum number** of idempotent generators through embeddings of Hasse diagrams into a complement of a hypercube; in particular the positivity criterion implicit in the displayed polynomial is not claimed as new. The contribution assessed here is the full, rank-free **number of ordered generating idempotent tuples for all finite posets, field sizes and lengths**, including its quantitative cover penalties and exact random-generation probability. A later study of random unrestricted incidence-algebra generators [4] addresses a different sampling population.

## Limitations
The formula may require summing up to \((2^k)^{|P|}\) assignments; no polynomial-time evaluation guarantee is implied. It does not enumerate tuples up to conjugacy or algebra automorphisms and does not apply without change to general coefficient rings or nonunital generation. The complete primary text of Kolegov [3] could not be inspected through accessible sources; its abstract describes minimum generator numbers, but a hidden equivalent exact enumeration cannot be ruled out. Other formulations under probabilistic generation or structural matrix algebra terminology could have appeared previously. Independent external mathematical validation has not been performed.

## References
[1] W. E. Longstaff and P. Rosenthal, *Generators of matrix incidence algebras*, Australasian Journal of Combinatorics 22 (2000), 117–121, https://ajc.maths.uq.edu.au/pdf/22/ocr-ajc-v22-p117.pdf (Main Theorem, pp. 118–120).

[2] N. S. Khripchenko and B. V. Novikov, *Finitary incidence algebras*, arXiv:0803.0069 (2008), https://arxiv.org/html/0803.0069v1 (Theorem 3, conjugacy of idempotents).

[3] N. A. Kolegov, *Idempotent generators of incidence algebras*, Bulletin of the Australian Mathematical Society 110 (2024), 488–497, https://doi.org/10.1017/S0004972724000078 (first online 5 March 2024; abstract accessible, full text not obtained).

[4] N. Kolegov, *On the probability of generating matrix incidence rings* (2025), https://doi.org/10.1007/s13366-025-00821-x (abstract on unrestricted generators; later than the primary source and not a basis for the middle-period assignment).
