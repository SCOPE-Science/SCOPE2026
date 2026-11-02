# Sharp orientation sensitivity of two-step randomly pivoted Cholesky on a three-dimensional rank-one spike

## Finding

Let \(L>1\), let \(v\in\mathbb C^3\) satisfy \(\|v\|_2=1\), and let \(K=I_3+(L-1)vv^*\). Apply **exact** sequential randomly pivoted Cholesky (RPCholesky) for two pivots, with each new coordinate sampled proportionally to the diagonal of the current positive-semidefinite residual. Denote its rank-two Nyström approximation by \(\widehat K_2\), and set \(\mathcal E_L(v)=\mathbb E\operatorname{tr}(K-\widehat K_2)\).

Write \(w_i=|v_i|^2\), so \(w_i\geq0\) and \(\sum_{i=1}^3w_i=1\). The **exact orientation law** is

\[
\mathcal E_L(v)=\frac{2L}{L+2}\sum_{i=1}^3\frac{1+(L-1)w_i}{L+1+(L-1)w_i}.
\]

Its **sharp extrema over every unit vector** are

\[
\boxed{\frac{L(L+5)}{(L+1)(L+2)}\ \leq\ \mathcal E_L(v)\ \leq\ \frac{3L}{2L+1}.}
\]

The lower equality holds **exactly when** \(v\) is a coordinate vector up to phase and permutation; the upper equality holds **exactly when** \(|v_1|=|v_2|=|v_3|=1/\sqrt3\). These are the complete equality cases for \(L>1\). The sharp ratio of largest to smallest expected residual is

\[
\boxed{\frac{3(L+1)(L+2)}{(2L+1)(L+5)}=1+\frac{(L-1)^2}{(2L+1)(L+5)}\ \nearrow\ \frac32\quad(L\to\infty).}
\]

In contrast, the expected trace residual after the **first** pivot is independent of \(v\):

\[
\mathbb E\operatorname{tr}(K-\widehat K_1)=\frac{2(2L+1)}{L+2}.
\]

Thus three dimensions and two pivots are the smallest dimensions/iteration count exhibiting dependence of expected RPCholesky trace error on eigenvector orientation at fixed spectrum. For size-two determinantal-point-process (\(2\)-DPP) sampling, the exact expected error is the orientation-independent value \(3L/(2L+1)\), equal to the **maximum** here. The DPP identity is a comparison, not a claim of inventing DPP sampling.

## Assumptions and scope

The input is a complex Hermitian positive-definite \(3\times3\) matrix with spectrum \(\{L,1,1\}\) and \(L>1\). Arithmetic is exact. Sampling is **sequential and adaptive**, according to the actual post-update residual diagonal at both stages; independent fixed-distribution sampling, block sampling, or deterministic greedy pivoting is not covered. At every pivot the algorithm performs the full Cholesky/Nyström Schur-complement update. The expectation is solely over the random ordered pair of distinct selected pivot coordinates.

There are no limiting assumptions in the orientation law or its equality cases. The value \(L=1\) is excluded from uniqueness statements because the input is the identity and every orientation coincides; its expected two-pivot residual equals one.

## Proof

**1. Exact two-pivot formula for arbitrary \(3\times3\) positive-definite input.** Let \(A\) be such an input, \(S=\operatorname{tr}A\), \(a_i=A_{ii}>0\), and let \(R^{(i)}=A-A_{:i}A_{i:}/a_i\) be the residual after first pivot \(i\). Its trace is

\[
t_i=\operatorname{tr}R^{(i)}=S-\frac{(A^2)_{ii}}{a_i}>0.
\]

Let \(\Delta_{ij}=a_ia_j-|A_{ij}|^2>0\). The first pivot has probability \(a_i/S\). The residual diagonal at the second candidate \(j\ne i\) is \(R^{(i)}_{jj}=\Delta_{ij}/a_i\), hence the **ordered** pair \((i,j)\) occurs with probability

\[
\mathbb P((i,j))=\frac{a_i}{S}\frac{\Delta_{ij}/a_i}{t_i}=\frac{\Delta_{ij}}{S t_i}.
\]

The final residual is a scalar Schur complement, embedded in the one remaining coordinate. The determinant identity for Schur complements gives its trace \(\det(A)/\Delta_{ij}\). Summing over the six possible ordered pairs gives cancellation of every principal minor:

\[
\mathbb E\operatorname{tr}R^{(2)}
=\sum_i\sum_{j\ne i}\frac{\Delta_{ij}}{S t_i}\frac{\det A}{\Delta_{ij}}
=\frac{2\det A}{S}\sum_{i=1}^3\frac1{t_i}.
\]

This identity is exact for every positive-definite \(3\times3\) input. No independent-pivot or replacement assumption has entered the computation.

**2. Spike specialization.** Set \(a=L-1\), \(w_i=|v_i|^2\). The matrix determinant lemma gives \(\det K=L\), while \(\operatorname{tr}K=L+2\), \(K_{ii}=1+aw_i\), and \((K^2)_{ii}=1+(L^2-1)w_i\). Therefore

\[
t_i=L+2-\frac{1+(L^2-1)w_i}{1+aw_i}
=\frac{L+1+aw_i}{1+aw_i}.
\]

