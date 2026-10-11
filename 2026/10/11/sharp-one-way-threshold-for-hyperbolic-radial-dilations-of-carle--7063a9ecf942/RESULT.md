# Sharp one-way threshold for hyperbolic radial dilations of Carleson interpolation

## Finding

For every
\[
a>0,
\]
define
\[
D_a(0)=0
\]
and
\[
D_a(re^{i\theta})
=
\tanh\!\bigl(a\,\operatorname{artanh}r\bigr)e^{i\theta}.
\]
In hyperbolic polar coordinates
\[
R=2\operatorname{artanh}r,
\]
this is simply
\[
D_a(R,\theta)=(aR,\theta).
\]

Then
\[
D_a
\]
preserves every Carleson interpolating sequence in the forward direction exactly when
\[
a\ge1.
\]
Preservation in both directions holds exactly when
\[
a=1.
\]

Equivalently, for the multiplicative semigroup
\[
D_a\circ D_b=D_{ab},
\]
the intersection with the one-way continuous-preserver class is precisely
\[
\{D_a:a\ge1\},
\]
whereas the intersection with the bidirectional-preserver class is
\[
\{D_1\}.
\]

The recent source's smooth example
\[
z\longmapsto\frac{2z}{1+|z|^2}
\]
is exactly the member
\[
D_2.
\]
Thus that isolated strict-inclusion witness sits inside a complete one-parameter phase diagram.

## Assumptions and scope

A sequence in the unit disk is called Carleson interpolating when it is interpolating for
\[
H^\infty(\mathbb D).
\]
The pseudohyperbolic distance is
\[
\rho(z,w)
=
\left|
\frac{z-w}{1-\overline zw}
\right|,
\]
and the hyperbolic distance is normalized by
\[
d_{\mathbb D}(z,w)
=
2\operatorname{artanh}\rho(z,w).
\]

The proof uses Carleson's product-separation criterion and the two-point packet lemma appearing in the recent primary source.

The statement concerns this canonical hyperbolic radial-dilation semigroup. It does not classify arbitrary radial homeomorphisms of the disk.

## Proof

The maps satisfy
\[
D_a\circ D_b=D_{ab}
\]
and
\[
D_a^{-1}=D_{1/a}.
\]

Assume first that
\[
a\ge1.
\]
The hyperbolic metric in polar coordinates is
\[
d\ell^2
=
dR^2+\sinh^2R\,d\theta^2.
\]
At a point with target radius \(R\), the inverse map
\[
D_{1/a}(R,\theta)
=
(R/a,\theta)
\]
has radial stretch
\[
\frac1a
\]
and tangential stretch
\[
\frac{\sinh(R/a)}{\sinh R}.
\]
Since
\[
\sinh(ax)\ge a\sinh x
\qquad
(a\ge1,\ x\ge0),
\]
the tangential stretch is at most
\[
\frac1a.
\]
Therefore \(D_{1/a}\) is globally \(1/a\)-Lipschitz for the hyperbolic distance. Hence
\[
d_{\mathbb D}(D_a z,D_a w)
\ge
a\,d_{\mathbb D}(z,w).
\]

Because
\[
\rho(z,w)
=
\tanh\!\left(
\frac{d_{\mathbb D}(z,w)}2
\right),
\]
it follows that
\[
\rho(D_a z,D_a w)
\ge
\rho(z,w).
\]
Carleson's product-separation criterion says that an indexed sequence
\[
\Lambda=(\lambda_j)
\]
is interpolating exactly when
\[
\inf_j
\prod_{k\ne j}
\rho(\lambda_j,\lambda_k)>0.
\]
Every factor in every finite partial product can only increase under \(D_a\), and passage to the infinite products therefore preserves the positive lower bound. Thus every \(D_a\) with \(a\ge1\) preserves all interpolating sequences.

Now suppose
\[
0<a<1.
\]
Choose radii
\[
R_n\longrightarrow\infty
\]
so rapidly that, with
\[
r_n=\tanh(R_n/2),
\]
the boundary defects
\[
\delta_n=1-r_n
\]
satisfy
\[
\delta_{n+1}\le\frac14\delta_n.
\]
Fix \(c>0\). After discarding finitely many initial indices, choose
\[
\theta_n\in(0,\pi)
\]
by
\[
\sin(\theta_n/2)
=
\frac{c}{\sinh R_n}.
\]
Set
\[
z_n=r_n,
\qquad
w_n=r_ne^{i\theta_n}.
\]

