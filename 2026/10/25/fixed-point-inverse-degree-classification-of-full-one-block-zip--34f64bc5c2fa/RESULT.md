# Fixed-point inverse-degree classification of full one-block zip shifts

## Finding
Let \(S\) and \(Z\) be nonempty finite alphabets, let \(\tau:S\twoheadrightarrow Z\), and let \(F_\tau\) be its full one-block zip shift. Put \(d_z=|\tau^{-1}(z)|\). The polynomial
\[
 I_\tau(v)=\sum_{x\in\operatorname{Fix}(F_\tau)}v^{|F_\tau^{-1}(x)|}
             =\sum_{z\in Z}d_zv^{d_z}
\]
is a **complete topological-conjugacy invariant** within this family: \(F_\tau\) and \(F_\rho\), even when presented over different alphabets, are topologically conjugate if and only if \(I_\tau=I_\rho\), equivalently if and only if the positive integer multisets \(\{d_z:z\in Z\}\) agree. Consequently, for \(|S|=N\geq1\) there are exactly \(p(N)\) conjugacy classes, indexed by partitions of \(N\); with \(|Z|=k\), the number is the number of partitions of \(N\) into exactly \(k\) positive parts.

All these systems for fixed \(N\) have topological entropy \(\log N\), exactly \(N^n\) points fixed by the \(n\)-th iterate, dynamical zeta function \((1-Nt)^{-1}\), and natural extension conjugate to the full two-sided \(N\)-shift. Nevertheless the degree-refined periodic zeta functions
\[
 \zeta_{\tau,r}(t)=\exp\!\left(\sum_{n\geq1}\frac{t^n}{n}
 \sum_{x\in\operatorname{Fix}(F_\tau^n)}
 \prod_{j=0}^{n-1}|F_\tau^{-1}(F_\tau^j x)|^r\right)
 =\frac{1}{1-t\sum_{z\in Z}d_z^{r+1}}
\]
for nonnegative integers \(r\) detect differences invisible to the ordinary zeta function. The polynomial \(I_\tau\), already supported at period one, is sufficient for complete classification.

## Assumptions and scope
Precisely, \(\Sigma_\tau=Z^{\{\ldots,-2,-1\}}\times S^{\{0,1,\ldots\}}\), with product topology. For \(x\in\Sigma_\tau\), define
\[
 (F_\tau x)_i=\begin{cases}\tau(x_0)&i=-1,\\x_{i+1}&i\ne-1.\end{cases}
\]
Every coordinate is independent subject only to alphabet membership; the map is continuous and onto. All conjugacies are unrestricted homeomorphisms \(h\) satisfying \(h\circ F_\tau=F_\rho\circ h\), not necessarily one-block codes. The theorem does not cover constrained shifts, higher-block transition maps, or arbitrary endomorphisms admitting zip-shift factors. The parameter \(N\) can differ between two given presentations: equality of the polynomials forces equal \(N\).

## Proof
**1. Local inverse degrees.** Given \(x\in\Sigma_\tau\), every inverse image \(y\) must satisfy \(y_i=x_{i-1}\) for \(i\ne0\) and \(\tau(y_0)=x_{-1}\). Conversely every choice of \(y_0\in\tau^{-1}(x_{-1})\) gives an inverse image. Thus
\[
 \delta_\tau(x):=|F_\tau^{-1}(x)|=d_{x_{-1}}.
\]
In particular the degree is always a finite positive integer. A conjugacy \(h\) induces bijections of inverse-image sets, hence \(\delta_\rho(hx)=\delta_\tau(x)\).

**2. Fixed points and completeness.** The equality \(F_\tau(x)=x\) forces every nonnegative coordinate of \(x\) to be one symbol \(s\in S\), and every negative coordinate to be \(\tau(s)\). Conversely such a point is fixed. Its degree is \(d_{\tau(s)}\). Grouping the \(N\) fixed points according to the image letter gives \(I_\tau(v)=\sum_zd_zv^{d_z}\). For each integer \(d\ge1\), the coefficient of \(v^d\) is \(d\) times the number of image letters with fiber size \(d\). Consequently \(I_\tau\) reconstructs the whole multiset of positive fiber sizes. Conversely, equality of those multisets permits bijections \(\alpha:S\to S'\), \(\beta:Z\to Z'\) satisfying \(\rho\circ\alpha=\beta\circ\tau\). Applying \(\alpha\) to each nonnegative coordinate and \(\beta\) to each negative coordinate defines a homeomorphism intertwining the two zip shifts. Necessity holds for *any* conjugacy by the intrinsic inverse-degree count. This proves the classification in both directions.

**3. Class counting.** Fiber sizes are positive integers summing to \(N\); conversely every partition of \(N\) is realized by a surjection from an \(N\)-letter alphabet. The classification therefore gives precisely \(p(N)\) distinct classes, and the fixed target-alphabet cardinality restriction amounts to partitions into the corresponding number of parts.

