# Exact beta-product leakage and logarithmic tails in Gaussian oblique tangent projection

## Finding

**Theorem.** Let \(m,n\ge s\ge2\), and choose orthonormal pairs \((u,u_\perp)\) in \(\mathbb R^m\) and \((v,v_\perp)\) in \(\mathbb R^n\). Fix a nonzero rank-one state \(Y=\sigma uv^{\mathsf T}\) and the unit Frobenius normal forcing \(Z=u_\perp v_\perp^{\mathsf T}\). Let independent real Gaussian sketches \(\Theta\in\mathbb R^{s\times m}\) and \(\Omega\in\mathbb R^{s\times n}\) have independent standard-normal entries. Define
\[
L=u\frac{(\Theta u)^{\mathsf T}\Theta}{\|\Theta u\|_2^2},\qquad
R=v\frac{(\Omega v)^{\mathsf T}\Omega}{\|\Omega v\|_2^2},\qquad
\mathcal P_{\mathrm{obl}}(B)=LB+BR^{\mathsf T}-LBR^{\mathsf T}.
\]
The denominators are positive almost surely. The orthogonal tangent projector annihilates \(Z\). For the squared oblique normal leakage \(W=\|\mathcal P_{\mathrm{obl}}(Z)\|_F^2\), let \(\alpha=s/2\) and \(B_*=\operatorname{B}(\alpha,1/2)\). Then
\[
1+W\ \overset{d}{=}\ \frac{1}{H_1H_2},\qquad
H_1,H_2\ \text{independent }\operatorname{Beta}(\alpha,1/2).
\]
Consequently, for \(t\ge0\), with \(q=(1+t)^{-1}\), density \(f_H(x)=x^{\alpha-1}(1-x)^{-1/2}/B_*\), and beta CDF \(F_H\),
\[
\Pr(W>t)=F_H(q)+\int_q^1 f_H(x)F_H(q/x)\,dx.
\]
The Mellin transform, exact moment threshold, and extreme tail are
\[
\mathbb E(1+W)^p=\left[\frac{\operatorname{B}(\alpha-p,1/2)}{B_*}\right]^2\quad(p<\alpha),
\qquad
\mathbb E W^p<\infty\ \Longleftrightarrow\ 0<p<\alpha,
\]
\[
\Pr(W>t)\sim\frac{t^{-\alpha}\log t}{\alpha B_*^2}\quad(t\to\infty).
\]
In particular \(\mathbb EW=(2s-3)/(s-2)^2\) if \(s>2\), and \(\mathbb EW=\infty\) when \(s=2\). For the leakage norm \(X=\sqrt W\), its \(p\)-th moment exists exactly when \(0<p<s\), and
\[
\Pr(X>x)\sim\frac{2\log x}{\alpha B_*^2x^s}.
\]
If only the column side is sketched (the row sketch is the identity), the corresponding normal leakage is \(|G|/\sqrt Q\) with independent \(G\sim N(0,1)\) and \(Q\sim\chi_s^2\). Its tail is \(x^{-s}/(\alpha B_*)\), without a logarithm. Thus two independent sketches impose a sharp multiplicative logarithmic penalty in the extreme tail, while the power-law moment threshold is unchanged.

## Assumptions and scope

All vectors and sketches are real. The sketch sizes on the two sides are equal to an integer \(s\) for clarity; the rank-one state can have arbitrary nonzero singular value \(\sigma\), which cancels from the projector. Gaussian entries may be scaled by any common nonzero deterministic factor separately on each side, since each projector is scale-invariant. The analysis concerns the instantaneous canonical oblique tangent projection of a **fixed normal forcing**, not a time-integrated differential equation. The comparison with the orthogonal tangent projector is exact for this forcing. The expression for \(\mathcal P_{\mathrm{obl}}\) is the canonical lifted two-sided projector of Carrel and Grigori, Lemma 4.2. The one-sided case uses their Remark 4.3. No embedding-success event is imposed: all probabilities and moments are unconditional over independent Gaussian sketches.

## Proof

