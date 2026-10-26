# Prime-step affine laws for low-degree ménage hit coefficients

## Finding
For every positive integer \(n\), consider the classical ménage hit polynomial
\[
H_n(t)=\sum_{k=0}^{n}\frac{2n}{2n-k}\binom{2n-k}{k}(n-k)!(t-1)^k,
\quad h_r(n)=[t^r]H_n(t).
\]
For any prime \(p\), any \(n\ge1\), and each \(0\le r<p\), **all** terms in the prime-step progression satisfy an exact affine residue law:
\[
\boxed{h_r(n+kp)\equiv(-1)^{n+kp-r}(A_{p,r}(n)+k B_{p,r}(n))\pmod p}\quad(k\ge0).
\]
Here \(A_{p,r}(n),B_{p,r}(n)\) are the following explicitly determined residues. Use \(\binom{a}{b}=0\) if \(b<0\) or \(b>a\), and for \(s\ge0\) set \((x)_{\underline{s}}=\prod_{i=0}^{s-1}(x-i)\), with the empty product one. For degree zero,
\[
A_{p,0}(n)=\sum_{j=0}^{p-1}(-1)^j j!\left[\binom{n+j}{2j}+\binom{n+j-1}{2j}\right]\pmod p,
\]
\[
B_{p,0}(n)=\sum_{j=\lceil p/2\rceil}^{p-1}(-1)^j j!\left[\binom{n+j}{2j-p}+\binom{n+j-1}{2j-p}\right]\pmod p.
\]
For \(1\le r<p\), where \(r!\) is invertible modulo \(p\),
\[
A_{p,r}(n)=\frac{2n}{r!}\sum_{j=0}^{p-1}(-1)^j j!\,(n-j-1)_{\underline{r-1}}\binom{n+j-1}{2j}\pmod p,
\]
\[
B_{p,r}(n)=\frac{2n}{r!}\sum_{j=\lceil p/2\rceil}^{p-1}(-1)^j j!\,(n-j-1)_{\underline{r-1}}\binom{n+j-1}{2j-p}\pmod p.
\]
A simultaneous consequence, interpreted coefficientwise in \(\mathbb F_p[t]\), is
\[
\boxed{H_n(t)+2H_{n+p}(t)+H_{n+2p}(t)\equiv0\pmod{(p,t^p)}}.
\]
Thus every coefficient of degree strictly below \(p\) obeys the same three-term congruence, not just one selected diagonal. The bound cannot uniformly be improved to degree \(p\): taking \(p=3\), \(n=1\), \(r=3\) gives
\[
h_3(1)=0,\quad h_3(4)=8,\quad h_3(7)=994,
\quad h_3(1)+2h_3(4)+h_3(7)=1010\equiv2\pmod3.
\]
For \(r=2\), this proves the prime-step congruence recorded as a conjecture for OEIS A000033 when \(p\ge3\). The omitted \(p=2,r=2\) case holds too by the separate parity argument below. An equivalent congruence is already recorded without the conjecture label for the normalized sequence in OEIS A000426; the contribution claimed here is the full uniform low-degree affine law and its sharp boundary.

## Assumptions and scope
All \(n,k,r\) are integers with \(n\ge1\), \(k\ge0\), \(0\le r<p\), and \(p\) prime. The coefficients \(h_r(n)\) are integers by the combinatorial interpretation as coefficients of the ménage hit polynomial. All fractions involving \(1/r!\) in the displayed formulas are interpreted in the field \(\mathbb F_p\) and are only used when \(r<p\). The asserted polynomial congruence means equality of coefficients of degrees \(0,\dots,p-1\), not equality as whole polynomials.

## Proof
**1. Exact factorial expansions.** Replacing \(k\) by \(n-j\) in the definition of \(H_n\), we have
\[
\frac{2n}{n+j}\binom{n+j}{2j}
=\binom{n+j}{2j}+\binom{n+j-1}{2j}.
\]
It follows immediately by evaluating at \(t=0\) that
\[
h_0(n)=(-1)^n\sum_{j=0}^{n}(-1)^j j!
\left[\binom{n+j}{2j}+\binom{n+j-1}{2j}\right].\tag{1}
\]
For \(r\ge1\), extracting \([t^r](t-1)^{n-j}=(-1)^{n-j-r}\binom{n-j}{r}\) and canceling factorials gives
\[
h_r(n)=(-1)^{n-r}\frac{2n}{r!}\sum_{j=0}^{n-r}(-1)^j j!
(n-j-1)_{\underline{r-1}}\binom{n+j-1}{2j}.\tag{2}
\]
If \(n<r\), the left side and the original right sum are zero. If \(n\ge r\), extending the right sum to all \(j\ge0\) introduces no nonzero terms because \(\binom{n+j-1}{2j}=0\) for \(j\ge n\) and \((n-j-1)_{\underline{r-1}}=0\) for \(n-r<j\le n-1\). The same extension is valid in (1). Formula (2) contains no problematic division modulo \(p\) for \(r<p\).

