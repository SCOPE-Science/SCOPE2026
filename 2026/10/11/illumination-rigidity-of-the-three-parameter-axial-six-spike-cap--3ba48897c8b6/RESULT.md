# Illumination rigidity of the three-parameter axial six-spike cap body
## Finding
For any three real parameters \(\rho_1,\rho_2,\rho_3>1\) satisfying
\[
\rho_i^{-2}+\rho_j^{-2}\ge 1\qquad(1\le i<j\le3),
\]
let
\[
K(\rho)=\operatorname{conv}\left(B_2^3\cup\{\pm\rho_1e_1,\pm\rho_2e_2,\pm\rho_3e_3\}\right)\subset\mathbb R^3.
\]
The exact ordinary directional illumination number is
\[
\boxed{I(K(\rho))=\begin{cases}
6,&\rho_1=\rho_2=\rho_3=\sqrt2,\\
4,&\text{otherwise}.
\end{cases}}
\]
In particular, no member of this entire three-parameter family has illumination number five. The collapse from six to the dimension-minimal value four persists when two pairwise base-cap tangencies remain exact. For example, \(\rho=(\sqrt5/2,\sqrt5/2,\sqrt5)\) has two such tangencies, yet needs only four directions.

## Assumptions and scope
The Euclidean unit ball is \(B_2^3=\{x\in\mathbb R^3:\|x\|_2\le1\}\). The vectors \(e_1,e_2,e_3\) form the standard orthonormal basis. A direction \(v\in S^2\) illuminates \(p\in\partial K\) when \(p+t v\in\operatorname{int}K\) for some \(t>0\). The number \(I(K)\) is the minimum cardinality of a finite set of illuminating unit directions.

Write
\[
q_i=\rho_i^{-2}\in(0,1),\qquad c_i=\sqrt{1-q_i}\in(0,1).
\]
For spikes on distinct coordinate axes, the minimum squared norm along the segment joining \(\sigma\rho_i e_i\) to \(\tau\rho_j e_j\), \(\sigma,\tau\in\{-1,1\}\), is \(\rho_i^2\rho_j^2/(\rho_i^2+\rho_j^2)\), hence that segment meets the unit ball exactly when \(q_i+q_j\ge1\). Segments between opposite spikes on the same axis pass through the origin. Thus the stated assumptions are precisely those making the six spikes a cap body of the ball. Each of the six exterior points is a vertex of this body.

The cap-body illumination criterion [1, Lemmas 5--8 and Theorem 2; 2, Proposition 3] states: an axial vertex \(\sigma\rho_i e_i\) is illuminated by \(v\in S^2\) exactly when
\[
\sigma v_i<-c_i,
\]
and a finite family of unit directions illuminating all exterior spike vertices illuminates the whole cap body provided its positive hull is \(\mathbb R^3\). All inequalities at the vertices are strict; equality never suffices.

