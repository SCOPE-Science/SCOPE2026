# An all-oversampling infinite-risk law for Gaussian-sketched FOM
## Finding

On a one-dimensional Krylov subspace, Gaussian-sketched full orthogonalization (FOM) has **infinite expected squared solution error at every finite sketch size**, even for symmetric positive definite linear systems. The corresponding one-step sketched GMRES method has finite expected squared residual as soon as the sketch has more than two rows. The distinction is an exact distributional property of the two projections, not a finite-precision effect.

Let
\[
A\in\mathbb R^{n\times n},\quad A=A^{\mathsf T}\succ0,\quad n\ge2,\quad b\ne0,
\]
put
\[
v=\frac b{\|b\|},\qquad a=v^{\mathsf T}Av,
\qquad d=\|Av-av\|,\qquad m=a^2+d^2.
\]
For the non-eigenvector case \(d>0\), use a Gaussian sketch \(\Omega\in\mathbb R^{\ell\times n}\) with i.i.d. entries of variance \(1/\ell\), where \(\ell\ge2\) is arbitrary but finite. Write the first sketched FOM and sketched GMRES solutions, starting at zero, as \(c_Fb\) and \(c_Gb\).

For standard Student random variables \(T_\ell\) and \(T'_\ell\), each with \(\ell\) degrees of freedom, their **marginal** laws are
\[
\boxed{c_F\ \overset d=\ \frac1{a+(d/\sqrt\ell)T_\ell}},
\qquad
\boxed{c_G\ \overset d=\ \frac a m+\frac{d}{m\sqrt\ell}T'_\ell}.
\]
These equalities do not assert that the two Student variables are independent when the algorithms reuse a sketch.

The Gaussian-sketch FOM coefficient is defined almost surely, but
\[
\boxed{\mathbb E|c_F|^q=\infty\quad\text{for every }q\ge1}
\]
and
\[
\boxed{\mathbb E\|A^{-1}b-c_Fb\|_A^2=\infty}
\]
for **every** finite \(\ell\). Its absolute tail has the sharp constant
\[
\boxed{
\lim_{t\to\infty}t\Pr\{|c_F|>t\}
=\frac{2\Gamma((\ell+1)/2)}{\sqrt\pi\,d\,\Gamma(\ell/2)}
\left(1+\frac{a^2}{d^2}\right)^{-(\ell+1)/2}.
}
\]

In contrast, if \(\ell>2\), the GMRES coefficient satisfies
\[
\boxed{\operatorname{Var}(c_G)=\frac{d^2}{m^2(\ell-2)}}
\]
and its expected squared **unsketched** residual is
\[
\boxed{
\mathbb E\|b-A(c_Gb)\|^2
=\|b\|^2\frac{d^2}{m}\frac{\ell-1}{\ell-2}.
}
\]
More generally, \(\mathbb E|c_G|^q<\infty\) exactly for \(0<q<\ell\); moments of order \(q\ge\ell\) diverge.

If \(d=0\), then \(Ab=ab\) and both coefficients equal \(1/a\) almost surely. Thus the non-eigenvector hypothesis precisely characterizes when the infinite first absolute moment of sketched FOM occurs.

## Assumptions and scope

The linear system is real, deterministic, and SPD. The starting iterate is zero and the Krylov subspace is exactly \(\operatorname{span}\{b\}\). The projection coefficients are computed in exact arithmetic; no regularization, clipping, rejection sampling, or condition-on-embedding filter is applied. Only marginal coefficient distributions and their moments are asserted.

Gaussian sketch entries have common variance \(1/\ell\). Any other common positive variance produces the same coefficient laws because a scalar sketch rescaling cancels out. No rank assumption is placed on the full \(\ell\times n\) sketch; \(\ell\) may exceed \(n\).

The error norm is \(\|z\|_A^2=z^{\mathsf T}Az\), and all expectations are unconditional over the Gaussian sketch. High-probability statements conditional on a successful subspace embedding are not being challenged.

## Proof

**Exact one-step formulas.** The sketched FOM Petrov–Galerkin equation is
\[
(\Omega b)^{\mathsf T}\Omega(b-A(c_Fb))=0,
\]
so
\[
c_F=\frac{\|\Omega b\|^2}{(\Omega b)^{\mathsf T}\Omega Ab}
\]
whenever its denominator is nonzero. The sketched GMRES normal equation minimizes \(\|\Omega(b-A(cb))\|^2\) and gives
\[
c_G=\frac{(\Omega Ab)^{\mathsf T}\Omega b}{\|\Omega Ab\|^2}.
\]

**FOM law.** For \(d>0\), define \(w=(Av-av)/d\). Then \(v,w\) are unit orthogonal vectors and \(Av=av+dw\). The independent Gaussian vectors \(u=\sqrt\ell\,\Omega v\) and \(z=\sqrt\ell\,\Omega w\) have independent standard normal coordinates. Thus
\[
c_F^{-1}=a+d\frac{u^{\mathsf T}z}{\|u\|^2}.
\]
Conditioning on \(u\), the variable \(Z=u^{\mathsf T}z/\|u\|\) is standard normal with a conditional law independent of \(u\); consequently \(Z\) is independent of \(H=\|u\|\), where \(H^2\sim\chi^2_\ell\). Therefore
\[
\frac{u^{\mathsf T}z}{\|u\|^2}=\frac ZH=\frac{T_\ell}{\sqrt\ell}.
\]
This proves the first marginal law.

Write \(Y=a+(d/\sqrt\ell)T_\ell\). Its continuous density is strictly positive at zero, with
\[
f_Y(0)=\frac{\Gamma((\ell+1)/2)}{\sqrt\pi\,d\,\Gamma(\ell/2)}
\left(1+\frac{a^2}{d^2}\right)^{-(\ell+1)/2}.
\]
Continuity implies
\[
\Pr\{|c_F|>t\}=\Pr\{|Y|<t^{-1}\}=\frac{2f_Y(0)}t+o(t^{-1}),
\]
so the displayed tail coefficient holds. The layer-cake formula
\[
\mathbb E|c_F|^q=q\int_0^\infty t^{q-1}\Pr\{|c_F|>t\}\,dt
\]
diverges for every \(q\ge1\).

For \(x_*=A^{-1}b\), the quadratic energy expands exactly as
\[
\|x_*-c_Fb\|_A^2
=\|x_*-a^{-1}b\|_A^2
+\|b\|^2a(c_F-a^{-1})^2,
\]
because the deterministic Galerkin minimizer over multiples of \(b\) is \(a^{-1}b\). The second term has infinite expectation by the squared tail, proving infinite expected energy error.

**GMRES law.** The normalized vector \(q=Av/\sqrt m\) has norm one. Decompose \(v\) into its component along \(q\) plus an orthogonal unit direction:
\[
v=\frac a{\sqrt m}q+\frac d{\sqrt m}q_\perp.
\]
Then \(\sqrt\ell\,\Omega q\) and \(\sqrt\ell\,\Omega q_\perp\) are independent standard Gaussian vectors. Substitution into the GMRES coefficient shows
\[
c_G=\frac a m+\frac d m\frac{Z'}{H'},
\]
where \(Z'\sim N(0,1)\), \((H')^2\sim\chi^2_\ell\), independently. This proves the stated second marginal Student law.

The standard Student second moment is \(\mathbb E(T'_\ell)^2=\ell/(\ell-2)\) when \(\ell>2\), and Student tails are of order \(t^{-\ell}\). Thus the moment threshold and variance follow. Finally, for any scalar \(c\),
\[
\|b-A(cb)\|^2=\|b\|^2(1-2ac+mc^2).
\]
Using \(\mathbb Ec_G=a/m\) and its variance gives the exact expected residual formula.

**Eigenvector boundary.** If \(d=0\), then \(Av=av\), so the numerators and denominators of both sketch coefficients cancel to give \(1/a\) whenever \(\Omega v\ne0\); this occurs almost surely.

## Verification

The accompanying `verify.py` reconstructs both sketched coefficient formulas directly on an SPD two-by-two example, checks their Gaussian projection representations across randomly generated sketch matrices, and verifies the deterministic algebra for the residual and energy decompositions. It also checks the exact density constant and moment formulas against independent numerical quadrature/algebra where appropriate.

Finite simulation does not establish the infinite moments or the tail asymptotic; those follow from the positive density at the reciprocal pole and the layer-cake integral, as shown above.

## Relationship to prior work

Güttel and Schweitzer's sketched FOM and sketched GMRES constructions reduce shifted linear-system projections to sketched Galerkin and least-squares equations, respectively. Timsit, Grigori, and Balabanov analyze randomized orthogonal projection methods and report occasional large energy-error spikes; their quasioptimality guarantees explicitly rely on embedding conditions. The new theorem addresses the **unconditional** distribution over a Gaussian sketch and proves an infinite-moment phenomenon that can coexist with their high-probability guarantees.

Palitta, Schweitzer, and Simoncini give a later algebraic analysis of sketched and truncated Krylov methods, including numerical stability. That work does not present the one-step Student reciprocal law or its moment threshold. The ordinary Student ratio and its moment facts are standard probability; the original contribution here is their exact appearance in the two distinct, published sketched Krylov projections and the resulting all-oversampling energy-risk separation.

The formula also explains why increasing a finite sketch size can make failures extremely rare without ever making the unconditional FOM mean squared energy finite: the positive pole-density constant decreases with sampling but never vanishes.

## Limitations

The result treats a single Krylov step and an unregularized Gaussian sketch, not the full iterated algorithm with safeguards or monitored embedding quality. It does not claim typical practical instability or failure of a high-probability error bound. It is a statement about unconditional mathematical expectations, whose divergence is driven by exceptionally rare samples. Structured bounded sketches and sketch-rejection rules can obey different moment laws. The finite-risk comparison for GMRES is made in the unsketched Euclidean residual, not in a general norm or later iteration.

## References

1. Stefan Güttel and Marcel Schweitzer, “Randomized sketching for Krylov approximations of large-scale matrix functions,” arXiv:2208.11447v1 (first public 2022-08-24); subsequently SIAM Journal on Matrix Analysis and Applications, DOI:10.1137/22M1518062.
2. Edouard Timsit, Laura Grigori, and Oleg Balabanov, “Randomized Orthogonal Projection Methods for Krylov Subspace Solvers,” arXiv:2302.07466v1 (first public 2023-02-15).
3. Oleg Balabanov and Laura Grigori, “Randomized Gram-Schmidt process with application to GMRES,” arXiv:2011.05090v1 (2020).
4. Davide Palitta, Marcel Schweitzer, and Valeria Simoncini, “Sketched and Truncated Polynomial Krylov Methods: Evaluation of Matrix Functions,” Numerical Linear Algebra with Applications, DOI:10.1002/nla.2596 (first online 2024-11-11).
