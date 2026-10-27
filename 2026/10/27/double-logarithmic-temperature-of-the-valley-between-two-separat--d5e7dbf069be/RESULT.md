# Double-logarithmic temperature of the valley between two separated Schottky anomalies

## Finding

For two independent equally weighted, nondegenerate two-level subsystems of respective excitation gaps \(\Delta>0\) and \(r\Delta\), with \(r>1\), let \(C_r(T)\) denote their total equilibrium heat capacity. As \(r\to\infty\), this two-scale heat-capacity curve has a **uniquely identified intermediate valley** whose inverse-temperature position is

\[
\frac{r\Delta}{k_BT_{\mathrm{val}}}=2\log r+\log\log r+\log4+o(1).
\]

Its dimensionless height obeys

\[
\frac{C_r(T_{\mathrm{val}})}{k_B}\sim\frac{(\log r)^2}{r^2}.
\]

More precisely, for every sufficiently large \(r\) there is exactly one stationary point whose coordinate \(y=r\Delta/(k_BT)\) lies in \((\log r,3\log r)\); it is a strict local minimum, with a local heat-capacity maximum on either side. Uniqueness is asserted *within this explicit intermediate window*, not as an unsupported classification of every stationary point for every finite gap ratio.

## Assumptions and scope

Take a tensor product of two noninteracting two-level quantum systems, each with energy levels \(\{0,\Delta_j\}\), one subsystem per type, with \(\Delta_1=\Delta\), \(\Delta_2=r\Delta\), \(\Delta>0\), \(r>1\). Degeneracies are one and the two subsystems have equal multiplicity (one copy each). Temperature \(T>0\), Boltzmann constant \(k_B>0\), and \(x=\Delta/(k_BT)>0\). The partition function is \(Z=(1+e^{-x})(1+e^{-rx})\). Define

\[
f(z)=\frac{z^2}{4\cosh^2(z/2)},\qquad F_r(x)=\frac{C_r(T)}{k_B}=f(x)+f(rx).
\]

The minima in temperature and inverse temperature correspond because \(T\mapsto x\) is a smooth strict monotone bijection. All limiting statements hold for real \(r\to+\infty\); the unspecified threshold for sufficiently large \(r\) is not claimed sharp.

## Proof

**1. Exact heat capacity and derivative.** From \(C=k_B\beta^2\partial_\beta^2\log Z\), or by independent two-state variances, the above expression for \(F_r\) is exact. Direct differentiation yields

\[
f'(z)=f(z)\left(\frac2z-\tanh\frac z2\right).
\]

