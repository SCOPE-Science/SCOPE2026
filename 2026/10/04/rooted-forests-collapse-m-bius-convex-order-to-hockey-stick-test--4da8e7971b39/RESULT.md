# Rooted forests collapse Möbius convex order to hockey-stick tests with sharp TV control

## Finding

Let \(P\) be a finite poset whose Hasse diagram is a rooted forest when edges are directed upward: every nonminimal element \(v\) has a unique lower cover, denoted \(p(v)\). For probability measures \(\mu\) and \(\nu\) on \(P\),

\[
\mu\preceq_{\mathrm{conv}}\nu
\quad\Longleftrightarrow\quad
\mu\preceq_{\mathrm{HS}}\nu
\text{ and }
m_1[\mu]=m_1[\nu].
\]

Thus the chain characterization of Möbius-convex order extends to every rooted forest, including arbitrarily branching rooted trees.

For arbitrary probability measures on the same rooted forest,

\[
d_{\mathrm{TV}}(\mu,\nu)\le 2d_\zeta(\mu,\nu).
\]

The constant \(2\) is best possible. Under hockey-stick domination, the source identity
\(2d_\zeta(\mu,\nu)=m_2[\nu]-m_2[\mu]\) therefore yields the sharp consequence

\[
d_{\mathrm{TV}}(\mu,\nu)
\le
m_2[\nu]-m_2[\mu].
\]

## Assumptions and scope

The order is the ancestry order in a finite rooted forest. Distinct components are incomparable. A root is a minimal element. The poset integral \(I\), Möbius derivative \(D\), hockey-stick functions \(\Phi_x=I^2\mathbf 1_{\{x\}}\), moments \(m_k\), Möbius-convex order, hockey-stick order, and \(d_\zeta\) are those of Jaramillo--Sigarreta.

The result concerns finite rooted forests only. No claim is made for general finite posets having merge points, meaning elements with more than one lower cover.

## Proof

For a root \(r\), Möbius inversion gives \(Df(r)=f(r)\). If \(v\) is nonminimal, every element strictly below \(v\) lies below its unique parent \(p(v)\). Hence the interval Möbius coefficients into \(v\) vanish except at \(v\) and \(p(v)\), and

\[
Df(v)=f(v)-f(p(v)).
\]

Applying the same identity to \(Df\),

\[
D^2f(v)=Df(v)-Df(p(v))
\]

for every nonroot \(v\). Therefore, if \(f\) is Möbius convex, so that \(Df\) is increasing, then \(D^2f(v)\ge0\) at every nonroot.

The hockey-stick representation from Jaramillo--Sigarreta is

\[
f=\sum_{x\in P}D^2f(x)\Phi_x.
\]

Put \(h_x=\langle\nu-\mu,\Phi_x\rangle\). Hockey-stick domination is exactly \(h_x\ge0\) for all \(x\).

Let \(R\) be the set of roots. The first power function satisfies

\[
\varphi_1=I\mathbf 1=\sum_{r\in R}\Phi_r,
\]

because at a point \(z\) only the root of its component contributes, and \(\Phi_r(z)\) counts the vertices on the unique root-to-\(z\) chain. Consequently,

\[
m_1[\nu]-m_1[\mu]=\sum_{r\in R}h_r.
\]

Under hockey-stick domination and equality of first moments, all \(h_r\) are nonnegative and their sum is zero, hence every \(h_r=0\). For a Möbius-convex \(f\),

\[
\langle\nu-\mu,f\rangle
=
\sum_{r\in R}D^2f(r)h_r
+
\sum_{v\notin R}D^2f(v)h_v
\ge0.
\]

This proves the sufficient direction. Conversely, every \(\Phi_x\) is Möbius convex because \(D\Phi_x=I\mathbf 1_{\{x\}}\) is increasing, so Möbius-convex domination implies hockey-stick domination. Also \(D\varphi_1\) is the constant function \(1\), so both \(\varphi_1\) and \(-\varphi_1\) are Möbius convex. Testing both signs forces equality of first moments.

For total variation, take any subset \(A\subseteq P\) and put \(f=\mathbf 1_A\). At a root, \(Df\) lies in \(\{0,1\}\); at a nonroot,

\[
Df(v)=\mathbf 1_A(v)-\mathbf 1_A(p(v))\in\{-1,0,1\}.
\]

Hence \(\lVert D^2f\rVert_\infty\le2\). By the definition of \(d_\zeta\),

\[
|\mu(A)-\nu(A)|\le2d_\zeta(\mu,\nu).
\]

Taking the supremum over \(A\) proves the metric inequality.

Sharpness occurs on the three-element chain \(r<a<b\). Let

\[
\mu=\delta_a,
\qquad
\nu=\tfrac12\delta_r+\tfrac12\delta_b.
\]

Then \(d_{\mathrm{TV}}(\mu,\nu)=1\). The three hockey-stick expectation differences are \(0,0,\tfrac12\), so the hockey-stick representation gives \(d_\zeta(\mu,\nu)=\tfrac12\). Thus equality holds in the factor-\(2\) bound. The first moments agree, and the source identity under hockey-stick domination gives \(m_2[\nu]-m_2[\mu]=1\), so the moment-form coefficient is also sharp.

## Verification

The local Möbius formula and the indicator bound were replayed on several branching forests by direct construction of the zeta and Möbius matrices. Exhaustive checks over every indicator function on those examples confirmed \(\lVert D^2\mathbf 1_A\rVert_\infty\le2\).

For the sharp three-point example, direct matrix calculation gives hockey-stick differences \((0,0,\tfrac12)\), equal first moment, second-moment gap \(1\), total variation \(1\), and \(d_\zeta=\tfrac12\).

## Relationship to prior work

Jaramillo--Sigarreta introduce Möbius convexity, hockey-stick domination, the associated Zolotarev-type metric, rooted-tree constructions, and the exact second-moment identity under hockey-stick domination. Their convex-order equivalence is stated for chains; their general total-variation comparison carries a poset-size-dependent factor. The theorem above uses the unique-parent geometry of rooted forests to remove both restrictions: it extends the order equivalence to arbitrary branching without merges and gives a sharp dimension-free factor \(2\) for total variation.

Boutsikas--Vaggelatou study distances between convex-ordered real random variables. That one-dimensional theory motivates comparison of convex orders and probability metrics but does not contain the finite-poset rooted-forest statement.

A separate recent finite-poset probability literature studies ordinary stochastic orders and probabilistic powerdomains; those orders are not the Möbius-convex/hockey-stick orders considered here.

## Limitations

The proof uses the unique lower cover at every nonroot. At a merge point with several lower covers, \(D^2f\) need not be nonnegative pointwise even when \(Df\) is increasing, so the argument does not extend automatically to diamonds or general lattices.

The originality comparison cannot exclude an equivalent rooted-tree statement hidden under different terminology in older stochastic-order or incidence-algebra literature. The most directly relevant primary source was inspected in full; an older real-line metric paper was compared from its abstract and bibliographic record.

## References

1. Arturo Jaramillo and Saylé Sigarreta, *Hockey-Stick Domination and Distributional Comparison on Finite Posets*, arXiv:2606.12017v1, first public June 10, 2026.
2. Michael V. Boutsikas and Eutichia Vaggelatou, *On the distance between convex-ordered random variables, with applications*, Advances in Applied Probability 34 (2002), 349--374, DOI 10.1239/aap/1025131222.
3. Recent work on probabilistic powerdomains over finite posets, arXiv:2607.02231v1, used only as a broader-order comparison.
