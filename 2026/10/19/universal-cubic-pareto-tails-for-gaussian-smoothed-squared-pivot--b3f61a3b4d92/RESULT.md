# Universal cubic Pareto tails for Gaussian-smoothed squared-pivot randomized LU

## Finding
Let \(m,n\ge 2\). For a real \(m\)-by-\(n\) matrix \(A\) whose entries are independent standard Gaussians, perform one step of exact randomly pivoted LU (RPLU): conditionally on \(A\), choose a pivot \((I,J)\) with probability \(|A_{ij}|^2/\|A\|_F^2\) and retain the Schur complement \(R\) outside pivot row and column. Put \(Z=\|R\|_F\). Then the tail has the exact asymptotic
\[
\lim_{t\to\infty}t^3\Pr(Z>t)=C_{m,n}
=\frac{16mn}{3(mn+3)\sqrt{2\pi}}
\frac{\Gamma((m+2)/2)}{\Gamma((m-1)/2)}
\frac{\Gamma((n+2)/2)}{\Gamma((n-1)/2)}>0.
\]
More generally, for **every deterministic** real \(m\)-by-\(n\) matrix \(B\) and every \(\sigma>0\), if \(A=B+\sigma G\) with independent standard-normal entries in \(G\), then the *same sharp tail exponent* holds:
\[
\lim_{t\to\infty}t^3\Pr(\|R\|_F>t)=C(B,\sigma)\in(0,\infty).
\]
For each candidate pivot \((i,j)\), partition the complementary random entries into pivot-column vector \(u_{ij}\), pivot-row vector \(v_{ij}\), and remaining block \(W_{ij}\), and define \(S_{ij}=\|u_{ij}\|_2^2+\|v_{ij}\|_2^2+\|W_{ij}\|_F^2\). Then the exact (generally noncentral) coefficient is
\[
C(B,\sigma)=\frac{2}{3\sigma\sqrt{2\pi}}
\sum_{i=1}^{m}\sum_{j=1}^{n}e^{-B_{ij}^2/(2\sigma^2)}
\mathbb E\left[\frac{(\|u_{ij}\|_2\|v_{ij}\|_2)^3}{S_{ij}}\right].
\]
In particular, **arbitrarily small independent Gaussian entry noise** suffices to produce this cubic tail, even when the underlying matrix is deterministic, and \(C(0,\sigma)=\sigma^3 C_{m,n}\). The centered formula above is its closed gamma-function specialization.

Consequently, for every real \(q>0\),
\[
\mathbb E Z^q<\infty\quad\Longleftrightarrow\quad 0<q<3.
\]
In the minimal \(2\)-by-\(2\) case, \(C_{2,2}=64/(21\pi\sqrt{2\pi})\). The unconditional second moment is nevertheless finite and equals
\[
\mathbb E Z^2=\frac{2m(m-1)n(n-1)}{mn+2}.
\]
The second-moment identity is included as a consistency check and is implied by the established one-step RPLU squared-residual identity, not presented as the new contribution. For contrast, complete-largest-entry pivoting on the same Gaussian input has finite residual moments of every positive order.

## Assumptions and scope
For the general theorem \(A=B+\sigma G\) with any deterministic \(B\in\mathbb R^{m\times n}\), any fixed \(\sigma>0\), and independent \(N(0,1)\) entries in \(G\), with fixed integers \(m,n\ge2\). The gamma-function coefficient and mean-square formula specialize to \(B=0,\sigma=1\). All expectations average jointly over the Gaussian input and the random pivot. Pivoting uses exactly the entry-square probabilities in the original RPLU rule; there are no repeated pivots, approximations, or finite-precision effects. An all-zero matrix and a zero selected pivot each have probability zero. The Schur complement \(R\in\mathbb R^{(m-1)\times(n-1)}\) is the unselected block after subtracting the pivot-column/pivot-row outer product divided by the pivot. No full factorization or multi-step assertion is made.

## Proof
**1. Reduce the centered tail to a single size-biased pivot.** By exchangeability of the independent Gaussian entries and invariance of the Frobenius norm under row and column permutations, sum over all \(mn\) possible pivots and fix pivot \((1,1)\). Partition
\[
A=\begin{pmatrix}X&v^{\mathsf T}\u&W\end{pmatrix},\qquad
S=\|u\|_2^2+\|v\|_2^2+\|W\|_F^2,\qquad h=\|u\|_2\|v\|_2,
\]
where \(X\sim N(0,1)\) is independent of \((u,v,W)\). The residual for this pivot is \(W-uv^{\mathsf T}/X\). With \(\varphi\) the standard normal density,
\[
\Pr(Z>t)=mn\,\mathbb E_{u,v,W}\!\left[\int_{\mathbb R}
\varphi(x)\frac{x^2}{x^2+S}
\mathbf 1\!\left\{\left\|W-\frac{uv^{\mathsf T}}x\right\|_F>t\right\}\,dx\right].
\]
In particular, the pivot-selection weight is inside the integral. Treating the pivot as an unweighted independent Gaussian would give an incorrect exponent.

