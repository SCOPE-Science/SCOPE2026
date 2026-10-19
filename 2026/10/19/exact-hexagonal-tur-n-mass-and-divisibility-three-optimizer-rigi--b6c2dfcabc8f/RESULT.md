# Exact hexagonal Turán mass and divisibility-three optimizer rigidity on finite tori

## Finding
For every integer \(n\ge3\), let \(G_n=(\mathbb Z/n\mathbb Z)^2\) and let
\[
\Omega=\{0,\pm e_1,\pm e_2,\pm(e_1-e_2)\}\subset G_n.
\]
Let \(\mathcal T_n\) be the maximum of \(\sum_{x\in G_n}f(x)\) among complex positive-definite functions \(f:G_n\to\mathbb C\) supported on \(\Omega\) and satisfying \(f(0)=1\). Define
\[
r_n=\left\lfloor\frac{n+1}{3}\right\rfloor,\qquad
\sigma_n=2\cos\left(\frac{2\pi r_n}{n}\right)+\cos\left(\frac{4\pi r_n}{n}\right)<0.
\]
Then the exact, counting-measure-normalized Turán mass is
\[
\boxed{\mathcal T_n=1-\frac3{\sigma_n}}.
\]
For \(3\nmid n\), the **unique** extremizer is \(f(0)=1\) and \(f(x)=-1/(2\sigma_n)\) at each of the six nonzero sites of \(\Omega\). For \(3\mid n\), \(\mathcal T_n=3\), and the full extremizer set is the four-real-dimensional convex face cut out by the two Fourier equalities
\[
\widehat f(n/3,2n/3)=\widehat f(2n/3,n/3)=0
\]
within the above positive-definite, supported, normalized function space; its relative interior contains the autocorrelation extremizer \(f(x)=1/3\) at all six nonzero sites. In particular, as \(n\to\infty\) through \(3\nmid n\),
\[
\mathcal T_n=3+\frac{8\pi^2}{9n^2}+O(n^{-3}),
\]
whereas every multiple of three has mass exactly \(3\). The exceptional grid \(n=4\) has nine minimizing Fourier characters rather than six, but its optimizer is still unique.

## Assumptions and scope
Positive definite means that \((f(x_i-x_j))_{i,j}\) is positive semidefinite for every finite family in \(G_n\). With \(\zeta_n=e^{2\pi i/n}\), use the unnormalized Fourier transform
\[
\widehat f(k,l)=\sum_{x=(x_1,x_2)\in G_n}f(x)\zeta_n^{kx_1+lx_2},
\]
which is pointwise real and nonnegative for positive-definite \(f\). The objective is \(\widehat f(0,0)\), with counting measure on the finite group. All six nonzero sites of \(\Omega\) are distinct when \(n\ge3\). The claim covers arbitrary complex coefficient phases; no assumption of radiality, nonnegative coefficients, or extra symmetry is imposed on competitors.

## Proof
**1. Symmetry reduction is lossless.** The order-six lattice automorphism
\[
R=\begin{pmatrix}1&1\\-1&0\end{pmatrix}
\]
cyclically permutes the six sites \(\pm e_1,\pm e_2,\pm(e_1-e_2)\); it satisfies \(R^3=-I\). Averaging any admissible \(f\) over \(\langle R\rangle\) preserves normalization, support, positive definiteness, and total mass. Averages therefore have \(f(0)=1\) and the same real coefficient \(a\) at every nonzero site. For \(u=2\pi k/n\), \(v=2\pi l/n\), define
\[
S_n(k,l)=\cos u+\cos v+\cos(u-v).
\]
Their Fourier transform is \(1+2aS_n(k,l)\), and total mass is \(1+6a\). Its optimum has \(a\ge0\). Thus, writing \(s_n=\min_{k,l}S_n(k,l)<0\), the upper bound and the matching symmetric admissible extremizer give \(\mathcal T_n=1-3/s_n\).

