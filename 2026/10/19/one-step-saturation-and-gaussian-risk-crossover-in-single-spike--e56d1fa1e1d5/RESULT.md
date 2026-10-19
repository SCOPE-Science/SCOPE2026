# One-step saturation and Gaussian risk crossover in single-spike sketch-power rangefinding

## Finding

Fix a real number \(c>0\) and an integer \(\ell\ge2\). For each integer \(n>\ell\), let
\[
A_n=\operatorname{diag}(\sqrt{cn},1,\ldots,1)\in\mathbb R^{n\times n},
\]
and take two independent real standard-Gaussian sketches \(\omega_n\in\mathbb R^n\) and \(\Phi_n\in\mathbb R^{n\times\ell}\). Define \(Y_n=A_n\omega_n\), \(Z_n=A_n\Phi_n\), and the normalized sketch-power rangefinders
\[
v_{n,0}=\frac{Y_n}{\|Y_n\|_2},\qquad
v_{n,q}=\frac{(Z_nZ_n^{\mathsf T})^qY_n}{\|(Z_nZ_n^{\mathsf T})^qY_n\|_2},\quad q\in\{1,2,\ldots\}.
\]
All denominators are nonzero almost surely. Let \(e_1\) be the distinguished spike direction (the principal singular direction when \(cn>1\)), \(a_{n,q}=|e_1^{\mathsf T}v_{n,q}|^2\) its captured squared alignment, and \(p_n=\|P_{\operatorname{range}(Z_n)}e_1\|_2^2\) the best possible capture inside the auxiliary sketch range.

**Exact finite-dimensional ceiling.** For every \(n>\ell\),
\[
\boxed{\quad p_n\ \overset{d}{=}\ \frac{cnX_\ell}{V_{n-\ell}+cnX_\ell}\quad}
\]
where \(X_\ell\sim\chi^2_\ell\) and \(V_{n-\ell}\sim\chi^2_{n-\ell}\) are independent.

**Uniform one-step saturation.** For fixed \(c,\ell\),
\[
\boxed{\quad\sup_{q\ge1}|a_{n,q}-p_n|\xrightarrow{\mathbb P}0\quad(n\to\infty).\quad}
\]
The supremum is over every positive integer, without an upper bound on the number of sketch-power steps. Moreover, jointly,
\[
\boxed{\quad(a_{n,0},a_{n,q_n})\xrightarrow{d}
\left(\frac{cH}{1+cH},\frac{cX_\ell}{1+cX_\ell}\right)\quad}
\]
for **every** possibly sketch-dependent integer sequence \(q_n\ge1\), with independent \(H\sim\chi^2_1\) and \(X_\ell\sim\chi^2_\ell\).

**Exact comparison of two independent sketches.** In particular,
\[
\boxed{\quad\lim_{n\to\infty}\mathbb P(a_{n,q_n}>a_{n,0})
=\mathbb P(X_\ell>H)
=1-I_{1/2}(\ell/2,1/2).\quad}
\]
For the smallest eligible auxiliary width \(\ell=2\), this probability is \(1/\sqrt2\). Thus, even though sketch-power improves *expected* alignment, in the specified independent-sketch scheme its limiting probability of making alignment worse is \(1-1/\sqrt2\) when \(\ell=2\).

Finally let \(R_{n,q}=\|(I-v_{n,q}v_{n,q}^{\mathsf T})A_n\|_2^2/(cn)\) be normalized squared **spectral** error of the rank-one *orthogonal range projection*, not the error of a separately reconstructed oblique factor. For every \(n>\ell\) and \(q\ge0\),
\[
1-a_{n,q}\ \le R_{n,q}\ \le1-a_{n,q}+\frac1{cn}.
\]
Consequently, for arbitrary \(q_n\ge1\),
\[
R_{n,q_n}\xrightarrow{d}\frac1{1+cX_\ell},\qquad
R_{n,0}\xrightarrow{d}\frac1{1+cH},
\]
and their expectations converge to the corresponding distributional expectations. For each \(\ell\ge2\), the former expected limit is strictly smaller than the latter.

## Assumptions and scope

The results concern exact real arithmetic, a square diagonal positive matrix, a single initial Gaussian test vector, and an independent \(n\times\ell\) auxiliary Gaussian sketch. The auxiliary width \(\ell\ge2\) and spike scale \(c>0\) remain fixed while \(n\to\infty\). The claim includes all positive integer step counts at once. It does not assume a deterministic step count; the uniform conclusion also covers adaptive choices.

The spike singular value is \(\sqrt{cn}\), exactly on the critical scale at which a fixed-width Gaussian rangefinder retains nontrivial random alignment with the leading direction. The algorithm here analyzes the rangefinder \((ZZ^{\mathsf T})^qY\) itself, without a downstream two-sided/oblique coefficient reconstruction.

## Proof

