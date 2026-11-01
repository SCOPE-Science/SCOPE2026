# Poisson-mixture rigidity and sharp conditioning of balanced-wall Ising Fourier frames

## Finding
Let \(n=4h\ge4\), let \(m=n/2\), and sample uniformly from the set \(\Omega_n\subset\{-1,1\}^n\) of cyclic spin strings with exactly \(m\) disagreeing adjacent pairs (domain walls). With the probability normalization, form the Gram matrix of the constant function and the \(n\) coordinate characters \(\chi_j(x)=x_j\), indexed cyclically. It is positive definite and its eigenvalues are \(1\) and \(\lambda_\ell\), \(0\le\ell<n\), with
\[
\lambda_\ell=\frac{1}{\mathrm B(1/2,m+1/2)}\int_0^1\frac{r^{-1/2}(1-r^m)(1-r^2)}{(1+r)^{m+1}\,[1+2r\cos(4\pi\ell/n)+r^2]}\,dr.
\]
The eigenvalues depend only on the distance of \(\ell\) from \(n/4\) modulo \(n/2\), and increase *strictly* as \(\ell\) runs from \(0\) to \(n/4\). The minimum is attained exactly at modes \(0,n/2\); the maximum exactly at \(n/4,3n/4\). For \(0\le j\le n/4\), put
\[
a_0=1,\qquad a_j=\prod_{s=1}^j\frac{2s-1}{n-(2s-1)}.
\]
Then
\[
\lambda_{\min}=\frac{n}{n+2},\qquad
\lambda_{\max}=1+2\sum_{j=1}^{n/4-1}a_j+a_{n/4},\qquad
\boxed{\ \kappa_n^2=\frac{n+2}{n}\left(1+2\sum_{j=1}^{n/4-1}a_j+a_{n/4}\right)=1+\frac4n+O(n^{-2})\ }.
\]
Here \(\kappa_n^2\) is the *squared* singular-value condition number of the complete constant-plus-coordinate sampling operator. Empty sums are zero. The modes \(0,n/2\) and \(n/4,3n/4\) each have multiplicity two within the coordinate block; every intermediate spectral level has multiplicity four. The constant function contributes the additional eigenvalue \(1\).

## Assumptions and scope
All strings and domain-wall subsets are labelled and the measure on \(\Omega_n\) is uniform. The cyclic edges are \((j,j+1\bmod n)\). The number of walls is exactly half the number of edges; \(n\) is a positive multiple of four. The Gram matrix is \(G_{uv}=\mathbb E_{\Omega_n}[f_u\overline{f_v}]\), not the unnormalized sum over observations. The beta function is \(\mathrm B(a,b)=\int_0^1 t^{a-1}(1-t)^{b-1}\,dt\) for positive arguments. Equal spectral values mentioned here are counted with algebraic multiplicity.

## Proof
**Cyclic covariance.** A wall set \(W\subset\mathbb Z_n\) of cardinality \(m\), together with the sign at one vertex, uniquely determines a cyclic spin string because \(m\) is even. Thus there are \(2\binom nm\) equally weighted samples. Spin reversal gives \(\mathbb E[\chi_j]=0\), making the constant mode orthogonal to the coordinate block. Let \(Y_e=(-1)^{\mathbf 1_{\{e\in W\}}}\). Exactly half these edge signs are positive and half negative, hence \(\sum_eY_e=0\) deterministically. Put \(c_t=\mathbb E[\chi_0\chi_t]\) for \(0\le t<n\); this equals the expected product of any \(t\) distinct edge signs. Complementing \(W\) shows \(c_t=0\) when \(t\) is odd. Multiplying \(\sum_eY_e=0\) by the product over a specified \(t\)-subset and taking expectations yields
\[
 t c_{t-1}+(n-t)c_{t+1}=0\qquad(1\le t<n),\qquad c_0=1.
\]
Therefore for \(0\le j\le m\),
\[
c_{2j}=(-1)^ja_j=(-1)^j\frac{\mathrm B(j+1/2,m-j+1/2)}{\mathrm B(1/2,m+1/2)}.
\]
The product formula follows by the recurrence, and the beta identity follows from the gamma-function recurrence. In particular \(c_{2j}=c_{n-2j}\). The coordinate Gram block is real symmetric circulant: \(G_{ij}=c_{j-i\bmod n}\).

