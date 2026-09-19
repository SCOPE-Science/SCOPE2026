# Half-Sobolev law for truncated diagonal Hilbert eigenstrips

## Statement

Let \(H\) be the one-dimensional Hilbert transform with Fourier multiplier
\(-i\,\mathrm{sgn}\,\xi\), and let
\[
   \mathcal H=H_1H_2
\]
be the double Hilbert transform on \(L^2(\mathbb R^2)\). Use the unitary Fourier transform
\[
   \widehat g(\xi)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}e^{-ix\xi}g(x)\,dx.
\]
For \(\varepsilon>0\) and \(g\in L^2(\mathbb R)\), define the truncated diagonal strip profile
\[
   F_{\varepsilon,g}(x,y)=\mathbf 1_{\{|x-y|<\varepsilon\}}\,g(y).
\]
Set
\[
   J(s)=\int_0^s\left(\frac{\sin u}{u}\right)^2du
       =\operatorname{Si}(2s)-\frac{1-\cos(2s)}{2s},
   \qquad J(0)=0.
\]

**Theorem.** For every \(g\in L^2(\mathbb R)\),
\[
\boxed{
 \|\mathcal H F_{\varepsilon,g}-F_{\varepsilon,g}\|_2^2
 =
 \frac{8\varepsilon}{\pi}
 \int_{\mathbb R}|\widehat g(\xi)|^2J(\varepsilon|\xi|)\,d\xi .
}
\]
Consequently,
\[
\boxed{
 \lim_{\varepsilon\downarrow0}
 \frac{\|\mathcal H F_{\varepsilon,g}-F_{\varepsilon,g}\|_2^2}{\varepsilon^2}
 =
 \frac8\pi\int_{\mathbb R}|\xi|\,|\widehat g(\xi)|^2\,d\xi
}
\]
with the value \(+\infty\) allowed on the right. Thus the natural cutoff threshold is exactly
\(\dot H^{1/2}(\mathbb R)\): for nonzero \(g\),
\[
 \|\mathcal H F_{\varepsilon,g}-F_{\varepsilon,g}\|_2=O(\varepsilon)
 \quad(\varepsilon\downarrow0)
\]
if and only if \(g\in\dot H^{1/2}\).

Since
\[
 \|F_{\varepsilon,g}\|_2^2=2\varepsilon\|g\|_2^2,
\]
for \(g\in\dot H^{1/2}\setminus\{0\}\) one has the normalized asymptotic
\[
\boxed{
 \frac{\|\mathcal H F_{\varepsilon,g}-F_{\varepsilon,g}\|_2}
      {\|F_{\varepsilon,g}\|_2}
 =
 \left(
 \frac4\pi
 \frac{\int |\xi||\widehat g(\xi)|^2\,d\xi}{\|g\|_2^2}
 \right)^{1/2}
 \varepsilon^{1/2}(1+o(1)).
}
\]

There is a sharp logarithmic boundary layer for jump cutoffs. Suppose \(g\) is compactly supported,
piecewise \(W^{1,1}\), with finitely many jump points \(x_j\), and let
\[
   \Delta_j=g(x_j+)-g(x_j-),\qquad
   S(g)=\sum_j|\Delta_j|^2.
\]
Then
\[
\boxed{
 \|\mathcal H F_{\varepsilon,g}-F_{\varepsilon,g}\|_2^2
 =
 \frac{8S(g)}{\pi^2}\,
 \varepsilon^2\log\frac1\varepsilon\,(1+o(1)).
}
\]
In particular, if \(g=\mathbf 1_E\) and \(E\) is a finite union of \(m\) bounded intervals, then
\(S(g)=2m\).

For the exact strip truncation used by Abakumov--Domelevo--Petermichl--Poltoratski,
\[
   V_\varepsilon=\{(x,y):|x-y|<\varepsilon,\ |y|<1\},
   \qquad \chi_{V_\varepsilon}=F_{\varepsilon,\mathbf 1_{(-1,1)}},
\]
the source paper proved only the upper-order estimate
\[
 \frac{\|\mathcal H\chi_{V_\varepsilon}-\chi_{V_\varepsilon}\|_2}
      {\|\chi_{V_\varepsilon}\|_2}
 \lesssim \sqrt{\varepsilon|\log\varepsilon|}.
\]
The exact leading asymptotic is
\[
\boxed{
 \frac{\|\mathcal H\chi_{V_\varepsilon}-\chi_{V_\varepsilon}\|_2}
      {\|\chi_{V_\varepsilon}\|_2}
 =
 \frac2\pi\sqrt{\varepsilon\log\frac1\varepsilon}\,(1+o(1)).
}
\]
Hence the logarithm is genuinely present for that hard cutoff, whereas a half-Sobolev cutoff has the
strictly better \(\sqrt{\varepsilon}\) normalized rate.

