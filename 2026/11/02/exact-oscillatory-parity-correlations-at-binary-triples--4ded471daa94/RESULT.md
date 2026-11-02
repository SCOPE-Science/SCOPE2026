# Exact oscillatory parity correlations at binary triples

## Finding

For a nonnegative integer \(n\), write \(s_2(n)\) for its binary digit sum and \(\tau(n)=(-1)^{s_2(n)}\). Define the dyadic multiplicative cross-correlation

\[
C_r=\sum_{n=0}^{2^r-1}\tau(n)\tau(3n),\qquad r\in\mathbb Z_{\ge0}.
\]

**Theorem.** For all integers \(r\ge0\),

\[
\sum_{r\ge0}C_rz^r=\frac{1-2z+3z^2}{(1-z)(1-z+2z^2)},
\qquad
C_r=1-\frac2{\sqrt7}\operatorname{Im}\!\left(\left(\frac{1+i\sqrt7}{2}\right)^r\right).
\]

In particular, \(C_0=1\), \(C_1=C_2=0\), and

\[
C_r=2C_{r-1}-3C_{r-2}+2C_{r-3}\qquad(r\ge3).
\]

Both strict inequalities \(C_r>0\) and \(C_r<0\) occur infinitely often; moreover \(C_r=O(2^{r/2})\), with the exponent sharp on infinite positive and negative subsequences.

For \(r\ge1\), let \(U_r=\sum_{0\le n<2^r}\tau(3n)\). The marginal obeys the previously known formula

\[
U_{2k+1}=2\cdot3^k\quad(k\ge0),\qquad
U_{2k}=4\cdot3^{k-1}\quad(k\ge1).
\]

For \(a,b\in\{+1,-1\}\), the **complete joint distribution** of the parities of \(n\) and \(3n\) is

\[
\#\{0\le n<2^r:\tau(n)=a,\ \tau(3n)=b\}
=\frac{2^r+bU_r+abC_r}{4}\qquad(r\ge1).
\]

Thus the classical one-coordinate excess occurs at scale \(3^{r/2}\), while the conditional two-coordinate imbalance has an exact, oscillating \(2^{r/2}\) term. Neither the marginal formula nor its original discovery is claimed here.

## Assumptions and scope

All parameters \(r\) are **nonnegative integers**, and \(n\) ranges over the half-open dyadic interval \(0\le n<2^r\). The variables \(a,b\) range over signs \(\{\pm1\}\), representing *even* and *odd* binary digit sums respectively. Multiplication is ordinary integer multiplication by \(3\), not multiplication modulo \(2^r\), and all high bits of \(3n\) are retained. Asymptotic statements concern \(r\to\infty\). The marginal identities are included for the joint-count reconstruction and credited as prior work.

## Proof

**1. Three-state carry enumeration.** Write the binary digits of \(n\) from least to most significant as \(b_0,\dots,b_{r-1}\in\{0,1\}\). In schoolbook multiplication by \(3\), set \(c_0=0\) and define output digits \(y_j\) and carries by

\[
3b_j+c_j=y_j+2c_{j+1},\quad y_j\in\{0,1\},\quad c_j\in\{0,1,2\}.
\]

The carry bound follows inductively from \(0\le3b_j+c_j\le5\). After the \(r\) input digits have been processed, the remaining high-bit contribution to \(s_2(3n)\) is exactly \(s_2(c_r)\). Because \(3b_j+c_j\equiv y_j\pmod2\), we have \(b_j+y_j\equiv c_j\pmod2\). Consequently

\[
\tau(n)\tau(3n)=(-1)^{\sum_{j<r}c_j}\tau(c_r).
\]

For every source carry \(c\), summing over both incoming binary choices gives the signed transition matrix (rows = current carry; columns = next carry)

\[
M=\begin{pmatrix}1&1&0\\-1&0&-1\\0&1&1\end{pmatrix},\quad
v=\begin{pmatrix}1\\-1\\-1\end{pmatrix},\quad e=(1,0,0).
\]

Every string of \(r\) binary digits gives exactly one path, and conversely. The terminal vector includes the complete residual carry, so **no leading bits are omitted**. It follows by finite combinatorial enumeration, valid for every \(r\), that

\[
C_r=eM^rv.
\]

**2. Rational resolvent and spectral identity.** Direct multiplication or Cramer's rule gives

\[
e(I-zM)^{-1}v=\frac{1-2z+3z^2}{(1-z)(1-z+2z^2)}.
\]

The characteristic polynomial is \((\lambda-1)(\lambda^2-\lambda+2)\). The other two eigenvalues are \(\lambda_\pm=(1\pm i\sqrt7)/2\). Matching the initial values \((C_0,C_1,C_2)=(1,0,0)\) yields

\[
C_r=1-\frac{2}{\sqrt7}\operatorname{Im}(\lambda_+^r).
\]

Cayley–Hamilton gives the displayed order-three integer recurrence without any numerical extrapolation.

**3. Exact rarefied marginal.** To count \(\tau(3n)\) alone, replace each transition sign by \((-1)^{y_j}=(-1)^{b_j+c_j}\). The resulting matrix is

