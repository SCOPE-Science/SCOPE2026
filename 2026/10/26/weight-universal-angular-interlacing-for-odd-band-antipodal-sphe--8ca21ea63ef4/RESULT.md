# Weight-universal angular interlacing for odd-band antipodal spherical concentration

## Finding
Let \(d\ge3\), let \(K\ge0\) be an integer, and let \(\mathcal B_K=\bigoplus_{j=0}^{K}\mathcal H_{2j+1}(S^{d-1})\) be the **complex** space spanned by spherical harmonics of odd degrees through \(2K+1\). Fix an axis \(u\in S^{d-1}\), a cutoff \(0<c<1\), and any positive measurable function \(h:(0,1)\to(0,\infty)\) such that \(0<\int_{S^{d-1}}h((u\cdot x)^2)\,d\sigma(x)<\infty\). The measure \(d\sigma\) is probability-normalized surface measure. Give \(\mathcal B_K\) the weighted inner product \(\langle f,g\rangle_h=\int f\overline g\,h((u\cdot x)^2)\,d\sigma\); this is a weighted norm on the *fixed, unweighted-defined harmonic band*, not a claim that the constituent harmonic degrees remain mutually orthogonal under the weight.

Compress multiplication by the indicator of the antipodal pair \(E_c=\{x:|u\cdot x|\ge c\}\) to this weighted finite-dimensional band. For each transverse harmonic order \(m=0,1,\ldots,2K+1\), its reduced eigenvalues are \(1>\lambda_{m,1}>\cdots>\lambda_{m,r_m}>0\), where \(r_m=K-\lfloor m/2\rfloor+1\). Every reduced eigenvalue is simple. For *every* adjacent pair \(m,m+1\), the following strict eigenvalue interlacing holds:
\[
\lambda_{m,j}>\lambda_{m+1,j}\quad(1\le j\le r_{m+1}),\qquad
\lambda_{m+1,j}>\lambda_{m,j+1}\quad(1\le j<r_m).
\]
The inequalities hold simultaneously for **all** admissible dimensions, odd bandwidths, cap sizes, and positive zonal weights.

Consequently, the largest eigenvalue of the full concentration operator is the simple axial eigenvalue \(\Lambda=\lambda_{0,1}\), and the next distinct eigenvalue is \(\Lambda_2=\lambda_{1,1}<\Lambda\), with multiplicity exactly \(d-1\). Every maximizing function is proportional to an axial odd polynomial \((u\cdot x)p_*((u\cdot x)^2)\), where \(p_*\) has degree at most \(K\) and is the unique (up to scale) top generalized eigenvector below. For the weighted orthogonal projection \(\Pi_*\) onto that line, the **optimal** quadratic stability inequality is
\[
\int_{E_c}|f|^2h((u\cdot x)^2)\,d\sigma(x)
\le \Lambda\|f\|_h^2-(\Lambda-\Lambda_2)\|f-\Pi_*f\|_h^2\qquad(f\in\mathcal B_K).
\]
The deficit coefficient is sharp; equality occurs precisely when the component orthogonal to the top line lies in the order-one top eigenspace (including the zero component).

## Assumptions and scope
The weight must be strictly positive almost everywhere on the full latitude interval and integrable against the spherical latitude measure. It need not be smooth, bounded, or polynomial. The region consists of two caps sharing one axis, with an interior cutoff. The theorem treats the **full consecutive odd-degree band**, not arbitrary degree masks or even-degree bands. At the endpoints \(c=0\) and \(c=1\), strictness is false or the concentration becomes degenerate; these endpoints are excluded.

Let \(a=c^2\), \(\gamma=(d-3)/2\), and \(k_m=K-\lfloor m/2\rfloor\). Define the positive density on \((0,1)\)
\[
w_m(s)=h(s)s^{\alpha_m}(1-s)^{\gamma+m},\qquad
\alpha_m=\begin{cases}1/2& m\text{ even},\\-1/2&m\text{ odd}.\end{cases}
\]
The reduced concentration quotient for every nonzero complex polynomial \(p\) of degree at most \(k_m\) is
\[
R_m(p)=\frac{\int_a^1|p(s)|^2w_m(s)\,ds}{\int_0^1|p(s)|^2w_m(s)\,ds}.
\]
All reduced eigenvalues are explicitly and reproducibly defined as the generalized eigenvalues \(Hv=\lambda Gv\), with matrix indices \(0\le i,j\le k_m\) and
\[
G^{(m)}_{ij}=\int_0^1s^{i+j}w_m(s)\,ds,\qquad H^{(m)}_{ij}=\int_a^1s^{i+j}w_m(s)\,ds.
\]
No closed elementary formula for these eigenvalues is asserted for arbitrary weights or bandwidths.