**2. Identify and justify the exact tail coefficient.** Write \(w=\|W\|_F\). The reverse triangle inequality gives
\[
\left|\left\|W-\frac{uv^{\mathsf T}}x\right\|_F-\frac h{|x|}\right|\le w.
\]
For each fixed \((u,v,W)\) with \(h,S>0\) and \(t>w\), the event in the preceding integral is squeezed between \(\{|x|<h/(t+w)\}\) and \(\{|x|<h/(t-w)\}\). Hence
\[
\lim_{t\to\infty}t^3\int_{\mathbb R}
\varphi(x)\frac{x^2}{x^2+S}
\mathbf 1\!\left\{\left\|W-\frac{uv^{\mathsf T}}x\right\|_F>t\right\}\,dx
=\frac{2\varphi(0)}3\frac{h^3}{S}.
\]
This limit may be integrated: on \(w\le t/2\), the integral is at most
\(16\varphi(0)h^3/(3St^3)\), while the discarded part \(w>t/2\) contributes at most \(\Pr(w>t/2)=o(t^{-3})\). The random dominating factor is integrable because \(h\le (\|u\|^2+\|v\|^2)/2\le S/2\), so \(h^3/S\le S^2/8\) and \(S\) is chi-squared with finite moments. Thus
\[
\lim_{t\to\infty}t^3\Pr(Z>t)
=\frac{2mn}{3\sqrt{2\pi}}\,\mathbb E\frac{h^3}{S}.
\]

**2a. Generalize the tail to arbitrary Gaussian-smoothed inputs.** For each possible \((i,j)\), isolate the pivot \(X_{ij}\sim N(B_{ij},\sigma^2)\), independent of its complement. Write the complement as \(u_{ij},v_{ij},W_{ij}\), with \(h_{ij}=\|u_{ij}\|_2\|v_{ij}\|_2\), \(S_{ij}=\|u_{ij}\|_2^2+\|v_{ij}\|_2^2+\|W_{ij}\|_F^2\), and \(w_{ij}=\|W_{ij}\|_F\). Replace \(\varphi(x)\) in Step 2 by the density \(f_{ij}(x)\) of \(X_{ij}\). The same squeeze gives \(2f_{ij}(0)h_{ij}^3/(3S_{ij})\) for the individual weighted-pivot tail coefficient; no exchangeability is needed. The density is bounded by \(1/(\sigma\sqrt{2\pi})\), and the previous domination with \(h_{ij}^3/S_{ij}\le S_{ij}^2/8\) still applies; each noncentral Gaussian \(S_{ij}\) has finite second moment. The discarded \(w_{ij}>t/2\) probability decreases faster than any polynomial. Sum the finitely many candidate-pivot terms to obtain the displayed \(C(B,\sigma)\). For \(m,n\ge2\), both \(u_{ij}\) and \(v_{ij}\) are nonempty random Gaussian vectors, so every summand is strictly positive and finite. Scaling proves \(C(0,\sigma)=\sigma^3 C_{m,n}\).

**3. Evaluate the expectation without an asymptotic approximation.** Let \(a=m-1\), \(b=n-1\), \(c=(m-1)(n-1)\) and \(D=a+b+c=mn-1\). The variables \(U=\|u\|^2\), \(V=\|v\|^2\), \(H=\|W\|_F^2\) are independent chi-squared variables with degrees of freedom \(a,b,c\). Their sum \(S\sim\chi_D^2\) is independent of the Dirichlet proportions \((U/S,V/S,H/S)\), with parameters \((a/2,b/2,c/2)\). Therefore
\[
\begin{aligned}
\mathbb E\frac{h^3}{S}
&=\mathbb E S^2\cdot\mathbb E\left[\left(\frac US\right)^{3/2}\left(\frac VS\right)^{3/2}\right]\
&=D(D+2)\frac{\Gamma(D/2)}{\Gamma(D/2+3)}
\frac{\Gamma((a+3)/2)}{\Gamma(a/2)}
\frac{\Gamma((b+3)/2)}{\Gamma(b/2)}\
&=\frac8{D+4}
\frac{\Gamma((m+2)/2)}{\Gamma((m-1)/2)}
\frac{\Gamma((n+2)/2)}{\Gamma((n-1)/2)}.
\end{aligned}
\]
Substitute \(D+4=mn+3\) into the coefficient of Step 2 to obtain \(C_{m,n}\).

