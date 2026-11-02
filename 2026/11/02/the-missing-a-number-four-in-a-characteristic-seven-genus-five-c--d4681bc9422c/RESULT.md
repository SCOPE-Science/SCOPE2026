# The missing \(a\)-number four in a characteristic-seven genus-five cover family

## Finding
Let \(k\) be algebraically closed of characteristic \(7\), and let \(t,u\in k\setminus\{0,1\}\), \(t\ne u\). Denote by \(X_{t,u}\) the smooth projective normalization of
\[
 z^4=(w^2-1)^2(w^2-t)(w^2-u).
\]
Its genus is five. Write \(a(X)=\dim_k\operatorname{Hom}(\alpha_7,\operatorname{Jac}(X)[7])\), equivalently the dimension of the kernel of the Cartier operator on holomorphic differentials. Then
\[
 \boxed{a(X_{t,u})=2+\mathbf1_{u/t\in\{2,4,6\}}+2\mathbf1_{t+u=1,\;tu=1}.}
\]
The only occurring values are \(2,3,5\); the value \(4\) is absent. The \(a=3\) locus is the union of the three punctured lines \(u=2t\), \(u=4t\), \(u=6t\), with two points removed. The \(a=5\) locus is exactly \((3,5)\) and \((5,3)\), both defined over \(\mathbb F_7\); these are two ordered presentations of one curve, not two asserted isomorphism classes. The isolated jump locus is reduced. Among the twenty ordered smooth presentations over \(\mathbb F_7\), the frequencies of \(a=2,3,5\) are \(8,10,2\).

## Assumptions and scope
All geometric assertions concern the algebraic closure of \(\mathbb F_7\). Distinct ordered pairs may present the same curve. No classification of isomorphism classes or assertions about higher characteristics are made. The displayed curve is birational to the unramified double cover \(w^2=x\) of the cyclic genus-three curve \(y^4=x^2(x-1)^2(x-t)(x-u)\), upon setting \(z=y/w\). This is the family studied by Booher and Pries, but the proof below works directly with the genus-five Kummer model. Set \(s=t+u\), \(v=tu\), and
\[
 G(X)=(X-1)^2(X^2-sX+v),\qquad F(w)=G(w^2).
\]
Smoothness of the parameter presentation is equivalent to
\[
 \Delta=v(v-s+1)(s^2-4v)\ne0.
\]
All numerical polynomial identities below are in \(\mathbb F_7[s,v]\).

## Proof
**Genus and regular differentials.** The tame degree-four map to the \(w\)-line is branched at the two roots of \(w^2-1\), each of inertia two, and the four roots of \((w^2-t)(w^2-u)\), each of inertia four; infinity is unramified. Riemann--Hurwitz gives \(2g-2=-8+2\cdot2+4\cdot3=8\), hence \(g=5\). The following five differentials are regular and linearly independent:
\[
 \eta_0=dw/z,\quad \eta_1=(w^2-1)dw/z^2,\quad
 \eta_2=(w^2-1)dw/z^3,\quad
 \eta_3=w(w^2-1)dw/z^3,\quad
 \eta_4=w^2(w^2-1)dw/z^3.
\]
For example, at a simple order-four branch, \(\operatorname{ord}(z)=1\) and \(\operatorname{ord}(dw)=3\); at either inertia-two branch, the orders are \(1\) and \(1\); and at infinity the orders of \(w,z,dw\) are \(-1,-2,-2\). These valuations prove holomorphy. The different characters of \(z\mapsto iz\), and the polynomial degrees inside the character-three subspace, prove independence. Since the genus is five, the displayed forms are a basis.

**Cartier blocks.** For each \(j\in\{1,2,3\}\), choose \(j'\in\{1,2,3\}\) with \(7j'\equiv j\pmod4\). The Cartier operator satisfies
\[
 \mathcal C\left(\frac{h(w)\,dw}{z^j}\right)
 =\frac1{z^{j'}}\mathcal C\left(h(w)F(w)^{(7j'-j)/4}dw\right),
\]
where on polynomials \(\mathcal C(\sum c_mw^m\,dw)=\sum c_{7r+6}^{1/7}w^r\,dw\). Its character transitions are \(1\leftrightarrow3\) and \(2\to2\). Write
\[
 \alpha_0=[X^3](X-1)^3(X^2-sX+v)=3s+v+3,
\]
\[
 \alpha_1=[X^2](X-1)^3(X^2-sX+v)=-3s-3v-1,
\]
\[
 \beta_0=[X^{10}]G(X)^5,\qquad \beta_1=[X^{17}]G(X)^5,
\]
\[
 \gamma=[X^3](X^2-sX+v)^3.
\]
Here each bracket denotes an exact polynomial coefficient. Cartier on the three forms with denominator \(z^3\) has a single-row image in the \(z^{-1}\)-character, with nonzero coefficients only \(\alpha_0,\alpha_1\) (the middle basis element has odd numerator and maps to zero). Cartier on \(\eta_0\) has image in the \(z^{-3}\)-character and is nonzero exactly when \((\beta_0,\beta_1)\ne(0,0)\); the coefficients in degrees \(0,2,4\) are constrained by their sum being zero, because the image is divisible by \(w^2-1\). Cartier on \(\eta_1\) has the scalar \(\gamma^{1/7}\). Therefore
\[
 \operatorname{rank}\mathcal C
 =\mathbf1_{(\alpha_0,\alpha_1)\ne(0,0)}
 +\mathbf1_{(\beta_0,\beta_1)\ne(0,0)}
 +\mathbf1_{\gamma\ne0}.
\]
The three images have disjoint character blocks, so their ranks add.