## Proof
**1. Angular reduction.** Write \(x=tu+\sqrt{1-t^2}\,y\), where \(y\in S^{d-2}\) is transverse to \(u\). The latitude density of probability surface measure is proportional to \((1-t^2)^\gamma\,dt\,d\sigma_{d-2}(y)\). Classical hyperspherical separation states that harmonics of degree \(\ell\) and transverse order \(m\le\ell\) have separated factors \((1-t^2)^{m/2}C_{\ell-m}^{m+(d-2)/2}(t)Y_m(y)\), with \(Y_m\in\mathcal H_m(S^{d-2})\). For the odd degrees \(1,3,\ldots,2K+1\), these Gegenbauer polynomials, taken at fixed \(m\), span precisely \(t^{\epsilon_m}p(t^2)\) with \(\deg p\le k_m\), where \(\epsilon_m=1\) for even \(m\) and \(\epsilon_m=0\) for odd \(m\). Different transverse orders are orthogonal because the cap and the weight are invariant under the transverse orthogonal group. Substitution \(s=t^2\) proves the stated weights and polynomial quotients. Each radial matrix repeats \(\dim\mathcal H_m(S^{d-2})\) times.

**2. Strict size-bias lemma.** Suppose \(\mu\) and \(\nu\) are finite positive measures on \((0,1)\), positive almost everywhere, with strictly increasing Radon–Nikodym ratio \(d\nu/d\mu\). For any nonzero polynomial \(q\), weighting both by \(|q|^2\) preserves strict monotone likelihood ratio. Consequently, for \(0<a<1\),
\[
\frac{\int_a^1|q|^2\,d\nu}{\int_0^1|q|^2\,d\nu}
>
\frac{\int_a^1|q|^2\,d\mu}{\int_0^1|q|^2\,d\mu}.
\]
This follows by cross multiplication: after pairing one integration point below \(a\) with one above \(a\), the integrand contains the strictly positive difference between the likelihood ratios at the higher and lower points. Polynomial zeros have zero measure, so strictness survives.

**3. Even-to-odd angular step.** If \(m\) is even, the two spaces are both \(\mathbb C[s]_{\le k_m}\), while \(w_m/w_{m+1}=s/(1-s)\) strictly increases. The size-bias lemma gives \(R_m(p)>R_{m+1}(p)\) for every nonzero \(p\), so the Courant–Fischer min–max principle gives \(\lambda_{m,j}>\lambda_{m+1,j}\) for each common index. For the reverse interlacing, compare the \(k_m\)-dimensional trial subspaces \((1-s)\mathbb C[s]_{\le k_m-1}\) in the even sector and \(s\mathbb C[s]_{\le k_m-1}\) in the odd sector. Their effective density ratio, odd over even, is again \(s/(1-s)\); the size-bias lemma followed by Cauchy interlacing for the restricted min–max problems yields \(\lambda_{m+1,j}>\lambda_{m,j+1}\), for all indices where the latter is defined. If \(k_m=0\), only the first comparison is required.

**4. Odd-to-even angular step.** If \(m\) is odd, the former sector has polynomial degree bound \(k_m\), and the next sector has degree bound \(k_m-1\). On \(\mathbb C[s]_{\le k_m-1}\), use trial functions \(sq\) in the odd sector and \(q\) in the following even sector. Their effective density ratio is \(w_m(s)s^2/w_{m+1}(s)=s/(1-s)\), yielding strict comparisons \(\lambda_{m,j}>\lambda_{m+1,j}\) by the same min–max argument. Conversely, the trial functions \((1-s)q\) in the odd sector have effective density ratio \(w_{m+1}(s)/[w_m(s)(1-s)^2]=s/(1-s)\), yielding \(\lambda_{m+1,j}>\lambda_{m,j+1}\). The first and last orders and all index bounds therefore follow without an induction gap.

