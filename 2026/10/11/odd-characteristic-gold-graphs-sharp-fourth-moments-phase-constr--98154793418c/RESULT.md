# Odd-characteristic Gold graphs: sharp fourth moments, phase constraints and exact deficits

## Finding

Let \(p\) be an odd prime, let \(m,k\geq1\), let \(F=\mathbb F_{p^m}\), and put \(q=p^m\), \(d=\gcd(m,k)\), and \(e=p^k+1\). The curve \(\Gamma=\{(t,t^e):t\in F\}\subset F^2\) defines the extension operator
\[
Tf(\xi,\eta)=\sum_{t\in F} f(t)\psi(\xi t+\eta t^e),
\]
for any fixed nontrivial additive character \(\psi\) of \(F\). Give the input counting-measure \(\ell^2(F)\) and the output probability-measure \(L^4(F^2)\). Define \(g=\gcd(p^k+1,q-1)\). Then
\[
\boxed{\|T\|_{\ell^2\to L^4}^{4}=g-\frac{g-1}{q}},\qquad
\boxed{g=\begin{cases}2,&m/d\text{ odd},\\p^d+1,&m/d\text{ even}.\end{cases}}
\]
Every nonzero maximizer has constant positive modulus: \(f=c\,u\) for \(c\in\mathbb C\setminus\{0\}\) and \(|u(t)|=1\) for all \(t\in F\). The **necessary-and-sufficient phase condition** is
\[
 u\!\left(\frac{s+h}{2}\right)u\!\left(\frac{s-h}{2}\right)
 =u\!\left(\frac{s+\zeta h}{2}\right)u\!\left(\frac{s-\zeta h}{2}\right)
 \quad(s,h\in F,\ \zeta\in H),
\]
where \(H=\{\zeta\in F^\times:\zeta^e=1\}\). Thus all unit-modulus phase patterns are maximizers in the odd \(m/d\) (planar) regime; in the even \(m/d\) regime there are genuine additional constraints, but also non-additive maximizers given by suitable quadratic trace phases \(u(t)=\exp(2\pi i\operatorname{Tr}_{F/\mathbb F_p}(\alpha t^{p^d+1})/p)\).

There is also a sharp **topological phase-rigidity dichotomy**: after quotienting by a common scalar of modulus one, the extremizer-phase space is a torus of real dimension \(q-1\) when \(m/d\) is odd, but a **finite group** when \(m/d\) is even. In the finite-group regime, not all phases are additive characters, because the quadratic-trace examples above are genuinely nonlinear.

The theorem includes an exact nonnegative **fourth-moment deficit identity**, displayed below, not only the operator norm.

## Assumptions and scope

All claims hold for every odd prime \(p\) and positive integers \(m,k\), including prime fields, extension fields, and arbitrary positive \(k\) (the exponent can exceed the field order). The additive character is arbitrary but nontrivial. No normalization factor is inserted in \(T\); the input squared norm is \(\sum_{t\in F}|f(t)|^2\), and the fourth output norm is \(q^{-2}\sum_{\xi,\eta\in F}|Tf(\xi,\eta)|^4\).