**Step 1: Reduction to two independent scalar slopes.** Put
\[
a=\frac{(\Theta u)^{\mathsf T}(\Theta u_\perp)}{\|\Theta u\|_2^2},\qquad
b=\frac{(\Omega v)^{\mathsf T}(\Omega v_\perp)}{\|\Omega v\|_2^2}.
\]
Direct multiplication gives \(LZ=a\,uv_\perp^{\mathsf T}\), \(ZR^{\mathsf T}=b\,u_\perp v^{\mathsf T}\), and \(LZR^{\mathsf T}=ab\,uv^{\mathsf T}\). In the orthonormal row-column coordinates \((u,u_\perp)\) and \((v,v_\perp)\), the only nonzero block is
\[
\mathcal P_{\mathrm{obl}}(Z)\longleftrightarrow
\begin{pmatrix}-ab&a\\b&0\end{pmatrix}.
\]
Its squared Frobenius norm is \(W=a^2+b^2+a^2b^2\), so \(1+W=(1+a^2)(1+b^2)\). The ordinary orthogonal tangent projection \(uu^{\mathsf T}Z+Zvv^{\mathsf T}-uu^{\mathsf T}Zvv^{\mathsf T}\) is zero.

**Step 2: Gaussian conditional law.** By rotational invariance, \(g=\Theta u\) and \(h=\Theta u_\perp\) are independent \(N(0,I_s)\) vectors. Conditional on \(g\), the numerator \(g^{\mathsf T}h\) has law \(\|g\|_2G\) with \(G\sim N(0,1)\) independent of \(Q=\|g\|_2^2\sim\chi_s^2\). Hence \(a\overset d=G/\sqrt Q\); the independent right sketch yields an independent copy for \(b\). Consequently \(H_1=(1+a^2)^{-1}=Q/(Q+G^2)\) has \(\operatorname{Beta}(s/2,1/2)\) law, as does independent \(H_2\). This proves the exact distribution identity. Conditioning on \(H_1=x\) proves the displayed finite-sample tail integral.

**Step 3: Moments.** Beta integration gives \(\mathbb EH_i^{-p}=\operatorname{B}(\alpha-p,1/2)/B_*\) for \(p<\alpha\), and infinity for \(p\ge\alpha\). Independence proves the Mellin identity. For \(p>0\), on \(W\ge1\) the quantity \(W^p\) is comparable with \((1+W)^p\), whereas on \(W<1\) it is bounded. Thus precisely the stated positive moments exist. At \(p=1\) (allowed iff \(s>2\)), \(\mathbb EH_i^{-1}=(s-1)/(s-2)\), giving \(\mathbb EW=((s-1)/(s-2))^2-1=(2s-3)/(s-2)^2\).

**Step 4: Exact logarithmic tail.** Let \(T_i=-\log H_i\). Their independent densities on \((0,\infty)\) are
\[
g(t)=\frac{e^{-\alpha t}}{B_*\sqrt{1-e^{-t}}}.
\]
The density of \(T_1+T_2\) is therefore
\[
(g*g)(z)=\frac{e^{-\alpha z}}{B_*^2}\int_0^z\frac{dt}{\sqrt{(1-e^{-t})(1-e^{-(z-t)})}}.
\]
The function \(r(t)=(1-e^{-t})^{-1/2}-1\) is nonnegative and integrable on \((0,\infty)\): it behaves as \(O(t^{-1/2})\) near zero and \(O(e^{-t})\) at infinity. Expanding the integrand as \((1+r(t))(1+r(z-t))\) shows that the integral is \(z+O(1)\), since the two linear terms have bounded integrals and their convolution is bounded. Therefore \((g*g)(z)=e^{-\alpha z}(z+O(1))/B_*^2\). Integrating the density from \(z\) to infinity yields
\[
\Pr(T_1+T_2>z)\sim\frac{ze^{-\alpha z}}{\alpha B_*^2}.
\]
Since \(W=e^{T_1+T_2}-1\), substitution \(z=\log(1+t)\) establishes the \(W\)-tail, then replacing \(t\) by \(x^2\) gives the \(X\)-tail.

