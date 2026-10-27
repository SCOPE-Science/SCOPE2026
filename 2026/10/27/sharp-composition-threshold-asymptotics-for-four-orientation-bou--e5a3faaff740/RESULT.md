# Sharp composition-threshold asymptotics for four-orientation bounded-run stacking words

## Finding
Let \(L_n(\alpha)\) count words of length \(n\) over the four orientations \(\{0,45,-45,90\}\), considered modulo \(180\) degrees, obeying (i) adjacent circular angular separation at most \(45\) degrees, (ii) every constant run has length at most three, (iii) equal counts of \(+45\) and \(-45\), and (iv) each of the four orientations occupies at least \(\lceil\alpha n\rceil\) positions. Let \(S_{2m}(\alpha)\) count additionally reflection-symmetric words of even length \(2m\).

Let \(\rho\in(0,1)\) be the positive solution of \(2(\rho+\rho^2+\rho^3)=1\), let \(\lambda=1/\rho\), and put
\[
K=\frac1{\rho(1+2\rho+3\rho^2)},\quad
p_j=2\rho^j\ (1\le j\le3),\quad
\mu=\sum_{j=1}^3 j p_j,\quad \nu=\sum_{j=1}^3 j^2p_j,\quad
s=\frac{\nu}{2\mu},\quad t=\frac{\nu-\mu^2}{\mu}.
\]
All \(s,t,K\) are positive. Write
\[
C=\frac{K}{\sqrt{2\pi s}},\qquad
C_*=\frac{8K}{(2\pi)^{3/2}s\sqrt t}.
\]
Then for **every fixed** \(0\le\alpha<1/4\),
\[
L_n(\alpha)\sim C\lambda^n n^{-1/2},\qquad
S_{2m}(\alpha)\sim 2\rho C\lambda^m m^{-1/2}.
\]
Moreover the difference between \(L_n(\alpha)\) and the count with no minimum-share rule is exponentially smaller than \(\lambda^n\), and likewise for symmetric half-words. At the **sharp boundary** \(\alpha=1/4\), \(L_n(\alpha)=0\) if \(4\nmid n\), whereas along multiples of four
\[
L_n(1/4)\sim C_*\lambda^n n^{-3/2}.
\]
For every \(\alpha>1/4\), \(L_n(\alpha)=S_{2m}(\alpha)=0\) for every positive permitted length. In particular, for fixed \(\alpha<1/4\),
\[
\frac{L_{2m}(\alpha)}{S_{2m}(\alpha)}\sim\frac{\lambda^m}{2\rho\sqrt2}.
\]
Numerically \(\lambda=2.919639565839418\ldots\), \(C=0.623563340731638\ldots\), \(C_*=1.617518528363286\ldots\), and \(2\rho C=0.427150904534587\ldots\).

## Assumptions and scope
Words are **labeled, linear** stacking sequences, not classes under cyclic rotation or reflection. Orientation angle is interpreted modulo \(180\) degrees. A change of orientation of exactly \(45\) degrees is allowed; adjacent equal orientations are allowed subject to the run-length cap of three. Balance means only equality between the two diagonal orientations, not equality of all four contents. Reflection symmetry in the even-length case means \(w_i=w_{2m+1-i}\). The result concerns counting accepted words, not mechanical rigidity or laminate optimization. The asymptotic constants depend on fixed \(\alpha\), with no assertion of uniformity as \(\alpha\uparrow1/4\).

