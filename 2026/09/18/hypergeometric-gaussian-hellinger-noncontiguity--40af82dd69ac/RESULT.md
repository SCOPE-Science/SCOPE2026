# Gaussian-boundary hypergeometric laws: sharp Hellinger rate and root-n noncontiguity

## Statement

Let \(P_a\) denote the Gaussian-nested hypergeometric law of Lawford with
\[
c=\frac32+a,\qquad a\ge 0,
\]
so that \(P_0=N(0,1)\). For \(a>0\), its density has the beta-precision representation
\[
g_a(x)=\frac{a}{\sqrt{2\pi}}\int_0^1
\lambda^{1/2}(1-\lambda)^{a-1}e^{-\lambda x^2/2}\,d\lambda.
\]
Write \(\phi\) for the standard normal density and
\[
H^2(P,Q)=\int_{\mathbb R}(\sqrt p-\sqrt q)^2\,dx
\]
for the squared Hellinger distance in the convention \(0\le H^2\le2\).

### Theorem 1: logarithmic Hellinger geometry

As \(a\downarrow0\), with \(L_a=\log(1/a)\),
\[
\boxed{
H^2(P_a,P_0)
=
\frac{a}{2L_a}\{1+o(1)\}.
}
\]
Equivalently, the Hellinger affinity satisfies
\[
\int_{\mathbb R}\sqrt{g_a(x)\phi(x)}\,dx
=
1-\frac{a}{4L_a}\{1+o(1)\}.
\]

Thus the Gaussian boundary is substantially more singular than a regular quadratic-mean path: the first Hellinger separation is of order \(a/\log(1/a)\), not \(a^2\).

For every fixed \(a>0\),
\[
D(P_a\Vert P_0)=\infty,
\qquad
\chi^2(P_a\Vert P_0)=\infty.
\]
These divergences coexist with \(H(P_a,P_0)\to0\) as \(a\downarrow0\).

### Theorem 2: the iid information boundary

Let \(a_n\downarrow0\), let \(P_{a_n}^{\,n}\) denote \(n\) iid observations, and define
\[
\gamma_n=\frac{n a_n}{\log(1/a_n)}.
\]
If \(\gamma_n\to\gamma\in[0,\infty)\), then
\[
\int\sqrt{dP_{a_n}^{\,n}\,dP_0^{\,n}}
\longrightarrow e^{-\gamma/4},
\]
and hence
\[
H^2(P_{a_n}^{\,n},P_0^{\,n})
\longrightarrow
2(1-e^{-\gamma/4}).
\]
Consequently:

- if \(\gamma_n\to0\), then
  \[
  \|P_{a_n}^{\,n}-P_0^{\,n}\|_{\rm TV}\to0;
  \]
- if \(\gamma_n\to\infty\), then
  \[
  \|P_{a_n}^{\,n}-P_0^{\,n}\|_{\rm TV}\to1.
  \]

In particular, the simple-vs-simple detection boundary is
\[
\boxed{
a_n\asymp\frac{\log n}{n}.
}
\]
More precisely, for \(a_n=\kappa(\log n)/n\) with fixed \(\kappa>0\),
\[
H^2(P_{a_n}^{\,n},P_0^{\,n})
\longrightarrow
2(1-e^{-\kappa/4}).
\]

### Theorem 3: a critical extreme-value profile

For \(a_n=\kappa(\log n)/n\), let
\[
M_n=\max_{1\le i\le n}|X_{i,n}|,
\qquad X_{i,n}\stackrel{\rm iid}{\sim}P_{a_n}.
\]
Then
\[
\frac{M_n^2}{2\log n}\Rightarrow Y_\kappa,
\]
where
\[
\Pr(Y_\kappa\le y)=
\begin{cases}
0,&y<1,\\[1mm]
\exp\{-\kappa/(2y)\},&y\ge1.
\end{cases}
\]
The limit has an atom of mass \(e^{-\kappa/2}\) at \(y=1\), followed by a continuous heavy-tail component on \((1,\infty)\).

### Theorem 4: root-\(n\) CDF locality is not experiment locality

Lawford studies the fixed-scale minimum-distance statistic
\[
Q_n(c)=\int\{\widehat F_n(z)-G_c(z)\}^2\,d\nu(z)
\]
and its standardized fit-improvement statistic \(\widetilde T_n\), where \(\nu\) is a fixed finite measure satisfying the stated regularity assumptions.

