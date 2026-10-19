# Dyadic one-gap two-binomial complexity of the period-doubling word

## Finding
Let \(p=0100010101000100\cdots\) be the fixed point of \(\sigma(0)=01\), \(\sigma(1)=00\). Write \(G_p(n)\) for the number of distinct length-\(n\) observation profiles of factors of \(p\), where the profile records occurrences of each symbol and of each ordered pair selected at positions separated by at least two. For every integer \(m\ge2\), with \(n=2^m\),
\[
G_p(n)=\begin{cases}
3n/2,&m\text{ even},\\
(17n-4)/12,&m\text{ odd}.
\end{cases}
\]
The length-\(n\) factor set has exactly \(3n/2\) members. At even \(m\) every observation class is a singleton. At odd \(m\) exactly \((n+4)/12\) classes are doubletons, and all other classes are singletons. In the latter case every collision is a pair of rotations separated by three positions of a particular primitive length-\(n\) word.

## Assumptions and scope
The alphabet is \(\{0,1\}\); the infinite word is indexed starting at position one. For \(u=u_1\cdots u_n\), a length-one count records the number of positions containing a chosen letter. For letters \(a,b\in\{0,1\}\), its one-gap count is \(c_{ab}(u)=|\{(i,j):1\le i<j\le n,\ j-i\ge2,\ u_i=a,\ u_j=b\}|\). The profile is the six-tuple of these two singleton and four one-gap pair counts. Repeated factors are regarded as identical words: \(G_p(n)\) counts profiles, not their total occurrence multiplicity. The theorem is only asserted at powers of two with \(m\ge2\).

## Proof
**1. Two rotation cycles describe every factor.** The substitution gives \(p_{2j-1}=0\) and \(p_{2j}=1-p_j\); equivalently \(p_j\equiv \nu_2(j)\pmod2\) for all \(j\ge1\). For \(n=2^m\), define the two blocks \(B_b=p_1\cdots p_{n-1}b\), where \(b\in\{0,1\}\). Every interval of \(n\) successive positive integers contains exactly one multiple of \(n\). All letters at the other positions depend only on the index modulo \(n\), because adding a multiple of \(n\) cannot change a valuation below \(m\). The exceptional multiple has either value zero or value one according to the parity of its valuation. Both possibilities occur infinitely often among multiples of \(n\); hence the factor set is exactly the union of all cyclic rotations of \(B_0\) and \(B_1\).

Put \(b_*=(m-1)\bmod2\), and call \(P=B_{b_*}\) and \(Q=B_{1-b_*}\). For \(1\le j<n/2\), \(p_{j+n/2}=p_j\), while the letters at positions \(n/2\) and \(n\) of \(P\) agree. Thus \(P\) has period \(n/2\), and \(Q\) differs from \(P\) at its last position. The number \(k_P\) of ones in \(P\) is \((n-2)/3\) when \(m\) is odd and \((n+2)/3\) when \(m\) is even. Both expressions are integers congruent to two modulo four. Therefore the period of \(P\) is exactly \(n/2\): any smaller period of a power-of-two word would imply at least four repeats, forcing the number of ones to be divisible by four. By construction \(k_Q=k_P+1\) when \(m\) is odd, and \(k_Q=k_P-1\) when \(m\) is even. Both values of \(k_Q\) are odd, and so \(Q\) has primitive period \(n\). The two cyclic orbits are disjoint because their numbers of ones differ. They contain \(n/2\) and \(n\) distinct factors, respectively.

**2. Reduction of each profile to three integers.** Neither circular word contains a pair \(11\) at adjacent cyclic positions: all odd-indexed positions are zero, and the final positions of both blocks are followed by their first zero. For any linear rotation \(u\), put \(k=|u|_1\), let \(F=u_1\) and \(L=u_n\), and let \(T\) be the number of *unrestricted* scattered ordered subsequences \(01\). Since the adjacent counts are \(N_{01}=k-F\), \(N_{10}=k-L\), \(N_{11}=0\), and \(N_{00}=n-1-2k+F+L\), the four one-gap counts are
\[
\begin{aligned}
c_{11}&=\binom{k}{2},&c_{00}&=\binom{n-k}{2}-(n-1-2k+F+L),\\
c_{01}&=T-k+F,&c_{10}&=k(n-k)-T-k+L.
\end{aligned}
\]
Consequently, among rotations of a fixed block, two profiles coincide if and only if all three numbers \(k\), \(R=T+F\), and \(S=F+L\) agree. Since \(P\) and \(Q\) have different \(k\), their profiles cannot collide.

**3. Only shifts of three can collide in the primitive orbit.** Denote the cyclic bits of either block by \(C_t\), for \(t\in\mathbb Z/n\mathbb Z\), and let \(R_t\) be the corresponding value of \(R\) in the length-\(n\) rotation beginning at \(t\). If \(1\le d<n\) and \(B=\sum_{j=0}^{d-1}C_{t+j}\), rotating by \(d\) gives \(T_{t+d}-T_t=nB-kd\); hence \(R_t=R_{t+d}\) if and only if
\[
nB-kd=C_t-C_{t+d}\in\{-1,0,1\}.
\]
For \(P\), the number of ones \(k_P\) is even with \(\gcd(n,k_P)=2\). Both \(nB\) and \(k_Pd\) are even, so the difference on the left must be zero. Divisibility then forces \(d\) to be a multiple of \(n/2\), which cannot relate two distinct rotations of the period-\(n/2\) word. All \(P\)-profiles are therefore distinct.

