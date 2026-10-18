# A polarized \(p\)-isogeny and supersingular but non-superspecial Jacobians in a double Artin--Schreier family

## Finding
Let \(k\) be algebraically closed of odd prime characteristic \(p\), let \(a\in k\setminus\mathbb F_p\) and \(b\in k^\times\). Write \(C_{a,b}\) for the smooth projective model of
\[
\big((x^p-x)-a(y^p-y)\big)^2=b^2(y^p-y).
\]
Put \(D_p:\ v^2=u^p-u\), a smooth curve of genus \(h=(p-1)/2\), and \(g=(p^2-1)/2\). There are \(p+1\) degree-\(p\) quotient maps \(\pi_H:C_{a,b}\longrightarrow D_H\cong D_p\), indexed by the order-\(p\) subgroups \(H\) of \(G\cong(\mathbb Z/p\mathbb Z)^2\). The canonical sum-of-pullbacks homomorphism
\[
\Phi=\sum_H\pi_H^*:\quad A:=\prod_H\operatorname{Jac}(D_H)\longrightarrow\operatorname{Jac}(C_{a,b})
\]
satisfies the *polarized identity*
\[
\Phi^\vee\Phi=[p]_A,\qquad
\Phi^*\lambda_{\operatorname{Jac}(C_{a,b})}=p\lambda_A,
\]
where duality uses the canonical principal polarizations and \(\lambda_A\) is their product. In particular \(\Phi\) is an isogeny of **exact degree** \(p^g\) with maximal isotropic finite subgroup-scheme kernel of order \(p^g\) in \(A[p]\). Thus
\[
\operatorname{Jac}(C_{a,b})\ \sim_k\ \operatorname{Jac}(D_p)^{p+1}.
\]
All the \(\operatorname{Jac}(D_p)\) are superspecial, so \(\operatorname{Jac}(C_{a,b})\) is geometrically **supersingular**: all \(2g\) Newton slopes are \(1/2\). Yet \(\operatorname{Jac}(C_{a,b})\) is **not superspecial**, because \(g>p(p-1)/2\), the Ekedahl bound for curves with zero Cartier operator. These assertions hold for every admissible parameter pair, including \(p=3\).

## Assumptions and scope
The ground field is algebraically closed, and \(p\ge3\) is prime. The coefficients satisfy \(a\notin\mathbb F_p\), \(b\ne0\). The Jacobian and polarizations are those of the smooth projective normalization, not of its potentially singular affine model. Isogeny degrees and kernels are interpreted scheme-theoretically in characteristic \(p\); there is no separability assertion. Supersingular means all rational Newton slopes equal \(1/2\); superspecial means an unpolarized product of supersingular elliptic curves, equivalently zero Cartier operator for a Jacobian of a smooth curve.

## Proof
**1. The elementary abelian cover and its genus.** Define \(t=((x^p-x)-a(y^p-y))/b\). Then the function field has the equivalent presentation
\[
y^p-y=t^2,\qquad x^p-x=a t^2+b t.
\]
For every nonzero \((c,d)\in\mathbb F_p^2\), the Artin--Schreier class of \((c+ad)t^2+dbt\) in \(k(t)/(F-1)k(t)\) is nonzero: the quadratic leading coefficient \(c+ad\) is nonzero since \(a\notin\mathbb F_p\), and a polynomial of reduced pole order \(2\), prime to \(p\), cannot be an Artin--Schreier coboundary. Thus the two classes are independent over \(\mathbb F_p\), and their compositum is a connected \(G\)-Galois cover of \(\mathbb P^1_t\) of degree \(p^2\). Every one-dimensional character has upper break \(2\) at infinity and no other ramification. Hence the lower ramification groups at the unique point above infinity have \(G_0=G_1=G_2=G\), with \(G_3=1\). The different exponent is \(3(p^2-1)\), and Riemann--Hurwitz gives
\[
2g(C_{a,b})-2=-2p^2+3(p^2-1)=p^2-3,
\]
so \(g(C_{a,b})=(p^2-1)/2=g\).

**2. The \(p+1\) quotient curves.** Nonzero lines \([c:d]\in\mathbb P^1(\mathbb F_p)\) index the intermediate degree-\(p\) quotient curves \(D_{[c:d]}\), with equation
\[
w^p-w=(c+ad)t^2+dbt.
\]
Since \(c+ad\ne0\), complete the square in \(t\), scale its coordinate by a square root, and translate \(w\) by a constant root of an Artin--Schreier equation. Over algebraically closed \(k\) this changes the model to \(w^p-w=t^2\). Interchanging the coordinate names gives \(D_p:v^2=u^p-u\). Its genus is \(h=(p-1)/2\), and \((p+1)h=g\).

