# Parity and transverse quadratic strata in interior coordinate cuts of Hankel determinants

## Finding
Let \(K\) be an algebraically closed field of characteristic zero. For every integer \(n\ge3\), let \(H_n=(a_{i+j})_{0\le i,j<n}\) be the generic symmetric Hankel matrix, and define \(D_n=V(\det H_n)\subset\mathbb P^{2n-2}_K\). Fix an **interior** coefficient index \(1\le k\le 2n-3\), and let \(Y_{n,k}=D_n\cap V(a_k)\subset\mathbb P^{2n-3}_K\). Write \(T_{n,k}\) for the reduced subscheme defined by \(a_k=0\) and all \((n-1)\)-minors of \(H_n\), so it is the corank-at-least-two locus within the hyperplane section.

**Parity theorem (reduced support).** If \(k\) is odd, then \(\operatorname{Sing}(Y_{n,k})_{\mathrm{red}}=T_{n,k}\). If \(k=2j\) is even, then necessarily \(1\le j\le n-2\), and
\[
\operatorname{Sing}(Y_{n,2j})_{\mathrm{red}}=T_{n,2j}\cup L_j,\qquad L_j:=V(a_j,a_{j+1},\ldots,a_{j+n-1})\simeq\mathbb P^{n-2}.
\]
The generic point of \(L_j\) has Hankel matrix rank exactly \(n-1\); thus \(L_j\) is an additional irreducible component not contained in the corank-at-least-two locus. Generically transverse to \(L_j\), the hypersurface has a nondegenerate quadratic singularity in \(n-1\) variables. For every \(n\ge4\), all \(Y_{n,k}\) are integral and normal, whereas for \(n=3\) the even-index section is integral but nonnormal. The two odd-index cubic-surface sections at \(n=3\) have exactly two isolated singularities, with ADE types \(A_1\) and \(A_5\).

This is a classification of the **reduced singular support**, not a statement about the generally more complicated nonreduced Jacobian ideal.

## Assumptions and scope
Every statement is over algebraically closed characteristic-zero \(K\); the integer ranges are \(n\ge3\) and \(1\le k\le2n-3\). Matrices are indexed from zero and \(I_{n-1}(H_n)\) denotes the ideal of all \((n-1)\)-minors. The word “transverse” means a completed local hypersurface slice at the generic point of a smooth open subset of \(L_j\), after extending residue fields if necessary. There is no claim for endpoint cuts \(k=0\) or \(k=2n-2\), which are covered by other degeneration literature.

## Proof
**1. Exact rank-one adjugate test.** At a corank-one point of \(D_n\), symmetry implies \(\operatorname{adj}(H_n)=\lambda vv^{\mathsf T}\) for \(\lambda\ne0\) and a nonzero kernel vector \(v=(v_0,\ldots,v_{n-1})\). Hence
\[
\frac{\partial\det H_n}{\partial a_t}=\lambda\sum_{i+j=t}v_iv_j=\lambda[z^t]q(z)^2,\quad q(z)=\sum_{i=0}^{n-1}v_i z^i.
\]
The projective section \(Y_{n,k}\) is singular at this point exactly if derivatives with respect to all remaining coefficients \(a_t\), \(t\ne k\), vanish. In characteristic zero this holds exactly when \(q(z)^2\) is a nonzero monomial of degree \(k\). Since \(K[z]\) is a UFD, this requires \(k=2j\) and \(q(z)=c z^j\). Equivalently \(v=e_j\), so the entire \(j\)-th row of \(H_n\) vanishes, i.e. \(a_j=\cdots=a_{j+n-1}=0\). Conversely every corank-one point of this linear space is singular. At corank at least two the adjugate vanishes and all derivatives vanish. This proves the set-theoretic equality of both parities and, after taking reductions, the asserted equality of reduced subschemes.

**2. The extra linear stratum has the expected generic rank.** On \(L_j\), delete row and column \(j\). The remaining matrix \(B\) splits into two blocks on indices below and above \(j\), respectively. Each block is anti-triangular along the first surviving coefficient, and
\[
\det B=(-1)^{\frac{j(j-1)}2+\frac{(n-1-j)(n-2-j)}2}\,a_{j-1}^{j}a_{j+n}^{n-1-j}.
\]
The two indicated coefficients exist for each interior \(j\) and are algebraically independent on \(L_j\). Thus \(B\) is invertible on the nonempty dense open set \(a_{j-1}a_{j+n}\ne0\), proving \(\operatorname{rank} H_n=n-1\) there, so \(L_j\not\subset T_{n,2j}\). Because \(L_j\) is a projective linear space and the other singular points are precisely in \(T_{n,2j}\), it is an irreducible component.

**3. Transverse quadratic singularity.** In the open locus \(\det B\ne0\), let \(r\) be the off-diagonal part of row \(j\), consisting of exactly the \(n-1\) independent normal coordinates \(a_{j+i}\), \(i\ne j\). The Schur complement gives, identically on \(a_{2j}=0\),
\[
\det H_n=-\det(B)\, r^{\mathsf T}B^{-1}r.
\]
At \(r=0\) the normal Hessian is a nonzero scalar multiple of \(B^{-1}\), hence nonsingular. The characteristic-zero formal Morse lemma yields the nondegenerate quadratic transverse germ in \(n-1\) variables. When \(n=3\), this is a normal-crossing ordinary double *curve slice*, not a normal surface germ; for \(n\ge4\) it has codimension at least two in \(Y_{n,k}\).

