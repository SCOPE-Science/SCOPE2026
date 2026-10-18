# Exact three-block binary-weight spectrum of Mersenne multiples

## Finding
For an integer \(m\ge2\), put \(T=2^m\), \(Q=T-1\), and let \(s_2(N)\) count the ones in the ordinary binary expansion of a nonnegative integer. Define the finite weight enumerator
\[
W_m(z)=\sum_{k=1}^{T^2+T+1}z^{s_2(kQ)}.
\]
These are exactly the positive multiples of \(Q\) strictly below \(2^{3m}\). Set
\[
K(z)=\begin{pmatrix}3z&z^3\\1&3z^2\end{pmatrix},\qquad A_m(z)=\bigl(K(z)^m\bigr)_{0,0}.
\]
Then the **exact weight distribution**, uniformly for every \(m\ge2\), is
\[
\boxed{W_m(z)=A_m(z)+z^{3m}A_m(z^{-1})+z^{3m}.}
\]
In particular, the attained Hamming weights are precisely
\[
\{m,m+1,\ldots,2m\}\cup\{3m\}.
\]
Thus all weights from \(2m+1\) through \(3m-1\) are impossible in this interval, even though every weight from \(m\) through \(2m\) occurs. The exact boundary multiplicities include
\[
[z^m]W_m(z)=[z^{2m}]W_m(z)=3^m,\qquad
[z^{m+1}]W_m(z)=m3^{m-2},\qquad
[z^{3m}]W_m(z)=1.
\]
The first multiplier producing weight \(m+1\) is exactly \(k=T+3\):
\[
\min\{k\ge1:s_2(k(2^m-1))=m+1\}=2^m+3.
\]
Moreover, the auxiliary polynomial satisfies the fixed-order recurrence
\[
A_0(z)=1,\quad A_1(z)=3z,\quad
A_{r+2}(z)=3z(1+z)A_{r+1}(z)-8z^3A_r(z)\quad(r\ge0),
\]
so the complete enumerator has a constant-size symbolic recurrence, rather than an enumeration growing exponentially with \(m\).

## Assumptions and scope
The exponent \(m\) is an arbitrary integer at least two. There is no primality assumption on \(Q=2^m-1\). The specified finite interval is the **three-block interval** \(0<N<2^{3m}\), where a block has exactly \(m\) binary digits (leading zeroes allowed inside blocks). No claim is made about the distribution at other length cutoffs, bases other than two, or the absence of any of the displayed gap weights among larger multiples.

## Proof
**1. Reduction to three equal-length blocks.** Every \(N\) with \(0\le N<T^3\) has a unique representation
\[
N=x+Ty+T^2w,\qquad 0\le x,y,w<T.
\]
Its Hamming weight is \(s_2(N)=s_2(x)+s_2(y)+s_2(w)\). As \(T\equiv1\pmod{Q}\), the condition \(Q\mid N\) is equivalent to \(Q\mid(x+y+w)\). Since \(0\le x+y+w\le3Q\), the only possible sums are \(0,Q,2Q,3Q\). Sum zero gives \(N=0\), excluded. Sum \(3Q\) forces \(x=y=w=Q\), giving the unique all-one word \(N=T^3-1\), of weight \(3m\). Bitwise complement of every block bijects triples of sum \(Q\) with triples of sum \(2Q\), and changes total weight \(d\) to \(3m-d\).