**3. Exact polarized degree.** Let \(\pi_H:C_{a,b}\to D_H=C_{a,b}/H\) be the finite separable degree-\(p\) quotient map. For each \(H\), the pushforward (norm) \(\pi_{H*}\) is the dual of pullback \(\pi_H^*\) under the canonical principal polarizations. On \(\operatorname{Jac}(D_H)\), \(\pi_{H*}\pi_H^*=[p]\). For distinct order-\(p\) groups \(H\ne K\), they generate \(G\) and intersect trivially. The correspondence between \(D_H\) and \(D_K\) coming from \(C_{a,b}\) is the full fiber product over \(C_{a,b}/G=\mathbb P^1_t\) (on generic fibers, each pair of quotient points has exactly one preimage). Thus \(\pi_{H*}\pi_K^*\) factors through the Jacobian of \(\mathbb P^1\), hence is the zero homomorphism. This gives the block-matrix identity
\[
\Phi^\vee\Phi=(\pi_{H*}\pi_K^*)_{H,K}=[p]_A.
\]
Since \(\dim A=(p+1)h=g=\dim\operatorname{Jac}(C_{a,b})\), the identity forces \(\Phi\) to be an isogeny. Comparing isogeny degrees yields \((\deg\Phi)^2=\deg[p]_A=p^{2g}\), so \(\deg\Phi=p^g\). The polarization identity \(\Phi^*\lambda_C=p\lambda_A\) follows by definition of the Rosati dual. Since this isogeny pulls back a principal polarization to the \(p\)-multiple of a principal polarization, its kernel is a maximal isotropic finite flat subgroup scheme of \(A[p]\), of order \(p^g\).

**4. Newton and Ekedahl--Oort consequences.** Set \(h=(p-1)/2\). The expansion \((u^p-u)^h\) has nonzero monomial terms only at exponents \(h+(p-1)j\) for \(0\le j\le h\). These exponents reduce modulo \(p\) to the residues \(h,h-1,\ldots,0\). In the standard hyperelliptic Cartier--Manin matrix, the \((i,j)\)-entry is the coefficient at exponent \(pi-j\), with \(1\le i,j\le h\), whose residue lies in \(\{h+1,\ldots,p-1\}\). Hence the entire Cartier operator on \(H^0(D_p,\Omega^1)\) vanishes. Therefore \(\operatorname{Jac}(D_p)\) is superspecial. Supersingular Newton polygons are invariant under isogeny, so the product isogeny of Step 3 forces all \(2g\) slopes of \(\operatorname{Jac}(C_{a,b})\) to equal \(1/2\). On the other hand, Ekedahl's bound for a smooth superspecial curve is \(g\le p(p-1)/2\), whereas \(g=(p^2-1)/2>p(p-1)/2\). Thus the Jacobian of \(C_{a,b}\) cannot be superspecial. \(\square\)

## Verification
Run the standalone standard-library program `verify.py` from this package with `python verify.py`. It checks, in exact modular arithmetic, the Cartier--Manin vanishing for \(p=3,5,7,11,13,17,19,23,29\), and verifies the pairwise direct-sum combinatorics of all order-\(p\) subgroup pairs. For \(p=3,5,7,11,13\), it constructs \(\mathbb F_{p^2}\), counts points of a representative member of the cover and each intermediate quotient, and verifies the predicted additive trace identity. Expected output starts `VERIFY_OK`. The argument above proves every prime and every allowed parameter; the bounded tests are corroborative rather than an infinite certificate.

## Relationship to prior work
Borges--Niemann--Zini, Example 3.9 of arXiv:2602.13925v1, already constructs the same one-nonrational-point conic family, identifies its genus and zero \(p\)-rank, and experimentally suggests minimality over an extension while explicitly leaving that claim for future work. Their equations (2.4)--(2.5) invoke idempotent relations and Kani--Rosen to sum genera and \(p\)-ranks. Arakelian--Kian, arXiv:2608.13768v1, studies the corresponding prime-square automorphism family in its geometric classification. Kazemifard--Tafazolian, arXiv:2609.33912v1, applies general elementary-abelian Jacobian factorization to a different Ree-type family, demonstrating that the decomposition technique itself is prior art. The present claim is not a new construction, genus formula, \(p\)-rank computation, or abstract isogeny principle: it is the complete identification of **all** \(p+1\) factors with one superspecial hyperelliptic Jacobian, together with an explicit canonical polarized \(p\)-isogeny of **exact degree**, its kernel structure, and the uniform supersingular/non-superspecial dichotomy for this family.

## Limitations
This is an isogeny-level result, not an isomorphism of principally polarized abelian varieties. It does not compute the complete Ekedahl--Oort type, the Cartier rank of \(C_{a,b}\), or the internal structure of its isotropic finite group-scheme kernel. The decomposition and superspeciality follow from recognizable general techniques; an equivalent implication may be latent in earlier literature. The 2026 originating articles and general Kani--Rosen identities create a concrete residual priority risk, which is not resolved by unsuccessful title or database searches. No independent mathematical audit or complete historical-priority certification has been performed.

## References
1. H. Borges, J. Niemann, G. Zini, *Double Artin--Schreier extensions of rational function fields with many lifted automorphisms*, arXiv:2602.13925v1, 2026, especially Section 2 and Example 3.9.
2. N. Arakelian, D. Kian, *Algebraic curves admitting automorphism groups of large prime square order*, arXiv:2608.13768v1, 2026.
3. A. Kazemifard, S. Tafazolian, *On the generalized Ree curve*, arXiv:2609.33912v1, 2026, especially Theorem 1.2 and Section 2.
4. E. Kani, M. Rosen, *Idempotent relations and factors of Jacobians*, Math. Ann. 284 (1989), 307--327.
5. Z. Zhou, *A bound on the genus of a curve with Cartier operator of small rank*, Rend. Circ. Mat. Palermo (2019), DOI:10.1007/s12215-018-0379-1, recalling Ekedahl's superspecial genus bound.
