# Exact Löwner ellipsoids and contact transitions for matched-pair Lipschitz metrics

## Finding
For every integer \(m\ge2\), let \(n=2m\) points form \(m\) distinguished pairs; points in one pair have metric distance \(t\in[1,2]\), and points in different pairs distance \(1\). Let \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), with its canonical Euclidean structure, and let the real Lipschitz dual ball be
\[
Q_{n,t}=\{x\in H:|x_i-x_j|\le d_t(i,j)\}.
\]
Write \(H=U\oplus W\), with \(U\) comprising the \(m\) pair-antisymmetric coordinates and \(W\) the \((m-1)\)-dimensional, centered, pair-constant coordinates; let \(P_U,P_W\) be the orthogonal projections. The unique minimum-volume enclosing ellipsoid is
\[
\boxed{E_{n,t}=\{x\in H:a_{n,t}\|P_Ux\|_2^2+b_{n,t}\|P_Wx\|_2^2\le1\},}
\]
where
\[
\boxed{(a_{n,t},b_{n,t})=\begin{cases}
(1/[1+(t-1)^2],1),&n=4,\\
(2/3,2/3),&n=6,\ 1\le t\le5/3,\\
((3-t)/2,(1+t)/4),&n=6,\ 5/3\le t\le2,\\
(4/n,4/n),&n\ge8.
\end{cases}}
\]
The two six-point formulas agree at the boundary. Hence for \(n\ge8\) the ellipsoid does not change at all while the metric and unit ball enlarge; at six points it changes after exactly \(t=5/3\). Its intrinsic volume is
\[
\operatorname{vol}_{n-1}(E_{n,t})=\frac{\pi^{(n-1)/2}}{\Gamma((n+1)/2)}a_{n,t}^{-m/2}b_{n,t}^{-(m-1)/2}.
\]
The exact numbers of touching **vertices** of \(Q_{n,t}\) are \(6\) at \(n=4,t\in\{1,2\}\) and \(10\) for \(n=4,1<t<2\); for \(n=6\) they are \(20\) when \(t<5/3\), \(56\) at \(t=5/3\), and \(24\) when \(t>5/3\); for \(n=8\) they are \(70\) when \(t<2\) and \(78\) when \(t=2\); for every even \(n\ge10\) they are \(\binom n{n/2}\) for all \(t\in[1,2]\).

## Assumptions and scope
The statements concern **real** finite-dimensional Lipschitz-free duality and the inherited Euclidean norm on the zero-sum hyperplane. The metric is valid since \(t\le2\). Both subspaces are canonical for the given matching. For any vector \(x\), writing \(\bar x=n^{-1}\sum_i x_i\),
\[
\|P_Ux\|^2=\frac12\sum_{j=1}^m(x_{2j-1}-x_{2j})^2,\qquad
\|P_Wx\|^2=\sum_i(x_i-\bar x)^2-\|P_Ux\|^2.
\]

## Proof
**Global symmetry.** Central symmetry and uniqueness center the Löwner ellipsoid at zero. Independently swapping members of each pair and permuting pairs preserve the body. Every invariant positive quadratic form is \(aP_U+bP_W\): swaps eliminate cross terms between pair differences and pair means, permutation symmetry equalizes antisymmetric coefficients, and the pair-mean representation restricted to sum zero admits one scalar coefficient. Thus the global problem reduces, without restricting competitors, to maximizing \(m\log a+(m-1)\log b\) under containment, since the ellipsoid volume is proportional to \(a^{-m/2}b^{-(m-1)/2}\).