## Proof
**1. Exact rational generating function.** Put \(A=\{0,90\}\) and \(B=\{+45,-45\}\). Different consecutive runs must alternate between \(A\) and \(B\): the allowable change graph is the four-cycle \(K_{2,2}\). A run has length \(j\in\{1,2,3\}\), and the choice between the two letters in its partition is independent of the previous run. For \(X=c_{+45}-c_{-45}\), \(Y=c_0-c_{90}\), and \(Z=(c_0+c_{90})-(c_{+45}+c_{-45})\), define Laurent polynomials
\[
A(z,y,v)=\sum_{j=1}^3 z^j v^j(y^j+y^{-j}),\qquad
B(z,x,v)=\sum_{j=1}^3 z^j v^{-j}(x^j+x^{-j}).
\]
The coefficient of \(z^nx^Xy^Yv^Z\) in
\[
F(z,x,y,v)=\frac{(1+A)(1+B)}{1-AB}
\]
counts exactly those words with prescribed length and signed contents: the expansion lists all alternating run sequences, including the empty word, without duplicates. With all markers one, \(A=B=2H(z)\), \(H=z+z^2+z^3\). Hence \(F(z,1,1,1)=(1+2H)/(1-2H)\). Its sole pole of minimum modulus is the simple positive root \(\rho\) of \(2H(\rho)=1\). Its normalized pole amplitude is \(K=1/(\rho H'(\rho))\); thus unrestricted locally admissible counts are asymptotic to \(K\lambda^n\).

**2. Balance local limit.** Restrict to \(y=v=1\) and \(x=e^{iu}\); then \(A=2H(z)\) and \(B=2\sum_{j=1}^3z^j\cos(ju)\). The unique minimal-modulus pole near \(u=0\) varies analytically. Its logarithmic curvature is \(s=\nu/(2\mu)\). The strict triangle inequality for the consecutive lengths \(1,2,3\) shows that no other point of the coefficient-extraction torus has the same pole modulus: equality forces the argument of \(z\) and \(u\) to vanish modulo \(2\pi\). Fourier inversion at \(X=0\) and a one-dimensional Gaussian saddle therefore give \([z^nx^0]F(z,x,1,1)\sim K\lambda^n/(\sqrt{2\pi s n})\). The positivity of the curvature follows from \(\nu>0\). The exponentially decaying remainder outside the saddle follows from compactness of the torus and analyticity in a common annulus.

**3. The four-way equality boundary.** At minimum share \(\alpha=1/4\), all four counts must equal \(n/4\), requiring \(4\mid n\). This is equivalent to \(X=Y=Z=0\). In a typical pair of consecutive independent \(A\)- and \(B\)-runs, lengths have distribution \(p_j=2\rho^j\), and the choices of letter within a partition are equiprobable. The expected pair length is \(2\mu\). The covariance of the pair's \((X,Y,Z)\) increments is \(\operatorname{diag}(\nu,\nu,2(\nu-\mu^2))\); all mixed covariances vanish by sign symmetry and independence. Per unit word length, the covariance is therefore \(\operatorname{diag}(s,s,t)\).

There are exactly **eight** contributing dominant Fourier phases. Indeed equality in the triangle inequalities for \(A\) and \(B\) at \(|z|=\rho\), \(|x|=|y|=|v|=1\) requires the angles of \(x,y\) to belong to \(\{0,\pi\}\), and writing the angles of \(z,x,y,v\) as \(\theta_z,\theta_x,\theta_y,\theta_v\), the conditions are
\[
\theta_z+\theta_v+\theta_y=0\pmod{2\pi},\quad
\theta_z-\theta_v+\theta_x=0\pmod{2\pi}.
\]
There are four choices of the two binary angles, two choices of \(\theta_z\), and one corresponding choice of \(\theta_v\). Each gives the same pole residue \(K\) and covariance. Along \(4\mid n\), their phases all add positively; otherwise the exact coefficient is zero. Three-dimensional Fourier inversion contributes \(1/((2\pi n)^{3/2}s\sqrt t)\), multiplied by eight, giving the stated \(C_*\). The positive variance \(t\) follows because the run-length distribution has nonzero variance.

**4. Minimum-content bounds away from the boundary.** Use the finite-state primitive transition graph recording the current orientation and current run length \(1,2,3\). Its spectral radius is \(\lambda\). Rotating the four-cycle permutes all orientations, so the Perron stationary frequency of each symbol is exactly \(1/4\). For the one-variable transfer matrix that weights each occurrence of a chosen symbol by \(e^u\), the leading eigenvalue \(\Lambda_a(u)\) is analytic with \(\Lambda_a(0)=\lambda\) and \((d/du)\log\Lambda_a(0)=1/4\). For each fixed \(\alpha<1/4\), a sufficiently small negative \(u\) has \(\log\Lambda_a(u)-\alpha u<\log\lambda\). The exponential Markov inequality bounds the number of locally admissible words with a specified symbol count below \(\lceil\alpha n\rceil\) by \(O(\eta_a^n)\), \(\eta_a<\lambda\). A union bound over four letters gives an exponentially smaller excluded count, also after imposing balance. For \(\alpha>1/4\), four minimum counts cannot sum to \(n\).

**5. Mirror condition.** A mirrored word of length \(2m\) is determined by its first \(m\) symbols. The central duplicated run has length twice the last run of the half-word; the run cap three holds at the seam if and only if that last run has length one. Local admissibility elsewhere, balance, and minimum-content percentages reduce exactly to the corresponding conditions on the half-word. In the run generating function, requiring the last run to have length one replaces the final \(A\)-run or \(B\)-run by \(A_1=2z\) or \(B_1=z(x+x^{-1})\) after setting \(y=v=1\). This yields
\[
E(z,x)=\frac{A_1(1+B)+B_1(1+A)}{1-AB},
\]
where \(A=2H(z)\) and \(B=\sum_{j=1}^3 z^j(x^j+x^{-j})\). At \(x=1\), \(E(z,1)=4z/(1-2H(z))\); thus the pole amplitude is \(2\rho K\). The marked denominator and hence the balance variance \(s\) are unchanged. The same local Fourier argument gives \(S_{2m}(0)\sim2\rho C\lambda^m/\sqrt m\). The tilted Perron bound with the terminal restriction on run length one remains valid, so any fixed sub-quarter minimum percentage only excludes exponentially fewer half-words. Substituting the two asymptotic formulas gives the ratio in the finding.

## Verification
The accompanying standalone program `verify_counts.py` uses an independent position-by-position state recurrence, not the run-generating-function formula. It verifies all local and balance conditions by brute-force enumeration for lengths one through seven; at length \(48\), it returns \(31{,}056{,}472{,}857{,}623{,}585{,}226{,}752\) locally admissible words, \(1{,}928{,}147{,}653{,}129{,}777{,}177{,}600\) balanced words, \(1{,}899{,}989{,}961{,}206{,}244{,}002{,}236\) satisfying the ten-percent rule, and \(98{,}266{,}297{,}652{,}879{,}155{,}168\) equal-content words. At mirrored full length \(48\), it obtains exactly \(11{,}236{,}189{,}644\) compliant words, equal to the integer in the source's Table 1. It independently recomputes the analytic constants. These finite checks supplement, but do not replace, the infinite analytic proof.

## Relationship to prior work
Langiu, Rubino and Canale (first publicly posted October 16, 2026) derive exact finite dynamic-programming enumeration and sampling algorithms for these manufacturing rules and report data at length \(48\). The present statement supplies explicit all-length exponential rates, Gaussian prefactors, a sharp one-quarter composition phase boundary with a change in polynomial exponent, and the exponential mirror-symmetry penalty. These assertions do not follow merely from a finite table. The generating-function and Fourier methods use standard analytic-combinatorics techniques, so priority concerns the application and explicit formulas, not their general methodological ingredients.

## Limitations
The proof is for exactly four orientation classes, maximum constant-run length three, and local angular tolerance \(45\) degrees. It does not enumerate stiffness-feasible laminates or other physical constraints. The asymptotics for \(\alpha<1/4\) are not uniform when \(\alpha\) approaches \(1/4\) with growing length. At the boundary, only the unsymmetric all-equal count is evaluated, not the reflected all-equal counterpart. Possible equivalent results outside the examined literature remain an originality risk; independent review has not been performed.

## References
1. A. Langiu, F. Rubino and G. Canale, *Counting and Sampling Manufacturable Stacking Sequences*, arXiv:2610.23146v1, initially public October 16, 2026. https://arxiv.org/abs/2610.23146
2. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, chapters on rational generating functions and saddle-point/local-limit methods.
