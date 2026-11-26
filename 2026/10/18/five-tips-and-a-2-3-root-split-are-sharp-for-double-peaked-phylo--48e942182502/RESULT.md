# A singleton root child precludes two strict rarefaction-variance peaks at five tips

## Finding

Let a rooted fully bifurcating ultrametric tree have five distinctly labelled tips, strictly positive edges and unit root-to-tip distance. For uniform sampling of exactly \(k\) tips without replacement, write \(V_k\) for the population variance of the length of the union of sampled root-to-tip paths (rooted Faith PD). **If the root split is \(1+4\), then \(V_2<V_3\) for every admissible choice of lengths, for both possible four-tip descendant shapes.** In particular such a tree cannot have strict interior peaks at both \(k=2\) and \(k=4\). The other possible split, \(2+3\), is therefore the only shape that can realize the previously recorded five-tip onset of bimodality.

## Proof

An interior peak is strict on both sides, with \(k\) between 2 and 4. Two such peaks cannot be adjacent, so at five tips they must be at 2 and 4. The two binary shapes of the four-tip root child are a ladder \((1,(1,(1,1)))\) and a pair of cherries \(((1,1),(1,1))\).

For an edge of length \(\ell_e\), let \(D_e\) be its descendant-tip set. Let \(f_k(r)=\binom{5-r}{k}/\binom5k\), with a zero numerator if there are fewer than \(k\) tips available. Writing rooted PD as total tree length minus the sum of lengths of omitted edges gives
\[
V_k=\sum_{e,f}\ell_e\ell_f\bigl[f_k(|D_e\cup D_f|)-f_k(|D_e|)f_k(|D_f|)\bigr].
\]
Indeed, the covariance of two omission indicators uses the omission probability of their union, less the product of their separate omission probabilities.

Label the singleton root child 0 and the four-tip descendants 1–4. In the ladder, put ages \(a>b>c>0\) on the successive internal vertices below the root, which has age 1. In the pair of cherries put age \(a<1\) on the four-tip crown and ages \(0<b,c<a\) on its two cherries. The age of each tip is zero. The descendant sets and lengths for the two evaluations are:

| Shape | Descendant set : edge length |
| --- | --- |
| Ladder | \(0:1,\ 1234:1-a,\ 1:a,\ 234:a-b,\ 2:b,\ 34:b-c,\ 3:c,\ 4:c\) |
| Two cherries | \(0:1,\ 1234:1-a,\ 12:a-b,\ 34:a-c,\ 1:b,\ 2:b,\ 3:c,\ 4:c\) |

In the table a string of tip labels denotes their set. Inserting the ladder row into the covariance sum with \(x=1-a,\ y=a-b,\ z=b-c\) gives
\[
100(V_2-V_3)=-12xy-8xz-15y^2-18yz-12z^2.
\]
Inserting the two-cherry row with \(x=1-a,\ y=a-b,\ z=a-c\) gives
\[
100(V_2-V_3)=-4\bigl[2x(y+z)+3y^2-4yz+3z^2\bigr].
\]
All three lengths \(x,y,z\) are positive in either row. In the two-cherry case \(3y^2-4yz+3z^2=(y-z)^2+2(y^2-yz+z^2)>0\). Both expressions are strictly negative throughout their domains, excluding a strict peak at 2 and hence excluding two strict peaks. Scaling to any positive common tree height multiplies these differences by its square.

## Relationship to the complete five-tip classification

Nipperess and Matsen [1] give the general variance formula for rooted PD rarefaction. Separately, *Sharp five-taxon onset and a phase region for bimodal ultrametric phylogenetic-rarefaction variance* [2] states the five-tip onset and the two exact strict phase inequalities on the \(2+3\) shape. Its root-depth parameters \((\alpha,\beta,\gamma)\) are \((1-a,1-b,1-c)\) when \(a,b,c\) denote the corresponding vertex ages measured upward from the tips, and its two inequalities become \(100(V_2-V_3)>0\) and \(100(V_4-V_3)>0\) in those age coordinates. That record explicitly does not classify other five-tip shapes. The contribution asserted here is the uniform \(1+4\) exclusion; the phase inequalities, existence at five tips and elementary lower bound on the tip count are not presented as distinct contributions. Combining the exclusion with the phase criterion gives the classification across all fully bifurcating five-tip shapes.

## Reproducibility and scope

The coefficient identities above can be checked either with the displayed covariance sum or by enumerating the ten equally likely subsets at each of \(k=2,3\) from the displayed edge table. The accompanying `verify.py` checks these two identities by exact symbolic subset enumeration; its other checks give the \(2+3\) formulas and an additional positive-edge witness. The result does not concern independently thinned survivor sets, unequal sampling weights, unrooted PD, or higher-order shape classification.

## References

1. D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, DOI [10.1111/2041-210X.12042](https://doi.org/10.1111/2041-210X.12042), arXiv:1208.6552.
2. [*Sharp five-taxon onset and a phase region for bimodal ultrametric phylogenetic-rarefaction variance*](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-sharp-five-taxon-onset-and-a-phase-region-for-bimodal-ultrametri--784aa021ee67/RESULT.md), Resultary record `784aa021ee67`.
