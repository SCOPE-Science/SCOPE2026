# Superspecial strata of bielliptic Picard curves at primes congruent to five modulo six

## Finding

Let \(p=6m+5\) be prime, with \(m\ge0\), and \(k\) an algebraically closed field of characteristic \(p\). For each \(a\in k\) satisfying \(a^2\ne4\), let \(C_a\) denote the smooth projective genus-three curve with affine equation
\[y^3=x^4+a x^2+1.\]
Define the degree-\(m\) Hasse polynomial
\[R_m(a)=[t^m](t^2+at+1)^{2m+1}.\]
Then \(R_m\) has precisely \(m\) distinct roots in \(k\), none equal to \(\pm2\). At these and only these parameters \(\operatorname{Jac}(C_a)\) is superspecial with \(p\)-rank zero and \(a\)-number three. Elsewhere in the smooth family its \(p\)-rank is two and \(a\)-number one; the corresponding Newton slopes are \(0,0,1/2,1/2,1,1\). At a superspecial point all six slopes are \(1/2\). The superspecial locus is therefore a reduced length-\(m\) divisor **on the marked parameter line** (not a count of geometric isomorphism classes).

## Assumptions and scope

The characteristic is a prime \(p\equiv5\pmod6\), the field is algebraically closed, and the even quartic is separable precisely when \(a^2\ne4\). Its projective closure is smooth of genus three. The involution \(x\mapsto-x\) yields a genus-one quotient and a two-dimensional Prym, motivating the explicit exceptional locus. This result does not address primes congruent to one modulo six or the quotient by automorphisms of the parameter line.

## Proof

Set \(g(t)=t^2+at+1\) and write \(p=6m+5\). A canonical basis of holomorphic differentials is \(\omega_0=dx/y^2\), \(\omega_1=x\,dx/y^2\), \(\omega_2=dx/y\). The Cartier identity \(\mathcal C(z^p\eta)=z\mathcal C(\eta)\), together with \(\mathcal C(x^{pi+p-1}dx)=x^i dx\), shows that, up to the nonzero \(p\)-th-root semilinearity, its only possibly nonzero arrows are
\[\omega_0\longmapsto U_m(a)\omega_2,\quad \omega_2\longmapsto V_m(a)\omega_0,\quad \omega_1\longmapsto0,\]
where the coefficients are interpreted under inverse Frobenius and
\[U_m=[t^{3m+2}]g^{2m+1}=[t^m]g^{2m+1}=R_m,\qquad V_m=[t^{3m+2}]g^{4m+3}.\]
The last equality for \(U_m\) uses reciprocity of the monic palindromic quadratic. Parity of \(g(x^2)\) forces all other entries to vanish. Roots of these coefficients are unchanged by inverse Frobenius.

