# Sharp \(\ell_1\) cycle-space projection constants for circular ladders

## Finding
Let \(G_n=C_n\square K_2\) be the unweighted \(n\)-gonal prism graph, where \(n\) is any integer at least \(10\). Give its \(3n\) edges arbitrary reference orientations, let \(\partial:\mathbb R^{E(G_n)}\to\mathbb R^{V(G_n)}\) be the signed incidence operator, and give the edge space the real coordinate \(\ell_1\) norm. Let \(Z_n=\ker\partial\) be its circulation (real cycle) subspace. Then the unrestricted **relative minimal projection norm** is
\[
\boxed{\lambda(Z_n,\ell_1(E(G_n)))
:=\min_{P^2=P,\ \operatorname{ran}P=Z_n}\|P\|_{1\to1}
=\frac{12}{5}-\frac{16}{5n}.}
\]
An explicit reflection-, rotation-, and layer-swap-invariant minimizer is constructed below. In particular, these exact constants increase strictly toward \(12/5\) as \(n\to\infty\). No assertion about the optimal constant for \(3\le n\le9\) is made.

## Assumptions and scope
All scalars are real and all graph edges are unweighted, with unit coordinate weight in \(\ell_1(E)\). The two copies of \(C_n\) have horizontal edges \(h_i^+\) and \(h_i^-\), both oriented from cyclic index \(i\) to \(i+1\). The matching rung \(v_i\) is oriented from the upper to the lower layer. Indices belong to \(\mathbb Z/n\mathbb Z\). The cycle vectors
\[
s_i=h_i^+-h_i^-+v_{i+1}-v_i,
\qquad t=\sum_i(h_i^++h_i^-)
\]
form a basis of \(Z_n\): they are \(n+1\) independent circulations, and \(\dim Z_n=3n-2n+1=n+1\). Orientation changes induce coordinate-sign isometries, so the minimum is orientation-independent. The invariant is the projection norm **onto the cycle subspace of the edge \(\ell_1\) space**, not an asserted equality with the absolute projection constant of the dual Lipschitz space.

## Proof
**1. Reduction to invariant projections.** Rotations and reflections of the rim, together with interchange of the two layers, act on the oriented edge space by signed permutations preserving \(\ell_1\) and \(Z_n\). Averaging any projection onto \(Z_n\) over this finite isometry group gives another projection onto \(Z_n\) with no larger norm. Hence a minimum exists among projections commuting with these actions.

For such a projection \(P\), rotations, layer interchange and \(P(t)=t\) force the following forms, with real cyclic coefficient arrays \(a_i,b_i\):
\[
\begin{aligned}
P(h_j^+)&=\frac{t}{2n}+\sum_i a_i s_{i+j},\\
P(h_j^-)&=\frac{t}{2n}-\sum_i a_i s_{i+j},\\
P(v_j)&=\sum_i b_i s_{i+j}.
\end{aligned}
\]
The reflection \(i\mapsto-i\) fixes the rung \(v_0\) but sends \(s_i\) to \(-s_{-i-1}\), so \(b_i=-b_{-i-1}\). Since \(P(s_0)=s_0\), the coefficient identity is
\[
2a_i+b_{i-1}-b_i=\mathbf1_{i=0}.
\]
Writing \(d_i=b_i-b_{i-1}\), it follows that \(2a_i=\mathbf1_{i=0}+d_i\) and \(d_i=d_{-i}\). Conversely, every array \(b\) obeying \(b_i=-b_{-i-1}\), together with this definition of \(a\), defines by these column formulas a projection onto \(Z_n\): all images lie in \(Z_n\), the formulas fix every \(s_i\), and they fix \(t\).

**2. Exact column norms.** The \(\ell_1\)-operator norm of a matrix is its largest absolute column sum. All horizontal columns have a common sum \(H\), and all vertical columns have a common sum \(V\). Expanding the square-cycle basis gives
\[
\begin{aligned}
H&=2\sum_i\max\{|a_i|,1/(2n)\}
   +\sum_i|a_i-a_{i-1}|,\\
V&=2\sum_i|b_i|+\sum_i|b_i-b_{i-1}|,\\
\|P\|_{1\to1}&=\max\{H,V\}.
\end{aligned}
\]
These identities include the contributions of both horizontal rims and the vertical matching; no factor of two is suppressed.

