# Branching Gaussian width and near-leaf exposure in enriched tree polytopes

## Finding
For an integer \(b\ge2\), let \(T_{b,h}\) be the complete rooted \(b\)-ary tree of height \(h\ge0\) (the root has depth zero). Order vertices by ancestry, and let \(K_{b,h}\subset\mathbb R^{n_h}\) be its enriched chain polytope, where
\[
n_h=\frac{b^{h+1}-1}{b-1},\qquad
K_{b,h}=\operatorname{conv}\{x\in\{-1,0,1\}^{T_{b,h}}:\operatorname{supp}(x)\text{ is an antichain}\}.
\]
Here all widths use the standard Euclidean embedding. The complete leaf set has \(b^h\) elements. For a standard normal \(G\), put
\[
W=|G|,\quad \mu=\mathbb EW=\sqrt{2/\pi},\quad
M=\mathbb E e^W=2e^{1/2}\Phi(1),\quad
\rho=\mathbb E e^{-W}=2e^{1/2}\Phi(-1)\in(0,1).
\]
Define independent-copy recursions
\[
Y_{b,0}\overset d=W,\qquad
Y_{b,r}\overset d=\max\left(W,\sum_{i=1}^bY_{b,r-1}^{(i)}\right),\quad r\ge1,
\]
where the variables on the right are independent. Set \(c_{b,h}=b^{-h}\mathbb E Y_{b,h}\). Then \(c_{b,h}\) increases strictly to a finite positive constant \(c_b\), and for every \(h\ge0\),
\[
\boxed{\quad 0<c_b-c_{b,h}\le\frac{M}{b-1}\,b^{-h}\rho^{b^{h+1}}.\quad}
\tag{1}
\]
The constants form a strict branching hierarchy:
\[
\boxed{\quad \mu<c_{b+1}<c_b\quad(b\ge2),\qquad
0<c_b-\mu\le\frac{M}{b-1}\rho^b,\qquad
\lim_{b\to\infty}c_b=\mu.\quad}
\tag{2}
\]
Write \(\overline w(K)=\mathbb E_{U}[h_K(U)+h_K(-U)]\), where \(U\) is uniform on the unit sphere in the ambient dimension. For fixed \(b\) and \(h\to\infty\),
\[
\boxed{\quad \frac{\overline w(K_{b,h})}{\sqrt{n_h}}\longrightarrow
2\frac{b-1}{b}c_b.\quad}
\tag{3}
\]
Moreover, the *random* Euclidean directional width obeys the same limit in probability after division by \(\sqrt{n_h}\). Let \(C_{b,h}\) be the embedded \(b^h\)-dimensional leaf cube (coordinates outside leaves zero); then the exact finite-height and limiting width ratios are
\[
\boxed{\quad\frac{\overline w(K_{b,h})}{\overline w(C_{b,h})}
=\frac{c_{b,h}}{\mu}\nearrow\frac{c_b}{\mu}>1.\quad}
\tag{4}
\]
Thus internal nodes produce a nonvanishing relative mean-width gain that is strictly larger for lower branching degree.

A further geometric localization holds for Gaussian-exposed vertices. With probability one a Gaussian direction exposes a unique signed-antichain vertex. Let \(H(v)\) be the number of edges on a longest downward path from a vertex \(v\) to a leaf. For all integers \(1\le L\le h\),
\[
\boxed{\quad\Pr\{\text{some exposed support vertex }v\text{ has }H(v)\ge L\}
\le M n_h\rho^{b^L}.\quad}
\tag{5}
\]
In particular, for all sufficiently large \(h\), taking
\[
L_h=\left\lceil\log_b\left(\frac{3\log n_h}{-\log\rho}\right)\right\rceil
\]
ensures that with probability at least \(1-Mn_h^{-2}\), every selected node lies in the final \(L_h\) levels. The depth of that boundary band is \(O(\log\log n_h)\).

## Assumptions and scope
The branching factor \(b\) is an integer at least two and is fixed in the height-asymptotic assertions. Every node of an internal level has exactly \(b\) children. Gaussian coordinates are independent \(N(0,1)\); normalization to spherical directions is intrinsic to the full coordinate space \(\mathbb R^{n_h}\). The exposed support is the vertex set of the unique maximizing signed antichain, not a face-dimension statistic. All height indices and probability statements are finite-dimensional as specified; the theorem does not concern arbitrary nonregular trees, unequal edge weights, or growing \(b\) simultaneously with \(h\).

## Proof
**Support recursion.** For any deterministic direction \(g\), the signed coordinates on an antichain are optimized by choosing each sign to agree with \(g\). Consequently
\[
h_{K_{b,h}}(g)=\max_{A\text{ antichain}}\sum_{v\in A}|g_v|.
\]
Every antichain either selects the root (and no descendants) or avoids the root and combines an optimal antichain independently from each child subtree. The optimum is therefore the recursion defining \(Y_{b,h}\). All normal coordinates are continuously distributed; finite sets of distinct antichain signed sums tie with probability zero. Every maximizing antichain is a vertex exposed by the direction.

**A convergent branching series with certified remainder.** Let
\[
e_{b,r}=\mathbb E\left(W-\sum_{i=1}^{b}Y_{b,r-1}^{(i)}\right)_+,\qquad r\ge1.
\]
Since \(\max(a,s)=s+(a-s)_+\), taking expectations in the recursion yields
\[
\mathbb EY_{b,r}=b\mathbb EY_{b,r-1}+e_{b,r},\qquad
c_{b,h}=\mu+\sum_{r=1}^h b^{-r}e_{b,r}.
\tag{6}
\]
Every \(e_{b,r}>0\), because \(W\) is unbounded and independent of its finite child sum. The child sum is at least the sum \(S\) of the absolute Gaussian weights at the \(b^r\) leaves (those leaves themselves are an admissible antichain in each subtree). For every real \(z\), \(z_+\le e^z\). Independence gives
\[
0<e_{b,r}\le\mathbb E e^{W-S}
= M\rho^{b^r}.
\tag{7}
\]
Summing (7) for \(r\ge h+1\) proves (1). It also gives the upper bound in (2) by summing \(\sum_{r\ge1}b^{-r}=1/(b-1)\).