**Global extremal reduction.** Let \(q_{a,b}(x)=a\|P_Ux\|^2+b\|P_Wx\|^2\), a positive quadratic form invariant under constants. For any feasible potential with range at most one, translate its minimum to zero and round each coordinate independently to \(0\) or \(1\). Feasibility is preserved and separate coordinate convexity guarantees some rounded potential has no smaller value of \(q_{a,b}\). If the range is \(s>1\), the two extreme points must be in one matched pair, since different pairs are at distance one. Put their values at \(0,s\). Each remaining coordinate lies in \([s-1,1]\), so rounding these coordinates to the endpoints again preserves all inequalities: the two allowed outside values differ by \(2-s\le1\), and matched-pair differences never exceed \(t\). For a fixed endpoint assignment the rounded vector is affine in \(s\in[1,t]\). Convexity of \(q_{a,b}\) in \(s\) makes its maximum an endpoint \(s=1\) or \(s=t\); at \(s=1\) it is binary. Consequently, checking **all** binary cuts and the exceptional-spread configurations with one pair \((0,t)\), all other coordinates in \(\{t-1,1\}\), proves containment for every real potential. No unproved vertex classification is used.

**Spherical regimes and sharp radius.** A binary potential with \(k\) ones has centered norm squared \(k(n-k)/n\le n/4\), with equality for balanced cuts. For a spread with a pair \((0,s)\) and \(k\) of the other \(n-2\) entries one, completing the square shows its centered norm squared maximized at the integer \(k=(n-2)/2\) with value \(F_n(s)=s^2/2+(n-2)(2-s)^2/4\). Since \(F_n\) is convex, the complete radius formula is
\[
R(Q_{n,t})^2=\max\{n/4,F_n(t)\},\qquad
F_n(t)-n/4=(t-1)(nt-3n+8)/4.
\]
At \(t=1\) all distances equal one; full symmetric-group invariance makes the unique Löwner ellipsoid the sphere of radius squared \(n/4\). Since \(Q_{n,1}\subseteq Q_{n,t}\), that optimal sphere persists whenever it continues to contain the enlarged ball. The radius formula shows this happens for all \(n\ge8\) and for \(n=6,t\le5/3\).

**Four points.** Let \(g=1+(t-1)^2\). One binary cut has \((\|P_Ux\|^2,\|P_Wx\|^2)=(0,1)\); one spread vector has \((g,0)\). Any enclosing ellipsoid therefore has \(b\le1\) and \(a\le1/g\). Their simultaneous equality at \(a=1/g,b=1\) is feasible: every binary cut has \(\|x\|^2\le1\), and the only spread type not already active has \((U^2,W^2)=(t^2/2,(2-t)^2/4)\) and slack
\[
1-\frac{t^2}{2g}-\frac{(2-t)^2}{4}=\frac{t(2-t)^3}{4g}\ge0.
\]
These sharp independent coordinate bounds uniquely maximize \(2\log a+\log b\).

**Six points.** For \(5/3\le t\le2\) set \(a=(3-t)/2\) and \(b=(1+t)/4\). The binary cuts have precisely five attainable \((U^2,W^2)\) classes and respective slacks:
\[
\begin{array}{c|c}
(U^2,W^2)&1-aU^2-bW^2\\
(1/2,1/3)&(1+t)/6\\
(0,4/3)&(2-t)/3\\
(1,1/3)&(5t-7)/12\\
(1/2,1)&0\\
(3/2,0)&(3t-5)/4.
\end{array}
\]
For exceptional-spread vectors (one pair \((0,t)\), two other pairs with coordinates in \(\{t-1,1\}\)), the complete four classes and slacks are
\[
\begin{array}{c|c}
(U^2,W^2)&1-aU^2-bW^2\\
(t^2/2,(2-t)^2/3)&(2-t)^2(1+t)/6\\
(t^2-2t+2,(2-t)^2/3)&(2-t)^2(5t-7)/12\\
(t^2/2,(2-t)^2)&0\\
(t^2/2+(2-t)^2,0)&(2-t)^2(3t-5)/4.
\end{array}
\]
Every listed slack is nonnegative. Two active inequality normals are \(C=(1/2,1)\) and \(S=(t^2/2,(2-t)^2)\). They certify **global**, rather than only symmetric local, optimality through the exact positive multipliers
\[
\nabla(3\log a+2\log b)=\lambda_C C+\lambda_S S,\qquad
\lambda_C=\frac{5t^3-15t^2+12}{(t-3)(t-1)(t+1)},\quad
\lambda_S=-\frac{5t-3}{(t-3)(t-1)(t+1)}.
\]
Both multipliers are positive for \(5/3\le t\le2\): their denominator is negative, the cubic numerator of \(\lambda_C\) is negative and decreasing there, and \(5t-3>0\). For any feasible \((a',b')\), concavity gives
\[
\Phi(a',b')-\Phi(a,b)\le\nabla\Phi\cdot((a',b')-(a,b))\le0.
\]
Strict concavity makes equality possible only at the stated precision pair. This proves the complete six-point regime.

