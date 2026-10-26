# Sharp bounded-error amplification and direction switching on anisotropic rook graphs

## Finding

Fix integers \(2\le a\le b\), and equip the rook graph \(K_a\mathbin{\square}K_b\) with conductance \(c>0\) on every edge changing its first coordinate and conductance \(d>0\) on every edge changing its second coordinate. Let \(P\) be the Euclidean orthogonal projector onto the gradients of vertex potentials when each oriented edge coordinate is normalized by the square root of its conductance. With the ordinary coordinate maximum norm on this edge space, set
\[
\kappa=\frac{\sqrt{cd}}{ac+bd}.
\]
Every output edge changing the first coordinate has absolute row sum
\[
R_A=\frac{2(a-1)}a+2(b-1)\kappa,
\]
while every output edge changing the second coordinate has absolute row sum
\[
R_B=\frac{2(b-1)}b+2(a-1)\kappa.
\]
Consequently the sharp amplification is \(\|P\|_{\infty\to\infty}=\max\{R_A,R_B\}\), with equality attained by a sign choice of bounded input edge data.

For every fixed \(a,b\), the conductance ratio \(c/d=b/a\) is the **unique** maximizing positive ratio, and
\[
\boxed{\ \sup_{c,d>0}\|P\|_{\infty\to\infty}
=\frac{2(a-1)}a+\frac{b-1}{\sqrt{ab}}\ }.
\]
The entire range as conductances vary is
\[
\left(\frac{2(b-1)}b,\ \frac{2(a-1)}a+\frac{b-1}{\sqrt{ab}}\right].
\]
The lower endpoint is approached by ratios tending to zero or infinity and is not attained.

When \(a<b\), define
\[
r_\pm=\left[\frac b2\left(1\pm\sqrt{1-\frac4{ab}}\right)\right]^2.
\]
These are two distinct positive thresholds with \(r_-<b/a<r_+\). For \(r=c/d\) strictly between the thresholds, **first-coordinate edges** give the sharp norm; for \(r<r_-\) or \(r>r_+\), **second-coordinate edges** do. At either threshold both edge directions tie. When \(a=b\), both directions tie for every positive conductance ratio.

In particular, at \(a=2\) and \(b\to\infty\) the optimally weighted norm is
\[
1+\frac{b-1}{\sqrt{2b}}\sim\sqrt{\frac b2},
\]
even though the orthogonal projector always has Hilbert-space norm one. Equal conductances, by contrast, always give \(\|P\|_{\infty\to\infty}<4\) in this family.

## Assumptions and scope

Vertices are pairs \((u,v)\in\{1,\ldots,a\}\times\{1,\ldots,b\}\). An edge is present precisely if one coordinate agrees and the other differs; the first-coordinate edges lie in copies of \(K_a\), and the second-coordinate edges lie in copies of \(K_b\). Choose an arbitrary orientation of each edge. Let \(M\) be the edge-by-vertex matrix whose row at edge \(xy\) is \(\sqrt{w_{xy}}(e_x-e_y)^\top\), where \(w_{xy}=c\) or \(d\) according to direction. Then \(L=M^\top M\) is the weighted vertex Laplacian and
\[
P=M L^\dagger M^\top
\]
is the orthogonal projector on the edge-gradient image. Both real and complex scalar edge inputs obey the stated induced \(\ell^\infty\) norm, since the matrix is real and its norm is the maximum absolute row sum. The theorem concerns the Euclidean projection in conductance-normalized edge coordinates, *not* a projection in the unnormalized physical-current maximum norm.

## Proof

**1. Invert the vertex Laplacian.** Write \(J_s\) for the orthogonal projector onto constants in \(\mathbb R^s\), and \(H_s=I-J_s\). On vertex functions the Laplacian has three nonzero spectral sectors, namely \(H_a\otimes J_b\), \(J_a\otimes H_b\), and \(H_a\otimes H_b\), with eigenvalues \(ac\), \(bd\), and \(ac+bd\), respectively. Therefore its Moore–Penrose inverse is exactly
\[
G=L^\dagger=
\frac{H_a\otimes J_b}{ac}
+\frac{J_a\otimes H_b}{bd}
+\frac{H_a\otimes H_b}{ac+bd}.
\]
For vertices \((u,v)\) and \((s,w)\), its scalar kernel is
\[
G((u,v),(s,w))=
\frac{\delta_{us}-1/a}{abc}
+\frac{\delta_{vw}-1/b}{abd}
+\frac{(\delta_{us}-1/a)(\delta_{vw}-1/b)}{ac+bd}.
\]
The constant sector is omitted because all edge differences annihilate it.

