# Complete two-adic period phases and an index-two mode defect for coupled cat maps

## Finding

Let \(k,c\in\mathbb Z\), \(s\ge1\), and set
\[
C=\begin{pmatrix}k&c\\c&k\end{pmatrix},\qquad
M=\begin{pmatrix}I_2&C\\C&I_2+C^2\end{pmatrix}.
\]
The reduction of \(M\) acts as a permutation of \((\mathbb Z/2^s\mathbb Z)^4\). Its *global order* \(T_s(k,c)\) is the smallest positive \(t\) for which \(M^t\equiv I_4\pmod{2^s}\). Write \(\nu_2(0)=+\infty\), and set \(r=\min\{\nu_2(k),\nu_2(c)\}\). Then the **complete period law** is
\[
\boxed{T_s(k,c)=\begin{cases}
3\,2^{\max\{0,s-2\}},&k+c\text{ odd},\\
2^s,&k,c\text{ both odd},\\
2^{\max\{0,s-r\}},&k,c\text{ both even},
\end{cases}}
\]
where the third expression is interpreted as \(1\) when \(k=c=0\).

Let \(B_d=\begin{pmatrix}1&d\\d&1+d^2\end{pmatrix}\), and let \(t_s(d)\) be its global order modulo \(2^s\). The two rational normal-mode couplings are \(k+c\) and \(k-c\). Their orders do **not**, in general, determine the four-dimensional map order by taking the least common multiple. Instead,
\[
\boxed{\frac{T_s(k,c)}{\operatorname{lcm}(t_s(k+c),t_s(k-c))}
=\begin{cases}
2,&\nu_2(k)=\nu_2(c)<s,\\
1,&\text{otherwise}.
\end{cases}}
\]
Thus an exact factor-two obstruction occurs precisely when the two couplings have the same finite two-adic valuation below the modulus depth. In particular \(k=c=1\) gives full order \(2^s\), while the two scalar modes together have order only \(2^{\max\{0,s-1\}}\). This is a phase diagram for **all integer coupling weights**, not just the two unweighted complete-graph choices.

## Assumptions and scope

The two-site symmetric coupling and four-dimensional symplectic update are exactly as displayed. The matrix \(M\) is integral and invertible because it factors as
\[
M=\begin{pmatrix}I_2&0\\C&I_2\end{pmatrix}
\begin{pmatrix}I_2&C\\0&I_2\end{pmatrix}.
\]
A global permutation order means the least exponent simultaneously fixing every grid point, not the primitive period of every individual orbit. Negative and zero integer parameters are included as algebraic limits, without asserting that their continuous toral dynamics is hyperbolic. All divisibility assertions concern the entire matrix, entrywise, and are independent of initial conditions.

## Proof

**1. Two-adic lifting lemma.** For any integral square matrix \(B\), define \(v_2(B-I)\) as the smallest entry valuation, with \(v_2(0)=+\infty\). If \(B=I+2^e E\), \(e\ge2\), with at least one odd entry in \(E\), then
\[
B^2-I=2^{e+1}(E+2^{e-1}E^2).
\]
The bracket remains nonzero modulo two. By induction, \(v_2(B^{2^j}-I)=e+j\) for all \(j\ge0\). A matrix order modulo two can acquire only powers of two on lifting to powers-of-two moduli, since the successive reduction kernels are two-groups.

**2. Both parameters even.** Suppose \(r\ge1\) is finite and write \(C=2^rD\), with an odd entry in \(D\). Since
\[
M-I_4=\begin{pmatrix}0&C\\C&C^2\end{pmatrix},
\]
we have \(v_2(M-I_4)=r\). For \(r\ge2\), the lemma gives \(v_2(M^{2^j}-I_4)=r+j\), including \(j=0\). If \(r=1\), the upper-right block of \(M^2-I_4\) is \(2C+C^3\); after division by four it equals \(D+2D^3\), with an odd entry. The other blocks are multiples of four, so \(v_2(M^2-I_4)=2\); the lemma now applies. Modulo two the order is one, and the exact period is \(2^{\max\{0,s-r\}}\). If \(k=c=0\), then \(M=I_4\).

**3. Both parameters odd.** Modulo two, \(C\) is the all-ones matrix \(J=\begin{pmatrix}1&1\\1&1\end{pmatrix}\), satisfying \(J^2=0\) over \(\mathbb F_2\). Thus \(M\bmod2=\begin{pmatrix}I_2&J\\J&I_2\end{pmatrix}\) has exact order two. Also \(C^2/2\equiv J\pmod2\), since the diagonal and off-diagonal entries of \(C^2\) are congruent to two modulo four. Direct multiplication gives
\[
M^2-I_4=\begin{pmatrix}C^2&2C+C^3\\2C+C^3&3C^2+C^4\end{pmatrix}=2E,
\]
with \(E\bmod2=\begin{pmatrix}J&J\\J&J\end{pmatrix}\ne0\). Because \(E^2\equiv0\pmod2\), we obtain \(M^4-I_4=4(E+E^2)\) of exact valuation two. Lifting yields order \(2^s\) for every \(s\ge1\).