For two points of common hyperbolic radius \(R\) and angular separation \(\theta\),
\[
\sinh\!\left(\frac{d_{\mathbb D}}2\right)
=
\sinh R\,\sin(\theta/2).
\]
Consequently
\[
\sinh\!\left(
\frac{d_{\mathbb D}(z_n,w_n)}2
\right)
=
c,
\]
so the within-packet pseudohyperbolic separation is a fixed positive constant.

The packets
\[
F_n=\{z_n,w_n\}
\]
have at most two points, fixed positive internal separation, and geometrically decreasing boundary depths. The packet lemma from the primary source therefore shows that
\[
\Lambda=\bigcup_nF_n
\]
is a Carleson interpolating sequence.

After applying \(D_a\), the two points in the \(n\)-th packet have common hyperbolic radius \(aR_n\) and the same angular separation. Hence
\[
\sinh\!\left(
\frac{
d_{\mathbb D}(D_a z_n,D_a w_n)
}{2}
\right)
=
c\,
\frac{\sinh(aR_n)}{\sinh R_n}.
\]
Since
\[
0<a<1,
\]
the quotient tends to zero exponentially. Thus
\[
\rho(D_a z_n,D_a w_n)\longrightarrow0.
\]
The image sequence is not pairwise separated and therefore is not interpolating.

This proves that forward preservation holds exactly for
\[
a\ge1.
\]

Finally, if
\[
a>1,
\]
then
\[
D_a^{-1}=D_{1/a}
\]
has parameter below one and fails forward preservation by the preceding construction. Hence \(D_a\) does not preserve interpolation equivalently in both directions. For
\[
a=1,
\]
the map is the identity. This proves the bidirectional classification.

## Verification

The recent primary source was inspected at Carleson's separation formulation, its two-point packet lemma, the complete one-way preservation theorem, and the explicit smooth example
\[
z\mapsto\frac{2z}{1+|z|^2}.
\]
That example is exactly \(D_2\), because
\[
\tanh(2\operatorname{artanh}r)
=
\frac{2r}{1+r^2}.
\]

The source computes the \(a=2\) hyperbolic stretch directly. The present calculation keeps the dilation parameter arbitrary and uses
\[
\sinh(ax)\ge a\sinh x
\]
to obtain the exact forward range.

For the failure range, the packet construction was checked against the hypotheses of the source lemma: every packet has two points, its internal separation is constant, and the common boundary depth can be chosen to decay by a fixed geometric factor.

The classical quasiconformal-preserver theorem of González and Nicolau was also inspected. It characterizes quasiconformal preservers by strong quasisymmetry of the boundary map. Except for \(a=1\), the maps \(D_a\) are not quasiconformal: their radial and tangential Euclidean stretch ratio becomes unbounded near the unit circle. Thus that theorem does not imply the present phase diagram.

No numerical experiment or finite enumeration is used.

## Relationship to prior work

The recent source characterizes arbitrary continuous one-way and bidirectional preservers. It also gives the single explicit radial example
\[
D_2(z)=\frac{2z}{1+|z|^2},
\]
showing that one-way preservation can hold without bidirectional preservation.

The present result classifies the entire canonical semigroup obtained by multiplying hyperbolic radius. It shows that the source example is not isolated: all expanding parameters
\[
a\ge1
\]
preserve interpolation forward, every contracting parameter
\[
0<a<1
\]
fails, and no nontrivial member is bidirectional.

González and Nicolau's earlier theorem concerns quasiconformal maps. The nontrivial \(D_a\) are outside that category, so the threshold here is genuinely a continuous non-quasiconformal phenomenon.

Targeted searches for hyperbolic radial dilations, the formula
\[
\tanh(a\operatorname{artanh}r),
\]
and one-way Carleson interpolation did not locate an implication-equivalent classification.

## Limitations

The theorem is a classification only inside the specific semigroup
\[
D_a(R,\theta)=(aR,\theta).
\]
It does not give a necessary and sufficient condition for a general radial homeomorphism
\[
(R,\theta)\mapsto(\Phi(R),\theta).
\]

For
\[
a>1,
\]
the maps preserve interpolation by hyperbolic expansion, but they are not uniformly continuous in the forward pseudohyperbolic direction and are not quasiconformal.

The counterexample for
\[
0<a<1
\]
establishes failure by a specially arranged interpolating packet sequence; it does not describe all sequences whose interpolation property is destroyed.

## References

1. J. Wu, *Characterizations and boundary regularity of continuous preservers of Carleson interpolating sequences*, arXiv:2609.32891v1, 2026.
2. M. J. González and A. Nicolau, *Quasiconformal mappings preserving interpolating sequences*, Annales Academiae Scientiarum Fennicae Mathematica 23 (1998), 283--290.
3. J. B. Garnett, *Bounded Analytic Functions*, revised first edition, Springer, 2007.
