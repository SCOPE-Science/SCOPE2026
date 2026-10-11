# Exact phase-rigidity threshold for all even Fourier moments of the ternary circle
## Finding
Let \(C=\{(1,0),(-1,0),(0,1),(0,-1)\}\subset\mathbb F_3^2\), the unit-radius circle \(s_1^2+s_2^2=1\) over \(\mathbb F_3\). Let \(\omega=e^{2\pi i/3}\) and assign a unit complex number \(z_s\) to each \(s\in C\). For every integer \(m\ge1\), set
\[
\mathcal M_{2m}(z)=\frac19\sum_{u\in\mathbb F_3^2}\left|\sum_{s\in C}z_s\,\omega^{u\cdot s}\right|^{2m}.
\]
The following value is sharp simultaneously for all \(m\):
\[
\boxed{\max_{|z_s|=1}\mathcal M_{2m}(z)=\frac{16^m+4\cdot4^m+4}{9}.}
\]
There is an exact three-stage transition in the entire maximizing phase set. For \(m=1\), **all** unit phases maximize. For \(m=2\), writing \((a,b,c,d)=(z_{(1,0)},z_{(-1,0)},z_{(0,1)},z_{(0,-1)})\), the complete condition is
\[ab=cd.\]
After quotienting by a common unit scalar, this family is a two-dimensional torus. For **every** \(m\ge3\), the complete set becomes
\[
\boxed{(a,b,c,d)=\lambda(\omega^j,\omega^{-j},\omega^k,\omega^{-k}),\quad
\lambda\in\mathbb T,\quad (j,k)\in\mathbb F_3^2.}
\]
Thus there are exactly nine maximizing phase classes modulo common phase from the sixth moment onward, whereas the fourth moment admits a continuous two-torus. In particular, the sharp normalized sixth-moment ratio is \(484/4^3=121/16\), while the sharp normalized fourth-moment ratio is \(36/4^2=9/4\).

## Assumptions and scope
All quantifiers refer to the specified four-point nonzero-radius quadratic circle in \(\mathbb F_3^2\), the standard nontrivial additive character, integer moments \(m\ge1\), and **unimodular** coefficient weights. The phase-only constraint is essential; no sharp unrestricted-coefficient \(L^2\to L^{2m}\) norm is claimed. Haar averaging is normalized by \(1/9\), the coefficient \(L^2\) mass is exactly \(4\), and the stated count of nine identifies only common complex phases, not spatial translations or other symmetries.

## Proof
Denote \(S=C\). For \(t\in\mathbb F_3^2\), write
\[
A_{m,z}(t)=\sum_{s_1+\cdots+s_m=t}\prod_{r=1}^m z_{s_r},\qquad
N_m(t)=\#\{(s_1,\ldots,s_m)\in S^m:s_1+\cdots+s_m=t\}.
\]
Orthogonality of the nine characters gives the exact identity
\[
\mathcal M_{2m}(z)=\sum_t|A_{m,z}(t)|^2\le\sum_tN_m(t)^2.
\]
The upper bound is attained by the constant assignment \(z_s=1\). Equality holds exactly when, **for each** \(t\), all products associated with ordered \(m\)-tuples summing to \(t\) have the same argument; no cancellation can be hidden between distinct frequencies because all deficits \(N_m(t)^2-|A_{m,z}(t)|^2\) are nonnegative.

For the constant assignment, the real-valued Fourier polynomial is \(2\) at zero and \(-1\) at each nonzero coordinate, summed across the two coordinates. It therefore takes the values \(4\) once, \(1\) four times, and \(-2\) four times. Its \(2m\)-th normalized moment is \((16^m+4\cdot4^m+4)/9\), proving every sharp value.

For \(m=1\), no pairwise phase constraints occur. For \(m=2\), the only unordered two-sum coincidence beyond permutations is
\[(1,0)+(-1,0)=(0,1)+(0,-1)=(0,0).\]
The equality condition is therefore precisely \(ab=cd\). Four unit-circle parameters minus one independent equation and one global phase yield a two-torus.

