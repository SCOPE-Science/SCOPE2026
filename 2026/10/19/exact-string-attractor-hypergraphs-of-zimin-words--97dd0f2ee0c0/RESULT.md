# Exact string-attractor hypergraphs of Zimin words

## Finding

Let \(Z_1=1\) and \(Z_n=Z_{n-1}\,n\,Z_{n-1}\) for integers \(n\ge2\), treating \(1,\ldots,n\) as distinct symbols. Let \(P_{n,k}\) be the set of positions occupied by symbol \(k\) in \(Z_n\). For every \(n\ge1\) and every set of positions \(\Gamma\subseteq\{1,\ldots,2^n-1\}\),

\[
\boxed{\Gamma\text{ is a string attractor of }Z_n\ \Longleftrightarrow\ \Gamma\cap P_{n,k}\ne\varnothing\text{ for every }1\le k\le n.}
\]

More strongly, the inclusion-minimal occurrence-coverage sets of all nonempty contiguous factors are **exactly** \(P_{n,1},\ldots,P_{n,n}\). Thus testing the \(n\) single-symbol factors is a complete and irredundant certificate even for position sets of arbitrary cardinality.

The attractor-size generating polynomial is exactly

\[
\boxed{A_n(t)=\sum_{\Gamma\text{ attracts }Z_n}t^{|\Gamma|}=\prod_{k=1}^{n}\left((1+t)^{2^{n-k}}-1\right).}
\]

In particular, the smallest attractor size is \(n\), and there are exactly \(2^{n(n-1)/2}\) smallest attractors. For \(n\ge2\), the least possible span \(\max\Gamma-\min\Gamma\) among smallest attractors is \(2^{n-2}\), attained by exactly \(2^{1+(n-2)(n-3)/2}\) of them. At \(n=1\), both the minimum span and its single realizing attractor are zero and one, respectively.

## Assumptions and scope

A **factor** is a nonempty contiguous substring. A position set \(\Gamma\) is a string attractor of a finite word \(W\) if every distinct factor \(u\) of \(W\) has *some* occurrence whose interval meets \(\Gamma\). The requirement is one occurrence per factor, not every occurrence.

For any factor \(u\) define its **coverage** \(\operatorname{Cov}_W(u)\) to be the union of the position intervals of all occurrences of \(u\). The inclusion-minimal factor coverages form an antichain. Position indices here are one-based. The family comprises all \(n\ge1\), with no asymptotic or alphabet-growth restrictions. The alphabet size grows with \(n\); these are the standard finite Zimin words, not arbitrary nonerasing images of Zimin patterns.

## Proof

**Ruler-word identity.** For each integer \(1\le j<2^n\), the symbol at position \(j\) is \(1+\nu_2(j)\), where \(\nu_2(j)\) is the exponent of \(2\) dividing \(j\). Indeed, for \(n=1\) the identity is immediate. Under the recursion, the central position \(2^{n-1}\) has symbol \(n\); for positions to the right, \(\nu_2(2^{n-1}+r)=\nu_2(r)\) whenever \(1\le r<2^{n-1}\), giving the same sequence in both halves. In particular,

\[
P_{n,k}=\{j:1\le j<2^n,\ \nu_2(j)=k-1\},\qquad |P_{n,k}|=2^{n-k}.
\]

**Transport of a factor to every occurrence of its largest letter.** Fix any nonempty factor \(u\) of \(Z_n\), and write \(k\) for the largest symbol appearing in \(u\). The positions carrying letters greater than \(k\) are precisely the positive multiples of \(2^k\) inside \(Z_n\). The intervals between them, including the first and last boundary intervals, are \(2^{n-k}\) identical copies of \(Z_k\): for every integer \(a\) with \(0\le a<2^{n-k}\) and \(1\le r<2^k\),

\[
Z_n[a2^k+r]=1+\nu_2(a2^k+r)=1+\nu_2(r)=Z_k[r].
\]

Because \(u\) has no symbol larger than \(k\), an occurrence of \(u\) cannot pass through a multiple of \(2^k\). It therefore lies wholly inside one copy of \(Z_k\). Because \(u\) contains symbol \(k\), it necessarily crosses that copy's unique \(k\) position \(a2^k+2^{k-1}\). Reproduce the same relative occurrence in every other copy of \(Z_k\). This shows

\[
\boxed{P_{n,k}\subseteq\operatorname{Cov}_{Z_n}(u).}
\]

Conversely, the one-symbol factor consisting of \(k\) has coverage exactly \(P_{n,k}\). The sets \(P_{n,1},\ldots,P_{n,n}\) are nonempty and pairwise disjoint. Every factor coverage contains at least one of them, and each itself occurs as a factor coverage, so the inclusion-minimal coverages are exactly these \(n\) sets.

