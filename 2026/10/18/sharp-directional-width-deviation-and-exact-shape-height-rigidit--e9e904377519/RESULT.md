# Sharp directional-width deviation and exact shape–height rigidity of right prisms

## Finding
Let \(K\subset\mathbb R^2\) be any compact convex body with nonempty interior, let \(h>0\), and form the Euclidean right prism \(P=K\times[-h/2,h/2]\subset\mathbb R^3\). For a uniform spherical direction \(U\in S^2\), denote its orthogonal-projection length by \(W=w_P(U)\). If \(V\) is independently uniform on \(S^1\), define
\[
\mu=\mathbb E\,w_K(V)>0,\qquad q=\frac{\mathbb E\,w_K(V)^2}{\mu^2}\ge1,\qquad \lambda=\frac h\mu,\qquad
\Delta(P)^2=\frac{\mathbb E W^2}{(\mathbb E W)^2}-1.
\]
Then, for every \(K\) and \(h>0\),
\[
\boxed{\Delta(P)^2+1=\frac{16(\lambda^2+2\lambda+2q)}{3(\pi+2\lambda)^2}.}\tag{1}
\]
For **each fixed base** \(K\), the unique height minimizing directional-width deviation is
\[
\boxed{h_*(K)=\mu\,\frac{4q-\pi}{\pi-2};\qquad
\min_{h>0}\Delta(P)^2=\frac{16(2q-1)}{3(\pi^2-4\pi+8q)}-1.}\tag{2}
\]
Among **all** such three-dimensional right prisms, the exact sharp global inequality is
\[
\boxed{\Delta(P)\ge\Delta_*:=\sqrt{\frac{16}{3(\pi^2-4\pi+8)}-1}
=0.075337220010735\ldots.}\tag{3}
\]
Equality holds **if and only if** \(K\) has constant Euclidean width \(w>0\) and \(h/w=(4-\pi)/(\pi-2)=0.751938393884108\ldots\). Thus circular cylinders and prisms with any other constant-width base, including Reuleaux triangles, are precisely the minimizers, up to translations and planar similarities.

The following exact **shape–height deficit identity** makes both equality mechanisms quantitative:
\[
\boxed{\begin{aligned}
\Delta(P)^2-\Delta_*^2={}&
\frac{16\big((\pi-2)\lambda+\pi-4q\big)^2}
{3(\pi+2\lambda)^2(\pi^2-4\pi+8q)}\\[2pt]
&+\frac{32(\pi-2)^2(q-1)}{3(\pi^2-4\pi+8)(\pi^2-4\pi+8q)}.
\end{aligned}}\tag{4}
\]
Both terms are nonnegative, and their simultaneous vanishing characterizes the equality cases in (3).

**Exact polygonal specialization.** Let \(n\ge3\) not be a power of two. Among all right prisms whose base is a genuine convex \(n\)-gon and whose height is free, the sharp minimum is attained **exactly** by Reinhardt \(n\)-gon bases with their individually optimal heights (2). More explicitly, put
\[
q_n=\frac{\pi}{4n\tan(\pi/(2n))}+\frac{\pi^2}{8n^2\sin^2(\pi/(2n))}.
\]
Then the sharp \(n\)-gonal prism bound is
\[
\boxed{\Delta(P)\ge\sqrt{\frac{16(2q_n-1)}{3(\pi^2-4\pi+8q_n)}-1},}\tag{5}
\]
with equality precisely for a Reinhardt \(n\)-gon base and height \(h=(\operatorname{per}(K)/\pi)(4q_n-\pi)/(\pi-2)\). This specialization uses the complete planar minimizer theorem of Akiyama and Kamae; it does not assert a classification for side counts that are powers of two.

## Assumptions and scope
Widths are support-function widths, \(w_C(u)=\max_{x\in C}x\cdot u-\min_{x\in C}x\cdot u\). All measures on \(S^1\) and \(S^2\) are normalized rotation-invariant probabilities. Bases can be nonsmooth or noncentrally symmetric. A right prism means the Cartesian product with a segment orthogonal to the base plane; no assertion is made for oblique prisms. Translating a body does not affect width. For a planar constant-width body \(K\), \(w_K(V)\equiv w\) by definition. A Reinhardt polygon means a planar extremizer in the Akiyama–Kamae classification, not merely a regular polygon.

## Proof
**Spherical decomposition.** A spherical uniform direction can be represented as
\[
U=(\sqrt{1-T^2}\,V,\varepsilon T),
\]
where \(T\) is uniform on \([0,1]\), \(V\) uniform on \(S^1\), and \(\varepsilon\) an independent symmetric sign. The product support-function identity therefore gives the **exact** width decomposition
\[
W=\sqrt{1-T^2}\,w_K(V)+hT.\tag{6}
\]
Elementary one-dimensional integration yields
\[
\mathbb E\sqrt{1-T^2}=\frac\pi4,\quad
\mathbb ET=\frac12,\quad
\mathbb E(1-T^2)=\frac23,\quad
\mathbb E[T\sqrt{1-T^2}]=\frac13,\quad
\mathbb ET^2=\frac13.
\]
Independence in (6) gives
\[
\mathbb EW=\mu\Big(\frac\pi4+\frac\lambda2\Big),\qquad
\mathbb EW^2=\frac{\mu^2}{3}(2q+2\lambda+\lambda^2).
\]
Dividing proves (1), without approximation or smoothness assumptions.

