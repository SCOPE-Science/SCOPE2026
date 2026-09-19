# Exact three-consecutive-derivative threshold for bounded-inner-diameter domains

## Statement

For a plane domain \(\Omega\), let \(d_\Omega\) denote its interior path metric. For a nonempty set
\(S\subseteq \mathbb N_0\), write \(\mathcal R(S)\) for the property that every unbounded holomorphic
function \(f\) on \(\Omega\) admits a sequence \(z_j\in\Omega\) such that
\[
   |f^{(k)}(z_j)|\longrightarrow\infty\qquad\text{for every }k\in S,
\]
where \(f^{(0)}=f\).

**Theorem.** The following are equivalent for every nonempty \(S\subseteq\mathbb N_0\).

1. Every simply connected plane domain of finite interior-path diameter has property \(\mathcal R(S)\).
2. \(S\) is contained in three consecutive integers:
   \[
      S\subseteq\{a,a+1,a+2\}
   \]
   for some \(a\ge0\).

Equivalently, finite interior-path diameter has an exact universal derivative-span threshold of two.

The negative direction is supplied by the stronger pairwise statement: for every \(0\le a<b\) with
\(b-a\ge3\), there are a simply connected plane domain \(\Omega\) of finite interior-path diameter and
an unbounded holomorphic \(F\) on \(\Omega\) for which
\[
   \sup_{z\in\Omega}\min\{|F^{(a)}(z)|,\ |F^{(b)}(z)|\}<\infty.
\]

## Context

MacMahon, arXiv:2609.20607, proved that a simply connected domain has finite interior-path diameter
if and only if it belongs to \(\mathrm{Rubel}_0(1)\), and in fact if and only if it belongs to
\(\mathrm{Rubel}_0(2)\). The same paper constructed a finite-inner-diameter cusp and an unbounded
holomorphic function for which \(f\) and \(f^{(3)}\) never become simultaneously large, proving
\(\mathrm{Rubel}_0(1)\not\subset\mathrm{Rubel}_0(3)\). Its final section introduces derivative-set
versions of the Rubel property and asks for geometric descriptions of them.

The theorem above identifies exactly which derivative index sets are forced by the finite-inner-diameter
geometry. It also extends the \(\{0,3\}\) obstruction to every pair of derivative orders separated by at
least three.

## Proof

### 1. Three consecutive orders are always forced

Let \(\Omega\) be simply connected with
\[
   D:=\operatorname{diam}(\Omega,d_\Omega)<\infty,
\]
let \(S\subseteq\{a,a+1,a+2\}\), and let \(f\) be unbounded and holomorphic on \(\Omega\).

First, \(f^{(a)}\) is unbounded. For \(a=0\) this is the hypothesis that \(f\) is unbounded.
For \(a\ge1\), if \(f^{(a)}\) were bounded, then for a fixed \(z_0\in\Omega\) and any
\(z\in\Omega\), integration along rectifiable paths of length arbitrarily close to
\(d_\Omega(z_0,z)\le D\) would give
\[
 |f^{(a-1)}(z)-f^{(a-1)}(z_0)|
 \le D\,\|f^{(a)}\|_\infty.
\]
Thus \(f^{(a-1)}\) would be bounded. Iterating downward would make \(f\) bounded, a contradiction.

Set \(h=f^{(a)}\). By MacMahon's \(\mathrm{Rubel}_0(2)\) characterization, finite interior-path
diameter implies that every unbounded holomorphic function on \(\Omega\) has a sequence on which the
function and its first two derivatives all diverge in modulus. Applied to \(h\), there is a sequence
\(z_j\) such that
\[
 |f^{(a)}(z_j)|,\quad |f^{(a+1)}(z_j)|,\quad |f^{(a+2)}(z_j)|
 \longrightarrow\infty.
\]
Hence all derivative orders in \(S\) diverge along the same sequence.

### 2. A pair with gap at least three can always be obstructed

Fix \(0\le a<b\) and put \(m=b-a\ge3\). Tile \([0,1)\) by
\[
 I_j=[t_j,t_{j+1}],\qquad
 t_j=1-\frac1j,\qquad
 \ell_j=t_{j+1}-t_j=\frac1{j(j+1)}.
\]
On \(I_j\) let
\[
 u_j(x)=\frac{4(x-t_j)(t_{j+1}-x)}{\ell_j^2},
\]
so \(0\le u_j\le1\), its maximum is one, and \(u_j^{(m)}\equiv0\) because \(m\ge3\).

Choose a smooth step \(\eta\) with \(0\le\eta\le1\), \(\eta=0\) on
\(( -\infty,1/3]\), and \(\eta=1\) on \([2/3,\infty)\). Put
\[
 A_j=j^{a+1},\qquad
 0<\delta_j\le \min\!\left(\frac{\ell_j}{8},
                  \frac{\ell_j}{8A_j}\right),
\]
and define on \(I_j\)
\[
 h(x)=A_j u_j(x)
 \eta\!\left(\frac{x-t_j}{\delta_j}\right)
 \eta\!\left(\frac{t_{j+1}-x}{\delta_j}\right).
\]
Because the cutoff is identically zero near each endpoint, the pieces fit to a \(C^\infty\) function
on \((0,1)\).