\[
N=\begin{pmatrix}1&-1&0\\-1&0&1\\0&1&-1\end{pmatrix}.
\]

The same terminal vector gives \(U_r=eN^rv\) and the rational identity

\[
\sum_{r\ge0}U_rz^r=e(I-zN)^{-1}v=\frac{(1+z)^2}{1-3z^2}.
\]

Extracting coefficients proves the stated formulas, consistent with the classical Newman/Coquet marginal theory. Meanwhile \(\sum_{n<2^r}\tau(n)=0\) for every \(r\ge1\), by pairing the most significant binary bit. Expanding the product of sign indicators

\[
\mathbf1_{\tau(n)=a}\,\mathbf1_{\tau(3n)=b}
=\frac{(1+a\tau(n))(1+b\tau(3n))}{4}
\]

and summing establishes all four joint-count formulas.

**4. Sharp oscillation.** Put \(\lambda_+=\sqrt2\,e^{i\theta}\), where \(\theta\in(0,\pi/2)\) and \(2\cos\theta=1/\sqrt2\). If \(\theta/\pi\) were rational, \(e^{i\theta}\) would be a root of unity and \(2\cos\theta=e^{i\theta}+e^{-i\theta}\) would be an algebraic integer. But \(1/\sqrt2\) is not an algebraic integer: its square is the nonintegral rational number \(1/2\), whereas the square of an algebraic integer is an algebraic integer and a rational algebraic integer is an integer. Thus \(\theta/\pi\) is irrational. The sequence \(r\theta\bmod2\pi\) is dense and visits each fixed open arc infinitely often. Substituting \(\operatorname{Im}(\lambda_+^r)=2^{r/2}\sin(r\theta)\) shows that infinitely many \(r\) satisfy \(C_r\le1-2^{r/2}/\sqrt7<0\), and infinitely many satisfy \(C_r\ge1+2^{r/2}/\sqrt7>0\); in particular the order \(2^{r/2}\) cannot be reduced on either sign subsequence.

## Verification

The standalone script `verify.py` independently enumerates all values of \(n\) for each \(0\le r\le17\), recomputes the exact digit parities, checks both transition-matrix sums, all four joint cells, the marginal closed formulas, and both integer recurrences. This consists of 18 dyadic levels and \(\sum_{r=0}^{17}2^r=262143\) complete input evaluations. It reports `PASS` on completion. A separate exact symbolic matrix calculation checked \(\det(\lambda I-M)=(\lambda-1)(\lambda^2-\lambda+2)\) and the two resolvents. These finite checks are *not* the infinite proof; Steps 1–4 supply that proof.

To reproduce without third-party packages, run `python3 verify.py` from the directory containing this file.

## Relationship to prior work

Shallit's 2023 article **Rarefied Thue-Morse Sums Via Automata Theory and Logic** addresses \(\sum\tau(3n)\), proving growth facts and building automata; its classical antecedents include Newman and Coquet. These results cover the marginal \(U_r\), not the new mixed correlation \(C_r\) on both \(n\) and \(3n\). Baake and Coons' **Correlations of the Thue–Morse sequence** investigates correlations at *fixed additive offsets* and their asymptotic means; a varying offset \(3n-n=2n\) is not fixed. Charlier–Cisternino–Massuir's automaton for multiplying the Thue–Morse set concerns recognizability and state complexity, not the exact distribution of the four parity cells. The 2011 paper **Coquet-type formulas for the rarefied weighted Thue–Morse sequence** uses position-dependent binary digit weights on \(3n+j\), which does not directly supply the joint weight \(\tau(n)\tau(3n)\). The proposed contribution is therefore the exact finite-scale joint distribution and the sharp sign-changing multiplicative cross-correlation, **not** the previously known single-coordinate rarefied sum or the general carry-automaton paradigm.

## Limitations

The result concerns only the multiplier \(3\), initial prefix lengths exactly powers of two, and parity (not full digit-sum distributions). It does not supply the same formula for arbitrary cutoffs or multipliers. The 2011 weighted-sum paper was inspected through an extensive accessible publisher rendering but not downloaded as a complete article; older multiplicative-digit-correlation results and implicit automaton consequences could still overlap with the claim. The result is verified by an internal self-review only, and **independent validation has not been performed**. No assertion of exhaustive literature coverage is made.

## References

1. J. Shallit, *Rarefied Thue-Morse Sums Via Automata Theory and Logic*, arXiv:2302.09436, first public 2023-02-18. https://arxiv.org/abs/2302.09436
2. M. Baake and M. Coons, *Correlations of the Thue–Morse sequence*, arXiv:2209.07102 (2022). https://arxiv.org/abs/2209.07102
3. J. Charlier, L. Cisternino and A. Massuir, *Minimal automaton for multiplying and translating the Thue-Morse set*, arXiv:1910.08543 (2019). https://arxiv.org/abs/1910.08543
4. *Coquet-type formulas for the rarefied weighted Thue–Morse sequence*, *Discrete Mathematics* 311 (2011), 1724–1734. https://doi.org/10.1016/j.disc.2011.04.008
5. D. J. Newman, *On the Number of Binary Digits in a Multiple of Three* (1969), as referenced and contextualized in [1].
