# Sharp linear collapse and dimension-one degeneration of a tent map with memory

## Finding

For the two-dimensional symmetric tent map with memory, the compact full forward core approaches the graph of the ordinary tent map **at sharp linear speed** as memory vanishes. The same forward core has a quantitative fractal-dimension upper bound tending to one.

Specifically, with the definitions below, for every \(0<\delta<1/4\),
\[
1\le\dim_H K_\alpha\le\overline{\dim}_B K_\alpha
\le1+\frac{\log2}{\log((1-2\delta)/\delta)}<2.
\]
For every \(0<\delta\le1/64\),
\[
\frac{4\delta}{5\sqrt5}\le d_H(K_\alpha,\Gamma)\le80\delta.
\]
Consequently \(d_H(K_\alpha,\Gamma)=\Theta(1-\alpha)\), and both indicated dimensions converge to one as \(\alpha\uparrow1\).

## Assumptions and scope

Let \(Q=[0,1]^2\), \(\tau(t)=2\min(t,1-t)\) for \(t\in[0,1]\), and \(\alpha=1-\delta\) with \(0<\delta<1/4\). Define the continuous, generally noninvertible map
\[
G_\alpha(x,y)=(y,\tau(\delta x+(1-\delta)y)),
\quad K_\alpha=\bigcap_{n=0}^{\infty}G_\alpha^n(Q).
\]
The comparison set is \(\Gamma=\{(t,\tau(t)):0\le t\le1\}\). It equals \(K_1\). Distances are Euclidean; \(d_H\) denotes Hausdorff distance of nonempty compact subsets of \(Q\). The dimensions are Hausdorff and upper Minkowski/upper box dimensions of **the forward core**. We make no identification of this set with the support of any particular stationary probability.

The sets \(G_\alpha^n(Q)\) are nested nonempty compact connected sets. Both \((0,0)\) and \((2/3,2/3)\) are fixed by \(G_\alpha\), hence lie in their intersection. Thus \(K_\alpha\) is a nondegenerate continuum and \(\dim_H K_\alpha\ge1\).

## Proof

### 1. Upper box-dimension estimate

Each inverse-branch itinerary of length \(n\) is cut out from \(Q\) by finitely many affine half-plane inequalities, hence is convex. There are at most \(2^n\) such domains. On each of them the iterate is affine with derivative a product of the matrices
\[
A_s=\begin{pmatrix}0&1\\2s\delta&2s(1-\delta)\end{pmatrix},
\qquad s\in\{-1,+1\}.
\]
The cone \(\mathcal C=\{(u,v):|u|\le|v|\}\) is forward invariant: if \((u,v)\in\mathcal C\), its image \((u',v')\) satisfies
\[
|v'|\ge 2(1-2\delta)|v|\ge|u'|.
\]
In particular, the image of \((0,1)\) under any derivative product of length \(n\) has second-coordinate magnitude at least \([2(1-2\delta)]^n\). Therefore the largest singular value of the product is at least this quantity. As the determinant has absolute value \((2\delta)^n\), its smaller singular value is no larger than
\[
q^n,\qquad q=\frac{\delta}{1-2\delta}<\frac12.
\]
The image of each convex itinerary polygon is inside \(Q\), so it has diameter at most \(\sqrt2\). Its width in its least-singular-value direction is at most \(\sqrt2q^n\), since the preimage polygon lies in \(Q\) and has diameter at most \(\sqrt2\). Such a set can be covered by at most \(Cq^{-n}\) Euclidean balls of radius \(q^n\), with an absolute constant \(C\) independent of the itinerary and \(n\). Since \(K_\alpha\subseteq G_\alpha^n(Q)\),
\[
N(K_\alpha,q^n)\le C(2/q)^n.
\]
The upper box-dimension definition yields
\[
\overline{\dim}_B K_\alpha\le
\frac{\log(2/q)}{\log(1/q)}
=1+\frac{\log2}{\log((1-2\delta)/\delta)}.
\]
This and the continuum lower bound establish the dimension statement, including its limit as \(\delta\downarrow0\).

### 2. One side of the Hausdorff bound

For any \((x,y)\in Q\), Lipschitz continuity of \(\tau\) gives
\[
|\tau((1-\delta)y+\delta x)-\tau(y)|\le2\delta.
\]
Thus \(G_\alpha(Q)\) is contained in the closed Euclidean \(2\delta\)-neighborhood of \(\Gamma\), and
\[
\sup_{z\in K_\alpha}\operatorname{dist}(z,\Gamma)\le2\delta.
\]

### 3. Sharp lower bound from a persistent two-cycle

Put
\[
a=\frac{2(1-2\delta)}{5-8\delta},
\qquad b=\frac{4(1-\delta)}{5-8\delta}.
\]
Direct substitution into the two affine branches of \(\tau\) shows that \(G_\alpha(a,b)=(b,a)\) and \(G_\alpha(b,a)=(a,b)\) for every \(0<\delta<1/4\). Therefore \((a,b)\in K_\alpha\). Also,
\[
b-\tau(a)=b-2a=\frac{4\delta}{5-8\delta}.
\]
The graph of a \(2\)-Lipschitz function has the distance inequality
\[
\operatorname{dist}((x,y),\Gamma)\ge\frac{|y-\tau(x)|}{\sqrt5},
\]
which follows by applying Cauchy--Schwarz to \(|y-\tau(x)|\le|y-\tau(t)|+2|t-x|\) for every \(t\). Hence
\[
d_H(K_\alpha,\Gamma)\ge\frac{4\delta}{(5-8\delta)\sqrt5}\ge\frac{4\delta}{5\sqrt5}.
\]

