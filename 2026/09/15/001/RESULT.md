# Entropy gap rigidity at the round cylinder in dimension 3

## Context

The admitted target asks whether the round cylinder $S^{n-1}\times\mathbb{R}$ is rigid among complete noncompact shrinking gradient Ricci solitons with bounded curvature under closeness of Perelman's $\nu$-entropy: is there $\varepsilon(n)>0$ such that $|\nu(M)-\nu_{\mathrm{cyl}}(n)|<\varepsilon$ forces isometry to the cylinder? For general $n\geq 4$ no shrinker classification exists and the question remains open. In dimension $3$ the classification of complete shrinkers closes the problem.

## Definitions

A shrinking gradient Ricci soliton is normalized by $\mathrm{Ric}+\nabla^2 f=g/2$ and $R+|\nabla f|^2=f$, with $p$ a minimum point of $f$. Perelman's $\nu$-entropy $\nu(M)=\inf_{\tau,u}\mathcal{W}(M,\tau,u)$ is the infimum of the $\mathcal{W}$-functional over admissible normalized test pairs; on a shrinker the infimum is attained at the shrinker potential (Yokota), so $\mu=\nu$. A shrinker quotient $M=\widetilde{M}/\Gamma$ means $\Gamma$ acts by isometries preserving the pair $(g,f)$. The round 3D cylinder is $S^2\times\mathbb{R}$ with $f=f_{S^2}+z^2/4$.

## Result

Let $(M^3,g,f,p)$ be a complete noncompact shrinking gradient Ricci soliton with bounded curvature under the above normalization, and let $\nu_{\mathrm{cyl}}(3)=\log 2-1$ be the $\nu$-entropy of the standard round cylinder $S^2\times\mathbb{R}$. With explicit constant $\varepsilon_3=0.2$,
$$|\nu(M)-\nu_{\mathrm{cyl}}(3)|<0.2 \Longrightarrow (M,g,f)\ \text{is isometric to}\ S^2\times\mathbb{R}.$$
The bounded-curvature hypothesis is retained from the target but is not needed in $n=3$.

## Proof and evidence

Step 1 (3D list): by Hamilton-Ivey-Perelman, Ni-Wallach, Petersen-Wylie, and Cao-Chen-Zhu, every complete 3D shrinker is a finite quotient of $S^3$, $\mathbb{R}^3$, or $S^2\times\mathbb{R}$. Noncompactness leaves quotients of $\mathbb{R}^3$ and $S^2\times\mathbb{R}$ by shrinker automorphisms. Deck transformations preserving normalized $f$ preserve its minimum set: a point for $\mathbb{R}^3$ (so $\Gamma\subset O(3)$) and the central $2$-sphere for $S^2\times\mathbb{R}$ (so $\Gamma\subset O(3)\times\mathbb{Z}_2$). A freely, properly discontinuously acting subgroup of a compact group is finite, so $|\Gamma|<\infty$; $z$-translations do not preserve $f$ and their quotients admit no shrinker structure.

Step 2 (quotient shift): for a finite Riemannian covering of shrinkers, lifting an admissible pair $(u,\tau)$ as $\tilde u=(u\circ\pi)/\sqrt{d}$ gives $\mathcal{W}(\widetilde M,\tau,\tilde u)=\mathcal{W}(M,\tau,u)+\log d$; descent of the minimizer yields $\nu(M)=\nu(\widetilde M)-\log|\Gamma|$. Quotients have strictly smaller entropy, consistent with $\nu(\mathbb{RP}^n)=\nu(S^n)-\log 2$.

Step 3 (values and gap): $\nu(\mathbb{R}^3)=0$ and $\nu_{\mathrm{cyl}}(3)=\log(8\pi/4\pi)-1=\log 2-1\approx-0.3068528194$. Hence $\mathbb{R}^3/\Gamma$ has $\nu=-\log|\Gamma|$ and $(S^2\times\mathbb{R})/\Gamma$ has $\nu=\log2-1-\log|\Gamma|$. Distances from $\nu_{\mathrm{cyl}}(3)$: $\mathbb{R}^3$ at $1-\log2\approx0.30685$; nontrivial Gaussian quotients at $\geq 2\log2-1\approx0.38629$; nontrivial cylinder quotients at $\geq\log2\approx0.69315$. All exceed $0.2$ with margin at least $0.106$, verified at 80-digit precision. Thus entropy-$0.2$-closeness forces $|\Gamma|=1$ on the cylinder branch and excludes the Gaussian branch.

## Limitations

The theorem covers only $n=3$; the general-$n$ target remains open. For $n\geq 4$ there is no classification, product entropy gaps shrink with $n$, and non-product families (Feldman-Ilmanen-Knopf, Appleton, Bamler-Cifarelli-Conlon-Deruelle) are invisible to this method. The quotient identity relies on minimizer attainment on shrinkers and the $f$-preserving finiteness argument; orbifold/conifold extensions are not claimed. Published cylinder rigidity under pointed-Gromov-Hausdorff closeness (Li-Wang; Li-Zhang) neither implies nor is implied by this entropy gap, since entropy closeness does not imply GH-closeness. Gaussian local entropy gaps (Chan-Zhang) concern a different model.

## Reproducibility

Run `python3 artifacts/entropy_gaps.py` (requires `mpmath`): checks $\nu_{\mathrm{cyl}}(3)=\log2-1$, all three competitor distances against $\varepsilon_3=0.2$, and prints the general-$n$ product table. Audit reproduction confirmed ALL CHECKS PASSED.

## References

Perelman entropy formula; Ni-Wallach 3D classification; Cao-Chen-Zhu 3D classification; Petersen-Wylie shrinker structure; Cao-Zhou potential and volume estimates; Yokota minimizer attainment; Li-Wang cylinder GH-rigidity; Li-Zhang generalized-cylinder GH-rigidity; Kotschwar-Wang asymptotically conical rigidity.
