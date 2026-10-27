# A universal Pareto tail and logarithmic trimming penalty for rank-one indefinite Nyström sketches

## Finding

For every fixed nonsingular real symmetric indefinite matrix \(A\) of order \(n\ge2\), the *unregularized rank-one Gaussian Nyström* approximation has an exactly determined heavy-tail exponent. If \(E\) denotes its spectral-norm residual, then
\[
\lim_{t\to\infty}t\,\Pr(E>t)=C(A),\qquad
C(A)=\frac{1}{|S^{n-1}|}\int_{Z_A}\|Au\|_2\,d\mathcal H^{n-2}(u)>0,
\]
where \(Z_A=\{u\in S^{n-1}:u^{\mathsf T}Au=0\}\). Consequently,
\[
\mathbb E E^p<\infty\quad\Longleftrightarrow\quad 0<p<1
\]
for every positive moment order \(p\). In contrast, every fixed real symmetric *definite* input gives a uniformly bounded error.

A simple hard cutoff that rejects almost-cancelled scalar cores has the sharp mean-risk growth
\[
\mathbb E\|A-N_\epsilon\|_2=C(A)\log(1/\epsilon)+O_A(1)
\qquad(\epsilon\downarrow0).
\]
The same geometric constant governs both the large-error probability and the regularization penalty.

## Assumptions and scope

Fix an integer \(n\ge2\), an invertible real symmetric matrix \(A\in\mathbb R^{n\times n}\) with at least one positive and one negative eigenvalue, and \(g\sim N(0,I_n)\). Define
\[
N=A g(g^{\mathsf T}Ag)^{-1}g^{\mathsf T}A,
\qquad E=\|A-N\|_2.
\]
The denominator vanishes on a Gaussian-null set; any definition there leaves the distribution unchanged. With \(U=g/\|g\|_2\), uniform on \(S^{n-1}\), set \(q(u)=u^{\mathsf T}Au\) and \(v(u)=\|Au\|_2^2\); then \(N=(Au)(Au)^{\mathsf T}/q(u)\). The sphere carries uniform probability measure, and \(|S^{n-1}|\) is its surface area. On \(Z_A\), \(\mathcal H^{n-2}\) means induced hypersurface measure, including counting measure when \(n=2\).

For \(0<\epsilon<1\), the *hard-trimmed* approximation is \(N_\epsilon=N\) if \(|q(U)|\ge\epsilon\|A\|_2\), and \(N_\epsilon=0\) otherwise. This is a specific scalar-core cutoff, not a claim about the stabilized algorithm of the motivating paper or about higher-rank sketches.

## Proof

**1. Regularity and spherical level-set geometry.** The symmetric indefinite form \(q\) takes both signs on the sphere; by continuity its zero set \(Z_A\) is nonempty. The tangential gradient of \(q\) on \(S^{n-1}\) equals \(2Au-2q(u)u\), hence on \(Z_A\) it equals \(2Au\). Invertibility gives \(\|Au\|_2\ge\sigma_{\min}(A)>0\), so zero is a regular value. Thus \(Z_A\) is a compact smooth hypersurface and its positive finite induced measure makes \(C(A)\) finite and strictly positive.

**2. Exact pole and tail coefficient.** Since \(N\) has rank one, its sole nonzero eigenvalue is \(v(u)/q(u)\), and therefore \(\|N\|_2=v(u)/|q(u)|\). Define \(h(u)=q(u)/v(u)\). On \(Z_A\), \(\nabla_S h=2Au/v(u)\), with gradient modulus \(2/\|Au\|_2\). The smooth coarea formula applied to the probability law of \(h(U)\) shows that its density is continuous in a neighborhood of zero and satisfies
\[
f_h(0)=\frac{1}{|S^{n-1}|}\int_{Z_A}\frac{1}{\|\nabla_S h(u)\|_2}\,d\mathcal H^{n-2}(u)=\frac{C(A)}2.
\]
Here regularity persists on a small neighborhood of the compact zero level, giving density continuity there by smooth local charts. Consequently,
\[
\Pr(\|N\|_2>t)=\Pr(|h(U)|<t^{-1})=\frac{C(A)}t+o(t^{-1}).
\]
The reverse triangle inequalities give \(|E-\|N\|_2|\le\|A\|_2\). Replacing \(t\) by \(t\pm\|A\|_2\) in the preceding tail asymptotic proves the claimed spectral-residual tail with the same \(C(A)\).

**3. Sharp moment threshold.** For every \(p>0\), the nonnegative moment formula is \(\mathbb E E^p=p\int_0^\infty t^{p-1}\Pr(E>t)\,dt\). Its tail integrand is asymptotic to \(pC(A)t^{p-2}\), which is integrable exactly when \(p<1\). At \(p=1\) the divergence is logarithmic; for larger \(p\), it is stronger. If \(A\) is positive or negative definite instead, then \(|q(u)|\ge\sigma_{\min}(A)\) for all unit \(u\), giving \(E\le\|A\|_2+\|A\|_2^2/\sigma_{\min}(A)\), so all positive moments exist.

