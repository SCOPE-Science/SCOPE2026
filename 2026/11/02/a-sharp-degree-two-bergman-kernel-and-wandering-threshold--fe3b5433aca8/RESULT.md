# A sharp degree-two Bergman kernel and wandering threshold

## Finding
Let \(\alpha>-1\) and equip the unit-disk weighted Bergman space \(A^2_\alpha\) with
\[
\|f\|_\alpha^2=(\alpha+1)\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,\frac{dx\,dy}{\pi}.
\]
Let \(\mathcal E_2=\overline{\operatorname{span}}\{z^{2n}:n\ge0\}\) and, for \(0\le a<1\), let
\[
 B_a(z)=\frac{z^2-a}{1-a z^2}.
\]
This is a degree-two finite Blaschke product when \(a\in[0,1)\). Write \(M_{B_a}\) for multiplication by \(B_a\). The subspace \(\mathcal E_2\) is \(M_{B_a}\)-invariant and cyclic with cyclic vector \(1\). Its wandering space \(\mathcal E_2\ominus B_a\mathcal E_2\) is one dimensional. The exact threshold for its wandering vector to generate all of \(\mathcal E_2\) is
\[
\boxed{\ \mathcal E_2=\overline{\operatorname{span}}\{B_a^n g:n\ge0,\ g\in\mathcal E_2\ominus B_a\mathcal E_2\}\quad\Longleftrightarrow\quad
 a\le \tan^2\!\left(\frac{\pi}{2(\alpha+2)}\right).\ }
\]
At equality the wandering vector has zeros on the boundary but remains cyclic. Consequently, for \(-1<\alpha\le0\), it is cyclic for every \(0\le a<1\), whereas for each \(\alpha>0\), failure begins at the exact interior threshold \(a=\tan^2(\pi/[2(\alpha+2)])\), with the equality itself still on the cyclic side.

More precisely, put
\[
 \mathcal K_\alpha(t)=\sum_{n=0}^\infty\frac{t^n}{\|z^{2n}\|_\alpha^2},\quad |t|<1.
\]
For integers \(j\ge0\) with \(4j<\alpha\), put
\[
 \rho_j(\alpha)=\tan^2\!\left(\frac{(2j+1)\pi}{2(\alpha+2)}\right).
\]
The complete zero set of \(\mathcal K_\alpha\) in \(\mathbb D\) consists of the distinct simple negative real values \(-\rho_j(\alpha)\), with no others; the number is \(\max\{0,\lceil\alpha/4\rceil\}\). The wandering vector is proportional to \(g_{\alpha,a}(z)=\mathcal K_\alpha(a z^2)\), and its number of zeros in \(\mathbb D\), counted without multiplicity, is exactly
\[
 2\#\big\{j\in\mathbb Z_{\ge0}:4j<\alpha\text{ and }\rho_j(\alpha)<a\big\}.
\]
Thus the full zero-count staircase, not only the first failure threshold, is explicit.

## Assumptions and scope
All statements concern the standard Hilbert norm written above, not an equivalent renorming. The parameter \(a\) is real with \(0\le a<1\). The operator is restricted to the specific cyclic invariant subspace \(\mathcal E_2\); no conclusion about every invariant subspace of \(M_{B_a}\) is asserted. The open disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Each monomial \(z^{2n}\) has strictly positive squared norm
\[
 \|z^{2n}\|_\alpha^2=\frac{\Gamma(\alpha+2)\Gamma(2n+1)}{\Gamma(2n+\alpha+2)}.
\]
The multiplier \(B_a\) is bounded and analytic on a neighborhood of the closed disk. All closures and orthogonal complements are in \(A^2_\alpha\).