The unique positive zero \(z_0\) of \(f'\) satisfies \(z_0\tanh(z_0/2)=2\), since the left side increases strictly from zero to infinity. Thus \(f'(z)>0\) for \(0<z<z_0\) and \(f'(z)<0\) for \(z>z_0\). In the intermediate variable \(y=rx\), the critical equation becomes

\[
G_r(y):=f'(y/r)+r f'(y)=0.
\]

**2. Uniform sign and uniqueness on an expanding interval.** Let \(L=\log r\) and \(I_r=[L,3L]\). Uniformly for \(y\in I_r\) as \(r\to\infty\), Taylor expansion at zero and exponential expansion at infinity give

\[
f'(y/r)=\frac{y}{2r}\left(1+O((L/r)^2)\right),
\qquad -f'(y)=y^2e^{-y}\left(1-\frac2y+O(e^{-y})\right).
\]

The latter remains strictly positive on \(I_r\) for sufficiently large \(r\). Define the positive ratio

\[
R_r(y)=\frac{f'(y/r)}{-r f'(y)}.
\]

Uniformly on \(I_r\),

\[
R_r(y)=\frac{e^y}{2r^2y}\left(1+O(L^{-1})+O((L/r)^2)\right).
\]

At \(y=L\) this tends to zero, while at \(y=3L\) it tends to infinity. The corresponding logarithmic-derivative expansion is uniform on \(I_r\):

\[
\frac{d}{dy}\log R_r(y)
=\frac1y+O(L/r^2)-\left(\frac2y-1+O(y^{-2})+O(e^{-y})\right)
=1-\frac1y+o(1)>0.
\]

Here the first logarithmic derivative is calculated from the small-argument expansion of \(f'\), and the second from the large-argument expansion of \(-f'\). Therefore \(R_r\) increases strictly from below one to above one and crosses one exactly once in \(I_r\). As \(G_r(y)=[-r f'(y)](R_r(y)-1)\), its sign changes from negative to positive there. Hence the unique intermediate critical point is a strict local minimum of \(F_r\).

**3. Position and height.** At this root \(y_r\), the ratio equation gives

\[
e^{y_r}=2r^2y_r\left(1+O(y_r^{-1})+O((L/r)^2)\right).
\]

Taking logarithms, \(y_r=2L+\log(2y_r)+o(1)\). The bounds \(L<y_r<3L\) first imply \(y_r=2L+O(\log L)\), and substitution then gives \(\log(2y_r)=\log L+\log4+o(1)\). Thus

\[
y_r=2\log r+\log\log r+\log4+o(1).
\]

At the root, \(f(y_r/r)=y_r^2/(4r^2)(1+o(1))\), while the stationary relation implies \(f(y_r)=y_r/(2r^2)(1+o(1))\). Consequently

\[
F_r(y_r/r)=\frac{y_r^2}{4r^2}(1+o(1))\sim\frac{(\log r)^2}{r^2}.
\]

Inverting the definition of \(y\) yields the temperature law in the Finding section.

**4. A peak on each side.** Fix any small \(\varepsilon\in(0,z_0/2)\). Near \(y=z_0\pm\varepsilon\), the term \(r f'(y)\) dominates \(f'(y/r)\), and the derivative changes from positive to negative, giving a local maximum with \(y=O(1)\), to the left of the valley. Near \(x=z_0\pm\varepsilon\), \(f'(x)\) dominates \(r f'(rx)\), whose magnitude decays exponentially in \(r\); this yields a second local maximum with \(x=O(1)\), to the right. No assertion of uniqueness of these peaks outside the intermediate window is needed.

## Verification

The attached standalone Python-standard-library checker independently evaluates the exact derivative, brackets the intermediate stationary point by bisection for seven ratios, checks the derivative changes from negative to positive, and compares both the double-log location and valley-height scaling. All 42 finite diagnostics passed. Computation only illustrates the theorem; it is not a proof of the unbounded-\(r\) limits. To replay: `python3 verify_schottky.py`.

## Relationship to prior work

The single-gap Schottky heat-capacity formula and its unique single-peak location are standard. Mahdavifar and Akbari (public preprint dated 2008-03-31) derive and use the one-gap formula to track a peak in quantum spin chains. Its original, accessible full manuscript treats one effective gap at a time, not the isolated minimum of a sum with two parametrically separated gaps. Experimental dual Schottky-scale features are reported in Pavlosiuk et al. (2016), but the retrieved description involves crystalline-field and nuclear scales, not a mathematical asymptotic theorem for equal-weight noninteracting TLS pairs. The newly assessed claim is the unique intermediate stationary point **within the logarithmic window** and its \(\log\log r+\log4\) correction, not the known two-level formula or the mere possibility of two peaks.

## Limitations

The result applies only to two independent, identically numerous, nondegenerate two-level constituents with a large gap ratio. Arbitrary multiplicities, interactions, non-two-level spectra, lattice backgrounds, and finite-gap-ratio threshold classifications are not covered. The estimate specifies an asymptotic regime rather than a sharp finite threshold. No experimental applicability, exclusion of all other stationary points, or historical-priority certainty is asserted. Other historical work might contain an equivalent scale separation calculation.

## References

1. S. Mahdavifar and A. Akbari, *Heat capacity of Schottky type in low-dimensional spin system*, arXiv:0803.4495, first public 2008-03-31. https://arxiv.org/abs/0803.4495
2. O. Pavlosiuk et al., *Antiferromagnetism and superconductivity in the half-Heusler semimetal HoPdBi*, Scientific Reports 6, 18797 (published 2016-01-05), DOI:10.1038/srep18797. https://www.nature.com/articles/srep18797
3. *MSC2020 Classification*, code 82B30, Statistical thermodynamics. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82-10