**1. Finite-dimensional projector law.** Write the first row of \(\Phi_n\) as \(g^{\mathsf T}\in\mathbb R^{1\times\ell}\), and write the remaining \(n-1\) rows as \(B\). Then
\[
Z_n=\begin{pmatrix}\sqrt{cn}\,g^{\mathsf T}\\B\end{pmatrix},\qquad
W=B^{\mathsf T}B,\qquad Z_n^{\mathsf T}Z_n=W+cn\,gg^{\mathsf T}.
\]
For \(n>\ell\), \(W\) is positive definite almost surely. Writing \(t=g^{\mathsf T}W^{-1}g\), the Sherman–Morrison identity gives
\[
p_n=(cn)\,g^{\mathsf T}(W+cn\,gg^{\mathsf T})^{-1}g
=\frac{cn\,t}{1+cn\,t}.
\]
By rotational invariance in \(\mathbb R^\ell\), conditional on \(g\) rotate the columns of \(B\) so that \(g=\|g\|_2e_1\). Partition this rotated \(B\) into its first column and the other \(\ell-1\) columns. The reciprocal of the \((1,1)\) entry of \(W^{-1}\) is the squared norm of the first column after orthogonal projection away from the other columns; it has the \(\chi^2_{n-\ell}\) law, independently of \(g\). Since \(\|g\|_2^2\sim\chi^2_\ell\), it follows that \(t\overset d=X_\ell/V_{n-\ell}\) with independent chi-square variables. This proves the exact law.

**2. Reduction of every power to a fixed-width symmetric matrix.** Write the first coordinate of \(\omega_n\) as \(h\), and the remaining coordinates as \(\xi\). Define
\[
K_n=\frac{Z_n^{\mathsf T}Z_n}{n}=\frac{B^{\mathsf T}B}{n}+cgg^{\mathsf T},\qquad
w_n=\frac{Z_n^{\mathsf T}Y_n}{n}=cgh+\frac{B^{\mathsf T}\xi}{n}.
\]
Since \(\ell\) is fixed and the Gaussian rows are independent, the law of large numbers and second moments give the joint convergence
\[
K_n-(I_\ell+cgg^{\mathsf T})\xrightarrow{\mathbb P}0,
\qquad w_n-cgh\xrightarrow{\mathbb P}0.
\]
These convergences can be realized under a coupling in which \(g,h\) do not vary with \(n\), and the additional Gaussian rows are taken from independent infinite sequences. With this coupling, \(g\ne0\) and \(h\ne0\) almost surely.

The limiting matrix \(K=I_\ell+cgg^{\mathsf T}\) has a simple largest eigenvalue \(1+c\|g\|_2^2>1\), eigenvector \(g/\|g\|_2\), and all remaining eigenvalues equal to \(1\). Let \(u_n\) be a unit top eigenvector of \(K_n\), chosen with \(g^{\mathsf T}u_n\ge0\), and decompose
\[
w_n=\alpha_nu_n+b_n,\qquad b_n\perp u_n.
\]
The spectral gap and the preceding convergences yield \(u_n\to g/\|g\|_2\), \(\alpha_n\to c\|g\|_2h\ne0\), and \(\|b_n\|_2\to0\), almost surely under this coupling. Denote the two largest eigenvalues of \(K_n\) by \(\lambda_{1,n}\ge\lambda_{2,n}\). Then for **every** integer \(q\ge1\),
\[
\frac{\|K_n^{q-1}b_n\|_2}{|\alpha_n|\lambda_{1,n}^{q-1}}
\le\frac{\|b_n\|_2}{|\alpha_n|}
\left(\frac{\lambda_{2,n}}{\lambda_{1,n}}\right)^{q-1}
\le\frac{\|b_n\|_2}{|\alpha_n|}\longrightarrow0.
\]
The identity \((Z_nZ_n^{\mathsf T})^qY_n=Z_n(nK_n)^{q-1}(nw_n)\) shows that the rangefinder direction is the image of \(K_n^{q-1}w_n\) under \(Z_n\). The condition number of this injective map on \(\mathbb R^\ell\) is \(\sqrt{\kappa(K_n)}\), which converges to \(\sqrt{1+c\|g\|_2^2}<\infty\). Hence, **uniformly over all** \(q\ge1\), the normalized rangefinder approaches the direction of \(Z_nu_n\), up to sign. Its squared capture approaches
\[
\frac{|e_1^{\mathsf T}Z_nu_n|^2}{\|Z_nu_n\|_2^2}
=\frac{c\,(g^{\mathsf T}u_n)^2}{\lambda_{1,n}}
\longrightarrow \frac{c\|g\|_2^2}{1+c\|g\|_2^2}.
\]
On the other hand, because \(W/n\to I_\ell\), the exact finite-dimensional projector identity from Step 1 gives \(p_n\to c\|g\|_2^2/(1+c\|g\|_2^2)\). The difference between all positive-step captures and the ceiling therefore vanishes uniformly. This proves the asserted convergence in probability without restricting how \(q\) grows.

