# Sharp base-five prefix discrepancy envelopes for central trinomial residues

## Finding

Let \(T_n=[x^n](1+x+x^2)^n\) be the central trinomial coefficient, and for \(r\in\{1,2,3,4\}\) set
\[
C_r(N)=\#\{0\le n<N:T_n\equiv r\pmod5\},\qquad E_r(N)=4C_r(N)-N.
\]
For every integer \(L\ge2\), the **exact extrema**, taken over all integer \(0\le N<5^L\), are
\[
\max E_r(N)=3L+\alpha_r,\qquad
\min E_r(N)=-\left\lfloor\frac{5L+\beta_r}{2}\right\rfloor,
\]
where the ordered tuples indexed by \(r=1,2,3,4\) are
\[
(\alpha_1,\alpha_2,\alpha_3,\alpha_4)=(3,-3,-2,-4),\qquad
(\beta_1,\beta_2,\beta_3,\beta_4)=(-10,2,-3,3).
\]
Both extrema are attained. For every integer \(L\ge0\), the complete-block counts are
\[
C_1(5^L)=\frac{5^L+3}{4},\qquad
C_2(5^L)=C_3(5^L)=C_4(5^L)=\frac{5^L-1}{4}.
\]
In particular, each nonzero residue has natural density \(1/4\), and every one of the four prefix discrepancies has genuinely logarithmic positive and negative excursions, with asymmetric optimal leading slopes \(3\) and \(-5/2\) per base-five digit.

## Assumptions and scope

All coefficients and counts are over nonnegative integers; \(N\) is an integer prefix endpoint, so \([0,N)\) contains \(N\) indices. The prime modulus is exactly five. Leading zeros are permitted when representing a number by a fixed number of base-five digits. All minima and maxima explicitly range over \(0\le N<5^L\), not over \(N\le5^L\).

## Proof

**1. Digit congruence and five-block recurrence.** The Lucas-type congruence for central trinomials, proved in Deutsch–Sagan [1, Theorem 4.7], states that if the base-five digits of \(n\) are \(n_j\), then
\[
t(n):=T_n\pmod5=\prod_j w_{n_j}\pmod5,\qquad (w_0,w_1,w_2,w_3,w_4)=(1,1,3,2,4).
\]
These five digits contain each unit modulo five exactly once, with unit one repeated. Thus every block \(5q,\ldots,5q+4\) contains each target residue \(r\in\{1,2,3,4\}\) exactly once, plus an extra copy of \(t(q)\). Consequently,
\[
C_r(5q)=q+C_r(q),\quad E_r(5q)=E_r(q),
\]
and for \(0\le d\le4\),
\[
E_r(5q+d)=E_r(q)+\Delta_r(t(q),d),\quad
\Delta_r(x,d)=4\sum_{j=0}^{d-1}{\bf1}_{xw_j\equiv r\ (5)}-d.
\tag{1}
\]
This identity also holds for \(d=0\), interpreting an empty sum as zero. The exact complete-block counts follow immediately by induction on \(L\), since \(C_r(1)={\bf1}_{r=1}\).

**2. An exact four-state extremal recurrence.** For each residue \(r\) and \(L\ge0\), define \(m_{r,L}(y)\) and \(M_{r,L}(y)\), respectively, as the minimum and maximum of \(E_r(N)\) over all \(0\le N<5^L\) satisfying \(t(N)=y\). Initially, the only reachable state is \(y=1\) with value zero; the other states have values \(+\infty\) for minima and \(-\infty\) for maxima. Formula (1) gives, for each \(y\in\{1,2,3,4\}\), the exact Bellman recurrences
\[
\begin{split}
m_{r,L+1}(y)&=\min_{\substack{x\in\{1,2,3,4\},\ 0\le d\le4\\xw_d\equiv y\ (5)}}\big(m_{r,L}(x)+\Delta_r(x,d)\big),\\
M_{r,L+1}(y)&=\max_{\substack{x\in\{1,2,3,4\},\ 0\le d\le4\\xw_d\equiv y\ (5)}}\big(M_{r,L}(x)+\Delta_r(x,d)\big).
\end{split}
\tag{2}
\]
These are finite minima/maxima of explicitly given integers. Because one may prepend leading zero digits and \(w_0=1\), they cover every possible prefix exactly.

**3. Finite certificates for all infinite levels.** The following vectors list states \(y=1,2,3,4\) in that order. Direct evaluation of (2) from the initial state gives:

| \(r\) | \(M_{r,2}\) | \(m_{r,2}\) | \(m_{r,3}\) | \(m_{r,4}\) |
|---|---|---|---|---|
| 1 | \((6,8,9,7)\) | \((0,2,1,3)\) | \((-2,1,0,-1)\) | \((-5,-3,-4,-2)\) |
| 2 | \((3,0,1,2)\) | \((-5,-6,-3,-4)\) | \((-6,-8,-7,-5)\) | \((-10,-11,-8,-9)\) |
| 3 | \((3,2,1,4)\) | \((-2,-2,-3,-2)\) | \((-4,-4,-6,-5)\) | \((-6,-7,-8,-7)\) |
| 4 | \((0,2,1,-1)\) | \((-5,-4,-3,-6)\) | \((-6,-8,-7,-9)\) | \((-10,-9,-8,-11)\) |