**4. Moment frontier.** For any nonnegative random variable and \(q>0\), the layer-cake identity yields \(\mathbb E Z^q=q\int_0^\infty t^{q-1}\Pr(Z>t)\,dt\). The proved positive cubic tail (both for centered inputs and for every Gaussian-smoothed deterministic input) makes this finite precisely for \(q<3\), with logarithmic divergence at \(q=3\).

**5. Check the mean square and contrast complete pivoting.** Conditionally on any fixed input \(A\ne0\), the entry-square weight cancels the denominator in the Schur-complement sum. Each squared \(2\)-by-\(2\) minor occurs in four oriented positions, so
\[
\mathbb E[Z^2\mid A]=\frac4{\|A\|_F^2}
\sum_{i<k}\sum_{j<\ell}\left(A_{ij}A_{k\ell}-A_{i\ell}A_{kj}\right)^2.
\]
This is the one-step squared-residual identity underlying published RPLU estimates. For a Gaussian matrix, each determinant square has mean \(2\). Each is homogeneous of degree four in the \(mn\) Gaussian coordinates, and radial independence gives \(\mathbb E[\det^2/\|A\|_F^2]=\mathbb E[\det^2]/(mn+2)\). Summing gives the displayed unconditional mean square. Under largest-entry (complete) pivoting, all entries of \(u,v\) have magnitude at most \(|X|\) in the analogous pivoted partition, so
\[
\|R\|_F\le\|W\|_F+\frac{\|u\|\|v\|}{|X|}
\le\bigl(1+\sqrt{(m-1)(n-1)}\bigr)\|A\|_F.
\]
A Gaussian input has all finite norm moments, proving the stated contrast.

## Verification
Run `python reproduce.py` with Python 3, NumPy, and SciPy installed. The program checks the exact coefficient in the \(2\)-by-\(2\) case, independently evaluates the chi-square/Dirichlet factor, checks the deterministic oriented-minor identity on multiple rectangular matrices, compares Monte Carlo second moments with their closed forms, and estimates scaled tails for three matrix sizes. Monte Carlo checks are finite corroboration only; the proof of all dimensions, arbitrary deterministic means and Gaussian smoothing, the infinite tail asymptotic, and moment divergence are the analytic arguments above.

## Relationship to prior work
Gilles and Wilber introduced squared-entry RPLU and derived its conditional expected squared-error bounds (arXiv:2601.22344v1, first public 2026-01-29), including the one-step Gram-matrix identity. Divan and Gilles analyzed approximate pivot distributions and spectral convergence through determinant identities (arXiv:2609.06287v1, first public 2026-09-05). Those findings treat fixed inputs with randomness in pivot selection; for each fixed finite input their one-step pivot support makes every finite residual moment finite. The present result instead jointly randomizes the input and the pivot, and derives a universal sharp cubic tail for any deterministic input with nondegenerate independent Gaussian entry perturbations, including a closed constant for centered inputs. Spielman and Yu's Gaussian-matrix growth lower bounds concern standard partial pivoting, not squared-entry RPLU (arXiv:2610.08701v1, first public 2026-10-06). The result does not follow from the cited expected-square estimates alone, which cannot decide third-moment integrability.

## Limitations
The theorem addresses only one step and independent additive real Gaussian perturbations with common positive standard deviation; the closed gamma constant additionally assumes a zero underlying matrix. It does not give a distribution-free arbitrary-input tail bound, a multi-step convergence rate, a high-probability relative-error guarantee, or a finite-precision growth theorem. The moment failure is **unconditional over random matrices**, not conditional on a fixed nonzero matrix. Unindexed equivalent results remain a literature-search risk; the stated mathematical conclusions have not undergone an independent external audit.

## References
1. M. A. Gilles and H. Wilber, *Low-Rank Approximation by Randomly Pivoted LU*, arXiv:2601.22344v1 (2026-01-29), https://arxiv.org/abs/2601.22344.
2. R. Divan and M. A. Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation*, arXiv:2609.06287v1 (2026-09-05), https://arxiv.org/abs/2609.06287.
3. D. A. Spielman and X. Yu, *Large Growth Happens: Gaussian Elimination with Partial Pivoting on Random Matrices*, arXiv:2610.08701v1 (2026-10-06), https://arxiv.org/abs/2610.08701.
