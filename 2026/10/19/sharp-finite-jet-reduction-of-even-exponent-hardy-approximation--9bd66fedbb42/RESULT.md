# Sharp finite-jet reduction of even-exponent Hardy approximation for inner functions

## Finding
Let \(m\geq 1\) and \(n\geq 0\) be integers, and set \(L=(m-1)n\). For an inner function \(f\) on the unit disk define, for each complex polynomial \(q\) of degree at most \(n\),
\[
\mathcal F_f(q)=\lVert 1-qf\rVert_{H^{2m}}^{2m}.
\]
If two inner functions \(f,g\) have matching Taylor coefficients through degree \(L\), then
\[
\boxed{\mathcal F_f(q)=\mathcal F_g(q)\quad\text{for every }\deg q\leq n.}
\]
Consequently their unique degree-at-most-\(n\) optimal polynomial approximants to their reciprocals, and the corresponding optimal errors, are identical. Moreover **every** inner \(f\) has a finite Blaschke replacement \(B\) of degree at most \(L+1\) with this exact equality of complete variational objectives. Both the jet cutoff \(L\) for the complete objective and the universal Blaschke degree bound \(L+1\) are best possible.

Write \(\langle u,v\rangle=\int_{\mathbb T}u\overline v\,dm\), linear in its first argument. The finite-coefficient formula is
\[
\mathcal F_f(q)
=\sum_{j=0}^{m}\binom mj^2\lVert q^j\rVert_2^2
+2\operatorname{Re}\sum_{0\leq k<j\leq m}
(-1)^{j+k}\binom mj\binom mk\langle q^j f^{j-k},q^k\rangle.
\]
Every cross inner product in this formula reads only Taylor coefficients of \(f\) through degree \(kn\leq L\). It is therefore an explicit real polynomial in the real and imaginary parts of the coefficients of \(q\) and the first \(L+1\) Taylor coefficients of \(f\).

## Assumptions and scope
The norm uses normalized Haar probability measure on the circle, \(dm(e^{it})=dt/(2\pi)\). An inner function is analytic on the open unit disk, bounded by one, and has boundary values of modulus one almost everywhere. The theorem covers singular inner functions and infinite Blaschke products as well as finite ones; no restriction on \(f(0)\) is imposed. The polynomial degree is an upper bound, so constant or zero optimal polynomials are permitted. The statement is for finite even exponents \(2m\), not arbitrary real Hardy exponents.

## Proof
**1. Finite moment identity.** On the boundary expand
\[
|1-qf|^{2m}=(1-qf)^m(1-\overline q\,\overline f)^m.
\]
For equal binomial indices \(j=k\), the factor \(f^j\overline f^{\,j}\) equals one almost everywhere. For \(j>k\), this factor becomes \(f^{j-k}\); pairing these terms with their conjugates gives the displayed formula. For \(j>k\), the analytic polynomial \(q^k\) has degree at most \(kn\), so
\[
\langle q^j f^{j-k},q^k\rangle
=\sum_{r=0}^{kn}[z^r](q^j f^{j-k})\,\overline{[z^r]q^k}.
\]
The coefficients of a power of a holomorphic function through degree \(kn\) depend only on its coefficients through that degree. Thus the whole expression depends only on the stated jet.

**2. Unique minimizing polynomial.** Multiplication by an inner function is an isometry on \(H^{2m}\), and \(\|1-qf\|_{2m}\geq\|q\|_{2m}-1\). Hence the objective is continuous and coercive on the finite-dimensional polynomial space, and it attains its minimum. The function \(|z|^{2m}\) is strictly convex on \(\mathbb C\) as a real vector space, and distinct polynomials give distinct residuals almost everywhere because \(|f|=1\) almost everywhere. The objective is strictly convex, so the minimizer is unique. Identical objectives therefore have the same unique minimizer and minimum.

**3. Constructive finite Blaschke reduction.** Start with the Schur iterate \(s_0=f\). For \(r=0,1,\ldots,L\), set \(\gamma_r=s_r(0)\), and when \(|\gamma_r|<1\) define
\[
s_{r+1}(z)=\frac{s_r(z)-\gamma_r}{z(1-\overline{\gamma_r}s_r(z))},\qquad
s_r(z)=\frac{\gamma_r+zs_{r+1}(z)}{1+\overline{\gamma_r}zs_{r+1}(z)}.
\]
Each forward iterate is inner: the disk automorphism that sends \(\gamma_r\) to zero preserves the boundary modulus and the Schwarz lemma allows division by \(z\). If some \(|\gamma_r|=1\), the iterate is a unimodular constant by the maximum modulus principle, so the original \(f\) is itself a finite Blaschke product of degree at most \(r\leq L\). Otherwise replace \(s_{L+1}\) by the constant inner function \(1\), and use the inverse recurrences to construct \(B\). Each inverse step is multiplication by \(z\) followed by a disk automorphism, so it increases finite Blaschke degree by at most one. This gives \(\deg B\leq L+1\). The difference between the inverse-step outputs from two inputs is \(z\) times their difference multiplied by a holomorphic function near zero, as follows by subtraction of the fractions. Thus \(f-B=O(z^{L+1})\), so \(B\) and \(f\) share the required jet. Step 1 proves equality of objectives. The Schur interpolation step is classical.