## Context

Abakumov, Domelevo, Petermichl and Poltoratski, arXiv:2609.15155, introduced bounded open sets whose
indicators are approximate eigenvectors of the double Hilbert transform. Their basic continuous example
starts from the infinite diagonal strip, whose indicator is a generalized eigenvector with eigenvalue
\(1\), and truncates it by \(|y|<1\). A direct Fourier estimate gives an upper bound of order
\(\sqrt{\varepsilon|\log\varepsilon|}\) for the normalized defect.

The result above extracts the exact spectral identity behind that computation. It identifies the
half-Sobolev energy of the longitudinal cutoff as the limiting defect energy, gives a converse
characterization, and shows that the logarithm in the source example is precisely the endpoint
signature of jump discontinuities.

## Proof

### 1. Fourier factorization and quadrant defect

The source computation extends verbatim from the indicator cutoff to arbitrary \(g\in L^2\):
\[
   \widehat{F_{\varepsilon,g}}(\xi_1,\xi_2)
   =
   \widehat{\mathbf 1_{(-\varepsilon,\varepsilon)}}(\xi_1)\,
   \widehat g(\xi_1+\xi_2),
\]
where
\[
   \left|
   \widehat{\mathbf 1_{(-\varepsilon,\varepsilon)}}(t)
   \right|^2
   =
   \frac2\pi\frac{\sin^2(\varepsilon t)}{t^2}.
\]

The multiplier of \(\mathcal H\) equals \(+1\) in the second and fourth quadrants and \(-1\) in
the first and third. Therefore
\[
 \|\mathcal HF_{\varepsilon,g}-F_{\varepsilon,g}\|_2^2
 =
 4\int_{\xi_1\xi_2>0}
 |\widehat{F_{\varepsilon,g}}(\xi_1,\xi_2)|^2\,d\xi_1d\xi_2.
\]
In the first quadrant put \(t=\xi_1>0\) and \(p=\xi_1+\xi_2>t\); in the third quadrant use the
corresponding negative variables. This gives
\[
\begin{aligned}
 D_\varepsilon(g)^2
 &:=
 \|\mathcal HF_{\varepsilon,g}-F_{\varepsilon,g}\|_2^2\\
 &=4\int_0^\infty
 \left|\widehat{\mathbf 1_{(-\varepsilon,\varepsilon)}}(t)\right|^2
 \left(
 \int_{p>t}|\widehat g(p)|^2\,dp+
 \int_{p<-t}|\widehat g(p)|^2\,dp
 \right)dt.
\end{aligned}
\]
Fubini yields
\[
 D_\varepsilon(g)^2
 =
 4\int_{\mathbb R}|\widehat g(p)|^2
 \int_0^{|p|}
 \frac2\pi\frac{\sin^2(\varepsilon t)}{t^2}\,dt\,dp.
\]
After \(u=\varepsilon t\),
\[
 \int_0^{|p|}
 \frac2\pi\frac{\sin^2(\varepsilon t)}{t^2}\,dt
 =
 \frac{2\varepsilon}{\pi}J(\varepsilon|p|),
\]
which proves the exact identity.

### 2. The half-Sobolev threshold

Since \(0\le(\sin u/u)^2\le1\),
\[
   0\le J(s)\le s,
   \qquad
   \frac{J(s)}s\longrightarrow1\quad(s\downarrow0).
\]
Thus
\[
 \frac{D_\varepsilon(g)^2}{\varepsilon^2}
 =
 \frac8\pi
 \int_{\mathbb R}
 |\widehat g(\xi)|^2
 \frac{J(\varepsilon|\xi|)}{\varepsilon}\,d\xi,
\]
and the integrand converges pointwise to
\[
   |\xi|\,|\widehat g(\xi)|^2.
\]
If the latter is integrable, dominated convergence applies because
\(J(\varepsilon|\xi|)/\varepsilon\le|\xi|\). If it is not integrable, Fatou's lemma gives
\[
   \liminf_{\varepsilon\downarrow0}D_\varepsilon(g)^2/\varepsilon^2=+\infty.
\]
This proves the extended-valued limit and the if-and-only-if \(\dot H^{1/2}\) characterization.
The normalized formula follows from
\[
 \|F_{\varepsilon,g}\|_2^2
 =
 \int_{\mathbb R}|g(y)|^2
 \left(\int_{|x-y|<\varepsilon}dx\right)dy
 =
 2\varepsilon\|g\|_2^2.
\]

