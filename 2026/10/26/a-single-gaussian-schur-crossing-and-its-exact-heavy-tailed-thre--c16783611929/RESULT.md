# A single Gaussian Schur crossing and its exact heavy-tailed threshold law

## Finding

Let \(a,b,c\) be independent standard circular complex Gaussian variables, each with density \(\pi^{-1}e^{-|w|^2}\) on \(\mathbb C\). For every \(s\ge0\), define
\[
P_s(z)=cz^2+s b z+a,\qquad
N_s=\#\{z:|z|<1,\ P_s(z)=0\},
\]
where roots are counted with multiplicity. Define, on the probability-one event of nondegeneracy,
\[
\Delta=|c|^2-|a|^2,\quad
B=b\overline c-a\overline b,\quad
T=\frac{|\Delta|}{|B|}.
\]
Then \(0<T<\infty\) almost surely and, *simultaneously for every \(s\ne T\)*,
\[
N_s=\begin{cases}
2,&0\le s<T,\ \Delta>0,\\
0,&0\le s<T,\ \Delta<0,\\
1,&s>T.
\end{cases}
\]
There is one unit-circle crossing at \(s=T\). The sign of \(\Delta\) is symmetric and independent of \(T\). The latter has exact cumulative distribution function and density
\[
\mathbb P(T\le s)=\frac{s}{\sqrt{s^2+2}}\quad(s\ge0),\qquad
f_T(s)=\frac{2}{(s^2+2)^{3/2}}\quad(s>0).
\]
Thus for each deterministic \(s\ge0\), with \(p_s=s/\sqrt{s^2+2}\),
\[
\mathbb P(N_s=0)=\mathbb P(N_s=2)=\frac{1-p_s}{2},\qquad
\mathbb P(N_s=1)=p_s,
\]
so \(\mathbb E N_s=1\) and \(\operatorname{Var}(N_s)=1-p_s\). For precisely \(-1<q<2\),
\[
\mathbb E[T^q]
=\frac{2^{q/2}\Gamma((q+1)/2)\Gamma(1-q/2)}{\sqrt\pi}.
\]
In particular \(\mathbb E T=\sqrt2\), \(\operatorname{med}(T)=\sqrt{2/3}\), and \(\mathbb E T^2=\infty\).

## Assumptions and scope

The coefficients are circular complex Gaussians, not real Gaussians, with independent real and imaginary parts each of variance \(1/2\). The same realization of \((a,b,c)\) is used for the entire amplitude path \(s\ge0\); this coupling is essential. The degree is exactly two almost surely. At the random isolated value \(s=T\), a root lies on the unit circle, so the strict open-disk count is not asserted by the displayed piecewise formula; for every fixed deterministic \(s\), this event has probability zero. All other roots are simple almost surely for any fixed \(s\). No higher-degree or non-Gaussian generalization is asserted.

## Proof

**1. A deterministic Schur crossing.** Write
\[
P_s^*(z)=z^2\overline{P_s(1/\overline z)}
=\overline a z^2+s\overline b z+\overline c.
\]
On \(|z|=1\), one has \(|P_s^*(z)|=|P_s(z)|\). The exact identity
\[
\overline c P_s(z)-aP_s^*(z)=z(\Delta z+sB)
\tag{1}
\]
holds. Suppose \(\Delta>0\), so \(|c|>|a|\). For \(s\ne T\), there cannot be a unit-circle root: such a root would make the right side of (1) vanish, requiring \(s|B|=|\Delta|\). Since \(|\overline cP_s|>|aP_s^*|\) on the unit circle at its nonzeros, Rouché's theorem and (1) imply
\[
N_s=1+\mathbf1_{\{s|B|<\Delta\}}
\qquad(\Delta>0,s\ne T).
\tag{2}
\]
Indeed the polynomial on the right of (1) has a zero at zero and another at \(-sB/\Delta\); for \(s=0\) the second root is also zero, counted twice. Conversely, at \(s=T\), choose \(z=-sB/\Delta\) on the unit circle. Identity (1) gives \(\overline cP_s(z)=aP_s^*(z)\). Taking moduli and using \(|P_s^*|=|P_s|\) forces \(P_s(z)=0\), because \(|c|\ne|a|\). Thus a boundary crossing occurs exactly there.

For \(\Delta<0\), apply the same reasoning to \(P_s^*\), which has leading-coefficient modulus \(|a|>|c|\) and whose corresponding \(B\) coefficient is \(-B\). Since its roots are reciprocal conjugates of the roots of \(P_s\), off the unit circle their counts add to two. Consequently
\[
N_s=1-\mathbf1_{\{s|B|<-\Delta\}}
\qquad(\Delta<0,s\ne T).
\tag{3}
\]
Combining (2) and (3) proves the pathwise classification and shows exactly one possible crossing.