**2. Exact finite-grid minimum.** Observe the phasor identity
\[
3+2S_n(k,l)=|1+\zeta_n^k+\zeta_n^l|^2.
\]
Place these three roots on the circle and write their three successive angular gaps, measured in multiples of \(2\pi/n\), as nonnegative integers \(a,b,c\) with \(a+b+c=n\). Then \(S=\cos(2\pi a/n)+\cos(2\pi b/n)+\cos(2\pi c/n)\). If one gap is at least \(n/2\), the sum of the cosines of the other two is nonnegative (use the cosine addition formula), whence \(S\ge-1\). For \(n\ge5\) the equally spaced-as-possible triple yields \(S<-1\) because its representative angle \(2\pi r_n/n\) lies strictly between \(\pi/2\) and \(\pi\). Thus a minimizer for \(n\ge5\) has every gap less than \(n/2\).

If two gaps \(a>b\) differ by at least two, move one unit from \(a\) to \(b\). The resulting change in their cosine sum is
\[
2\cos\left(\frac{\pi(a+b)}n\right)
\left[\cos\left(\frac{\pi(a-b-2)}n\right)
-\cos\left(\frac{\pi(a-b)}n\right)\right]<0.
\]
Indeed \(a+b=n-c>n/2\), the first factor is negative, and the bracket is positive because cosine strictly decreases on \([0,\pi/2]\). Repeated smoothing terminates only when the three gaps differ by at most one. The gap multisets are \((m,m,m)\) for \(n=3m\), \((m,m,m+1)\) for \(n=3m+1\), and \((m,m+1,m+1)\) for \(n=3m+2\). Each can be represented by the roots \(1,\zeta_n^{r_n},\zeta_n^{2r_n}\), proving \(s_n=\sigma_n\). For \(n=3\), direct three-root balancing gives \(-3/2\); for \(n=4\), all triples have a gap at least two and attain no value below \(-1\), while \((1,1,2)\) attains \(-1\). These agree with the formula.

The same strict smoothing shows that when \(n\ge5\) and \(3\nmid n\), exactly six Fourier characters minimize \(S_n\); when \(3\mid n\), exactly two do. For \(n=4\), there are nine minima: the six balanced configurations and three configurations containing two coincident roots. The six-character rotation orbit is present in every case \(3\nmid n\).

**3. Rigidity away from three-divisibility.** Put \(t=\zeta_n^{r_n}\), \(v_j=R^je_1\), and \(\chi_i=(R^{-\mathsf T})^i(r_n,2r_n)\) for \(0\le i,j<6\). All six \(\chi_i\) are Fourier minimizers when \(3\nmid n\). The Fourier evaluation matrix \(M_{ij}=\zeta_n^{\langle\chi_i,v_j\rangle}\) is circulant, with first row
\[
(t,t^{-1},t^{-2},t^{-1},t,t^2).
\]
Set \(\omega=e^{\pi i/3}\). Direct six-point Fourier diagonalization gives eigenvalues \(\lambda_h=\sum_{j=0}^5 M_{0j}\omega^{hj}\). Up to nonzero scalar factors, the polynomials \(t^2\lambda_h\), ordered by \(h=0,1,2,3,4,5\), are
\[
\begin{split}
&t^4+2t^3+2t+1,\\
&(t-1)(t+1)(t^2+t+1),\\
&(t-1)^2(t^2+t+1),\\
&-(t-1)^3(t+1),\\
&(t-1)^2(t^2+t+1),\\
&(t-1)(t+1)(t^2+t+1).
\end{split}
\]
The first equals \(2t^2\sigma_n\), so none vanishes: \(\sigma_n<0\), and \(3\nmid n\) implies that \(t\) is neither \(1\), \(-1\), nor a primitive third root. Hence \(M\) is invertible.

Let \(f\) be any optimizer and \(\bar f\) its rotational average. At each minimizing character \(\chi\), \(\widehat{\bar f}(\chi)=0\) while all \(\widehat{f\circ R^j}(\chi)\ge0\). Every term is therefore zero, implying \(\widehat f(\chi_i)=0\) for all six \(i\). Subtract the symmetric extremizer from \(f\): the difference vanishes at zero, is supported on the six sites, and has zero Fourier evaluation under the invertible matrix \(M\). It must be identically zero. This proves uniqueness including the exceptional \(n=4\) grid.

