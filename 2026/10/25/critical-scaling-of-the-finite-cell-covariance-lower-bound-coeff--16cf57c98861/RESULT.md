# Critical scaling of the finite-cell covariance lower-bound coefficient

## Finding

Let \(E\in C^4([0,\pi])\) satisfy \(E(k)>0\) for \(0\le k<\pi\) and \(E(\pi)=0\). Suppose that for an integer \(z\ge1\) and \(v>0\), as \(s\downarrow0\),

\[
E(\pi-s)=v s^z+O(s^{z+1}),\qquad E'(\pi-s)=-vz s^{z-1}+O(s^z).
\]

For \(\beta>0\) and an integer cell count \(M\ge1\), set \(h=\pi/M\), \(I_{j,M}=[(j-1)h,jh]\), and \(\bar E_{j,M}=h^{-1}\int_{I_{j,M}}E(k)\,dk\). Define the midpoint-covariance functional

\[
S_M(\beta)=\frac{\beta}{\pi}\sum_{j=1}^M\int_{I_{j,M}}(E(k)-\bar E_{j,M})\tanh(\beta E(k))\,dk.
\]

Then for every fixed \(\beta>0\),

\[
S_M(\beta)=\frac{C_E(\beta)}{M^2}+O(M^{-4}),\qquad C_E(\beta)=\frac{\pi\beta^2}{12}\int_0^\pi E'(k)^2\operatorname{sech}^2(\beta E(k))\,dk.
\]

As \(\beta\to\infty\), the exact coefficient obeys the critical-order law

\[
C_E(\beta)\sim K_z(\beta v)^{1/z},\qquad K_z=\frac{\pi z}{12}\int_0^\infty u^{1-1/z}\operatorname{sech}^2(u)\,du.
\]

The constant \(K_z\) is finite and positive; in particular \(K_1=\pi/12\). Therefore, for this lower-bound term to be no larger than a fixed tolerance \(\varepsilon>0\), its asymptotic coefficient imposes the necessary scale \(M\gtrsim  \sqrt{K_z/\varepsilon}(\beta v)^{1/(2z)}\). This is a necessary scale for the bound term, not a sufficient guarantee on the actual preparation error.

For the critical transverse-field Ising dispersion \(E(k)=2J\cos(k/2)\), \(J>0\), the endpoint behavior is \(E(\pi-s)\sim Js\), so \(z=1\), \(v=J\), and \(C_E(\beta)\sim\pi\beta J/12\).

## Assumptions and scope

The coefficient expansion is for fixed \(\beta\) as \(M\to\infty\); the critical-order asymptotic is then for \(\beta\to\infty\). The dispersion is smooth on the closed interval, has a unique zero at the right endpoint, and has the stated one-sided power law there. The functional \(S_M\) is the interval-covariance expression appearing as a lower-bound term in the quasi-adiabatic thermal-preparation analysis of the transverse-field Ising chain. Extending the formula to an abstract dispersion \(E\) proves an asymptotic property of that functional; it does not by itself prove that every physical model has the same entropy bound.

## Proof

Write \(g(k)=\tanh(\beta E(k))\). On a cell of width \(h\) centered at \(c\), Taylor expansion and symmetry give

\[
\int_{c-h/2}^{c+h/2}(E-\bar E)g\,dk=\frac{h^3}{12}E'(c)g'(c)+O(h^5)
=\frac{\beta h^3}{12}E'(c)^2\operatorname{sech}^2(\beta E(c))+O(h^5).
\]

The remainder is uniform over the compact interval for fixed \(\beta\), because \(E\in C^4\). Summing the cells and applying the midpoint Riemann-sum estimate to \(E'^2\operatorname{sech}^2(\beta E)\) yields

\[
S_M(\beta)=\frac{\beta^2h^2}{12\pi}\int_0^\pi E'(k)^2\operatorname{sech}^2(\beta E(k))\,dk+O(h^4),
\]

which is the stated \(M^{-2}\) expansion after substituting \(h=\pi/M\). The next correction is order \(h^4\), since the cellwise odd Taylor terms integrate to zero.

For the low-temperature coefficient, the integrand away from \(k=\pi\) is exponentially suppressed because \(E\) is bounded below there. Set \(s=\pi-k\) near the unique zero and then \(u=(\beta v)^{1/z}s\). The endpoint hypotheses imply

\[
\int_0^\pi E'(k)^2\operatorname{sech}^2(\beta E(k))\,dk
\sim v^2z^2(\beta v)^{-(2z-1)/z}\int_0^\infty u^{2z-2}\operatorname{sech}^2(u^z)\,du.
\]

Multiplication by \(\pi\beta^2/12\), followed by the substitution \(w=u^z\), gives

\[
C_E(\beta)\sim\frac{\pi z}{12}(\beta v)^{1/z}\int_0^\infty w^{1-1/z}\operatorname{sech}^2(w)\,dw.
\]

The integral converges at zero because \(1-1/z\ge0\), and at infinity by exponential decay. For \(z=1\), it equals \(\int_0^\infty\operatorname{sech}^2w\,dw=1\), so \(K_1=\pi/12\). The Ising specialization follows from \(2J\cos((\pi-s)/2)=2J\sin(s/2)=Js+O(s^3)\).

Each cell contribution is nonnegative: it is the covariance integral of \(E\) with the increasing function \(\tanh(\beta E)\). The asymptotic derivation does not use numerical experiments as proof.

## Verification

The analytic derivation establishes the fixed-\(\beta\) coefficient and the low-temperature exponent under the stated hypotheses. The included standard-library script numerically compares \(M^2S_M(\beta)\) with \(C_E(\beta)\) for the critical Ising dispersion and checks the \(z=2\) coefficient against its defining integral. These finite computations are corroborative only; they do not establish the limits. The claim is restricted to the defined functional and the stated endpoint assumptions.

## Relationship to prior work

Shirai's *Quasi-adiabatic thermal ensemble preparation in the thermodynamic limit* derives the interval-covariance lower-bound expression for the transverse-field Ising model, reports the order \(S_M\sim M^{-2}\), and analyzes the \(z=1\) critical behavior of its periodically modulated Ising chain. The present statement supplies the exact leading coefficient of that functional and proves the conditional power-law classification for any smooth dispersion with endpoint order \(z\ge1\). It does not claim that the source's physical lower bound is saturated for finite \(M\), and it does not claim a physical application to a new Hamiltonian without a separate derivation of the bound.

## Limitations

The result is asymptotic, not a uniform finite-\(M\) error bound. The \(O(M^{-4})\) constant may depend on \(\beta\) and on derivatives of \(E\). The low-temperature law assumes a unique endpoint zero with the specified power law; multiple zeros require summing their contributions, and a gapped dispersion has a different low-temperature asymptotic. The necessary cell-count scale is not a sufficient preparation-complexity guarantee. For \(z>1\), the theorem classifies the defined functional; a physical model must independently justify that this functional is its relevant entropy lower bound.

## References

1. T. Shirai, “Quasi-adiabatic thermal ensemble preparation in the thermodynamic limit,” arXiv:2510.13555v1, first submitted 15 October 2025; revised as v2 on 25 February 2026; *Physical Review E* **113**, 054113 (2026). DOI: 10.1103/dcwj-j65m. The first public version fixes the date used for the literature window.
2. MSC2020 82B20, lattice systems including Ising models.