**A positive mixture of Poisson kernels.** Circulant Fourier diagonalization gives
\[
\lambda_\ell=\sum_{j=0}^{m-1}(-1)^ja_j\exp(-2\pi i\ell j/m).
\]
Substitute \(r=u/(1-u)\) into the beta integral and split at \(r=1\). For \(0\le j<m\), inversion in the upper half gives
\[
a_j=\frac{1}{\mathrm B(1/2,m+1/2)}\int_0^1\frac{r^{-1/2}\bigl(r^j+r^{m-j}\bigr)}{(1+r)^{m+1}}\,dr.
\]
For every \(0<r<1\) and \(z^m=1\), the *finite* geometric identity is
\[
\sum_{j=0}^{m-1}(r^j+r^{m-j})z^j
=\frac{(1-r^m)(1-r^2)}{1-2r\operatorname{Re}(z)+r^2}.
\]
Because \(m\) is even, \(z=-\exp(-2\pi i\ell/m)\) obeys \(z^m=1\). Inserting this \(z\) proves the displayed integral formula exactly. Its integrand is positive for \(0<r<1\), and its only angular dependence occurs through a denominator strictly *increasing* with \(\cos(4\pi\ell/n)\). This proves positivity, strict spectral ordering, all extremizing modes, and the stated multiplicities. The proof does not infer infinite positivity from finite experiments.

**Exact extremes.** At \(\ell=n/4\), all phase factors align with \((-1)^j\), and symmetry \(a_j=a_{m-j}\) gives the finite-sum expression for \(\lambda_{\max}\). For \(\ell=0\), use the wall-subset generating function
\[
\sum_{t=0}^{n-1}(1-u)^t(1+u)^{n-t}=\frac{(1+u)\big((1+u)^n-(1-u)^n\big)}{2u}.
\]
Taking the coefficient of \(u^m\), with \(m\) even, and dividing by \(\binom nm\) yields \(\lambda_0=\binom n{m+1}/\binom nm=n/(n+2)\). As the mean of the \(n\) coordinate eigenvalues equals \(1\), strict ordering implies \(\lambda_{\min}<1<\lambda_{\max}\); including the constant mode does not change the extreme values. Thus the condition-number formula is exact.

**Large-order estimate.** The product coefficients obey \(a_1=1/(n-1)\), \(a_2=3/((n-1)(n-3))\), and \(a_{j+1}/a_j=(2j+1)/(n-2j-1)\). For \(2\le j\le\lfloor n/8\rfloor\) this ratio is uniformly bounded away from one for sufficiently large \(n\); for \(\lfloor n/8\rfloor\le j\le n/4\), the coefficients continue decreasing and are exponentially small compared with \(a_2\). Consequently \(\sum_{j=2}^{n/4}a_j=O(n^{-2})\). Hence \(\lambda_{\max}=1+2/(n-1)+O(n^{-2})\). Multiplication by \((n+2)/n\) yields \(\kappa_n^2=1+4/n+O(n^{-2})\), with the asymptotic along multiples of four.

## Verification
The accompanying standalone `check.py` uses only Python's standard library. Running `python check.py` verifies the exact hypergeometric and recurrence moments for multiples of four through \(128\), the predicted Fourier extrema and strict ordering, direct independent enumeration of all wall sets at \(n=4,8,12,16\), and the beta integral against independently computed eigenvalues for representative frequencies. It also checks asymptotic behavior for four larger instances. Its passing output is `PASS 220411 assertion groups/weighted enumerated moments`; the number includes individually counted moment cases and does not purport to be independent proofs. Reproducibility requires Python 3.10 or later. The analytic beta-mixture argument, not computation, proves the universal statement.

## Relationship to prior work
Antal, Droz, and Rácz give the finite periodic Ising spin-correlation function for a *canonical* temperature ensemble and analyze magnetization distributions and fixed-wall sectors. In particular their periodic correlation formula can be expanded to recover fixed-wall two-point moments; these elementary moments are not claimed as new. Denisov and Hänggi study finite-chain wall statistics under free boundary conditions. The present result concerns the *balanced microcanonical cyclic shell* and gives a positive Poisson-kernel mixture, a strict ordering of every spatial Fourier mode, all sharp reconstruction extremizers, and an exact squared condition number. None of those ordering or sharp frame-conditioning statements was found in the inspected primary material. Broader equivalences through classical Krawtchouk transforms or statistical-mechanical structure factors remain a historical risk.

## Limitations
The theorem assumes uniform weights, exactly \(n/2\) domain walls, and \(4\mid n\); it does not characterize unequal wall densities or arbitrary positive reweightings. Its sharpness concerns the first-coordinate Fourier sampling band, not all higher-order Walsh characters. The originality assessment is bounded by the inspected literature and is not an independent audit.

## References
- T. Antal, M. Droz, and Z. Rácz, *Probability distribution of magnetization in the one-dimensional Ising model: Effects of boundary conditions*, arXiv:cond-mat/0308442 (first posted 2003-08-21), especially Secs. II and IV, Eq. (3).
- S. I. Denisov and P. Hänggi, *Domain statistics in a finite Ising chain*, Physical Review E 71 (2005), 046137, DOI:10.1103/PhysRevE.71.046137; accessible arXiv version cond-mat/0603417 (posted 2006-03-15).