We establish the nontrivial polynomial identity, **in characteristic \(p\)**,
\[V_m(a)=K_m(a^2-4)^{m+1}R_m(a),\quad K_m=\frac{\binom{4m+3}{3m+2}}{\binom{2m+1}{m}}\in\mathbb F_p^\times.\]
For arbitrary nonnegative integers \(N,j\), the coefficient polynomial \(F_{N,j}(a)=[t^j](t^2+at+1)^N\) satisfies (by checking its multinomial coefficients) the differential equation
\[(a^2-4)F''+(1-2N)aF'+j(2N-j)F=0.\]
In particular \(R_m=F_{2m+1,m}\) satisfies
\[(a^2-4)R_m''-(4m+1)aR_m'+m(3m+2)R_m=0.\]
Write \(V_m=F_{4m+3,3m+2}\). For \(0\le r\le m\), differentiating with respect to \(a\) and specializing \(a=2\) gives
\[V_m^{(r)}(2)=(4m+3)_{\underline r}\binom{8m+6-2r}{3m+2-r}=0\pmod p.\]
Indeed \(8m+6-2r=p+(2m+1-2r)\), while the lower index lies strictly between this remainder and \(p\); Lucas's binomial congruence applies. The same argument holds at \(a=-2\), with an immaterial sign. Since \(m+1<p\), \((a^2-4)^{m+1}\) divides \(V_m\). Put \(T_m=V_m/(a^2-4)^{m+1}\), of degree at most \(m\). Substituting this factorization into the equation for \(F_{4m+3,3m+2}\), both extra terms vanish modulo \(p=6m+5\), and \(T_m\) obeys exactly the displayed differential equation for \(R_m\). Solutions of degree at most \(m\) to this equation form a one-dimensional space: descending comparison of coefficients involves the nonzero multipliers \((j-m)(j-3m-2)\) for \(0\le j<m\), and fixes each lower coefficient from the leading one. The leading coefficients of \(V_m\) and \(R_m\) are respectively \(\binom{4m+3}{3m+2}\) and \(\binom{2m+1}{m}\), both nonzero modulo \(p\), proving the identity.

The leading term of \(R_m\) is nonzero, hence \(\deg R_m=m\). At the forbidden values \(a=\pm2\), reciprocity gives \(R_m(\pm2)=(\pm1)^m\binom{4m+2}{m}\ne0\pmod p\). If \(R_m\) had a double root away from these two values, differentiating its second-order differential equation successively would force every derivative at that root to vanish. Since \(m<p\), this forces the degree-\(m\) polynomial to vanish identically, a contradiction. Thus it has exactly \(m\) simple roots. At a smooth parameter, \(a^2-4\ne0\), the identity shows \(U_m\) and \(V_m\) are either both zero or both nonzero. If both are nonzero, Cartier iterates retain rank two, proving \(p\)-rank two and Cartier nullity one. If both vanish, Cartier is zero on all holomorphic forms, hence the Jacobian is superspecial, with \(p\)-rank zero and \(a\)-number three. The Newton slopes in the first case follow from the elliptic quotient (with supersingular \(j=0\) in characteristic \(p\equiv2\pmod3\)) and the ordinary two-dimensional Prym; in the second case superspeciality gives the stated slopes.

## Verification

A standalone pure-Python script `verify.py` independently constructs the relevant coefficient polynomials over several finite prime fields and checks their factor identity, degree, squarefreeness and exclusion of the singular boundary; its normal successful output ends with `VERIFY_OK`. This is a test, **not** a substitute for the preceding all-prime proof. Examples: at \(p=5\), \(m=0\) and no superspecial parameter occurs; at \(p=11\), \(m=1\) and the sole parameter is \(a=0\); at \(p=17\), the superspecial points solve \(a^2=8\) in \(k\).

## Relationship to prior work

Bouw studies generalized Hasse–Witt invariants and the generic behavior of tame cyclic covers, not the exact marked superspecial divisor of this symmetric quartic family. Kazemifard–Tafazolian classify Newton polygons of two special Picard curves including the \(a=0\) case; that individual case is not claimed as new. Nourozi–Rahmati give the Picard differential basis and general Cartier framework but do not derive this prime-uniform coefficient factorization or the degree-and-reducedness classification. Their stated unconditional \(a\)-number assertion does not cover the exceptional reality; the special example at \(p=11\) was already known elsewhere. Laga–Shnidman identify the family and its Prym with quaternionic multiplication but focus on geometry and arithmetic over characteristic zero. The present claim is the all-prime explicit superspecial **divisor**, its squarefreeness and sharp two-stratum classification, not novelty of the general Cartier technique, of the family, or of any known individual special point.

## Limitations

No statement about distinct isomorphism classes of curves after parameter identifications is made. Published coverage of Shimura-curve Hasse invariants could imply related assertions in different moduli coordinates; this is a residual literature risk, despite the targeted searches. No independent audit has been performed. This proof uses elementary Cartier and polynomial identities, not a calculation of every zeta function.

## References

1. I. I. Bouw, “The p-Rank of Ramified Covers of Curves,” Compositio Mathematica 126 (2001), 295–322, DOI:10.1023/A:1017513122376 (MSC 14H30; primary archive direction).
2. A. Kazemifard and S. Tafazolian, “A note on some Picard curves over finite fields,” Finite Fields and Their Applications 34 (2015), 107–122, DOI:10.1016/j.ffa.2014.12.002 (the \(a=0\) special curves, not the full parameter family).
3. V. Nourozi and F. Rahmati, “The Rank of the Cartier operator on Picard Curves,” arXiv:2306.07823 (2023; general differential basis and Cartier framework; its stated universal \(a\)-number conclusion cannot be applied at the exceptional points).
4. J. Laga and A. Shnidman, “The geometry and arithmetic of bielliptic Picard curves,” arXiv:2308.15297 (2023); Journal of the London Mathematical Society 112 (2025), e70347 (Prym and moduli motivation).