If
\[
a_n=o(n^{-1/2}),
\]
then under \(P_{a_n}^{\,n}\),
\[
\widetilde T_n
\Rightarrow
\frac12\delta_0+\frac12\chi_1^2,
\]
the same first-order limit as under the Gaussian null. Therefore the corresponding asymptotic level-\(\alpha\) minimum-distance test has limiting power \(\alpha\) throughout this regime. In particular, it is first-order blind at the Hellinger-critical scale
\[
a_n=\kappa\frac{\log n}{n}.
\]
More strongly, whenever
\[
\frac{n a_n}{\log(1/a_n)}\to\infty
\qquad\text{and}\qquad
\sqrt n\,a_n\to0,
\]
the full iid experiments satisfy total-variation distance tending to one while the minimum-distance statistic still has its null first-order law. For example, this occurs for \(a_n=n^{-3/4}\).

At the apparently larger "local" scale
\[
a_n=\frac{\tau}{\sqrt n},\qquad \tau>0,
\]
the experiments are instead asymptotically separated:
\[
\|P_{\tau/\sqrt n}^{\,n}-P_0^{\,n}\|_{\rm TV}\to1.
\]
Indeed, for any fixed \(\varepsilon>0\),
\[
A_n=
\left\{
\max_i|X_i|>
\sqrt{2(1+\varepsilon)\log n}
\right\}
\]
satisfies
\[
P_0^{\,n}(A_n)\to0,
\qquad
P_{\tau/\sqrt n}^{\,n}(A_n)\to1.
\]
Thus \(P_{\tau/\sqrt n}^{\,n}\) is not contiguous to \(P_0^{\,n}\).

This does not contradict a root-\(n\) empirical-CDF expansion: the body of the CDF can have an \(n^{-1/2}\) deterministic drift while rare extreme observations already separate the full statistical experiments. It does show that root-\(n\) hypergeometric alternatives are not local in the likelihood/contiguity sense, and that the minimum-distance local-power scale is much coarser than the information-theoretic detection scale.

## Proof

### 1. A tail lemma from the precision mixture

For \(X_a\sim P_a\),
\[
\Pr(|X_a|>x)
=
a\int_0^1
2\bar\Phi(x\sqrt\lambda)(1-\lambda)^{a-1}\,d\lambda.
\]
With \(t=x^2\lambda\),
\[
\Pr(|X_a|>x)
=
\frac{a}{x^2}
\int_0^{x^2}
2\bar\Phi(\sqrt t)
\left(1-\frac{t}{x^2}\right)^{a-1}dt.
\]
The identity
\[
\int_0^\infty2\bar\Phi(\sqrt t)\,dt=1
\]
follows from
\[
\int_0^\infty4u\bar\Phi(u)\,du
=2\,\mathbb E[(Z_+)^2]=1.
\]

Let \(L=\log(1/a)\). If
\[
x^2=2L+d\log L+O(1)
\]
for any fixed \(d>1\), the contribution from precision values bounded away from zero is negligible compared with \(a/x^2\), while on the small-precision region the factor
\((1-t/x^2)^{a-1}\) converges uniformly on bounded \(t\)-sets to one. Splitting the integral at a fixed large \(t\), then sending that cutoff to infinity, gives
\[
\boxed{
\Pr(|X_a|>x)
=
\frac{a}{x^2}\{1+o(1)\}
}
\]
uniformly for the specific logarithmic windows used below.

This is the uniform form of the fixed-\(a\) survival law
\(\Pr(|X_a|>x)\sim a/x^2\).

### 2. Hellinger mass is created beyond the Gaussian-to-polynomial crossover

Set
\[
s_a^2=2L+2\log L,\qquad
r_a^2=2L+6\log L.
\]
The Gaussian tail at either cutoff is \(o(a/L)\), while the tail lemma gives
\[
P_a(|X|>s_a)\sim\frac{a}{s_a^2},
\qquad
P_a(|X|>r_a)\sim\frac{a}{r_a^2}
\sim\frac{a}{2L}.
\]
Moreover,
\[
P_a(s_a<|X|\le r_a)
=
O\!\left(\frac{a\log L}{L^2}\right)
+o(a/L).
\]

