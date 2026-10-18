# Exact dyadic residue spectra of Narayana numbers in Mersenne rows

## Finding
For integers \(r\ge s\ge2\), put
\[
n=2^r-1,\qquad M=2^s,\qquad t=2^{r-s+1},\qquad B=2^{s-1}.
\]
Write the Narayana number as
\[
\mathcal N(n,k)=\frac1n\binom nk\binom n{k+1},\qquad 0\le k<n.
\]
All occurrences of inverses below are taken in the unit group modulo \(M\). For each \(1\le m<B\), write \(m=2^{v_m}u_m\) with \(u_m\) odd and define
\[
w_m=1-2^{s-1-v_m}u_m^{-1}\pmod M,\qquad
F_0=1,\qquad F_j=\prod_{m=1}^j w_m\pmod M.
\]
Then the **complete row-residue law** is
\[
\mathcal N(n,k)\equiv
\begin{cases}
F_{\lfloor k/t\rfloor}^{\,2}&\text{if }t\nmid(k+1),\\
F_{m-1}F_m&\text{if } k=mt-1,\ 1\le m<B
\end{cases}\pmod M.
\]
For every residue \(a\in\mathbb Z/M\mathbb Z\), its exact number of occurrences in the row is
\[
C_{r,s}(a)=(t-1)\sum_{j=0}^{B-1}\mathbf1_{F_j^2\equiv a\ (\bmod M)}+
\sum_{m=1}^{B-1}\mathbf1_{F_{m-1}F_m\equiv a\ (\bmod M)}.
\]
Thus for any fixed precision \(s\), the entire residue spectrum of every row with \(r\ge s\) is obtained from just \(2^{s-1}-1\) factors, independently of the row length.

**Exact modulus-16 classification.** For every \(r\ge4\), there are precisely four attainable residues, with multiplicities
\[
C_{r,4}(1)=C_{r,4}(9)=2^{r-1}-2,\qquad C_{r,4}(13)=2,\qquad C_{r,4}(7)=1,
\]
and \(C_{r,4}(a)=0\) for every other residue \(a\pmod{16}\). The exceptional value \(13\) occurs exactly at \(k=2^{r-2}-1\) and \(k=3\cdot2^{r-2}-1\); the unique \(7\) occurs exactly at \(k=2^{r-1}-1\).

## Assumptions and scope
All integers \(r,s,k\) satisfy \(r\ge s\ge2\) and \(0\le k<2^r-1\). The indexing \(k\) starts at zero, so \(\mathcal N(n,k)\) corresponds to the usual \((k+1)\)-st entry of row \(n\). There are exactly \(2^r-1\) entries in this row. Every factor \(w_m\) is a well-defined odd residue, because \(v_m\le s-2\) and \(u_m\) is odd. No assertion is made about arbitrary non-Mersenne rows or about moduli not powers of two.

## Proof
Let \(Q_k=\binom{2^r-1}{k}\), for \(0\le k\le2^r-1\). The elementary product identity is
\[
Q_k=(-1)^k\prod_{j=1}^k\left(1-\frac{2^r}{j}\right).
\]
Every factor is a \(2\)-adic integer: if \(j=2^v u\) with \(u\) odd then \(2^r/j=2^{r-v}u^{-1}\). For \(j<2^r\), a factor is congruent to \(1\pmod{2^s}\) whenever \(v\le r-s\). Hence exactly the factors indexed by multiples \(j=mt\), with \(t=2^{r-s+1}\), may contribute nontrivially. These are \(m=1,\ldots,\lfloor k/t\rfloor\), and \(m<B\) since \(k\le2^r-1\). Writing \(m=2^{v_m}u_m\), their factors reduce to
\[
1-\frac{2^r}{mt}\equiv 1-2^{s-1-v_m}u_m^{-1}=w_m\pmod M.
\]
Consequently, uniformly in \(k\),
\[
Q_k\equiv(-1)^kF_{\lfloor k/t\rfloor}\pmod M.
\]
Now \(n=2^r-1\equiv-1\pmod M\), since \(r\ge s\); thus \(n\) is invertible and \(n^{-1}\equiv-1\pmod M\). Therefore
\[
\mathcal N(n,k)=n^{-1}Q_kQ_{k+1}
\equiv F_{\lfloor k/t\rfloor}F_{\lfloor(k+1)/t\rfloor}\pmod M,
\]
because \((-1)^{k+(k+1)}=-1\) cancels the factor \(n^{-1}\equiv-1\). The two floor indices are equal unless \(k+1\) is divisible by \(t\), in which case they are \(m-1\) and \(m\). This proves the two-case congruence.

