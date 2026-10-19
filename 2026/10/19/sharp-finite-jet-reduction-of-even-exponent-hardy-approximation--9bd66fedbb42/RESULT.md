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

More explicitly, write \(q^{[j]}=q^j\) and let \(\langle u,v\rangle=\int_{\mathbb T}u\overline v\,dm\), linear in its first argument. The finite-coefficient formula is
\[
\mathcal F_f(q)
=\sum_{j=0}^{m}\binom mj^2\lVert q^j\rVert_2^2
+2\operatorname{Re}\sum_{0\leq k<j\leq m}
(-1)^{j+k}\binom mj\binom mk\langle q^j f^{j-k},q^k\rangle.
\]
Every cross inner product in this formula reads only Taylor coefficients of \(f\) through degree \(kn\leq L\). It is therefore an explicit real polynomial in the coefficients of \(q\) and the first \(L+1\) Taylor coefficients of \(f\).

## Assumptions and scope
The norm uses normalized Haar probability measure on the circle, \(dm(e^{it})=dt/(2\pi)\). An inner function is analytic on the open unit disk, bounded by one, and has boundary values of modulus one almost everywhere. The theorem covers singular inner functions and infinite Blaschke products as well as finite ones; no restriction on \(f(0)\) is imposed. The polynomial degree is an upper bound, so constant or zero optimal polynomials are permitted. The statement is for finite even exponents \(2m\), not arbitrary real Hardy exponents.

## Proof
**1. Finite moment identity.** On the boundary, use \(\overline f=f^{-1}\) almost everywhere. Expand
\[
|1-qf|^{2m}=(1-qf)^m(1-\overline q\,\overline f)^m.
\]
For the terms with equal binomial indices \(j=k\), the boundary factor \(f^j\overline f^{\,j}\) equals one, giving \(\binom mj^2\|q^j\|_2^2\). Pair the terms with \(j>k\) with their conjugates. This produces exactly the displayed formula. For \(j>k\), the analytic polynomial \(q^k\) has degree at most \(kn\). Therefore
\[
\langle q^j f^{j-k},q^k\rangle
=\sum_{r=0}^{kn}[z^r](q^j f^{j-k})\,\overline{[z^r]q^k}.
\]
Because the first \(kn+1\) coefficients of a power of a holomorphic function depend only on the first \(kn+1\) coefficients of that function, the entire expression depends only on \(f_0,\ldots,f_L\), where \(f_r=[z^r]f\). Equality of these jets for two inner functions therefore forces equality of objectives for every admissible polynomial.

**2. Unique minimizing polynomial.** For any nonzero inner \(f\), multiplication by \(f\) is an isometry in \(H^{2m}\). The objective is coercive on the finite-dimensional polynomial coefficient space, since
\[
\|1-qf\|_{2m}\geq\|q\|_{2m}-1.
\]
Strict convexity of \(L^{2m}\), together with injectivity of multiplication by \(f\), makes the minimizing polynomial unique. Identical objectives therefore have the same unique minimizer and minimum.

**3. Constructive finite Blaschke reduction.** Start with \(f_0=f\). For \(r=0,1,\ldots,L\), set \(\gamma_r=f_r(0)\), where here \(f_r\) denotes the \(r\)-th Schur iterate, and when \(|\gamma_r|<1\) define
\[
f_{r+1}(z)=\frac{f_r(z)-\gamma_r}{z(1-\overline{\gamma_r}f_r(z))},\qquad
f_r(z)=\frac{\gamma_r+zf_{r+1}(z)}{1+\overline{\gamma_r}zf_{r+1}(z)}.
\]
Each iterate is inner. If some \(|\gamma_r|=1\), the maximum-modulus principle makes that iterate a unimodular constant and the original \(f\) itself a finite Blaschke product of degree at most \(r\leq L\). Otherwise replace the final Schur iterate \(f_{L+1}\) by the constant inner function \(1\), and use the inverse recurrences to obtain \(B\). Every inverse step increases finite Blaschke degree by at most one; hence \(\deg B\leq L+1\). Each step inserts a factor of \(z\) into the dependence on the remaining iterate. Consequently \(f-B=O(z^{L+1})\), so \(B\) and \(f\) share exactly the jet needed in step 1, proving the objective and optimizer reduction. The Schur interpolation step itself is classical; the claim is its precise coupling to the even-Hardy variational objective.

