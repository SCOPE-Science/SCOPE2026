# A uniformly superspecial Prym family in characteristic five

## Finding
Let \(k\) be any algebraically closed field of characteristic \(5\). For each parameter \(a\in k\) with \(a^2\ne4\), let \(C_a\) be the smooth projective model of
\[
 y^3=x^5+a x^3+x.
\]
It has genus \(4\) and the involution \(\tau:(x,y)\mapsto(-x,-y)\). Its genus-two quotient has the explicit hyperelliptic model
\[
 D_a:\qquad w^2=(t^3-a)^2-4.
\]
**Theorem.** The Prym abelian surface
\[
 P_a=\ker(\operatorname{Nm}_{C_a/D_a}:\operatorname{Jac}(C_a)\longrightarrow\operatorname{Jac}(D_a))^0
\]
is **superspecial for every smooth parameter**. Equivalently, it is isomorphic over \(k\) to a product of supersingular elliptic curves. The family of source curves is nonisotrivial: \(\operatorname{Jac}(C_0)\) is superspecial, while for all \(a\ne0\) with \(a^2\ne4\) it has \(5\)-rank \(2\) and \(a\)-number \(2\). For these nonzero parameters, \(\operatorname{Jac}(D_a)\) is ordinary, while \(P_a\) remains superspecial. No assertion is made that the Prym families are isomorphic over their original, possibly non-algebraically-closed fields, nor is a polarization-level classification claimed.

## Assumptions and scope
All curves are replaced by their unique smooth projective models. The polynomial \(f_a(x)=x^5+a x^3+x\) is squarefree precisely when \(a^2\ne4\) in characteristic \(5\). The cyclic degree-three cover of \(\mathbb P^1\) is totally ramified at five distinct finite roots and once at infinity; by Riemann–Hurwitz its genus is \(4\). The involution \(\tau\) fixes exactly \((0,0)\) and the unique point at infinity; it is tame. Consequently the quotient has genus \(2\) by Riemann–Hurwitz, and the connected Prym has dimension \(2\). The characteristic assumption is essential; the result is not a statement about characteristic zero or other residue characteristics.

## Proof
**Quotient.** Away from \(x=0\), the invariants \(t=y/x\) and \(u=x^2\) satisfy
\[
 u^2-(t^3-a)u+1=0.
\]
Putting \(w=2u-(t^3-a)\) gives \(w^2=(t^3-a)^2-4\). Its degree-six right-hand side is squarefree when \(a^2\ne4\): its derivative is \(6t^2(t^3-a)\), and a common zero with \((t^3-a)^2-4\) would force \(t=0\) and \(a^2=4\). Thus this is the smooth quotient model.

**Differentials.** A basis of \(H^0(C_a,\Omega^1)\), obtained from the valuations of \(x,y,dx\) at the unique point at infinity, is
\[
 \omega_0=dx/y,\quad \omega_1=dx/y^2,\quad
 \omega_2=x\,dx/y^2,\quad \omega_3=x^2\,dx/y^2.
\]
The involution acts with \(+1\) on \(\omega_0,\omega_2\) and with \(-1\) on \(\omega_1,\omega_3\). Since the characteristic is not \(2\), the minus-eigenspace is the cotangent space of the Prym.

**Exact Cartier operator.** In characteristic \(5\), the identities \(1/y=f_a(x)^3/y^{10}\) and \(1/y^2=f_a(x)/y^5\) permit the standard Cartier coefficient extraction: only monomials of degree congruent to \(4\) modulo \(5\) contribute. Direct polynomial expansion over \(\mathbb F_5[a,x]\) yields
\[
 [x^4]f_a^3=[x^{14}]f_a^3=0,\qquad
 [x^9]f_a^3=a^3+a,
\]
and
\[
 [x^4]f_a=[x^4](x^2f_a)=0,\qquad [x^4](xf_a)=a.
\]
Therefore the semilinear Cartier operator satisfies
\[
 \mathcal C(\omega_0)=(a^3+a)^{1/5}\omega_2,
 \quad \mathcal C(\omega_2)=a^{1/5}\omega_0,
 \quad \mathcal C(\omega_1)=\mathcal C(\omega_3)=0.
\]
These are polynomial identities in the parameter, not extrapolations from finite testing. In particular Cartier kills the full two-dimensional anti-invariant subspace for **every** smooth parameter. Hence the Prym surface has \(a(P_a)=2=\dim P_a\), and the standard superspecial criterion for abelian varieties implies that \(P_a\) is superspecial.

