# Exact five-point finite-parabola uncertainty over the field of seven elements

## Finding
Let \(\mathbb F_7\) be the field of seven elements and \(\zeta=e^{2\pi i/7}\). For every five-element set \(R\subset\mathbb F_7\) and every collection of nonzero complex coefficients \(c_x\) indexed by \(R\), define
\[
F_{R,c}(a,b)=\sum_{x\in R}c_x\zeta^{ax^2+bx},\qquad(a,b)\in\mathbb F_7^2.
\]
There are **at most five** zeros of \(F_{R,c}\). Five zeros are attainable. For each fixed \(R\), precisely **3234 complex projective full-support coefficient vectors** attain the maximum. Under the action \(c_x\mapsto c_x\zeta^{ux^2+vx}\), these extremizers split into **66 free orbits of size 49**.

## Assumptions and scope
The coefficients are arbitrary nonzero complex numbers, and projective equivalence identifies vectors that differ by one common nonzero scalar. Only the prime \(7\) and exactly five nonzero coordinates are covered. The result is an exact zero-set statement for the Fourier transform of a function supported at five points of the finite parabola \(\{(x^2,x):x\in\mathbb F_7\}\).

## Proof
**Reduction to one support and one zero.** Every two-point complement of a five-element \(R\) can be carried to \(\{0,1\}\) by an invertible affine map on \(\mathbb F_7\). Substituting \(x\mapsto ux+v\) transforms the pair of frequency coordinates invertibly, up to an everywhere nonzero scalar, so zero counts and projective-extremizer counts are unchanged. Hence fix \(R=\{2,3,4,5,6\}\). If \((a_0,b_0)\) is a zero, multiplication of each \(c_x\) by \(\zeta^{a_0x^2+b_0x}\) shifts that zero to \((0,0)\). It suffices to examine five-row constraint matrices containing that origin.

**Exact rank criterion.** Put \(K=\mathbb Q(\zeta)\). For each set \(E\) of five distinct frequencies including the origin, form the \(5\times5\) matrix
\[
M_E=\bigl(\zeta^{ax^2+bx}\bigr)_{(a,b)\in E,\,x\in R}.
\]
If its rank is five, no nonzero coefficients satisfy those five equations. At rank four the kernel is a projective point; such coefficients have full support exactly when all five four-row cofactors are nonzero, and every further zero may be decided exactly in \(K\). At rank three, a column whose removal reduces the rank forces that coefficient to vanish in every kernel vector; no rank-two-or-smaller case occurs in the enumeration.

**Exhaustive certificate.** There are precisely \(\binom{48}{4}=194580\) choices of \(E\). The accompanying program `verify_parabola_7.py` enumerates every such choice using only integer arithmetic in the cyclotomic ring \(\mathbb Z[\zeta]\). Represent \(\sum_{j=0}^{6}d_j\zeta^j\) by the integer vector \((d_0,\ldots,d_6)\); it vanishes exactly when all seven entries are equal, by the irreducible minimal polynomial \(1+X+\cdots+X^6\). Determinants are evaluated as signed sums of permutation monomials. The inexpensive test \(\zeta\mapsto16\) modulo \(29\) eliminates matrices with nonzero determinant before exact work, because \(16\) has order seven in \(\mathbb F_{29}\); a nonzero modular image entails a nonzero cyclotomic determinant.

The exact exhaustive counts are as follows: \(185895\) matrices have nonzero determinant modulo \(29\); of the remaining \(8685\), exactly \(3225\) have nonzero cyclotomic determinant. Among the \(5460\) singular matrices, \(5415\) have rank four, and \(5085\) of those force at least one coefficient to vanish. The other **330** rank-four matrices have full-support kernels, and in every case the exact check of all \(49\) frequencies finds **precisely five zeros**, namely the selected ones. The remaining \(45\) matrices have rank three with an essential column, so also force a zero coefficient. Therefore a six-zero full-support vector is impossible: choosing five of its zeros and shifting one to the origin would contradict this exhaustive list.