It remains to show that the central Hellinger contribution is smaller. The density ratio has the exact representation
\[
R_a(x):=\frac{g_a(x)}{\phi(x)}
=
a\int_0^1
(1-u)^{1/2}u^{a-1}e^{ux^2/2}\,du.
\]
Subtracting
\(a\int_0^1u^{a-1}du=1\), splitting the integral near the two endpoints, and using a one-sided Laplace bound at \(u=1\) gives, uniformly for \(|x|\le s_a\),
\[
|R_a(x)-1|
\le
C a(1+x^2)
+
C a\frac{e^{x^2/2}}{(1+x^2)^{3/2}}.
\]
The right-hand side is \(o(1)\) uniformly on this interval. Hence
\[
(\sqrt{R_a}-1)^2\le C(R_a-1)^2,
\]
and Gaussian integration yields
\[
\int_{|x|\le s_a}
\phi(x)(\sqrt{R_a(x)}-1)^2\,dx
=
O(a^2)+O(aL^{-5/2})
=
o(a/L).
\]

On \(s_a<|x|\le r_a\), use
\[
(\sqrt{g_a}-\sqrt\phi)^2\le g_a+\phi
\]
and the preceding tail estimates to obtain another \(o(a/L)\) contribution.

Finally let \(A_a=\{|x|>r_a\}\). Then
\[
P_a(A_a)\sim\frac{a}{2L},
\qquad
P_0(A_a)=o(a/L),
\]
and Cauchy-Schwarz gives
\[
\int_{A_a}\sqrt{g_a\phi}
\le
\sqrt{P_a(A_a)P_0(A_a)}
=o(a/L).
\]
Therefore
\[
H^2(P_a,P_0)
=
P_a(A_a)+o(a/L)
=
\frac{a}{2L}\{1+o(1)\},
\]
proving Theorem 1.

The fixed-\(a\) algebraic density tail \(g_a(x)\sim a|x|^{-3}\) also gives
\[
g_a(x)\log\frac{g_a(x)}{\phi(x)}
\sim
\frac{a}{2|x|}
\]
up to lower-order logarithmic terms on each tail, so
\(D(P_a\Vert P_0)=\infty\). Likewise \(g_a^2/\phi\) is nonintegrable, giving infinite chi-square divergence.

### 3. Tensorization gives the statistical detection boundary

If
\[
\rho_a=\int\sqrt{g_a\phi}
=1-\frac12H^2(P_a,P_0),
\]
then iid tensorization is exact:
\[
\rho(P_a^{\,n},P_0^{\,n})=\rho_a^n.
\]
Theorem 1 gives
\[
\log\rho_a
=
-\frac{a}{4\log(1/a)}\{1+o(1)\}.
\]
The claims in Theorem 2 follow immediately. Standard inequalities between total variation and Hellinger distance give the indistinguishable and asymptotically singular regimes.

### 4. Critical maxima

Let \(a_n=\kappa(\log n)/n\) and
\[
x_n(y)=\sqrt{2y\log n}.
\]
For every fixed \(y\ge1\), the precision-mixture tail calculation gives
\[
P_{a_n}(|X|>x_n(y))
\sim
\frac{a_n}{x_n(y)^2}
=
\frac{\kappa}{2yn}.
\]
Thus
\[
\Pr(M_n\le x_n(y))
=
\{1-P_{a_n}(|X|>x_n(y))\}^n
\longrightarrow e^{-\kappa/(2y)}.
\]
For \(y<1\), the precision-mixture coupling \(|\varepsilon|/\sqrt\Lambda\ge|\varepsilon|\) implies a tail at least as large as the Gaussian tail, which already forces the maximum above that level with probability tending to one. This proves Theorem 3.

### 5. Minimum-distance blindness below the root-\(n\) CDF scale

Lawford proves uniform boundedness of \(\partial_cG_c\) and
\(\partial_c^2G_c\) in a neighbourhood of \(c=3/2\). Hence
\[
\sup_z|G_{3/2+a_n}(z)-\Phi(z)|=O(a_n).
\]
If \(\sqrt n\,a_n\to0\), then
\[
\sqrt n\{G_{3/2+a_n}-\Phi\}\to0
\]
uniformly.

For the empirical CDF under \(P_{a_n}\),
\[
\sqrt n(\widehat F_n-\Phi)
=
\sqrt n(\widehat F_n-G_{3/2+a_n})
+
\sqrt n(G_{3/2+a_n}-\Phi).
\]
The first term is the usual triangular-array empirical process and converges to a \(\Phi\)-Brownian bridge because
\(G_{3/2+a_n}\to\Phi\) uniformly; the second term vanishes. Thus the score of the minimum-distance criterion has exactly its null first-order limit.