**3. Universal sharp lower bound.** Assume \(n\ge10\), so the ten cyclic indices \(0,1,2,3,4,-1,-2,-3,-4,-5\) are distinct. Define
\[
u=-b_0,\qquad v=-b_1,\qquad w=-b_2,\qquad \Delta=b_4-b_3.
\]
For every real \(z\), \(\max(|z|,1/n)\ge z\), \(\max(|z|,1/n)\ge1/n\), and hence \(\max(|z|,1/n)\ge(z+1/n)/2\). Apply the first inequality at cyclic indices \(0,\pm1\), the averaged inequality at \(\pm2\), and the second at all remaining indices. Since \(2|a_i|=|\mathbf1_{i=0}+d_i|\), this yields
\[
2\sum_i\max\{|a_i|,1/(2n)\}
\ge 2-\frac4n+d_0+d_1+d_{-1}
+\frac{d_2+d_{-2}}2.
\]
Total variation on a cycle is at least twice the difference between two chosen entries, so
\[
\sum_i|a_i-a_{i-1}|\ge2(a_0-a_4)=1+d_0-d_4.
\]
Using \(d_0=-2u\), \(d_{\pm1}=u-v\), \(d_{\pm2}=v-w\), and \(d_4=\Delta\), we obtain
\[
H\ge3-\frac4n-2u-v-w-\Delta.
\]
Reflection antisymmetry of \(b\) makes the pairs indexed by \(0,1,2,3,4\) and \(-1,-2,-3,-4,-5\) opposite in sign. Consequently
\[
2\sum_i|b_i|\ge4\sum_{j=0}^4|b_j|
\ge-4b_0-4b_1-4b_2-4b_3+4b_4.
\]
The cyclic total variation is at least twice the gap between \(b_0\) and \(b_{-1}=-b_0\), hence
\[
\sum_i|b_i-b_{i-1}|\ge4|b_0|\ge-4b_0.
\]
It follows that
\[
V\ge8u+4v+4w+4\Delta.
\]
Thus \(4H+V\ge12-16/n\), so
\[
\|P\|_{1\to1}\ge(4H+V)/5\ge\frac{12}{5}-\frac{16}{5n}.
\]
Symmetry averaging makes this a lower bound for **every** linear projection, not only invariant ones.

**4. Attaining the bound.** Set
\[
u=\frac{3n-9}{10n},\qquad v=\frac1n,
\qquad b_0=-u,\quad b_1=-v,\quad b_{n-2}=v,\quad b_{n-1}=u,
\]
and set every other \(b_i\) to zero. The associated array \(a_i=(\mathbf1_{i=0}+b_i-b_{i-1})/2\) satisfies
\[
a_0=\frac12-u,\qquad a_{\pm1}=\frac{u-v}{2},\qquad a_{\pm2}=\frac{v}{2}=\frac1{2n},
\]
with all other entries zero. For every integer \(n\ge10\),
\(a_0\ge a_{\pm1}\ge a_{\pm2}>0\). Hence the horizontal absolute sum equals \(2-5/n\), and the cyclic variation of \(a\) equals \(1-2u\). The horizontal column norm is therefore \(H=3-5/n-2u\). The vertical column has total absolute horizontal contribution \(4(u+v)\) and vertical variation \(4u\), giving \(V=8u+4v\). Both simplify exactly to
\[
H=V=\frac{12}{5}-\frac{16}{5n}.
\]
The corresponding operator is a projection by Step 1. This meets the unrestricted lower bound and completes the proof.

## Verification
The standalone standard-library Python script `verify.py` builds the displayed projection over exact rational arithmetic, verifies vanishing incidence, checks that it fixes the entire square-cycle basis and the global rim cycle, and compares every column norm with the claimed rational value for each \(10\le n\le30\). It also runs 400 exact-rational arbitrary-coefficient stress tests of the lower inequality. Its execution returned `CHECK_OK exact_projection_and_norm_assertions= 2122 dimensions=10..30 random_lower_inequality_samples=400`. The finite checks are ancillary; Steps 1–4 prove the theorem for every integer \(n\ge10\).

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii introduced and systematically studied cycle-subspace projections in graph-edge \(\ell_1\) spaces, including diamond and Laakso graph families. Their later study of invariant cycle projections treats equal-factor discrete tori \(C_m\square C_m\), their higher products, and Hamming graphs, rather than the mixed factor \(C_n\square K_2\) for \(n\ge10\). The published general symmetry-averaging and cycle-space framework are used here but do not supply the prism's sharp lower certificate or its explicit \(n\)-dependent value. The present claim is a family-specific exact minimization, not a new general averaging theorem.

## Limitations
The result is restricted to unweighted circular ladders, the real \(\ell_1\) edge norm, and \(n\ge10\). It does not determine the smaller cases, weighted rungs, open ladders, alternative edge \(\ell_p\) norms, or minimum complementary cut-space projection norms. It makes no uniqueness claim for optimal projections. Literature searches and inspections do not certify historical priority; an equivalent formula under generalized Petersen or network-flow terminology is a residual risk. Independent mathematical validation has not been performed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, first posted 2018-07-10, https://arxiv.org/abs/1807.03814.
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949, first posted 2020-07-15, https://arxiv.org/abs/2007.07949.
3. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 2023-05-21, https://arxiv.org/abs/2305.12582.