**2. Gaussian decomposition.** Write \(b=\rho e^{i\psi}\), with \(\rho\ge0\). Then \(\rho^2\) is exponential of mean one. Conditional on \((\rho,\psi)\), let \(d=e^{2i\psi}\overline c\). Circular symmetry makes \(a,d\) independent standard complex Gaussians. Introduce the independent standard complex Gaussians \(u=(a+d)/\sqrt2\) and \(v=(a-d)/\sqrt2\). Direct calculation gives
\[
\Delta=-2\operatorname{Re}(u\overline v),\qquad
|B|=\sqrt2\rho|v|.
\]
On \(v\ne0\), put \(Z=\sqrt2\operatorname{Re}(u\overline v)/|v|\). Conditional on \(v\), \(Z\) is a standard *real* normal, with a conditional law independent of \(v\). It is independent of \(\rho\), and
\[
T=\frac{|Z|}{\rho},\qquad
\operatorname{sgn}\Delta=-\operatorname{sgn}Z.
\tag{4}
\]
The normal sign is fair and independent of its magnitude. This proves independence of \(\operatorname{sgn}\Delta\) from \(T\).

**3. Exact threshold law.** For \(s>0\), the exponential distribution of \(\rho^2\) and (4) yield
\[
\mathbb P(T\le s)
=\mathbb E\left[\mathbb P\left(\rho^2\ge Z^2/s^2\mid Z\right)\right]
=\mathbb E e^{-Z^2/s^2}
=\frac{s}{\sqrt{s^2+2}}.
\]
At \(s=0\) this probability is zero by continuity. Differentiation gives the stated density. Integrating the density after the substitution \(s=\sqrt2\,t\) gives
\[
\mathbb E T^q
=2^{q/2}\int_0^\infty\frac{t^q}{(1+t^2)^{3/2}}\,dt
=\frac{2^{q/2}\Gamma((q+1)/2)\Gamma(1-q/2)}{\sqrt\pi}.
\]
The integral converges at zero exactly for \(q>-1\), and at infinity exactly for \(q<2\). Finally the exact zero-count probabilities follow by conditioning on whether \(T\) is greater or smaller than \(s\), using the independent fair sign. Their mean and variance are immediate.

## Verification

The supplied stand-alone `verify_gaussian_quadratic.py` uses Python's standard library. Run `python3 verify_gaussian_quadratic.py` in the directory containing this document. With the recorded fixed seed it checks the root formula against the deterministic Schur classification for \(100{,}000\) coefficient triples at each of eight amplitudes, tests the empirical category proportions against the proved law, and directly checks both sides of the transition for \(5{,}000\) triples. These finite tests corroborate, but do not replace, the argument above. Gaussian normalization, reverse-polynomial algebra, reciprocal root counting, and the beta-integral convergence are explicitly checked analytically in the proof.

## Relationship to prior work

The deterministic Schur–Cohn method and the 2023 complex-trinomial Schur stability region provide background for (1), but do not, in the inspected portions, state a coupled random-amplitude transition law or its distribution. A 2023 probabilistic Eneström–Kakeya analysis treats different, real-Gaussian coefficient laws and probability bounds rather than the exact present complex-Gaussian distribution; available indexing and abstract were checked, but the full article could not be read, leaving a priority risk. Yakir's 2020 random Littlewood result studies asymptotic counts for long signed polynomials; the 2021 Gaussian Taylor-series paper studies infinite series. A 2023 public question notes the inversion-symmetric expected fraction of inside-disk zeros, which is weaker than the full count distribution and pathwise threshold established here. Claims of historical novelty remain conditional on more exhaustive source comparisons; neither the Schur criterion nor the simple expected-count symmetry is claimed new.

## Limitations

The pathwise statement is almost sure and explicitly excludes the random boundary event \(s=T\). The constant \(2\) in the distribution depends on the specified circular-Gaussian normalization and equal coefficient variances; no assertion is made for dependent, noncircular, real, or other variances without modification. This is a self-reviewed mathematical argument and has not received an independent audit. A possible previously published equivalent formulation under Schur stability or random-polynomial zero-count terminology remains a historical-priority risk.

## References

1. *The stability region for Schur stable trinomials with general complex coefficients*, arXiv:2304.09147, first posted 2023-04-18, https://arxiv.org/abs/2304.09147.
2. *A Probabilistic Version of Eneström–Kakeya Theorem for Certain Random Polynomials*, Mathematics 11 (2023), 4061, DOI:10.3390/math11194061, https://doi.org/10.3390/math11194061.
3. O. Yakir, *Approximately half of the roots of a random Littlewood polynomial are inside the disk*, arXiv:2011.06234, https://arxiv.org/abs/2011.06234.
4. *Fluctuations for zeros of Gaussian Taylor series*, 2021, https://onlinelibrary.wiley.com/doi/10.1112/jlms.12436.