For each \(j=0,\ldots,B-1\), the block \(jt\le k<(j+1)t\) contains \(t-1\) interior positions; the last block has its terminal position \(Bt-1=2^r-1\) excluded from \(k<n\). Each of the other \(B-1\) blocks contributes one boundary position \(k=mt-1\) with \(1\le m<B\). The claimed exact multiplicity follows by counting these disjoint positions. This also verifies the total \(B(t-1)+(B-1)=Bt-1=2^r-1\).

For the modulus-16 corollary take \(s=4\), so \(B=8\), and calculate in exact integer arithmetic
\[
(w_1,\ldots,w_7)=(9,13,9,15,9,5,9),\qquad
(F_0,\ldots,F_7)=(1,9,5,13,3,11,7,15)\pmod{16}.
\]
The eight squared block values are
\[
(1,1,9,9,9,9,1,1)\pmod{16},
\]
and the seven boundary values are
\[
(9,13,1,7,1,13,9)\pmod{16}.
\]
Each of \(1\) and \(9\) thus occupies four blocks of \(t-1\) ordinary positions; the boundary list contains \(1\) twice and \(9\) twice, yielding \(4(t-1)+2=4t-2=2^{r-1}-2\) positions of each residue. The remaining boundary values are two \(13\) and one \(7\). Their indices are \(k=2t-1\), \(k=6t-1\), and \(k=4t-1\), respectively. Since \(t=2^{r-3}\), these are the positions displayed in the finding. All remaining residues occur zero times.

## Verification
Run the standalone program `python3 verify.py` with Python 3 and no third-party packages. It recomputes every Narayana number as an exact integer independently of the factored congruence, and compares its reduction with the formula. It checks all \(r=2,\ldots,12\) and all \(s=2,\ldots,\min(r,8)\), a total of 56,780 entries, along with all predicted residue histograms. It independently checks the modulus-16 multiplicities and exceptional boundary residues for \(r=4,\ldots,12\). The executed program returned `VERIFY_OK`; this finite verification supplements, but does not replace, the algebraic proof for all allowed \(r,s\).

## Relationship to prior work
Bóna and Sagan studied divisibility of Narayana numbers by primes and proved, in particular, that Mersenne rows have entirely odd entries. Their criterion determines the parity layer; it does not give the full residue histogram modulo higher powers of two. The result above gives an explicit residue law for every precision \(s\ge2\) and sharp, location-specific counts modulo sixteen. General algorithms for computing binomial coefficients modulo prime powers can evaluate individual terms; an exact uniform classification of entire Mersenne Narayana rows and their multiplicities is an additional statement. The available 2013 binomial-modulus paper does not state this classification.

## Limitations
The uniform theorem concerns \(n=2^r-1\) and powers-of-two moduli \(2^s\) with \(r\ge s\ge2\) only. The modulus-16 closed counts require \(r\ge4\). The finite verification does not certify all unbounded cases; those follow from the proof. Literature searches do not exclude an equivalent earlier result in unindexed sources, and a potentially related 2006 combinatorial-congruence article was not available in full text.

## References
- M. Bóna and B. E. Sagan, *On divisibility of Narayana numbers by primes* (first arXiv version 2005-05-18), arXiv:math/0505382. https://arxiv.org/abs/math/0505382
- G. Andreica, *A Fast Algorithm for Computing Binomial Coefficients Modulo Powers of Two* (2013), https://doi.org/10.1155/2013/751358
- Eu, Liu, and Yeh, *On the Congruences of Some Combinatorial Numbers* (2006), https://doi.org/10.1111/j.1467-9590.2006.00337.x (full text not inspected).
