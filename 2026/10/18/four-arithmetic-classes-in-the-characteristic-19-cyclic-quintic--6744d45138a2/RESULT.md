# Four arithmetic classes in the characteristic-\(19\) cyclic-quintic genus-four family

## Finding
Let \(k=\overline{\mathbf F}_{19}\). For \(t\in k\setminus\{0,1\}\), let \(C_t\) be the smooth projective normalization of
\[
C_t:\qquad y^5=x(x-1)(x-t).
\]
All these curves have genus \(4\). Their Jacobian invariants obey the **complete geometric dichotomy**
\[
(\operatorname{rank}_{19} J(C_t),a(J(C_t)))=
\begin{cases}(0,4),&t\in\{-1,2,1/2\},\\(2,2),&t\notin\{0,1,-1,2,1/2\}.
\end{cases}
\]
In particular, precisely the three harmonic parameters are superspecial (Cartier operator zero), and these curves are mutually isomorphic over \(\mathbf F_{19}\).

Among the \(17\) parameters \(t\in\mathbf F_{19}\setminus\{0,1\}\), there are **exactly four distinct \(\mathbf F_{19}\)-isomorphism classes**. Their six-element anharmonic transformations, point counts and invariants are as follows:

| Parameter orbit in \(\mathbf F_{19}\) | \(\#C_t(\mathbf F_{19})\) | \(\#C_t(\mathbf F_{19^2})\) | \(19\)-rank | \(a\)-number |
|---|---:|---:|---:|---:|
| \(\{2,10,18\}\) | 20 | 514 | 0 | 4 |
| \(\{8,12\}\) | 20 | 354 | 2 | 2 |
| \(\{3,7,9,11,13,17\}\) | 20 | 404 | 2 | 2 |
| \(\{4,5,6,14,15,16\}\) | 20 | 424 | 2 | 2 |

Only the harmonic orbit meets the genus-four Hasse–Weil upper bound \(19^2+1+8\cdot19=514\) over \(\mathbf F_{19^2}\).

## Assumptions and scope
The field has characteristic \(19\), and the three finite branch points \(0,1,t\) must be distinct. The Kummer cover is separable of degree \(5\), totally ramified at \(0,1,t,\infty\), and its unique smooth projective normalization is intended throughout. The arithmetic orbit/count table concerns parameters defined over \(\mathbf F_{19}\); the Cartier classification holds for every geometric parameter in \(k\setminus\{0,1\}\). \(19\)-rank denotes the dimension of the stable Cartier image, equivalently the Jacobian \(19\)-rank, and \(a\)-number is the dimension of its Cartier kernel.

## Proof
**Genus and holomorphic forms.** Riemann–Hurwitz for the tamely branched degree-five map gives \(2g-2=-10+4\cdot4=6\), hence \(g=4\). At finite branch points the valuation of \(dx\) is \(4\), and \(y\) is a uniformizer. At infinity, \(v(x)=-5\), \(v(y)=-3\), \(v(dx)=-6\). The four regular, linearly independent differentials
\[
\omega_2=\frac{dx}{y^2},\quad \omega_3=\frac{dx}{y^3},\quad
\omega_4=\frac{dx}{y^4},\quad \eta_4=\frac{x\,dx}{y^4}
\]
therefore form a basis of \(H^0(C_t,\Omega^1)\).

**Complete Cartier matrix.** Write \(f(x)=x(x-1)(x-t)\). In characteristic \(19\), the relations \(y^5=f\) yield
\[
\omega_2=y^{-57}f^{11}dx,\qquad
\omega_3=y^{-38}f^{7}dx,\qquad
\omega_4=y^{-19}f^{3}dx,\quad
\eta_4=y^{-19}x f^{3}dx.
\]
By the Cartier coefficient-selection rule, only terms of \(x\)-degree congruent to \(18\) modulo \(19\) survive, with their coefficients raised to the \(19\)th inverse Frobenius power. As \(\deg_x f^{11}=33\), \(\deg_x f^7=21\), and \(\deg_x(xf^3)=10\), this gives
\[
\mathcal C(\omega_2)=A(t)^{1/19}\omega_3,\quad
\mathcal C(\omega_3)=B(t)^{1/19}\omega_2,\quad
\mathcal C(\omega_4)=\mathcal C(\eta_4)=0,
\]
where the *exact* coefficients in \(\mathbf F_{19}[t]\) are
\[
A(t)=[x^{18}]f^{11}=-7t^4(t-1)^4(t-2)(t+1)(t+9),
\qquad B(t)=[x^{18}]f^7=3(t-2)(t+1)(t+9).
\]
For reproducibility these follow directly from the finite sum
\[
[x^{18}]f^n=(-1)^{18-n}\sum_{r+s=18-n}\binom nr\binom ns\,t^{n-s}
\qquad(n=7,11),
\]
using coefficients reduced modulo \(19\). Since \(t\ne0,1\), the two off-diagonal coefficients vanish simultaneously precisely when \(t\in\{2,-1,-9\}=\{2,-1,1/2\}\). Otherwise both are nonzero, so the Cartier operator has rank \(2\) and invertible semilinear action on its two-dimensional image; every iterate has image of dimension \(2\). Thus its stable rank is \(2\), its kernel dimension is \(2\), and the stated \(19\)-rank and \(a\)-number dichotomy follows. When both coefficients vanish, the entire Cartier operator is zero, so the Jacobian is superspecial and has invariants \((0,4)\).

**Rational isomorphism orbits.** The transformations \(t\mapsto1-t\) and \(t\mapsto1/t\) arise by affine relabeling of the three finite branch points, fixing infinity. These coordinate changes multiply the cubic on the right by an element of \(\mathbf F_{19}^{\times}\), which has a unique fifth root because \(\gcd(5,18)=1\). Thus members of each resulting anharmonic orbit are \(\mathbf F_{19}\)-isomorphic. Direct modular arithmetic partitions the 17 parameters into the four orbits in the table.

**Exact point counts and inequivalence.** The fifth-power map permutes \(\mathbf F_{19}\), so every member has \(19\) affine rational points and one point at infinity: \(\#C_t(\mathbf F_{19})=20\). In the explicit quadratic field \(K=\mathbf F_{19}[u]/(u^2-2)\), where \(2\) is a nonsquare, a nonzero element has five fifth roots exactly when its \(72\)nd power is \(1\). Enumerating the \(361\) values of \(x\in K\) therefore computes
\[
\#C_t(K)=1+\sum_{x\in K}\begin{cases}
1,&f(x)=0,\\5,&f(x)\ne0\text{ and }f(x)^{72}=1,\\0,&\text{otherwise}.
\end{cases}
\]
The executable `verify.py` implements this exact calculation for all 17 parameters and produces the table. Because the four counts \(514,354,404,424\) are distinct, curves from different orbits cannot be \(\mathbf F_{19}\)-isomorphic. This proves both the four-class assertion and sharp maximality statement.

## Verification
Run `python3 verify.py` using Python's standard library (no dependencies). It checks both coefficient-polynomial identities, the complete 17-parameter partition under anharmonic transformations, all quadratic-extension point counts, the Cartier-rank assignments, and the Hasse–Weil equality. Expected terminal status ends `All 17 parameters, four F_19-isomorphism classes, and maximality: PASS`. The infinite-field Cartier statement is proved algebraically above rather than extrapolated from the finite enumerations.

## Relationship to prior work
Cavalieri and Pries, arXiv:2308.14891 (first public version August 28, 2023), identify the four-branch-point genus-four cyclic quintic family as Moonen's special family \(M[11]\), with inertia type equivalent to \((1,1,1,2)\), and prove mass-formula results for the congruence class \(p\equiv1\pmod5\). Here \(p=19\equiv4\pmod5\) and the point of interest is a complete geometric Cartier-rank stratification and exact small-field parameter classification, not their mass formula. Li, Mantovan, Pries and Tang, arXiv:1805.06914, §6.2, list both \(\mathrm{ord}^2\oplus\mathrm{ss}^2\) and \(\mathrm{ss}^4\) as Newton polygon possibilities for this family when \(p\equiv4\pmod5\); their table does not identify the three harmonic parameters, Cartier kernels, or all four \(\mathbf F_{19}\)-isomorphism classes and quadratic point counts. Explicit supersingular cyclic curves by Streng, arXiv:2501.14902, treats different Moonen families \(M[6],M[8],M[16]\), not \(M[11]\). General prior supersingular-existence statements are not claimed as new.

## Limitations
This theorem concerns only this displayed one-dimensional family, not all genus-four curves. Parameter orbits classify the 17 members defined by these parameters over \(\mathbf F_{19}\), not all geometric curves in the family. The proof of inequivalence uses point counts over \(\mathbf F_{19^2}\), so it makes no assertion that the four classes remain distinct over an algebraic closure. No independently validated publication priority is claimed; an unnoticed earlier equivalent explicit computation remains a bibliographic possibility.

## References
- R. Cavalieri and R. Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891v1 (August 28, 2023), especially §6.1 and Remark 6.5(3): https://arxiv.org/abs/2308.14891.
- W. Li, E. Mantovan, R. Pries and Y. Tang, *Newton polygons arising from special families of cyclic covers of the projective line*, arXiv:1805.06914 (May 17, 2018), especially §6.2: https://arxiv.org/abs/1805.06914.
- M. Streng, *Explicit supersingular cyclic curves*, arXiv:2501.14902 (January 24, 2025), introduction and family scope: https://arxiv.org/abs/2501.14902.