For \(m=3\), the four triples consisting of three repeated copies of any individual point all sum to zero because the ambient group has exponent \(3\). Equality consequently forces \(a^3=b^3=c^3=d^3\). The two triples \(((1,0),(1,0),(-1,0))\) and \(((1,0),(0,1),(0,-1))\) both sum to \((1,0)\), forcing \(a^2b=acd\), hence \(ab=cd\).

These two conditions are sufficient. The common cube condition yields \((a,b,c,d)=\lambda(\omega^{r_1},\omega^{r_2},\omega^{r_3},\omega^{r_4})\) for some \(r_i\in\mathbb F_3\). The product condition is \(r_1+r_2=r_3+r_4\). Since \(2\) is invertible in \(\mathbb F_3\), subtracting half the common sum from all four exponents writes them as \((j,-j,k,-k)\). Thus the four phases are the restriction of a common scalar times one ambient additive character. Every ordered triple product then equals \(\lambda^3\omega^{(j,k)\cdot t}\), depending only on its sum \(t\). These and only these choices maximize the sixth moment.

For \(m>3\), any collision of two triple sums can be extended to a collision of \(m\)-sums by adjoining the same fixed \(m-3\) points to each triple. Therefore equality at the \(2m\)-th moment implies the sixth-moment conditions; conversely, a restricted additive character gives coherent products for every \(m\). Finally, two choices \((j,k)\) and \((j',k')\) cannot differ by a global scalar unless they are identical, because evaluating the four opposite pairs gives a character that is constant only for the zero frequency. Exactly nine projective classes remain.

## Verification
The self-contained `circle_phase_checker.py` expands ordered additive convolutions and verifies their exact integer-count moments for \(1\le m\le8\). It exhausts the \(256\) fourth-root coefficient assignments, checking the sharp fourth/sixth moments and an explicit fourth-moment optimizer that is not a sixth-moment optimizer; it also enumerates the \(27\) cube-root quadruples satisfying the pair condition and their nine classes modulo common cube-root phase. The checker returned `PASS`. These finite checks support, but do not prove, the all-\(m\) classification; the orthogonality, triangle-equality, and collision implications above are the proof.

## Relationship to prior work
The finite-field sphere restriction literature of Iosevich, Koh, Lee, Pham and Shen (arXiv:1806.11387) gives \(L^p\to L^4\) estimates for nonzero-radius spheres in specified dimensions, but not this four-point, phase-only **all-even-moment equality hierarchy**. González-Riquelme and Oliveira e Silva (arXiv:2405.16647) classify sharp extension extremizers for certain parabolic surfaces, including a sixth-moment parabola theorem in characteristic above three; this differs both in the quadratic surface and in the ternary characteristic. The published small-field anisotropic-sphere phase dichotomy treats six-point and twenty-point spheres in \(\mathbb F_3^3\) and \(\mathbb F_5^3\) at the fourth moment; it does not cover the present four-point planar circle or the sixth-moment rigidity threshold. The elementary fact that positive coefficients maximize a phase-only moment does **not** by itself give the equality geometry or minimal rigidifying moment determined here.

## Limitations
This is a phase-only result on one canonical finite-field circle, not an all-fields sphere theorem or a characterization of unrestricted Fourier extension norm maximizers. The highest moments were checked by finite code only through \(m=8\), whereas their formulas and equality classifications are proved algebraically for every integer \(m\ge1\). An equivalent characterization hidden in a broader unpublished or differently indexed phase-retrieval/Freiman-character treatment remains a bibliographic possibility. No independent mathematical audit has been performed.

## References
1. A. Iosevich, D. Koh, S. Lee, T. Pham, C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387, first posted 2018-06-29.
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first posted 2024-05-26.
3. *Small-field phase dichotomy for anisotropic sphere extremizers*, published mathematical note concerning three-dimensional finite-field spheres (2026), for comparison of fourth-moment phase geometry.
