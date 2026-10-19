# Sharp full-spark transition for four Fourier rows on twice prime-power cycles

## Finding
For every odd prime \(p\) and integer \(k\ge1\), put \(N=2p^k\), \(R=\{0,1,2,5\}\), and \(\omega=\exp(2\pi i/N)\). The four-row partial discrete Fourier transform
\[
F_R=(\omega^{rt})_{r\in R,\;0\le t<N}
\]
is **full spark**—every four distinct columns are independent—if and only if \(p\ne5\). Thus this explicit fixed row mask gives full-spark harmonic frames for every twice-prime-power cycle except the family with prime factor five.

This is the first nontrivial contrast after the consecutive four-row mask: moving its last row from \(3\) to \(4\) produces the Schur factor \(h_1\), which necessarily vanishes on some even-order columns; moving it once more to \(5\) yields \(h_2\) and a radically different arithmetic criterion. Thus the choice of mask is the first degree-two complete-homogeneous test after the known even-order failure, rather than an arbitrary finite sample.

The following general sufficient criterion explains the result. Let \(0\le r_1<\cdots<r_m<N\) be distinct row indices, with \(m\le N\). For indeterminates \(z_1,\ldots,z_m\), divide the generalized Vandermonde determinant by its ordinary Vandermonde factor:
\[
s_{\lambda}(z_1,\ldots,z_m)=
\frac{\det(z_j^{r_i})_{i,j=1}^m}{\prod_{1\le i<j\le m}(z_j-z_i)}.
\]
The quotient is a Schur polynomial with integer coefficients. If, for a given odd prime \(p\),
\[
p\nmid s_{\lambda}(\varepsilon_1,\ldots,\varepsilon_m)
\quad\text{for every }\varepsilon\in\{-1,1\}^m,
\]
then the row-selected Fourier matrix is full spark for every modulus \(N=2p^k\) with \(N>r_m\). This is a sufficient condition, not a converse for arbitrary masks.

## Assumptions and scope
All ranks, determinants, and full-spark claims are over \(\mathbb C\). Row order affects determinants only by sign. The Fourier transform uses unnormalized entries of modulus one, but nonzero scalar row/column normalization does not affect full spark. The theorem covers every odd prime and every positive integer exponent, including \(p=3\), \(k=1\), where \(N=6\). It makes no classification claim for general composite moduli outside the twice-prime-power family or for other row masks.

## Proof
**Step 1: the signed-Schur obstruction.** Fix \(N=2p^k\) and let \(\xi\) be a primitive \(p^k\)-th root of unity. Because \(p\) is odd, every \(N\)-th root \(z_j\) has a unique representation \(z_j=\varepsilon_j\xi^{a_j}\) with \(\varepsilon_j\in\{-1,1\}\), \(a_j\in\{0,\ldots,p^k-1\}\). Suppose a maximal Fourier minor vanishes on distinct roots \(z_1,\ldots,z_m\). The ordinary Vandermonde factor is nonzero, so \(s_{\lambda}(z_1,\ldots,z_m)=0\).

Set
\[
Q(X)=s_{\lambda}(\varepsilon_1X^{a_1},\ldots,\varepsilon_mX^{a_m})\in\mathbb Z[X].
\]
Then \(Q(\xi)=0\). The cyclotomic polynomial \(\Phi_{p^k}\), the minimal polynomial of \(\xi\) over \(\mathbb Q\), divides \(Q\) in \(\mathbb Z[X]\) by monic polynomial division and Gauss's lemma. Evaluating at \(X=1\) shows
\[
p=\Phi_{p^k}(1)\mid Q(1)=s_{\lambda}(\varepsilon_1,\ldots,\varepsilon_m).
\]
Therefore if none of the signed Schur evaluations is divisible by \(p\), no maximal minor vanishes.

