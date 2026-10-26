# Two-ring Fock localization: a sharp modal transition and inward spectral bias

## Finding

Fix \(\delta>0\) with \(\delta\ne1\). For all sufficiently large real \(T\), let
\[
 E_{T,\delta}=\bigcup_{\sigma\in\{-1,1\}}
 [T+\sigma\delta\sqrt T-\tfrac12,\ T+\sigma\delta\sqrt T+\tfrac12].
\]
The positive radial Toeplitz operator on the classical Gaussian Bargmann–Fock space with symbol \(\mathbf1_{\{|z|^2\in E_{T,\delta}\}}\) has eigenvalues
\[
 \lambda_n(T,\delta)=\int_{E_{T,\delta}}e^{-t}\frac{t^n}{n!}\,dt,
 \qquad n\in\mathbb Z_{\ge0}.
\]
A *modal plateau* means a maximal consecutive block of indices on which the eigenvalues are equal and which forms a local maximum; a block has length one or two in the regimes below.

**One-versus-two modes.** If \(0<\delta<1\), the complete eigenvalue sequence has exactly one modal plateau, centered at \(n=T+O_\delta(1)\). If \(\delta>1\), it has exactly two modal plateaus, separated by one local-minimum plateau, and they are located at
\[
 n_\pm=T\pm r_\delta\sqrt T+O_\delta(1),
 \qquad r_\delta=\delta\tanh(\delta r_\delta),\quad 0<r_\delta<\delta.
\]
The positive root \(r_\delta\) is unique. A plateau may have two adjacent, tied integer indices; the assertions concern plateaus, not uniqueness of an integer index.

**Sharp inward preference.** Set
\[
 G_\delta(s)=e^{-(s-\delta)^2/2}+e^{-(s+\delta)^2/2},
 \qquad C_\delta=\frac{G_\delta(r_\delta)r_\delta(\delta^2+3-r_\delta^2)}{3\sqrt{2\pi}}>0.
\]
For \(\delta>1\), if \(L_-(T,\delta)\) and \(L_+(T,\delta)\) are the heights of the inner and outer maximum plateaus, respectively, then
\[
 L_--L_+=C_\delta T^{-1}+O_\delta(T^{-3/2}).
\]
In particular the inner plateau, and never the outer one, realizes the operator norm for all sufficiently large \(T\). More precisely,
\[
 \|T_{E_{T,\delta}}\|=
 \begin{cases}
 \dfrac{2e^{-\delta^2/2}}{\sqrt{2\pi T}}+O_\delta(T^{-3/2}),&0<\delta<1,\\[6pt]
 \dfrac{G_\delta(r_\delta)}{\sqrt{2\pi T}}+\dfrac{C_\delta}{2T}+O_\delta(T^{-3/2}),&\delta>1.
 \end{cases}
\]
All large-\(T\) assertions are for each **fixed** \(\delta\ne1\), not uniform as \(\delta\to1\).

## Assumptions and scope

The Hilbert space is
\[
 \mathcal F^2=\left\{f\text{ entire}:\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}.
\]
The Toeplitz operator is \(T_E f=P_{\mathcal F^2}(\mathbf1_{\{|z|^2\in E\}}f)\). The nonnegative integers index the standard orthonormal basis \(e_n(z)=z^n/\sqrt{n!}\). The two intervals are disjoint subsets of \((0,\infty)\) for sufficiently large \(T\); they have exactly unit width **in the squared-radius variable**. The spectrum is discrete with accumulation only at zero.

## Proof

**Step 1: spectral reduction.** Polar integration and angular orthogonality give
\[
 \langle T_Ee_m,e_n\rangle=\delta_{mn}\int_E e^{-t}t^n/n!\,dt.
\]
Positivity and compactness imply \(\|T_E\|=\max_{n\ge0}\lambda_n\). To study adjacent eigenvalues, put \(a_\sigma=T+\sigma\delta\sqrt T-\tfrac12\), \(b_\sigma=a_\sigma+1\). Direct integration by parts yields the *exact* identity
\[
 \lambda_{n+1}-\lambda_n=\frac{1}{(n+1)!}
 \sum_{\sigma=\pm1}\bigl(e^{-a_\sigma}a_\sigma^{n+1}-e^{-b_\sigma}b_\sigma^{n+1}\bigr).
 \tag{1}
\]
Extend the right side to real \(x>-1\) by replacing \(n!\) with \(\Gamma(x+1)\). Its numerator is a four-term exponential polynomial in \(x\) with distinct positive bases \(a_-<b_-<a_+<b_+\). Any nonzero sum of four real exponentials with distinct exponents has at most three real zeros, counting multiplicities. To see this, divide by the first exponential, differentiate, and induct using Rolle's theorem. The numerator is nonzero because its four coefficients are nonzero. Thus the real interpolated adjacent difference has at most three zeros. The integral formula also shows \(\lambda_{x+1}-\lambda_x>0\) when \(x+1<a_-\), and \(<0\) when \(x+1>b_+\): every possible zero lies in \([a_--1,b_+-1]\).

