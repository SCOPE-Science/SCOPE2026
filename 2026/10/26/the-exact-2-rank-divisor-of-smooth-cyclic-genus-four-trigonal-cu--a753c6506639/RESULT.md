# The exact 2-rank divisor of smooth cyclic genus-four trigonal curves

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). Write
\[
f(x)=x^5+a_4x^4+a_3x^3+a_2x^2+a_1x+a_0
\]
with coefficients in \(k\) and nonzero discriminant. On the smooth projective curve \(C_f\) whose affine model is \(y^3=f(x)\), use the ordered differential basis
\[
(\omega_0,\omega_1,\omega_2,\omega_3)
=\left(\frac{dx}{y},\frac{dx}{y^2},\frac{x\,dx}{y^2},\frac{x^2\,dx}{y^2}\right).
\]
Its characteristic-two Cartier operator satisfies the identities
\[
\begin{aligned}
\mathcal C(\omega_0)&=\sqrt{a_1}\,\omega_1+\sqrt{a_3}\,\omega_2+\omega_3,\\
\mathcal C(\omega_1)&=0,\\
\mathcal C(\omega_2)&=\omega_0,\\
\mathcal C(\omega_3)&=0.
\end{aligned}
\]
Therefore \(a(C_f)=2\) for every smooth member and
\[
f_2(C_f)=\begin{cases}0,&a_3=0,\\2,&a_3\ne0,\end{cases}
\]
where \(f_2\) is the \(2\)-rank of the Jacobian. On the marked coefficient parameter space \(U=\operatorname{Spec}k[a_0,\ldots,a_4,1/\Delta(f)]\), the rank-zero locus is the reduced smooth nonempty divisor \(U\cap V(a_3)\). Along this divisor \(\mathcal C^3=0\) but \(\mathcal C^2\ne0\). No intermediate \(2\)-rank occurs.

## Assumptions and scope
The result concerns the entire five-coefficient family of **monic, squarefree quintics** over algebraically closed fields of characteristic two, with its distinguished degree-three morphism to the \(x\)-line. It does not classify unmarked isomorphism classes, Newton polygons, or arbitrary non-cyclic trigonal curves. The \(2\)-rank means the dimension over \(\mathbb F_2\) of \(\operatorname{Jac}(C_f)[2](k)\); the \(a\)-number is \(\dim_k\ker\mathcal C\).

## Proof
**Genus and basis.** Because \(f\) is squarefree, the degree-three map \(C_f\to\mathbb P^1\) is tame and totally ramified at five finite zeros of \(f\) and at infinity. Riemann--Hurwitz gives \(2g-2=-6+6\cdot2=6\), hence \(g=4\). At the unique point at infinity, \(\operatorname{ord}(x)=-3\), \(\operatorname{ord}(y)=-5\), and \(\operatorname{ord}(dx)=-4\). Thus the orders of the displayed forms there are \(1,6,3,0\), all nonnegative. At any branch zero of \(f\), a uniformizer \(y\) has \(\operatorname{ord}(dx)=2\) because the cover is tamely totally ramified; the displayed forms are regular. They therefore form four linearly independent regular differentials, and hence a basis.

**Exact Cartier action.** Let \(\mathcal C\) denote the characteristic-two Cartier operator, characterized by \(\mathcal C(h^2\eta)=h\mathcal C(\eta)\), \(\mathcal C(x^{2j}\,dx)=0\), and \(\mathcal C(x^{2j+1}\,dx)=x^j\,dx\). Because \(k\) is perfect, put
\[
A=\sqrt{a_0}+\sqrt{a_2}\,x+\sqrt{a_4}\,x^2,\qquad
B=\sqrt{a_1}+\sqrt{a_3}\,x+x^2.
\]
The **polynomial identity** \(f=A^2+xB^2\) holds. As \(\mathcal C(f\,dx)=B\,dx\) and \(y^3=f\),
\[
\mathcal C\left(\frac{dx}{y}\right)
=\mathcal C\left(\left(\frac y f\right)^2 f\,dx\right)
=\frac y f B\,dx=\frac{B\,dx}{y^2}.
\]
For \(j=0,1,2\), \(x^j\,dx/y^2=(y^2/f)^2x^j\,dx\). Applying the same Cartier rules gives \(\mathcal C(dx/y^2)=0\), \(\mathcal C(x\,dx/y^2)=dx/y\), and \(\mathcal C(x^2\,dx/y^2)=0\). This establishes the four asserted images *uniformly in every coefficient*.