Substitution into step 1 proves the displayed exact orientation law. The relative phases of the entries of \(v\) are irrelevant.

**3. Complete optimization and equality cases.** Define \(f_L(w)=(1+aw)/(L+1+aw)=1-L/(L+1+aw)\) on \([0,1]\). For \(L>1\),

\[
f_L''(w)=-\frac{2L(L-1)^2}{(L+1+(L-1)w)^3}<0.
\]

Strict Jensen concavity on the three-simplex gives \(\sum_i f_L(w_i)\leq3f_L(1/3)\), with equality exactly at \(w=(1/3,1/3,1/3)\). Conversely, every simplex point is a convex combination of the three vertices, and concavity gives \(\sum_i f_L(w_i)\geq f_L(1)+2f_L(0)\), with equality exactly at a vertex (by strict concavity). Evaluating these expressions gives respectively \(3L/(2L+1)\) and \(L(L+5)/((L+1)(L+2))\). Their ratio simplifies to the displayed formula, whose derivative is strictly positive for \(L>1\), and whose limit as \(L\to\infty\) is \(3/2\).

**4. First-step invariance and minimality.** Directly averaging the first Schur-complement update for any positive-definite \(A\) yields the previously established identity

\[
\mathbb E R^{(1)}=A-\frac{A^2}{\operatorname{tr}A},\qquad
\mathbb E\operatorname{tr}R^{(1)}=\operatorname{tr}A-\frac{\operatorname{tr}(A^2)}{\operatorname{tr}A}.
\]

Consequently one pivot cannot distinguish orthogonal/unitary conjugates in trace expectation. Any positive-definite \(2\times2\) input is recovered exactly after two distinct pivots, so dimension three with two pivots is minimal. Evaluating the last identity for eigenvalues \(L,1,1\) gives \(2(2L+1)/(L+2)\).

**5. DPP comparison.** The known \(2\)-DPP law on a positive-definite \(3\times3\) matrix samples an unordered pair \(\{i,j\}\) with probability \(\Delta_{ij}/\sum_{r<s}\Delta_{rs}\). Its expected remaining trace is \(3\det A/\sum_{r<s}\Delta_{rs}\). For eigenvalues \(L,1,1\), the denominator equals the second elementary spectral symmetric polynomial \(2L+1\), proving the stated equality with the orientation-maximal RPCholesky error. No comparison for arbitrary spectra or sample sizes is asserted.

## Verification

Run `python3 verify.py` using Python's standard library. The verifier enumerates all six ordered adaptive pivot histories with exact rational arithmetic for the identity, several rational spike heights, and several axis, balanced, and interior spike directions. It independently computes both update stages, their exact probabilities, the trace after the second update, the general determinant identity, the sharp bounds, all attainable equality examples, and the \(2\)-DPP benchmark. All finite checks are supplemental: the strict Jensen argument proves the global, infinite family of orientations, and rational enumeration does not substitute for that proof.

## Relationship to prior work

Chen, Epperly, Tropp and Webber introduce and analyze the exact sequential diagonal-residual RPCholesky rule and the one-step expected-residual map \(A-A^2/\operatorname{tr}A\) (arXiv:2207.06503, Algorithm 1, Section 5.1). Their results include general mean-error bounds and the determinantal-sampling comparison; these are acknowledged rather than claimed here. The new assertion is the **complete, sharp eigenvector-orientation extremum of the actual two-step expectation** for a fixed spiked spectrum, not a bound on the iteration of the nonlinear one-step expectation map.

Epperly, Tropp and Webber (arXiv:2410.03969, Sections 1.3–2) show that their accelerated implementation preserves the sequential RPCholesky pivot law, so the exact two-step classification also applies to that implementation. Epperly (arXiv:2608.20633, Sections 1.2 and 4) establishes sharper general expectation and concentration bounds; these do not themselves specify this orientation classification. The 2026 source is contextual literature, not a source of the claimed 2022 public date.

## Limitations

The sharp \(3/2\) limiting ratio is an **orientation-induced difference in mean residual trace for the same spectrum**, not a universal performance ratio for arbitrary positive-semidefinite inputs. The classification concerns only three dimensions, the spectrum \(\{L,1,1\}\), and exactly two exact-arithmetic, sequential pivots. It says nothing about finite-precision roundoff, arbitrary rank, arbitrary eigenvalue multiplicities, other pivot distributions, or whether the same extremizers persist for larger matrices. Originality is a best-knowledge assessment rather than independently certified priority.

## References

1. Y. Chen, E. N. Epperly, J. A. Tropp, R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503 (first posted 2022-07-13), especially Algorithm 1, Section 5.1, and Appendix C; https://arxiv.org/abs/2207.06503 .
2. E. N. Epperly, J. A. Tropp, R. J. Webber, *Embrace rejection: Kernel matrix approximation by accelerated randomly pivoted Cholesky*, arXiv:2410.03969 (first posted 2024-10-04), Sections 1.3–2; https://arxiv.org/abs/2410.03969 .
3. E. N. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm*, arXiv:2608.20633 (2026), Sections 1.2 and 4; https://arxiv.org/abs/2608.20633 .