**Step 2: uniform Gaussian limit and its first correction.** For real \(x=T+s\sqrt T\), uniformly with two derivatives in \(s\) on any fixed compact interval, Stirling's formula applied to the gamma density gives
\[
 \frac{e^{-(T+v\sqrt T)}(T+v\sqrt T)^{T+s\sqrt T}}
 {\Gamma(T+s\sqrt T+1)}
 =\frac{e^{-(s-v)^2/2}}{\sqrt{2\pi T}}
 \left[1+\frac{H(s,v)}{\sqrt T}+O(T^{-1})\right],
\]
where
\[
 H(s,v)=\frac{v^3}{3}-\frac{sv^2}{2}+\frac{s^3}{6}-\frac s2.
\]
For each width-one interval write \(t=T+v\sqrt T+u\), \(-1/2\le u\le1/2\), and integrate. Its centered first moment vanishes, so
\[
 F_T(s):=\lambda_{T+s\sqrt T}
 =\frac1{\sqrt{2\pi T}}\left[G_\delta(s)+\frac{J_\delta(s)}{\sqrt T}+O_\delta(T^{-1})\right],
 \tag{2}
\]
where the expansion and its first two \(s\)-derivatives are uniform on compacts, and
\[
 J_\delta(s)=\sum_{v=\pm\delta}e^{-(s-v)^2/2}H(s,v).
\]
Here \(\lambda_x\) is the gamma-function extension of the eigenvalue integral. Taylor's formula applied to \(F_T(s+T^{-1/2})-F_T(s)\) shows that the scaled interpolated adjacent difference, with its first derivative, converges uniformly on compacts:
\[
 \sqrt{2\pi}\,T\bigl(\lambda_{T+s\sqrt T+1}-\lambda_{T+s\sqrt T}\bigr)
 \longrightarrow G_\delta'(s).
 \tag{3}
\]

**Step 3: exact number and location of modes.** A direct differentiation gives
\[
 G_\delta'(s)=G_\delta(s)\bigl(\delta\tanh(\delta s)-s\bigr).
\]
For \(0<\delta<1\), this derivative has one simple zero at \(0\) and changes from positive to negative. For \(\delta>1\), strict concavity of \(\delta\tanh(\delta s)\) on \(s>0\) gives one positive root \(r_\delta\), and exactly three simple derivative zeros \(-r_\delta,0,r_\delta\), with signs \(+,-,+,-\). Formula (3), its derivative convergence, and the zero restriction in Step 1 put one zero of the interpolated difference near each simple limiting zero and none elsewhere. Alternatively, the three-zero exponential-polynomial bound excludes further zeros once the three crossings are found. Therefore the integer difference sequence has precisely the claimed sign-changing plateaus, and each plateau contains at most two tied integers. The real crossing locations are \(T+s_0\sqrt T+O_\delta(1)\).

**Step 4: selection and sharp coefficient.** The function \(G_\delta\) is even and \(J_\delta\) is odd. At a positive critical point \(r=r_\delta\), the Gaussian weights at \(v=\pm\delta\) have mean \(r\), second moment \(\delta^2\), and third moment \(r\delta^2\). Thus
\[
 J_\delta(r)=\frac{G_\delta(r)r(r^2-\delta^2-3)}6<0,
 \qquad J_\delta(-r)=-J_\delta(r)>0.
\]
The modal shifts from the limiting critical points are \(O_\delta(1)\) integer indices, changing the leading height by only \(O_\delta(T^{-3/2})\) because the leading derivative vanishes. Substitute (2) at \(s=\pm r\) to obtain
\[
 L_--L_+=\frac{J_\delta(-r)-J_\delta(r)}{\sqrt{2\pi}\,T}
 +O_\delta(T^{-3/2})=\frac{C_\delta}{T}+O_\delta(T^{-3/2}).
\]
For \(0<\delta<1\), \(J_\delta(0)=0\) and the maximizing index is \(T+O_\delta(1)\), giving the first norm formula. The positive signed coefficient finishes the second norm formula and strict global selection.

## Verification

The standalone script `verify.py` numerically integrates the **actual** gamma densities for a grid of widths, separations, and large radii; checks one-versus-two discrete modal transitions, inward dominance, mode locations, and the sharp \(T^{-1}\) coefficient; and independently checks the correction polynomial at the Gaussian critical points. Run `python verify.py` with Python and SciPy as specified in `requirements.txt`. Recorded output is `verification_output.txt`. These finite consistency checks do not replace the proof of the claims for all sufficiently large \(T\); neither the root bound nor the asymptotic error estimate is inferred from the test suite.

## Relationship to prior work

The Gaussian-window Daubechies localization operator and the explicit gamma-integral Hermite eigenvalue formula are established results; the present theorem does **not** claim either as new. Knutsen's 2019 study treats a single thin ring and Cantor-type sets, including a one-ring norm asymptotic, but does not supply the separated two-ring modal count, transition at critical scaled separation, or signed \(T^{-1}\) asymmetry of the two competing peaks. Galbis's 2021 Fock Toeplitz norm estimate is a general bound rather than an exact competing-mode law. Dewage–Ólafsson's 2021 quasi-radial spectral-algebra theory describes radial eigenvalue sequences but does not assert the two-ring transition or peak-height bias. The symmetric Gaussian-mixture bifurcation \(\delta=1\) is classical in substance; the added theorem is the finite-\(T\) modal classification and an explicit skew-induced selection that the symmetric Gaussian limit alone cannot decide.

## Limitations

The asymptotic theorem fixes \(\delta\) away from the degenerate threshold \(\delta=1\); it makes no uniform transition-layer statement as \(\delta\) approaches one with \(T\), and it does not treat unequal ring widths or weights. The sharp asymmetry is an asymptotic assertion, not an explicit finite-\(T\) cutoff. Source inspection cannot exclude every older equivalent result in Poisson-mixture, gamma-density, or time-frequency localization literature.

## References

1. I. Daubechies, *Time-Frequency Localization Operators: A Geometric Phase Space Approach* (1988), IEEE Transactions on Information Theory 34, 605–612. Foundational diagonalization.
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, arXiv:1907.00848 (first public July 1, 2019), especially Section 2.3 and Section 3.1; Journal of Fourier Analysis and Applications 26 (2020), DOI: 10.1007/s00041-020-09751-9.
3. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (first public February 3, 2021).
4. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first public July 3, 2021).