**5. Simplicity and global order.** Every polynomial quotient lies strictly between zero and one. Suppose a reduced eigenpolynomial \(p\) vanishes at the cutoff \(a\). Testing its eigenvalue equation against \(q=p/(s-a)\), of degree at most \(k_m-1\), gives
\[
0=(1-\lambda)\int_a^1\frac{|p|^2}{s-a}w_m\,ds
-\lambda\int_0^a\frac{|p|^2}{s-a}w_m\,ds>0,
\]
a contradiction. Every eigenpolynomial is therefore nonzero at \(a\). Any eigenspace of dimension at least two would contain a nonzero linear combination vanishing at \(a\), so all reduced eigenvalues are simple. Adjacent-order inequalities put the axial leading eigenvalue above the leading eigenvalue of every other order. The first reverse interlacing gives \(\lambda_{0,2}<\lambda_{1,1}\) when \(K\ge1\); all remaining axial eigenvalues are still lower. Every order at least two has its leading eigenvalue below \(\lambda_{1,1}\). This establishes the top-two classification for every \(K\ge0\), including the case \(K=0\).

**6. Optimal stability.** Orthogonally expand a function into eigenvectors of the self-adjoint concentration operator. The leading coefficient contributes exactly \(\Lambda\) times its squared norm, while every orthogonal component contributes at most \(\Lambda_2\) times its squared norm. This is the displayed inequality. Choosing a nonzero order-one leading eigenfunction proves optimality of the deficit coefficient. The order-one eigenspace has dimension \(\dim\mathcal H_1(S^{d-2})=d-1\), establishing the multiplicity and equality condition.

## Verification
The attached standalone `check.py` evaluates exact rational truncated and full moments for odd spatial dimensions and rational cap cutoffs. It numerically diagonalizes their generalized eigenproblems for multiple bandwidths and tests both strict adjacent-order inequalities, the top-two classification, positive Gram matrices, and eigenvalue ranges. It also tests three positive zonal weights: constant, linear, and quadratic. A replay produced **3726 passing assertions**. The polynomial argument above—not a finite numerical experiment—proves the infinite-dimensional parameter family.

## Relationship to prior work
Simons and Dahlen (2006) formulated double-polar-cap spherical Slepian concentration and separated its harmonic matrices by order and parity. Their available full text supplies the classical operator framework and the commuting-matrix construction, but its reviewed fixed-order spectral sections, plots, and appendix do not give this weight-universal strict interlacing of **different** angular orders or identify the general top-two sharp gap. Michel, Plattner, and Seibert (2021) treat scalar/vector/tensor spherical Slepian functions and commuting operators; their abstract was accessible, but complete text could not be inspected. Gerhards and Huang (2023) study asymptotic eigenvalue distributions for polynomial/Fourier–Jacobi concentration on the *ball*, a distinct operator and asymptotic objective. Other published hemispherical and finite-degree spherical results involve different degree masks and domains. The contribution here is a non-asymptotic angular interlacing theorem and its sharp stability consequence for every odd bandwidth, dimension, and positive zonal weight; the classical Gegenbauer separation and variational tools are not claimed as inventions.

## Limitations
The weight must be positive almost everywhere and even in latitude; no conclusion is claimed for a weight with interior gaps, asymmetric caps, arbitrary degree masks, or an even-degree band. The sharp spectral gap is a computable difference of two finite generalized eigenvalues, not a uniform lower bound independent of the cap size or weight. The general 2021 paper could not be checked in full; an undiscovered broader interlacing theorem remains a priority risk. No independent scientific validation has been performed.

## References
1. F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy* (2006), arXiv:math/0603271, https://arxiv.org/abs/math/0603271 ; particularly §§4–5 and Appendix A.
2. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, initial public submission 2021-03-26, https://arxiv.org/abs/2103.14650 .
3. C. Gerhards and X. Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth*, arXiv:2308.03543, https://arxiv.org/html/2308.03543v4 .
