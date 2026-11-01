# Sharp subsequential constants for Bergman concentration on balanced Cantor annuli

## Finding
Let \(b>0\), let \(\delta=\log 2/\log 3\), and consider the weighted analytic Bergman space with probability measure \(b(1-|z|^2)^{b-1}\,dA(z)/\pi\). For the balanced radial Cantor sets \(E_n\) defined below, the Toeplitz concentration operator \(T_n\) has two explicit positive, finite subsequential limits:
\[
\lim_{m\to\infty}(3/2)^m\|T_{2m}\|=L_{\mathrm e}(b),\qquad
\lim_{m\to\infty}(3/2)^{m+1/2}\|T_{2m+1}\|=L_{\mathrm o}(b).
\]
These constants are characterized as maxima of absolutely convergent Cantor-integer series, not merely bounds up to unspecified multiplicative factors. In addition, the corresponding asymptotics hold for every fixed monomial eigenvalue, and the normalized eigenvalues satisfy a uniform high-degree bound tending to zero. No equality or inequality between the two limiting constants is asserted.

## Assumptions and scope
For \(n\ge0\), define the stage-\(n\) middle-third set by
\[
C_n=\bigcup_{\varepsilon\in\{0,2\}^{n}}
\left[\sum_{j=1}^n\varepsilon_j3^{-j},\ \sum_{j=1}^n\varepsilon_j3^{-j}+3^{-n}\right],\quad C_0=[0,1].
\]
Set \(R_n=3^{n/2}\), and \(E_n=\{z\in\mathbb D: |z|^2/(1-|z|^2)\in R_nC_n\}\). The operator \(T_n\) is the positive Toeplitz operator with symbol \(1_{E_n}\), equivalently the quadratic form \(\langle T_nf,f\rangle=\int_{E_n}|f|^2b(1-|z|^2)^{b-1}\,dA/\pi\).

Let \(\mu\) be the probability middle-third Cantor measure: the law of \(Y=\sum_{j\ge1}2\xi_j3^{-j}\), with independent equiprobable Bernoulli digits \(\xi_j\). Let \(\mathcal D\) denote the countable set of nonnegative integers having only ternary digits zero and two, including zero, and put
\[
\nu=\sum_{a\in\mathcal D}(y\mapsto a+y)_\#\mu.
\]
This is a locally finite measure. For \(k\in\mathbb Z_{\ge0}\) define the beta-prime probability density
\[
g_{k,b}(t)=\frac{t^k}{B(k+1,b)(1+t)^{k+b+1}},\qquad t\ge0.
\]
Define
\[
L_{\mathrm e}(b)=\max_{k\ge0}\int_0^\infty g_{k,b}(t)\,d\nu(t),\quad
L_{\mathrm o}(b)=\max_{k\ge0}\sqrt2\int_0^\infty g_{k,b}(\sqrt3t)\,d\nu(t).
\]
Both maxima are attained at finite integer indices (not necessarily the same). The exact assertions concern this balanced scaling and all real \(b>0\); they do not classify maximizing indices.

## Proof
**Step 1: diagonalization and normalization.** The normalized monomial \(e_k(z)=z^k/\sqrt{bB(k+1,b)}\) has norm one because its radial squared norm is \(bB(k+1,b)\). Rotation invariance makes the monomials eigenvectors of \(T_n\). With \(s=|z|^2\) and \(t=s/(1-s)\), direct substitution gives
\[
\lambda_{k,n}=\langle T_ne_k,e_k\rangle
=\int_{R_nC_n}g_{k,b}(t)\,dt,
\qquad \|T_n\|=\sup_{k\ge0}\lambda_{k,n}.
\]
All eigenvalues are nonnegative.

**Step 2: exact digit decomposition.** Write \(\mathcal D_m=\{\sum_{j=0}^{m-1}2\eta_j3^j:\eta_j\in\{0,1\}\}\) and \(d\mu_m=(3/2)^m1_{C_m}(y)\,dy\). Both \(\mu_m\) and \(\mu\) are probability measures and \(\mu_m\Rightarrow\mu\). Partitioning the first \(m\) and remaining \(m\) digits of \(C_{2m}\) yields the **exact** decomposition, up to endpoints,
\[
3^m C_{2m}=\bigcup_{a\in\mathcal D_m}(a+C_m).
\]
Similarly, splitting the first \(m\) and final \(m+1\) digits gives
\[
3^{m+1/2}C_{2m+1}=\bigcup_{a\in\mathcal D_m}\sqrt3(a+C_{m+1}).
\]
Thus, for every fixed \(k\),
\[
(3/2)^m\lambda_{k,2m}
=\sum_{a\in\mathcal D_m}\int g_{k,b}(a+y)\,d\mu_m(y),
\]
\[
(3/2)^{m+1/2}\lambda_{k,2m+1}
=\sqrt2\sum_{a\in\mathcal D_m}\int g_{k,b}(\sqrt3(a+y))\,d\mu_{m+1}(y).
\]
The factor \(\sqrt2\) in the second formula follows from the Jacobian \(\sqrt3\) and the masses \((2/3)^{m+1}\) of the stage-\(m+1\) Cantor pieces.

