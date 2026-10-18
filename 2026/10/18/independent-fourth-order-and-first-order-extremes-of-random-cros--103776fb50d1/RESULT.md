# Independent fourth-order and first-order extremes of random cross-polytope sections

## Finding

Let \(C_n=\{x\in\mathbb R^n:\sum_{i=1}^{n}|x_i|\le1\}\), \(n\ge2\), and let \(H_n\) be a Haar-uniform central hyperplane. The Euclidean diameter \(D_n\) and the smallest Euclidean norm \(R_n\) among **vertices** of \(C_n\cap H_n\) have the joint limit
\[
\left(n\sqrt{\log n}(2-D_n),\;n^4\left(R_n-\frac1{\sqrt2}\right)\right)
\Longrightarrow\left(E,\frac{W^2}{2\sqrt2}\right),
\]
where \(E\sim\operatorname{Exp}(1/\sqrt\pi)\) and \(W\sim\operatorname{Exp}(2/\pi)\) are **independent**. The second marginal therefore has exact limiting survival function \(\exp(-2^{7/4}\sqrt t/\pi)\) for \(t\ge0\). The first marginal is known; the contribution here is the sharp fourth-order vertex-radius law and, principally, the simultaneous asymptotic independence of two geometrically opposite extremes.

## Assumptions and scope

The normal is Haar-uniform on \(S^{n-1}\), the section is central, and Euclidean norm is the ambient norm. The *minimum vertex norm* is not the inradius of the section (whose center is the origin) and is not the diameter. The comparison scale is the \(\ell_1\)-unit ball with vertices \(\pm e_i\). All statements hold for integer \(n\ge2\) in finite-dimensional identities; limits refer to \(n\to\infty\). The generic assumptions of no zero normal coordinate and no ties in absolute values hold almost surely.

## Proof

**1. All section vertices and opposite extremes.** Write the hyperplane normal as \(G/\|G\|_2\), with independent standard Gaussian coordinates, and let \(X_i=|G_i|\). For every unordered pair \(i<j\), two opposite edges of \(C_n\) cross the hyperplane. Their two section vertices are antipodal and have common Euclidean norm
\[
 r_{ij}=\frac{\sqrt{X_i^2+X_j^2}}{X_i+X_j}
 =\frac1{\sqrt2}\sqrt{1+\left(\frac{X_i-X_j}{X_i+X_j}\right)^2}.
\]
Every vertex of a generic hyperplane section of a polytope arises from a crossed edge, so these are all \(n(n-1)\) vertices. Hence, with
\[
 Z_n=\min_{i<j}\frac{|X_i-X_j|}{X_i+X_j},\qquad m_n=\min_i X_i,\qquad M_n=\max_i X_i,
\]
we have the exact identities
\[
 R_n=\frac1{\sqrt2}\sqrt{1+Z_n^2},\qquad
 D_n=2\frac{\sqrt{m_n^2+M_n^2}}{m_n+M_n}.
\]
The diameter identity is previously known and is **not claimed as new**. It follows by maximizing the pair norm: for \(0<a\le b\), the ratio \(\sqrt{a^2+b^2}/(a+b)\) increases with \(b/a\).

**2. Close-pair Poisson limit.** The variables \(X_i\) have density \(f(x)=\sqrt{2/\pi}\,e^{-x^2/2}\) on \([0,\infty)\). Given fixed \(u\ge0\), put \(\delta=u/n^2\) and
\[
 N_n(u)=\sum_{1\le i<j\le n}\mathbf1\left\{\frac{|X_i-X_j|}{X_i+X_j}\le\delta\right\}.
\]
For two independent observations, the event is \(x(1-\delta)/(1+\delta)\le y\le x(1+\delta)/(1-\delta)\). Dominated convergence, using the boundedness of \(x f(x)\), gives
\[
 p_\delta=\Pr\left\{\frac{|X_1-X_2|}{X_1+X_2}\le\delta\right\}
 =4\delta\int_0^\infty x f(x)^2\,dx+o(\delta)
 =\frac4\pi\delta+o(\delta).
\]
Moreover, uniformly in \(x\ge0\) and for \(0<\delta<1/3\), the probability that an independent observation \(Y\) satisfies \(|Y-x|/(Y+x)\le\delta\) is at most \(C\delta\): the admissible interval has length at most \(5\delta x\), its left endpoint is at least \(x/2\), and \(\sup_{x\ge0}x f(x/2)<\infty\).

For each fixed integer \(r\ge1\), expand the factorial moment \(\mathbb E[(N_n(u))_r]\) over ordered \(r\)-tuples of *distinct edges* in the complete graph on \(n\) indices. Contributions from pairwise vertex-disjoint edges converge to \((2u/\pi)^r\), by independence and the above pair probability. Any other edge graph has \(v\) vertices, \(c\) connected components, with \(v\ge2c+1\). Exposing a spanning forest successively and using the uniform conditional bound shows its joint probability is at most \((C\delta)^{v-c}\); there are \(O_r(n^v)\) labelings. Its contribution is \(O_r(n^{2c-v})=O_r(n^{-1})\). Thus all factorial moments tend to those of \(\operatorname{Poisson}(2u/\pi)\), yielding
\[
 N_n(u)\Longrightarrow\operatorname{Poisson}(2u/\pi),\qquad
 \Pr(n^2 Z_n>u)\longrightarrow e^{-2u/\pi}.
\]
In particular \(n^2Z_n\Longrightarrow W\sim\operatorname{Exp}(2/\pi)\). The exact identity for \(R_n\) and Taylor expansion at zero now imply \(n^4(R_n-1/\sqrt2)\Longrightarrow W^2/(2\sqrt2)\).

