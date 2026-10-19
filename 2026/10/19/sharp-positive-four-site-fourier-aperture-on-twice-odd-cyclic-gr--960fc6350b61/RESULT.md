# Sharp positive four-site Fourier aperture on twice-odd cyclic grids

## Finding
For each integer \(q\geq1\), let \(N=4q+2\), \(A=\{0,1,2,3\}\subset\mathbb Z/N\mathbb Z\), and \(D=3q+2=\lceil3N/4\rceil\). For each \(j\in\mathbb Z/N\mathbb Z\), put \(v_j=(e^{2\pi iaj/N})_{a\in A}\in\mathbb C^4\). The least integer \(L\in\{0,\ldots,N-1\}\) for which nonnegative weights supported on the consecutive frequency window \(\{0,\ldots,L\}\) obey
\[
\sum_{j=0}^L w_jv_jv_j^*=I_4
\]
is exactly \(D\). This minimum is attained with *strictly positive weights at both window endpoints* and at most eight positive-weight frequencies; at \(N=6\), repeated locations are combined, giving six frequencies. The explicit rule below works for every \(q\), including \(q=1\). Any translated frequency window has the same minimum length by diagonal unitary conjugation.

## Assumptions and scope
Only \(N\equiv2\pmod4\), \(N\ge6\), is asserted; the arithmetic restriction ensures four equally spaced frequency locations do not lie on the cyclic grid. Weights are real and nonnegative, normalized by \(\sum_j w_j=1\), and the Fourier vectors have unnormalized components of modulus one. Thus the diagonal frame equations equal one, and the off-diagonal equations demand exact vanishing of the first three Fourier moments. The claim concerns the minimum *frequency aperture* (last-minus-first frequency within a nonwrapping consecutive window), not the minimum number of distinct sampled frequencies.

## Proof
Put \(s=1/\sqrt2\). **Necessity.** Suppose \(0\le L<3N/4\) and \(\mu\) is a probability weighting of the grid points \(j=0,\ldots,L\) annihilating the first three complex Fourier moments. Recenter the angles as \(\theta_j=2\pi j/N-\pi L/N\), and write \(x_j=\cos\theta_j\). Since \(|\theta_j|\le\pi L/N<3\pi/4\), one has \(x_j>-s\). The vanishing moments and the identities \(\cos2\theta=2x^2-1\), \(\cos3\theta=4x^3-3x\) imply
\[
\mathbb E_\mu x=0,\qquad\mathbb E_\mu x^2=1/2,\qquad\mathbb E_\mu x^3=0.
\]
The cubic \(Q(x)=(x+s)(x-s)^2=x^3-sx^2-s^2x+s^3\) satisfies \(\mathbb E_\mu Q(x)=0\) because \(s^2=1/2\). Yet \(Q(x_j)\ge0\) and, on \(x_j>-s\), equality is possible only for \(x_j=s\). The zero expectation would force all positive mass to lie at \(x=s\), contradicting \(\mathbb E_\mu x=0\). Hence \(L\ge\lceil3N/4\rceil=D\).

**Constructive sufficiency.** Define
\[
\theta_0=\frac{\pi(N-D)}N=\frac{\pi q}{4q+2},\qquad
\theta_1=\theta_0+\frac{2\pi}N=\frac{\pi(q+2)}{4q+2},
\quad u=\cos\theta_0,\quad v=\cos\theta_1.
\]
For \(q\ge1\), \(0<\theta_0<\pi/4<\theta_1\le\pi/2\), so \(0\le v<s<u\). Therefore
\[
\alpha=\frac{1/2-v^2}{u^2-v^2}\quad\hbox{satisfies}\quad0<\alpha<1,
\qquad\alpha u^2+(1-\alpha)v^2=1/2.
\]
Start with all weights zero; add \(\alpha/4\) at *each occurrence* in the four-index list
\[
J_u=(0,D,N/2,D-N/2),
\]
and add \((1-\alpha)/4\) at each occurrence in
\[
J_v=(1,D-1,N/2+1,D-N/2-1).
\]
Every index lies in \(\{0,\ldots,D\}\). A location occurring twice receives the sum of the two contributions; this occurs when \(N=6\). In the centered-angle coordinates \(\theta_j=2\pi j/N-\pi D/N\), the four entries of \(J_u\) give equally weighted cosine values \(u,u,-u,-u\), and those of \(J_v\) give \(v,v,-v,-v\) (with coinciding zero cosine values handled by the multiset convention). Reflection \(j\mapsto D-j\) makes the imaginary part of each centered Fourier moment vanish. The induced distribution of \(x=\cos\theta\) consequently satisfies
\[
\mathbb E x=0,\quad \mathbb E x^2=\alpha u^2+(1-\alpha)v^2=1/2,\quad\mathbb E x^3=0.
\]
Hence \(\mathbb E\cos(k\theta)=0\) for \(k=1,2,3\), and all the original complex moments vanish. The weights sum to one, proving the exact Parseval identity. Since indices \(0,D\in J_u\) have positive weights, the window endpoints are occupied. This achieves the lower bound.

## Verification
The accompanying standalone file `verify.py` computes these weights using standard-library numerical arithmetic and checks normalization, support range, endpoint occupation, and all three Fourier moments for every even \(N=4q+2\le998\). It uses tolerances only as a finite consistency test. The universal assertion is proved by the preceding cubic positivity certificate and symbolic four-atom moment calculation; the finite test is not an infinite proof.

## Relationship to prior work
Bownik and Yu, *Uniform discretization of continuous frames* (arXiv:2603.10423v1, initially public March 11, 2026), establish uniformly discrete near-tight samples for broad continuous frames. Their theorem does not determine this exact finite cyclic Fourier aperture or construct weights meeting four-site Parseval identities. Tan and Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples* (arXiv:2609.07646v1, September 7, 2026), provide a strong general lower-arc obstruction from initial vanishing Fourier moments; the cubic necessity here is consistent with and can be viewed as an instance of that method. Their abstract and an accessible detailed secondary exposition were checked, but their complete primary manuscript was not available in this run; the affirmative exact construction for orders \(N\equiv2\pmod4\) is the assessed contribution, **not** the lower-arc bound alone. Three-site cyclic sampling solves only the first two moment constraints; it does not imply the present three-moment construction on the twice-odd grids. A complete historical-priority determination requires comparison with possibly unindexed positive cyclic quadrature literature.

## Limitations
This theorem does not classify the odd-order cyclic case, the minimum number of nonzero weights, arbitrary four-point site sets, or robustness to weight perturbations. The computational tests have finite range. The inaccessible primary body of arXiv:2609.07646v1 and possible classical cyclic quadrature treatments remain literature-priority risks. No independent scientific audit has been performed.

## References
1. M. Bownik and P.-T. Yu, *Uniform discretization of continuous frames*, arXiv:2603.10423v1 (2026), https://arxiv.org/abs/2603.10423.
2. H. Tan and Y. Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646v1 (2026), https://arxiv.org/abs/2609.07646.
