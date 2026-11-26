# Exact quartic coefficient for finite-period Lyapunov variance near doubling

## Finding

On the circle let \(f_\varepsilon(x)=2x+\varepsilon[\sin(4\pi x)-2\sin(2\pi x)]\pmod 1\), with \(|\varepsilon|<1/(16\pi)\). For every fixed integer \(n\ge5\), the population variance \(V_n(\varepsilon)\) of \(n^{-1}\log((f_\varepsilon^n)'(p))\) under the uniform distribution on \(\operatorname{Fix}(f_\varepsilon^n)\) satisfies
\[
V_n(\varepsilon)=\frac{36\pi^4}{n}\varepsilon^4+O_n(|\varepsilon|^5).
\]
The last exception is \(n=4\), for which the quartic coefficient in \(nV_n\) is \(54\pi^4\), not \(36\pi^4\).

## Assumptions and scope

The lower bound \(f_\varepsilon'\ge 2-8\pi|\varepsilon|>3/2\) makes this a degree-two expanding covering. All \(2^n-1\) fixed points of the \(n\)-fold iterate are counted separately, including points of smaller least period. All expansions here take \(\varepsilon\to0\) with \(n\) fixed. They do not give a joint error bound or an identity at nonzero \(\varepsilon\).

## Proof

Put \(q(x)=\sin(2\pi x)\), \(T(x)=2x\pmod1\), \(u=q\circ T-2q\), and \(H_\varepsilon(x)=x+\varepsilon q(x)\pmod1\). This is a smooth diffeomorphism since \(H_\varepsilon'>0\). Taylor expansion of the lifts gives
\[
f_\varepsilon(H_\varepsilon x)=2x+\varepsilon q(2x)+\varepsilon^2q(x)u'(x)+O(\varepsilon^3).
\]
Inverting \(H_\varepsilon\) removes the first-order term: \(g_\varepsilon=H_\varepsilon^{-1}f_\varepsilon H_\varepsilon=2x+\varepsilon^2q(x)u'(x)+O_{C^2}(\varepsilon^3)\). The smooth expansions are uniform on the circle. Since \(q u'=2\pi(\sin(6\pi x)-\sin(2\pi x)-\sin(4\pi x))\),
\[
\log g_\varepsilon' = \log 2+\varepsilon^2 B+O_{C^1}(|\varepsilon|^3),\qquad
B(x)=2\pi^2(3\cos(6\pi x)-\cos(2\pi x)-2\cos(4\pi x)).
\]
The factors of \(H_\varepsilon'\) cancel in the multiplier on a periodic orbit. Write \(M=2^n-1\). At \(\varepsilon=0\) the fixed points of \(T^n\) are \(x_k=k/M\), \(0\le k<M\). They continue, along with each of their orbit points for fixed \(n\), with displacement \(O_n(\varepsilon^2)\), by the implicit function theorem and the expansion of \(g_\varepsilon\). These are all the points: the increment in the lift \(g_\varepsilon^n(x)-x\) over one circuit is \(M\) and its derivative is positive (each \(g_\varepsilon'>7/6\) by the conjugacy derivative formula). Thus the exponent equals \(\log2+\varepsilon^2 B_n(x_k)+O_n(|\varepsilon|^3)\), where \(B_n=n^{-1}\sum_{j=0}^{n-1} B\circ T^j\).

Define \(S_m(k)=\sum_{j=0}^{n-1}\cos(2\pi m2^jk/M)\). Because multiplication by 2 cycles the orbit frequencies, \(S_2=S_1\), so \(B_n(x_k)=6\pi^2(S_3(k)-S_1(k))/n\). For \(n\ge5\) the signed residues \(\pm2^j\) and \(\pm3\cdot 2^j\), \(0\le j<n\), are all distinct and nonzero modulo \(M\). In the first family a collision after cancelling a power of 2 would require \(2^k\equiv\pm1\) with \(1\le k<n\), excluded by size. Between families one would need \(3\cdot 2^k\equiv\pm1\); this integer is strictly between 1 and \(M-1\) for \(0\le k\le n-2\), and strictly between \(M+1\) and \(2M-1\) for \(k=n-1\). Within the second family a collision at distinct exponents would require \(M\mid 3(2^k\pm1)\) for \(1\le k<n\). The positive integer is below \(M\) for \(k\le n-2\) and strictly between \(M\) and \(2M\) for \(k=n-1\). Opposite signs at the same exponent would instead require \(M\mid 2\) or \(M\mid 6\), both impossible.

Exact character orthogonality gives mean zero for both sums, second moments \(n/2\) each, and zero mixed moment. It follows that \(\operatorname{Var}(B_n)=36\pi^4/n\). Centering and squaring the exponent expansion gives the stated remainder. At \(n=4\), \(M=15\), the first family still has eight distinct signed residues, but the second family has just four distinct residues, each of multiplicity two, disjoint from the first family. Hence \(\mathbb E S_1^2=2\), \(\mathbb E S_3^2=4\), and the mixed moment is zero. This gives the stated \(n=4\) exception.

## Verification

The accompanying `CHECK.py` tests finite cases of the character calculation using exact rational arithmetic, and representative nonlinear fixed-period equations numerically. The residue inequalities and Taylor argument prove the all-period result; finite tests do not replace them.

## Relationship to prior work and limitations

Drach, Fu, Kaloshin, Li and Liverani, *Normal distribution of Lyapunov exponents of periodic orbits for expanding circle maps*, arXiv:2511.15662, §4, study the infinite-period variance via a covariance series. The asymptotic quartic coefficient for this very family is also given in [*Quartic Lyapunov variance onset along conjugacy-tangent expanding perturbations*](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-quartic-lyapunov-variance-onset-along-conjugacy-tangent-expandin--06a032792658/RESULT.md) as \((9/4)\delta^4=36\pi^4\varepsilon^4\), under \(\delta=2\pi\varepsilon\). The distinct claim here concerns the coefficient at every fixed period from five on. Agreement of an infinite-period coefficient with the scaled finite coefficients is not a consequence of the variance limit; finite cyclic frequency collisions have to be excluded, and the last collision changes the coefficient. No general assertion for arbitrary perturbation directions is made.
