# Sharp \(m+1\) polyhedral generators for neutral–expanding toral products

## Finding
For every integer \(m\ge2\), let \(T_m\) be the Haar-preserving endomorphism
\[
 T_m:\mathbb T^2\longrightarrow\mathbb T^2,\qquad
 T_m(\theta,y)=(\theta,my\bmod1),
\]
where \(\mathbb T=\mathbb R/\mathbb Z\). Write \(g(T_m)\) for the least cardinality of a finite Borel one-sided generating partition modulo Haar measure, and \(g_{\mathrm{poly}}(T_m)\) for the least cardinality when every boundary is piecewise affine. Then
\[
\boxed{g(T_m)=g_{\mathrm{poly}}(T_m)=m+1.}
\]
The construction is fully explicit and recovers both coordinates from almost every forward itinerary. In particular, the neutral eigenvalue \(1\) does not prevent finite generators with piecewise smooth boundaries, despite preventing the map from being ergodic; the sharp cardinality is one above its uniform expanding degree.

## Assumptions and scope
Use the standard half-open representatives \((\theta,y)\in[0,1)^2\), identifying opposite sides to form the torus; all statements about generating partitions are modulo normalized Haar probability measure \(\lambda\). A partition \(\mathcal P\) is one-sided generating if the forward name \((\mathcal P(T_m^n z))_{n\ge0}\) separates a measurable full-measure subset of \(\mathbb T^2\). Its boundary is piecewise affine if the boundary in the torus is covered by finitely many affine line segments in local charts. We make no Markov, independent-translate, or generating-for-every-point assertion.

Set \(m\ge2\) and define the following \(m+1\) cells using canonical representatives:
\[
\begin{aligned}
P_a&=\{(\theta,y):0\le y<\theta/m\},\\
P_b&=\{(\theta,y):\theta/m\le y<1/m\},\\
P_j&=\{(\theta,y):j/m\le y<(j+1)/m\},\quad 1\le j\le m-1.
\end{aligned}
\]
The cells are disjoint and cover the torus, with harmless half-open edge conventions. Their boundaries lie on finitely many horizontal, diagonal, and seam segments, hence are piecewise affine and have zero Haar measure.

## Proof
**Upper bound and complete recovery.** Merge symbols \(a\) and \(b\) into a symbol \(0\), retaining symbol \(j\) for each \(1\le j\le m-1\). The merged forward itinerary is exactly the greedy base-\(m\) digit stream of the second coordinate. Indeed, if \(y_n=m^ny\bmod1\), the digit is \(d_n=\lfloor my_n\rfloor\), so every point's second coordinate is reconstructed as
\[
 y=\sum_{n=0}^{\infty}\frac{d_n}{m^{n+1}}.
\]
The canonical greedy rule fixes even base-expansion endpoint ambiguities. The unmerged letter \(a\) occurs precisely when \(y_n<\theta/m\).

There is a Lebesgue-full, forward invariant subset \(Y\subset[0,1)\) for which the orbit \((m^ny\bmod1)_{n\ge0}\) is uniformly distributed in \([0,1)\). One direct construction takes the common full-measure set of points obeying Birkhoff's theorem for the countably many indicators of rational intervals \([0,r)\), and then squeezes every real threshold between rationals. Ergodicity of \(y\mapsto my\bmod1\) follows, for example, from its independent base-\(m\) digits. Consequently, for every \(y\in Y\) and **every** \(\theta\in[0,1)\), the frequency of \(a\) is
\[
 \lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}
  \mathbf1_{\{\mathcal P(T_m^n(\theta,y))=a\}}
   =\frac{\theta}{m}.