**Attractor characterization.** The definition says that \(\Gamma\) is an attractor precisely if it intersects every factor coverage. If it intersects each \(P_{n,k}\), it intersects the coverage of a factor whose largest symbol is \(k\), by the inclusion just proved. Conversely, if \(\Gamma\) misses \(P_{n,k}\), it cannot attract the one-symbol factor \(k\). This proves the equivalence and the irredundancy: omitting any one single-symbol coverage permits a position set meeting every remaining symbol class but not that class.

**Counting and minimum span.** For each symbol class \(P_{n,k}\) of size \(2^{n-k}\), one can choose any nonempty subset, independently. Multiplication gives \(A_n(t)\). A smallest attractor chooses exactly one position from every class, hence has size \(n\) and has \(\prod_{k=1}^n2^{n-k}=2^{n(n-1)/2}\) possibilities.

For \(n\ge2\), the sole symbol \(n\) lies at \(2^{n-1}\); the two occurrences of \(n-1\) lie at \(2^{n-2}\) and \(3\cdot2^{n-2}\). Every smallest attractor must include the first position and one of the latter two, so its span is at least \(2^{n-2}\). Equality forces all other selected positions to lie in the closed interval between that chosen \(n-1\) and \(n\). Each such interval has interior word exactly \(Z_{n-2}\) when \(n\ge3\). Consequently there are \(2^{(n-2)(n-3)/2}\) choices of representatives of letters \(1,\ldots,n-2\) within either interval, giving twice that number; for \(n=2\) the interiors are empty and the same formula yields two choices. The case \(n=1\) is immediate.

## Verification

The standalone script `check.py` constructs words by the recurrence, enumerates every distinct factor and every factor's union-of-occurrence coverage, calculates the exact inclusion-minimal coverage antichain, and checks that it equals the letter-position partition. It also exhaustively checks every minimum-cardinality attractor for orders \(1\le n\le6\), including its span and the number of minimum-span solutions. These finite tests are independent checks and are not the proof for arbitrary \(n\).

Run `python3 check.py` with Python 3 (standard library only); `check_output.txt` contains the matching output. The explicit ruler identity and coverage-transport argument, rather than enumeration, establish the unlimited-order theorem.

## Relationship to prior work

Recent exact attractor work by Banbara et al. classifies minimum-cardinality attractors of Fibonacci, period-doubling, and Thue–Morse words. Faro, Marino, and Pavone additionally identify all inclusion-minimal factor coverages of finite Thue–Morse words; their resulting arbitrary-cardinality certificate has \(8n-22\) constraints. These theorems concern different word families and do not imply that **every** factor coverage of a Zimin word contains the entire position class of its largest letter. The present structural transport establishes that stronger property and gives an \(n\)-constraint exact certificate and an all-sizes polynomial.

Béal, Crochemore, and Romana study general algorithmic attractor checking and greedy construction; those procedures do not give this family-specific formula. Connor studies the distribution of Zimin-pattern occurrences rather than string attractors. The recursive Zimin definition and their significance as unavoidable patterns predate the present statement.

## Limitations

The result applies to the literal Zimin words over \(n\) **distinct** symbols. It does not assert the same property for a finite-alphabet morphic image where symbols are identified or replaced by strings; the location classes then cease to be disjoint and the proof does not apply. The formula is a structural equality, not a claim that every similar recursively defined word has the same certificate. The literature comparison cannot exclude differently titled or unindexed prior work. Computational checks stop at order six, while the mathematical proof covers all orders.

## References

1. S. Faro, F. P. Marino, A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue--Morse Words*, arXiv:2610.10950v1, first public October 7, 2026; especially Sections 3 and 6 on canonical coverage antichains. https://arxiv.org/abs/2610.10950
2. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue--Morse Words*, arXiv:2602.16152v1, first public February 18, 2026 (also consulted v2). https://arxiv.org/abs/2602.16152
3. M.-P. Béal, M. Crochemore, G. Romana, *Checking and producing word attractors*, arXiv:2509.08503v1, first public September 10, 2025 (also consulted v2). https://arxiv.org/abs/2509.08503
4. J. Connor, *A Self-Referential Property of Zimin Words*, arXiv:1611.01061v1, November 3, 2016, Definition 1.1. https://arxiv.org/abs/1611.01061
5. D. Kempa, N. Prezza, *At the Roots of Dictionary Compression: String Attractors*, STOC 2018, DOI:10.1145/3188745.3188814.