**3. Baseline, comparison probability, and expected risk.** By independence of the first and subsequent Gaussian coordinates,
\[
a_{n,0}=\frac{cn\,h^2}{cn\,h^2+\|\xi\|_2^2}
\longrightarrow \frac{ch^2}{1+ch^2}.
\]
The first row \(g\) of \(\Phi_n\) and the first entry \(h\) of \(\omega_n\) are independent. Thus \(\|g\|_2^2\sim\chi^2_\ell\), \(h^2\sim\chi^2_1\), independently, and the joint limit follows. Because the two continuous limits are almost surely unequal, the improvement event converges in probability. The beta–gamma identity gives \(X_\ell/(X_\ell+H)\sim\operatorname{Beta}(\ell/2,1/2)\); its probability of exceeding one half is the displayed regularized-beta tail. For \(\ell=2\), \(X_2\) is exponential with mean two, so \(\mathbb P(X_2>H)=\mathbb E e^{-H/2}=1/\sqrt2\).

Finally, \(A_nA_n^{\mathsf T}=cn\,e_1e_1^{\mathsf T}+(I-e_1e_1^{\mathsf T})\). Compressing by \(I-vv^{\mathsf T}\) sandwiches the squared residual operator between \(cn\,(I-vv^{\mathsf T})e_1e_1^{\mathsf T}(I-vv^{\mathsf T})\) and this rank-one operator plus \(I\). Taking largest eigenvalues gives \(cn(1-|v^{\mathsf T}e_1|^2)\le\|(I-vv^{\mathsf T})A_n\|_2^2\le cn(1-|v^{\mathsf T}e_1|^2)+1\). The normalized errors are bounded by \(1+1/(cn)\), yielding expectation convergence by boundedness. Strict expected improvement follows by coupling \(X_\ell=H+J\) where \(J\sim\chi^2_{\ell-1}>0\) almost surely and is independent of \(H\).

## Verification

Run `python3 CHECK.py` using Python 3 and NumPy. The standalone checker compares 240 exact projector identities, 960 direct versus reduced power iterations, 960 deterministic spectral-risk inequalities, and 280 fixed-width Gaussian spike trials at two increasing dimensions. Its finite numerical tests validate formulas and implementation consistency; they do **not** establish the uniform-in-power limit, the probability identity, or distributional convergence, which follow from the proof above.

## Relationship to prior work

Chang and Yang introduce the exact sketch-power rangefinder \((ZZ^{\mathsf T})^qY\) and prove general expected and probabilistic error bounds. Their analysis and experiments establish practical improvement, and their discussion observes that one step often nearly reaches the auxiliary sketch's leading subspace. Their full publicly available manuscript includes the general-\(q\) analysis and supplementary sections; it does not give the fixed-width, critically scaled one-spike joint chi-square law, a **uniform** result for every positive step count, or the exact chance of a negative sample-level gain.

Chenakkod and Dereziński analyze a closely related sketched power method with \(Y\) *initialized inside* the auxiliary sketched column space and with fast sparse sketches. Their guarantees are regularized-spectral inequalities, not joint laws for two independent Gaussian sketches. The initialization distinction matters: a direct \(A\omega\) may favor the true spike over the independent auxiliary sketch on some instances.

Tropp, Yurtsever, Udell and Cevher introduce one-pass sketch-based low-rank approximation with general average-error bounds and a separate co-range sketch; their estimator and results do not assert this exact rangefinder law. Townsend and Wang study the distinction between injection and embedding guarantees for randomized SVD and a separate single-sketch diagonal test matrix, not repeated powers of an independent auxiliary sketch.

The exact finite-dimensional projector identity is an instance of the classical Gaussian-Wishart inverse-quadratic-form law, and the chi-square ratio is a standard beta-law calculation. Those ingredients are **not** claimed as new. The assessed contribution is their integration with the **uniform-in-iteration** limit of this specific algorithm and the joint, sharp improvement/regression risk.

## Limitations

The theorem does not claim finite-dimensional monotonicity in iteration count or samplewise improvement. The nonvanishing probability of worsening is part of its conclusion. It does not cover \(\ell\) growing with dimension, non-Gaussian sketches, arbitrary spectra, dependent sketches, stabilized floating-point implementations, or the final oblique reconstruction step used in some one-pass algorithms.

A result with equivalent content could exist under terms such as spiked-Wishart power iteration, random projected singular vectors, or asymptotic kernel principal components. Comparisons were made to closely related full-text sources, but an exhaustive historical theorem search is not possible and independent validation remains outstanding.

## References

1. C. Chang and Y. Yang, *Improving Sketching Algorithms for Low-Rank Matrix Approximation via Sketch-Power Iterations*, arXiv:2603.26298v1 (first public 27 March 2026); SIAM Journal on Matrix Analysis and Applications 47 (2026), 1122–1165.
2. S. Chenakkod and M. Dereziński, *Accelerating Power Method with Fast Sketching for Stronger Low-Rank Approximation*, arXiv:2605.09755v1 (10 May 2026).
3. J. A. Tropp, A. Yurtsever, M. Udell, and V. Cevher, *Practical Sketching Algorithms for Low-Rank Matrix Approximation*, SIAM Journal on Matrix Analysis and Applications 38 (2017), 1454–1485.
4. A. Townsend and C. Wang, *Oblivious Subspace Injection Is Not Enough for Relative Error*, arXiv:2604.10215 (2026).
