# Sharp spectral-island bound for multiring weighted Bergman concentration

## Finding

Let \(\alpha>-1\), let \(m\ge1\) be an integer, and let \(E=\bigcup_{j=1}^{m}(a_j,b_j)\) be a union of \(m\) pairwise disjoint intervals with \(0<a_1<b_1<\cdots<a_m<b_m<1\). On the analytic weighted Bergman space \(A^2_\alpha(\mathbb D)\), define the positive concentration operator corresponding to the union of circular annuli \(\{|z|^2\in E\}\): \(T_E=P_\alpha\mathbf 1_{\{|z|^2\in E\}}P_\alpha\). Its eigenvalues in the normalized monomial basis are
\[
\lambda_k=\frac{\int_E t^k(1-t)^\alpha\,dt}{B(k+1,\alpha+1)},\qquad k=0,1,2,\ldots.
\]
For every \(0<c<1\), **the set of integers \(\{k\ge0:\lambda_k>c\}\) consists of at most \(m\) maximal consecutive blocks.** More strongly, the continuous interpolation
\[
\lambda(s)=\frac{\int_E t^s(1-t)^\alpha\,dt}{B(s+1,\alpha+1)},\qquad s\ge0,
\]
has at most \(m\) connected components in \(\{s\ge0:\lambda(s)>c\}\).

The bound is optimal simultaneously for every \(\alpha>-1\), integer \(m\ge1\), and threshold \(0<c<1\): there exist precisely \(m\) disjoint annuli for which the discrete and continuous superlevel sets each have **exactly** \(m\) components. The proof constructs such annuli at geometrically separated radii and uses a gamma scaling limit to prove the necessary strict inequalities.

## Assumptions and scope

The measure is \(d\mu_\alpha(z)=(\alpha+1)\pi^{-1}(1-|z|^2)^\alpha\,dA(z)\), with unnormalized planar area \(dA\). The holomorphic Bergman projection \(P_\alpha\) is orthogonal in \(L^2(\mu_\alpha)\). Each interval endpoint is strictly between zero and one; thus the symbol is a finite union of positive-area annuli whose closure is contained in the disk, and \(T_E\) is positive, diagonal and compact. A “block” means a maximal nonempty run of consecutive nonnegative integer indices. The theorem holds for all stated parameters, not just integral \(\alpha\). It bounds spectral cluster **number**, not their widths or an optimal universal spectral gap.

## Proof

**1. Radial diagonalization.** Substituting \(t=|z|^2\) in the inner product gives \(\|z^k\|^2=(\alpha+1)B(k+1,\alpha+1)\). Angular orthogonality diagonalizes \(T_E\), with Rayleigh quotient exactly \(\lambda_k\). The beta normalization makes \(0<\lambda_k<1\). Since \(b_m<1\), \(\lambda_k\to0\) as \(k\to\infty\). The same concentration estimate shows \(\lambda(s)\to0\) as \(s\to\infty\).

**2. Mellin sign-variation lemma.** Let \(f\) be bounded and piecewise continuous on \((0,1)\), nonzero on a set of positive measure, and suppose its sign changes at most \(r\) times. For a strictly positive weight \(w(t)\) with all integrals convergent, set \(H(s)=\int_0^1f(t)t^sw(t)\,dt\). On any real interval of parameters where the integrals and their derivatives exist, \(H\) has at most \(r\) zeros, *counted with multiplicities*, unless it is identically zero (which is impossible here). To prove it, assume there are \(r+1\) zeros counted with multiplicity at real parameters \(s_i\), and form the \((r+1)\)-dimensional span of the functions \(t^{s_i}(\log t)^h\), taking the appropriate derivative orders at repeated roots. Under \(x=\log t\), these are real exponential polynomials \(e^{s_ix}x^h\), an extended complete Chebyshev system: each nonzero element has at most \(r\) real zeros, counted with multiplicity. This last assertion follows by induction on the number of exponent blocks: divide by the exponential with smallest real exponent and apply Rolle's theorem between zeros; the derivative removes one constant direction, with further applications for repeated exponents. Prescribe the \(r\) sign-change locations of \(f\) as zeros of a nonzero element \(G\) of this span. By the Chebyshev bound, these zeros are all simple and there are no others, so a choice of overall sign gives \(fG\ge0\) almost everywhere and \(fG>0\) on a positive-measure set. Yet the zero conditions on \(H\) and its derivatives yield \(\int_0^1 fGw\,dt=0\), a contradiction. For fewer than \(r\) sign changes apply the same argument with their actual count.

**3. Spectral-island bound.** For fixed \(0<c<1\) consider
\[
H_c(s)=\int_0^1\big(\mathbf1_E(t)-c\big)t^s(1-t)^\alpha\,dt
=B(s+1,\alpha+1)\big(\lambda(s)-c\big).
\]
The sign-changing factor \(\mathbf1_E-c\) is negative off \(E\), positive on each component of \(E\), and has exactly \(2m\) alternating sign changes. By Step 2, \(H_c\) has at most \(2m\) real zeros on \([0,\infty)\), counting tangencies twice. Moreover \(H_c(s)<0\) for all sufficiently large \(s\), because \(\lambda(s)\to0<c\). If the strict positive set had \(m+1\) distinct connected components, transitions into and out of its components, including zero-multiplicity tangencies that split positive intervals, would require at least \(2m+1\) zeros counted with multiplicity; this contradicts the bound. For discrete indices, \(m+1\) nonempty separated high blocks would furnish high points separated by non-high integer points, and eventually a negative tail. The intermediate-value theorem and even multiplicity at any equality-only separator again force at least \(2m+1\) zeros. Therefore both component counts are at most \(m\).