**Step 2: the four-row mask.** For \(R=\{0,1,2,5\}\), the generalized Vandermonde quotient is the complete homogeneous symmetric polynomial of degree two,
\[
h_2(z_1,z_2,z_3,z_4)=\sum_{1\le i\le j\le4}z_iz_j.
\]
The identity follows from the alternant definition of the Schur polynomial of partition \((2)\), or by expanding the determinant. For signs \(\varepsilon_i\), the identity
\[
h_2(\varepsilon)=\tfrac12\left(4+(\varepsilon_1+\varepsilon_2+\varepsilon_3+\varepsilon_4)^2\right)
\]
shows that the only possible values are \(2\), \(4\), and \(10\). No odd prime other than five divides any of these. Step 1 therefore proves full spark for \(p\ne5\), uniformly in \(k\).

**Step 3: sharpness at five.** Suppose \(p=5\). Since \(5\mid N\), the \(N\)-th roots include at least four distinct fifth roots of unity. On such columns, the two Fourier rows indexed by \(0\) and \(5\) are identical, because \(z^5=1\). Hence their four-column minor is zero, proving failure of full spark for every \(k\ge1\). This gives the converse.

## Verification
The included standalone `CHECK.py` computes, using integer polynomial arithmetic and SymPy, the exact factorization of the \(4\times4\) generalized Vandermonde determinant into its Vandermonde factor and \(h_2\), and all sixteen signed values. It additionally checks every four-column minor by reduction modulo the relevant cyclotomic polynomial for moduli \(N=6,10,14,18,22\). The counts checked are respectively \(15,210,1001,3060,7315\) four-column sets; no minors vanish for \(N=6,14,18,22\), while \(10\) vanish for \(N=10\). The all-degree, all-exponent assertion is proved above and not inferred from these finite tests.

Reproduction: use Python 3 with SymPy installed, then execute `python3 CHECK.py` in the directory containing this document and the checker. No external dataset is required.

## Relationship to prior work
Alexeev, Cahill, and Mixon develop full-spark partial DFTs, prove uniform distribution to be necessary for arbitrary moduli, and prove a sufficient and necessary uniform-distribution theorem when the ambient order is a prime power. Their proof includes the cyclotomic divisibility device underlying Step 1. The present statement treats the composite orders \(2p^k\), to which that prime-power equivalence does not directly apply; it exploits the additional sign factor and the exact signed evaluation of a nonconsecutive four-row Schur polynomial. The exclusion of \(p=5\) also follows from the older necessary uniform-distribution obstruction; the positive sufficiency for all other odd primes is the distinguishing point.

Published mathematical-record results for the distinct row masks \(\{0,1,2,4\}\) and \(\{0,1,3,4\}\) give different full-spark criteria. The first mask fails for every even order, while the second has its own arithmetic criterion. Specific published censuses for moduli ten and fourteen cover those isolated moduli but do not establish an unrestricted twice-prime-power theorem for the present mask.

## Limitations
The general signed-Schur condition is sufficient only and may fail to decide other patterns. The theorem establishes algebraic full spark, not numerical condition-number bounds. Although primary source material was inspected and published mathematical-record summaries were compared by implications, some potentially relevant historical full texts could not be inspected; novelty relative to all literature is not independently certified. No independent mathematical audit has been performed.

## References
1. B. Alexeev, J. Cahill, and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first public version October 17, 2011. Theorem 9 and the cyclotomic divisibility argument in Lemmas 10–11. https://arxiv.org/abs/1110.3548
2. Published published-finding corpus research record, *Exact singular minors for the near-consecutive four-row harmonic frame*, record `2026/10/4/SCOPE-exact-singular-minors-for-the-near-consecutive-four-row-harmonic--bb8a5601ae6d` (different mask).
3. Published published-finding corpus research record, *Exact full-spark criterion for the four-row Fourier pattern* \(\{0,1,3,4\}\), record `2026/10/4/SCOPE-exact-full-spark-criterion-for-the-four-row-fourier-pattern-0-1--de39e0486913` (different mask).
4. Published published-finding corpus mathematical records on complete Fourier-row classifications at orders ten and fourteen, identifiers recorded in the accompanying review.