**Contact enumeration.** Strict convexity implies every maximizer of \(q_{a,b}\) on the polytope is a vertex, and the reduction above gives all possible contact types. In the spherical regimes, the balanced cuts yield \(\binom n{n/2}\) contacts. Additional spreads can be spherical contacts only when \(F_n(t)=n/4\): at \((n,t)=(6,5/3)\), there are \(3\) exceptional-pair choices, \(2\) extreme orientations and \(\binom42=6\) outside endpoint assignments, yielding \(36\) extras; at \((8,2)\) there are \(8\) distinct extremal exceptional-pair choices/orientations and one outside value, hence \(8\) extras. The strict four-point regime has \(2\) pair-constant cuts and \(8\) split-outside spreads. For \(n=6\), \(5/3<t<2\), exactly \(12\) balanced cuts with one split pair and \(12\) spreads whose other two pairs are each monochromatic at opposite endpoints touch. At \(t=2\), six spread patterns coalesce while six pair-constant cuts join, retaining \(24\); at four points endpoint coincidences reduce the count to six. At \(t=1\) the equilateral contact count is the balanced-cut count. This exhausts the displayed phase chart.

## Verification
The attached standalone Python 3 exact-rational checker tests thirteen cases at \(n\in\{4,6,8,10\}\), including every critical threshold and the contact-count jumps. The strict-convexity and tight-incidence arguments guarantee that at rational \(t=p/q\) all vertices have coordinates on the \(1/q\) mesh after translation, so these finite enumerations do cover every vertex in their respective cases. Its final output is `EXACT_ELLIPSOID_PASS: 13`. This corroborates the algebra but does not establish infinite-parameter validity, which rests on the proof above.

## Relationship to prior work
The duality between finite Lipschitz-free balls and Lipschitz potential polytopes, the uniqueness of the Löwner ellipsoid and basic symmetry principles are standard. Higashitani, Jochemko and Michałek classify facets for complete multipartite **graph metrics** at \(t=2\). A previously indexed complete-multipartite interpolation theorem classifies the same binary and spread potential families over \(1<t<2\), but neither result determines the optimal two-eigenvalue enclosing quadratic form, the six-point phase at \(5/3\), nor the full optimal-ellipsoid contact counts. These latter results require the independent enclosing-ellipsoid optimization and its exact dual multipliers. General finite-dimensional Lipschitz-free geometry is credited as background.

## Limitations
Only common exceptional-pair lengths \(1\le t\le2\), even point counts at least four, and canonical mean-zero Euclidean coordinates are treated. The results are not the John **inscribed** ellipsoid, nor Banach–Mazur distances or affine-universal constructions. Contact counts refer to vertices of the dual Lipschitz polytope, equivalently polar facets, not every face. An equivalent theorem in unindexed literature remains possible; the search comparison cannot establish absolute novelty. No independent mathematical audit is represented.

## References
1. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (2018-07-20), Section 3.1 and Proposition 3.5. https://arxiv.org/abs/1807.07678
2. R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278v1 (2018-10-26). https://arxiv.org/abs/1810.11278
3. M. Alexander, M. Fradelizi, M. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1 (2019-11-24). https://arxiv.org/abs/1911.10642
4. *Sharp facet jumps for interpolated complete-multipartite Lipschitz-free balls*, publicly accessible mathematical research record (2026); the cited result is a facet classification, not an optimal ellipsoid theorem.
