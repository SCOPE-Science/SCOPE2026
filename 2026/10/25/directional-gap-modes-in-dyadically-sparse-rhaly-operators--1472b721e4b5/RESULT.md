# Directional gap modes in dyadically sparse Rhaly operators

## Finding

For any \(u,v>0\), a two-periodically modulated dyadic Rhaly matrix has a completely explicit singular-operator spectrum. Put
\[
A=\frac3{u^2},\quad B=\frac3{v^2},\quad t=\frac{\sqrt2}{uv},\quad
L=\frac{A+B-\sqrt{(A-B)^2+16t^2}}2,\quad
U=\frac{A+B+\sqrt{(A-B)^2+16t^2}}2.
\]
Then \(0<L<\min(A,B)\le\max(A,B)<U\), and the positive part of the spectrum of \(|R|=(R^*R)^{1/2}\) is exactly
\[
\left[\frac1{\sqrt U},\frac{\min(u,v)}{\sqrt3}\right]
\cup
\left[\frac{\max(u,v)}{\sqrt3},\frac1{\sqrt L}\right]
\cup E_{u,v},
\]
where \(E_{u,v}=\{uv/\sqrt{2v^2+u^2}\}\) for \(u<v\), and \(E_{u,v}=\varnothing\) for \(u\ge v\). When \(u<v\), the isolated point is a simple eigenvalue strictly between the two bands. When \(u>v\), the open band gap is empty; when \(u=v\), the bands touch. Every band point is essential spectrum, with no nonzero eigenvalues in the bands. The point \(0\) is an eigenvalue of infinite multiplicity. In particular,
\[
\|R\|=\|R\|_{\mathrm{ess}}=L^{-1/2},\qquad
\|R\|\big|_{u=v=b}=b(1+\sqrt2).
\]
The bulk bands are invariant under interchanging \(u\) and \(v\), while the localized gap mode is not.

## Assumptions and scope

Take \(H=\ell^2(\mathbb N_0)\) with standard basis \((e_m)_{m\ge0}\). The Rhaly (terraced) matrix is initially defined on finitely supported vectors by
\[
(Rx)_m=\eta_m\sum_{j=0}^{m}x_j,
\quad
\eta_{2^k-1}=2^{-k/2}b_k,\quad
b_{2j}=u,\quad b_{2j+1}=v\quad(j,k\ge0),
\]
and \(\eta_m=0\) at all other indices. The theorem proves this matrix extends boundedly to \(H\). Zero coefficients are intentional: the operator is sparse and not covered by hypotheses demanding strictly positive coefficients. Here the “singular spectrum” means the full operator spectrum of \(|R|\), not a list of discrete approximation numbers (the operator is not compact).

## Proof

**1. Bounded row Gram and invertibility on the active output.** For each \(k\ge0\) let
\[
f_k=2^{-k/2}\sum_{j=0}^{2^k-1}e_j,\qquad a=2^{-1/2}.
\]
The nonzero row at output \(m=2^k-1\) is \(b_k f_k^*\), and the exact inner products are
\[
\langle f_k,f_l\rangle=2^{-|k-l|/2}=a^{|k-l|}.
\]
Thus on the active output \(E=\overline{\operatorname{span}}\{e_{2^k-1}:k\ge0\}\), the row Gram \(RR^*\) is unitarily identified with
\[
K=D_bT_aD_b,\quad (T_a)_{kl}=a^{|k-l|},\quad D_b=\operatorname{diag}(b_0,b_1,\ldots).
\]
The covariance matrix \(T_a\) is bounded, positive and boundedly invertible: its inverse (verified by multiplying the tridiagonal matrix with \(T_a\) on finitely supported columns and extending by boundedness) is
\[
T_a^{-1}=\frac1{1-a^2}
\begin{pmatrix}
1&-a&0&\cdots\\
-a&1+a^2&-a&\ddots\\
0&-a&1+a^2&\ddots\\
\vdots&\ddots&\ddots&\ddots
\end{pmatrix}.
\]
For example positivity and invertibility also follow from its Fourier symbol \((1-a^2)/(1-2a\cos\theta+a^2)\), which is uniformly bounded above and below by positive constants. Since \(D_b\) is positive and boundedly invertible, \(K\) is likewise. Hence the row family is Bessel, and the initially defined \(R\) extends boundedly. Its restriction \(RR^*|_E\) is \(K\), and the nonzero spectra of \(|R|\) and \(K^{1/2}\) agree with multiplicities, by polar decomposition. Also, \(R^*R\) vanishes on \(\ker R\).

**2. Exact half-line periodic Jacobi reduction.** The inverse \(J=K^{-1}=D_b^{-1}T_a^{-1}D_b^{-1}\) has first diagonal entry \(d_0=2/u^2\); thereafter its diagonal is \(A=3/u^2\) at even sites and \(B=3/v^2\) at odd sites. Every upper and lower off-diagonal entry equals \(-t=-\sqrt2/(uv)\). Thus \(J\) is a positive bounded Jacobi operator with a period-two tail and one exceptional boundary diagonal. Its spectrum is contained in a fixed positive interval because \(K\) is boundedly invertible.