**2. Truncation and the sole surviving base-\(p\) carry.** Reducing (1) and (2) modulo \(p\), all terms with \(j\ge p\) vanish because \(p\mid j!\). For any nonnegative integer \(N\), \(k\ge0\), and \(0\le m\le2p-2\), the elementary polynomial identity
\[
(1+X)^{N+kp}\equiv(1+X)^N(1+X^p)^k\pmod p
\]
gives the exact two-term binomial congruence
\[
\binom{N+kp}{m}\equiv\binom Nm+k\binom N{m-p}\pmod p.\tag{3}
\]
Indeed, all terms with two or more copies of \(X^p\) have degree at least \(2p\). Throughout the truncated sums \(j<p\), the lower binomial index is \(m=2j\le2p-2\), so (3) applies. The multiplicative factors \(2n\) and \((n-j-1)_{\underline{r-1}}\) are unchanged modulo \(p\) when \(n\) is replaced by \(n+kp\). Substituting (3) into (1) and (2) yields exactly the displayed finite formulas for \(A_{p,r}(n)\) and \(B_{p,r}(n)\), including cases where the original \(h_r(n)\) vanishes.

**3. Three-term congruence.** When \(p\) is odd, the affine law yields
\[
h_r(n+kp)\equiv(-1)^{n-r}(-1)^k(A_{p,r}(n)+kB_{p,r}(n))\pmod p.
\]
For the values \(k=0,1,2\), the weighted sum with weights \(1,2,1\) is
\[
A-2(A+B)+(A+2B)=0.
\]
For \(p=2\), the middle coefficient vanishes and the affine law implies \(h_r(n+2p)\equiv h_r(n)\pmod2\). Thus the same congruence holds at every \(0\le r<p\), including \(p=2\). Coefficientwise this is the asserted truncated-polynomial congruence.

**4. The exceptional \(p=2,r=2\) diagonal.** Formula (2) at \(r=2\) simplifies *over the integers* to
\[
h_2(n)=(-1)^{n-2}n\sum_{j=0}^{n-2}(-1)^j j!(n-j-1)\binom{n+j-1}{2j}.\tag{4}
\]
Modulo \(2\), only \(j=0,1\) survive. The remaining factors depend only on \(n\bmod4\) since their binomial lower indices are \(0,2\); directly, \(\binom{N+4}{m}\equiv\binom Nm\pmod2\) for \(m=0,2\). Consequently \(h_2(n+4)\equiv h_2(n)\pmod2\), which is the claimed \(p=2\) case. For \(n<2\) the zero terms are handled by the same extended-sum convention.

**5. Sharp boundary.** The three displayed exact coefficients \(h_3(1),h_3(4),h_3(7)\) follow from the defining polynomial (and are independently reproduced in the verifier); their nonzero weighted residue shows the cutoff is sharp. \(\square\)

## Verification
The enclosed standalone Python 3 verifier recomputes coefficients using the original polynomial rather than the proof's factorial expansion. For \(p\in\{2,3,5,7,11,13,17\}\), all \(0\le r<p\), all \(1\le n\le24\) and \(0\le k\le4\), it compares the exact coefficient with the stated explicit affine residue formula. This comprises 6,960 checks, plus checks of the whole three-term congruence and the boundary counterexample. It separately compares the first 12 terms of the familiar degree-two diagonal against the published integer sequence and checks its special parity case. Run `python3 verify.py`; expected output is `VERIFY_OK`. Finite tests are only checks, not a substitute for the proof.

## Relationship to prior work
The classical ménage rook/Touchard formula is historically documented by Kaplansky and Riordan and appears verbatim as the hit polynomial in OEIS A058087. OEIS A000033 explicitly labels its degree-two prime-step three-term congruence as a 2019 conjecture. Crucially, OEIS A000426 **already records** a closely related congruence for the divided coefficient \(h_2(n)/n\) without a conjecture label; because \(n+kp\equiv n\pmod p\), that statement entails the degree-two congruence in A000033. Neither entry records the affine progression law for every \(0\le r<p\) or its sharp cutoff at degree \(p\). OEIS A000179 records a different prime-step congruence for the zero-hit ménage numbers, with step \(2p\) and an ordinary rather than alternating second difference. Alekseyev's 2015 full-text paper develops graph-theoretic enumeration and generating functions for the ménage problem and its ternary generalization; its theorems do not assert these uniform coefficientwise congruences.

## Limitations
This is a congruence modulo the prime \(p\), not modulo higher prime powers. The cutoff \(r<p\) is necessary for the *uniform* assertion; isolated larger degrees can still satisfy special identities. The classification applies to this classical family, not arbitrary rook polynomials. As with any priority comparison, unlocated general results on factorial-weighted binomial sums might imply the theorem. The early Kaplansky--Riordan original scan was not available for complete inspection; the accessible secondary formula and full 2015 paper were examined. Independent review and external certification have not been performed.

## References
1. I. Kaplansky and J. Riordan, *The problème des ménages*, Scripta Mathematica 12 (1946), 113–124; formula recorded in OEIS A058087, https://oeis.org/A058087.
2. OEIS A000033, ménage-hit coefficient of degree two and Mark van Hoeij's June 10, 2019 conjecture, https://oeis.org/A000033.
3. OEIS A000426, normalized ménage coefficient and Mark van Hoeij's June 13, 2019 prime-step identity, https://oeis.org/A000426.
4. OEIS A000179, ménage numbers and other prime-step congruences, https://oeis.org/A000179.
5. M. A. Alekseyev, *Weighted de Bruijn Graphs for the Menage Problem and Its Generalizations*, arXiv:1510.07926 (2015), https://arxiv.org/abs/1510.07926.
