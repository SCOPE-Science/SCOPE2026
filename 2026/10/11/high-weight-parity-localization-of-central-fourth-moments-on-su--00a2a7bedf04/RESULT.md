# High-weight parity localization of central fourth moments on \(SU(2)\)

## Finding
Let \(S\subset\mathbb Z_{\ge0}\) be any nonempty finite offset set with \(\min S=0\), \(L=\max S\), and let \(e=|S\cap2\mathbb Z|\), \(o=|S\cap(2\mathbb Z+1)|\). For each integer \(m\ge L\), let \(\chi_j\) be the unnormalized irreducible character of \(SU(2)\) with highest weight \(j\) (thus \(\|\chi_j\|_2=1\)), and define
\[
K_m(S)=\max_{\sum_{s\in S}|c_s|^2=1}\biggl\|\sum_{s\in S}c_s\chi_{m+s}\biggr\|_{L^4(SU(2))}^4.
\]
Then \(K_m(S)=mC(e,o)+O_S(1)\), with the **explicit sharp limit**
\[
C(e,o)=\begin{cases}
e^2,&e\ge3o,\\
o^2,&o\ge3e,\\
\displaystyle\frac{8e^2o^2}{6eo-e^2-o^2},&e<3o\ \text{and}\ o<3e.
\end{cases}
\]
The boundary cases \(e=3o\) and \(o=3e\) belong to the single-parity branches. Quantitatively, for \(n=|S|\),
\[
\bigl|K_m(S)-mC(e,o)\bigr|\le(L+1)n^2\quad(m\ge L).
\]
The exact limiting maximizing coefficient profiles depend only on the two parity counts. If \(e\ge3o\), all odd coefficients vanish and the even coefficients are equal, with modulus \(1/\sqrt e\). The analogous statement holds for \(o\ge3e\). In the strict mixed range, put
\[
\Delta=6eo-e^2-o^2,\qquad x_*={o(3e-o)\over\Delta},\qquad y_*={e(3o-e)\over\Delta}.
\]
Then each even coefficient equals \(e^{i\alpha}\sqrt{x_*/e}\) and each odd coefficient equals \(\varepsilon e^{i\alpha}\sqrt{y_*/o}\), where \(\alpha\in\mathbb R\), \(\varepsilon\in\{-1,1\}\). Every sequence of unit-energy maximizers of \(K_m(S)\) approaches this stated compact set of profiles in Euclidean distance as \(m\to\infty\). The limit is independent of the spacings inside either parity class.

## Assumptions and scope
Haar measure on \(SU(2)\) has total mass one, the characters are the ordinary traces (not divided by their dimensions), and the norm \(\|\cdot\|_2\) is Haar-normalized. Only central (character) polynomials are optimized: no statement concerns the complete matrix-coefficient spectral spaces. Offsets \(S\) are fixed as \(m\to\infty\); this is not a uniform theorem when their diameter grows with \(m\). Coefficients may be arbitrary complex numbers, subject to the unit \(\ell^2\) constraint.

## Proof
**1. Exact fourth-moment expansion.** The Clebsch–Gordan character identity is
\[
\chi_a\chi_b=\chi_{|a-b|}+\chi_{|a-b|+2}+\cdots+\chi_{a+b},
\]
with each summand occurring once. Schur orthogonality makes the characters orthonormal in Haar \(L^2\). Hence the inner product of two products \(\chi_{m+s}\chi_{m+t}\) and \(\chi_{m+u}\chi_{m+v}\) is zero unless \(s+t\equiv u+v\pmod2\). When their parities agree and \(m\ge L\), it is exactly
\[
m+1+\frac{\min(s+t,u+v)-\max(|s-t|,|u-v|)}2.
\]
Indeed, the two multiplicity-one lists of irreducibles intersect from the larger lower endpoint to the smaller upper endpoint in steps of two; the lower endpoint is at most \(L\), and the upper endpoint is at least \(2m\ge2L\). This verifies all endpoints and integrality.

Define \(U=\sum_{s\text{ even}}c_s\) and \(V=\sum_{s\text{ odd}}c_s\). Collecting the coefficient of \(m\) in the preceding exact identity yields
\[
\Bigl\|\sum_{s\in S}c_s\chi_{m+s}\Bigr\|_4^4
=mF(c)+B_S(c),\qquad
F(c)=|U^2+V^2|^2+4|UV|^2,
\]
where the **explicit finite correction** is
\[
B_S(c)=\!\sum_{\substack{s,t,u,v\in S\\s+t\equiv u+v\ ({\rm mod}\ 2)}}
 c_sc_t\overline{c_u c_v}
\biggl(1+{\min(s+t,u+v)-\max(|s-t|,|u-v|)\over2}\biggr).
\]
The real-valuedness of the correction follows by swapping \((s,t)\) with \((u,v)\). Every correction factor has absolute value at most \(L+1\). On \(\sum|c_s|^2=1\), Cauchy–Schwarz gives \(\sum|c_s|\le\sqrt n\), hence \(|B_S(c)|\le(L+1)n^2\) uniformly. Thus \(m^{-1}\) times the exact fourth-moment functional converges uniformly on the unit sphere to \(F\).

