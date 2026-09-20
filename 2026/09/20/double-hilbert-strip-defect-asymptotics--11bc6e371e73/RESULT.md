# Sharp strip-defect asymptotics for the double Hilbert transform

## Result

Let \(H=H_2H_1\) be the double Hilbert transform on \(\mathbb R^2\), with the unitary Fourier convention
\[
\widehat h(\xi)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-ix\xi}h(x)\,dx.
\]
For \(\varepsilon>0\) and \(g\in L^2(\mathbb R)\), put
\[
f_{\varepsilon,g}(x_1,x_2)
=\mathbf 1_{\{|x_1-x_2|<\varepsilon\}}g(x_2),
\qquad
F(s)=\int_0^s\left(\frac{\sin u}{u}\right)^2du.
\]
Then the defect from the \(+1\) eigenspace has the exact identity
\[
\boxed{
\|(H-I)f_{\varepsilon,g}\|_2^2
=\frac{8\varepsilon}{\pi}
\int_{\mathbb R}|\widehat g(\xi)|^2F(\varepsilon|\xi|)\,d\xi .
}
\tag{1}
\]
Since \(\|f_{\varepsilon,g}\|_2^2=2\varepsilon\|g\|_2^2\), (1) gives an exact one-dimensional description of the quasi-eigenfunction defect for every transverse cutoff.

If \(g\in \dot H^{1/2}(\mathbb R)\), then
\[
\boxed{
\|(H-I)f_{\varepsilon,g}\|_2^2
=\frac8\pi\,\varepsilon^2
\int_{\mathbb R}|\xi|\,|\widehat g(\xi)|^2\,d\xi
+o(\varepsilon^2).
}
\tag{2}
\]
Thus a regular transverse cutoff has relative defect of order \(\sqrt\varepsilon\). The logarithm in the hard-cutoff example below is an endpoint \(\dot H^{1/2}\) effect caused by jumps.

Now let
\[
E=\bigcup_{r=1}^m(x_{2r-1},x_{2r}),
\qquad x_1<x_2<\cdots<x_{2m},
\]
be a fixed bounded finite-perimeter subset of the line, let
\[
\sigma_j=(-1)^{j+1},\qquad P(E)=2m,
\]
and define
\[
V_{\varepsilon,E}
=\{(x_1,x_2):x_2\in E,\ |x_1-x_2|<\varepsilon\}.
\]
Then, as \(\varepsilon\downarrow0\),
\[
\boxed{
\begin{aligned}
\|(H-I)\mathbf1_{V_{\varepsilon,E}}\|_2^2
&=\frac{8\varepsilon^2}{\pi^2}
\Bigg[
P(E)\left(\log\frac1\varepsilon+\frac52-\log2\right)\\
&\qquad\qquad
-2\sum_{1\le j<k\le2m}\sigma_j\sigma_k
\log|x_j-x_k|
\Bigg]
+o(\varepsilon^2).
\end{aligned}
}
\tag{3}
\]
The second term is a logarithmic interaction of the jump points. Formula (3) is covariant under simultaneous dilation of \(E\) and \(\varepsilon\); the apparent change of the individual logarithms cancels because
\[
\sum_{j<k}\sigma_j\sigma_k=-\frac{P(E)}2.
\]
In particular,
\[
\boxed{
\frac{\|(H-I)\mathbf1_{V_{\varepsilon,E}}\|_2}
{\|\mathbf1_{V_{\varepsilon,E}}\|_2}
\sim
\frac2\pi
\sqrt{\frac{P(E)}{|E|}\,\varepsilon\log\frac1\varepsilon}.
}
\tag{4}
\]

For a single interval \(E=(-L,L)\), (3) simplifies to
\[
\boxed{
\|(H-I)\mathbf1_{V_{\varepsilon,L}}\|_2^2
=\frac{16}{\pi^2}\varepsilon^2
\left(\log\frac L\varepsilon+\frac52+o(1)\right),
}
\tag{5}
\]
where
\[
V_{\varepsilon,L}=\{(x_1,x_2):|x_1-x_2|<\varepsilon,\ |x_2|<L\}.
\]
Consequently
\[
\boxed{
\frac{\|(H-I)\mathbf1_{V_{\varepsilon,L}}\|_2}
{\|\mathbf1_{V_{\varepsilon,L}}\|_2}
=
\frac2\pi
\sqrt{\frac\varepsilon L
\left(\log\frac L\varepsilon+\frac52+o(1)\right)}.
}
\tag{6}
\]
For the truncated strip \(L=1\) used by Abakumov--Domelevo--Petermichl--Poltoratski, their upper rate \(\sqrt{\varepsilon|\log\varepsilon|}\) is therefore sharp for that construction, with leading relative constant \(2/\pi\), and the next constant inside the square root is \(5/2\).

## Proof

The Fourier multiplier of \(H\) is \(+1\) on the second and fourth quadrants and \(-1\) on the first and third quadrants. With \(p=\xi_1+\xi_2\),
\[
\widehat f_{\varepsilon,g}(\xi_1,\xi_2)
=\widehat{\mathbf1_{(-\varepsilon,\varepsilon)}}(\xi_1)\widehat g(p),
\]
and
\[
\left|\widehat{\mathbf1_{(-\varepsilon,\varepsilon)}}(t)\right|^2
=\frac2\pi\frac{\sin^2(\varepsilon t)}{t^2}.
\]
Because \(H-I=-2\) exactly on the same-sign quadrants, Plancherel gives
\[
\|(H-I)f_{\varepsilon,g}\|_2^2
=4\int_{\xi_1\xi_2>0}
\left|\widehat{\mathbf1_{(-\varepsilon,\varepsilon)}}(\xi_1)\right|^2
|\widehat g(\xi_1+\xi_2)|^2\,d\xi_1d\xi_2.
\]
For fixed \(p>0\), the same-sign condition is \(0<\xi_1<p\); for \(p<0\) it is \(p<\xi_1<0\). Integrating in \(\xi_1\) yields (1).

