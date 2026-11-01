# Exact inverse-logarithmic singular values for continuous-symbol Bergman Hankel operators

## Finding
For every real \(\alpha>-1\) and \(a>0\), consider the big Hankel operator with the continuous symbol
\[
\Phi_a(z)=\overline z\left(1+\left[\log\frac{e}{1-|z|^2}\right]^{-a}\right),\qquad |z|<1,
\]
whose boundary extension is \(\Phi_a(z)=\overline z\) for \(|z|=1\). If \(s_j\) are the nonincreasing singular values, counted with multiplicity, of \(H_{\Phi_a}\) on the weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\), then
\[
\boxed{\lim_{j\to\infty}(\log j)^{a+1}s_j(H_{\Phi_a})
=a\sqrt{\psi_1(\alpha+1)}},
\]
where \(\psi_1(x)=\frac{d^2}{dx^2}\log\Gamma(x)\) denotes the trigamma function. In particular \(H_{\Phi_a}\) is compact, but it belongs to no finite Schatten class \(\mathcal S_p\), \(p>0\). Equivalently, if \(N(t)=\#\{j:s_j(H_{\Phi_a})>t\}\), then
\[
\log N(t)\sim\left(\frac{a\sqrt{\psi_1(\alpha+1)}}{t}\right)^{1/(a+1)},\qquad t\downarrow0.
\]
The result is exact in its leading constant for every fixed pair \((\alpha,a)\); there is no claim of uniformity as either parameter varies.

## Assumptions and scope
The normalized weighted area measure is
\[
d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dx\,dy,
\qquad \alpha>-1.
\]
The Hilbert space \(A^2_\alpha\) is the holomorphic subspace of \(L^2(\mu_\alpha)\); \(P_\alpha\) denotes its orthogonal projection. The *big* Hankel operator is \(H_{\Phi_a}=(I-P_\alpha)M_{\Phi_a}\), mapping \(A^2_\alpha\) into \(L^2(\mu_\alpha)\ominus A^2_\alpha\). It is bounded because \(\Phi_a\) is bounded by \(2\) in modulus. All logarithms are natural and all singular values are counted with multiplicity. The result concerns nonanalytic symbols; its special radial multiplier is not itself an anti-analytic function.

## Proof
**1. Exact angular diagonalization.** Define \(b_n=\|z^n\|^2=\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)}\) and \(e_n=z^n/\sqrt{b_n}\). Put \(h_a(v)=1+[\log(e/v)]^{-a}\) for \(0<v\le1\). The angular Fourier modes of \(H_{\Phi_a}e_n\) have orders \(n-1\), and distinct images are orthogonal in \(L^2(\mu_\alpha)\). Thus the singular values are the decreasing rearrangement of \(d_n=\|H_{\Phi_a}e_n\|\), \(n\ge0\).

For each integer \(n\ge1\) let \(U_n\sim\operatorname{Beta}(n+1,\alpha+1)\), set \(S_n=1-U_n\), and write \(Y_n=h_a(S_n)\). Direct angular integration and projection onto the single analytic monomial of degree \(n-1\) give the **exact identity**
\[
\boxed{d_n^2=\mathbb E[U_nY_n^2]-\frac{n}{n+\alpha+1}(\mathbb E Y_n)^2.}\tag{1}
\]
For \(n=0\), the projection is zero, and \(d_0^2=\mathbb E[U_0 h_a(1-U_0)^2]\) with \(U_0\sim\operatorname{Beta}(1,\alpha+1)\). This one term has no effect on tail asymptotics.

**2. Reduction to a beta-logarithm variance.** Since \(1\le Y_n\le2\), \(\mathbb E(1-U_n)=\frac{\alpha+1}{n+\alpha+2}\), and \(1-\frac n{n+\alpha+1}=\frac{\alpha+1}{n+\alpha+1}\), subtracting \(\operatorname{Var}(Y_n)\) from (1) yields
\[
\left|d_n^2-\operatorname{Var}(Y_n)\right|
\le4\frac{\alpha+1}{n+\alpha+2}+4\frac{\alpha+1}{n+\alpha+1}
=O_\alpha(n^{-1}).\tag{2}
\]
The constant part of \(Y_n\) does not affect its variance, so it is enough to analyze \(F_n=[\log(e/S_n)]^{-a}\).