**Variation of the source curves and quotients.** When \(a=0\), the displayed Cartier operator vanishes, so \(\operatorname{Jac}(C_0)\) is superspecial. For \(a\ne0\) with \(a^2\ne4\), the two nonzero cross-coefficients are invertible, since \(a^3+a=a(a^2-4)\) in characteristic \(5\). Their two-dimensional semilinear block is bijective, so the stable rank is \(2\), the \(5\)-rank is \(2\), and the full Cartier rank is \(2\). These values distinguish \(C_0\) from \(C_a\) for nonzero \(a\); the family is nonisotrivial.

For the quotient, write \(h_a(t)=(t^3-a)^2-4\). The coefficients of \(h_a^2\) give its genus-two Cartier–Manin matrix in the basis \(dt/w,t\,dt/w\):
\[
 \begin{pmatrix}0&a(a^2-4)\\ a&0\end{pmatrix},
\]
up to entrywise fifth roots and the conventional transpose. It is invertible for the same nonzero smooth parameters, so the quotient Jacobian is ordinary. At \(a=0\) it is zero. Alternatively, the degree-a-power-of-two isogeny between \(\operatorname{Jac}(D_a)\times P_a\) and \(\operatorname{Jac}(C_a)\) explains the splitting of the \(5\)-rank and \(a\)-number.

## Verification
The accompanying standalone `verify.py` checks all required Cartier coefficient identities **symbolically** in \(\mathbb F_5[a,x]\), including the genus-two coefficient matrix. It also constructs \(\mathbb F_{25}\) exactly and checks the independent model-point count \(\#C_0(\mathbb F_{25})=66\), consistent with genus-four superspeciality. Running the embedded program with Python 3 prints `VERIFY_OK`. A point count is only a consistency check; the proof for all parameters is the symbolic Cartier computation and Prym decomposition, not sample enumeration.

## Relationship to prior work
Baldwin, Eilbeck, Gibbons and Ônishi study the general genus-four cyclic trigonal equation and Abelian-function theory in arXiv:math/0612654 (first posted 21 December 2006). This supplies established context for the objects, not the stated positive-characteristic Prym phenomenon. Kudo and Harashita, arXiv:1607.01114 (first posted 5 July 2016), classify superspecial genus-four curves in small characteristics: their genus-four superspeciality results concern \(\operatorname{Jac}(C_a)\), not the dimension-two Prym of a varying non-superspecial genus-four curve. Lange and Ortega, arXiv:1902.00251, explain general ramified Prym geometry; their trigonal construction does not supply the characteristic-five Cartier vanishing in this pencil.

Related calculations of the \(5\)-rank of general genus-four cyclic trigonal Jacobians cover the ambient Jacobian's rank, but do not assert uniform superspeciality of this anti-invariant Prym factor. A calculation in characteristic \(7\) for the same named pencil yields the opposite, ordinary Prym behavior; it does not imply the characteristic-five theorem. The additional content here is a **complete positive-dimensional family of superspecial Prym surfaces**, identified by the zero anti-invariant Cartier matrix, despite variation in its genus-four source curves.

## Limitations
Superspeciality is asserted over algebraic closures, not a uniform field-of-definition classification. No polarized isomorphism, endomorphism ring, explicit rational splitting map, or assertion about all genus-four cyclic trigonal curves is established. The computation does not certify historical first discovery, and a related characteristic-five Prym result might be known under a different moduli description. Independent assessment of priority and proof has not been performed.

## References
1. S. Baldwin, J. C. Eilbeck, J. Gibbons, Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654 (2006), https://arxiv.org/pdf/math/0612654.
2. M. Kudo, S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114 (2016), https://arxiv.org/pdf/1607.01114, especially Section 5.1.
3. H. Lange, A. Ortega, *The trigonal construction in the ramified case*, arXiv:1902.00251 (2019), https://arxiv.org/abs/1902.00251.
