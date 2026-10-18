# Sharp branching growth of graph-heat Lipschitz smoothing on double stars

## Finding

Let \(G_m\), for every integer \(m\ge2\), be the tree formed from two adjacent hubs, each joined to \(m\) distinct pendant vertices. Write \(L_m=D-A\) for its unnormalized, unit-conductance graph Laplacian and \(H_m(t)=\exp(-tL_m)\). Use the edge Lipschitz seminorm \(\operatorname{Lip}_{G_m}(g)=\max_{uv\in E(G_m)}|g(u)-g(v)|\) and the counting-measure sup norm on vertex functions. Define the optimal time-weighted smoothing constant

\[
\mathcal K_m=\sup_{t>0}\sqrt t\sup_{\|f\|_\infty\le1}\operatorname{Lip}_{G_m}(H_m(t)f).
\]

Set

\[
\Delta_m=\sqrt{(m+3)^2-8},\qquad
\lambda_-(m)=\frac{m+3-\Delta_m}{2}
=\frac4{m+3+\Delta_m},\qquad
\lambda_+(m)=\frac{m+3+\Delta_m}{2}.
\]

**Exact bridge-edge norm.** For every \(m\ge2\) and \(t\ge0\), the sharp norm of the signed derivative across the edge joining the hubs is

\[
B_m(t)=2\left[
\frac{m+1-\lambda_-}{\Delta_m}e^{-\lambda_-t}
+\frac{2-\lambda_-}{\Delta_m}e^{-\lambda_+t}
\right].
\]

It is attained by the input equal to \(+1\) on the left hub and all its leaves, and \(-1\) on the right hub and its leaves. The two coefficients in brackets are strictly positive and sum to one.

**Sharp growth and localization.** The full edge-Lipschitz smoothing constants satisfy

\[
\boxed{\lim_{m\to\infty}\frac{\mathcal K_m}{\sqrt m}=e^{-1/2}.}
\]

For every sufficiently large \(m\), only the hub-to-hub edge realizes the maximum over edges at an optimizing time. Every maximizing time \(t_m\) then satisfies

\[
\boxed{\lim_{m\to\infty}\frac{t_m}{m}=\frac14.}
\]

In particular, no universal bound \(\operatorname{Lip}_G(e^{-tL_G}f)\le C t^{-1/2}\|f\|_\infty\) can hold with one finite \(C\) for all finite unit-edge trees of diameter three and their unnormalized combinatorial Laplacians. The best constant on \(G_m\) grows as \(e^{-1/2}\sqrt m\).

## Assumptions and scope

Every edge has unit conductance; the vertex measure is counting measure, rather than degree measure. In particular \(L_m f(v)=\sum_{w\sim v}(f(v)-f(w))\), and this is not the random-walk degree-normalized Laplacian. The underlying continuous-time Markov semigroup is symmetric and preserves constants. The parameter \(m\) counts leaves **on each** side; \(G_m\) has \(2m+2\) vertices, maximum degree \(m+1\), and diameter exactly three. The input functions are arbitrary real vertex functions. The Lipschitz seminorm is taken in the graph shortest-path metric, equivalently as the maximum single-edge difference. Norm optimization is over all \(t>0\).

## Proof

**1. Dual characterization.** Symmetry of the heat matrix and elementary \(\ell^\infty\)-\(\ell^1\) duality show, for an oriented edge \(uv\),

\[
\sup_{\|f\|_\infty\le1}|(H_m(t)f)(u)-(H_m(t)f)(v)|
=\|H_m(t)(\delta_u-\delta_v)\|_1.
\]

The edge orbits are the bridge and the pendant edges. Thus it suffices to estimate one representative of each.

**2. The bridge edge.** Let \(u,v\) be the left and right hubs, respectively. By symmetry, the vector \(H_m(t)(\delta_u-\delta_v)\) has value \(h(t)\) at the left hub, value \(a(t)\) at each left leaf, and their negatives at the corresponding right vertices. Directly from the unnormalized graph Laplacian,

\[
\binom{h'}{a'}=
\begin{pmatrix}-(m+2)&m\\1&-1\end{pmatrix}\binom{h}{a},\qquad
(h(0),a(0))=(1,0).
\]