**4. Optimality of the jet cutoff.** Suppose \(m\geq2\) and \(n\geq1\), so \(L\geq1\). Take \(f_\pm(z)=\pm z^L\) and \(q(z)=1+z^n\). For \(j>k\), a cross term can be nonzero only when \((j-k)L\leq kn\), which forces \((j,k)=(m,m-1)\); the constant coefficient of \(q^m\) and the leading coefficient of \(q^{m-1}\) are both one. The surviving cross term changes sign, and
\[
\mathcal F_{f_+}(1+z^n)-\mathcal F_{f_-}(1+z^n)=-4m\neq0.
\]
Thus matching through \(L-1\) cannot suffice. When \(L=0\), even the constant Taylor coefficient is necessary: the constant inner functions \(1\) and \(-1\) have different objectives at \(q=1\).

**5. Optimality of the objective-equivalent Blaschke degree bound.** In fact equality of the complete objectives implies equality of the jet. Write \(q(z)=\sum_{i=0}^n a_i z^i\). In the boundary expansion before taking real parts, the only term of bidegree \((m,m-1)\) in \((a,\bar a)\) is
\[
-m\langle q^m f,q^{m-1}\rangle.
\]
If \(b_0,\ldots,b_n\) are nonnegative integers with \(\sum_i b_i=m-1\), its coefficient of \(a_0^m\prod_{i=0}^n\bar a_i^{b_i}\) is
\[
-m\frac{(m-1)!}{\prod_i b_i!}\,[z^{\sum_i i b_i}]f(z).
\]
Indeed, the holomorphic monomial comes from taking \(a_0\) in all \(m\) factors of \(q^m\); the antiholomorphic factors select the one frequency \(\sum_i i b_i\) in \(q^{m-1}\). Equality on all complex \(a\) implies equality of these coefficients, since the change of formal variables between \((a,\bar a)\) and the real and imaginary coordinate variables is invertible over \(\mathbb C\). Every \(r\in\{0,\ldots,L\}\) is a sum of \(m-1\) integers from \(0\) to \(n\); repeated summands give the multiplicities \(b_i\). If \(m=1\), the empty sum reads the constant coefficient, and if \(n=0\), only zero is read. Hence the objective determines the full required jet in all cases.

Now let \(f(z)=z^{L+1}\). Every objective-equivalent finite Blaschke product must have all coefficients through degree \(L\) zero by the converse just proved. It has a zero of multiplicity at least \(L+1\) at the origin, and therefore degree at least \(L+1\). This lower bound is for objective equivalence, not merely for replacements required in advance to match the jet.

## Verification
The frozen support file `verify.py` computes the finite-coefficient moment formula and compares it with circle quadrature, constructs truncated Schur replacements, and compares floating-point objective differences with the exact formula \(-4m\). The frozen `verification_output.txt` contains the reported finite checks. These checks neither establish the all-parameter theorem nor test the coefficient-extraction converse; those are analytic arguments above.

For a concrete nonidentical pair at \((m,n)=(3,2)\), let \(b_a(z)=(z-a)/(1-az)\), with real \(a\in(0,1)\), and put
\[
f(z)=b_{1/3}(z)b_{1/2}(z^5),\qquad g(z)=b_{1/3}(z)b_{1/2}(z^6).
\]
They have different zero sets and share their Taylor coefficients through degree four, so their full sextic degree-two objectives agree.

## Relationship to prior work
Classical Schur interpolation treats prescribed finite coefficient jets; see Bolotnikov (2009). Bénéteau et al. (2017) treat the constant optimal approximants for inner functions in the Hilbert-space case \(H^2\). Centner (2021), Centner, Cheng, and Felder (2023), and Cheng and Felder (2023) develop \(H^p\) and \(L^p\) optimal polynomial approximation, including optimizer and error properties. The claim here concerns the all-degree, all-even-exponent *complete objective*, with its exact jet cutoff and sharp universal degree for objective-equivalent Blaschke replacement. The Schur construction, the Hilbert-space case, and low-degree optimizer-only results are not asserted as new.

## Limitations
The exact cutoff is sharp for the whole objective, not necessarily for determining only the minimizing polynomial or minimum. For example, if \(f(0)=0\), the residual has constant coefficient one for all \(q\), so its norm is at least one and the unique minimizing polynomial is zero. No analogue for non-even exponents, non-inner generators, or vector-valued inner functions is asserted. The theorem yields a finite variational problem without generally solving it in closed form. Literature comparisons cannot certify historical priority.

## References
1. R. Centner, *Optimal Polynomial Approximants in \(L^p\)*, arXiv:2112.14002, https://arxiv.org/abs/2112.14002.
2. R. Centner, R. Cheng, C. Felder, *Optimal Polynomial Approximants in \(H^p\)*, arXiv:2305.16068, https://arxiv.org/abs/2305.16068.
3. R. Cheng, C. Felder, *More properties of optimal polynomial approximants in Hardy spaces*, arXiv:2310.16010, https://arxiv.org/abs/2310.16010.
4. C. Bénéteau, M. Fleeman, D. Khavinson, D. Seco, A. Sola, *Remarks on inner functions and optimal approximants*, arXiv:1707.06166, https://arxiv.org/abs/1707.06166.
5. V. Bolotnikov, *An algorithm for finding low degree rational solutions to the Schur coefficient problem*, arXiv:0912.5034, https://arxiv.org/abs/0912.5034.
6. C. Felder, T. Le, *Analogues of finite Blaschke products as inner functions*, arXiv:2105.01766, https://arxiv.org/abs/2105.01766.