**Height optimization.** Let \(R(q,\lambda)=\Delta(P)^2+1\) denote the right-hand side of (1). At fixed \(q\ge1\), direct differentiation gives
\[
\frac{\partial R}{\partial\lambda}
=\frac{32\big((\pi-2)\lambda+\pi-4q\big)}{3(\pi+2\lambda)^3}.
\tag{7}
\]
Since \(\pi-2>0\) and \(4q-\pi\ge4-\pi>0\), the derivative is strictly negative until the single positive point \(\lambda=(4q-\pi)/(\pi-2)\) and strictly positive afterward. Substitution proves the second expression in (2); in particular the infimum is attained at a finite positive height.

**Global shape optimization and rigidity.** The optimized second-moment ratio is
\[
R_*(q)=\frac{16(2q-1)}{3(\pi^2-4\pi+8q)},\qquad
R_*'(q)=\frac{32(\pi-2)^2}{3(\pi^2-4\pi+8q)^2}>0.
\]
The inequality \(q\ge1\) is exactly nonnegativity of the variance of the planar width. Equality \(q=1\) means this continuous directional-width function is constant almost everywhere and hence everywhere. Therefore (2) yields the sharp global inequality (3), attained by every constant-width base at the stated unique height.

To verify the **exact** deficit (4), split
\[
R(q,\lambda)-R_*(1)=[R(q,\lambda)-R_*(q)]+[R_*(q)-R_*(1)].
\]
Algebraic common-denominator reduction yields
\[
R(q,\lambda)-R_*(q)=
\frac{16((\pi-2)\lambda+\pi-4q)^2}{3(\pi+2\lambda)^2(\pi^2-4\pi+8q)},
\]
\[
R_*(q)-R_*(1)=
\frac{32(\pi-2)^2(q-1)}{3(\pi^2-4\pi+8)(\pi^2-4\pi+8q)}.
\]
All denominators are strictly positive, which proves (4), its sharpness, and the complete equality classification.

**Polygonal transfer.** For every planar convex body, Cauchy's projection formula gives \(\mu=\operatorname{per}(K)/\pi\). The increasing function \(R_*(q)\) transfers the entire planar classification of \(q=1+\delta(w_K)^2\) exactly to the height-optimized right-prism problem. Akiyama and Kamae prove (Theorems 6–7 of their first public 2022 preprint) that for \(n\ge3\) not a power of two, the minimum planar deviation squared is \(q_n-1\), and the minimizing \(n\)-gons are exactly the Reinhardt polygons. Substitution into (2) proves (5) and its full base-and-height equality cases. This step expressly relies on their cited planar theorem rather than reproving it.

## Verification
The standalone standard-library `verify.py` implements 4,000 seeded independent parameter pairs to test the two-term exact deficit identity and unique-height inequalities (16,000 individual algebraic comparisons). It independently computes planar projection widths of regular triangles, squares, pentagons, and heptagons and integrates actual three-dimensional prism widths over spherical directions for three heights per base; these 12 directional integrations agree with (1). It additionally checks three direct polar integrations of constant-width cylinder profiles, two sharp numerical constants, and three checks of the published odd-polygon planar formula. Run `python3 verify.py` from the extracted package directory; expected output starts with `VERIFY_OK 16020`. These finite computations are regression checks; the proofs of all infinite statements are the identities and monotonicity arguments above.

## Relationship to prior work
Akiyama and Kamae, *Width Deviation of Convex Polygons* (first public 18 January 2022), determine the planar width-deviation minimizers, including Reinhardt polygons when the number of sides is not a power of two. Their problem is confined to directions in a plane and does not optimize three-dimensional prism height. A publicly available calculation entitled *Exact mean-square width of every uniform regular prism* treats only unit-edge regular polygon bases with height equal to that edge; it establishes the spherical product decomposition but not the sharp shape-and-height optimization, arbitrary convex bases, the exact two-term rigidity identity, or the full constant-width equality family. Classical Cauchy width integrals and the constant-width characterization are ingredients, not the combined optimization result. The polygonal specialization (5) uses the prior planar minimizer theorem as a stated input; that prior characterization is not claimed as new.

## Limitations
The theorem concerns only Euclidean right prisms in three dimensions and the coefficient of variation of directional widths. Other shape statistics or ambient dimensions may behave differently. At numbers of base vertices equal to powers of two, the general reduction (1)–(4) remains valid but no exact polygonal minimizing shape is asserted. No claim is made that the circle uniquely minimizes: all planar constant-width bodies give equality. Mathematical originality is assessed against the cited accessible sources and may be affected by earlier stereological treatments using alternative terminology. Independent validation has not been performed.

## References
1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1 (first public 18 January 2022), https://arxiv.org/pdf/2201.06736 ; see especially Theorems 6–7.
2. *Exact mean-square width of every uniform regular prism*, public research record dated 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mean-square-width-of-every-uniform-regular-prism--eb371b3be549 ; especially the full mathematical result's equations (2)–(3) and limitations.
3. *Exact cylinder shadow mixed moment and sharp positive covariance*, public research record dated 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-cylinder-shadow-mixed-moment-and-sharp-positive-covariance--1feeb231b707 ; concerning different random projected area/perimeter observables.
