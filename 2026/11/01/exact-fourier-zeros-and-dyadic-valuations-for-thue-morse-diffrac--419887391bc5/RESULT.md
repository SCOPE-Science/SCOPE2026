# Exact Fourier zeros and dyadic valuations for Thue–Morse diffraction

## Finding
Let \(t_j=(-1)^{s_2(j)}\), where \(s_2(j)\) is the sum of the binary digits of \(j\). Its balanced autocorrelations are
\[
\eta(n)=\lim_{L\to\infty}\frac1L\sum_{j=0}^{L-1}t_jt_{j+n},\qquad n\in\mathbb Z.
\]
The limit exists, and \(\eta(n)\) is the Fourier–Stieltjes coefficient at frequency \(n\) of the Thue–Morse diffraction probability measure \(\nu\) on \(\mathbb T\). The exact vanishing set is
\[
\boxed{\{n\in\mathbb Z:\eta(n)=0\}
 =\{\pm5\cdot2^r,\ \pm7\cdot2^r:r\in\mathbb Z_{\ge0}\}.}
\]
More precisely, for every **odd** integer \(n\ge9\), put \(k=\lfloor\log_2n\rfloor\). Then
\[
\boxed{3\cdot2^{k-2}\eta(n)\ \text{is an odd integer},\qquad
 v_2(\eta(n))=2-k.}
\]
Here \(v_2\) is the rational \(2\)-adic valuation (and \(v_2(0)=+\infty\)). This quantifies nonvanishing: \(|\eta(n)|\ge 1/(3\cdot2^{k-2})\) on every odd-frequency dyadic shell \([2^k,2^{k+1})\), \(k\ge3\). The only equal consecutive coefficients are \(\eta(1)=\eta(2)\), and the only opposite consecutive coefficients at nonnegative indices are \(\eta(2)=-\eta(3)\) and \(\eta(3)=-\eta(4)\).

Consequently, for every integer \(K\ge3\), exactly \(4(K-2)\) nonzero Fourier modes with \(|n|<2^K\) are annihilated by convolution with \(\nu\). On \(L^2(\mathbb T)\), the full convolution nullspace is the closed linear span of the characters with frequencies in the displayed vanishing set.

## Assumptions and scope
The weight sequence is the standard balanced binary Thue–Morse sequence with \(t_0=1\); correlations are two-point, volume-normalized limits, **not** finite-word aperiodic autocorrelations. Frequencies are integers; the measure \(\nu\) is the unique positive probability measure whose Fourier coefficients are \(\eta(n)\). All equalities hold in exact rational arithmetic. The theorem does not apply to general substitution sequences or to other digit weights.

## Proof
The classical recursions for the Thue–Morse autocorrelations are
\[
\eta(0)=1,\quad \eta(-n)=\eta(n),\quad
\eta(2m)=\eta(m),\quad
\eta(2m+1)=-\frac{\eta(m)+\eta(m+1)}2\quad(m\ge0).
\]
The last equation at \(m=0\) gives \(\eta(1)=-1/3\). Direct exact substitution gives
\[
(\eta(1),\ldots,\eta(8))=(-1,-1,1,-1,0,1,0,-1)/3.
\]
For every integer \(n\ge4\), write \(k=\lfloor\log_2n\rfloor\), and define the rescaled adjacent-frequency vector
\[
Y_n=(A_n,B_n)=3\cdot2^{k-2}(\eta(n),\eta(n+1)).
\]
The four initial vectors are
\[
Y_4=(-1,0),\quad Y_5=(0,1),\quad
Y_6=(1,0),\quad Y_7=(0,-1).
\]
Because the floor of the binary logarithm increases by exactly one under either child map \(n\mapsto2n\) or \(n\mapsto2n+1\), the recurrence implies **exact integer** matrix identities
\[
Y_{2n}=\begin{pmatrix}2&0\\-1&-1\end{pmatrix}Y_n,
\qquad
Y_{2n+1}=\begin{pmatrix}-1&-1\\0&2\end{pmatrix}Y_n,
\quad n\ge4.
\]
Suppose \(Y_n=(A_n,B_n)\in\mathbb Z^2\) and \(A_n+B_n\) is odd. Modulo two, the first matrix sends this pair to \((0,1)\), and the second sends it to \((1,0)\). In particular the child sums are odd, and the invariant propagates to every binary descendant of the four initial indices. As every \(n\ge4\) lies in one of their descendant trees, it follows for all such \(n\) that \(Y_n\in\mathbb Z^2\) with \(A_n+B_n\) odd. In the stronger form, for every even \(n\ge8\), \(A_n\) is even and \(B_n\) odd; for every odd \(n\ge9\), \(A_n\) is odd and \(B_n\) even.

