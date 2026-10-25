# Exact zeta function and a simple ordinary surface factor of an equianharmonic genus-ten generalized Fermat curve over \(\mathbb F_4\)

## Finding
Put \(k=\mathbb F_4=\mathbb F_2(\omega)\), with \(\omega^2+\omega+1=0\). The smooth projective complete-intersection curve
\[
X:\quad V^3+U^3+Z^3=0,\qquad W^3+U^3+\omega Z^3=0
\]
in \(\mathbb P^3_k\) has genus \(10\) and zeta function
\[
Z(X/k,T)=\frac{(1-2T+4T^2)^2(1+4T+4T^2)^2(1+T+4T^2)^2(1-T-3T^2-4T^3+16T^4)^2}{(1-T)(1-4T)}.
\]
The quartic factor \(D(T)=1-T-3T^2-4T^3+16T^4\) is irreducible over \(\mathbb Q\) and defines a \(k\)-simple ordinary abelian-surface isogeny factor occurring twice in \(\operatorname{Jac}(X)\). The Jacobian has \(2\)-rank \(6\), \(a\)-number \(4\), and Newton slopes \(0^{[6]},(1/2)^{[8]},1^{[6]}\). In particular \(\#X(k)=9\), \(\#X(\mathbb F_{16})=9\), \(\#X(\mathbb F_{64})=63\), and \(\#X(\mathbb F_{256})=225\). The displayed zeta function determines all extension-field counts.

## Assumptions and scope
All varieties and isogenies are over \(k=\mathbb F_4\), not merely over its algebraic closure. The equations define the particular coordinate-marked \(k\)-model above; no claim is made that other Kummer twists have the same zeta function. The two cubics form a smooth intersection: their gradients are \( (U^2,V^2,0,Z^2)\) and \( (U^2,0,W^2,\omega Z^2)\); dependence at a common projective zero forces \(U=V=W=Z=0\), or, with both coefficients nonzero, \(U=V=W=Z=0\) after using \(\omega\ne1\). Thus no projective singular points exist.

## Proof
**Cover, connectedness and genus.** On the chart \(Z=1\), write \(t=U^3\). Then
\[
U^3=t,\qquad V^3=t+1,\qquad W^3=t+\omega.
\]
The three Kummer classes in \(\overline{k}(t)^\times/\overline{k}(t)^{\times3}\) are independent: valuation at \(0,1,\omega\), respectively, selects each generator. Consequently the function field is a connected Galois extension of degree \(27\) with deck group \(G=(\mathbb Z/3\mathbb Z)^3\), since \(\mu_3\subset k\). The four branch points are \(0,1,\omega,\infty\), each with inertia group of order \(3\). The tame Riemann–Hurwitz formula gives \(2g-2=27(-2)+4\cdot18=18\), hence \(g=10\). This independently agrees with complete-intersection adjunction.

**Thirteen character-line quotients.** For each nonzero \(v=(a,b,c)\in(\mathbb Z/3)^3\) modulo \(v\sim-v\), let \(C_v\) be the smooth completion of
\[
y^3=t^a(t+1)^b(t+\omega)^c,\quad a,b,c\in\{0,1,2\}.
\]
These are all \(13\) index-three cyclic quotients of \(X\). Their branch number is \(r_v=\mathbf 1_{a\ne0}+\mathbf 1_{b\ne0}+\mathbf 1_{c\ne0}+\mathbf 1_{a+b+c\not\equiv0\pmod3}\), so \(g(C_v)=r_v-2\). Six quotient curves have genus \(0\), four have genus \(1\), and three have genus \(2\). Their positive genera sum to \(10\). For any prime \(\ell\ne2,3\), the \(G\)-action on \(H^1_{\mathrm{et}}(X_{\overline{k}},\mathbb Q_\ell)\) splits into characters because \(3\) is invertible. Every nontrivial character lies in exactly one unordered inverse pair and occurs in the corresponding \(H^1(C_v)\); the trivial-character part is \(H^1(\mathbb P^1)=0\). All deck actions and quotients are defined over \(k\), so Frobenius commutes with the splitting. Hence \(P_X(T)=\prod_{v:g(C_v)>0}P_{C_v}(T)\), including multiplicities; this does not assume an unverified characteristic-zero isogeny specialization.

**Exact arithmetic table.** For \(K=\mathbb F_{4^m}\), define \(\rho_K(h)=1\) when \(h=0\), \(\rho_K(h)=3\) when \(h\ne0\) is a cube, and \(\rho_K(h)=0\) otherwise. The number of \(K\)-points on \(C_v\) equals \(\sum_{t\in K}\rho_K(t^a(t+1)^b(t+\omega)^c)\) plus \(3\) points over infinity when \(a+b+c\equiv0\pmod3\), and \(1\) otherwise. These integer sums for \(K=\mathbb F_4\) and \(\mathbb F_{16}\) are exactly:

| Character representative \(v\) | Genus | \(\#C_v(\mathbb F_4)\) | \(\#C_v(\mathbb F_{16})\) | Numerator \(P_{C_v}(T)\) |
| --- | ---: | ---: | ---: | --- |
| \((0,1,1)\), \((1,0,1)\) | 1 each | 3 each | 21 each | \(1-2T+4T^2\) each |
| \((1,1,0)\), \((1,1,1)\) | 1 each | 9 each | 9 each | \(1+4T+4T^2\) each |
| \((1,1,2)\) | 2 | 7 | 31 | \((1+T+4T^2)^2\) |
| \((1,2,1)\), \((1,2,2)\) | 2 each | 4 each | 10 each | \(D(T)\) each |

For a genus-one quotient, its numerator is determined by \(s_1=5-N_1\): \(P(T)=1-s_1T+4T^2\). For a genus-two quotient, its first two traces \(s_1=5-N_1\) and \(s_2=17-N_2\) determine the full numerator by the genus-two functional equation:
\[
P(T)=1-s_1T+\tfrac{s_1^2-s_2}{2}T^2-4s_1T^3+16T^4.
\]
For example, the final two quotient curves have \(s_1=1\), \(s_2=7\), whence \(P(T)=D(T)\). Multiplying the seven displayed polynomials gives the asserted degree-20 numerator. No extrapolation from a finite list of extension counts is used: exactly two finite base-field counts determine the genus-two factors by the functional equation.

**Irreducibility and arithmetic type.** Let \(Q(z)=z^4-z^3-3z^2-4z+16=z^4D(1/z)\). The Weil property puts every complex root on the circle of radius \(2\). Its only possible rational roots are \(\pm2\), and \(Q(2)=4\), \(Q(-2)=36\). A factorization into two rational quadratics would therefore pair conjugate nonreal roots, each quadratic having constant term \(4\) (the product of each conjugate pair), hence form \((z^2-az+4)(z^2-bz+4)\) with \(a,b\in\mathbb Z\). Coefficient comparison yields \(a+b=1\) and \(ab=-11\); but \(x^2-x-11\) has nonsquare discriminant \(45\). Thus \(Q\) is irreducible over \(\mathbb Q\). The abelian surface with Frobenius polynomial \(Q\) is consequently \(k\)-simple. Since the coefficient of \(T^2\) in \(D(T)\) is odd, it is ordinary. The other factors show four supersingular elliptic factors (traces \(\pm2\) over \(\mathbb F_4\)) and two ordinary elliptic factors (trace \(-1\)) up to a prime-to-two decomposition induced by \(G\), along with two ordinary simple genus-two factors. Hence \(2\)-rank \(6\) and Newton slopes as stated. The same prime-to-two decomposition, or the known Cartier calculation, gives \(a=4\); this \(a\)-number was previously established for the full family, and is not asserted to be new.

**All extension counts.** Because each nonzero field element has either zero or three cube roots, the full covering has
\[
\#X(\mathbb F_{4^m})=9+\sum_{t\in\mathbb F_{4^m}}\rho(t)\rho(t+1)\rho(t+\omega).
\]
All nine points above infinity are rational over \(\mathbb F_4\). For \(m=1,2,3,4\), the formula gives respectively \(9,9,63,225\), agreeing with the independently reconstructed numerator above.

## Verification
The included `verify.py` uses only the Python standard library, constructs fields with \(4\), \(16\), \(64\) and \(256\) elements, checks all seven quotient sums and their numerator factors, independently counts full-cover points for the four extension degrees, and enumerates all \(85\) projective \(\mathbb F_4\)-points of \(\mathbb P^3\). Run `python verify.py`; the expected terminal marker is `VERIFY_OK`. The proof of the extension-uniform formula is the character decomposition, not the finite-field sample.

## Relationship to prior work
Hidalgo's 2017 preprint establishes the generalized Fermat model and, in characteristic two, the family-wide \(2\)-rank \(6\) and \(a\)-number \(4\). Carvacho–Hidalgo–Quispe's earlier work establishes the general Jacobian quotient decomposition, including genus-one and genus-two quotients for type \((3,3)\). Those results supply the framework but do not state the explicit \(\mathbb F_4\) Frobenius factor \(D(T)\), complete zeta numerator of the displayed twist, or its simple ordinary abelian-surface factor. The extra arithmetic is obtained here by exact quotient point sums and the genus-two functional equation. Related 2022 and 2023 studies of smooth quotients and Jacobian decompositions likewise concern structural geometry, not these finite-field traces.

## Limitations
This is the arithmetic of one explicitly marked \(\mathbb F_4\)-model, not a classification of every twist or parameter. The complete zeta factorization and the irreducible ordinary factor are the claimed contribution; genus, general decomposition, and family-wide \(2\)-rank and \(a\)-number are acknowledged precedents. The exact finite computations identify low-genus Frobenius data, but are not proposed as a standalone proof for all extension degrees. Unindexed classical Jacobi-sum calculations may overlap the present specific arithmetic claim; no independent audit has been performed.

## References
- R. A. Hidalgo, *Holomorphic differentials of generalized Fermat curves*, arXiv:1710.01349 (first publicly posted 2017-10-03), especially Sections 4.4 and 5.3.3.
- M. Carvacho, R. A. Hidalgo, and S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903 (2015), especially Section 6.3.
- R. A. Hidalgo, *Smooth quotients of generalized Fermat curves*, arXiv:2202.12663 (2022).
- G. Martinez-Nunez, *Decomposition of Jacobians of generalized Fermat curves*, arXiv:2303.18056 (2023).
