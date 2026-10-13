# Exact reshuffling contraction on the regular-simplex Kaczmarz frame

## Finding
Let \(v_1,\ldots,v_{n+1}\in\mathbb R^n\) be the unit vertices of a centered regular simplex,
\[
\langle v_i,v_j\rangle=-\frac1n\quad(i\ne j),
\qquad
\sum_{i=1}^{n+1}v_iv_i^{\mathsf T}=\frac{n+1}n I.
\]
For a consistent linear system whose normalized rows are \(v_i^{\mathsf T}\), write
\[
P_i=I-v_iv_i^{\mathsf T}.
\]
A fresh random-reshuffling Kaczmarz epoch chooses a uniform permutation \(\pi\) and maps the incoming solution error \(e\) to
\[
T_\pi e,
\qquad
T_\pi=P_{\pi_{n+1}}\cdots P_{\pi_1}.
\]
Then, for every deterministic \(e\),
\[
\mathbb E_\pi\|T_\pi e\|_2^2=c_n\|e\|_2^2,
\]
with the exact factor
\[
c_n=-\frac1n+\frac1{n^3}\sum_{\ell=0}^{n-1}(n-\ell)\left(1+\frac1n\right)^{2\ell}
\]
and equivalently
\[
c_n=\frac{n}{(2n+1)^2}
\left[
\left(1+\frac1n\right)^{2n+2}-7-\frac7n-\frac2{n^2}
\right].
\]
Thus independent fresh reshuffling at each epoch gives the exact law
\[
\mathbb E\|e_k\|_2^2=c_n^k\|e_0\|_2^2.
\]

Uniform with-replacement randomized Kaczmarz is also exactly solvable on this frame. Each row action has conditional squared-error factor \(1-1/n\), so after \(n+1\) row actions its factor is
\[
d_n=\left(1-\frac1n\right)^{n+1}.
\]
The asymptotics separate the two protocols sharply:
\[
c_n=\frac{e^2-7}{4n}+O(n^{-2}),
\qquad
d_n\longrightarrow e^{-1}.
\]
Hence a complete fresh reshuffled pass leaves only order \(1/n\) of the incoming mean-square error on this canonical frame, while the same number of independent with-replacement projections leaves a positive limiting fraction.

## Assumptions and scope
The system is consistent and has exactly \(n+1\) unit-normalized rows forming a regular simplex in \(\mathbb R^n\). The result concerns ordinary unit-relaxation Kaczmarz projections. A fresh independent permutation is drawn at the beginning of every reshuffling epoch. The expectation is over the ordering only; the incoming error may be any deterministic vector.

The comparison uses the same cost unit for both protocols: one epoch consists of \(n+1\) row projections. No statement is made here for noisy or inconsistent systems, relaxed projections, non-simplex equiangular frames, or reuse of a single permutation across epochs.

## Proof
Use the standard simplex realization in
\[
H=\left\{y\in\mathbb R^{n+1}:\mathbf 1^{\mathsf T}y=0}\right\},
\]
namely
\[
v_i=\sqrt{\frac{n+1}n}\left(e_i-\frac1{n+1}\mathbf1\right).
\]
Coordinate permutations act transitively on the \(v_i\) and orthogonally on \(H\). Define
\[
G=\mathbb E_\pi[T_\pi^{\mathsf T}T_\pi].
\]
Uniformity of \(\pi\) makes \(G\) commute with every coordinate permutation. The permutation representation on \(H\) is irreducible over \(\mathbb R\), so the symmetric operator \(G|_H\) is a scalar multiple of the identity:
\[
G|_H=c_nI_H.
\]
Therefore
\[
c_n=\frac1n\|T\|_{\mathrm{HS}(H)}^2
\]
for any fixed order \(T=P_{n+1}\cdots P_1\), because all fixed orders are conjugate by simplex symmetries.

Let
\[
T_i=P_i\cdots P_1,
\qquad
F_i=\|T_i\|_{\mathrm{HS}(H)}^2,
\qquad
F_0=n.
\]
Since \(P_i\) is the orthogonal projection perpendicular to \(v_i\),
\[
F_i=F_{i-1}-\|T_{i-1}^{\mathsf T}v_i\|_2^2.
\]
To evaluate the lost norm, apply \(T_{i-1}^{\mathsf T}=P_1\cdots P_{i-1}\) to \(v_i\). Before any previous vertex is removed, its inner product with every such vertex is \(-1/n\). If the common inner product with every still-unprocessed previous vertex is \(t\), projecting away one previous vertex changes each remaining common inner product to
\[
t-t\left(-\frac1n\right)=\left(1+\frac1n\right)t.
\]
Thus the successive squared norm losses are
\[
\frac1{n^2}\left(1+\frac1n\right)^{2\ell},
\qquad \ell=0,\ldots,i-2,
\]
and hence
\[
\|T_{i-1}^{\mathsf T}v_i\|_2^2
=1-\frac1{n^2}\sum_{\ell=0}^{i-2}
\left(1+\frac1n\right)^{2\ell}.
\]
Summing \(F_i-F_{i-1}\) through \(i=n+1\) yields
\[
F_{n+1}
=-1+\frac1{n^2}\sum_{\ell=0}^{n-1}(n-\ell)
\left(1+\frac1n\right)^{2\ell},
\]
and division by \(n\) gives the first formula for \(c_n\).

