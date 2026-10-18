# Palindromic shell amplification of strongly pseudoperfect representations
## Finding
For any integer \(N>1\), let \(R(N)\) be the number of sets \(S\) of positive divisors of \(N\) satisfying both
\[
 d\in S\iff N/d\in S,\qquad \sum_{d\in S}d=2N.
\]
Let \(r(n)\) count those sets for \(N=n\) that contain \(1\) and \(n\). The following statement holds for **every** integer \(n>1\) with \(r(n)>0\) and **every** integer \(k\ge1\):
\[
 R(n^k)\ge r(n)^{\lceil k/2\rceil}.
\]
In fact, the explicitly defined shell-lift subfamily in the proof has cardinality **exactly** \(r(n)^{\lceil k/2\rceil}\).

For the odd base \(n=45045=3^2\cdot5\cdot7\cdot11\cdot13\), an exhaustive complementary-divisor-pair calculation gives \(r(45045)=695\). Thus every positive integer \(k\) satisfies
\[
 R(45045^k)\ge695^{\lceil k/2\rceil}\ge (45045^k)^\alpha,
 \qquad \alpha=\frac{\log695}{2\log45045}=0.3053503042\ldots.
\]
In particular, the multiplicities of representations are unbounded **among odd strongly pseudoperfect integers**.

## Assumptions and scope
A representation is an unlabelled subset of divisors, not an ordered partition. The involution \(d\mapsto N/d\) acts on the complete divisor set of \(N\); membership of a square-root divisor, when present, is unrestricted except for the sum. For the transfer theorem only the \(r(n)\) representations containing both endpoints are used. No coprimality, squarefreeness, or oddness hypothesis is needed in the general transfer theorem; oddness is used solely for its example.

## Proof
Fix \(n>1\). Every endpoint-containing representation \(S\) corresponds to an internal set \(A=S\setminus\{1,n\}\) of divisors strictly between \(1\) and \(n\). It satisfies
\[
 \sum_{d\in A}d=n-1,\qquad d\in A\iff n/d\in A.
\]
Write \(\mathcal A_n\) for this family, so \(|\mathcal A_n|=r(n)\). Given \(k\ge1\), select a sequence \((A_0,\ldots,A_{k-1})\) in \(\mathcal A_n^k\) that is palindromic: \(A_j=A_{k-1-j}\). Define
\[
 T=\{1,n^k\}\cup\bigcup_{j=0}^{k-1}\{n^jd:d\in A_j\}.
\]
Each \(n^jd\) divides \(n^{j+1}\), hence divides \(n^k\). Because \(1<d<n\), the elements of the \(j\)-th shell lie strictly between \(n^j\) and \(n^{j+1}\); different shells and the two endpoints are disjoint. This also proves injectivity of the map from palindromic sequences to \(T\): its intersection with each shell reconstructs \(A_j\) uniquely.

For \(d\in A_j\), taking the complementary divisor in \(n^k\) gives
\[
 \frac{n^k}{n^jd}=n^{k-1-j}\frac nd.
\]
Since \(A_{k-1-j}=A_j\) and \(A_j\) is closed under \(d\mapsto n/d\), the complement belongs to the matching shell. The endpoints complement each other. Finally,
\[
 \sum_{x\in T}x
 =1+n^k+\sum_{j=0}^{k-1}n^j(n-1)
 =1+n^k+(n^k-1)=2n^k.
\]
There are precisely \(r(n)^{\lceil k/2\rceil}\) palindromic sequences, proving the general theorem. Conversely, **within this shell-lift class** if a sequence of reciprocal-closed internal base sets yields a reciprocal-closed union, inspection of each disjoint shell forces \(A_j=A_{k-1-j}\). This proves the stated exact count within the class, without claiming to enumerate all representations of \(n^k\).

To establish the numerical base, \(45045=3^2\cdot5\cdot7\cdot11\cdot13\) has \(48\) positive divisors and divisor sum
\[
 \sigma(45045)=13\cdot6\cdot8\cdot12\cdot14=104832.
\]
The pair \((1,45045)\) must occur in every representation because the sum of all other divisors, \(104832-45046=59786\), is less than \(2\cdot45045=90090\). There are \(23\) other complementary divisor pairs, each of weight \(d+45045/d\), indexed by \(1<d<45045/d\). Since each endpoint-containing representation has internal sum \(45044\), their number is the exact coefficient
\[
 r(45045)=[z^{45044}]\prod_{\substack{d\mid45045\\1<d<45045/d}}
 \bigl(1+z^{d+45045/d}\bigr)=695.
\]
The coefficient is evaluated by two independent exact algorithms in the supplied standalone verifier: a \(2^{11}\)-by-\(2^{12}\) meet-in-the-middle enumeration, and a truncated dynamic program through all \(23\) weights. Both give \(695\), with no randomness or unsearched subset cases. Because \(45045\) is odd, so are all its powers. The inequality \(\lceil k/2\rceil\ge k/2\) gives the power-law lower bound.

## Verification
Run \(\texttt{python3 verify.py}\) using only the Python standard library. It confirms the base factorization/divisors, the forced endpoint pair, the \(23\) internal complementary pairs and the count \(695\) by two independent exact methods. It also constructs three distinct internal base sets and verifies divisor membership, reciprocal closure, sum and distinctness for palindromic shell choices at each \(1\le k\le6\). These finite calculations establish the finite coefficient identity and are sanity checks for the general construction; the infinitely many levels follow from the written proof.

## Relationship to prior work
Wang and Zelinsky introduce the power-lifting existence theorem in their 2026 paper, Theorem 5: **one** endpoint-containing representation of \(n\) yields a representation for every power. Their Table 1 already tabulates \(695\) representations for \(45045\); this base count is therefore **not** claimed as newly discovered. The new assertion is the mirror-shell independence mechanism and its exact count, which amplifies multiple base representations simultaneously and supplies an explicit polynomial lower bound for multiplicity along odd powers. McCormack and Zelinsky previously introduced and developed the strongly pseudoperfect notion.

## Limitations
The stated bound counts a deliberately constructed subfamily, not all representations of \(45045^k\); neither an exact full-power count nor optimality of the exponent \(\alpha\) is established. The proof does not imply positive density of strongly pseudoperfect integers. The theorem is a quantitative extension of an existing source's power construction, so an equivalent unstated or unindexed earlier counting observation remains a bibliographic risk.

## References
1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068, first public version 28 September 2026; especially Theorem 5 and Table 1. https://arxiv.org/abs/2609.36068
2. Tim McCormack and Joshua Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function*, arXiv:2312.11661 (2023), for the defining context. https://arxiv.org/abs/2312.11661
3. OEIS A334405, *Strongly pseudoperfect numbers*. https://oeis.org/A334405