**4. Optimality of the jet cutoff.** Suppose \(m\geq2\) and \(n\geq1\), so \(L\geq1\). The inner functions \(f_+(z)=z^L\) and \(f_-(z)=-z^L\) agree in all coefficients of degrees less than \(L\). Take \(q(z)=1+z^n\). In step 1, every cross term involving a positive power of \(f_\pm\) vanishes except the pair of indices \((j,k)=(m,m-1)\): this is because \((j-k)L\leq kn\) can then hold only in that pair, and its relevant Fourier coefficient equals one. The two signs make this surviving term opposite. Directly,
\[
\mathcal F_{f_+}(1+z^n)-\mathcal F_{f_-}(1+z^n)=-4m\neq0.
\]
Thus replacing cutoff \(L\) by \(L-1\) cannot preserve the full objective universally. For \(L=0\), even the constant Taylor coefficient is necessary, as witnessed by the constant inner functions \(1\) and \(-1\) evaluated at \(q=1\).

**5. Optimality of the Blaschke degree bound.** The inner function \(f(z)=z^{L+1}\) has vanishing Taylor coefficients at degrees \(0,1,\ldots,L\). Any finite Blaschke product matching that jet must have a zero of multiplicity at least \(L+1\) at the origin, and therefore degree at least \(L+1\). The universal bound from step 3 is sharp.

## Verification
The accompanying standalone standard-library Python program `verify.py` computes the finite-coefficient moment identity independently of circle quadrature and constructs the Schur finite-Blaschke replacement from truncated jets. It compares two different inner functions with matching jets and a Schur-generated replacement for \((m,n)=(2,1),(3,2),(4,1)\), checking numerical circular integrals against the algebraic formula. It also checks exact integer objective differences \(-4m\) at \((2,1),(3,2),(4,1),(5,3)\). The reproduced checks are in `verification_output.txt`; all pass. These finite tests are not used as substitutes for the analytic proof or for exhaustive verification over arbitrary \(m,n\).

For a concrete nonidentical pair at \((m,n)=(3,2)\), let \(b_a(z)=(z-a)/(1-az)\), with real \(a\in(0,1)\), and put
\[
f(z)=b_{1/3}(z)b_{1/2}(z^5),\qquad g(z)=b_{1/3}(z)b_{1/2}(z^6).
\]
The two functions have different zero sets, yet share their Taylor coefficients through degree four and hence the entire sextic degree-two approximation objective.

## Relationship to prior work
Classical Schur interpolation produces bounded analytic functions, including finite Blaschke products, with prescribed finite coefficient jets; see Bolotnikov (2009). Bénéteau et al. (2017) establish that classical \(H^2\) optimal approximants for inner functions are constant. Centner (2021) and Centner, Cheng, and Felder (2023) develop nonlinear \(H^p\) optimal polynomial approximants, while Cheng and Felder (2023) investigate their fixed-point and error properties. The previously established first-jet behavior for linear \(H^4\) inner approximants is an instance \((m,n)=(2,1)\). The result here is the all-degree, all-even-exponent determination of the *complete objective* with the exact universal jet cutoff and optimal finite-Blaschke replacement degree; it does not claim that Schur interpolation itself or Hilbert-space constant approximants are new.

## Limitations
The exact cutoff is sharp for the *whole variational objective*, but need not be the smallest number of Taylor coefficients needed to determine only the minimizing polynomial in each special case. In particular, if \(f(0)=0\), the unique optimal polynomial is zero even though nonoptimal objective values still contain higher-jet information. No analogue for non-even Hardy exponents, arbitrary non-inner generators, or vector-valued inner functions is asserted. The theorem yields a finite polynomial optimization problem; it does not generally solve that remaining nonlinear finite optimization in radicals. Novelty is assessed relative to accessible records and literature, not certified against every unindexed source.

## References
1. R. Centner, *Optimal Polynomial Approximants in \(L^p\)*, arXiv:2112.14002, first posted 2021-12-28, https://arxiv.org/abs/2112.14002.
2. R. Centner, R. Cheng, C. Felder, *Optimal Polynomial Approximants in \(H^p\)*, arXiv:2305.16068, first posted 2023-05-25, https://arxiv.org/abs/2305.16068.
3. R. Cheng, C. Felder, *More properties of optimal polynomial approximants in Hardy spaces*, arXiv:2310.16010, first posted 2023-10-24, https://arxiv.org/abs/2310.16010.
4. C. Bénéteau, M. Fleeman, D. Khavinson, D. Seco, A. Sola, *Remarks on inner functions and optimal approximants*, arXiv:1707.06166, 2017, https://arxiv.org/abs/1707.06166.
5. V. Bolotnikov, *An algorithm for finding low degree rational solutions to the Schur coefficient problem*, arXiv:0912.5034, 2009, https://arxiv.org/abs/0912.5034.
6. C. Felder, T. Le, *Analogues of finite Blaschke products as inner functions*, arXiv:2105.01766, 2021, https://arxiv.org/abs/2105.01766.