### 4. The reverse Hausdorff inclusion by uniform periodic shadowing

We now assume \(0<\delta\le1/64\). Choose
\[
m=\left\lfloor\log_2\frac1{16\delta}\right\rfloor\ge2.
\]
Then \(2^{-m}<32\delta\) and \(\delta(2^m+1)\le5/64<1/8\).

Every length-\(m\) monotonicity interval of \(\tau^m\) has length \(2^{-m}\) and maps linearly onto \([0,1]\). Its graph crosses the diagonal, so it contains a point \(x\) fixed by \(\tau^m\). These periodic points form a \(2^{-m}\)-net of \([0,1]\). Apart from the zero fixed point, every such orbit \((x_j^0)_{j\in\mathbb Z/m\mathbb Z}\) lies strictly in \((0,1)\). Every coordinate is a rational with odd denominator at most \(2^m+1\): on the corresponding branch, the equation \(\tau^m(x)=x\) has the form \(\pm2^m x+k=x\) for an integer \(k\). Consequently each coordinate lies at distance at least \(1/[2(2^m+1)]\) from the folding point \(1/2\), and at least \(1/(2^m+1)\) from \(0\) and \(1\).

Fix one nonzero periodic tent orbit, and write its branch formula as
\[
x_{j+1}^0=c_j+2s_j x_j^0,
\qquad(s_j,c_j)\in\{(1,0),(-1,2)\}.
\]
On the finite-dimensional sup-norm space of cyclic sequences \(z=(z_j)_{j\in\mathbb Z/m\mathbb Z}\), define
\[
(\Phi_\delta z)_j=
\frac{(z_{j+1}-c_j)/(2s_j)-\delta z_{j-1}}{1-\delta}.
\]
Its contraction factor is \((1/2+\delta)/(1-\delta)<1\). The unique fixed sequence \(z^\delta\) obeys
\[
\|z^\delta-x^0\|_\infty
\le\frac{2\delta}{1-4\delta},
\]
because \(\|\Phi_\delta x^0-x^0\|_\infty\le\delta/(1-\delta)\). Each weighted input \((1-\delta)z_j^\delta+\delta z_{j-1}^\delta\) differs from \(x_j^0\) by at most \(2\delta/(1-4\delta)+\delta<4\delta\). Our choice of \(m\) ensures this is smaller than the distance to \(1/2\); the same bounds keep the sequence coordinates strictly in \((0,1)\). Thus the branch labels remain valid and
\[
z_{j+1}^\delta=
\tau((1-\delta)z_j^\delta+\delta z_{j-1}^\delta).
\]
Therefore \((z_{j-1}^\delta,z_j^\delta)\) belongs to a genuine periodic orbit of \(G_\alpha\), hence lies in \(K_\alpha\). The zero tent orbit persists exactly as \((0,0)\).

Given any \((t,\tau(t))\in\Gamma\), select an above tent period-\(m\) point \(x\) with \(|x-t|\le2^{-m}\). Its perturbed periodic orbit has a point within Euclidean distance \(\sqrt2\,2\delta/(1-4\delta)\) of \((x,\tau(x))\). Therefore
\[
\begin{aligned}
\operatorname{dist}((t,\tau(t)),K_\alpha)
&\le\sqrt5\,2^{-m}+\frac{2\sqrt2\,\delta}{1-4\delta}\\
&<\left(32\sqrt5+\frac{32\sqrt2}{15}\right)\delta
<80\delta.
\end{aligned}
\]
This establishes the reverse inclusion and finishes the sharp linear Hausdorff bound.

## Verification

The accompanying `verify.py` carries out exact rational checks of all monotonicity-cylinder periodic points and their perturbed cycles for \(\delta\in\{1/64,1/128,1/256,1/512,1/1024,1/2048\}\), including the branch-validity inequalities and the exact two-cycle formulas. It checks the unstable cone estimate over finite sign itineraries. Its deterministic output is `VERIFY_OK 246`. All infinite claims are established by the proof above, not the finite checks.

## Relationship to prior work

Góra--Boyarsky--Li (2016) establish existence of a singular Sinai--Ruelle--Bowen measure for this map when \(3/4<\alpha<1\), with conditional absolute continuity in unstable directions. Their full manuscript studies invariant probabilities and unstable/stable foliations. The present statement is instead about the **full compact forward core** and quantifies both its approach to the zero-memory graph and the collapse of an upper bound on its fractal dimension. The earlier map-with-memory paper treats the complementary parameter range. Neither source's existing qualitative invariant-measure assertions imply the stated sharp Hausdorff order or the explicit all-parameter upper box bound without additional work.

## Limitations

The box-dimension estimate is an upper bound, not an exact dimension formula for fixed \(\alpha\). The Hausdorff-order result is proved for \(\delta\le1/64\), although the lower bound holds throughout \((0,1/4)\). The forward core can properly contain the support of an individual invariant measure; no equality with the physical SRB support is claimed. The result neither identifies the limiting physical measures nor proves uniform dynamical conjugacy across parameters.

## References

1. P. Góra, A. Boyarsky, and Z. Li, *Singular SRB measures for a non 1--1 map of the unit square*, arXiv:1607.01658, first public version July 6, 2016; *Journal of Statistical Physics* 165 (2016), 409--433, DOI:10.1007/s10955-016-1620-y. Author-accessible full text: https://mypage.concordia.ca/mathstat/pgora/G-map/Singular_SRB_Above075_6.pdf .
2. P. Góra, A. Boyarsky, Z. Li, and H. Proppe, *Statistical and Deterministic Dynamics of Maps with Memory*, arXiv:1604.06991, first public version April 24, 2016.