**4. Opposite parities.** Now \(C\bmod2\) is either \(I_2\) or the exchange matrix, so \(C^2\equiv I_2\pmod2\). The corresponding \(M\bmod2\) has exact order three. In fact \(C^2\equiv I_2\pmod4\), and
\[
M^3-I_4=\begin{pmatrix}
C^2(C^2+3I_2)&C(C^2+I_2)(C^2+3I_2)\\
C(C^2+I_2)(C^2+3I_2)&C^2(C^2+2I_2)(C^2+3I_2)
\end{pmatrix}.
\]
This is divisible entrywise by four. It is never divisible by eight. Indeed, if the even one of \(k,c\) is divisible by four, then \(C^2\equiv I_2\pmod8\), giving upper-left block \(4I_2\pmod8\). Otherwise the even parameter is two modulo four and \(C^2\equiv5I_2+4S\pmod8\), where \(S=\begin{pmatrix}0&1\\1&0\end{pmatrix}\); the upper-left block is \(4S\pmod8\). Hence \(v_2(M^3-I_4)=2\). The lifting lemma produces \(3\,2^{\max\{0,s-2\}}\) for every \(s\).

**5. The mode-index defect.** The scalar matrix \(B_d\) obeys, by the same block identities, the exact order law
\[
t_s(d)=\begin{cases}3\,2^{\max\{0,s-2\}},&d\text{ odd},\\2^{\max\{0,s-\nu_2(d)\}},&d\text{ even},\end{cases}
\]
with order one for \(d=0\). If \(k,c\) have opposite parity, both modes are odd, and their least common multiple equals the full order. If \(k,c\) are even with different valuations, both modes have valuation \(r\) and again give the full order. If \(\nu_2(k)=\nu_2(c)=r<\infty\), both modes have valuation at least \(r+1\), and one has valuation **exactly** \(r+1\), because the sum and difference of two odd integers have valuations with minimum one. Their least common multiple is \(2^{\max\{0,s-r-1\}}\), whereas the full order is \(2^{\max\{0,s-r\}}\); this gives exactly the stated factor two when \(r<s\). If both parameters vanish all orders are one. The rational mode change \(\begin{pmatrix}1&1\\1&-1\end{pmatrix}\) has determinant \(-2\), so it is *not* a change of basis over \(\mathbb Z/2^s\mathbb Z\), explaining why rational diagonalization cannot discard this factor.

## Verification

The standalone Python 3 program `verify.py` uses exact integer arithmetic. It checks the mod-eight seed congruences over all \(64\) classes of \((k,c)\bmod8\); this covers the polynomial congruence classes, unlike a mere sample of a continuous parameter range. It independently checks the predicted global order, all prime-divisor proper exponents, and the scalar-mode index ratio for \(625\) signed parameter pairs and eight modulus depths. It additionally checks the valuation lifting on six representative matrices. Execute `python verify.py` alongside this file. The expected terminal marker is `VERIFY_OK; exact assertions: 16962`.

The universal claim is established by the block identities and valuation-lifting proof, *not* by the finite regression calculations.

## Relationship to prior work

Axenides, Floratos and Nicolis introduced this coupled two-cat-map block family in equations (3.8)–(3.9) of their 2022 preprint and developed matrix-Fibonacci period methods, concentrating their finite-torus experiments on odd denominators; their equation (3.9) permits the equal-site choice treated here. Manolas and Floratos (2026) studied general symmetric circulant graph couplings, including numerical finite-torus periods, without the displayed full two-parameter two-adic classification. A separate published result, *Exact powers-of-two torus orders for all-to-all coupled cat maps* (2026), establishes global order formulas for unweighted complete-graph matrices in every number of sites. At two sites its cases \((k,c)=(0,1)\) and \((1,1)\) are **already covered** and are not new here. Neither result gives the all-integer \((k,c)\) phase diagram or the exact criterion for a factor-two failure of rational normal-mode period decomposition. Classical single-cat congruence periods motivate the comparison but do not themselves justify an integral decomposition at modulus two.

## Limitations

Only equal diagonal entries \(k\) and a symmetric two-site coupling \(c\) are classified. Unequal site parameters, other lattice sizes, odd prime powers, and individual orbit-length multiplicities are not addressed. This is an elementary finite-torus algebraic period theorem; it does not establish new hyperbolicity, mixing or quantum dynamics. Existing unindexed work could contain equivalent calculations; search results cannot prove historical priority. The accepted claims concern permutation orders and their mode-index discrepancy, not a decomposition of the full orbit spectrum.

## References

1. M. Axenides, E. Floratos, S. Nicolis, *Arnol'd cat map lattices*, arXiv:2208.03267, first released August 5, 2022; in particular equations (3.8)–(3.9), Section 6 and appendix A. https://arxiv.org/html/2208.03267v3
2. K. Manolas, E. Floratos, *Coupled Arnol'd cat maps on circulant graphs*, arXiv:2605.00965, first released May 1, 2026; Section 4.1 and Fibonacci-period formulas. https://arxiv.org/html/2605.00965v2
3. *Exact powers-of-two torus orders for all-to-all coupled cat maps*, published October 11, 2026; comparison of its complete-graph cases with the full weighted two-site family. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-powers-of-two-torus-orders-for-all-to-all-coupled-cat-maps--6ce73c0ff68d
4. F. J. Dyson, H. Falk, *Period of a discrete cat mapping*, American Mathematical Monthly 99 (1992), 603–614, DOI:10.1080/00029890.1992.11995900 (historical background).