Let \(\mathcal T_r^{\max}\) and \(\mathcal T_r^{\min}\) denote the operators on vectors in (2), and let \({\bf1}=(1,1,1,1)\). Every entry of the table and each of the following **twelve finite vector identities** is obtained by at most 20 integer comparisons per target state, using weights \((1,1,3,2,4)\):
\[
\begin{split}
\mathcal T_r^{\max}(M_{r,2})&=M_{r,2}+3{\bf1},\\
\mathcal T_r^{\min}(m_{r,3})&=m_{r,4},\\
\mathcal T_r^{\min}(m_{r,4})&=m_{r,3}-5{\bf1},\qquad r=1,2,3,4.
\end{split}
\tag{3}
\]
The exact standalone verifier reproduces all table entries and all identities directly from (1) and (2). Both operators commute with addition of a constant vector. Iterating (3) therefore yields
\[
M_{r,L}=M_{r,2}+3(L-2){\bf1}\quad(L\ge2),\qquad
m_{r,L+2}=m_{r,L}-5{\bf1}\quad(L\ge3).
\tag{4}
\]
The initial vectors \(m_{r,2}\), \(m_{r,3}\), and \(m_{r,4}\) then give the claimed closed extrema on taking maxima/minima over states, separately for even and odd \(L\). As every finite-state extremum in (2) is attained by at least one digit word, both bounds are exact, not just inequalities.

In fact the maxima have explicit witnesses: for \(L\ge2\), take the base-five integer whose digits are \(1^{L-1}2\) for \(r=1\), \(31^{L-2}2\) for \(r=2\), \(21^{L-2}2\) for \(r=3\), or \(41^{L-2}2\) for \(r=4\). These are ordinary strings of base-five digits and all have length \(L\). Substituting them in (1) gives the corresponding value \(3L+\alpha_r\); the minimum witnesses are likewise obtained by finite-state backtracking in (2).

**4. Density and sharp growth.** Let \(N>1\) and take \(L=\lceil\log_5(N+1)\rceil\), so \(N<5^L\). The extrema imply \(|E_r(N)|=O(\log(N+1))\), whence \(C_r(N)/N\to1/4\). Conversely, the explicit maximizing digit words (and the attained minima) show discrepancies growing linearly in \(L\) at arguments of size at most \(5^L\), proving that \(O(\log N)\) cannot be improved to \(o(\log N)\) for any residue.

## Verification

Run the dependency-free Python 3 program `verify.py`. It independently computes 700 central trinomial coefficients by the integer recurrence \((n+1)T_{n+1}=(2n+1)T_n+3nT_{n-1}\) and 80 by the binomial sum, compares their residues with digit products, reproduces every Bellman table/certificate in (3), exhaustively checks all 15,625 digit-defined residues and their four prefix discrepancies through length six, and tests the explicit upper-extremum witnesses through length twelve. Successful execution prints `VERIFY_OK`. The program checks finite arithmetic used in the infinite proof; it does not independently verify literary novelty or establish the infinite claim by sampling.

## Relationship to prior work

Deutsch and Sagan [1] proved the base-prime digit-product congruence used as the starting point, not the sharp frequency-excursion profile. Rampersad and Shallit [2, Theorem 8] developed a different automatic-sequence analysis of central trinomials modulo five, proving nonvanishing and uniform recurrence, rather than the exact four-residue prefix extrema above. OEIS A002426 [3] lists the underlying integers, and known automatic-sequence techniques can imply less explicit logarithmic discrepancy bounds. The specifically claimed contribution is the complete, residue-dependent **exact finite-scale maximum/minimum classification** and attainable asymmetric slopes; nothing here claims a new Lucas property, nonvanishing fact, or general automata theorem.

## Limitations

The formulas concern the single prime modulus five, four nonzero residues, integer prefix endpoints strictly smaller than a power of five, and fixed starting index zero. Analogous claims for other primes, prime powers, shifts, or general digit-product sequences are not proved. A stronger general theorem or an unlocated specialized formula could implicitly cover the exact extrema; published-priority claims remain subject to independent literature review. This proof has not undergone independent mathematical audit.

## References

[1] E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326, first submitted 2004-07-19, Theorem 4.7. https://arxiv.org/abs/math/0407326 ; author-hosted article https://users.math.msu.edu/users/sagan/papers/old/ccm.pdf .

[2] N. Rampersad and J. Shallit, *Congruence Properties of Combinatorial Sequences via Walnut and the Rowland–Yassawi–Zeilberger Automaton*, Electronic Journal of Combinatorics **29** (2022), #P3.36, Theorem 8, DOI:10.37236/10799. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i3p36/pdf/ .

[3] OEIS A002426, central trinomial coefficients. https://oeis.org/A002426 .