**4. Periodic points and weighted zeta functions.** If \(F_\tau^n x=x\), the forward coordinates consist of a periodic word \(w\in S^n\). For every negative coordinate \(i<0\), periodicity and the orbit rule force \(x_i=\tau(w_{i\bmod n})\). Conversely these choices give one periodic point for each word, so \(|\operatorname{Fix}(F_\tau^n)|=N^n\). Along the orbit associated with \(w\), the multiset of inverse degrees is \(\{d_{\tau(w_j)}:0\le j<n\}\). Therefore the total degree-weighted fixed-point sum equals
\[
 \sum_{w\in S^n}\prod_{j=0}^{n-1}d_{\tau(w_j)}^r
  =\left(\sum_{s\in S}d_{\tau(s)}^r\right)^n
  =\left(\sum_{z\in Z}d_z^{r+1}\right)^n.
\]
The formal-power-series identity \(\exp(\sum_{n\ge1}u^n/n)=(1-u)^{-1}\) gives the advertised rational functions, including \(r=0\).

**5. Natural extension and entropy.** Let \(S^{\mathbb Z}\) have its full shift \(\sigma\). The zipper projection \(\pi:S^{\mathbb Z}\to\Sigma_\tau\) sends \((s_i)_{i\in\mathbb Z}\) to \(x_i=s_i\) for \(i\ge0\) and \(x_i=\tau(s_i)\) for \(i<0\). This continuous onto map satisfies \(\pi\sigma=F_\tau\pi\). Because its inverse-limit lift records the complete orbit \((F_\tau^j\pi(s))_{j\in\mathbb Z}\), and the symbol \(s_j\) can be recovered as coordinate zero of its \(j\)-th element, this lift is a continuous bijection between compact and Hausdorff spaces; it is a conjugacy with the natural extension. Entropy monotonicity under factors gives \(h_{\mathrm{top}}(F_\tau)\le\log N\) from \(\pi\). Projection onto nonnegative coordinates gives the full one-sided \(N\)-shift as a factor of \(F_\tau\), giving the reverse inequality.

## Verification
The standalone `CHECKS.py` enumerates all surjections for \(1\le N\le6\), confirms that their fixed-point inverse-degree polynomials have precisely partition-many values, and checks weighted fixed-period sums for \(N\le4\), \(1\le n\le3\), \(0\le r\le2\). Its observed output was `CHECKS_PASS 5316 surjective maps; N=1..6; periodic n=1..3 for N<=4; weighted r=0..2`. All infinite statements follow from the arguments above rather than these finite computations.

For instance, with \(N=4\), fiber partitions \((3,1)\) and \((2,2)\) yield respectively \(I(v)=3v^3+v\) and \(I(v)=4v^2\). Both have entropy \(\log4\), ordinary zeta \((1-4t)^{-1}\), and full four-symbol natural extensions, but cannot be conjugate. The first degree-weighted zetas are respectively \((1-10t)^{-1}\) and \((1-8t)^{-1}\).

## Relationship to prior work
Lamei and Mehdipour (arXiv:2502.11272v1, Sections 2–5) introduced zip shifts, their local-preimage analysis, and conjugacies to examples of noninvertible horseshoes; in particular, their Example 4.3 contrasts constant-degree systems. Their paper provides the object and motivates conjugacy classification, but the present claim characterizes *all* full one-block presentations, including nonconstant fiber sizes, by an intrinsic fixed-point polynomial, counts classes for every \(N\), and separates them from entropy, ordinary periodic counts and their shared natural extensions. Lamei, Mehdipour and Vargas (arXiv:2510.12980v1, Section 2) investigate expansiveness and shadowing, rather than this equivalence criterion. Work on uniform-degree Bernoulli transformations (arXiv:2505.24647) concerns a different, measure-theoretic isomorphism problem and uniform degree. These comparisons do not establish exhaustive novelty.

## Limitations
The classification depends essentially on the **full one-block** presentation, where negative coordinates are independent and the image alphabet map is a letterwise surjection. Fixed-point inverse-degree data need not classify general local homeomorphisms, higher-block zip shifts, sofic constrained spaces, or measure-preserving systems. The refined zeta functions are formal power series and do not claim analytic continuation beyond the displayed rational expressions. Independent mathematical and literature-priority validation has not been performed. Stronger general classification results under other terminology could subsume this theorem; that remains a residual priority risk.

## References
- Sanaz Lamei and Pouya Mehdipour, *Zip shift space*, arXiv:2502.11272v1, 2025-02-16, https://arxiv.org/html/2502.11272v1 (especially §§2–5).
- S. Lamei, P. Mehdipour and W. Vargas, *S-Expansiveness and Zip Shift Maps in Symbolic Dynamics*, arXiv:2510.12980v1, 2025-10-14, https://arxiv.org/html/2510.12980v1 (§2).
- *Square Entropy and Uniform n-to-1 Bernoulli Transformations*, arXiv:2505.24647, 2025-05-30, https://arxiv.org/abs/2505.24647 (§4, uniform-degree comparison).
- *Zip cellular automata*, *Chaos* (2026), https://doi.org/10.1063/5.0300898 (related zip-shift constructions).