**3. Exact variance coefficient.** Let \(X_n=nS_n\), \(L_n=1+\log n\), and \(X\sim\operatorname{Gamma}(\alpha+1,1)\). Beta-to-Gamma convergence gives \(X_n\Rightarrow X\), while the beta logarithmic moment identities give
\[
\operatorname{Var}(\log X_n)=\psi_1(\alpha+1)-\psi_1(n+\alpha+2)
\longrightarrow\psi_1(\alpha+1).\tag{3}
\]
The fourth moments of \(\log X_n\) are uniformly bounded. To justify Taylor expansion despite the endpoints, work first on \(E_n=\{|\log X_n|\le L_n/2\}\). On this event,
\[
L_n^{a+1}\bigl(F_n-L_n^{-a}\bigr)
=a\log X_n+O_a\bigl(L_n^{-1}(\log X_n)^2\bigr).\tag{4}
\]
The beta density implies \(\mathbb P(X_n<e^{-L_n/2})=O_{\alpha}(e^{-(\alpha+1)L_n/2})\) and \(\mathbb P(X_n>e^{L_n/2})\le C_\alpha e^{-c\sqrt n}\) for all sufficiently large \(n\). Since \(0<F_n\le1\), these tails contribute negligibly to the squared error in (4) after multiplying by any fixed power of \(L_n\). Uniform logarithmic fourth moments control the remaining Taylor remainder. Hence the centered version of (4) converges in mean square to zero, and (3) implies
\[
\boxed{\operatorname{Var}(Y_n)
= a^2\psi_1(\alpha+1)L_n^{-2a-2}(1+o(1)).}\tag{5}
\]
One can also verify uniform moment bounds directly from the density \(x^\alpha(1-x/n)^n\) of \(X_n\), after normalization: its small-\(x\) bound is a multiple of \(x^\alpha\), and its large-\(x\) bound is a multiple of \(x^\alpha e^{-x/2}\).

**4. Singular values and counting.** Combining (2) and (5), because \(n^{-1}=o((\log n)^{-2a-2})\), gives
\[
d_n=\frac{a\sqrt{\psi_1(\alpha+1)}}{(\log n)^{a+1}}(1+o(1)).\tag{6}
\]
The right-hand comparison sequence is eventually decreasing. For each \(\varepsilon>0\), all but finitely many \(d_n\) lie between \((1-\varepsilon)\) and \((1+\varepsilon)\) times that comparison sequence. Decreasing rearrangement changes no leading constant, proving the displayed formula for \(s_j\). Since \(d_n\to0\), angular diagonalization proves compactness. Every finite positive power of \((\log j)^{-1}\) has divergent sum, so \(H_{\Phi_a}\notin\mathcal S_p\) for every \(p>0\). Inverting the same monotone asymptotic establishes the formula for \(N(t)\).

## Verification
The numerical computations in `checker.py` verify the exact beta-moment normalization, the \(\overline z\) baseline, and the formula (1) against separate Beta integration, then check finite-level trends of the explicit leading coefficient across several parameter pairs. The checker is a finite diagnostic, not a substitute for the limiting argument in steps 3 and 4. Run `python checker.py` with Python 3, NumPy and SciPy. In particular, when \(h_a\) is replaced by the constant function \(1\), exact moments give
\[
\|H_{\overline z}e_n\|^2=\frac{\alpha+1}{(n+\alpha+1)(n+\alpha+2)},\quad n\ge1,
\]
so the ordinary anti-analytic symbol has \(n^{-1}\) singular-value decay, sharply contrasting with (6).

## Relationship to prior work
Keshavarzi and Wu (arXiv:2210.06896, first public 2022-10-13) give general Schatten-membership characterizations for **both** big Hankel operators associated to a symbol and its conjugate, using mean oscillation on regular weighted Bergman spaces. Those characterizations do not give the exact inverse-log singular-value coefficient for this concrete nonanalytic radial-angular symbol. Bourass, El-Fallah, Marrhich and Naqos (arXiv:2102.01743, 2021) obtain singular-value asymptotics under an **anti-analytic symbol** assumption and record the \(n^{-1}\) baseline for \(H_{\overline z}\); the displayed nonanalytic multiplier lies outside that class. Peláez, Perälä and Rättyä (arXiv:1806.09854, 2018) study simultaneous boundedness in radial weighted Bergman settings; their reported estimates are not this singular-value asymptotic. Generic compactness or Schatten criteria may recover some qualitative consequences, but cannot by themselves specify the trigamma leading constant. Historical priority beyond the inspected literature remains to be verified independently.

## Limitations
The theorem covers fixed \(\alpha>-1\) and \(a>0\), the standard power-weighted unit disk, and exactly the indicated radial-angular symbol family. It does not assert an asymptotic for arbitrary continuous symbols, other radial weights, higher dimensions, or uniformity in \((\alpha,a)\). The self-review is not an independent mathematical audit. Finite quadrature is only corroborative.

## References
1. H. Keshavarzi and F. Wu, *Schatten Class Hankel Operators on Weighted Bergman Spaces induced by regular weights*, arXiv:2210.06896 (first posted 2022-10-13). https://arxiv.org/abs/2210.06896
2. M. Bourass, O. El-Fallah, I. Marrhich and H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743 (first posted 2021-02-02). https://arxiv.org/abs/2102.01743
3. J. Á. Peláez, A. Perälä and J. Rättyä, *Hankel operators induced by radial Bekollé–Bonami weights on Bergman spaces*, arXiv:1806.09854 (first posted 2018-06-26). https://arxiv.org/abs/1806.09854
