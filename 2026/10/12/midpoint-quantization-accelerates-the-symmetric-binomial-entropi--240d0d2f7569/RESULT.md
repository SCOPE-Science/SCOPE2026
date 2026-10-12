# Midpoint quantization accelerates the symmetric-binomial entropic CLT by one order
## Finding
Let \(S_n\sim\operatorname{Bin}(n,1/2)\) and standardize it as
\[
Z_n=\frac{2S_n-n}{\sqrt n}.
\]
Its lattice points are \(z_{n,k}=(2k-n)/\sqrt n\), with spacing \(2/\sqrt n\). For a fixed phase \(c\in\mathbb R\), define a Gaussian lattice law \(Q_{n,c}\) by
\[
q_{n,c}(k)=\Phi\!\left(z_{n,k}+\frac{2c+1}{\sqrt n}\right)-\Phi\!\left(z_{n,k}+\frac{2c-1}{\sqrt n}\right),
\]
and write
\[
D_n(c)=D_{\mathrm{KL}}\!\left(\mathcal L(Z_n)\,\middle\|\,Q_{n,c}\right).
\]
Then, for every integer \(n\ge1\), the function \(c\mapsto D_n(c)\) is even and strictly convex. Hence \(c=0\), which centers each Gaussian cell on its lattice point, is the unique global minimizer.

For every fixed real \(c\), as \(n\to\infty\),
\[
D_n(c)=\frac{2c^2}{n}+\frac{1/9-(2/3)c^2}{n^2}+o(n^{-2}).
\]
In particular, the boundary-aligned cells used in the discrete entropic central limit theorem of Gavalakis and Kontoyiannis correspond to \(c=1/2\), and obey
\[
D_n(1/2)=\frac1{2n}-\frac1{18n^2}+o(n^{-2}).
\]
The midpoint cells instead obey
\[
D_n(0)=\frac1{9n^2}+o(n^{-2}).
\]
Thus a half-cell continuity correction cancels the entire order-\(n^{-1}\) relative-entropy penalty in the canonical symmetric Bernoulli example.

## Assumptions and scope
The statement concerns symmetric binomial sums only. The phase \(c\) is fixed while \(n\to\infty\); no uniformity for phases growing with \(n\) is asserted. Logarithms are natural. The comparison law is obtained by integrating the standard-normal density over consecutive cells of width \(2/\sqrt n\), whose center is displaced by \(2c/\sqrt n\) from the corresponding point of the standardized binomial lattice.

## Proof
Write \(a=1/\sqrt n\), and for a lattice point \(z\) define
\[
q_c(z)=\int_{z+(2c-1)a}^{z+(2c+1)a}\phi(u)\,du.
\]
First consider phase optimality. With \(s=z+2ca\),
\[
q_c(z)=\frac{e^{-s^2/2}}{\sqrt{2\pi}}\int_{-a}^a e^{-st-t^2/2}\,dt.
\]
If \(T\) has density proportional to \(e^{-st-t^2/2}\) on \([-a,a]\), differentiation gives
\[
\frac{d^2}{ds^2}\log q_c(z)=-1+\operatorname{Var}_s(T).
\]
Since \(a\le1\) and this tilted law is nondegenerate, \(\operatorname{Var}_s(T)<a^2\le1\). Therefore \(q_c(z)\) is strictly log-concave as a function of \(c\), and \(-\log q_c(z)\) is strictly convex. Averaging with the positive binomial masses shows that \(D_n(c)\) is strictly convex. Binomial symmetry gives \(q_{n,n-k,c}=q_{n,k,-c}\), hence \(D_n(c)=D_n(-c)\). Strict convexity and evenness force the unique minimum at \(c=0\).