**3. The bulk bands.** The two-site Bloch fiber of the bilateral periodic continuation of the tail has diagonal \(A,B\) and off-diagonal \(-t(1+e^{i\theta})\). Its eigenvalues are
\[
\lambda_{\pm}(\theta)=\frac{A+B\pm\sqrt{(A-B)^2+16t^2\cos^2(\theta/2)}}2.
\]
Consequently, the periodic bulk spectrum is exactly
\[
\Sigma=[L,\min(A,B)]\cup[\max(A,B),U].
\]
Every point of \(\Sigma\) belongs to the essential spectrum of the half-line operator \(J\): truncate a bounded Bloch wave far down the periodic tail and normalize to obtain a weakly null Weyl sequence. Conversely, outside \(\Sigma\), the two-step transfer matrix has reciprocal real multipliers with one of modulus less than one; its growing and decaying solutions yield a Fredholm half-line recurrence with at most a one-dimensional boundary obstruction. This is the elementary Floquet/exponential-dichotomy argument and rules out additional continuous spectrum. Inside a band the Bloch multipliers have modulus one, and at the edges the only generalized solutions are bounded or grow polynomially; no nonzero solution lies in \(\ell^2\). Thus any spectrum outside \(\Sigma\) must be a simple eigenvalue.

**4. Exact boundary-mode calculation.** At any real \(\lambda\notin\Sigma\), a square-summable nonzero solution has the form
\[
x_{2k}=r^k x_0,\qquad x_{2k+1}=yr^k x_0,\qquad |r|<1.
\]
The boundary equation is \((2/u^2-\lambda)x_0-tx_1=0\). Comparing it with the periodic even-site recurrence gives
\[
y=\frac{2/u^2-\lambda}{t},\qquad r=u^2(2/u^2-\lambda)=2-u^2\lambda.
\]
The odd-site recurrence then gives \((B-\lambda)r=u^2t^2(1+r)\). Substitution and multiplication by \(u^2\) yield the *exact* polynomial constraint
\[
(u^2\lambda)\big(u^2\lambda-(2+u^2/v^2)\big)=0.
\]
Since \(J\) is boundedly invertible and strictly positive, \(\lambda=0\) is excluded. The only candidate is
\[
\lambda_*=\frac2{u^2}+\frac1{v^2},\qquad
r_*=-\frac{u^2}{v^2},\qquad
 y_*=-\frac{u}{\sqrt2\,v}.
\]
The corresponding explicit vector
\[
x_{2k}=\left(-\frac{u^2}{v^2}\right)^k,\qquad
x_{2k+1}=-\frac{u}{\sqrt2\,v}\left(-\frac{u^2}{v^2}\right)^k
\]
belongs to \(\ell^2\) if and only if \(u<v\). In that case \(\lambda_*\) lies strictly between \(\min(A,B)\) and \(\max(A,B)\); direct substitution verifies the eigen-equation at every site. If \(u>v\), the candidate grows, so the gap contains no spectrum. At \(u=v\) the multiplier equals \(-1\) and is not square-summable. The second-order recurrence shows simplicity.

**5. Inverting the spectrum and zero.** Spectral mapping for the positive invertible \(K=J^{-1}\) transforms \(\lambda\mapsto\lambda^{-1/2}\). This yields precisely the two displayed positive bands and the edge singular value \(\lambda_*^{-1/2}=uv/\sqrt{2v^2+u^2}\). Because \(\Sigma\) is essential, both singular bands are essential. The largest positive spectral point is \(L^{-1/2}\), which therefore equals both the norm and essential norm of \(R\). Finally, all vectors \(e_{2^k}-e_{2^k+1}\) for \(k\ge1\) lie in \(\ker R\) and are mutually orthogonal; hence \(0\) has infinite multiplicity in \(|R|\). If \(u=v=b\), substituting into \(L\) gives \(L^{-1/2}=b(1+\sqrt2)\).

## Verification

The accompanying `verify.py` uses only the Python standard library. Execute `python verify.py`; it verifies exact finite covariance inverse identities, the boundary and periodic recurrence of the candidate eigenvector over rational parameter pairs, dyadic Gram coefficients against explicit matrix rows, and sample spectral-edge relations. These tests are finite supplementary checks and are **not** used as substitutes for the above infinite-dimensional Floquet and spectral-mapping arguments.

## Relationship to prior work

Bellavita, Dellepiane and Stylogiannis [1] develop boundedness, compactness and Schatten properties for weighted Hardy-space Rhaly/factorable operators and expose the natural role of dyadic blocking. Their earlier work [2] obtains Rhaly Schatten membership classifications. Neither inspected treatment supplies the present exact singular spectral bands, the asymmetry of the boundary gap state, or the sharp essential norm for the two-periodic dyadic-row family. Classical periodic Jacobi/Floquet theory supplies the spectral machinery; the explicitly inverted sparse Rhaly Gram, unusual first boundary coefficient, and directional gap test are the family-specific calculations. Spectral investigations of factorable triangular matrices [3] concern the original operator spectrum, which is different from the singular spectrum of \(|R|\).

## Limitations

The theorem concerns dyadically supported Rhaly coefficients with strictly positive two-periodic sampled amplitudes; it does not classify other supports, arbitrary modulation periods, or the spectrum of \(R\) itself. It proves exact infinite-dimensional singular spectra, not an approximation-number list. Publication priority remains subject to checking older unindexed Jacobi, lacunary Cesàro, and factorable-matrix literature, including full texts that were not available. No independent validation has been performed.

## References

[1] C. Bellavita, E. Dellepiane, G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875 (first posted 2026-06-14). https://arxiv.org/abs/2606.15875

[2] C. Bellavita, E. Dellepiane, G. Stylogiannis, *Schatten class for Rhaly matrices and spaces of analytic functions*, arXiv:2503.21930 (first posted 2025-03-27); journal version *Boundedness, compactness and Schatten class for Rhaly matrices*, DOI:10.1112/jlms.70304.

[3] B. E. Rhoades and M. Yıldırım, *Spectra for factorable matrices on \(\ell_p\)*, Integral Equations and Operator Theory 55 (2006), 111–126, DOI:10.1007/s00020-005-1383-3 (abstract consulted).