### 3. Jump cutoffs

Let \(g\) be compactly supported and piecewise \(W^{1,1}\), with jumps \(\Delta_j\) at distinct
points \(x_j\). In the sense of distributions,
\[
   g'=h+\sum_j\Delta_j\delta_{x_j},
   \qquad h\in L^1(\mathbb R).
\]
Hence, by the Riemann--Lebesgue lemma,
\[
   i\xi\,\widehat g(\xi)
   =
   \widehat h(\xi)
   +\frac1{\sqrt{2\pi}}\sum_j\Delta_je^{-i\xi x_j}
   =
   \frac1{\sqrt{2\pi}}\sum_j\Delta_je^{-i\xi x_j}+o(1).
\]
It follows that
\[
 \int_{1<|\xi|<R}|\xi|\,|\widehat g(\xi)|^2\,d\xi
 =
 \frac{S(g)}{\pi}\log R+o(\log R).
\]
Indeed, the diagonal terms contribute
\((S(g)/\pi)\log R\); for distinct \(x_j-x_k\), the cross terms contain
\(\int_1^R e^{-i\xi(x_j-x_k)}\,d\xi/\xi=O(1)\), while the \(o(1)\) Fourier remainder contributes
\(o(\log R)\).

Write
\[
   L(s)=\frac{J(s)}s,\qquad L(0)=1.
\]
Then \(0\le L\le1\), \(L(s)\to1\) as \(s\downarrow0\), and \(L(s)\lesssim s^{-1}\) for \(s\ge1\).
The exact identity becomes
\[
 \frac{D_\varepsilon(g)^2}{\varepsilon^2}
 =
 \frac8\pi
 \int_{\mathbb R}
 |\xi|\,|\widehat g(\xi)|^2L(\varepsilon|\xi|)\,d\xi.
\]
The logarithmic spectral asymptotic above, together with the bounds on \(L\), gives
\[
 \int_{\mathbb R}
 |\xi|\,|\widehat g(\xi)|^2L(\varepsilon|\xi|)\,d\xi
 =
 \frac{S(g)}{\pi}\log\frac1\varepsilon\,(1+o(1)).
\]
Therefore
\[
 D_\varepsilon(g)^2
 =
 \frac{8S(g)}{\pi^2}
 \varepsilon^2\log\frac1\varepsilon\,(1+o(1)).
\]

For \(g=\mathbf 1_{(-1,1)}\), there are two jumps of modulus one, so \(S(g)=2\), while
\(\|g\|_2^2=2\). Thus
\[
 D_\varepsilon(g)^2
 =
 \frac{16}{\pi^2}\varepsilon^2\log\frac1\varepsilon\,(1+o(1)),
 \qquad
 \|F_{\varepsilon,g}\|_2^2=4\varepsilon,
\]
which gives the constant \(2/\pi\) in the normalized defect.

## Consequences

The cutoff direction of the approximate eigenstrip has a precise regularity law. A hard longitudinal
jump is exactly borderline for the half-Sobolev energy and creates the logarithm. Replacing the hard
cutoff by any nonzero \(g\in\dot H^{1/2}\cap L^2\) removes that logarithm and yields the normalized
rate \(\asymp\sqrt{\varepsilon}\), with an explicit leading constant.

For indicator cutoffs of finite unions of intervals, the leading logarithmic coefficient depends only
on the number of boundary jumps (equivalently, twice the number of interval components), not on their
locations.

## Limitations

This result analyzes the diagonal-strip truncation mechanism and \(L^2\) cutoff profiles. Except when
\(g\) itself is an indicator, the profile \(F_{\varepsilon,g}\) is not an indicator of a set. It does not
classify near-invariant sets, does not solve the quantitative stability question posed in
arXiv:2609.15155, and does not address nonlinear bent-strip families. No claim is made about the best
possible defect among all bounded sets of a prescribed measure.

Originality is asserted only to the best of our knowledge. The direct source is extremely recent, and
the exact identity is a natural Fourier refinement of its computation; an equivalent formulation could
therefore exist in unindexed contemporaneous work or in older product-Hardy-space language not located
by the searches described in `REVIEW.md`.

## References

1. E. Abakumov, K. Domelevo, S. Petermichl, A. Poltoratski,
   *Invariant sets of the double Hilbert transform*, arXiv:2609.15155 (2026),
   https://arxiv.org/abs/2609.15155.
2. C. Fefferman, *Estimates for double Hilbert transform*, Studia Math. 44 (1972), 1--15,
   https://doi.org/10.4064/sm-44-1-1-15.