\]
Thus the original, unsplit-neutral coordinate is exactly \(\theta=m\lim_N N^{-1}\#\{0\le n<N:\text{letter }a\}\). Both coordinates are determined on \([0,1)\times Y\), a full Haar-measure set; hence this piecewise affine partition generates one-sidedly. Therefore \(g_{\mathrm{poly}}(T_m)\le m+1\).

**Lower bound for arbitrary measurable partitions.** The Haar entropy is \(h_\lambda(T_m)=\log m\): the multiplier coordinate is the uniform one-sided \(m\)-symbol Bernoulli shift via its digits, the fixed \(\theta\) factor has entropy \(0\), and entropy is additive under direct products. Suppose a one-sided generating Borel partition has \(s\) cells. The generator theorem gives \(h_\lambda(T_m)=h_\lambda(T_m,\mathcal P)\le\log s\), so \(s\ge m\).

If \(s=m\), let \(H_n\) be the Shannon entropy of the stationary length-\(n\) name block. The alphabet bound gives \(H_n\le n\log m\), while the subadditivity formula
\[
 h_\lambda(T_m,\mathcal P)=\inf_{n\ge1}\frac{H_n}{n}=\log m
\]
forces equality \(H_n=n\log m\) for every \(n\ge1\). Equality in the finite-alphabet entropy bound means every length-\(n\) word has probability \(m^{-n}\). Thus the entire stationary name process is i.i.d. uniform, and its one-sided shift is ergodic. Because \(\mathcal P\) is generating, its forward-name map is a measure-theoretic isomorphism, so \(T_m\) would be ergodic as well. This is impossible: the nonconstant indicator \(\mathbf1_{\{\theta<1/2\}}\) is \(T_m\)-invariant. Hence \(s\ne m\), and \(s\ge m+1\). Combined with the construction, both minima are exactly \(m+1\).

## Verification
The interval split is exhaustive: for each \(\theta\), the lengths of \(P_a,P_b\) in the zero-digit strip sum to \(1/m\), and the remaining \(m-1\) strips have width \(1/m\). In particular, every cell has positive Haar measure: \(\lambda(P_a)=\lambda(P_b)=1/(2m)\), and \(\lambda(P_j)=1/m\) for \(1\le j<m\). The only dynamical inputs are base-\(m\) digit reconstruction, uniform distribution on one fixed full-measure set, and the entropy-rate equality argument. The equality argument uses **all** block lengths, not a finite observation or a numerical test. To reproduce the proof for any integer \(m\ge2\), write down the displayed strips, merge their letters to verify the digit shift, count the asymptotic \(a\)-frequency on uniformly distributed orbits, and apply the maximal finite-alphabet entropy criterion.

## Relationship to prior work
Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators* (arXiv:2610.01642v1, first public 2026-10-01), defines smooth finite generators using piecewise smooth boundaries. Its Theorem 1 proves a boundary-regularity obstruction **when an eigenvalue has modulus strictly below \(1\)**; the present neutral–expanding diagonal matrices have spectrum \(\{1,m\}\) and lie outside that theorem's hypothesis. Although the paper's abstract uses broader nonexpanding wording, the actual theorem and its proof invoke strict contraction. The present result identifies a sharp, constructive, opposite-side phenomenon: an explicit minimal smooth generator with one symbol beyond the expanding degree.

Hughes and de Jong, *Smoothness of Markov Partitions for Expanding Toral Endomorphisms* (arXiv:2604.00257v1), investigate a stronger Markov-partition condition **with all eigenvalues expanding** and do not give the minimal ordinary generator for a neutral–expanding product. Hoffman and Rudolph's Bernoulli endomorphism results concern isomorphism to a uniform one-sided Bernoulli shift, which is impossible for this nonergodic product. The general finite-generator entropy theorem yields the cardinality obstruction, but by itself supplies neither these affine cells nor the coordinate-recovery mechanism.

## Limitations
The statement is for the diagonal family \(\operatorname{diag}(1,m)\), \(m\ge2\), with Haar measure and almost-everywhere one-sided generation. It does not classify neutral Jordan blocks, arbitrary non-diagonal integer matrices, other invariant measures, or generators with additional Markov/independence requirements. It does not assert the optimality of any geometric complexity beyond the number of atoms. An equivalent specialized construction elsewhere under a different coding vocabulary remains a residual literature risk; searches alone cannot eliminate that risk.

## References
1. Christophe Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators*, arXiv:2610.01642v1 (first public 2026-10-01), https://arxiv.org/abs/2610.01642 .
2. Chayce Hughes and Huub de Jong, *Smoothness of Markov Partitions for Expanding Toral Endomorphisms*, arXiv:2604.00257v1 (2026), https://arxiv.org/abs/2604.00257 .
3. Christopher Hoffman and Daniel Rudolph, *Uniform endomorphisms which are isomorphic to a Bernoulli shift*, *Annals of Mathematics* 156 (2002), 79–101, https://annals.math.princeton.edu/2002/156-1/p02 .
4. Kolmogorov–Sinai generator theorem and subadditive block-entropy identity (standard finite-alphabet entropy theory).