For \(s,h\in F\), define \(u_s(h)=f((s+h)/2)f((s-h)/2)\). Let \(\mathcal O\) run over the orbits of the multiplicative group \(H\) on \(F^\times\). Put \(S=\sum_t|f(t)|^2\). The exact identity is
\[
\begin{aligned}
&\left(g-\frac{g-1}{q}\right)S^2-\|Tf\|_{L^4}^{4}\\
&\qquad=(g-1)\left(\sum_t|f(t)|^4-\frac{S^2}{q}\right)
+\sum_{s\in F}\sum_{\mathcal O}\sum_{\{h,h'\}\subset\mathcal O}
|u_s(h)-u_s(h')|^2.
\end{aligned}
\]
The inner sum takes each unordered distinct pair in the orbit exactly once; both terms on the right are nonnegative.

## Proof

**Fourier orthogonality.** Set
\[
R_f(s,y)=\sum_{\substack{a+b=s\\a^e+b^e=y}}f(a)f(b).
\]
Expanding the fourth output moment and applying orthogonality of additive characters in both ambient coordinates gives the exact convolution formula
\[
\|Tf\|_{L^4}^{4}=\sum_{s,y\in F}|R_f(s,y)|^2.
\]
This formula has no remaining power of \(q\), because the output normalization \(q^{-2}\) cancels the two orthogonality sums.

**Root-of-unity collision fibers.** Since \(p\) is odd, every ordered pair \((a,b)\) has unique coordinates \(s=a+b\), \(h=a-b\). The Frobenius identity \((x+y)^{p^k}=x^{p^k}+y^{p^k}\) yields
\[
a^e+b^e=\frac{s^e+h^e}{2}.
\]
Consequently, for each fixed \(s\), the fiber with \(h=0\) is a singleton, and every nonzero fiber is an orbit \(hH\) with exactly \(g\) elements. In these coordinates the preceding convolution identity reads
\[
\|Tf\|_{L^4}^{4}=\sum_s|u_s(0)|^2+
\sum_s\sum_{\mathcal O}\left|\sum_{h\in\mathcal O}u_s(h)\right|^2.
\]
For any \(g\) complex numbers \(z_h\), the exact identity
\[
g\sum_h|z_h|^2-\left|\sum_h z_h\right|^2
=\sum_{\{h,h'\}}|z_h-z_{h'}|^2
\]
shows that replacing every orbit sum by \(g\sum_h|u_s(h)|^2\) produces precisely the nonnegative orbit deficit. The bijection between \((s,h)\) and \((a,b)\) gives
\[
\sum_{s,h}|u_s(h)|^2=S^2,
\qquad\sum_s|u_s(0)|^2=\sum_t|f(t)|^4.
\]
Hence
\[
\|Tf\|_{L^4}^4=gS^2-(g-1)\sum_t|f(t)|^4
-\sum_s\sum_{\mathcal O}\sum_{\{h,h'\}\subset\mathcal O}|u_s(h)-u_s(h')|^2.
\]
Subtracting from \((g-(g-1)/q)S^2\) gives the asserted exact deficit identity. Since \(\sum_t|f(t)|^4\geq S^2/q\), the claimed upper bound follows. Constant nonzero \(f\) makes both deficits vanish, so the bound is sharp. Equality for nonzero \(f\) requires and is implied by constant modulus and equality of \(u_s(h)\) on every multiplicative \(H\)-orbit. This is exactly the displayed phase condition; it is a complete test for all complex maximizers without an unproved assertion that every phase admits a quadratic parametrization.

**Arithmetic dichotomy.** Writing \(d=\gcd(m,k)\), \(a=m/d\), \(b=k/d\), and \(Y=p^d\), one has \(\gcd(a,b)=1\) and
\[
g=\gcd(Y^b+1,Y^a-1).
\]
The elementary Euclidean gcd identity for odd \(Y\) gives \(2\) when \(a\) is odd, and \(Y+1\) when \(a\) is even (then \(b\) is odd). This proves the formula for \(g\). If \(g=2\), \(H=\{1,-1\}\), and \(u_s(h)=u_s(-h)\) automatically: all constant-modulus functions maximize. If \(g=p^d+1\), every \(\zeta\in H\) obeys \(\zeta^{p^d+1}=1\); therefore the trace-quadratic phase stated above has a sum of exponents invariant under \(h\mapsto\zeta h\). To see that genuinely non-additive examples exist, choose \(\alpha\in F\) with \(\operatorname{Tr}(2\alpha)\ne0\). Then the additive second difference of the exponent at \((1,1)\) equals \(\operatorname{Tr}(2\alpha)\), so the resulting phase cannot be an additive character times a scalar.

**Finite phase rigidity in the nonplanar case.** Let \(g>2\) and fix \(\zeta\in H\setminus\{1,-1\}\). The phase relations define a compact abelian subgroup of \((S^1)^F\) by finitely many integral monomial equations. Let \(L\subset\mathbb Z^F\) be the integral lattice generated by their exponent vectors. Its real orthogonal complement consists of functions \(\theta:F\to\mathbb R\) satisfying
\[
\theta(x+y)+\theta(x-y)=\theta(x+\zeta y)+\theta(x-\zeta y)
\qquad(x,y\in F).
\]
Fourier transform in the variable \(x\) shows that a nontrivial additive frequency \(\chi_\beta(x)=\exp(2\pi i\operatorname{Tr}(\beta x)/p)\), \(\beta\ne0\), could occur only if
\[
\chi_\beta(y)+\chi_\beta(-y)=\chi_\beta(\zeta y)+\chi_\beta(-\zeta y)
\quad\text{for every }y\in F.
\]
For two unit complex numbers \(z,z'\), equality \(z+z^{-1}=z'+z'^{-1}\) forces \(z'=z\) or \(z'=z^{-1}\). Thus for every \(y\) one has \(\operatorname{Tr}(\beta\zeta y)=\pm\operatorname{Tr}(\beta y)\) in \(\mathbb F_p\). The union of two proper linear subspaces cannot cover \(F\), so one sign must hold identically. By nondegeneracy of the trace pairing this forces \(\beta\zeta=\pm\beta\), contrary to \(\beta\ne0\) and \(\zeta\notin\{\pm1\}\). Hence the real solution space is exactly the constants. Therefore \(\mathbb Z^F/L\) has free rank one and finite torsion; the phase solution group \(\operatorname{Hom}(\mathbb Z^F/L,S^1)\), modulo its scalar circle, is finite. If \(g=2\), by contrast, there are no phase constraints beyond unit modulus, leaving the full \((S^1)^{q-1}\) quotient torus.

## Verification

Run `python3 artifacts/verify.py` from the directory containing this report and the accompanying `artifacts/verify.py`. The standalone Python checker uses explicit prime-power field arithmetic and verifies the collision-orbit count, the exact integer-amplitude deficit identity, the arithmetic dichotomy, quadratic-trace phase feasibility, nonlinearity in the nonplanar cases, and selected direct Fourier fourth moments. Its parameter cases include \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_9\), \(\mathbb F_{25}\), \(\mathbb F_{27}\), \(\mathbb F_{49}\), and \(\mathbb F_{81}\), including two different exponents over \(\mathbb F_{81}\). These finitely many computations corroborate but do not establish the all-field theorem; the proof above supplies universal quantifiers.

## Relationship to prior work

Mockenhaupt and Tao introduced finite-field Fourier restriction and its use of algebraic surface structure. The 2024 sharp-extension work of González-Riquelme and Oliveira e Silva treats other surfaces and endpoint exponents, specifically the two-dimensional paraboloid at fourth moment and the one-dimensional parabola at sixth moment. Beierle and Felke discuss the established planarity classification of odd-characteristic Dembowski–Ostrom monomials. The odd-characteristic Gold graph in the present fourth-moment normalization and its nonplanar sharp phase-orbit deficit are distinct from those stated results. The planarity arithmetic criterion itself is not claimed as new. The nonplanar branch is the essential structural distinction.

## Limitations

The phase-orbit equation is a necessary-and-sufficient classification, and the nonplanar projective solution group is proven finite, but its exact group structure and cardinality are not determined. No claim is made about higher even Fourier moments, other monomial exponents, or characteristic two. Tests cover only the specified finite fields. The possible presence of an equivalent fourth-moment identity in older additive-energy or coding-theoretic language remains a literature-priority risk.

## References

1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first public preprint 2002-04-18; especially the restriction framework and normalization.
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647; Theorems 1.1–1.3 and the convolution calculations.
3. C. Beierle and P. Felke, *On matrix algebras isomorphic to finite fields and planar Dembowski–Ostrom monomials*, arXiv:2211.17103; introduction on the odd-characteristic Gold planarity criterion.