For \(Q\), its number of ones \(k_Q\) satisfies \(3k_Q=n-1\) if \(m\) is even and \(3k_Q=n+1\) if \(m\) is odd. In both cases \(k_Q\) is relatively prime to \(n\). The preceding congruence permits only the residues \(d\equiv 0,3,-3\pmod n\); \(d=0\) is the same rotation, so every collision must connect rotations three positions apart. We may inspect the directed shift \(d=3\) by exchanging the pair if needed.

When \(m\) is even, \(3k_Q=n-1\), so the equality of \(R\) forces \(B=1\), \(C_t=1\), and \(C_{t+3}=0\). The absence of adjacent ones yields \(C_{t-1}=C_{t+2}=0\), and thus \(S_t=C_t+C_{t-1}=1\), whereas \(S_{t+3}=C_{t+3}+C_{t+2}=0\). Hence no collision occurs.

When \(m\) is odd, \(3k_Q=n+1\), and equality of \(R\) requires \(B=1\), \(C_t=0\), and \(C_{t+3}=1\). Since the cycle avoids \(11\), its four successive bits must be \(C_tC_{t+1}C_{t+2}C_{t+3}=0101\). Equality of \(S_t=C_{t-1}+C_t\) and \(S_{t+3}=C_{t+2}+C_{t+3}\) holds precisely when \(C_{t-1}=1\). Therefore a pair of distinct rotations has an equal profile if and only if it corresponds to a cyclic occurrence of \(10101\). All such classes are doubletons: an ending rotation begins with one, whereas a starting rotation begins with zero, so no rotation can belong to two different pairs; moreover each start has a unique partner three positions ahead.

**4. Count the cyclic patterns.** Suppose \(m\) is odd. Then the primitive block \(Q\) is the genuine prefix \(p_1\cdots p_n\) (its last symbol is one). For an internal center \(j\), a cyclic pattern \(10101\) requires \(p_j=1\) and \(p_{j-2}=p_{j+2}=1\), with zero odd neighbors. When \(j\equiv2\pmod4\), one of \(j-2\) and \(j+2\) is divisible by four with valuation exactly two, so the pattern is impossible. When \(4\mid j\), both neighbors at distance two have valuation one, so the condition is simply that \(\nu_2(j)\) be odd and at least three. This characterization also covers the cyclic boundary at \(j=n\), because \(\nu_2(n)=m\) is odd and the two preceding/following cyclic residues have valuation one. The count is therefore
\[
1+\sum_{\substack{3\le r<m\\r\text{ odd}}}\frac{n}{2^{r+1}}=\frac{n+4}{12}.
\]
The pattern count subtracts one profile for each doubleton from the total of \(3n/2\) factors. For odd \(m\), this yields \(3n/2-(n+4)/12=(17n-4)/12\); for even \(m\), it yields \(3n/2\), proving all assertions.

## Verification
The standalone program `verify_pd_gap.py` constructs the two exact cyclic factor orbits, counts all one-gap subsequences directly, and independently obtains the same counts using unrestricted subsequences minus adjacent pairs. It checks all dyadic lengths from \(4\) through \(512\), performs direct quadratic profile enumeration through \(64\), checks collision-class multiplicities and the cyclic \(10101\) count, and cross-checks the factor orbits against a long substitution-generated prefix through length \(128\). These are independent finite checks; the argument above proves all \(m\ge2\).

## Relationship to prior work
Rigo, Stipulanti, and Whiteland, *Gapped Binomial Complexities in Sequences* (2023), define and study the gapped-binomial statistics; their results include other infinite words, without this dyadic period-doubling formula in the inspected text. The related ordinary (nongapped) binomial complexity literature determines dyadic period-doubling behavior for a *different, finer* observation statistic; its injectivity does not imply injectivity under one-gap observations. Work on two-abelian complexity studies adjacent-factor statistics rather than nonadjacent scattered-pair statistics. The new claim is the complete dyadic gapped-profile classification, including all doubleton classes.

## Limitations
The conclusion concerns only lengths \(2^m\) with \(m\ge2\). It does not assert a formula for arbitrary \(n\), for other infinite words, or for higher-order gap counts. Literature searches and comparisons reduce but cannot eliminate the possibility of an unindexed earlier equivalent result. Computational enumeration corroborates, but does not independently prove, the unbounded theorem.

## References
1. M. Rigo, M. Stipulanti, M. A. Whiteland, *Gapped Binomial Complexities in Sequences* (2023). Open full text: https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf ; public record: https://orbi.uliege.be/handle/2268/302524 .
2. M. Rigo, M. Stipulanti, M. A. Whiteland, *On the binomial complexity of infinite words* (2022), https://arxiv.org/abs/2201.04603 .
3. A. Parreau, M. Rigo, E. Rowland, E. Vandomme, *A new approach to the 2-abelian complexity of 2-automatic sequences*, https://arxiv.org/abs/1404.3961 .