**Stable rank and divisor.** Let \(v=\sqrt{a_1}\,\omega_1+\sqrt{a_3}\,\omega_2+\omega_3\). Because the \(\omega_3\) coefficient of \(v\) equals one, \(v\) and \(\omega_0\) are independent, and \(\operatorname{im}\mathcal C=\langle v,\omega_0\rangle\) has dimension two. Moreover \(\mathcal C(v)=a_3^{1/4}\omega_0\). If \(a_3\ne0\), Cartier restricts to a semilinear bijection on this two-dimensional image, so its stable image has dimension two. If \(a_3=0\), then \(\mathcal C(v)=0\), \(\mathcal C^2(\omega_2)=v\ne0\), and \(\mathcal C^3=0\) on the whole basis. The stable image is zero. The \(2\)-rank equals the stable Cartier rank; the \(a\)-number is \(4-\operatorname{rank}\mathcal C=2\).

The parameter space \(U\) is an open subscheme of affine five-space. Its intersection with the linear hyperplane \(a_3=0\) is reduced and smooth of codimension one. It is nonempty because \(x^5+x+1\) is squarefree; the complementary locus is nonempty because \(x^5+x^3+x+1\) is squarefree. No claim of irreducibility of their images in the coarse moduli space is needed.

## Verification
Run \(`python verify.py`\) with Python 3 and SymPy installed. The script checks the universal polynomial decomposition with independent square-root coefficient indeterminates, the odd-exponent Cartier extraction, the squarefreeness of two witnesses, and all \(\mathbb F_{2^m}\)-point counts for \(1\le m\le8\) for both witnesses. From Newton identities it recovers zeta numerators
\[
\begin{aligned}
L_{x^5+x+1}(T)&=1+2T^2+6T^4+8T^6+16T^8,\\
L_{x^5+x^3+x+1}(T)&=1+3T^2+4T^4+12T^6+16T^8.
\end{aligned}
\]
Their reductions modulo \(2\) have degrees zero and two respectively, consistent with the theorem. The finite computations independently check examples; they are not substitutes for the uniform proof.

## Relationship to prior work
Baldwin, Eilbeck, Gibbons and Ônishi (first publicly available 2006) study this same cyclic genus-four quintic family and list a differential basis for its complex theory; the contribution here concerns a characteristic-two Cartier and \(2\)-rank stratification. Dragutinović studies characteristic-two genus-four Ekedahl--Oort strata and gives a broad Hasse--Witt framework for trigonal curves, but its inspected results do not state this marked cyclic-family divisor. Sohn (2025) addresses \(a\)-numbers of superelliptic genus-four curves via Cartier--Manin matrices: that is the closest later potential overlap. Its abstract is accessible, but the full text could not be examined; the possibility that a displayed matrix implies this particular \(2\)-rank formula remains an originality risk. The existing general Cartier formulas and the known existence of \(2\)-rank-zero genus-four curves are not attributed as new.

## Limitations
The parameter criterion concerns a marked coefficient family, not an assertion that its rank-zero image is a divisor in every moduli compactification. The result does not determine Newton polygons or Ekedahl--Oort types in full. A later calculation of the complete Cartier matrix for this identical model could imply the rank criterion without using its present wording. The closed-form theorem is verified algebraically; finite-field counts cover only the two stated witnesses.

## References
1. S. Baldwin, J. C. Eilbeck, J. Gibbons, Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654 (first posted 2006-12-21), especially Section 2.
2. D. Dragutinović, *Supersingular curves of genus four in characteristic two*, arXiv:2301.12897 (2023), especially Section 5.
3. G. Sohn, *The \(a\)-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics 7 (2025), 59--66, DOI 10.23091/japm.2025.059 (abstract consulted; full text inaccessible).