For \(b'>b\), couple the two branching recursions inductively by matching the first \(b\) children and adjoining independent extra children. Since all child values are nonnegative, \(Y_{b',r}\) stochastically dominates \(Y_{b,r}\). Thus \(e_{b',r}\le e_{b,r}\) at every positive height. In (6), both the factor \(b^{-r}\) and the nonnegative increment decrease when \(b\) increases, with strict decrease already at \(r=1\). This proves the strict inequality \(c_{b+1}<c_b\); the remaining assertions in (2) follow from (7).

**Euclidean mean width and concentration.** Write \(g=R U\) with independent \(R=\|g\|_2\) and uniform \(U\in S^{n_h-1}\), and set
\[
\eta_n=\mathbb E\|N(0,I_n)\|_2=\sqrt2\,\frac{\Gamma((n+1)/2)}{\Gamma(n/2)}.
\]
Central symmetry and homogeneity of the support function give the exact identity
\[
\overline w(K_{b,h})=\frac{2\mathbb E Y_{b,h}}{\eta_{n_h}}
=\frac{2b^h c_{b,h}}{\eta_{n_h}}.
\tag{8}
\]
Since \(\eta_{n_h}/\sqrt{n_h}\to1\) and \(b^h/n_h\to(b-1)/b\), (1) and (8) imply (3). For \(C_{b,h}\), the Gaussian support is exactly the sum of \(b^h\) independent copies of \(W\), yielding (4).

Every defining signed-antichain vector has Euclidean norm at most \(\sqrt{b^h}\), because an antichain meets each root-to-leaf path at most once. Hence \(g\mapsto h_{K_{b,h}}(g)\) is \(\sqrt{b^h}\)-Lipschitz, and the standard Gaussian Poincaré inequality gives \(\operatorname{Var}(Y_{b,h})\le b^h\). Therefore \(Y_{b,h}/b^h-c_{b,h}\to0\) in \(L^2\). Also \(R/\sqrt{n_h}\to1\) in probability. Applying Slutsky's lemma to \(2Y_{b,h}/(R\sqrt{n_h})\) proves convergence in probability of the normalized directional width. No finite experiment is used as an infinite-dimensional proof.

**Near-leaf localization.** If an optimal antichain contains a node \(v\) with remaining subtree height \(r\ge1\), replacing \(v\) by optimal antichains in each of its \(b\) child subtrees cannot improve the optimum. Necessarily its weight exceeds their summed optimum. By the same leaf domination and exponential Markov bound as in (7),
\[
\Pr\{v\text{ is selected}\}\le
\Pr\left\{W\ge\sum_{i=1}^{b}Y_{b,r-1}^{(i)}\right\}
\le M\rho^{b^r}.
\tag{9}
\]
There are fewer than \(n_h\) nodes. Summing (9) over the nodes with \(r\ge L\) proves (5). The displayed choice of \(L_h\) ensures \(b^{L_h}\ge3\log n_h/(-\log\rho)\), whence the right side of (5) is at most \(Mn_h^{-2}\).

## Verification
The attached `verify.py` uses only the Python standard library. It constructs complete rooted trees, compares the dynamic-programming support with exhaustive enumeration of every antichain for a total of 158 finite test cases, checks the Gaussian-transform constants, and reports independent Monte Carlo diagnostics for three branching factors. These diagnostics are not substituted for any arbitrary-height argument. The remainder estimate (1) is analytic and bounds the unknown infinite-depth constant without statistical assumptions. Reproduction: `python3 verify.py`.

## Relationship to prior work
Ohsugi and Tsuchiya introduced enriched chain polytopes and proved their reflexivity, unimodular triangulations, and Ehrhart identities (arXiv:1812.02097, first public 2018-12-05). The construction and signed-antichain support description are starting points, not new claims. Misanantenaina and Wagner studied rooted-tree antichain enumerators and their product-plus-root recursion (arXiv:1803.09623); that is a counting polynomial, not an expected Gaussian support nor a depth-localization result. The previously published exact inradius/circumradius theorem for enriched chain polytopes determines radii from poset height and width; it does not imply the branching constant, mean width, or random-direction localization. Gaussian concentration and classical expectation identities are standard tools and are not asserted to be new. The claimed contribution is the jointly proved quantitative branching-width law, strict branching hierarchy, and geometric exposure-localization bound.

## Limitations
The constant \(c_b\) is specified by a convergent distributional recursion and a rigorous superexponentially small truncation error; no elementary closed form is asserted. The \(O(\log\log n_h)\) exposure band is a proven upper bound, not a matching necessary threshold. The branching-monotonicity result concerns the Gaussian width *gain relative to the leaf cube*, not monotonicity of unnormalized widths across different ambient dimensions. Earlier weighted-antichain or branching-algorithm literature under alternate terminology might contain an equivalent recurrence; the accessible literature comparison found no source covering this complete geometric asymptotic and localization package. Independent mathematical validation remains outstanding.

## References
1. H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097 (first version 2018-12-05), Israel Journal of Mathematics 237 (2020), 485–500.
2. V. R. Misanantenaina and S. Wagner, *A polynomial associated with rooted trees and specific posets*, arXiv:1803.09623 (first version 2018-03-26).
3. R. Vershynin, *High-Dimensional Probability*, Gaussian width and Gaussian concentration, standard background.