**Step 3: fixed-degree limits.** The digit-count bound
\[
\#\{a\in\mathcal D:a\le T\}\le C(1+T)^\delta
\]
holds for every \(T\ge0\), by enclosing the allowed ternary digits within the first \(\lceil\log_3(T+1)\rceil\) positions. Since \(\mu_m\) is supported in \([0,1]\), the measures \(\sum_{a\in\mathcal D_m}(a+\cdot)_\#\mu_m\), their limits, and their \(\sqrt3\)-dilates all obey \(\sigma([0,T])\le C(1+T)^\delta\) uniformly in \(m\) (changing the constant for a dilation). For fixed \(k\), the density satisfies \(g_{k,b}(t)\le C_{b,k}(1+t)^{-b-1}\). A dyadic-tail estimate therefore gives
\[
\int_{t>T}g_{k,b}(t)\,d\sigma(t)
\le C_{b,k}(1+T)^{\delta-b-1}\longrightarrow0.
\]
Weak convergence of \(\mu_m\) to \(\mu\) on bounded digit sets, followed by this uniform tail estimate, proves the asserted fixed-degree limits in Step 2. Absolute convergence of both series follows by the same bound, because \(\delta-b-1<0\).

**Step 4: high-degree uniformity.** For \(k\ge1\) set \(K=k+1\). The gamma-ratio estimate \(B(k+1,b)^{-1}\le C_b K^b\) and the inequality \((t/(1+t))^k\le\exp[-k/(1+t)]\) imply
\[
g_{k,b}(t)\le\frac{C_b}{K}
\left(\frac{1+t}{K}\right)^{-b-1}
\exp\!\left[-\frac{1}{2}\left(\frac{1+t}{K}\right)^{-1}\right].
\]
Integrate against any of the uniformly growing digit measures in Step 3. Divide \((1+t)/K\) into dyadic ranges. In ranges with \(K2^j\ge1\), the growth bound contributes at most \(C(K2^j)^\delta\), yielding the summable bound
\[
CK^{\delta-1}\sum_{j\in\mathbb Z}
2^{j(\delta-b-1)}e^{-c2^{-j}}.
\]
For the ranges with \(K2^j<1\), the exponential factor dominates the bounded mass \(\sigma([0,1])\), giving the same order. The \(k=0\) case follows from Step 3. Consequently, with a constant depending only on \(b\),
\[
\sup_{n\ge0}(3/2)^{n/2}\lambda_{k,n}\le C_b(k+1)^{\delta-1}.
\]
Since \(\delta<1\), the right-hand side tends to zero as \(k\to\infty\). The fixed-mode limits from Step 3 therefore converge uniformly at the spectral supremum: split at a finite \(k\)-cutoff, take the limit for the finite portion, and let the cutoff grow. This establishes both sharp operator-norm constants and attainment of the maxima defining them. Positivity follows from \(g_{0,b}>0\) and the positive mass of the \(a=0\) summand of \(\nu\).

## Verification
The included standalone `check.py` checks exactly, using rational arithmetic for the flat Bergman weight \(b=1\), the even-stage digit identities for several stages and degrees; it checks the corresponding odd-stage equalities and subsequential convergence numerically. Its finite tests pass (91 assertions in the packaged version), but the uniform high-degree estimate and infinite limits rest on the analytical argument above. Running `python check.py` in the package directory requires only the Python standard library. For an independently reproducible finite eigenvalue in the flat case, if the \(t\)-intervals have endpoints \(u_j,v_j\), then
\[
\lambda_{k,n}=\sum_j\left[\left(\frac{v_j}{1+v_j}\right)^{k+1}
-\left(\frac{u_j}{1+u_j}\right)^{k+1}\right].
\]
The constants are constructively approximable: restrict \(a\in\mathcal D\) to \(a\le T\), replace \(\mu\) by \(\mu_m\), and truncate the spectral maximum at \(k\le K\). The digit tail is bounded by \(O_{b,k}(T^{\delta-b-1})\); fixed-index \(\mu_m\)-approximations converge by weak convergence; the spectral omission is bounded by \(O_b(K^{\delta-1})\).

## Relationship to prior work
Abreu, Mouayn and Voigtlaender derive the beta-prime spectral formula and prove two-sided **order estimates** for these radial Bergman Cantor localization operators, including balanced scaling (arXiv:2201.11705, Section 4). The result here sharpens that order statement to two explicit subsequential limiting coefficients for the **operator norm**, with rigorous control of escape to large monomial degree. Knutsen's related Gaussian STFT Cantor results (2019/2020 and 2021) give bounds up to multiplicative constants for a different radial density and include general Cantor alphabets. Neither is invoked to assert that the current constants coincide with STFT constants. The elementary Cantor digit decomposition and monomial eigenvalue identity are background; the new claim is the norm-level limiting constant with an explicit measure formula and high-degree tightness.

## Limitations
The theorem does not identify the maximizing monomial order, prove that the two constants differ, give a rate of norm convergence, or cover nonradial fractals. No result is claimed outside positive Bergman weight parameter \(b\) or beyond the precisely balanced scale \(R_n=3^{n/2}\). Historical-priority checking cannot exclude every obscure equivalent treatment; independent audit and validation are not performed.

## References
1. L. D. Abreu, Z. Mouayn, and F. Voigtlaender, *A fractal uncertainty principle for Bergman spaces and analytic wavelets*, arXiv:2201.11705 (first submitted 2022-01-27), J. Math. Anal. Appl. 519 (2023), 126699; https://arxiv.org/abs/2201.11705.
2. H. Knutsen, *Daubechies' Time–Frequency Localization Operator on Cantor Type Sets I*, J. Fourier Anal. Appl. 26 (2020), article 47; https://doi.org/10.1007/s00041-020-09751-9.
3. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets II*, arXiv:2104.10976 (first submitted 2021-04-22); https://arxiv.org/abs/2104.10976.