**4. The divisible-by-three face.** Let \(n=3m\) and \(H=\{0,e_1,e_2\}\). Its normalized autocorrelation \(f_H=\tfrac13\mathbf1_H*\mathbf1_{-H}\) has central value one, all six neighboring values \(1/3\), and Fourier transform \(\tfrac13|1+\zeta_n^k+\zeta_n^l|^2\). Exactly the two characters \((m,2m)\) and \((2m,m)\) are zeros. Since the rotational average of any optimizer vanishes at these characters, nonnegativity forces each optimizer to vanish at both. Conversely, writing \(A=f(e_1)\), \(B=f(e_2)\), \(C=f(e_1-e_2)\) and \(\eta=e^{2\pi i/3}\), the sum of the two Fourier values is
\[
2+2\operatorname{Re}[(A+B+C)(\eta+\eta^2)]
=2-2\operatorname{Re}(A+B+C).
\]
If both are zero, \(\operatorname{Re}(A+B+C)=1\), so total mass equals three. The two real Fourier conditions are independent linear equations on the six real coordinates of \((A,B,C)\); at \(f_H\) every other Fourier value is strictly positive. Consequently the extremal face has real affine dimension four, with \(f_H\) in its relative interior.

**5. Asymptotic.** For \(3\nmid n\), the angle \(2\pi r_n/n\) equals \(2\pi/3\pm2\pi/(3n)\). Taylor expansion yields \(\sigma_n=-3/2+2\pi^2/(3n^2)+O(n^{-3})\), and substituting into the exact formula gives the asserted correction.

## Verification
Run `python CHECKER.py` from the unpacked files; it requires Python 3.10+, `numpy`, `scipy`, and `sympy`. It independently exhausts the \(n^2\) Fourier grid values for every \(3\le n\le100\), solves the **unrestricted six-real-variable linear program** for every \(3\le n\le25\), checks the contact-matrix ranks for those same moduli, and symbolically verifies all six complex eigenvalue factorizations above. Each check passed when run from the packaged path. The proof of the infinite family is the analytic symmetry reduction, gap-smoothing lemma, and circulant factorization, not finite enumeration.

## Relationship to prior work
Arestov–Berdysheva (2001) solved the **Euclidean continuous** regular-hexagon Turán problem. Kolountzakis–Révész (arXiv:math/0204086, 2002) proved spectral convex Euclidean domains are Turán domains; their arXiv:math/0312218 (2003) develops general positive-definite Turán estimates on finite groups, including spectral-set and packing bounds. In this problem \(\Omega=H-H\) for a three-point \(H\), and a spectral three-point configuration occurs when \(3\mid n\). These general results motivate the base mass three but do not give the exact *finite-grid excess*, mod-three formula, unique off-three optimizer, or the four-dimensional on-three face. Closely related later public results on cyclic five-site and Lee-ball Turán supports concern different groups/neighbor sets; a three-frequency conditioning result concerns a different objective. The present theorem is specific to the natural triangular-lattice six-neighbor support and arbitrary complex positive-definite competitors.

## Limitations
The theorem gives the exact Turán mass and optimizer-face structure only for the stated seven-site triangular neighborhood, not for arbitrary hexagonal-radius supports or anisotropic edge weights. It makes no claim about independent publication priority. Unindexed lattice-spectrum or finite-positive-type tables might contain an equivalent special case; the named sources examined do not supply the complete claimed theorem. The checker is finite and cannot independently certify the all-moduli proof.

## References
1. V. V. Arestov and E. E. Berdysheva, "Turán's problem for positive definite functions with supports in a hexagon," *Trudy Instituta Matematiki i Mekhaniki UrO RAN* 7(1), 21–29 (2001), https://www.mathnet.ru/eng/timm297 (full Russian text available).
2. M. N. Kolountzakis and S. Gy. Révész, "On a problem of Turán about positive definite functions," arXiv:math/0204086, publicly posted 2002-04-08, https://arxiv.org/abs/math/0204086.
3. M. N. Kolountzakis and S. Gy. Révész, "Turán's extremal problem for positive definite functions on groups," arXiv:math/0312218, publicly posted 2003-12-10, https://arxiv.org/abs/math/0312218.
4. Public research records for "Exact Turan mass for the five-point support {0, ±1, ±3} on cyclic groups," "Exact divisibility threshold for the Turán mass of a cyclic Lee two-ball," and "Sharp Riesz conditioning for consecutive triples on finite cycles" (published-finding corpus, 2026); these are nearby but different statements.
