# A separation barrier for gap-bridging three-means of uniform mixtures

## Finding

**Theorem.** Let \(L>0\), \(G\ge L/\sqrt{2}\), \(0<p<1\), and \(q=1-p\). Define the probability law
\[
P=p\,\operatorname{Unif}[0,L]+q\,\operatorname{Unif}[L+G,2L+G].
\]
For the unconstrained quadratic three-point quantization problem
\[
V_3(P)=\inf_{|\alpha|\le3}\int\min_{a\in\alpha}(x-a)^2\,dP(x),
\]
**no optimal codebook** consists of one point in each of the three successive regions \([0,L]\), \((L,L+G)\), and \([L+G,2L+G]\). This rules out the support–gap–support configuration uniformly over the mixing probability.

In particular, for the intervals \([0,1/3]\) and \([2/3,1]\), no probability \(0<p<1\) allows an optimal three-mean set with a point in each support interval and one in the intervening gap. Consequently the **simultaneous two-mean/three-mean configuration** asked about in Open 3.17 of Barua, Fernandez, Gomez, Lopez, and Roychowdhury has a negative answer. This statement does **not** decide whether an optimal two-mean set alone can have a point in the gap.

## Assumptions and scope

The two component laws are continuous uniform distributions on closed intervals of the same positive length \(L\), separated by an empty gap of length \(G\). Both mixing masses are strictly positive. The codebook is optimized over all subsets of the real line with at most three points, and the loss is squared Euclidean distance. No extra conditions are imposed on the optimal points. The separation bound \(G\ge L/\sqrt2\) is **sufficient**, not asserted to be sharp.

## Proof

Any optimal three-point codebook has three distinct points of positive Voronoi mass, each equal to the conditional mean of its Voronoi cell. These standard properties also follow directly: an unused point could instead reduce the distortion on a positive-mass interval, and differentiating the distortion with fixed Voronoi cells places each point at the corresponding mean.

Suppose for a contradiction that an optimal codebook has \(a<z<b\), with \(a\in[0,L]\), \(z\in(L,L+G)\), and \(b\in[L+G,2L+G]\). Because \(z\) is the mean of its cell but lies strictly between the two support components, this cell must receive positive mass from **both** components. Since one-dimensional Voronoi cells are intervals, there are lengths \(u,v\in(0,L)\) such that the three cells intersect the support in, respectively,
\[
[0,L-u],\qquad [L-u,L]\cup[L+G,L+G+v],\qquad [L+G+v,2L+G].
\]
Put \(A=pu/L\) and \(B=qv/L\), the two masses of the central cell. Their conditional component means are \(L-u/2\) and \(L+G+v/2\), at separation \(G+(u+v)/2\). The standard within-group/between-group variance decomposition gives the *smallest possible error for this cell allocation* as
\[
E(u,v)=\frac{p[(L-u)^3+u^3]+q[(L-v)^3+v^3]}{12L}
+\frac{AB}{A+B}\left(G+\frac{u+v}{2}\right)^2.
\]
Thus the error of the putative optimal codebook is at least \(E(u,v)\) (indeed equal by the centroid property).

Define the two within-support splitting gains and the cross-gap penalty by
\[
S_L=\frac{pu(L-u)}4,\qquad S_R=\frac{qv(L-v)}4,\qquad
T=\frac{AB}{A+B}\left(G+\frac{u+v}{2}\right)^2.
\]
The cubic identity \((L-u)^3+u^3=L^3-3Lu(L-u)\) gives
\[
E(u,v)=\frac{L^2}{12}-S_L-S_R+T.
\]
For positive \(A,B\), \(AB/(A+B)\ge\min(A,B)/2\). Since \(u,v>0\) and \(G\ge L/\sqrt2\),
\[
T>\frac{L^2}{4}\min(A,B)\ge\min(S_L,S_R),
\]
where the second inequality follows from \(S_L\le L^2A/4\) and \(S_R\le L^2B/4\). Consequently,
\[
E(u,v)>\frac{L^2}{12}-\max(S_L,S_R)
\ge\frac{L^2}{12}-\frac{L^2}{16}\max(p,q).
\]
But the explicit codebook placing two equal-spaced midpoint quantizers on the component with larger mass and one midpoint quantizer on the other has distortion **at most**
\[
\min\left\{\frac{pL^2}{48}+\frac{qL^2}{12},
\frac{pL^2}{12}+\frac{qL^2}{48}\right\}
=\frac{L^2}{12}-\frac{L^2}{16}\max(p,q).
\]
(The actual nearest-center distortion cannot exceed the cost of assigning each entire support to its designated centers.) Hence the proposed support–gap–support codebook cannot minimize distortion, a contradiction. For \([0,1/3]\cup[2/3,1]\) the gap and component lengths are equal, so the theorem applies. \(\square\)

## Verification

Run `python3 verify.py` from the directory containing this document. The standard-library script uses `fractions.Fraction` to check the exact cell-cost identity and the strict competitor inequality in 2,187 rational parameter cases for unit-length components and gaps \(3/4\), \(1\), and \(2\). It also integrates a small-gap example independently.

For \(L=1\), \(G=1/10\), and \(p=q=1/2\), the centroidal codebook \(\{7/20,21/20,7/4\}\) has exact distortion \(257/6000\), below the componentwise \((2,1)\) allocation cost \(5/96\). This is **not** a claim that the displayed small-gap codebook is globally optimal; it illustrates why a positive separation condition is mathematically relevant. The analytic argument above, rather than the finite checks, proves the theorem for every allowed real parameter.

## Relationship to prior work

Barua, Fernandez, Gomez, Lopez, and Roychowdhury study quadratic quantization for mixtures of two uniform laws on connected or disconnected intervals. Their 2025 article (arXiv preprint first posted 23 March 2022) establishes several exact codebooks at specified mixing weights and states Open 3.17 and Conjecture 3.19 for the two equal-length intervals with an equally long gap. The theorem here excludes the three-mean support–gap–support geometry for **every** positive mixing pair, and therefore resolves the conjunction in that open question without asserting a classification of all three-mean codebooks. The source's general eventual-separation conjecture concerns sufficiently large numbers of quantizers, whereas this theorem concerns precisely three points.

## Limitations

Only the three-point support–gap–support configuration is excluded; a gap point accompanied by two other points in the same support, and the separate two-point problem, are not covered. The bound \(G\ge L/\sqrt2\) is a sufficient barrier and is not claimed optimal. The code does not establish any infinite-domain assertion by enumeration. No independent external review is claimed.

## References

1. A. Barua, G. Fernandez, A. Gomez, O. Lopez and M. K. Roychowdhury, *Quantization for the mixtures of uniform distributions on connected and disconnected line segments*, arXiv:2203.12664 (first submission 23 March 2022), https://arxiv.org/abs/2203.12664.
2. Same authors, *Arabian Journal of Mathematics* (2025), DOI:10.1007/s40065-025-00557-5, especially Open 3.17 and Conjecture 3.19, https://link.springer.com/article/10.1007/s40065-025-00557-5.