**2. Transfer matrix for sum \(Q\).** Write the three words \(x,y,w\) in columns of \(m\) binary digits, from least significant to most significant. To sum to the all-one word \(Q\), the initial and final carry must both be zero. The intermediate carry lies in \(\{0,1\}\): indeed, if incoming carry is zero, respectively one, the number of input ones in a column must be odd, respectively even. With outgoing carry \(c'\), the four possibilities (incoming carry, outgoing carry) have the following numbers of choices and contributed weights:
\[
0\to0:(3,1),\quad0\to1:(1,3),\quad
1\to0:(1,0),\quad1\to1:(3,2).
\]
For instance \(0\to1\) requires three input ones; \(1\to0\) requires zero. Therefore the transfer matrix tracking the power of \(z\) contributed by each column is exactly \(K(z)\), and \(A_m(z)=(K(z)^m)_{0,0}\) enumerates all triples of sum \(Q\), by their joint weight. Complementing and adding the single all-one word yields the boxed polynomial identity. The upper summation bound is \((T^3-1)/Q=T^2+T+1\), so the algebra enumerates precisely the claimed multiples and no others.

**3. Exact support and boundary coefficients.** A return path from carry zero to carry zero that never leaves state zero has weight \(m\) and exactly \(3^m\) choices. Any other return path has one or more excursions away from zero. A single excursion occupying \(\ell\) consecutive columns, where \(2\le\ell\le m\), has transitions \(0\to1\), then \(\ell-2\) loops \(1\to1\), then \(1\to0\). It contributes weight \(2\ell-1\), whereas the same \(\ell\) positions remaining at carry zero contribute weight \(\ell\). The excursion increases the weight by exactly \(\ell-1\). Consequently every return path has weight in \([m,2m-1]\). Conversely one excursion of each possible length \(2\le\ell\le m\) gives each weight \(m+1,\ldots,2m-1\), alongside the all-zero-carry path of weight \(m\). Thus
\[
\operatorname{supp} A_m=\{m,\ldots,2m-1\}.
\]
The complementary summand has support \(\{m+1,\ldots,2m\}\), and the remaining singleton has weight \(3m\). The full spectrum follows.

The coefficient of degree \(m\) in \(A_m\) is \(3^m\). Its leading coefficient, at \(2m-1\), arises only from the excursion using all \(m\) columns, so equals \(3^{m-2}\). At degree \(m+1\), exactly one excursion of length two may begin in any of the \(m-1\) successive positions, with \(3\) choices at each of the \(m-2\) other columns, giving \((m-1)3^{m-2}\) in \(A_m\). The complement adds \(3^{m-2}\) to this degree, establishing \(m3^{m-2}\). Complementation also identifies the coefficient of degree \(2m\) with \([z^m]A_m=3^m\). The all-one triple accounts for the unique coefficient at \(3m\).

**4. Least multiplier of next-to-minimum weight.** For \(1\le k\le T+1\), \(kQ\le T^2-1\), so it has two \(m\)-bit blocks \(x+Ty\). Divisibility forces \(x+y=Q\) or \(2Q\). In the first case the blocks are complementary and their joint weight is \(m\); the latter case forces both blocks to be all ones and weight \(2m\). Thus none of these multipliers has weight \(m+1\). The next multiplier \(k=T+2\) gives \(kQ=T^2+T-2\), whose weight is \(1+(m-1)=m\). Finally \(k=T+3\) gives \(kQ=T^2+2T-3\); because \(2T-3\) has exactly \(m\) binary ones for \(m\ge2\), its weight is \(m+1\). This proves the least multiplier statement.

**5. Recurrence.** The trace and determinant of \(K(z)\) are \(3z(1+z)\) and \(8z^3\), respectively. The Cayley–Hamilton identity applied to successive powers of \(K(z)\), then to their \((0,0)\)-entries, gives the stated recurrence with initial values \(A_0=1\), \(A_1=3z\).

## Verification
The accompanying standalone Python 3 checker `VERIFY.py` independently constructs the polynomial through the four carry transitions and also enumerates every positive multiple in the finite interval directly using exact integer multiplication and binary popcounts for \(1\le m\le8\). The predicted and direct weight histograms agree in all eight cases, covering \(87898\) distinct positive multiples in total. The script also checks the exact support, boundary coefficients, total count, and least multiplier \(T+3\) for \(m\ge2\). Run `python3 VERIFY.py` from the directory containing the file. This finite cross-check is not the proof of the arbitrary-\(m\) result; the preceding carry-path argument supplies the uniform proof.

## Relationship to prior work
The classical literature on binary Hamming weights of multiples includes Stolarsky's work on anomalous digit frequencies. Elsholtz (2016) invokes the minimum-weight phenomenon while investigating small-weight multiples of primes. Clokie and coauthors (2020), Section 3, give Mersenne sturdiness and more general minimum-weight arguments, while their Theorem 4 ensures higher weights eventually occur among unbounded multiples. Those assertions do not provide the exact **three-block** weight enumerator, the uniform matrix polynomial, the finite-cutoff spectral gap, or the least multiplier of weight \(m+1\). An algorithm deciding the minimum weight for an individual input modulus likewise does not imply this uniform, all-weight, finite-length classification.

Targeted mathematical searches also considered the equivalent problems of summing three \(m\)-bit integers to an all-one word and enumerating Hamming-weight-constrained residues modulo a Mersenne number. The searched published-result abstracts and selected neighboring full texts did not provide a covering formula. This is a best-knowledge comparison, not a universal uniqueness guarantee. The 1980 Stolarsky article's full text could not be read, so possible statements hidden in that source remain a residual literature risk; later works explicitly attribute the **minimum-weight** phenomenon to it, not the exact three-block enumerator.

## Limitations
The claims concern only strictly positive multiples smaller than \(2^{3m}\). The gap \(2m+1,\ldots,3m-1\) is a finite-window statement and must not be interpreted as a global absence of multiples of those weights. A general finite-state computation could yield numeric histograms for individual \(m\), but numerical agreement alone does not establish the proof or originality. No independent mathematical audit is claimed. The historical Stolarsky full text remains an access limitation in the literature comparison.

## References
1. C. Elsholtz, “Almost all primes have a multiple of small Hamming weight,” arXiv:1602.05974v1, first submitted 18 February 2016; *Bull. Aust. Math. Soc.* 94 (2016), 224–235. https://arxiv.org/abs/1602.05974
2. D. Clokie, F. Lidbetter, T. Molina Lovett, J. Shallit, D. Witzman, “Computational Aspects of Sturdy and Flimsy Numbers,” arXiv:2002.02731v1, 2020. https://arxiv.org/html/2002.02731v1
3. K. Stolarsky, “Integers whose multiples have anomalous digital frequencies,” *Acta Arith.* 38 (1980), 117–128, DOI 10.4064/aa-38-2-117-128 (bibliography verified; full text unavailable).
4. S. S. Wagstaff Jr., “Prime Numbers with a Fixed Number of One Bits or Zero Bits in Their Binary Representation,” *Experimental Mathematics* 10 (2001), 267–273, DOI 10.1080/10586458.2001.10504447 (partial text inspected).
