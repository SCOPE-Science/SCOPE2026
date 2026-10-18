# A joint Crofton face-vector law and common random exponent for cross-polytope sections

## Finding

Let \(C_n=\operatorname{conv}\{\pm e_1,\ldots,\pm e_n\}\subset\mathbb R^n\), for every integer \(n\ge2\). Choose an affine hyperplane by Euclidean-motion-invariant measure on the space of unoriented hyperplanes, conditioned on intersecting the interior of \(C_n\). Write \(F_{n,j}\) for the number of \(j\)-faces of the section, \(0\le j\le n-2\). The following statements hold simultaneously.

Set \(p(s)=2[1-\Phi(s)]\) for \(s\ge0\), where \(\Phi\) is the standard Gaussian distribution function, and let
\[
 m_n=\mathbb E\max_{1\le i\le n}|G_i|=\int_0^\infty\{1-[1-p(s)]^n\}\,ds
\]
for independent standard Gaussians \(G_i\). There is an integer \(K_n\in\{1,\ldots,n\}\) whose exact law is
\[
 \Pr(K_n=k)=\frac{\binom nk}{m_n}\int_0^\infty p(s)^k[1-p(s)]^{n-k}\,ds,\qquad 1\le k\le n.
\]
The entire section face vector is a deterministic function of that single integer: with \(r=j+2\),
\[
 \boxed{F_{n,j}=2^r\binom nr-\binom{K_n}{r}-
 \sum_{a=0}^r\binom{K_n}{a}\binom{n-K_n}{r-a}2^{r-a}.}
\]
Binomial coefficients outside their usual ranges are zero. In particular,
\[
 \boxed{F_{n,0}=K_n(2n-K_n-1).}
\]
This determines the exact finite-dimensional **joint** distribution (merge different values of \(K_n\) whenever they give the same face vector).

For every \(j\) in the indicated range, define \(\mu_r=\mathbb E\max_{1\le i\le r}G_i\). Then
\[
 \boxed{\mathbb EF_{n,j}=\frac{2^{j+2}\binom n{j+2}\mu_{j+2}}{m_n}.}
\]
In particular, \(\mu_2=1/\sqrt\pi\) and
\[
 \mathbb EF_{n,0}=\frac{2n(n-1)}{\sqrt\pi\,m_n}
 \sim\frac{\sqrt2\,n^2}{\sqrt{\pi\log n}}.
\]

There is a single random variable \(U\), uniform on \([0,1]\), governing **all fixed face ranks** in the large-dimension limit. For every fixed finite collection \(J\subset\mathbb Z_{\ge0}\),
\[
 \boxed{\left(\frac{\log F_{n,j}}{\log n}\right)_{j\in J}
 \Longrightarrow (j+2-U^2)_{j\in J}.}
\]
Equivalently, each shifted marginal has continuous distribution \(\Pr(j+2-U^2\le z)=1-\sqrt{j+2-z}\) for \(j+1\le z\le j+2\). Furthermore,
\[
 \boxed{\frac{F_{n,j}}{n^jF_{n,0}}\xrightarrow{\Pr}\frac{2^j}{(j+1)!},\qquad
 \frac{F_{n,j}}{\mathbb EF_{n,j}}\xrightarrow{\Pr}0}
\]
for every fixed \(j\). Thus a single random exponent is shared across dimensions of faces, while their normalized counts converge to a deterministic profile. Mean face counts, at each fixed rank, are dominated by increasingly atypical hyperplane orientations and offsets.

## Assumptions and scope

Hyperplane measure is the rotation-and-translation invariant measure \(du\,dt\), with unit normal \(u\in S^{n-1}\) and signed offset \(t\in\mathbb R\), modulo the two-to-one identification \((u,t)\sim(-u,-t)\). Conditioning on \(H\cap\operatorname{int} C_n\ne\varnothing\) means that the normal density is proportional to the width \(2h_{C_n}(u)\) and, given the normal, the offset is uniform in \((-h_{C_n}(u),h_{C_n}(u))\), where \(h_{C_n}(u)=\max_i|u_i|\). This is *not* a uniformly chosen oriented central hyperplane. All statements ignore a probability-zero collection of hyperplanes passing through vertices or containing faces. The full face-vector formula holds for every finite \(n\ge2\), while the joint asymptotic assertions hold for fixed \(j\) as \(n\to\infty\) and do not assert control when \(j\) increases with \(n\).

## Proof

