# Sharp radial-weight plateau and radical boundary for wheel cycle projections

## Finding

Let \(m\ge 6\) be an integer. Give each rim edge of the wheel graph \(W_m=K_1*C_m\) length \(1\), and each of its \(m\) spokes length \(t\). Let \(X_{m,t}\) be the real edge space with norm
\[
\|(s,r)\|_{m,t}=t\sum_{i=0}^{m-1}|s_i|+\sum_{i=0}^{m-1}|r_i|,
\]
and let \(Z_m\subseteq X_{m,t}\) be the real circulation (cycle) subspace. The infimum of the norms of **all** real linear projections \(P:X_{m,t}\to Z_m\) is denoted \(\lambda_m(t)\).

Write
\[
t_* =\frac{1+\sqrt{17}}4,\qquad F(t)=\frac{(1+2t)^2}{1+2t+2t^2}.
\]
**Theorem.** For every integer \(m\ge6\) and every real \(t\in[1/2,t_*]\),
\[
\boxed{\lambda_m(t)=F(t).}
\]
In particular, the optimal constant is independent of the number of rim vertices throughout the specified interval and is strictly increasing in the spoke length. The parameter boundary is sharp in the following explicit sense: for every \(m\ge6\) and every \(t\in(t_*,3/2)\),
\[
\boxed{\lambda_m(t)>F(t).}
\]
Moreover, for each \(m\in\{3,4,5\}\) and each \(t\in(1/2,t_*]\), one has \(\lambda_m(t)<F(t)\); thus six is the smallest rim size at which this common-value law holds throughout the nondegenerate interval. No formula for \(\lambda_m(t)\) beyond the stated interval is asserted.

## Assumptions and scope

The edge set consists of \(m\) oriented spokes from the hub to rim vertex \(i\in\mathbb Z/m\mathbb Z\) and \(m\) oriented rim edges from \(i\) to \(i+1\). Edge coordinates are real and all weights positive. The norm above is an **edge** weighted \(\ell_1\)-norm, not the Hilbert edge norm or the norm of the quotient space. All projections, whether or not they respect graph symmetries, are included in the infimum. At \(t=1/2\), a rim edge is tied with the two-spoke route, so the presentation retains some metrically redundant edges; the statement remains valid for the displayed edge-space model. For \(t>1/2\), these are canonical shortest-path edges.

Define the cyclic difference operator \(D:\mathbb R^m\to\mathbb R^m\) by \((Dr)_i=r_i-r_{i-1}\). Flow conservation at rim vertex \(i\) gives \(s_i=(Dr)_i\), hence
\[
Z_m=\{(Dr,r):r\in\mathbb R^m\}.
\]
The choice of orientations changes only coordinate signs and does not alter any projection norm.

## Proof

**1. Reduction to a dihedral convolution.** The wheel's rotations and reflections induce signed coordinate-permutation isometries of \(X_{m,t}\) leaving \(Z_m\) invariant. Averaging any projection over this finite group produces a dihedrally invariant projection without increasing its norm. A projection onto \(Z_m\) is determined by a linear map from the input spoke and rim coordinates to an output rim vector:
\[
P(s,r)=(D(As+Br),As+Br).
\]
It acts as the identity on \(Z_m\) precisely when \(AD+B=I\). Rotation invariance makes \(A\) circulant. Its first column \(a=(a_i)\) satisfies, by reflection equivariance,
\[
a_i=-a_{-i-1}\qquad(i\in\mathbb Z/m\mathbb Z).
\]
Conversely, every such \(a\) defines a dihedrally invariant projection by taking \(A\) to be its convolution matrix and \(B=I-AD\).

Put \(p=Da\) and \(b=e_0-p\), where \(e_0\) is the first coordinate vector. Since a circulant convolution commutes with \(D\), all spoke-input columns have the same weighted column norm and all rim-input columns have the same norm. The induced \(\ell_1\)-operator norm therefore equals
\[
\|P\|=\max\{S(a),T(a)\},\qquad
S(a)=\frac{\|a\|_1}{t}+\|Da\|_1,\qquad
T(a)=\|b\|_1+t\|Db\|_1.
\]
This is an exact reduction of the unrestricted projection problem, not an assumption that the optimal projection is orthogonal.

