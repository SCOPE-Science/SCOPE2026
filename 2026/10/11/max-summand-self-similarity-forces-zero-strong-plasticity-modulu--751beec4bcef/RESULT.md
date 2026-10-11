# Max-summand self-similarity forces zero strong-plasticity modulus
## Finding
Let \(X\) be a real Banach space for which there is a linear isometric embedding
\[
J:\mathbb R\oplus_\infty X\longrightarrow X.
\]
Then the unit sphere \(S_X\) has zero strong-plasticity modulus at every scale \(0<\varepsilon<2\). More concretely, there is one injective non-contractive self-map \(F:S_X\to S_X\) such that no distance is decreased and, for every \(\eta>0\), some pair \(x,y\in S_X\) satisfies
\[
0<\|x-y\|<\eta,\qquad \|F(x)-F(y)\|=2.
\]
Consequently \(S_X\) is not strongly plastic.

For \(X=c\) and \(X=\ell_\infty\), coordinate prepending gives an isometric identification of \(\mathbb R\oplus_\infty X\) with \(X\). Hence both spheres have identically zero strong-plasticity modulus on \((0,2)\). Levchenko and Zavarzina prove that these same two spheres are plastic, so they give natural examples where ordinary plasticity holds while strong plasticity fails maximally at arbitrarily small scales.
## Assumptions and scope
All spaces are real. The strong-plasticity convention is the one in which a metric space is strongly plastic when every non-contractive self-map is an isometric embedding. For \(0<\varepsilon<2\), its strong-plasticity modulus is the largest guaranteed contraction depth after an arbitrary self-map expands some pair by more than \(\varepsilon\). The conclusion \(0\) means that no positive contraction depth can be guaranteed.

The structural hypothesis is only the existence of a linear isometric embedding \(J:\mathbb R\oplus_\infty X\to X\). It automatically forces \(X\) to be infinite-dimensional, hence \(S_X\) has non-isolated points. For \(c\) and \(\ell_\infty\), one may take
\[
J(a,(x_1,x_2,\ldots))=(a,x_1,x_2,\ldots).
\]
## Proof
Choose a point \(u\in S_X\) and distinct points \(u_n\in S_X\) with \(u_n\to u\). Such a sequence exists because \(X\) is infinite-dimensional. Define \(\sigma:S_X\to\{-1,1\}\) by \(\sigma(u)=1\), \(\sigma(u_n)=-1\) for every \(n\), and \(\sigma(x)=1\) at all remaining points. Put
\[
F(x)=J(\sigma(x),x),\qquad x\in S_X.
\]
Since \(\|(\sigma(x),x)\|_{\mathbb R\oplus_\infty X}=1\), the map really takes values in \(S_X\). Linearity and isometry of \(J\) give the exact distance identity
\[
\|F(x)-F(y)\|
=\max\bigl\{|\sigma(x)-\sigma(y)|,\|x-y\|\bigr\}
\ge \|x-y\|.
\]
Thus \(F\) is non-contractive; in particular it is injective. Yet
\[
\|F(u)-F(u_n)\|=2
\]
for every \(n\), while \(\|u-u_n\|\to0\). Hence \(F\) is not an isometric embedding and \(S_X\) is not strongly plastic.

For the quantitative statement, fix \(0<\varepsilon<2\). For sufficiently large \(n\),
\[
2>\|u-u_n\|+\varepsilon.
\]
The same map \(F\) therefore expands the pair \((u,u_n)\) by more than \(\varepsilon\), but it contracts no pair at all. By the definition of the strong-plasticity modulus, the modulus equals \(0\) at this \(\varepsilon\). Since \(\varepsilon\) was arbitrary, it is zero throughout \((0,2)\).
## Verification
The proof is symbolic and uses only the max norm and a linear isometric embedding. The critical identity is the displayed max formula for pairwise distances. It simultaneously verifies that \(F\) is a self-map of the sphere, is non-contractive, and has no contracted pair. The sequence \(u_n\to u\) makes the input distance tend to \(0\), whereas the corresponding output distance is exactly the sphere diameter \(2\).

For \(c\) and \(\ell_\infty\), the prepending map is checked directly: it preserves the sup norm, and in the case of \(c\) adding one initial coordinate does not change convergence of the tail. No finite experiment, numerical approximation, density argument, or unproved limiting computation is used.
## Relationship to prior work
Levchenko and Zavarzina prove that the unit spheres of \(\ell_\infty\) and \(c\) are plastic, while proving strong plasticity for Hilbert spheres. Their full text defines strong plasticity but does not state strong plasticity or its failure for the two sup-norm sequence spheres. The present argument supplies that missing separation and strengthens it to an exact zero value of the strong-plasticity modulus at every nontrivial expansion scale.

Kadets and Zavarzina introduced the quantitative strong-plasticity modulus and exhibited the Hilbert unit ball as plastic but not strongly plastic. That example does not imply the max-summand criterion above, nor does it cover the unit spheres of \(c\) or \(\ell_\infty\). The older theorem of Naimpally, Piotrowski and Wingler gives strong plasticity for totally bounded metric spaces; these infinite-dimensional spheres are not totally bounded.
## Limitations
The structural theorem assumes a linear isometric copy of \(\mathbb R\oplus_\infty X\) inside \(X\). It does not classify strong plasticity for spaces lacking such max-summand self-similarity, and in particular it makes no claim about the unit sphere of \(\ell_1\). The construction deliberately uses a discontinuous sign selector; strong plasticity places no continuity hypothesis on the non-contractive map. An equivalent observation may exist under different terminology for self-similar max-sums, which remains the main literature risk.
## References
1. M. Levchenko and O. Zavarzina, *On the plasticity of the unit spheres of \(\ell_1\), \(\ell_\infty\), \(c\), and Hilbert spaces*, arXiv:2605.06622v1, 2026.
2. V. Kadets and O. Zavarzina, *Plastic pairs of metric spaces*, arXiv:2301.06589v1; Journal of Mathematical Analysis and Applications, 2023.
3. S. A. Naimpally, Z. Piotrowski and E. J. Wingler, *Plasticity in metric spaces*, Journal of Mathematical Analysis and Applications 313 (2006), 38–48, DOI:10.1016/j.jmaa.2005.04.070.