Thus \(3\cdot2^{k-2}\eta(n)=A_n\) is an odd integer for every odd \(n\ge9\), giving the valuation formula and the stated lower bound. The remaining positive odd indices \(1,3,5,7\) have coefficients \(-1/3,1/3,0,0\), respectively. By \(\eta(2m)=\eta(m)\), the positive-frequency zeros are therefore exactly the powers-of-two multiples of \(5\) and \(7\); the symmetry \(\eta(-m)=\eta(m)\) completes the classification, and \(\eta(0)=1\) excludes zero frequency. The oddness of \(A_n+B_n\) also excludes \(\eta(n)=\eta(n+1)\) and \(\eta(n)=-\eta(n+1)\) for all \(n\ge4\); the explicit initial coefficients determine the listed exceptional adjacent pairs.

For \(K\ge3\), precisely \(K-2\) nonnegative exponents \(r\) satisfy \(5\cdot2^r<2^K\), and likewise for \(7\cdot2^r\). Doubling for negative frequencies gives \(4(K-2)\). Finally, convolution with \(\nu\) acts on the standard Fourier basis by multiplication by \(\widehat\nu(n)=\eta(n)\). Plancherel and the zero classification give the stated exact nullspace, including its closure.

## Verification
A standalone standard-library Python checker, `check_thue_morse.py`, independently reconstructs the rational correlation sequence by the original recurrence and the integer vector sequence by the two child matrices. It checks all \(1\le n<65536\), compares the two constructions exactly, tests odd/even parity and the full finite zero classification, and checks dyadic-band zero counts through \(K=15\). The observed completion marker is `THUE_MORSE_DYADIC_ZERO_CERTIFICATE_OK 65535`. These finite checks are a reproducibility supplement; the matrix induction proves the infinite statement.

## Relationship to prior work
The definition, Fourier–Stieltjes interpretation, recursion, and Riesz-product background are classical; in particular Baake and Grimm (2008), equations (4), (5), and (12), give these ingredients. Baake and Coons (2022/2023) develop matrix representations and mean-value properties of the same correlations. Coons, Mazáč, Pincus-Kazmar, and Stout (2025) explicitly list the infinite zero family \(\eta(2^a+2^{a-2})=0\) for \(a\ge2\), which is the \(5\cdot2^{a-2}\) half of the classification here. None of those examined results gives the other family together with **exclusion of all other zeros**, the exact odd-shell valuations, or the resulting complete convolution nullspace. The new argument is the integral parity invariant of both child matrices, not the known recursion alone.

## Limitations
A complete search of all historical substitution/diffraction literature is not established. The 1990 paper *Autocorrelation properties of the Thue-Morse sequence and their use in synchronization* is a plausible overlap source, but its full text was not obtained; its abstract does not resolve whether it contains an equivalent classification. The theorem makes no claim about the exact magnitudes, signs, or distribution of nonzero autocorrelations beyond the stated valuation constraints, and no independent validation has been performed.

## References
1. M. Baake and U. Grimm, *The singular continuous diffraction measure of the Thue–Morse chain*, arXiv:0809.0580, initially public 2008-09-03; especially equations (4), (5), and (12). https://arxiv.org/abs/0809.0580
2. M. Baake and M. Coons, *Correlations of the Thue–Morse sequence*, arXiv:2209.07102; especially Section 3 and equation (3.1). https://arxiv.org/abs/2209.07102
3. M. Coons, J. Mazáč, A. Pincus-Kazmar, and A. Stout, *On the absolute value of the autocorrelations of the Thue–Morse sequence*, arXiv:2511.06386, initially public 2025-11-09; especially the introduction. https://arxiv.org/abs/2511.06386
4. *Autocorrelation properties of the Thue-Morse sequence and their use in synchronization*, IEEE Transactions on Communications 38 (1990), 2099–2102, DOI:10.1109/26.64649; abstract consulted, full text unavailable.
