# Maximal-edge plateaus determine sharp one-pass relaxation for causal weighted shifts

## Finding
Let \(n\ge2\), and let \(W\in\mathbb C^{n\times n}\) be a nonzero strictly lower one-step weighted shift, \(We_i=w_ie_{i+1}\) for \(1\le i<n\), with arbitrary complex weights. Define \(M=\max_i|w_i|>0\). Among the indices \(i\) with \(|w_i|=M\), let \(L\) be the length of the longest consecutive run (so \(1\le L\le n-1\)). Let
\[
 c_L=\cos\!\left(\frac{\pi}{L+1}\right),\qquad
 \nu(W)=\lambda_{\max}\!\left(\frac{|W|+|W|^{\mathsf T}}{2}\right),
\]
where \(|W|\) denotes the entrywise absolute-value matrix. For the one-pass Euclidean worst-case error factor
\[
 F(t)=\|(1-t)I_n+tW\|_2,\qquad t\in[0,1],
\]
**the minimizing parameter is unique**, and it obeys the following exact three-way classification:
\[
\boxed{\begin{array}{ll}
 t_*=1&\text{if }M\le c_L;\\
 0<t_*<1&\text{if }M>c_L\text{ and }\nu(W)<1;\\
 t_*=0&\text{if }\nu(W)\ge1.
\end{array}}
\]
These conditions are exhaustive and mutually exclusive; the first case implies \(\nu(W)<1\). In the middle case, \(F(t_*)<\min\{M,1\}\); at the two endpoints the respective minimum factors are \(M\) and \(1\). The same optimizer is globally optimal among all \(t\ge0\).

Thus whether the spectrally ideal nilpotent iteration \(t=1\) is also one-pass-norm optimal depends only on \(M\) and the **contiguity of its maximum-weight edges**, not on the other weights. For example the two sequences
\[
 (2/5,2/5,1/5,1/5)\quad\text{and}\quad(2/5,1/5,2/5,1/5)
\]
produce shifts with the same weight multiset and the same spectral radius \(|1-t|\) for the relaxed iteration. In the first, \(L=2\), \(M=2/5<1/2=c_L\), and \(t_*=1\). In the second, \(L=1\), \(c_L=0\), and \(0<t_*<1\). Both have \(\nu(W)<1\), since \(\nu(W)\le M<1\).

More generally, for a causal one-lag transmission model \(G=-aI_n+C\) with \(a\ge0\) and nonzero weighted one-step shift \(C\), its relaxed error operator is \(H_\theta=(1-\theta)I+\theta G\), \(0\le\theta\le1\). Set \(d=1+a\), \(W=C/d\), and \(t=d\theta\). The same complete criterion applies, and the unique optimum is \(\theta_*=t_*/d\).

## Assumptions and scope
All dimensions are finite, with arbitrary complex subdiagonal weights (zero weights allowed), but at least one weight nonzero. The norm is the induced Euclidean matrix norm. A maximum-edge run consists of consecutive positions among \(1,\ldots,n-1\), *not* a run of states; its length is the number of edges. The quantity \(\nu(W)\) is the numerical radius of this weighted shift, which equals the largest eigenvalue of the explicitly displayed real symmetric tridiagonal matrix. The transmission interpretation concerns an exact one-lag causal error transfer, not all discretizations of a heat equation or all waveform iterations. The optimization criterion is the supremum over all initial error vectors after **one** outer iteration, not asymptotic spectral radius and not a fixed initial error.

## Proof
**Phase normalization.** Because the directed path has no cycles, a diagonal unitary gauge removes the phases of all nonzero weights: \(D^*WD=|W|\). This also preserves \(I\) and the induced norm. Thus assume that \(W\) has real nonnegative weights. Writing \(J=(|W|+|W|^{\mathsf T})/2\), phase alignment along the path and the Rayleigh quotient give \(\nu(W)=\lambda_{\max}(J)\).

**Strict convexity and existence.** Put \(B=W-I\). Since \(W\) is nilpotent, \(B\) is invertible. For every unit vector \(x\), the function \(\|(I+tB)x\|_2^2\) has second derivative \(2\|Bx\|^2\ge 2\sigma_{\min}(B)^2>0\). Taking the supremum over unit vectors preserves this common strong-convexity modulus. Consequently \(g(t)=F(t)^2=\max_{\|x\|=1}\|(I+tB)x\|^2\) is strictly convex on the real line. It is coercive because \(B\) is invertible, so it has one global minimizer.

**Derivative at zero.** Direct multiplication gives \((I+tB)^*(I+tB)=I+t(W+W^*-2I)+t^2B^*B\). The top eigenvalue perturbation of \(I\), or the Rayleigh max principle uniformly on the unit sphere, yields
\[
 g'(0+)=\lambda_{\max}(W+W^*-2I)=2(\nu(W)-1).
\]
Thus the global minimum is exactly at \(t=0\) when \(\nu(W)\ge1\), including equality by strict convexity, and lies to its right otherwise.