**1. A Gaussian representation of invariant hyperplane measure.** Let \(G=(G_1,\ldots,G_n)\) have independent standard-normal coordinates and let \(R=\|G\|_2\). The direction \(G/R\) is uniform on the sphere and independent of \(R\). Write \(M=\max_i|G_i|\), so that \(M=Rh_{C_n}(G/R)\). Reweighting the Gaussian law by \(M\) therefore reweights its direction precisely by \(h_{C_n}\); the extra radial factor \(R\) integrates to a common constant. Conditional on the resulting Gaussian sample, choose an offset uniformly from \((-M,M)\), measured in the unnormalized normal coordinate \(\langle G,x\rangle=t\). Replacing its sign by a sign change of \(G\) reduces to the positive level \(S=|t|\). The resulting joint probability of \((G,S)\) is
\[
  \frac{\prod_i\phi(G_i)}{m_n}\,dG\,dS\,\mathbf1_{\{0<S<M\}},
\]
where \(\phi\) is the standard Gaussian density. This is normalized since \(\int_0^M dS=M\) and \(\mathbb EM=m_n\).

**2. Exact integer law.** At a positive level \(S=s\), the cross-polytope has exactly \(K=\#\{i:|G_i|>s\}\) vertices with projection strictly above \(s\). Each of these indices supplies exactly one high signed vertex; all other signed vertices are below \(s\). For fixed \(s\), the indicators \(\mathbf1_{\{|G_i|>s\}}\) are independent Bernoulli variables with probability \(p(s)\). Integrating their binomial probability against the preceding joint measure gives the stated formula for \(K_n\). The event \(K=0\) makes \(s\ge M\) and is excluded. Summing the formula over \(1\le k\le n\) gives one by the tail integral for \(m_n\).

**3. Exact face counting.** Every \((r-1)\)-face of \(C_n\), \(2\le r\le n\), consists of a choice of \(r\) distinct coordinate indices and a sign for each; there are \(2^r\binom nr\) such faces. A generic hyperplane cuts its relative interior exactly when its signed vertex heights lie on both sides of the level. Exactly \(\binom Kr\) such faces have every vertex above the level. An all-low face may choose \(a\) of the \(K\) active indices, where the single low sign is forced, and \(r-a\) inactive indices, where two low signs are available. Hence the count of all-low faces is
\[
 \sum_a\binom Ka\binom{n-K}{r-a}2^{r-a}.
\]
Subtracting both monochromatic types gives the exact \(j=r-2\) face count of the section. For \(r=2\), elementary binomial simplification gives \(F_{n,0}=K(2n-K-1)\). Distinct intersected faces of \(C_n\) give distinct faces of the generic section, so nothing is overcounted.

**4. Expected face counts.** Each original \((j+1)\)-face has \(r=j+2\) signed coordinate vertices. As the section offset varies at a fixed direction, that face is cut over an interval whose length is the range of its \(r\) vertex projections. Averaging over Gaussian directions gives the expected range of \(r\) independent standard normals, equal by symmetry to \(2\mu_r\). The complete cross-polytope has projection width \(2M\), with mean \(2m_n\). Integrating the face-cutting indicator over invariant hyperplanes and dividing by the total measure of hyperplanes hitting \(C_n\) yields
\[
  \mathbb EF_{n,j}=2^r\binom nr\frac{2\mu_r}{2m_n}.
\]
This is an equality for all finite \(n\ge r\). A direct two-normal calculation gives \(\mu_2=\mathbb E|G_1-G_2|/2=1/\sqrt\pi\). Standard Gaussian tail bounds imply \(m_n\sim\sqrt{2\log n}\), proving the displayed vertex expectation asymptotic.

**5. Uniform offset scale and tail-count exponent.** Marginalizing the Gaussian vector gives
\[
 \Pr(S\in ds)=\frac{\Pr(M>s)}{m_n}\,ds
 =\frac{1-[1-p(s)]^n}{m_n}\,ds,\qquad s>0.
\]
The Gaussian maximum satisfies \(M/\sqrt{2\log n}\to1\) in probability and in mean: the upper bound follows from a union bound and the Gaussian upper tail; the lower bound follows from \(n\Pr(|G_1|>(1-\eta)\sqrt{2\log n})\to\infty\) for each \(0<\eta<1\); uniform integrability follows from the same upper-tail estimate. Consequently, for each \(0<t<1\),
\[
 \Pr\!\left(\frac{S}{\sqrt{2\log n}}\le t\right)
 =\frac{\mathbb E\min\{M,t\sqrt{2\log n}\}}{m_n}\longrightarrow t.
\]
Thus \(S/\sqrt{2\log n}\Rightarrow U\), uniform on \([0,1]\). For levels in any fixed compact subinterval of \((0,1)\) on this scale, Mills' Gaussian tail bounds imply uniformly
\[
 \frac{\log(np(S))}{\log n}=1-\left(\frac{S}{\sqrt{2\log n}}\right)^2+o(1),\qquad np(S)\longrightarrow\infty.
\]
Conditioned on \(S=s\), \(K\) has a binomial \(\operatorname{Bin}(n,p(s))\) law conditioned on being nonzero. The conditioning is asymptotically immaterial on such compact subintervals because \(np(s)\to\infty\); binomial concentration gives \(K/[np(S)]\to1\) in probability there. The excluded ends of \([0,1]\) have arbitrarily small limiting probability. Hence
\[
  \frac{\log K_n}{\log n}\Rightarrow1-U^2,
 \qquad K_n\xrightarrow{\Pr}\infty,
 \qquad K_n/n\xrightarrow{\Pr}0.
\]

**6. All ranks share the same exponent.** A more useful positive counting expansion for \(r=j+2\) is
\[
 F_{n,j}=\sum_{a=1}^{\min(K,r-1)}\binom Ka
 [z^{r-a}](1+z)^{K-a}(1+2z)^{n-K}.
\]
The first term selects exactly one above-level vertex, while all remaining vertices lie below; the remaining terms select two or more above-level vertices. For fixed \(r\), as \(K\to\infty\) and \(K/n\to0\), the first term is
\[
 K\frac{2^{r-1}n^{r-1}}{(r-1)!}\bigl(1+O_r(K/n+1/n)\bigr),
\]
while all other terms together are \(O_r(K^2n^{r-2})\). Therefore
\[
 F_{n,j}=\frac{2^{j+1}}{(j+1)!}K_n n^{j+1}\bigl(1+o_{\Pr}(1)\bigr),
\qquad F_{n,0}=2K_nn(1+o_{\Pr}(1)).
\]
The joint logarithmic weak limit follows by applying this relation to each fixed rank and using the common \(K_n\). Dividing the two relations gives the deterministic rank ratios. Finally, the exact expectation and \(m_n\sim\sqrt{2\log n}\) imply \(\mathbb EF_{n,j}\asymp_j n^{j+2}/\sqrt{\log n}\), whereas the preceding log law places \(F_{n,j}\) below \(n^{j+2-\varepsilon}\) with probability tending to at least \(1-\sqrt\varepsilon\) for any fixed small \(\varepsilon>0\). Letting \(\varepsilon\downarrow0\) proves \(F_{n,j}/\mathbb EF_{n,j}\to0\) in probability. This completes the proof.

## Verification

The accompanying `checker.py` requires only the Python standard library. Running `python checker.py` enumerates the signed-coordinate faces directly for 84 generic sections with dimensions \(2\) through \(8\), checks the exact polynomial count, numerically integrates seven complete distributions and their face expectations, and prints supplementary higher-dimensional simulated exponent comparisons. All integral checks use deterministic composite Simpson quadrature with a truncated Gaussian tail and documented tolerances. The standalone code is supplementary: the exact law, the asymptotic statements, and the infinite-dimension quantifiers are proved above, not inferred from finite tests.

## Relationship to prior work

The September 2026 work of Birkemeyer, Brose, Brandenburg, and Prün develops combinatorial invariants of hyperplane sections, including separate affine and central section hierarchies. De Loera, Lopez-Campos, and Torres (2024/2025) study attainable vertex-count sequences, maximization, and enumeration of sections; these discrete support questions do not specify invariant probabilities. Brazitikos and Pandis (June 2026) optimize volumes of restricted cross-polytope sections, not their random face-vector distribution. The present statement combines an explicit invariant-measure law for *all* face dimensions with a shared continuous random exponent and a nonrepresentative-mean phenomenon. The binomial coefficient counts, Gaussian maximum estimates, and Crofton normalization are standard tools; they are not claimed as separately new results.

## Limitations

This is a statement about hyperplanes sampled from invariant *affine* measure conditioned on hitting the regular cross-polytope, not about uniformly oriented central hyperplanes or projections. The asymptotic result is restricted to fixed face dimension, with no assertion for ranks growing with \(n\). Different values of the latent integer may correspond to the same observed face vector. The preprint concerning combinatorial slicing could be inspected only at the level of accessible abstract and indexing information; a bibliographic priority risk therefore remains. No assertion of independent scientific verification is made.

## References

1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, first posted 14 September 2026.
2. J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419, first posted 17 December 2024, revised 22 July 2025.
3. S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163, first posted 5 June 2026.
4. Z. Kabluchko, *Expected f-vector of the Poisson zero polytope and random convex hulls in the half-sphere*, Mathematika 66 (2020), 1028–1053. (Different random-polytope model.)