**Step 5: One-sided contrast.** Set \(L=uu^{\mathsf T}\) rather than a random oblique projector. Then \(LZ=LZR^{\mathsf T}=0\), so \(\|\mathcal P_{\mathrm{obl}}(Z)\|_F=|b|\) and \(\Pr(|b|>x)=\Pr(H_2<(1+x^2)^{-1})\). The beta density near zero gives \(F_H(y)\sim y^\alpha/(\alpha B_*)\), hence \(\Pr(|b|>x)\sim x^{-s}/(\alpha B_*)\). The ratio of the two-sided to one-sided norm-tail probabilities is asymptotic to \(2\log x/B_*\).

## Verification

The standalone companion script `verify_beta_leakage.py` reconstructs the two oblique projectors from independent Gaussian matrices and checks the actual matrix projection against the scalar reduction for multiple dimensions and sketch sizes. It also verifies beta inverse moments, compares the exact distribution integral with independent beta-product simulations, and checks logarithmic-tail prefactors at multiple thresholds. It completed **3,221 passing deterministic assertions**, with its fixed pseudo-random seed. Running the script requires Python, NumPy, and SciPy. These finite calculations independently test the formulas; the universal conclusions follow from the analytic argument above.

## Relationship to prior work

Carrel and Grigori (2026), Lemma 4.2 and Remark 4.3, supply the canonical oblique tangent operator and show that large perpendicular forcing can corrupt oblique-sketch low-rank dynamics; their conditional embedding analysis does not itself supply this unconditional exact rank-one leakage distribution, Mellin transform, moment cutoff, or the two-sided logarithmic tail. Balabanov and Nouy (2018) analyze randomized Galerkin subspace embeddings and errors under embedding events, rather than the exact unconditional normal-leakage law. Niu et al. (2026) analyze random oblique projections in subsampled least squares/CUR with different projectors and statistical regimes. Dereziński et al. (2020/2022) analyze expected residuals of *orthogonal* random row-space projections, not the two-sided oblique tangent projection of a fixed normal rank-one forcing. Stewart (2011) studies deterministic perturbations of oblique projectors. Standard beta-ratio and product-tail principles are used, not claimed as discoveries by themselves. The asserted contribution is specifically their complete analytic application and sharp one-sided/two-sided contrast for this newly studied projector.

## Limitations

The theorem is an exact **single-forcing projection law**, not an error bound or divergence theorem for the numerical evolution obtained by integrating an ODE. Gaussian sketches are independent and unconditioned; conditioning on a successful subspace embedding truncates the rare events and changes the conclusions. A large tail or an infinite moment does not mean almost-sure failure. Both sides use the same sketch size \(s\); different sizes yield a related but different product tail. Nothing is asserted for structured sketches, finite-precision computations, or correlations between the two sketches. Exact historical priority relative to older specialized random-projector literature remains subject to further independent scrutiny.

## References

1. B. Carrel and L. Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections*, arXiv:2607.03402v1 (first public July 3, 2026), esp. §§2, 4, Lemma 4.2, Remark 4.3. https://arxiv.org/abs/2607.03402
2. O. Balabanov and A. Nouy, *Randomized linear algebra for model reduction. Part I: Galerkin methods and error estimation*, arXiv:1803.02602 (2018). https://arxiv.org/abs/1803.02602
3. C. Niu and collaborators, *Debiasing Random Oblique Projections for Subsampled OLS and Fast CUR in High Dimensions*, arXiv:2605.24955 (2026). https://arxiv.org/abs/2605.24955
4. M. Dereziński, F. Liang, Z. Liao, and M. W. Mahoney, *Precise expressions for random projections: Low-rank approximation and randomized Newton*, arXiv:2006.10653 (2020, revised 2022). https://arxiv.org/abs/2006.10653
5. G. W. Stewart, *On the Numerical Analysis of Oblique Projectors*, SIAM Journal on Matrix Analysis and Applications (2011), doi:10.1137/100792093. https://doi.org/10.1137/100792093