**4. Exact logarithmic cost of rejecting small cores.** For the cutoff, \(\|N_\epsilon\|_2=v(U)/|q(U)|\) on the accepted region and zero otherwise; and \(|\|A-N_\epsilon\|_2-\|N_\epsilon\|_2|\le\|A\|_2\) everywhere. By coarea applied directly to \(q\), the weighted level-set density
\[
F(s)=\frac1{|S^{n-1}|}\int_{\{q=s\}}\frac{v(u)}{\|\nabla_S q(u)\|_2}\,d\mathcal H^{n-2}(u)
\]
is continuously differentiable around zero and has \(F(0)=C(A)/2\). Consequently, taking \(\delta>0\) smaller than the regularity radius, the contribution from \(\epsilon\|A\|_2\le|q|<\delta\) equals
\[
\int_{\epsilon\|A\|_2}^{\delta}\frac{F(s)+F(-s)}{s}\,ds
=C(A)\log(1/\epsilon)+O_A(1),
\]
since \(F(s)+F(-s)=C(A)+O_A(|s|)\). The region \(|q|\ge\delta\) contributes a bounded amount. The uniform residual-versus-core norm bound transfers the asymptotic to \(\mathbb E\|A-N_\epsilon\|_2\).

**5. Exact two-dimensional witness and geometric family.** For \(A=\operatorname{diag}(a,-b)\), \(a,b>0\), the residual \(A-N\) has determinant zero and trace \(-ab/q(U)\), so \(E=ab/|q(U)|\). When \(a=b=1\), writing \(U=(\cos\theta,\sin\theta)\) gives \(q(U)=\cos(2\theta)\), uniform \(\theta\) on \([0,2\pi)\), and therefore
\[
\Pr(E>t)=\frac2\pi\arcsin(1/t)\quad(t\ge1),\qquad C(A)=\frac2\pi.
\]
For this same reflection, an exact integration of the hard cutoff gives
\[
\mathbb E\|A-N_\epsilon\|_2
=\frac2\pi\left[\log\!\left(\frac{1+\sqrt{1-\epsilon^2}}{\epsilon}\right)+\arcsin(\epsilon)\right].
\]
For the higher-dimensional signature family \(A=\operatorname{diag}(1,\ldots,1,-1)\), the two zero-level latitudes give the explicit positive constant
\[
C(A)=\frac{2^{2-n/2}\Gamma(n/2)}{\sqrt\pi\,\Gamma((n-1)/2)}.
\]
In particular, every finite dimension retains a divergent mean even as this coefficient decreases with dimension.

## Verification

Run `python3 verify.py` with only the Python standard library. The program checks 672 exact-rational two-dimensional rank-one residual identities, 25 analytic tail/coarea constant numerical cross-checks, and eight independent cutoff quadrature/asymptotic comparisons. Expected terminal output:

`VERIFY_OK rank-one residual rational identities=672, sharp-tail asymptotics and coarea constants=25, normalized core truncation=8`

The proof of the infinite-dimensional quantifier over all finite \(n\), the asymptotic tail, and the moment threshold is analytical. These finite tests do **not** certify a general coarea theorem or replace its justification.

## Relationship to prior work

Park and Nakatsukasa introduced and analyzed the difficulties of applying Nyström approximation to symmetric indefinite inputs. Their examples demonstrate potentially unbounded error for a specially chosen sketch, and they construct stabilized variants. The present claim is more specific and probabilistic: for a *single isotropic Gaussian probe* in *every fixed dimension*, it identifies the exact asymptotic Pareto tail coefficient, all moment thresholds, and a matching logarithmic hard-trimming penalty. It does not claim priority for the already known possibility of indefinite Nyström instability.

Nakatsukasa's generalized Nyström methods use two-sided, independently sketched constructions, distinct from this symmetric one-probe scalar core. Classical ratio-of-quadratic-forms theory supplies related statistical methods; a potentially equivalent formulation outside low-rank approximation remains an originality risk, and absence of a discovered matching formulation is not proof of uniqueness. Later indefinite-sketch studies analyze different approximations and do not by themselves establish this rank-one law.

## Limitations

The theorem requires a real symmetric **invertible** matrix and exactly one isotropic Gaussian sketch vector; an indefinite singular matrix or higher sketch rank is not classified. It uses exact arithmetic and a specifically defined core cutoff. The distributional statement is a large-error asymptotic, not an exact finite-threshold probability formula in general. The comparison with definite inputs is solely a boundedness statement and does not characterize their approximation accuracy. The result has only self-review, with no independent audit or validation of novelty.

## References

1. T. Park and Y. Nakatsukasa, *Randomized low-rank approximation for symmetric indefinite matrices*, arXiv:2212.01127, first public version 2022-12-02. https://arxiv.org/abs/2212.01127
2. Y. Nakatsukasa, *Fast and stable randomized low-rank matrix approximation*, arXiv:2009.11392 (2020). https://arxiv.org/abs/2009.11392
3. Y. Chen, Y. Nakatsukasa, A. Narendran, and T. Park, *Nyström method for symmetric indefinite matrices*, arXiv:2608.20531 (2026); later context, outside the motivating middle-cohort date window. https://arxiv.org/abs/2608.20531
4. M. D. Smith, *On the expectation of a ratio of quadratic forms in normal variables*, Journal of Multivariate Analysis 31 (1989), 244–257. https://doi.org/10.1016/0047-259X(89)90065-1