**4. Integrality and normality.** Standard Hankel determinantal geometry identifies the projective corank-at-least-two locus \(V(I_{n-1}(H_n))\) as the \((n-3)\)-secant variety of a rational normal curve. It is integral of dimension \(2n-5\) and is not contained in a coordinate hyperplane (the rank-one point with every coefficient equal to \(1\) already lies off every coordinate hyperplane). Thus \(T_{n,k}\) has dimension \(2n-6\) whenever nonempty, while \(\dim Y_{n,k}=2n-4\). The determinant \(\det H_n\) is irreducible before taking a hyperplane section (standard catalecticant fact), so its restriction to any coordinate hyperplane is not the zero polynomial. Hence \(Y_{n,k}\) is a genuine projective hypersurface; for \(n\ge4\) every component of its singular set has codimension at least two, because \(\dim L_j=n-2\). By Serre's criterion the section is normal after reduction, since hypersurfaces are \(S_2\). More explicitly: a reducible or generically nonreduced projective hypersurface would have a singular locus of codimension at most one; our exact Jacobian calculation excludes this. Therefore \(Y_{n,k}\) is integral and normal for \(n\ge4\). For \(n=3\) and odd \(k\), the singularity locus is finite, giving the same conclusion. For \(n=3\) and \(k=2\), the equation is \(-a_0a_3^2-a_1^2a_4=0\), which is irreducible by Gauss's lemma (viewing it as a primitive degree-one polynomial in \(a_0\)) but singular along the divisor \(L_1\); hence it is integral and nonnormal.

**5. Sharp small-dimensional boundary.** When \(n=3\) and \(k=1\), the cubic surface in coordinates \([a_0:a_2:a_3:a_4]\) has equation
\[
F=a_0a_2a_4-a_0a_3^2-a_2^3.
\]
Its four first derivatives vanish exactly at \([1:0:0:0]\) and \([0:0:0:1]\). In the first affine chart, putting \(u=a_2\), \(v=a_3\), and \(w=a_4-a_2^2\) gives \(F=uw-v^2\), an \(A_1\) point. In the last chart, putting \(u=a_2-a_3^2\), \(v=a_3\), and \(w=a_0-u^2-3uv^2-3v^4\) gives \(F=uw-v^6\), an \(A_5\) point. The case \(k=3\) is obtained by reversing the coefficient indices.

## Verification
A standalone pure-Python/SymPy verifier accompanies this finding as `hankel_interior_verifier.py`. It checks the exact complementary-minor factorization for every \(3\le n\le8\) and every interior \(j\), the exact sum-of-convolutions coefficient identity for \(3\le n\le5\), and the cubic \(A_5\) coordinate transformation. Execute `python hankel_interior_verifier.py` (requires SymPy). It must terminate with `VERIFY_OK`. These finite and symbolic tests corroborate the closed-form proof above; they do not serve as a substitute for the unbounded quantifier argument.

## Relationship to prior work
Mostafazadehfard and Simis, *Homaloidal determinants* (arXiv:1407.8089v1, 2014), treat the generic Hankel determinant, its gradient ideal, and sub-Hankel terminal degenerations. Cunha, Mostafazadehfard, Ramos, and Simis, *Coordinate sections of generic Hankel matrices* (arXiv:2005.02909v1, 2020), analyze the **terminal consecutive-zero** degeneration \(H_n[r]\); their Theorem 3.9 classifies minimal primes of the gradient ideal for \(1\le r\le n-3\). The present claim deliberately excludes endpoint coefficient cuts and treats all isolated **interior** coefficient cuts, where a parity-dependent rank-one singular stratum appears. The known rank-minor locus and general adjugate derivative formula are not presented as novel. The contribution is the complete interior-cut parity classification, explicit extra linear strata and transverse germs, and the normality transition with an \(A_1+A_5\) cubic boundary. Standard general theory of linear determinantal sections may implicitly imply parts of the analysis; that possibility remains a qualification of originality.

## Limitations
This is only a reduced support classification, not a scheme-theoretic primary decomposition of the Jacobian ideal. No assertion is made for positive characteristic, endpoint cuts, nongeneric transverse strata, or the singularity types at intersections \(L_j\cap T_{n,2j}\). Rank-locus hyperplane sections may themselves have several irreducible components: none of their component counts are asserted. General ambient linear-section theorems and an inaccessible-to-full-inspection 2024 book chapter remain possible sources of implicit broader coverage. Independent mathematical audit remains outstanding.

## References
1. M. Mostafazadehfard and A. Simis, *Homaloidal determinants*, first public arXiv version 2014-07-30, arXiv:1407.8089v1. https://arxiv.org/abs/1407.8089
2. R. Cunha, M. Mostafazadehfard, Z. Ramos and A. Simis, *Coordinate sections of generic Hankel matrices*, arXiv:2005.02909v1 (2020), especially §§1.3, 2.1 and Theorem 3.9. https://arxiv.org/abs/2005.02909
3. D. Eisenbud, *Linear Sections of Determinantal Varieties*, Amer. J. Math. 110 (1988), 541–575, doi:10.2307/2374622 (general background; complete primary text not inspected).