**Derivative at the nilpotent parameter.** At \(t=1\), \(g(1)=\|W\|^2=M^2\). For \(\delta\downarrow0\),
\[
 [(1-\delta)W+\delta I]^*[(1-\delta)W+\delta I]
 =W^*W+\delta(W+W^*-2W^*W)+O(\delta^2).
\]
The top eigenspace of \(W^*W\) is spanned by exactly those basis vectors \(e_i\) for which \(|w_i|=M\). The compression of its first-order perturbation has constant diagonal \(-2M^2\), and neighboring off-diagonal entries \(M\) exactly where **both** consecutive edge indices are maximal. Therefore it splits into path adjacency blocks of lengths equal to the maximal-edge run lengths. A length-\(\ell\) path block has highest adjacency eigenvalue \(2\cos(\pi/(\ell+1))\), as follows by the sine eigenvector identity with zero boundary conditions. Taking the largest block gives the exact one-sided expansion
\[
 g(1-\delta)=M^2+2M(c_L-M)\delta+O(\delta^2),\qquad
 g'(1-)=2M(M-c_L).
\]
This standard finite-dimensional Hermitian perturbation statement also holds for a multiple top eigenvalue: the right derivative in \(\delta\) is the largest eigenvalue of the perturbation compressed to the entire top eigenspace. One can prove it directly by decomposing a maximizing unit vector into the top eigenspace and its spectral-gap complement, then applying the Rayleigh variational principle; finite dimensionality supplies a positive gap below the top eigenvalue whenever the complement is nonempty. In the empty-complement case the compressed formula is immediate.

If \(M\le c_L\), then \(g'(1-)\le0\), so strict convexity makes \(t=1\) its unique minimizer on \(( -\infty,1]\). To exclude \(t>1\), use nonnegativity and entrywise monotonicity of the Euclidean operator norm for nonnegative matrices: for every \(t>1\), diagonal sign-gauge equivalence yields
\[
 F(t)=\|(t-1)I+tW\|_2\ge t\|W\|_2=tM>M=F(1).
\]
If instead \(M>c_L\), the displayed left derivative is positive and the unique minimizing parameter lies **strictly below** \(1\). Together with the sign of \(g'(0+)\), this gives all three regimes.

**Exhaustiveness and the transmission normalization.** For a finite nonzero nilpotent weighted shift, \(\nu(W)<\|W\|=M\): equality in numerical-radius versus operator-norm would require a norming unit vector to be a modulus-\(M\) eigenvector, impossible for a nilpotent matrix. Thus \(M\le c_L<1\) implies \(\nu(W)<1\), and the three cases do not overlap. For the one-lag transmission form, \(H_\theta=(1-d\theta)I+\theta C=(1-t)I+tW\). Its allowed interval \(t\in[0,d]\) contains \([0,1]\); no \(t>1\) can improve on \(t=1\), as proved above. This proves the full claim.

## Verification
Run `python check.py` with NumPy and SciPy installed. The checker generates representative maximum-run regimes, checks the exact graph threshold and interval predictions against direct singular-value minimization, checks the two explicitly rearranged weight sequences, and cross-checks the one-sided slope formula using rational finite differences. The mathematical proof above is for every dimension and every admissible weight vector; finite tests do not establish the universal theorem.

## Relationship to prior work
Birken and Kotarsky (2026, arXiv:2610.01475v1, full HTML Sections 1–3 consulted) develop fully discrete finite-window \(\ell^2\) DNWR convergence estimates for heterogeneous heat equations. They motivate dependence on relaxation and temporal coupling, but their actual error operator generally has more than one delay diagonal; the theorem here claims neither an exact representation of their entire method nor an improvement to their PDE bounds. Kotarsky, Birken, Gander and Lu (2026, arXiv:2606.29987) study related time-discrete finite-window \(L^2\) convergence and relaxation selection, without an arbitrary weighted one-lag matrix norm classification.

The published result *The sharp affine Jordan norm pencil and its scaled q-spectral-set transition* (2026, full RESULT text inspected) gives a unique exact norm minimizer for the **unweighted** Jordan pencil \((1-t)I+tJ_n\). Its special unweighted-coefficient instance is acknowledged as prior coverage; arbitrary edge weights and the maximum-weight-run trichotomy here do not follow from its result by replacing one scalar parameter. The separate published result *Smoothness classification for binary weighted-shift numerical-radius norms* (2026, full RESULT text inspected) proves a longest-run law for the numerical radius and smoothness of binary shifts on an infinite-dimensional sequence space. It does not optimize \(\|(1-t)I+tW\|\), and its binary numerical-radius law does not imply the one-pass optimality classification for arbitrary nonbinary weights. The overlapping sine-eigenvalue path calculation is standard and not claimed as new.

## Limitations
The classification covers only an affine one-lag nilpotent error-transfer family, with arbitrary time-dependent weights but a common scalar relaxation. It does not extend automatically to full causal Toeplitz transfers with multiple delay taps, arbitrary feedback matrices, or minimization of an entire sequence of iterates. Its sharpness is one outer sweep in Euclidean norm; the spectral-radius optimum remains \(t=1\) for every weight vector. The exact value of an interior minimizer is implicitly characterized by the strictly convex singular-value norm, not generally given in radicals. General older matrix-optimization literature may contain equivalent statements not indexed in the searched resources. No independent audit has been performed.

## References
1. P. Birken and N. Kotarsky, *Dirichlet–Neumann waveform relaxation for heterogeneous heat equations: fully discrete l² analysis*, arXiv:2610.01475v1, first submitted 2026-10-01. https://arxiv.org/abs/2610.01475
2. N. Kotarsky, P. Birken, M. J. Gander and L.-D. Lu, *Dirichlet–Neumann waveform relaxation for heterogeneous heat equations: continuous and time discrete L² analysis*, arXiv:2606.29987, first submitted 2026-06-29. https://arxiv.org/abs/2606.29987
3. *The sharp affine Jordan norm pencil and its scaled q-spectral-set transition*, public mathematical result, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-sharp-affine-jordan-norm-pencil-and-its-scaled-q-spectral-se--00a25760cd57
4. *Smoothness classification for binary weighted-shift numerical-radius norms*, public mathematical result, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-smoothness-classification-for-binary-weighted-shift-numerical-ra--c193c24462fb
