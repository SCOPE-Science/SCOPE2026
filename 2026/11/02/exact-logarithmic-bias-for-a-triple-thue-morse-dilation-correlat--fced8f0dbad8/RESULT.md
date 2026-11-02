# Exact logarithmic bias for a triple Thue--Morse dilation correlation

## Finding

Let \(s_2(n)\) be the number of ones in the base-two expansion of a nonnegative integer \(n\), and set \(t(n)=(-1)^{s_2(n)}\). For every integer \(r\geq 0\), put
\[
C_r=\sum_{n=0}^{2^r-1}t(n)t(3n)t(5n).
\]
Then
\[
\boxed{C_0=1,\qquad C_r=-2\left\lfloor\frac{r-1}{2}\right\rfloor\quad(r\geq1).}
\]
Equivalently, as a formal power series,
\[
\boxed{\sum_{r\geq0}C_r z^r=1-\frac{2z^3}{(1-z)(1-z^2)}.}
\]
Thus, for each \(r\geq1\), among the \(2^r\) integers \(0\leq n<2^r\), the numbers for which \(s_2(n)+s_2(3n)+s_2(5n)\) is even and odd are, respectively,
\[
\boxed{2^{r-1}-\left\lfloor\frac{r-1}{2}\right\rfloor\quad\text{and}\quad
2^{r-1}+\left\lfloor\frac{r-1}{2}\right\rfloor.}
\]
In particular, the unnormalized correlation is of logarithmic order in the dyadic cutoff rather than polynomial order.

## Assumptions and scope

All digits are ordinary base-two digits of nonnegative integers, and each sum contains every integer in the indicated half-open interval, including zero. The multipliers are exactly the first three positive odd integers, \(1,3,5\); the statements hold for every integer \(r\geq0\). The assertion concerns simultaneous *multiplicative dilations*, not translations by fixed offsets.

## Proof

Write a binary input \(n=\sum_{j=0}^{r-1}b_j2^j\) with digits \(b_j\in\{0,1\}\), read from least to most significant, allowing leading zero digits. Maintain the pair of nonnegative carries \((c,d)\) for the products \(3n\) and \(5n\), initially \((0,0)\). On reading digit \(b\), define \(u=3b+c\) and \(v=5b+d\). The next carries are \((\lfloor u/2\rfloor,\lfloor v/2\rfloor)\), and the parity contribution of this digit to the three digit sums is \(b+(u\bmod2)+(v\bmod2)\). Therefore the transition has weight \((-1)^{b+(u\bmod2)+(v\bmod2)}\). Once all \(r\) digits are consumed, the still-unread upper parts of the two products are precisely the carries \(c,d\), contributing the terminal weight \(t(c)t(d)\).

Starting at \((0,0)\), the closed set of reachable carry states, in a fixed order, is
\[
(0,0),\ (1,2),\ (0,1),\ (2,3),\ (1,3),\ (1,1),\ (2,4).
\]
Let \(M_{ij}\) be the sum of transition weights (over the two possible input bits) from state \(i\) to state \(j\). Explicitly, in the displayed order,
\[
M=\begin{pmatrix}
1&-1&0&0&0&0&0\\
0&0&-1&1&0&0&0\\
-1&0&0&0&1&0&0\\
0&0&0&0&0&-1&1\\
0&0&1&0&0&0&-1\\
1&0&0&-1&0&0&0\\
0&1&0&0&0&0&-1
\end{pmatrix},\qquad
w=\begin{pmatrix}1\\1\\-1\\-1\\-1\\1\\1\end{pmatrix}.
\]
The digit-by-digit construction, including terminal carries, proves the exact identity
\[
C_r=e_1^\mathsf{T}M^rw\qquad(r\geq0),
\]
where \(e_1\) is the first coordinate vector. A direct integer-matrix multiplication gives the finite algebraic identity
\[
\boxed{M(M^2-I)^3=0.}
\]
The accompanying self-contained checker regenerates all fourteen weighted transitions and verifies this entire matrix identity by integer arithmetic; the displayed matrix makes the identity independently reproducible without trusting a numerical approximation. Consequently, for every \(r\geq0\),
\[
C_{r+7}-3C_{r+5}+3C_{r+3}-C_{r+1}=0.
\]
Direct multiplication of the same seven-state matrix gives
\[
(C_0,C_1,\ldots,C_6)=(1,0,0,-2,-2,-4,-4).
\]
Set \(d_0=1\) and \(d_r=-2\lfloor(r-1)/2\rfloor\) for \(r\geq1\). On each parity class of positive indices, \(d_r\) is an affine function of \(r\). Its third forward difference with step two is zero, so \(d_{r+7}-3d_{r+5}+3d_{r+3}-d_{r+1}=0\) for every \(r\geq0\). The first seven \(d_r\) equal the seven \(C_r\) above. Induction using the order-seven recurrence yields \(C_r=d_r\) for every \(r\geq0\).

Finally, the elementary geometric-series identity \(\sum_{r\geq1}\lfloor(r-1)/2\rfloor z^r=z^3/((1-z)(1-z^2))\) proves the generating function. If \(E_r\) and \(O_r\) denote the even- and odd-parity populations, then \(E_r+O_r=2^r\) and \(E_r-O_r=C_r\). Their asserted exact counts follow.

## Verification

Run `python3 verify.py` using Python 3.8 or later. The script independently generates the weighted transfer matrix from the carry rule, confirms the seven listed states are closed, performs exact integer arithmetic to certify \(M(M^2-I)^3=0\), checks the initial conditions and twenty transfer-matrix values, and independently evaluates the original sum directly for all sixteen cutoff exponents \(0\leq r\leq15\) (65,535 summands across these tests). The completed execution printed a PASS message. The unrestricted conclusion follows from the proof and exact matrix certificate, not from those finite direct sums.

## Relationship to prior work

Baake and Coons (first public posting 2022-09-15) study Thue--Morse higher-order correlations formed by **fixed additive shifts** and their asymptotic means. Their vanishing of stationary odd-order correlations does not determine this nonstationary three-dilation correlation or its exact finite dyadic sums. Charlier, Cisternino and Massuir treat automata for multiplying and translating the Thue--Morse set, a related digit-automata framework but not this joint parity count. Morgenbesser, Shallit and Stoll study Thue--Morse at individual integer multiples, not the three-way signed product. An exact joint statistic requires the seven-state weighted carry calculation above.

## Limitations

Only the dyadic intervals and exactly the multipliers \(1,3,5\) are classified. The proof does not give formulas for arbitrary cutoff lengths or arbitrary dilation triples. A related earlier result may exist in literature not retrievable through the inspected full texts and available bibliographic searches; this work does not assert priority over uninspected sources. Independent scientific validation has not been performed.

## References

1. Michael Baake and Michael Coons, *Correlations of the Thue--Morse sequence*, first posted 2022-09-15, https://arxiv.org/abs/2209.07102 .
2. Émilie Charlier, Célia Cisternino, and Adeline Massuir, *Minimal automaton for multiplying and translating the Thue-Morse set*, 2019, https://arxiv.org/abs/1910.08543 .
3. Johannes F. Morgenbesser, Jeffrey Shallit, and Thomas Stoll, *Thue-Morse at Multiples of an Integer*, 2010, https://arxiv.org/abs/1009.5357 .
4. Christian Mauduit, *Multiplicative properties of the Thue-Morse sequence*, 2002, https://doi.org/10.1023/A:1015241900975 . Full text not inspected.