**2. Count absolute masses within one edge direction.** Fix an output first-coordinate edge \(((u,v),(u',v))\), and an input first-coordinate edge \(((s,w),(s',w))\). Applying both signed edge differences to \(G\) gives the matrix entry
\[
P_{AA}=D_{uu';ss'}\left[\frac1{ab}+
\frac{c(\delta_{vw}-1/b)}{ac+bd}\right],
\quad
D_{uu';ss'}=\delta_{us}-\delta_{us'}-\delta_{u's}+\delta_{u's'}.
\]
The bracket is strictly positive for every \(v,w\): if \(w=v\) it equals \(1/(ab)+c(b-1)/(b(ac+bd))\), and otherwise it equals \(d/[a(ac+bd)]\). Summing these brackets over all \(b\) values of \(w\) gives exactly \(1/a\). For any fixed edge of \(K_a\), the sum of \(|D_{uu';ss'}|\) over all its unordered edges \(\{s,s'\}\) is \(2+2(a-2)=2(a-1)\): one identical edge contributes \(2\), the \(2(a-2)\) other incident edges contribute \(1\), and disjoint edges contribute zero. Hence the total same-direction absolute row mass is \(2(a-1)/a\), independently of both conductances.

**3. Count transverse masses.** For an input second-coordinate edge \(((s,w),(s,w'))\), the two edge differences annihilate the first two sectors of \(G\). The remaining matrix entry has absolute value
\[
|P_{AB}|=\frac{\sqrt{cd}}{ac+bd}
|\delta_{us}-\delta_{u's}|\,|\delta_{vw}-\delta_{vw'}|.
\]
It is nonzero exactly if \(s\in\{u,u'\}\) and the input second-coordinate edge is incident to \(v\). There are precisely \(2(b-1)\) such edges. The transverse absolute row mass is therefore \(2(b-1)\kappa\). This proves \(R_A\). Interchanging the two vertex coordinates and conductances proves \(R_B\). Each row norm is attained by assigning the input coordinate signs to match that row's matrix-entry signs, proving the induced-norm identity without any positivity assumption on the input data.

**4. Optimize conductances and classify the worst direction.** Only the ratio \(r=c/d>0\) matters, and
\[
\kappa(r)=\frac{\sqrt r}{ar+b}\le\frac1{2\sqrt{ab}},
\]
with equality only when \(ar=b\), by strict arithmetic–geometric mean inequality. Both \(R_A\) and \(R_B\) increase strictly with \(\kappa\), so their maximum is uniquely maximized at \(r=b/a\). Moreover,
\[
R_A-R_B=2(b-a)\left(\kappa-\frac1{ab}\right).
\]
For \(a<b\), the maximal \(\kappa=1/(2\sqrt{ab})\) exceeds \(1/(ab)\) because \(ab>4\). Thus the first-coordinate row wins at the conductance optimum. Solving \(\kappa=1/(ab)\) with \(x=\sqrt r\) yields the quadratic \(ax^2-abx+b=0\), whose two distinct positive solutions square to \(r_-\) and \(r_+\). Outside the interval, \(\kappa<1/(ab)\), reversing the worst edge direction. If \(a=b\), the row sums are always equal. Finally \(\kappa\) takes every value in \((0,1/(2\sqrt{ab})]\); the range assertion follows from strict monotonicity of \(\max\{R_A,R_B\}\) in \(\kappa\). The contrasting large-aspect-ratio growth follows by substituting \(a=2\) and taking \(b\to\infty\). For \(c=d\), \(\kappa=1/(a+b)\); both row sums are strictly below four.

## Verification

Run `python3 verify.py` using Python's standard library. The checker constructs each weighted graph independently, inverts its anchored integer/rational Laplacian using exact fractions, reconstructs every projection matrix entry, checks both directional absolute row masses, checks symmetry and rank trace, and checks idempotence on the smallest cases. It tests 55 positive integral conductance configurations and asserts 39,265 exact rational identities. These finite tests are not a proof of the arbitrary-parameter theorem, which follows from the preceding spectral decomposition and counting argument.

## Relationship to prior work

The graph Hodge-decomposition framework and interpretation as least-squares gradient fitting are classical; see Jiang–Lim–Yao–Ye, 2008, especially Theorem 5.1. Kassel–Wu, 2013, identify edge transfer-current entries as differences of Green functions in their Section 2. Those identities motivate the object and supply general notation, but neither examined article states the present exact weighted-rook absolute-row-mass formulas, the two direction-switching thresholds, or the unique maximizing ratio. Known exact results for complete multipartite graph edge projections and for anisotropically weighted Boolean-cube edge projections are not direct coverings: except for the four-cycle, their edge graphs differ from the rook graphs here, and their formulas do not imply the two-parameter weighted-rook classification without additional arguments.

## Limitations

The result assumes exactly two complete-graph factors and conductances constant *within* each coordinate direction; it does not cover arbitrary edge-by-edge weights, larger Cartesian products, or non-Euclidean metric projections. Only absolute-coordinate edge perturbations are controlled; the amplification value does not measure mean-square noise. An equivalent earlier calculation could exist in transfer-current or weighted Cartesian-product literature under different terminology; historical priority has not been independently established.

## References

1. X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, *Statistical Ranking and Combinatorial Hodge Theory*, arXiv:0811.1067, first submitted 2008-11-07, especially Sections 4–5. https://arxiv.org/abs/0811.1067
2. A. Kassel and W. Wu, *Transfer Current and Pattern Fields in Spanning Trees*, arXiv:1312.2946, first submitted 2013-12-10, especially Section 2. https://arxiv.org/abs/1312.2946