## Proof
**1. Kernel and exact zeros.** Orthogonality and completeness of disk monomials yield the displayed squared norms. Put \(s=\alpha+2>1\). The binomial series gives, for \(|u|<1\) and \(x^2=u\),
\[
 \mathcal K_\alpha(u)=\sum_{n\ge0}\frac{(s)_{2n}}{(2n)!}u^n
 =\frac{(1-x)^{-s}+(1+x)^{-s}}2.
\]
The expression is even in \(x\) and hence single-valued in \(u\); powers use logarithms analytic in \(1\pm\mathbb D\) and real at \(1\). At \(u=0\) the value equals \(1\). For a nonzero zero set \(w=(1+x)/(1-x)\), which has positive real part when \(|x|<1\). Then
\[
 s\operatorname{Log}w=(2k+1)\pi i,
\]
for an integer \(k\). As \(|\arg w|<\pi/2\), the only permissible indices satisfy \(|2k+1|<s/2\). They give
\[
 x=i\tan\!\left(\frac{(2k+1)\pi}{2s}\right),\qquad
 u=-\tan^2\!\left(\frac{(2k+1)\pi}{2s}\right).
\]
Opposite odd indices give the two square roots of one \(u\); each nonnegative \(j\) with \(2j+1<s/2\), equivalently \(4j<\alpha\), gives one distinct negative zero. Conversely all those values lie in \(\mathbb D\) and solve the equation. At a zero the derivative of \((1-x)^{-s}+(1+x)^{-s}\) is nonzero: the two summands are negatives and
\[
 \frac{d}{dx}\big((1-x)^{-s}+(1+x)^{-s}\big)
 =\frac{2s(1-x)^{-s}}{1-x^2}\ne0.
\]
As \(x\ne0\), changing from \(x\) to \(u=x^2\) preserves simplicity. This proves the exhaustive zero census, including the strict boundary convention at \(\alpha=4j\).

**2. The exact wandering vector.** Map \(F(w)=\sum_{n\ge0}c_nw^n\) to \(F(z^2)\). The induced coefficient norm has squared monomial weights \(\|z^{2n}\|_\alpha^2\). By the gamma-ratio formula these are bounded above and below by positive multiples of the ordinary \(A^2_\alpha\) weights \(\|z^n\|_\alpha^2\), because their ratio tends to \(2^{-(\alpha+1)}\). Thus the induced space has the same holomorphic functions and equivalent norm. For \(0\le a<1\), division of a Bergman function vanishing at \(a\) by \(w-a\) is bounded: outside a small disk about \(a\) divide pointwise, and inside use the compact-set derivative estimate furnished by bounded Bergman evaluations. Multiplication by \(1-aw\) is bounded, so
\[
 b_a\mathcal H=\{F\in\mathcal H:F(a)=0\},\qquad b_a(w)=\frac{w-a}{1-aw},
\]
for this induced Hilbert space \(\mathcal H\). Transferring to \(\mathcal E_2\) shows
\[
 B_a\mathcal E_2=\{f\in\mathcal E_2:f(\sqrt a)=0\},
\quad \mathcal E_2\ominus B_a\mathcal E_2=\mathbb C\,g_{\alpha,a},
\quad g_{\alpha,a}(z)=\mathcal K_\alpha(a z^2).
\]
The formula includes \(a=0\). Furthermore, \(w=(b_a(w)+a)/(1+a b_a(w))\) and the denominator has a uniformly convergent geometric reciprocal on the closed disk. Hence each monomial in \(w\) is a uniform limit of polynomials in \(b_a\); conversely \(b_a\) is a uniform limit of polynomials in \(w\). Consequently \(1\) is cyclic for \(M_{B_a}\) on \(\mathcal E_2\), and the polynomial orbit of any \(g\) under \(B_a\) is dense exactly when the polynomial orbit of its corresponding \(G(w)\) under \(w\) is dense in \(\mathcal H\).

**3. Boundary zeros are cyclic; interior zeros obstruct.** The function \(G(w)=\mathcal K_\alpha(aw)\) extends holomorphically to \(|w|<1/a\) when \(a>0\), and is identically \(1\) when \(a=0\). If it has a zero in \(\mathbb D\), every polynomial multiple vanishes there, whereas constants do not; hence it is noncyclic. If it has no zero in \(\mathbb D\), its finitely many zeros on the unit circle can be factored as \(G(w)=h(w)\prod_\nu(1-\overline{\zeta_\nu}w)^{m_\nu}\), where \(|\zeta_\nu|=1\), and \(h\) and \(1/h\) are analytic on a neighborhood of the closed disk. Such \(h\) is an invertible multiplier. Each boundary factor is cyclic because
\[
 (1-\overline\zeta w)\sum_{j=0}^N\overline\zeta^{\,j}w^j
 =1-\overline\zeta^{\,N+1}w^{N+1},\qquad
 \|w^{N+1}\|_{\mathcal H}=\|z^{2N+2}\|_\alpha\longrightarrow0.
\]
Products of cyclic polynomial multipliers are cyclic: approximating \(1\) by polynomial multiples of the first factor shows the cyclic subspace of the product contains the second factor, and iterate. Thus \(G\) is cyclic exactly when it has no zero in \(\mathbb D\). By Step 1, the first root has modulus \(\rho_0(\alpha)=\tan^2(\pi/[2(\alpha+2)])\), which is at least \(1\) for \(-1<\alpha\le0\), and is strictly smaller than \(1\) for \(\alpha>0\). Its scaled value enters \(\mathbb D\) precisely when \(a>\rho_0(\alpha)\). Remaining zeros enter at their respective \(a=\rho_j(\alpha)\). Since \(w=z^2\), each interior root yields two simple zeros of \(g_{\alpha,a}\), as claimed.