**2. Explicit upper certificate.** For \(t\in[1/2,t_*]\), set
\[
Z=1+2t+2t^2,\qquad u=\frac{t(1+2t)}{2Z},\qquad
a_0=u,\quad a_{m-1}=-u,\quad a_i=0\ \text{otherwise}.
\]
A direct calculation, valid for all \(m\ge6\), gives
\[
Da=(2u,-u,0,\ldots,0,-u),\qquad
b=(1-2u,u,0,\ldots,0,u).
\]
The defining inequality \(t\le t_*\) is equivalent to \(2t^2-t-2\le0\), which is in turn equivalent to \(u\le1/3\). Consequently \(b\) has nonnegative coordinates, \(\|b\|_1=1\), and
\[
\|a\|_1=2u,\quad\|Da\|_1=4u,\quad\|Db\|_1=2-4u.
\]
It follows that
\[
S(a)=\left(\frac2t+4\right)u,
\qquad T(a)=1+2t-4tu,
\]
and substitution of \(u\) shows that both are exactly \(F(t)\). Thus \(\lambda_m(t)\le F(t)\).

**3. A uniform lower certificate.** Consider an arbitrary reflection-antisymmetric kernel \(a\). Write \(h=\lfloor(m-2)/2\rfloor\). Its independent coordinates are \(a_0,a_1,\ldots,a_h\); the remaining coordinates are determined by \(a_i=-a_{m-1-i}\), and a middle coordinate is zero when \(m\) is odd. Because \(\sum_i (Da)_i=0\) and \((Da)_0=2a_0\),
\[
\|a\|_1=2\sum_{j=0}^{h}|a_j|,\qquad
\|Da\|_1\ge 4|a_0|.
\]
Therefore, with \(A=2/t+4\),
\[
S(a)\ge A a_0+\frac2t\sum_{j=1}^{h}|a_j|.\tag{1}
\]

Define a sign vector \(q\in[-1,1]^m\) by \(q_0=q_{m-2}=q_{m-1}=1\), \(q_1=q_2=-1\), and all other coordinates zero. The indices here are distinct for every \(m\ge6\). The cyclic second-difference calculation \((q^{\mathsf T}D^2)_j=q_j-2q_{j+1}+q_{j+2}\) yields
\[
q^{\mathsf T}D e_0=2,\qquad
q^{\mathsf T}D^2a=4a_0+\sum_{j=1}^{h}c_j a_j,
\qquad |c_j|\le1.\tag{2}
\]
For clarity, the nonzero coefficients after \(c_0=4\) are: \((c_1,c_2)=(1,1)\) for \(m=6\); \((c_1,c_2)=(1,0)\) for \(m=7\); and \(c_1=1,c_3=-1\) for \(m\ge8\), with all other \(c_j=0\). The formula is valid at \(m=8\), when \(h=3\).