For (2), note that \(F(s)/s\to1\) as \(s\downarrow0\) and \(F(s)\le s\). Hence
\[
\frac{F(\varepsilon|\xi|)}\varepsilon\to|\xi|,
\qquad
0\le \frac{F(\varepsilon|\xi|)}\varepsilon\le|\xi|,
\]
and dominated convergence applies under the \(\dot H^{1/2}\) assumption.

For (3),
\[
\widehat{\mathbf1_E}(\xi)
=\frac1{i\xi\sqrt{2\pi}}
\sum_{j=1}^{2m}\sigma_j e^{-ix_j\xi}.
\]
Since \(\sum_j\sigma_j=0\),
\[
|\widehat{\mathbf1_E}(\xi)|^2
=\frac1{\pi\xi^2}
\sum_{j<k}\sigma_j\sigma_k
\bigl(\cos((x_j-x_k)\xi)-1\bigr).
\]
Substitution into (1) gives
\[
\|(H-I)\mathbf1_{V_{\varepsilon,E}}\|_2^2
=\frac{16\varepsilon^2}{\pi^2}
\sum_{j<k}\sigma_j\sigma_k
I\!\left(\frac{|x_j-x_k|}{\varepsilon}\right),
\tag{7}
\]
where
\[
I(a)=\int_0^\infty(\cos(au)-1)\frac{F(u)}{u^2}\,du.
\]
The needed universal asymptotic is
\[
\boxed{
I(a)=-\log a-\left(\frac52-\log2\right)+o(1).
}
\tag{8}
\]
To compute the constant, set \(\phi(u)=F(u)/u\). A standard cosine-integral asymptotic gives
\[
\int_0^\infty(1-\cos au)\frac{\phi(u)}u\,du
=\log a+\gamma+C_\phi+o(1),
\]
where
\[
C_\phi=
\int_0^1\frac{\phi(u)-1}{u}\,du
+\int_1^\infty\frac{\phi(u)}u\,du.
\]
Writing \(q(u)=(\sin u/u)^2=F'(u)\) and integrating by parts gives
\[
C_\phi=1+\operatorname{FP}_{s=0}M(s),
\qquad
M(s)=\int_0^\infty q(u)u^{s-1}\,du.
\]
For \(0<s<2\), the classical cosine Mellin integral gives
\[
M(s)=\frac{\pi 2^{-s}}{\Gamma(3-s)\sin(\pi s/2)}
=\frac1s+\left(\frac32-\gamma-\log2\right)+O(s).
\]
Therefore
\[
C_\phi=\frac52-\gamma-\log2,
\]
which proves (8). Inserting (8) into (7), using
\(\sum_{j<k}\sigma_j\sigma_k=-P(E)/2\), gives (3). Equations (4)--(6) follow from \(|V_{\varepsilon,E}|=2\varepsilon|E|\).

## Relation to prior work

Abakumov, Domelevo, Petermichl and Poltoratski, *Invariant sets of the double Hilbert transform* (arXiv:2609.15155), construct the bounded truncated diagonal strip
\[
V_\varepsilon=\{|x_1-x_2|<\varepsilon,\ |x_2|<1\}
\]
and prove
\[
\|H\mathbf1_{V_\varepsilon}-\mathbf1_{V_\varepsilon}\|_2^2
\lesssim \varepsilon^2|\log\varepsilon|,
\qquad |V_\varepsilon|=4\varepsilon.
\]
They later identify the resulting \(\sqrt{\varepsilon|\log\varepsilon|}\) cost as the model computation for their quantitative-stability question. The present result sharpens that model computation to an exact leading constant and a second asymptotic term, identifies the logarithm as a transverse \(\dot H^{1/2}\) endpoint phenomenon, and extends the calculation to arbitrary \(L^2\) transverse cutoffs and bounded one-dimensional finite-perimeter cutoffs.

The older paper by Holmes--Treil--Volberg, *Dyadic bi-parameter repeated commutator and dyadic product BMO* (arXiv:2101.00763), is relevant to the commutator motivation cited by the direct source but concerns a dyadic bi-parameter commutator problem, not these strip-defect asymptotics. Older papers titled “double Hilbert transform” in the polynomial-surface literature study different singular-integral operators and do not address characteristic strip quasi-eigenvectors.

## Limitations

- The sharp asymptotics here concern diagonal tubes with a transverse cutoff depending only on \(x_2\); no classification of general near-invariant planar sets is proved.
- Formula (3) assumes a fixed bounded one-dimensional finite-perimeter set as \(\varepsilon\to0\); no uniform statement is claimed when endpoints collide with \(\varepsilon\).
- The result does not solve the quantitative-stability question posed in arXiv:2609.15155.
- No claim is made that the finite-union family is globally extremal among bounded sets of a given area or geometry.
- The direct source is very recent, so an unindexed contemporaneous refinement remains a residual originality risk.

## References

1. E. Abakumov, K. Domelevo, S. Petermichl, A. Poltoratski, *Invariant sets of the double Hilbert transform*, arXiv:2609.15155 (2026), https://arxiv.org/abs/2609.15155.
2. I. Holmes, S. Treil, A. Volberg, *Dyadic bi-parameter repeated commutator and dyadic product BMO*, arXiv:2101.00763 (2021), https://arxiv.org/abs/2101.00763.