**2. Leading optimization.** Set \(x=\sum_{s\text{ even}}|c_s|^2\), so that the odd class has energy \(1-x\). Cauchy–Schwarz gives \(|U|^2\le e x\) and \(|V|^2\le o(1-x)\), with equality exactly when coefficients are constant inside each nonempty parity class. Moreover,
\[
F(c)\le |U|^4+6|U|^2|V|^2+|V|^4
\le e^2x^2+6eo x(1-x)+o^2(1-x)^2=:Q(x).
\]
Both inequalities can be made equal simultaneously by choosing all coefficients within a parity class equal and choosing the two class phases to differ by \(0\) or \(\pi\). If \(e=0\) or \(o=0\) the same conclusion reduces to a single group.

The derivative of \(Q\) is
\[
Q'(x)=2(e^2-6eo+o^2)x+6eo-2o^2.
\]
For \(e\ge3o\), its maximum on \([0,1]\) is uniquely at \(x=1\); for \(o\ge3e\), uniquely at \(x=0\). In the remaining strict range, \(\Delta=6eo-e^2-o^2>0\), the unique maximizer is \(x_*=o(3e-o)/\Delta\), and substitution gives \(Q(x_*)=8e^2o^2/\Delta\). Equality in both prior inequalities gives exactly the stated profiles, including the relative sign restriction; the boundary ratios have no extra mixed profiles.

**3. Sharp asymptotic and maximizer localization.** By uniform boundedness of \(B_S\), taking suprema yields \(|K_m-m\max F|\le(L+1)n^2\). Existence of finite-\(m\) maximizers follows from compactness. If a maximizing sequence stayed a positive Euclidean distance from the compact set \(\operatorname{argmax}F\), a convergent subsequence would limit to a nonmaximizer of \(F\), contradicting \(F(c_m)\ge C(e,o)-2(L+1)n^2/m\). This proves all conclusions without relying on finite experiments.

## Verification
Run `python3 verify.py` in this directory. Its direct multiplicity-one tensor-product computation is compared with the four-index correction formula for 216 integer-Gaussian coefficient cases, across eight offset families and three high weights each. Rational arithmetic independently checks the stationary point and all branches of \(C(e,o)\). These finite checks test normalization, endpoint parity and coefficient conjugations; they are not the proof for arbitrary \(m\) or arbitrary finite \(S\).

## Relationship to prior work
Clebsch–Gordan decomposition and Schur orthogonality are classical inputs, not new. Travaglini establishes weighted maximal-torus norm descriptions and an \(A_p\) criterion for central Fourier polynomials on compact Lie groups; that theorem does not determine a sharp fixed-packet fourth-moment asymptotic or equality profiles. Dooley–Gupta study a different extremal problem: \(L^4\) norms of noncentral matrix coefficients from a single irreducible block, motivated by an \(L^p\)-multiplier conjecture, rather than a moving short span of central irreducible characters. The parity-count universality and its \(3:1\) concentration transition are the statements considered here.

## Limitations
The asserted sharpness concerns the leading coefficient of \(m\), not an explicit finite-\(m\) maximizer or the constant-order correction to \(K_m\). It is not uniform in the offset diameter, gives no unrestricted noncentral bound, and claims no resolution of historical multiplier conjectures. Independent mathematical review and a comprehensive priority determination remain outstanding; older compact-group and orthogonal-polynomial literature may contain equivalent asymptotics.

## References
- G. Travaglini, *Weyl functions and the \(A_p\) condition on compact Lie groups*, Journal of the Australian Mathematical Society (Series A) 33 (1982), 185–192, DOI: 10.1017/S1446788700018322. The publisher documents an online release on 2009-04-09; the 1982 print date predates that online release.
- A. H. Dooley and S. K. Gupta, *On norms of trigonometric polynomials on \(SU(2)\)*, Pacific Journal of Mathematics 175 (1996), 491–509; https://msp.org/pjm/1996/175-2/pjm-v175-n2-p09-p.pdf.
- A. H. Dooley, *Central lacunary sets for Lie groups*, Journal of the Australian Mathematical Society 45 (1988), 30–45, DOI: 10.1017/S1446788700032249 (background on central lacunarity).