Since \(\sum b_i=1\), \(\|b\|_1\ge1\). By duality for \(\ell_1\), \(\|Db\|_1\ge q^{\mathsf T}Db\). Using (2),
\[
T(a)\ge1+2t-4t a_0-t\sum_{j=1}^{h}|a_j|.\tag{3}
\]
Set
\[
\alpha=\frac{2t^2}{Z},\qquad \beta=\frac{1+2t}{Z},
\qquad \alpha+\beta=1.
\]
The \(a_0\) coefficients in \(\alpha\) times (1) plus \(\beta\) times (3) cancel because \(\alpha A=4t\beta\). Their remaining coefficient is
\[
\frac{2\alpha}{t}-t\beta
=\frac{t(3-2t)}{Z}>0\quad\text{for }0<t<3/2.
\]
Consequently, for every \(m\ge6\) and every \(0<t<3/2\),
\[
\max\{S(a),T(a)\}\ge\alpha S(a)+\beta T(a)
\ge F(t)+\frac{t(3-2t)}{Z}\sum_{j=1}^{h}|a_j|.\tag{4}
\]
Together with the upper certificate, (4) proves the exact formula on \([1/2,t_*]\). Differentiation gives \(F'(t)=2(1+2t)/(1+2t+2t^2)^2>0\).

**4. Sharpness of the radial boundary.** Fix \(m\ge6\) and \(t\in(t_*,3/2)\). Suppose a projection of norm at most \(F(t)\) existed. Average it to obtain a kernel \(a\). Since the coefficient of the sum in (4) is strictly positive, equality forces \(a_j=0\) for all \(1\le j\le h\). The only potentially nonzero entries are therefore \(a_0=v\) and \(a_{m-1}=-v\). Equality of the convex combination \(\alpha S+\beta T\) and \(\max\{S,T\}=F(t)\), with \(\alpha,\beta>0\), forces \(S=T=F(t)\); hence \(v=t(1+2t)/(2Z)>1/3\). In the specified interval also \(v<1/2\), so \(\|b\|_1=1\) but \(\|Db\|_1=8v-2\). The resulting \(T=1+t(8v-2)\) exceeds \(1+2t-4tv=F(t)\) by \(4t(3v-1)>0\), a contradiction. Therefore \(\lambda_m(t)>F(t)\) for every \(t\in(t_*,3/2)\).

**5. Minimality of the six-rim cutoff.** For \(m\in\{3,4,5\}\), let
\[
H_m=\sum_{j=0}^{m-1}\left|1-\frac{2j}{m-1}\right|,
\qquad (H_3,H_4,H_5)=(2,8/3,3),
\]
and choose a convolution kernel \(a_j=v(1-2j/(m-1))\), where
\[
v=\frac{t(1+2t)}{H_m+4t+\frac{4m}{m-1}t^2}.
\]
For every \(t\in[1/2,t_*]\), direct column calculations give an admissible projection of norm
\[
U_m(t)=\frac{(H_m+4t)(1+2t)}{H_m+4t+\frac{4m}{m-1}t^2}.
\]
An exact common-denominator comparison gives
\[
\begin{aligned}
F(t)-U_3(t)&=\frac{t^2(2t+1)^2}{(2t^2+2t+1)(3t^2+2t+1)},\\
F(t)-U_4(t)&=\frac{2t^3(2t+1)}{(2t^2+2t+1)(4t^2+3t+2)},\\
F(t)-U_5(t)&=\frac{t^2(2t-1)(2t+1)}{(2t^2+2t+1)(5t^2+4t+3)}.
\end{aligned}
\]
All three differences are strictly positive when \(t>1/2\). Since \(\lambda_m(t)\le U_m(t)\), this proves that no smaller wheel shares the six-rim formula on the indicated open interval. This finishes the theorem. \(\square\)

## Verification

The bundled `check_wheel_exact.py` uses only standard-library rational arithmetic. It checks 520 pairs \((m,t)\) in the theorem's range (including large rim counts), verifies both column norms of the explicit projection, constructs the five-entry sign vector, checks its cyclic second-difference coefficients, and checks the convex-dual cancellation. It also checks 30 smaller-wheel explicit comparisons. The bundled `check_wheel_unrestricted_lp.py` independently optimizes over **all** projection matrices (no symmetry restriction) in 20 cases using SciPy's linear-programming solver. Both completed successfully on the packaged code. The uniform proof is algebraic and does not depend on extrapolating these finite checks.

To reproduce: run `python check_wheel_exact.py`; optionally, with NumPy and SciPy installed, run `python check_wheel_unrestricted_lp.py`.

## Relationship to prior work

The transportation-cost quotient and weighted-edge framework are described by Ostrovska and Ostrovskii (2019). Dilworth, Kutzarova and Ostrovskii (2018, 2023) develop cycle-space methods and averaging invariant projections, the latter focusing on tori and Hamming graphs. The previously known **unit-weight wheel constants** are treated as a boundary case here; in particular this theorem does not claim the value \(\lambda_m(1)=9/5\) for \(m\ge6\) as independently new. The new result is the exact positive-length interval, its radical sharp boundary, and the sharp six-rim stabilization under the coupled edge-weight deformation. The general averaging method alone does not yield the dual sign-vector inequality (4) or determine the threshold.

## Limitations

The formula concerns the minimum norm of projections **onto the edge cycle space**; it is not an assertion about the quotient transportation-cost space's projection constant. The continuation of the true optimal norm for \(t\ge3/2\) is not determined here. The strict inequality beyond \(t_*\) is established only for \(t<3/2\). A bibliographically unindexed equivalent weighted-wheel computation cannot be excluded by search alone. No independent scientific audit is claimed.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, first public arXiv version July 10, 2018, arXiv:1807.03814, https://arxiv.org/abs/1807.03814.
2. S. Ostrovska and M. I. Ostrovskii, *On relations between transportation cost spaces and \(\ell_1\)*, first public arXiv version October 8, 2019, arXiv:1910.03625, https://arxiv.org/abs/1910.03625.
3. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, first public arXiv version May 21, 2023, arXiv:2305.12582, https://arxiv.org/abs/2305.12582.