For \(r=(1+1/n)^2\), the arithmetic-geometric identity
\[
\sum_{\ell=0}^{n-1}(n-\ell)r^\ell
=\frac{r^{n+1}-(n+1)r+n}{(r-1)^2}
\]
gives the closed form. Since \(n/(2n+1)^2=1/(4n)+O(n^{-2})\) and \((1+1/n)^{2n+2}=e^2+O(n^{-1})\), the stated asymptotic follows.

For with-replacement sampling, the tight-frame identity gives, conditionally on the current error,
\[
\mathbb E_i\|P_ie\|_2^2
=\|e\|_2^2-\frac1{n+1}
\sum_i\langle v_i,e\rangle^2
=\left(1-\frac1n\right)\|e\|_2^2.
\]
Iterating this conditional identity for \(n+1\) independent draws proves the exact factor \(d_n\).

## Verification
The embedded `verify.py` uses exact `Fraction` arithmetic. For \(1\le n\le5\) it enumerates every one of the \((n+1)!\) row orders, forms every projection product exactly in the ambient \(\mathbb R^{n+1}\) simplex model, and verifies that the averaged Gram matrix is
\[
\frac1{n+1}\mathbf1\mathbf1^{\mathsf T}
+c_n\left(I-\frac1{n+1}\mathbf1\mathbf1^{\mathsf T}\right).
\]
It separately checks the summation and closed forms for \(c_n\), the with-replacement factor, and the exact values
\[
c_1=0,
\quad c_2=\frac1{32},
\quad c_3=\frac{58}{2187},
\quad c_4=\frac{5673}{262144},
\quad c_5=\frac{879916}{48828125}.
\]
This finite enumeration corroborates the formulas; the proof for all \(n\) is the symmetry-and-Hilbert--Schmidt argument above.

## Relationship to prior work
Strohmer and Vershynin introduced randomized Kaczmarz with row sampling proportional to squared row norm and proved exponential convergence in expected squared error. On a unit-norm tight frame, their one-step expectation specializes to the exact with-replacement identity used here, but their result does not analyze a without-replacement simplex epoch.

Han and Xie analyze random-reshuffling Kaczmarz directly. They represent an epoch by the same product of row projections and prove a general linear-convergence bound using the spectral norm of that product. Their result is broader in admissible linear systems but does not give the exact averaged squared-error channel for a regular-simplex frame, the closed form \(c_n\), or its \(1/n\) asymptotic comparison with with-replacement sampling.

A 2026 unrefereed manuscript on metric-dependent random-reshuffling dynamics also studies a regular-simplex contraction family, but its factors are
\[
C_i(\rho)=\frac12\left[I+\rho(uz_i^{\mathsf T}+z_iu^{\mathsf T})\right],
\]
not Kaczmarz hyperplane projections. Its certified full-reshuffling results concern five- and six-factor families, and its stated all-length simplex-positivity question remains open for that different factor family. Those statements neither contain nor imply the all-dimensional projection formula proved here.

Agaskar, Wang, and Lu derive exact mean-square formulas for with-replacement randomized Kaczmarz and optimal sampling probabilities. The accessible abstract confirms the exact-MSE setting, but the full text was not inspected here; this remains an alias-risk source rather than evidence of coverage.

## Limitations
The exact scalar channel relies on the full permutation symmetry of the regular simplex. It is not asserted for arbitrary equiangular tight frames or generic unit-norm tight frames. The comparison fixes unit relaxation and exact consistency. It does not address noisy right-hand sides, inconsistent least squares, block Kaczmarz, adaptive row selection, or finite-precision effects.

The main residual originality risk is older projection-method or frame literature that may encode the same regular-simplex product average in different language. A second risk is that exact-MSE Kaczmarz literature not fully accessible in this check may contain a special-frame specialization equivalent to the displayed closed form.

## References
1. T. Strohmer and R. Vershynin, “A randomized Kaczmarz algorithm with exponential convergence,” arXiv:math/0702226, first public version 2007-02-08; later Journal of Fourier Analysis and Applications 15 (2009), 262–278.
2. D. Han and J. Xie, “A simple linear convergence analysis of the randomized reshuffling Kaczmarz method,” arXiv:2410.01140, first public version 2024-10-02; Journal of the Operations Research Society of China (2025).
3. Anonymous, “Which Sampling Scheme Is Better? Metric-Dependent Rankings in Random Reshuffling Dynamics,” version 1.1.1-candidate, 2026, DOI 10.5281/zenodo.22037371.
4. A. Agaskar, C. Wang, and Y. M. Lu, “Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities,” 2014.