## Proof
**1. A strict pair gives four directions.** Assume that \(q_i+q_j>1\) for some pair \(i\ne j\), and denote the remaining index by \(k\). Since
\[
c_i^2+c_j^2=2-q_i-q_j<1,
\]
the open positive-quadrant arc
\[
U=\{(a,b)\in S^1:a>c_i,\ b>c_j\}
\]
is nonempty. More precisely, put \(\alpha=\arcsin(c_j)\), \(\beta=\arccos(c_i)\), and define
\[
\theta=\tfrac12(\alpha+\beta),\qquad\delta=\min\{(\beta-\alpha)/4,\sqrt{q_k}/2\}>0.
\]
Take \(u=(a,b)=(\cos\theta,\sin\theta)\) and \(u'=(a',b')=(\cos(\theta+\delta),\sin(\theta+\delta))\). Both belong to \(U\), are distinct and nonparallel, and \(\|u'-u\|/2=\sin(\delta/2)<\sqrt{q_k}\). Set
\[
w=\tfrac12(u'-u),\qquad z=\sqrt{1-\lVert w\rVert_2^2}.
\]
By the explicit bound on \(\delta\), we have \(\lVert w\rVert_2^2<q_k\), hence \(z>\sqrt{1-q_k}=c_k\).

Specify four vectors by their coordinates in the ordered orthonormal basis \((e_i,e_j,e_k)\):
\[
v_1=(a,b,0),\quad v_2=(-a',-b',0),\quad
v_3=(w_1,w_2,z),\quad v_4=(w_1,w_2,-z).
\]
All four are unit vectors. They satisfy the **strict six-spike tests**: \(v_1\) illuminates the two negative spikes on axes \(i,j\) because \(a>c_i\), \(b>c_j\); \(v_2\) illuminates the two positive spikes on those axes because \(a'>c_i\), \(b'>c_j\); \(v_3\) illuminates the negative spike on axis \(k\) and \(v_4\) the positive spike there because \(z>c_k\).

Moreover, their sum vanishes:
\[
v_1+v_2+v_3+v_4=(u-u'+2w,0)=0.
\]
As \(u\) and \(u'\) are not parallel and \(z>0\), the first three vectors are linearly independent. A spanning family of four vectors with a dependence having **all strictly positive coefficients** positively spans \(\mathbb R^3\): write an arbitrary target in the basis \(v_1,v_2,v_3\), then add a sufficiently large positive multiple of the zero-sum relation to make all four coefficients positive. Thus the published cap-body criterion shows \(I(K(\rho))\le4\).

Every three-dimensional convex body needs at least four illuminating directions. Indeed, an illuminating family must positively span \(\mathbb R^3\) in order to illuminate every unit-sphere point not hidden behind a spike; more generally, a family of at most three vectors in \(\mathbb R^3\) lies in a closed hemisphere, so a supporting boundary point with outward normal orthogonal or opposite to their directions cannot be illuminated by any of them. Therefore \(I(K(\rho))=4\).

**2. The unique no-strict-pair case.** If there is no strict pair, all three inequalities \(q_i+q_j\ge1\) are equalities. Subtraction gives \(q_1=q_2=q_3=1/2\), equivalently \(\rho_1=\rho_2=\rho_3=\sqrt2\). The six vertex tests then require a signed coordinate strictly larger than \(1/\sqrt2\) in magnitude. A single unit vector cannot illuminate two vertices on different axes, since the sum of the squares of the two relevant coordinates would exceed one; neither can it illuminate opposite vertices on the same axis. Hence at least six directions are needed. The six directions \(\pm e_i\) positively span the space and illuminate the six corresponding opposite spikes, so six suffice. This proves the asserted classification for all allowed parameters.

## Verification
An independent-from-the-text standalone script `verify.py` checks the four-direction construction numerically at structured boundary/tangency cases and 300 randomized strictly feasible triples, asserting unit norms, zero sum, full rank, and all six strict inequalities. It prints `VERIFY_OK`; these finite evaluations are only consistency checks. The proof for uncountably many parameters is the analytic existence argument in the preceding section, not the tests.

For reproduction, run `python verify.py` using the Python standard library. The example \(q=(4/5,4/5,1/5)\) checks two tangencies; the endpoint \(q=(1/2,1/2,1/2)\) takes the six-direction branch. All formulas use exact real inequalities in the theorem and do not depend on floating-point tolerances.

## Relationship to prior work
Ivanov and Strachan [1] proved the sharp uniform bound six for centrally symmetric three-dimensional cap bodies and gave the vertex illumination criterion. Arman, Kaire and Prymak [2] proved the same six bound for all three-dimensional cap bodies; their paper identifies the regular six-spike octahedral extremizer. Neither result determines the exact illumination number at every point of the unequal-radius three-parameter family. The related published calculation [4] determines exactly the **equal-radius line** \(\rho_1=\rho_2=\rho_3\), obtaining four below the octahedral endpoint and six at it, but explicitly leaves unequal axial radii untreated. The current result supplies the full anisotropic extension, including all tangent boundary strata and a proof that the intermediate value five does not appear within this family.

The spherical-code bounds in [3] address global cap-body illumination and do not imply this exact parameterwise four-direction construction. Because [1]--[4] already cover the general six upper bound, the octahedral value six, and the equal-radius four/six jump, none of those earlier statements is represented here as new.

## Limitations
The theorem applies only to ordinary one-fold directional illumination in \(\mathbb R^3\), and only to a Euclidean unit ball with three antipodal pairs of spikes on mutually orthogonal axes under the exact cap-body constraints. The conclusion does not classify off-axis configurations, arbitrary centrally symmetric cap bodies, multiply illuminated bodies, or quantitative robustness of the four-direction witnesses as a strict pair approaches tangency. The derivation proves existence rather than a uniform positive geometric margin near the exceptional point. Exhaustive search of unpublished or unindexed work is impossible; an equivalent prior classification under another formulation remains an originality risk.

## References
[1] I. Ivanov and C. Strachan, *On the illumination of centrally symmetric cap bodies in small dimensions*, arXiv:2007.09765v1 (2020), especially Theorem 2, Lemma 5, and Section 3. https://arxiv.org/pdf/2007.09765

[2] A. Arman, J. S. Kaire, and A. Prymak, *Illumination number of 3-dimensional cap bodies*, arXiv:2507.08712v1 (first posted 2025-07-11), primary MSC 52A15, especially Proposition 4 and Theorem 2. https://arxiv.org/abs/2507.08712

[3] A. Arman, A. Bondarenko, A. Prymak, and D. Radchenko, *On a Gallai-type problem and illumination of spiky balls and cap bodies*, Mathematika 71 (2025), e70017, especially Proposition 9 and Theorem 4. https://doi.org/10.1112/mtk.70017

[4] *Endpoint instability of the six-spike octahedral cap body* (2026), public research record `2026/10/4/SCOPE-endpoint-instability-of-the-six-spike-octahedral-cap-body--1f124f444fca`; equal-radius theorem and explicit exclusion of unequal radii. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-endpoint-instability-of-the-six-spike-octahedral-cap-body--1f124f444fca

[5] A. Arman, J. S. Kaire, and A. Prymak, *Hadwiger's conjecture for cap bodies*, arXiv:2510.25968v1 (2025), Proposition 3 and global dimensional bounds. https://arxiv.org/abs/2510.25968
