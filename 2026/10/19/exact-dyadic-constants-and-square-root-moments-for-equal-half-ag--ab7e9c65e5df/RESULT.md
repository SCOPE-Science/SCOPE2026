# Exact dyadic constants and square-root moments for equal-half aggregation–fragmentation

## Finding

In the mass-independent continuous-mass aggregation–fragmentation model of Krapivsky with deterministic division into two equal halves, let \(A_1=1\) and, for every integer \(n\ge2\), define the dimensionless stationary mass moments by
\[
 (1-2^{1-n})A_n=\sum_{k=1}^{n-1}\binom nk A_kA_{n-k}.
\]
This recurrence is Eq. (43) in the reference specialized to equal splitting; the present result determines its previously unspecified exponential rate and leading amplitude.

Set \(a_0=1/2\), \(a_{j+1}=a_j(1-a_j)/2\) for \(j\ge0\), and
\[
 \sigma=\lim_{j\to\infty}2^j a_j,\qquad
 P=\prod_{j=1}^{\infty}(1-2a_j),\qquad
 B=\frac{1}{2\sqrt{\pi P}}.
\]
These limits satisfy \(\sigma>0\), \(P>0\), and the **rigorous** coefficient asymptotic is
\[
 \boxed{A_n\sim\sqrt\sigma\,B\;n!\,\sigma^{-n}n^{-3/2}}\quad(n\to\infty).
\]
Thus the moment exponential-growth constant is \(\sigma^{-1}\), and the leading amplitude is given by a convergent dyadic product. Certified rational enclosures yield
\[
 \sigma=0.19645342637788979403575206272387\ldots,\quad
 B=0.36347986949375689508193099528108\ldots.
\]
For every \(j\ge1\), defining \(P_j=\prod_{k=1}^{j}(1-2a_k)\), valid explicit error enclosures are
\[
 2^j a_j(1-2a_j)\le\sigma\le2^j a_j,\qquad
 P_j(1-2a_j)\le P\le P_j,
\]
and hence
\[
 \frac{1}{2\sqrt{\pi P_j}}\le B\le
 \frac{1}{2\sqrt{\pi P_j(1-2a_j)}}.
\]
No numerical root-finding or simulation of the physical process is required.

## Assumptions and scope

The physical reference model has constant mass-independent binary merger rate (set to unity), positive mass-independent binary fragmentation rate \(\lambda\), and each fragmentation maps a mass \(x>0\) to two masses \(x/2\). For the stationary cluster density \(c(x)\) with unit conserved total mass, define \(M_n=\int_0^\infty x^n c(x)\,dx\). The reference's moment hierarchy gives \(M_n=A_n\lambda^{1-n}\). The theorem concerns the unique **formal positive moment solution** of that hierarchy and therefore its positive-radius exponential generating series; physical identification uses the stationary moment hierarchy already established in the reference. It does not assume a pointwise density-tail formula, nor assert one.

Let \(G(z)=\sum_{n\ge1}A_nz^n/n!\). All analytic assertions below concern this series and its analytic continuation. The parameters \(\sigma\) and \(B\) are dimensionless and are not arbitrary fitting constants.

## Proof

