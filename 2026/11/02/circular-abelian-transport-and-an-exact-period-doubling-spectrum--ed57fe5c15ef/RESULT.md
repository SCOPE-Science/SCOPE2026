# Circular Abelian transport and an exact period-doubling spectrum

## Finding

For a nonempty binary word \(w\) of length \(n\), let \(L_w(t)\) and \(U_w(t)\) be the minimum and maximum numbers of ones among the \(n\) circular length-\(t\) factors, where \(0\le t\le n\), and set \(L_w(0)=U_w(0)=0\). Define \(a_w(t)=U_w(t)-L_w(t)+1\) and \(S(w)=\sum_{t=1}^{n}a_w(t)\). Thus \(a_w(t)\) is the exact number of Parikh classes of circular length-\(t\) factors, and \(S(w)\) counts length-tagged circular Abelian classes.

Let \(\mu(0)=01\) and \(\mu(1)=00\). For **every** nonempty binary \(w\), every integer \(1\le m\le n\), and every \(0\le r<n\), the entire circular Abelian spectrum of \(\mu(w)\) obeys

\[
\begin{aligned}
L_{\mu(w)}(2m)&=m-U_w(m),&U_{\mu(w)}(2m)&=m-L_w(m),\\
L_{\mu(w)}(2r+1)&=r-U_w(r),&U_{\mu(w)}(2r+1)&=r+1-L_w(r+1).
\end{aligned}
\]

Equivalently, with \(a_w(0)=1\),

\[
a_{\mu(w)}(2m)=a_w(m),\qquad
a_{\mu(w)}(2r+1)=a_w(r)+1-L_w(r+1)+L_w(r).
\]

In particular the **universal exact transport law** is

\[
\boxed{S(\mu(w))=2S(w)+n-|w|_1.}
\]

Now let \(P_k=\mu^k(0)\), for integers \(k\ge0\). These recurrences, beginning with \(L_{P_0}(0)=U_{P_0}(0)=L_{P_0}(1)=U_{P_0}(1)=0\), determine the exact circular Abelian complexity at **every length and every rank**. Its sum has the closed form

\[
\boxed{S(P_k)=\frac{(3k+10)2^k-(-1)^k}{9}\quad(k\ge0).}
\]

Consequently, \(S(P_k)/|P_k|=k/3+10/9-(-1)^k/(9\cdot2^k)\), so the mean number of circular Abelian classes per factor length grows as \(k/3+10/9+o(1)\).

## Assumptions and scope

All words are finite and binary. Circular factors are taken from one complete traversal of the periodic extension \(w^\omega\), of length at most \(|w|\), beginning at one of the \(|w|\) original positions. Parikh equivalence counts words with the same number of zeros and ones; the factor length is part of the class label for \(S\). The map \(\mu\) is applied as a morphism, and the statements hold even if \(w\) is nonprimitive or constant. The rank \(k\) may be zero.

## Proof

**1. Interval property.** For fixed \(t\), sliding a circular length-\(t\) window one position changes its number of ones by \(-1\), \(0\), or \(1\). Walking through all circular starting positions therefore reaches every integer between the observed minimum and maximum. Hence the set of observed one-counts is the full integer interval \([L_w(t),U_w(t)]\), establishing \(a_w(t)=U_w(t)-L_w(t)+1\). Moreover, lengthening a window by one symbol gives

\[
L_w(t+1)-L_w(t)\in\{0,1\},\qquad U_w(t+1)-U_w(t)\in\{0,1\}
\]

for every \(0\le t<n\). This uses both directions: every window of length \(t\) has a one-letter extension, and every window of length \(t+1\) has a length-\(t\) prefix.

**2. Parity decimation.** Write \(w=w_0\cdots w_{n-1}\) with indices modulo \(n\). In \(\mu(w)\), even positions are zero and odd positions are \(1-w_i\). A circular length-\(2m\) factor at either parity has precisely \(m\) odd positions, corresponding to a circular length-\(m\) factor of \(w\). Hence its one-count ranges exactly from \(m-U_w(m)\) to \(m-L_w(m)\).

For a length-\((2r+1)\) factor, an even starting position contributes \(r\) odd positions and one-count interval \([r-U_w(r),r-L_w(r)]\). An odd starting position contributes \(r+1\) odd positions and interval \([r+1-U_w(r+1),r+1-L_w(r+1)]\). By Step 1, the second interval starts at the first interval's left endpoint or one above it, and ends at the first interval's right endpoint or one above it. Their union is an integer interval with the claimed extreme endpoints. This proves all four extreme-count recurrences, including \(r=0\), \(m=n\), and constant words.