## Verification
The standalone `CHECK.py` verifies 271 supplementary arithmetic assertions, including integer-weight numerator identities, exact Sturm root counts for weights from zero through twelve, boundary cases, and high-precision noninteger test points. These are finite checks only; the infinite family and completeness of the zero list follow from the analytic binomial/Cayley proof. Reproduce with `python CHECK.py` using SymPy and mpmath.

## Relationship to prior work
Lin, Xu and Yu (arXiv:2609.36723, first public September 29, 2026) determine the global shift wandering threshold for weighted Bergman spaces via zero-based invariant subspaces, not this two-channel Möbius multiplier or the precise location of its cyclic wandering-vector zeros. Gallardo-Gutiérrez, Partington and Seco (arXiv:1904.02974; 2020 publication) study finite Blaschke multipliers, including equivalent renormings and special monomial cases; changing the norm does not settle the present original-norm phase diagram. A later preprint by Xu and Yu (arXiv:2610.37035, first posted October 27, 2026) establishes nonwandering for some finite Blaschke multiplier for each weight, gives a degree-three example at the unweighted Bergman point, and displays an even-subspace kernel series. Its inspected full text does not give the exact degree-two parameter classification or the all-weight scalar zero census. A published mathematical record on Euclidean boundary-distance weighted disk kernels has tangent-square zero locations for a different weight; its result does not imply the present cyclicity criterion. Another record concerns extraneous zeros of zero-based invariant subspaces when \(\alpha>1\), not the specific \(\mathcal E_2\) multiplier problem. The algebraic resemblance of some zero formulas is acknowledged; novelty is claimed only for the exact combined kernel/wandering phase diagram, not for the general binomial-series technique.

## Limitations
The theorem concerns the explicitly defined real one-parameter degree-two Blaschke family and its canonical even-power invariant subspace; it does not classify arbitrary quadratic Blaschke products or all invariant subspaces. It gives no universal Beurling-type theorem for \(M_{B_a}\). General claims of uniqueness across unpublished or unindexed literature are not made. The September 2026 focal preprint was available in indexed abstract form but its full text could not be retrieved in this run; its potential unstated comparison is a residual originality risk. The later October 27 preprint was read in full relevant sections and treated only as overlap evidence, not as an eligible first-public motivating source for the current week.

## References
1. Z. Lin, S. Xu, T. Yu, *The Critical Value for the Beurling-Type Theorem in Weighted Bergman Spaces*, arXiv:2609.36723v1 (first public September 29, 2026), https://arxiv.org/abs/2609.36723.
2. E. A. Gallardo-Gutiérrez, J. R. Partington, D. Seco, *On the Wandering Property in Dirichlet Spaces*, arXiv:1904.02974v1 (April 5, 2019), and *Integral Equations and Operator Theory* 92 (2020), 16. Open accepted text: https://eprints.whiterose.ac.uk/id/eprint/157517/1/GGPS20190729.pdf.
3. S. Xu, T. Yu, *The Beurling-type theorem for powers of weighted Bergman shifts*, arXiv:2610.37035v1 (first public October 27, 2026), https://arxiv.org/html/2610.37035.
4. Published mathematical finding, *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-lu-qi-keng-transitions-for-euclidean-boundary-distance-wei--b68d363f03d0.
5. Published mathematical finding, *Arbitrarily many real extraneous zeros from finite weighted-Bergman zero sets*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-arbitrarily-many-real-extraneous-zeros-from-finite-weighted-berg--7cb0246c0b46.