For the asymptotics, expand the Gaussian cell mass about its lattice point. Uniformly on every polynomially growing central window,
\[
\begin{aligned}
\log\frac{q_c(z)}{2a\phi(z)}={}&-2cz\,a+\left(\frac{z^2-1}6-2c^2\right)a^2+\frac{2cz}3a^3\\
&+\left(\frac{2c^2}3+\frac{-z^4-4z^2+2}{180}\right)a^4+O\!\left(a^5(1+|z|^5)\right).
\end{aligned}
\]
For \(Z_n\), symmetry and the exact moments
\[
\mathbb E Z_n^2=1,\qquad \mathbb E Z_n^4=3-\frac2n
\]
therefore yield the Gaussian-cell cross-entropy expansion
\[
-\mathbb E\log q_{n,c}(S_n)=\frac12\log\!\left(\frac{\pi e n}2\right)+\frac{2c^2}n+\frac{1/36-(2/3)c^2}{n^2}+o(n^{-2}).
\]
Here \(q_{n,c}(S_n)\) denotes the cell mass indexed by the realized binomial count.

A Stirling expansion of the symmetric binomial mass, combined with
\[
\mathbb E Z_n^6=15-\frac{30}n+\frac{16}{n^2},
\]
gives
\[
H(S_n)=\frac12\log\!\left(\frac{\pi e n}2\right)-\frac1{12n^2}+o(n^{-2}).
\]
Subtracting this entropy from the cross-entropy proves
\[
D_n(c)=\frac{2c^2}n+\frac{1/9-(2/3)c^2}{n^2}+o(n^{-2}).
\]
To justify termwise expectation, one may restrict first to \(|Z_n|\le n^{1/12}\), where the Taylor and Stirling remainders are uniform, and use a binomial Chernoff bound outside that window. The tail contribution is smaller than \(n^{-2}\), while the required standardized moments remain bounded.

## Verification
The accompanying script `verification.py` evaluates the exact finite-\(n\) divergence using log-domain Gaussian cell probabilities. It checks evenness numerically, verifies that \(c=0\) is smaller than several nonzero phases, and confirms convergence of the scaled midpoint and boundary-aligned expressions to \(1/9\), \(1/2\), and \(-1/18\), respectively. These computations are regression checks; strict convexity and the asymptotic expansion are proved analytically above.

## Relationship to prior work
Gavalakis and Kontoyiannis define the discrete Gaussian comparison by integrating the Gaussian density over cells beginning at each lattice point, and prove that its relative entropy from standardized iid lattice sums tends to zero. Their definition is exactly the phase \(c=1/2\) used above. Their Bernoulli specialization supplies a qualitative convergence result and a finite bound of order \(n^{-1/2}\), but not the sharp phase-dependent expansion, the exact finite-\(n\) phase minimizer, or the midpoint acceleration.

Cichoń and Gołębiewski give a general entropy expansion for multinomial laws and note the earlier full binomial expansions of Jacquet and Szpankowski. Their displayed theorem gives only an \(O(n^{-2})\) remainder at the symmetric binomial point because its \(n^{-1}\) coefficient vanishes. The coefficient \(-1/12\) used here is derived directly in the proof and is combined with the Gaussian cell expansion to obtain the new phase law.

## Limitations
No claim is made that midpoint quantization is optimal for nonsymmetric lattice sums or for a different divergence. The expansion is for fixed phase. Classical work on refined binomial normal approximations and full entropy expansions creates a residual possibility that some components of the calculation have appeared separately under continuity-correction terminology; the searches and source inspections described in the review did not locate the combined strict-optimality and phase-dependent KL statement.

## References
[1] Lampros Gavalakis and Ioannis Kontoyiannis, *Entropy and the discrete central limit theorem*, arXiv:2106.00514v1, 2021; later published in *Stochastic Processes and their Applications*.

[2] Jacek Cichoń and Zbigniew Gołębiewski, *On Bernoulli Sums and Bernstein Polynomials*, DMTCS Proceedings AQ, 2012, DOI:10.46298/dmtcs.2993.