**3. Asymptotic independence from the sample minimum.** Fix \(t\ge0\). On the event \(n m_n>t\), the independent half-normal observations are distributed conditionally as independent copies truncated below at \(t/n\). Write \(f_{n,t}(x)=f(x)\mathbf1_{x>t/n}/[1-F(t/n)]\). For fixed \(t\), its pair probability still satisfies \(p^{(n,t)}_{u/n^2}=4u/(\pi n^2)+o(n^{-2})\): the removed integration region shrinks to zero, and the normalizing denominator tends to one. Likewise the uniform conditional close-pair bound remains \(C_t\delta\). Thus the identical factorial-moment proof, under this conditioning, gives
\[
 \Pr(N_n(u)=0\mid n m_n>t)\longrightarrow e^{-2u/\pi}.
\]
Since \(F(s)=\sqrt{2/\pi}\,s+O(s^3)\) near zero,
\[
 \Pr(nm_n>t)=(1-F(t/n))^n\longrightarrow e^{-\sqrt{2/\pi}\,t}.
\]
Multiplication yields convergence of the joint upper-tail probabilities of \(nm_n\) and \(n^2Z_n\) to those of **independent** exponentials with respective rates \(\sqrt{2/\pi}\) and \(2/\pi\); continuity of the marginals identifies their joint weak limit.

**4. Diameter scaling and the joint geometric limit.** Standard Gaussian maximum bounds imply \(M_n/\sqrt{2\log n}\to1\) in probability: use a union bound for the upper tail, and \(F(s)^n\) together with a Gaussian lower-tail estimate for the lower tail. Since \(m_n/M_n\to0\) in probability and \(2-2\sqrt{1+q^2}/(1+q)=2q+O(q^2)\) as \(q\downarrow0\), we obtain
\[
 n\sqrt{\log n}(2-D_n)=\sqrt2\,nm_n+o_{\Pr}(1).
\]
The joint limit in Step 3 and Slutsky's theorem therefore imply the stated independent limit, because scaling an exponential variable of rate \(\sqrt{2/\pi}\) by \(\sqrt2\) produces rate \(1/\sqrt\pi\). Finally, \(\Pr(W^2/(2\sqrt2)>t)=\exp(-2^{7/4}\sqrt t/\pi)\).

## Verification

The accompanying `verify.py` checks the complete section-vertex formula against explicitly intersected crossed edges, verifies the extreme diameter and minimum-vertex-radius identities for independently seeded Gaussian normals, confirms the pair-probability constant by numerical quadrature, and compares simulated tail probabilities with the independently derived two marginal limits. Run `python verify.py`. These finite checks are **not** proofs of convergence or independence; the analytical factorial-moment and conditioning arguments above are the proofs.

## Relationship to prior work

The September 2026 preprint of Guédon, Litvak, Tatarko and Vritsiou studies random **diameters** of general convex-body sections and motivates the present geometry. The published October 2026 note *Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections* proves precisely the first **marginal** and the section-vertex representation in Step 1; neither is new here. Its full proof was compared directly: it does **not** consider the smallest vertex norm, Poisson near-tie pairs, or the joint independence of the first- and fourth-order extremes. The 2017 study *Spacings Around An Order Statistic* analyzes local sample spacings and independence from a **selected order statistic**, not the global ratio-gap minimum coupled with geometric diameter and vertex radius. Classical spacing theory motivates, but does not itself assert, the simultaneous geometric limit with these two sharp normalizations.

## Limitations

Only Haar-distributed **central hyperplane** sections of the Euclidean \(\ell_1\) unit ball are covered, not arbitrary codimension, noncentral sections, or weighted cross-polytopes. The proof provides weak convergence, not convergence of moments, finite-dimensional exact joint densities, or quantitative convergence rates. The two marginal phenomena have connections to general sample-extreme and small-spacing theory, and an equivalent reformulation may predate the geometric statement; absence in indexed searches cannot exclude that priority risk. Independent scientific audit has not been performed.

## References

1. O. Guédon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, publicly posted 21 September 2026, arXiv:2609.24131, https://arxiv.org/abs/2609.24131.
2. *Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections*, published 11 October 2026, published-finding corpus research record `2026/10/11/SCOPE-exact-diameter-law-and-exponential-endpoint-fluctuations-for-ran--72b090c504e9`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-diameter-law-and-exponential-endpoint-fluctuations-for-ran--72b090c504e9.
3. H. N. Nagaraja, K. Bharath, F. Zhang, *Spacings Around An Order Statistic*, arXiv:1702.05910, https://arxiv.org/abs/1702.05910.
4. L. Weiss, *The limiting joint distribution of the largest and smallest sample spacings*, Annals of Mathematical Statistics **30** (1959), 590–593; compare spacing-extremal background, not a random-section theorem.