The generator matrix has nonnegative off-diagonal entries, so \(h(t),a(t)\ge0\). Its decay rates are the two roots of \(\lambda^2-(m+3)\lambda+2=0\), namely \(\lambda_\pm\). Consequently the sharp bridge norm is \(2(h(t)+ma(t))\). Writing \(h+ma=c_-e^{-\lambda_-t}+c_+e^{-\lambda_+t}\), the values \((h+ma)(0)=1\) and \((h+ma)'(0)=-2\) give

\[
c_-=(m+1-\lambda_-)/\Delta_m,\qquad c_+=(2-\lambda_-)/\Delta_m.
\]

Both are positive. The sign of the bridge vector is positive throughout the left half and negative throughout the right half, proving the asserted sign-function extremizer.

**3. Pendant-edge control with an explicit two-rate remainder.** Fix the left hub \(u\) and one adjacent leaf \(z\). Let \(\bar\ell_L\) and \(\bar\ell_R\) be the arithmetic means of the point masses on the left and right leaf sets. Decompose

\[
\delta_u-\delta_z
=(\bar\ell_L-\delta_z)
+\tfrac12(\delta_u+\delta_v-\bar\ell_L-\bar\ell_R)
+\tfrac12(\delta_u-\delta_v-\bar\ell_L+\bar\ell_R).
\]

The first component is a Laplacian eigenvector of eigenvalue \(1\), with \(\ell^1\)-norm \(2(1-1/m)\). The second is an eigenvector of eigenvalue \(m+1\), with \(\ell^1\)-norm \(2\). The third lies in the antisymmetric two-dimensional invariant subspace in step 2. Its left-leaf coordinate begins at \(-1/(2m)\), its left-hub coordinate at \(1/2\), and the left-leaf coefficient of a \(\lambda\)-eigenmode is multiplied by \(1-\lambda\) at the hub. Solving the two initial-value equations gives modal left-leaf coefficients

\[
d_-=(\lambda_--2)/(2m\Delta_m),\qquad
d_+=(2-\lambda_+)/(2m\Delta_m).
\]

Triangle inequality on the four contributions now gives, for every \(t\ge0\),

\[
C_m^{\mathrm{leaf}}(t):=\|H_m(t)(\delta_u-\delta_z)\|_1
\le 2(1-1/m)e^{-t}+2e^{-(m+1)t}
+A_m e^{-\lambda_-t}+R_m e^{-\lambda_+t},
\]

where

\[
A_m=\frac{(2-\lambda_-)(m+1-\lambda_-)}{m\Delta_m},
\qquad
R_m=\frac{(\lambda_+-2)(m+\lambda_+-1)}{m\Delta_m}.
\]

For every \(m\ge2\), direct comparison of \(m+1\le\Delta_m\le m+3\) gives

\[
\frac2{m+3}\le\lambda_-\le\frac2{m+2},\qquad
\lambda_+\ge m+2,\qquad
A_m\le\frac2m,\qquad R_m\le3.
\]

Using \(\sup_{t>0}\sqrt t\,e^{-rt}=(2er)^{-1/2}\), we obtain

\[
\sup_{t>0}\sqrt t\,C_m^{\mathrm{leaf}}(t)
\le\frac2{\sqrt{2e}}+\frac2{\sqrt{2e(m+1)}}
+\frac{2}{m\sqrt{2e\lambda_-}}
+\frac3{\sqrt{2e\lambda_+}}=O(1),
\]

where the implicit bound is uniform over \(m\ge2\). Hence pendant edges cannot produce a contribution of order \(\sqrt m\).

**4. Sharp bridge scaling.** By the explicit spectral formula, \(m\lambda_-\to2\), \(c_-\to1\), \(c_+\to0\) as \(m\to\infty\). For every \(s>0\),

\[
B_m(ms)\longrightarrow2e^{-2s},\qquad
\sqrt s\,B_m(ms)\longrightarrow2\sqrt s\,e^{-2s}.
\]

For matching optimization upper and lower bounds, separate the two exponential terms and apply the preceding sharp scalar exponential maximum:

\[
\sup_{t>0}\sqrt t B_m(t)
\le\frac{2c_-}{\sqrt{2e\lambda_-}}+
\frac{2c_+}{\sqrt{2e\lambda_+}},
\]

while evaluating at \(t=1/(2\lambda_-)\) gives the lower bound

\[
\sup_{t>0}\sqrt t B_m(t)
\ge\frac{2c_-}{\sqrt{2e\lambda_-}}.
\]

The first term divided by \(\sqrt m\) converges to \(e^{-1/2}\), and the second does not contribute in that scaling. Combined with step 3, this proves the sharp constant for the full Lipschitz norm.

**5. Location and time of the maximizer.** The time-weighted norms vanish as \(t\downarrow0\) (the heat operators are uniformly bounded) and as \(t\to\infty\) (every signed edge mass has zero sum and lies in positive Laplacian eigenspaces). Thus maxima occur at finite positive times. The pendant-edge supremum in step 3 is uniformly bounded, whereas the bridge maximum diverges as \(e^{-1/2}\sqrt m\). Consequently, for all sufficiently large \(m\), the maximizing edge is necessarily the bridge.

For any maximizing bridge time \(t_m\), put \(s_m=t_m/m\). The bound \(B_m(t)\le2\) rules out \(s_m\to0\) at the sharp scale. Since \(\lambda_-m\to2\) and \(B_m(t)\le2e^{-\lambda_-t}\), the maximizing property rules out \(s_m\to\infty\). Every subsequential limit \(s\in(0,\infty)\) maximizes \(2\sqrt s\,e^{-2s}\), whose unique maximum is at \(s=1/4\). Hence \(t_m/m\to1/4\).

## Verification

The accompanying standard-library Python script `verify.py` independently constructs finite bistar heat vectors by Poisson uniformization of the Markov matrix, without diagonalizing the same two-dimensional reduced system. It checks the exact bridge norm, signed-mass structure and rigorous pendant-edge upper bound for leaf multiplicities \(2\le m\le12\), and probes the stated asymptotic scalings at larger multiplicities. Executing `python verify.py` yielded `PASS: 542 finite deterministic assertions (no external dependencies)`. Numerical tests are evidence for finite instances only; the universal and limiting statements are proved in the previous section.

## Relationship to prior work

Bauer, Horn, Lin, Lippner, Mangoubi and Yau (2013 preprint; 2015 publication) establish curvature-dependent Li–Yau type estimates and related heat-kernel/gradient bounds on graphs, with unweighted and degree-weighted vertex-measure conventions distinguished. Their results do not identify the sharp bounded-input-to-edge-Lipschitz norm for this unnormalized bistar family. Horn's later Hamilton-type spatial estimate concerns positive heat solutions and curvature assumptions, not the optimized signed-data endpoint norm computed here.

Münch and Wojciechowski (2017 preprint) characterize curvature lower bounds by \(\operatorname{Lip}(H_t f)\le e^{-Kt}\operatorname{Lip}(f)\), a Lipschitz-input-to-Lipschitz-output estimate. That theorem does not fix the sharp bounded-input norm or optimize its time on the present graph family.

De Ponti and Stefani (2024 preprint) explicitly formulate the optimal \(L^\infty\)-to-Lipschitz smoothing function and develop general consequences of its bounds. Their analysis does not compute the sharp growing-degree constant on combinatorial double stars. The result here is a family-specific determination of that optimal function's leading time-weighted norm and the unique maximizing edge orbit for sufficiently large multiplicity. A spectral-gap calculation alone gives \(\lambda_-\sim2/m\), but does not determine the \(\ell^1\)-size or sign pattern of a heat-evolved edge mass, the sharp factor \(e^{-1/2}\), or the competition with pendant edges.

## Limitations

The exact all-time formula is for the hub-to-hub edge. For pendant edges, only an explicit sufficient upper bound is used; there is no claimed closed all-time expression for the full norm at every finite \(m\). The eventual bridge-maximization threshold is not numerically identified. The theorem is for symmetric double stars with equally many leaves on both sides, unit conductances, counting measure, and the unnormalized Laplacian; no corresponding assertion is made for random-walk normalization, arbitrary trees, or asymmetric pairs of stars. Historical priority has not been independently certified; comparable special-family total-variation calculations under alternate terminology remain a residual bibliographic risk.

## References

1. F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi and S.-T. Yau, *Li-Yau inequality on graphs*, arXiv:1306.2561, first publicly posted 2013-06-11; Journal of Differential Geometry **99** (2015), 359–405. DOI: 10.4310/jdg/1424880980.
2. P. Horn, *A Spacial Gradient Estimate for Solutions to the Heat Equation on Graphs*, SIAM Journal on Discrete Mathematics, DOI: 10.1137/16M1091988; author full text: https://cs.du.edu/~paulhorn/pap/hg.pdf.
3. N. De Ponti and G. Stefani, *Properties of Lipschitz smoothing heat semigroups*, arXiv:2403.00620; see Definition 3.1 and Section 4 on sharp smoothing profiles. The 2024 paper supplies later supporting context, not the archival date anchor.
4. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (2017), especially Theorem 3.8 on Lipschitz-to-Lipschitz contraction.