The source paper's curvature argument also transfers directly: the empirical second derivative differs from its null population counterpart by a term bounded by the uniform CDF error times an integrable derivative envelope, while the null curvature is strictly positive. Uniform consistency of the criterion places its minimizer near the boundary. The same elementary quadratic lower bound used for boundary-estimator tightness therefore yields
\[
\sqrt n(\widehat c_n-3/2)=O_p(1)
\]
without any contiguity assumption. Localizing \(c=3/2+h/\sqrt n\) then gives the same null quadratic process and hence
\[
\widetilde T_n
\Rightarrow
\frac12\delta_0+\frac12\chi_1^2.
\]

At \(a_n=\kappa(\log n)/n\), this null first-order limit coexists with the nondegenerate product-Hellinger separation in Theorem 2.

Finally, if \(a_n=\tau/\sqrt n\) and
\[
b_n=\sqrt{2(1+\varepsilon)\log n},
\]
then under the Gaussian null
\[
nP_0(|Z|>b_n)\to0,
\]
whereas the precision-mixture tail gives
\[
nP_{a_n}(|X|>b_n)
\sim
\frac{\tau\sqrt n}{2(1+\varepsilon)\log n}
\to\infty.
\]
Hence the maximum event in Theorem 4 separates the two experiments, proving noncontiguity.

## Relation to the recent hypergeometric inference result

Lawford introduced this Gaussian-nested family, proved the algebraic tail and beta-precision representation, and explicitly noted that the model is not differentiable in quadratic mean at the Gaussian boundary. The same paper develops minimum-distance boundary inference and states local power for
\[
c_n=\frac32+\frac{\tau}{\sqrt n}.
\]

The present result quantifies the non-DQM boundary in an experiment-level metric. The Hellinger calculation shows that the actual simple-vs-simple information boundary is \((\log n)/n\), while the minimum-distance statistic operates on the coarser root-\(n\) CDF scale. It also shows that the root-\(n\) hypergeometric alternatives are not contiguous to the Gaussian null.

Accordingly, a contiguity sentence used in the proof of the general local-power theorem cannot justify the hypergeometric specialization at \(a_n=\tau/\sqrt n\). This observation does not by itself invalidate the displayed minimum-distance local-power formula: the required estimator tightness can be proved directly from the score and curvature argument. What fails is the interpretation of those alternatives as contiguous local experiments.

General sparse-mixture detection theory already shows that Hellinger geometry and extreme likelihood ratios can determine nonstandard detection boundaries. Heavy-tailed-impurity extreme-value theory likewise shows that vanishing heavy contamination can create discontinuous maximum limits. The claims here are therefore restricted to the sharp constant and logarithmic Hellinger law for this beta-precision hypergeometric path, the resulting \((\log n)/n\) boundary, its explicit maximum profile, and the separation between CDF locality and experiment locality for this newly introduced family.

## Limitations

- The sharp Hellinger calculation is for the standardized one-parameter family with fixed location and scale.
- No full likelihood-ratio limit experiment is identified at \(a_n=\kappa(\log n)/n\); the product Hellinger affinity and maximum profile are given instead.
- The maximum profile is a model-specific specialization of a mechanism already known in triangular heavy-tailed-impurity models.
- Plug-in location and scale, including the robust median/IQR procedure in the source paper, are not analyzed here.
- The result gives first-order Hellinger asymptotics but not a second-order expansion or a finite-sample error bound.
- Originality is to the best of our knowledge. General sparse-mixture detection and normal-scale-mixture literature may contain abstract results from which qualitative parts can be recovered; no inspected source gave the displayed sharp \(a/\log(1/a)\) constant or the consequences for this hypergeometric path.

## References

1. S. Lawford, *Gaussian Boundary Inference in a Hypergeometric Heavy-Tailed Family*, arXiv:2609.20393 (2026). https://arxiv.org/abs/2609.20393
2. T. T. Cai and Y. Wu, *Optimal detection of sparse mixtures against a given null distribution*, IEEE Transactions on Information Theory 60 (2014), 2217-2232. https://doi.org/10.1109/TIT.2014.2304295
3. E. Morozova and V. Panov, *Extreme Value Analysis for Mixture Models with Heavy-Tailed Impurity*, Mathematics 9 (2021), 2208. https://doi.org/10.3390/math9182208