Where both cutoffs equal one, \(h=A_j u_j\), hence \(h^{(m)}=0\). If at least one cutoff is not one,
then \(x\) lies within \(\delta_j\) of an endpoint and
\[
 A_j u_j(x)\le \frac{4A_j\delta_j}{\ell_j}\le\frac12.
\]
Consequently
\[
   \min\{|h(x)|,\ |h^{(m)}(x)|\}\le\frac12
   \qquad (0<x<1).
\]

If \(a=0\), set \(H=h\). If \(a\ge1\), set
\[
 H(x)=\frac1{(a-1)!}\int_0^x (x-t)^{a-1}h(t)\,dt.
\]
Then in either case
\[
 H^{(a)}=h,\qquad H^{(b)}=h^{(m)}.
\]
Moreover \(H\) is unbounded. For \(a=0\) this is immediate from
\(\max_{I_j}h=A_j\to\infty\). For \(a\ge1\), on the middle half of \(I_j\) the cutoffs equal one and
\(u_j\ge3/4\), so
\[
 \int_{I_j}(1-t)^{a-1}h(t)\,dt
 \ge c_a A_j\ell_j(j+1)^{-(a-1)}
 \ge c_a'\left(\frac{j}{j+1}\right)^a.
\]
The sum over \(j\) diverges, and therefore \(H(x)\to+\infty\) along \(x\uparrow1\).

Whitney's finite-order analytic approximation theorem gives a real-analytic \(g\) on \((0,1)\) such
that, for a fixed small \(\varepsilon>0\),
\[
   |g^{(r)}(x)-H^{(r)}(x)|<\varepsilon
   \qquad(0\le r\le b,\ 0<x<1).
\]
Thus \(g\) is unbounded and
\[
 \min\{|g^{(a)}(x)|,\ |g^{(b)}(x)|\}\le \frac12+\varepsilon
 \qquad(0<x<1).
\]

A real-analytic function on \((0,1)\) has a holomorphic continuation to some variable-width
neighborhood of the interval. By shrinking this neighborhood, choose a continuous
\(\rho:(0,1)\to(0,1]\) so that \(g\) is holomorphic on
\[
 \Omega=\{x+iy:0<x<1,\ |y|<\rho(x)\}
\]
and, for \(r=a,b\),
\[
 |g^{(r)}(x+iy)-g^{(r)}(x)|<\varepsilon.
\]
The domain \(\Omega\) deformation retracts vertically onto \((0,1)\), so it is simply connected.
Any two points can be joined by a vertical-horizontal-vertical path of length at most \(3\), hence
\(\operatorname{diam}(\Omega,d_\Omega)\le3\). Along the real axis \(g\) remains unbounded, while
throughout \(\Omega\)
\[
 \min\{|g^{(a)}(z)|,\ |g^{(b)}(z)|\}\le \frac12+2\varepsilon.
\]
This proves the pairwise obstruction.

If \(S\) is not contained in three consecutive integers, let \(a=\min S\). Then some
\(b\in S\) has \(b-a\ge3\). The pairwise construction prevents the simultaneous divergence of all
derivatives indexed by \(S\), completing the equivalence.

## Consequences

The threshold is genuinely about the geometry's universal guarantee, not about individual domains.
A disc, for example, has much stronger simultaneous-divergence behavior. What fails beyond span two
is the assertion that *every* simply connected finite-inner-diameter domain must force the chosen
derivatives to diverge together.

The construction also shows that the obstruction is not special to the pair \(\{0,3\}\): arbitrary
low derivative order and arbitrary gap at least three can be prescribed.

## Limitations

The theorem classifies derivative sets only for the universal statement over simply connected domains
of finite interior-path diameter. It does not characterize \(\mathcal R(S)\) for a fixed general domain,
does not optimize cusp regularity, and does not give quantitative growth rates for the divergent
derivatives. The counterexample domain depends on the obstructed derivative pair. No claim is made
about a single finite-inner-diameter domain simultaneously realizing every gap obstruction.

Originality is asserted only to the best of our knowledge. The most directly relevant source is very
recent. The full text of Rubel's 1984 paper was not independently inspected here, and it is the older
source most plausibly capable of containing an equivalent selected-derivative formulation.

## References

1. C. MacMahon, *On Simply Connected Domains Supporting an Unbounded Analytic Function with Bounded
   Derivative*, arXiv:2609.20607 (2026), https://arxiv.org/abs/2609.20607.
2. H. Whitney, *Analytic extensions of differentiable functions defined in closed sets*,
   Trans. Amer. Math. Soc. 36 (1934), 63-89, https://doi.org/10.2307/1989708.
3. J. D. Hinchliffe, *Unbounded analytic functions on plane domains*, Mathematika 50 (2003), 207-214,
   https://doi.org/10.1112/S002557930001490X.
4. A. Ya. Gordon, *Strong unboundedness of unbounded analytic functions*,
   Proc. Amer. Math. Soc. 122 (1994), 525-529,
   https://doi.org/10.1090/S0002-9939-1994-1204374-0.
5. L. A. Rubel, *Unbounded analytic functions and their derivatives on plane domains*,
   Bull. Inst. Math. Acad. Sinica 12 (1984), 363-377.