**Exact common-zero computation.** Elementary linear algebra gives
\(\langle\alpha_0,\alpha_1\rangle=\langle s-1,v-1\rangle\). For reproducibility, the two remaining coefficient polynomials are
\[
 \begin{aligned}
 \beta_0={}&3s^3v^2+3s^3+2s^2v^3+2s^2+sv^4-sv^3-sv+s\\
 &+v^5+v^4+v+1,\\
 \beta_1={}&-3s^3-2s^2+sv-s-v-1.
 \end{aligned}
\]
An exact lexicographic Gröbner-basis calculation in \(\mathbb F_7[h,s,v]\), ordered \(h>s>v\), gives
\[
 \operatorname{GB}_{\rm lex}
 \langle\beta_0,\beta_1,h\Delta-1\rangle
 =\{h-2,\ s-1,\ v-1\}.
\]
The full generating polynomials and a replay of Buchberger's exact finite-field computation are provided in `verify.py` (no numerical tolerance or sampling). Since \(\Delta\ne0\), this establishes that the two \(\beta\)-coefficients vanish simultaneously precisely at \((s,v)=(1,1)\). At that point \(\Delta=4\ne0\); both vanishing ideals localize to the reduced maximal ideal \((s-1,v-1)\).

**Central block and final strata.** The freshman's-dream identity \((X-1)^7=X^7-1\) yields
\[
 \gamma=[X^3](X-t)^3(X-u)^3=-t^3H_7(u/t),
\]
where
\[
 H_7(\lambda)=1+2\lambda+2\lambda^2+\lambda^3
 =(\lambda-2)(\lambda-4)(\lambda-6).
\]
If \((s,v)=(1,1)\), then \((t,u)=(3,5)\) or \((5,3)\), and the ratio is respectively \(4\) or \(2\), so \(\gamma=0\) as well. Away from these two points, the two off-diagonal Cartier blocks each have rank one. Thus the displayed formula for \(a=5-\operatorname{rank}\mathcal C\) follows, including the absence of value \(4\). The map from ordered parameters to \((s,v)\) is étale away from \(s^2-4v=0\), so the two-point exceptional locus is reduced.

Over \(\mathbb F_7\), there are \(5\cdot4=20\) smooth ordered parameter pairs. Each of the three lines \(u=2t,4t,6t\) contains four of these pairs, for twelve points in the central Cartier-zero locus. Two are exceptional, leaving ten with \(a=3\), eight with \(a=2\), and two with \(a=5\).

## Verification
Run `python verify.py` and `python direct_check.py` with the symbolic dependency in `requirements.txt`. The script recomputes the four coefficient polynomials, the characteristic-seven Legendre factorization, the holomorphy coefficient identities, both Gröbner bases, and the complete twenty-pair \(\mathbb F_7\) frequency table. The first returns `VERIFY_OK`; the independent direct-matrix check returns `DIRECT_OK`. The geometric theorem is proved by exact identities over \(\mathbb F_7[s,v]\) and a tame-cover differential basis; the finite rational-parameter enumeration checks only the final frequency corollary.

## Relationship to prior work
Booher and Pries (arXiv:2410.20262v1, 26 October 2024) introduced the genus-three cyclic-cover family and the associated genus-five étale double covers; their Propositions 2.6 and 3.5 classify the supersingular locus by Hasse-type polynomials. Those conditions concern stable Frobenius rank and do not give this full one-step Cartier-rank stratification, the missing value \(4\), or the reduced two-point jump locus in characteristic seven. Ohashi (arXiv:2604.18074v1, 20 April 2026) establishes existence of genus-five superspecial curves in characteristic seven using generalized Howe curves with completely decomposable Jacobians; this does not identify the Cartier strata of the present two-parameter family. Elkin's general work on Cartier ranks of tame cyclic covers provides bounds and techniques rather than this concrete specialized classification.

## Limitations
This is a complete \(a\)-number classification only for characteristic seven and the indicated smooth two-parameter presentations. It does not assert that distinct coefficient pairs represent distinct geometric isomorphism classes, does not give all Newton polygons or Ekedahl--Oort types, and does not classify characteristic \(p\ne7\). Existing general cyclic-cover theory could provide an alternative derivation; definitive historical priority and independent validation remain open.

## References
- Jeremy Booher and Rachel Pries, *Supersingular curves of genus five for primes congruent to three modulo four*, arXiv:2410.20262v1 (first submitted 2024-10-26), especially equation (2.4) and Propositions 2.6, 3.4, 3.5.
- Ryo Ohashi, *Superspecial generalized Howe curves of genus 4, 5, and 6 with completely decomposable Jacobians*, arXiv:2604.18074v1 (submitted 2026-04-20), especially Section 4 and Appendix A.
- Arsen Elkin, *The rank of the Cartier operator on cyclic covers of the projective line*, Journal of Algebra 327 (2011), 1–12; arXiv:0708.0431.
