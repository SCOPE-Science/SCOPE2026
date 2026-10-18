# Sharp exponential rarity and a Gaussian diagonal-image law for regular magma-monoid elements

## Finding

Let \(\mathcal M_n\) be the monoid of all binary operations on an \(n\)-element set under the standard magma-monoid composition, and select \(f\in\mathcal M_n\) uniformly. Let \(R_n\) mean that \(f\) is regular in this monoid, and let \(D_n=|\{f(i,i):1\le i\le n\}|\). For every \(n\ge1\), with \(N=\binom n2\), the exact probability is
\[
\Pr(R_n)=\sum_{d=1}^{n}\frac{\binom nd\,d!\,S(n,d)}{n^n}\left(1-\frac{n-d}{n^2}\right)^N,
\]
where \(S(n,d)\) denotes a Stirling number of the second kind. **This exact enumeration is a prior result, not the new claim** (Baiduk–Kozerenko, Theorem 25).

The new conclusions are a *sharp equivalent including its leading multiplicative constant* and the *conditional Gaussian distribution of diagonal-image size*. Let \(\lambda_*\in(0,1)\) be the unique root of
\[
(\lambda_*-1)e^{\lambda_*}+1=e^{-1/2},\qquad x_*=(1-e^{-\lambda_*})/\lambda_*.
\]
For \(0<x<1\), let \(\lambda(x)>0\) be the unique solution to
\[
x=\frac{1-e^{-\lambda}}{\lambda},\quad H(x)=-x\log x-(1-x)\log(1-x),
\]
and define
\[
h(x)=H(x)-1+x\log(e^{\lambda(x)}-1)-\log\lambda(x),\qquad F(x)=h(x)-(1-x)/2.
\]
Set \(I=-F(x_*)\), \(v_* =x_*^{-1}(1+\lambda_*-x_*^{-1})\), and \(\kappa=-F''(x_*)\), where
\[
F''(x)=-\frac1{x(1-x)}+\frac{e^{\lambda(x)}}{e^{\lambda(x)}-1}\frac1{x'(\lambda(x))},\quad x'(\lambda)=\frac{(\lambda+1)e^{-\lambda}-1}{\lambda^2}.
\]
All three \(I,v_*,\kappa\) are strictly positive. Put
\[
C=\frac{\exp((1-x_*^2)/4)}{x_*\sqrt{(1-x_*)v_*}\sqrt\kappa}.
\]
Then, as \(n\to\infty\),
\[
\boxed{\Pr(R_n)\sim C e^{-In}},\qquad
\boxed{\left.\frac{D_n-nx_*}{\sqrt n}\ \right|\ R_n\ \Longrightarrow\ \mathcal N(0,\kappa^{-1})}.
\]
Numerically, \(\lambda_*\approx0.828102026619\), \(x_*\approx0.680015625794\), \(I\approx0.171897973381\), \(C\approx1.256970100571\), and \(\kappa^{-1}\approx0.093950190004\). The unconditional typical diagonal-image proportion is \(1-e^{-1}\approx0.63212\), strictly below the regularity-conditioned limit.

## Assumptions and scope

All operations are labeled and sampled independently and uniformly from the \(n^{n^2}\) possible binary operation tables; \(n\) tends through positive integers. The monoid product is \((f\triangleleft g)(a,b)=g(f(a,b),f(b,a))\). Regularity means that there exists \(g\in\mathcal M_n\) with \(f\triangleleft g\triangleleft f=f\). Natural logarithms are used. The result concerns regular *elements*, not regularity of the entire monoid, and describes the conditional law with ordinary weak convergence.

## Proof

**1. Image/regularity criterion.** Associate to each operation \(f\) the transformation \(T_f(a,b)=(f(a,b),f(b,a))\) of the square. It commutes with the swap involution \(\tau(a,b)=(b,a)\). Conversely, every transformation commuting with this involution has exactly this form. Monoid multiplication corresponds to composition of the equivariant transformations. An equivariant transformation \(T\) is regular in the equivariant transformation monoid exactly when each swap-fixed point in its image has a swap-fixed preimage. Necessity follows by applying an equivariant inner inverse \(U\) to a fixed image point: \(U(y)=\tau U(y)\), and \(TU(y)=y\). For sufficiency, choose one preimage on each two-element orbit in the image, extend by equivariance, and choose a fixed preimage for each fixed orbit in the image; the resulting equivariant section extends outside the image by mapping all remaining points to a single fixed diagonal point, producing an equivariant inner inverse. Thus \(f\) is regular if and only if every \(z\) for which \(f(a,b)=f(b,a)=z\) for some \(a\ne b\) occurs among the diagonal values \(f(i,i)\).

**2. Conditioning on the diagonal image.** The diagonal table cells are independent uniform labels, so the chance their image has size \(d\) is \(\binom nd\,d!\,S(n,d)/n^n\). Each of the \(\binom n2\) unordered off-diagonal pairs independently yields a uniform ordered label pair. Exactly \(n-d\) of its \(n^2\) possibilities are prohibited diagonal-equal output pairs. Conditional regularity probability is thus \((1-(n-d)/n^2)^N\). This proves the displayed exact probability, agreeing with Baiduk–Kozerenko's earlier count.

**3. Uniform interior saddle point.** Write \(d=nx\) and \(A_{n,d}=\Pr(D_n=d)\). The exponential generating function for surjections gives
\[
A_{n,d}=\binom nd\frac{n!}{n^n}[z^n](e^z-1)^d.
\]
For an interior compact range \(x\in[\delta,1-\delta]\), let \(Y_1,\dots,Y_d\) be iid zero-truncated Poisson variables with parameter \(\lambda(x)\):
\[
\Pr(Y=k)=\frac{\lambda^k}{k!(e^\lambda-1)},\ k\ge1,\quad
\mathbb E Y=1/x,\quad\operatorname{Var}(Y)=v(x)=x^{-1}(1+\lambda-x^{-1}).
\]
Their sum has mean exactly \(n\). A uniform span-one lattice local central-limit estimate (obtainable by Fourier inversion, using the uniform bounded third moments and uniform spectral gap off zero on any compact parameter interval) yields
\[
\Pr\!\left(\sum_{j=1}^dY_j=n\right)=\frac{1+o(1)}{\sqrt{2\pi n x v(x)}}
\]
uniformly on interior compact ranges. The coefficient identity and Stirling's formula then give
\[
A_{n,d}=\frac{1+o(1)}{\sqrt{2\pi n}\,x\sqrt{(1-x)v(x)}}\exp\{n h(x)\}.
\]
The conditional off-diagonal factor has the uniform expansion
\[
\left(1-\frac{1-x}{n}\right)^{n(n-1)/2}
=\exp\left(-\frac{n(1-x)}2+\frac{1-x^2}4+O(n^{-1})\right).
\]
Therefore the contribution at \(d=nx\) equals
\[
\frac{e^{(1-x^2)/4}+o(1)}{\sqrt{2\pi n}\,x\sqrt{(1-x)v(x)}}\exp\{n F(x)\}.
\]

**4. A unique dominant fraction.** Since \(x(\lambda)=(1-e^{-\lambda})/\lambda\) decreases strictly from one to zero, its inverse exists on \((0,1)\). Differentiating by the saddle-point envelope identity gives
\[
F'(x)=\log\!\left(\frac{(1-x)(e^{\lambda(x)}-1)}x\right)+\frac12.
\]
Its derivative is negative everywhere because \(F''(x)=-1/[x(1-x)]+[e^{\lambda}/(e^{\lambda}-1)]/x'(\lambda)<0\). The unique critical-point equation simplifies to \((\lambda-1)e^\lambda+1=e^{-1/2}\). The left side increases strictly for positive \(\lambda\), starting at zero and exceeding \(e^{-1/2}\) at \(\lambda=1\); hence there is one root in \((0,1)\). In particular, \(x_*\) is the sole global maximum. At the endpoints \(F(x)\to-\infty\) as \(x\downarrow0\) and \(F(x)\to-1\) as \(x\uparrow1\), both below the interior maximum. Moreover \(F(x_*)<0\): because occupancy probabilities never exceed one, the large-deviation exponent satisfies \(h(x)\le0\) on the interior; the extra contribution \(-(1-x)/2\) is strictly negative. Direct substitution gives \(F(x_*)\approx-0.1718979734\).

**5. Tail control and discrete Laplace method.** For arbitrary \(d\in\{1,\dots,n\}\) use the nonnegative coefficient bound \([z^n](e^z-1)^d\le(e^\lambda-1)^d/\lambda^n\) with \(\lambda=\lambda(d/n)\), together with Stirling bounds uniform in \(d\), obtaining the exponential upper bound \(A_{n,d}\le\exp\{n h(d/n)+O(\log n)\}\). At \(d=n\), use the direct value \(A_{n,n}=n!/n^n\). Since \(F\) has a strictly separated unique maximum and decays to minus infinity near zero, all terms with \(|d/n-x_*|\ge\epsilon\) are exponentially smaller than \(e^{nF(x_*)}\). Within any fixed interior neighborhood, Taylor expansion yields \(F(x)=F(x_*)-\kappa(x-x_*)^2/2+O(|x-x_*|^3)\), with \(\kappa>0\). Summing the resulting discrete Gaussian over a lattice of spacing \(1/n\) gives a factor \(\sqrt{2\pi n/\kappa}\). Multiplying the local prefactor proves \(\Pr(R_n)\sim C e^{-In}\), including the constant \(C\) above. The same localized expansion, with a bounded continuous test function of \((d-nx_*)/\sqrt n\), proves the conditional normal limit of variance \(\kappa^{-1}\).

## Verification

Run the included standalone `verify.py` with Python 3, using no external libraries. It independently enumerates all \(n^{n^2}\) operations for \(n=1,2,3\), checks regularity through the fixed-output criterion, and verifies the exact occupancy formula. For \(n=2\) it separately tests existence of an inner inverse by enumerating every possible intermediate magma operation, independently confirming the fixed-output criterion. It then evaluates the exact occupancy-weighted probability through \(n=640\). At \(n=640\), the ratio of the exact probability to \(Ce^{-In}\) is approximately \(0.999963\), and the conditional diagonal-image fraction is approximately \(0.680268\), and its conditional variance divided by \(n\) is approximately \(0.093976\), near the predicted \(0.093950\). The verifier reports `VERIFY_OK`. This numerical evidence is finite and is not a proof of the limiting statements; the proof uses the uniform local central-limit and Laplace arguments above.

## Relationship to prior work

Baiduk and Kozerenko (2026, arXiv:2607.13746v1, Sections 6–7, especially Proposition 24 and Theorem 25) characterize regular elements of the magma monoid and exactly enumerate them via surjection counts. The exact sum in this result is credited to them. Our new statements extract a sharp **exponential rate and leading constant** plus a **regularity-conditioned Gaussian law for diagonal image size**, neither of which is stated in the inspected parts of their paper. Rafieipour's earlier thesis studies regularity and finite examples; López-Permouth studies idempotents and their counts (a different property). The present inference applies saddle-point analysis to the established structural enumeration rather than claiming discovery of that enumeration.

## Limitations

The asymptotic fixes the uniform labeling model and assumes \(n\to\infty\); no large-deviation local limit outside the Gaussian scale or nonuniform random-table law is claimed. No independent audit has been performed. An equivalent sharp asymptotic could exist in unindexed or inaccessible specialized literature. The local limit lemma is a standard span-one triangular-parameter estimate, not a machine-certified proof. Small-case computations are checks only.

## References

1. Y. Baiduk and S. Kozerenko, *Transformation semigroup perspective on the magma monoid*, arXiv:2607.13746v1 (first public version, 15 July 2026), https://arxiv.org/abs/2607.13746 ; *Semigroup Forum* 113 (2026), 335–356, https://doi.org/10.1007/s00233-026-10659-x.
2. A. Rafieipour, *The Magma Monoid and Related Algebraic Structures*, Ohio University doctoral dissertation (2023), https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=ohiou1702861814455082&disposition=inline .
3. S. R. López-Permouth, *Idempotent elements in binary and s-ary magma monoids*, *São Paulo Journal of Mathematical Sciences* 20, Article 14 (2026), https://doi.org/10.1007/s40863-025-00519-x.
4. L. Comtet, *Advanced Combinatorics*, Reidel (1974), standard Stirling-number and exponential generating-function identities (background).
