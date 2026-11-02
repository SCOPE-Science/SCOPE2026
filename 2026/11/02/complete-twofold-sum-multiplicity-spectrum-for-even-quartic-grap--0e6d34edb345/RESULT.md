# Complete twofold-sum multiplicity spectrum for even-quartic graphs over finite fields

## Finding
For every finite field \(F=\mathbb F_q\) and every \(a\in F\), let
\[
C_a=\{(x,x^4+ax^2):x\in F\},\qquad
r_a(s,v)=\#\{(x,y)\in F^2:x+y=s,\ x^4+y^4+a(x^2+y^2)=v\}.
\]
Pairs \((x,y)\) are ordered. Write \(A_j(a)=\#\{(s,v)\in F^2:r_a(s,v)=j\}\) for the complete target multiplicity spectrum, including \(j=0\).

**Characteristic two.** The graph is an additive subgroup of \(F^2\), so
\[
\boxed{A_0=q^2-q,\qquad A_q=q,\qquad A_j=0\ (j\notin\{0,q\}).}
\]

**Odd characteristic.** Let \(\chi\) be the quadratic character of \(F\), extended by \(\chi(0)=0\). Define
\[
\epsilon=\chi(-1),\quad \tau=\chi(2),\quad d=\gcd(4,q-1),\quad B_s=6s^2+4a,
\]
\[
Z=\#\{s\in F:B_s=0\},\quad T=\sum_{s:B_s\ne0}\chi(-B_s),\quad n_\pm=(q-Z\pm T)/2.
\]
For \(j\in\{0,1,2,3,4\}\), let \(D_j\) be zero except
\[
D_0=q-1-\frac{q-1}{d},\quad D_1=1,\quad D_d=\frac{q-1}{d}.
\]
For \(\lambda\in\{-1,1\}\), let
\[
\begin{aligned}
H_0(\lambda)&=\frac{5q-4-\epsilon+2\lambda(1-\tau)}8,&
H_1(\lambda)&=\frac{1-\lambda}2,\\
H_2(\lambda)&=\frac{q+\epsilon+2\tau\lambda}4,&
H_3(\lambda)&=\frac{1+\lambda}2,\\
H_4(\lambda)&=\frac{q-4-\epsilon-2\lambda(1+\tau)}8.
\end{aligned}
\]
Every displayed quantity is a nonnegative integer, and the **entire spectrum** is
\[
\boxed{A_j(a)=Z D_j+n_+H_j(1)+n_-H_j(-1)\quad(0\le j\le4),\qquad A_j(a)=0\quad(j>4).}
\]
The input parameters are explicit. When \(\operatorname{char}F\ge5\),
\[
(Z,T)=
\begin{cases}
(1,(q-1)\chi(-6)),&a=0,\\
(1+\chi(-2a/3),-\chi(-6)),&a\ne0.
\end{cases}
\]
When \(\operatorname{char}F=3\),
\[
(Z,T)=\begin{cases}(q,0),&a=0,\\(0,q\chi(-a)),&a\ne0.\end{cases}
\]
In particular, for odd \(q\), the exact twofold-sumset size is
\[
\boxed{|C_a+C_a|=\frac{(q-Z)(3q+4+\epsilon)}8+\frac{T(\tau-1)}4+Z\left(1+\frac{q-1}{d}\right).}
\]
For \(\operatorname{char}F\ge5\) and \(a\ne0\), precisely two possible coefficient square classes occur. If \(S_2\) denotes the sumset size when \(\chi(-2a/3)=1\) and \(S_0\) when \(\chi(-2a/3)=-1\), then
\[
\boxed{S_2-S_0=\begin{cases}-(q-1)/4,&q\equiv1\pmod4,\\(q+1)/4,&q\equiv3\pmod4.\end{cases}}
\]
Thus the larger sumset *switches coefficient class* with the congruence class of \(q\) modulo four.

The additive energy is also exact:
\[
\boxed{E(C_a)=\sum_{s,v}r_a(s,v)^2=(q-Z)(3q-3-\epsilon)-2\tau T+Z\bigl(1+d(q-1)\bigr)}
\]
in odd characteristic; in characteristic two it equals \(q^3\).

## Assumptions and scope
Every prime power \(q\ge2\) is included. The coefficient \(a\) may vanish. Division by \(2\) and by \(3\) is used only in branches where those elements are invertible. The multiplicities count ordered pairs in \(F^2\), while \(A_j\) counts *targets* \((s,v)\in F^2\), including unattained targets. For odd \(q\), the supports \(D_j\) can overlap the indices \(2\) or \(4\) of the \(H\) terms; the formula adds their contributions at each numerical index. The characteristic-two formula is separate because fibers then have multiplicity \(q\), which need not be at most four.

## Proof
In characteristic two the function \(h_a(t)=t^4+at^2\) is additive, so \(C_a\) is an additive subgroup of \(F^2\) of order \(q\). Every point of this subgroup has exactly \(q\) ordered representations as a sum of two graph points, and other targets have none.

Assume that \(q\) is odd. Fix the first-coordinate sum \(s=x+y\) and write \(x=(s+t)/2\) and \(y=(s-t)/2\). Direct expansion gives
\[
8\bigl(h_a(x)+h_a(y)\bigr)=t^4+(6s^2+4a)t^2+s^4+4as^2.
\]
The affine transformation of the target coordinate on the left changes neither fiber sizes nor their multiplicity histogram. Thus, for each \(s\), it suffices to count the fibers of \(t\mapsto t^4+B_st^2\).

If \(B_s=0\), the map is \(t\mapsto t^4\). Its zero fiber has one element, its nonzero image values have \(d=\gcd(4,q-1)\) preimages each, and its other targets have none. This is exactly the histogram \(D_j\).

Suppose \(B=B_s\ne0\), and put \(\lambda=\chi(-B)\). The target attained by \(t=0\) is also attained by the nonzero roots of \(t^2=-B\); its multiplicity is \(1+2\mathbf 1_{\lambda=1}\), equal to one for \(\lambda=-1\) and three for \(\lambda=1\). Every other nonempty fiber consists of \(\pm t\) pairs and therefore has multiplicity two or four. This immediately gives \(H_1=(1-\lambda)/2\) and \(H_3=(1+\lambda)/2\).

To count the four-element fibers, set \(w=t^2\). Distinct nonzero squares \(w_1,w_2\) satisfy
\[
w_1^2+Bw_1=w_2^2+Bw_2
\quad\Longleftrightarrow\quad w_1+w_2=-B.
\]
The elementary quadratic-character identity
\[
\sum_{z\in F}\chi(z(1-z))=-\chi(-1)=-\epsilon
\]
shows that the number of *ordered* pairs of nonzero squares summing to \(-B\) is
\[
O=\frac{q-2-2\lambda-\epsilon}{4}.
\]
Indeed, write the pairs as \((-Bz,-B(1-z))\), expand the two nonzero-square indicators, and use \(\sum\chi(z)=0\). A pair on the diagonal exists exactly when \(-B/2\) is a square; the diagonal count is \((1+\tau\lambda)/2\). Every unordered pair of *distinct* nonzero squares yields one four-element fiber. Consequently,
\[
H_4=\frac12\left(O-\frac{1+\tau\lambda}{2}\right)
=\frac{q-4-\epsilon-2\lambda(1+\tau)}8.
\]
All \(q\) inputs appear in the fibers; therefore
\(H_1+2H_2+3H_3+4H_4=q\), which determines the displayed \(H_2\). As there are exactly \(q\) possible second-coordinate targets, \(\sum_{j=0}^4H_j=q\), determining \(H_0\). Each expression is a count of an actual fiber type, proving integrality and nonnegativity without relying on the displayed fractions alone.

The number of first-coordinate slices with \(B_s=0\) is \(Z\). The difference between the numbers of nonzero slices of quadratic character \(+1\) and \(-1\) is \(T\). These two facts give \(n_\pm=(q-Z\pm T)/2\) and the complete formula for \(A_j\). For \(\operatorname{char}F\ge5\) and \(a\ne0\), completing the square in \(6s^2+4a\) and using \(\sum_{s\in F}\chi(s^2+c)=-1\) when \(c\ne0\) yields the asserted \(Z\) and \(T\). For \(a=0\), the only zero is \(s=0\) and \(\chi(-6s^2)=\chi(-6)\) for nonzero \(s\). In characteristic three, \(B_s=4a=a\) is independent of \(s\), which gives the separate listed values.

Finally, summing \(A_j\) over positive multiplicities gives the sumset size because a nondegenerate slice has
\[
\sum_{j=1}^4 H_j(\lambda)=\frac{3q+4+\epsilon+2\lambda(\tau-1)}8
\]
and a zero-parameter slice has \(1+(q-1)/d\) positive targets. For nonzero \(a\) in characteristic at least five, \(T=-\chi(-6)\) is constant and \(Z\in\{0,2\}\); substituting \(d=4\) when \(q\equiv1\pmod4\), or \(d=2\) when \(q\equiv3\pmod4\), proves the sharp signed gap. Squaring and summing the multiplicities in \(D\) and \(H\) yields the stated energy formula. These arguments cover all field sizes, not only those computationally tested.

## Verification
Run `python verify_even_quartic_graph.py` from this directory with Python 3 and the standard library only. The checker constructs finite-field arithmetic explicitly, enumerates all \(q^2\) ordered graph pairs per coefficient, records every target multiplicity including zero, and independently compares the result with the theorem for \(618\) coefficient cases in \(41\) finite fields, including nonprime fields. Its successful execution prints `VERIFY_OK finite_fields=41 coefficient_cases=618`. It also checks that the derived spectra account for exactly \(q^2\) targets and \(q^2\) ordered pairs. This is finite corroboration, **not** an infinite proof; the preceding argument provides the proof.

## Relationship to prior work
Mockenhaupt and Tao (2002), especially their section on even exponents, explain the representation-count and Fourier-energy framework, but do not analyze this even-quartic one-parameter graph family. Zhi-Hong Sun (online 2005; journal 2006), Theorem 2.1, computes the **one-variable** image cardinality of \(t^4+bt^2\) over prime fields; Ding and Zieve (2023), Section 3, study its image and power sums over general odd finite fields. Their local value-set information applies to an individual first-coordinate slice after the change of variables above. Thus the **sumset cardinality alone has a route through that earlier local work**; the claimed new object is the complete globally assembled target *multiplicity distribution*, including zero targets, the characteristic-three/two branches, the all-characteristic energy, and the exact coefficient-square-class bifurcation. We do not claim the local quartic image cardinality as new.

A published 2026 result on \(\{(t,t^4)\}\) computes the additive energy at coefficient \(a=0\) in characteristics other than two and three. The formula above specializes to its energy result in that range, so this special case is acknowledged as **covered** rather than independently original; the nonzero-coefficient spectra and exceptional characteristics are not covered there. A separately published fifth-power graph spectrum concerns \(\{(t,t^5)\}\), not the deformation studied here. Character orthogonality relates the computed energy to a constant-input fourth Fourier-extension moment, but no sharp operator norm for arbitrary inputs is asserted.

## Limitations
The result is restricted to sums of **two** points on the indicated graphs; it does not treat higher sumsets, all polynomial deformations, or the optimal weighted Fourier-extension constant. The mathematical identities are elementary once the reduction to square-pair counting is recognized. The classification's originality has been checked against the closest located literature, but unindexed work on correlated quartic fiber distributions may imply an equivalent result. Independent mathematical validation remains outstanding.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (18 April 2002), especially Section 5. https://arxiv.org/abs/math/0204234
2. Zhi-Hong Sun, *On the number of incongruent residues of \(x^4+ax^2+bx\) modulo \(p\)*, *Journal of Number Theory* **119** (2006), 210–241; first online 15 December 2005, Theorem 2.1. DOI:10.1016/j.jnt.2005.10.012. https://maths.hytc.edu.cn/__local/F/F9/62/93E0759CBCD3FFD65A5BB7F3767_7DBD24B5_40CB9.pdf
3. Z. Ding and M. E. Zieve, *On sums of powers of consecutive squares over finite fields, and sums of distinct values of polynomials*, arXiv:2309.14979v1 (26 September 2023), Section 3. https://arxiv.org/abs/2309.14979
4. *Exact additive energy of the finite-field quartic graph*, published mathematical result (2026), publicly accessible at https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f
5. *Complete two-sum spectrum of the finite-field fifth-power graph*, published mathematical result (2026), publicly accessible at https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-two-sum-spectrum-of-the-finite-field-fifth-power-graph--f9410cde2e91