**Attainment and projective census.** One rank-four certificate is given by the five zeros
\[
(0,0),\quad(0,1),\quad(0,3),\quad(1,0),\quad(3,2).
\]
With the support coordinates \(x=2,3,4,5,6\), respectively, one explicit coefficient vector is
\[
\begin{aligned}
c_2&=-2+2\zeta-\zeta^2+3\zeta^3-3\zeta^5+\zeta^6,\\
c_3&=-3+3\zeta^2-\zeta^3+2\zeta^4-2\zeta^5+\zeta^6,\\
c_4&=1-4\zeta-2\zeta^2+2\zeta^4+4\zeta^5-\zeta^6,\\
c_5&=1-\zeta^2-2\zeta^3-3\zeta^4+3\zeta^5+2\zeta^6,\\
c_6&=3+2\zeta+\zeta^2-\zeta^4-2\zeta^5-3\zeta^6.
\end{aligned}
\]
All five coefficients are nonzero, and direct exact evaluation gives precisely the displayed zero set. Each of the 330 origin-containing full-support five-zero sets determines one projective coefficient vector, and every maximal vector has five zeros. Double-counting pairs consisting of such a vector and one of its zeros yields \(49\cdot330=5\cdot3234\). Multiplication by all \(49\) quadratic-linear characters acts freely, because a polynomial of degree at most two constant on five distinct field elements must be constant identically; hence \(3234/49=66\) free character orbits.

## Verification
Run `python3 verify_parabola_7.py` using Python 3 (only the standard library is required). It prints `EXACT_CERTIFICATE_PASS`, the full rank-count breakdown, one witness and its precisely five zeros. Exhaustiveness is finite and explicit: each of the \(194580\) five-row choices is visited, and every required singular-kernel and further-root check is exact. Modular computation discards only matrices conclusively nonsingular over the cyclotomic field. The analytic reductions preceding the calculation justify why this finite certificate covers every complex coefficient vector and every five-element support.

## Relationship to prior work
Dongwei Li's September 11, 2026 initial preprint, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola* (arXiv:2609.16030v1), announced the general odd-support estimate \(|Z|\le\min\{p+2r-2,r(r+1)\}\) for support size \(2r+1\); here it gives \(6\), not the sharp count \(5\). The October 3, 2026 revised manuscript, *Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases* (arXiv:2609.16030v2), proves a broader but numerically weaker bound at this support and focuses its equality classification on **global total-support minimizers**. Their distinction from the present fixed-five-point optimization is substantive: the five-point examples here have total support \(5+49-5=49\), whereas the global minimum is \(44\). Fiorentino and Weigert (2022) study complete-basis total-support bounds in dimension seven; their Section 5.3 does not enumerate the fixed-five-support maximal parabolic zero sets or the projective coefficient vectors. These comparisons establish a meaningful gap in the inspected claims but cannot rule out unindexed equivalent results.

## Limitations
This is one exact natural finite-field case, not an asymptotic statement or a general theorem for all odd support sizes or larger primes. The enumeration characterizes extremizers by their exact kernel and root tests rather than an elegant closed-form parametrization of all 66 orbits. The initial version of the motivating article could not be inspected in full; a more detailed equivalent special case in that version is an outstanding originality risk. Independent verification has not been performed.

## References
1. Dongwei Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030v1, first posted 2026-09-11, https://arxiv.org/abs/2609.16030v1.
2. Dongwei Li, *Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases*, arXiv:2609.16030v2, posted 2026-10-03, https://arxiv.org/html/2609.16030v2.
3. Vincenzo Fiorentino and Stefan Weigert, *Uncertainty relations for the support of quantum states*, Journal of Physics A 55 (2022), 495305, https://doi.org/10.1088/1751-8121/aca9a4.