**1. Positive convergence radius.** Write \(c_n=A_n/n!\). The recurrence becomes \((1-2^{1-n})c_n=\sum_{k=1}^{n-1}c_kc_{n-k}\) with \(c_1=1\), so all \(c_n\) are positive. Because \((1-2^{1-n})^{-1}\le2\) for \(n\ge2\), coefficientwise \(G\) is bounded by the unique series \(H=z+2H^2\), explicitly \(H(z)=(1-\sqrt{1-8z})/4\). Hence the convergence radius \(R\) of \(G\) is at least \(1/8\). Summing the recurrence gives the exact functional identity
\[
 G(z)=G(z)^2+2G(z/2),\quad G(0)=0,\quad G'(0)=1.
\]
On the positive real interval \((0,R)\), \(G'\!>0\). Differentiation gives \((1-2G(z))G'(z)=G'(z/2)>0\). As \(G(0)=0\), continuity implies \(0<G(z)<1/2\). Moreover \(G(z/2)\ge z/2\), so \(z\le G(z)-G(z)^2\le1/4\). Consequently \(R\le1/4\), in particular \(R\) is finite.

**2. Location of the first singularity.** Since all coefficients are nonnegative, Pringsheim's theorem makes \(z=R\) a singular point. The monotone real limit \(G(R^-)=L\le1/2\) exists. Since \(G(z/2)\) is analytic at \(z=R\), the identity \(G(z)-G(z)^2=2G(z/2)\) would analytically continue \(G\) through \(R\) if \(L<1/2\), by the holomorphic implicit-function theorem. This contradicts Pringsheim. Therefore \(L=1/2\) and \(G(R/2)=1/8\).

**3. An exact logistic characterization.** Define \(a_j=G(R/2^j)\) for \(j\ge0\). Then \(a_0=1/2\) and the functional equation gives \(a_{j+1}=a_j(1-a_j)/2\), with \(0<a_j<1/2\). Since \(G(z)=z+O(z^2)\) near zero,
\[
 2^j a_j=2^j G(R/2^j)\longrightarrow R.
\]
Thus \(\sigma=R\). The sequence \(b_j=2^ja_j\) satisfies \(b_{j+1}=b_j(1-a_j)\) and decreases to \(\sigma>0\). The geometric inequality \(a_{j+k}\le2^{-k}a_j\) implies \(\sum_{k\ge0}a_{j+k}\le2a_j\). Applying \(\prod(1-u_k)\ge1-\sum u_k\) for \(u_k\in[0,1]\) to the product \(b_j\prod_{k\ge j}(1-a_k)\) gives the asserted two-sided \(\sigma\) bounds.

**4. Derivative and product amplitude.** Differentiating the functional identity yields
\[
 (1-2G(z))G'(z)=G'(z/2).
\]
Evaluate iteratively at \(z=\sigma/2,\sigma/4,\ldots\), and use \(G'(0)=1\):
\[
 G'(\sigma/2)=\prod_{j\ge1}(1-2a_j)^{-1}=P^{-1}.
\]
The product converges to a strictly positive value because \(\sum_{j\ge1}2a_j<\infty\) and each factor is positive. The bound on its tail follows from \(\sum_{k>j}2a_k\le2a_j\), giving \(P_j(1-2a_j)\le P\le P_j\).

**5. Square-root singularity and coefficient extraction.** For \(0\le z<\sigma\), the lower quadratic branch satisfies
\[
 G(z)=\frac{1-\sqrt{1-8G(z/2)}}2.
\]
The inner function is analytic near \(z=\sigma\) and its discriminant has the expansion
\[
 1-8G(z/2)=\frac{4\sigma}{P}(1-z/\sigma)+O((1-z/\sigma)^2).
\]
Consequently
\[
 G(z)=\frac12-\sqrt{\frac\sigma P}\,(1-z/\sigma)^{1/2}+O(1-z/\sigma).
\]
There are no other singularities on \(|z|=\sigma\): for \(|z|=\sigma\), \(z\ne\sigma\), strict positivity of every coefficient gives \(|G(z/2)|<G(\sigma/2)=1/8\). The discriminant therefore never vanishes at such points, and the original power series continues analytically there. The analytic function \(G(z/2)\) extends throughout \(|z|<2\sigma\); its unique simple zero of the discriminant on \(|z|=\sigma\) yields a standard dented-disk continuation at \(\sigma\). The transfer theorem for a square-root singularity, using \([z^n](1-z/\sigma)^{1/2}\sim-\sigma^{-n}/(2\sqrt\pi n^{3/2})\), now gives
\[
 \frac{A_n}{n!}\sim\frac{1}{2\sqrt\pi}\sqrt{\frac\sigma P}\,\sigma^{-n}n^{-3/2}
 =\sqrt\sigma\,B\,\sigma^{-n}n^{-3/2}.
\]
This completes the proof.

## Verification

Run the standard-library-only script `python3 verify.py`. It recomputes the first thirteen moments from the rational recurrence, and uses outward integer-rounded, fixed-grid interval arithmetic to enclose the logistic orbit and derivative product for 150 iterations. The rigorous product and rate inequalities above convert these finite orbit enclosures into enclosures for the **infinite** quantities. At iteration 150, the certified interval widths are below \(5.5\times10^{-47}\) for \(\sigma\) and \(5.1\times10^{-47}\) for \(B\), with \(\pi\) bounded by printed decimal rational endpoints. The script does not infer infinite asymptotics from a finite sample: the preceding argument proves them.

## Relationship to prior work

Krapivsky (2026), Section III, equations (43), (59), (62), and (65)–(67), already derived the moment recurrence and the equal-half logistic reduction. It explicitly left the dimensionless large-mass exponential rate and amplitude undetermined. Here the new content is a **rigorous coefficient asymptotic**, two convergent formulas identifying its precise constants, and effective rational error bounds. Its tentative density-tail relation (55) is not promoted into a proven pointwise asymptotic by this work. Kawagoe et al. (2017) study a spatial diffusion/aggregation/fragmentation trail process with distinct kinetics and small-mass tails, not this mean-field stationary moment radius. Standard analytic-combinatorics transfer methods are mathematical tools, not a prior proof for these constants.

## Limitations

The theorem determines the exponential moment radius and all-order moment leading coefficient, but it **does not** prove the physical density has a pointwise \(x^{-3/2}e^{-\sigma\lambda x}\) tail, or a quantitative finite-time convergence rate for the model. It assumes the stationary moment hierarchy's validity, as in the cited primary model. A general result for analytic functional equations could imply aspects of the singularity analysis; originality is asserted only for the specific explicit dyadic constants and proved moment asymptotic, subject to independent literature assessment.

## References

1. P. L. Krapivsky, *Aggregation-Fragmentation Processes with Broken Detailed Balance*, arXiv:2605.22383v1 (publicly posted 2026-05-21), especially Section III and equations (43), (55), (59), (62), (65)–(67). https://arxiv.org/abs/2605.22383
2. K. Kawagoe, G. Huber, M. Pradas, M. Wilkinson, A. Pumir and E. Ben-Naim, *Aggregation-fragmentation-diffusion model for trail dynamics*, Phys. Rev. E **96**, 012142 (2017); arXiv:1705.05400. https://arxiv.org/abs/1705.05400
3. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapter VI (square-root singularity transfer); available at https://ac.cs.princeton.edu/home/.