**3. Summation.** The even lengths contribute \(S(w)\). The odd lengths contribute

\[
\begin{aligned}
\sum_{r=0}^{n-1}a_{\mu(w)}(2r+1)
&=\sum_{r=0}^{n-1}a_w(r)+n-\big(L_w(n)-L_w(0)\big)\\
&=S(w)+n-|w|_1,
\end{aligned}
\]

because \(a_w(0)=a_w(n)=1\) and every full-length circular factor contains exactly \(|w|_1\) ones. Adding the even and odd contributions proves the universal transport law.

**4. Closed form for period doubling.** Put \(q_k=|P_k|_1\). Since every substituted symbol contributes one initial zero and the output contains a one precisely when the input is zero,

\[
q_0=0,\qquad q_k=2^{k-1}-q_{k-1}\quad(k\ge1),
\]

so \(q_k=(2^k-(-1)^k)/3\) by induction. With \(S(P_0)=1\), Step 3 gives \(S(P_k)=2S(P_{k-1})+q_k\). Summing this first-order recurrence yields

\[
S(P_k)=2^k\left(1+\sum_{j=1}^{k}\frac{q_j}{2^j}\right)=\frac{(3k+10)2^k-(-1)^k}{9}.
\]

The extreme-count recurrences inductively determine each lengthwise \(a_{P_k}(t)\), completing the classification.

## Verification

The accompanying `checker.py` implements a direct rolling-window calculation of the minimum, maximum and number of Parikh classes for every circular window length. It exhaustively compares all formulas for all binary input words of lengths \(1\) through \(8\), and checks the complete rankwise spectra and total closed form for \(P_k\) at ranks \(0\) through \(11\). It does **not** treat finite enumeration as a proof of the statements for unrestricted length or rank.

For ranks \(k=0,1,\ldots,10\), the totals are \(1,3,7,17,39,89,199,441,967,2105,4551\).

Run: `python3 checker.py`.

## Relationship to prior work

The starting point is the well-established distinction between Abelian complexity, conjugacy-class complexity, and finer \(2\)-Abelian complexity. Parreau, Rigo, Rowland and Vandomme (arXiv:1405.3532, first public version 14 May 2014) investigate infinite-word \(2\)-Abelian complexity of period doubling and Abelian complexity of a corresponding two-block coding. Cassaigne, Fici, Sciortino and Zamboni (arXiv:1402.5843, first public version 24 February 2014) study conjugacy classes of contiguous factors of infinite words; their period-doubling example is not a finite circular Parikh spectrum. The distinct finite-circle domain and the summed statistic prevent either theorem, as stated there, from implying the formulas above. Neither work asserts the universal \(S(\mu(w))\) identity.

A related 2016 paper by Blanchet-Sadri, Seita and Wise, *Computing abelian complexity of binary uniform morphic words*, studies Abelian complexity of infinite morphic words. The full article could not be inspected; this leaves a historical-priority risk, although its accessible abstract concerns a different factor domain. The claim here concerns circular windows of complete finite iterates and an exact identity valid for arbitrary finite inputs, not the Abelian complexity of the infinite fixed point.

## Limitations

These formulas count Parikh classes, not distinct factors, their multiplicities, or conjugacy classes. The period-doubling specialization uses only complete iterates \(P_k\), not arbitrary prefixes. The two-length recurrences determine the full spectrum recursively but are not an explicit nonrecursive digit formula for each individual length. Exhaustive independent mathematical validation and complete historical-priority verification have not been performed.

## References

1. A. Parreau, M. Rigo, E. Rowland and É. Vandomme, *A new approach to the 2-regularity of the ℓ-Abelian complexity of 2-automatic sequences*, first public version 14 May 2014, arXiv:1405.3532, https://arxiv.org/abs/1405.3532. MSC 68R15.
2. J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, first public version 24 February 2014, arXiv:1402.5843, https://arxiv.org/abs/1402.5843.
3. F. Blanchet-Sadri, D. Seita and D. Wise, *Computing abelian complexity of binary uniform morphic words*, Theoretical Computer Science **640** (2016), 41–51, DOI:10.1016/j.tcs.2016.05.046 (full text not inspected).