**4. Matching realizations for arbitrary parameters.** Fix \(\alpha>-1\), \(m\ge1\), and \(0<c<1\). Choose \(0<A<B<\infty\) so that
\[
Q=\frac1{\Gamma(\alpha+1)}\int_A^B u^\alpha e^{-u}\,du>c.
\]
This is possible because the gamma density is strictly positive and has total mass one. For a large integer \(L\), set \(K_j=L^{2j}\) for \(1\le j\le m\) and
\[
E_j=\big(1-B/K_j,\,1-A/K_j\big),\qquad E=\bigcup_{j=1}^{m}E_j.
\]
For sufficiently large \(L\), these are nonempty disjoint intervals compactly contained in \((0,1)\). Under the beta probability density \(t^{k}(1-t)^\alpha/B(k+1,\alpha+1)\), the scaled random variable \((k+1)(1-t)\) converges in distribution as \(k\to\infty\) to the gamma law of shape \(\alpha+1\) and unit rate. For each fixed \(j\), at index \(k_j=K_j-1\) the \(j\)-th interval has limiting probability \(Q\), while all the other intervals have limiting probability zero (their scaled endpoints tend to zero or infinity). Thus \(\lambda_{k_j}\to Q>c\). At each separating index \(h_j=L^{2j+1}-1\) for \(1\le j<m\), all the scaled intervals escape to zero or infinity, hence \(\lambda_{h_j}\to0<c\). For large enough \(L\), all \(m\) peak inequalities and all \(m-1\) valley inequalities hold simultaneously. There are at least \(m\) discrete blocks, hence exactly \(m\) by Step 3, and the same high/low witnesses give exactly \(m\) continuous components. This completes the proof.

## Verification

The packaged script `check.py` checks the incomplete-beta representation against independent numerical integration for three weights and nine indices each, verifies 20 exact rational eigenvalue-difference identities, and gives an explicit three-annulus numerical witness at threshold \(1/2\) with alternating spectral peaks and valleys at six indices. It passed 55 assertions. These are consistency checks, not substitutes for the Mellin sign-variation proof or the gamma-limit realization argument. Reproduce with `python check.py` using Python 3 and the `mpmath` package; expected output is saved as `verification_output.txt`.

## Relationship to prior work

The classical theory of totally positive kernels and Chebyshev systems supplies the sign-variation principle underlying the upper bound; that principle alone is **not** asserted as a discovery. Korhonen and Rättyä study sampling and dominating measures for weighted Bergman spaces but do not state the spectral superlevel-component theorem or its matching annulus construction. Maximenko and Pacheco diagonalize Toeplitz operators from general radial measures, giving the eigenvalue framework, and study spectral/functional-analytic properties; their inspected results do not state this optimal count of superlevel bands. The published sharp frequency staircase for harmonic Bergman **circle traces** describes the winning single mode for a one-circle singular trace, and does not cover the threshold-band capacity or matching construction for multiple positive-area annuli.

A related prior result for *Gaussian Bargmann–Fock* annular localization establishes at most \(m\) local-maximum plateaux for its Poisson-weighted eigenvalue sequence, with sharp examples. That statement does not imply the present result for beta-weighted Bergman eigenvalues, whose normalization, disk boundary asymptotics, and spectral-threshold quantifiers differ. The use of generalized Descartes and multiscale separation is related; the present Bergman theorem should not be described as introducing those mechanisms.

The distinctive assertion here is the joint **universal sharp upper bound and realization** for every \(\alpha\), threshold \(c\), and annulus count \(m\), for both continuous Mellin interpolation and the actual discrete concentration spectrum.

## Limitations

The theorem assumes nonnegative characteristic symbols of finitely many centered annuli separated from the boundary, and analytic Hilbert Bergman spaces. It does not treat signed radial masks, nonradial domains, non-Hilbert exponents, or arbitrary infinite collections of annuli. The upper-bound mechanism belongs to classical variation-diminishing theory, so an older rephrasing as a total-positivity corollary cannot be ruled out from searchable literature. The matching multi-scale sharpness realization is proved here, but an unindexed equivalent construction remains an originality risk. No independent mathematical audit has been performed.

## References

1. T. Korhonen and J. Rättyä, *Zero sequences, factorization and sampling measures for weighted Bergman spaces*, arXiv:1709.09956v1 (first public September 28, 2017); *Mathematische Zeitschrift* (2019), DOI: 10.1007/s00209-019-02243-7. Primary classification 30H20.
2. E. A. Maximenko and C. G. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, arXiv:2503.23649 (2025).
3. *Exact frequency staircase for weighted harmonic Bergman circle traces*, published mathematical note (2026), `2026/10/11/SCOPE-exact-frequency-staircase-for-weighted-harmonic-bergman-circle-t--e5356e299a36`.
4. S. Karlin, *Total Positivity*, Stanford University Press (1968), background on variation diminishing and Chebyshev systems.
