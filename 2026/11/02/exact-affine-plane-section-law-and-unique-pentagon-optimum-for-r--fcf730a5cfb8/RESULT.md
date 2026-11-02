# Exact affine-plane section law and unique pentagon optimum for right equilateral triangular prisms

## Finding
For every \(h>0\), let \(P_h\) be the Euclidean right triangular prism whose equatorial vertices are
\[v_j=(\cos(2\pi j/3),\sin(2\pi j/3)),\quad j=0,1,2,\]
and whose three vertical edges join \((v_j,-h)\) and \((v_j,h)\). The equilateral base has circumradius one and each vertical edge length \(2h\).

Choose an unoriented affine plane from invariant rigid-motion measure, conditioned to meet \(P_h\), and let \(N_h\) be the number of vertices of its section. Put
\[c=\frac{3\sqrt3}{4},\qquad S(h)=\sqrt{4h^2+3},\]
\[\Psi(h)=\sqrt3\arctan\frac{3}{4h}+2S(h)\arctan\frac{2h}{\sqrt3 S(h)}+\frac{\pi h}{3}-\frac{\pi S(h)}{2}.\]
Then the full section-type distribution is
\[\begin{aligned}
p_5(h)&=\mathbb P(N_h=5)=\frac{3\Psi(h)}{\pi(h+c)},\\
p_3(h)&=\mathbb P(N_h=3)=4+p_5(h)-\frac{3(h+\sqrt3)}{h+c},\\
p_4(h)&=\mathbb P(N_h=4)=\frac{3(h+\sqrt3)}{h+c}-3-2p_5(h).
\end{aligned}\]
There are no other section types except on a measure-zero set of tangent/vertex planes.

The function \(p_5\) is strictly increasing then strictly decreasing, with a unique maximum at the positive solution of
\[(h+c)\Psi'(h)=\Psi(h).\]
In particular,
\[h_*=0.4095226703062659704\ldots,\qquad \max_{h>0}p_5(h)=0.1126501962109488213\ldots.\]
The regular-faced prism, with equal horizontal and vertical edge lengths, has \(h=\sqrt3/2\), and is not the optimizer. The endpoints satisfy
\[p_5(h)\sim\frac{4h}{3\sqrt3}\quad(h\downarrow0),\qquad p_5(h)\sim\frac{3(3\sqrt3-\pi)}{8\pi h^2}\quad(h\to\infty).\]

## Assumptions and scope
All parameters satisfy \(h>0\). A plane is represented by \(\{x:u\cdot x=t\}\), where \(u\in S^2\) and \(t\in\mathbb R\), identifying \((u,t)\) with \((-u,-t)\). The measure is the restriction of \(d\sigma(u)\,dt\) to planes meeting \(P_h\), normalized to probability. Equivalently, the normal direction has probability proportional to the directional width and, given the normal, the offset is uniform in the support interval. This is **not** the model in which directions are sampled uniformly and every direction is assigned equal mass after conditioning the offset.

All assertions about the section polygon hold outside the null set of planes through a vertex or containing an edge. The unit base circumradius is a similarity normalization; for base circumradius \(R>0\), replace \(h\) throughout by the physical half-height divided by \(R\).

## Proof
**1. Width normalizer and mean section count.** For a unit normal \(u=(u_x,u_y,u_z)\), write \(a_j=(u_x,u_y)\cdot v_j\), and let \(a_-\) and \(a_+\) be the least and greatest \(a_j\). The offset interval meeting the prism is \([a_--h|u_z|,a_++h|u_z|]\); its length is
\[w_h(u)=a_+-a_-+2h|u_z|.\]
Spherical averaging gives
\[\overline w_h=\frac1{4\pi}\int_{S^2}w_h(u)\,d\sigma(u)=h+\frac{3\sqrt3}{4}=h+c.\]
Indeed, the planar equilateral base contributes \(3\sqrt3/4\), obtained by integrating its projected range over the six symmetry sectors; the vertical segment contributes \(2h\mathbb E|u_z|=h\). A generic section vertex lies on precisely one prism edge. Integrating its crossing-offset interval, then using \(\mathbb E|u\cdot e|=|e|/2\), yields
\[\mathbb E N_h=\frac{\sum_{e\text{ edge}}|e|}{2\overline w_h}=\frac{6\sqrt3+6h}{2(h+c)}=\frac{3(h+\sqrt3)}{h+c}.\]
This counts six horizontal edges of length \(\sqrt3\) and three vertical edges of length \(2h\).

**2. Exactly which offsets give a pentagon.** By symmetry take \(u_z\ge0\) and sort the planar vertex projections as \(a_1<a_2<a_3\). Put \(b=h u_z\). The two triangular caps are intersected in line segments simultaneously only when
\[a_1+b<t<a_3-b.\]
Within this interval the first and third vertical edges cannot be cut. A pentagon occurs precisely when the middle vertical edge is also cut, i.e. \(a_2-b<t<a_2+b\). Thus the total offset length giving a pentagon is
\[\begin{aligned}
L_5(u)&=\Bigl[\min(a_3-b,a_2+b)-\max(a_1+b,a_2-b)\Bigr]_+\\
&=[a_3-a_1-2b]_+-[a_2-a_1-2b]_+-[a_3-a_2-2b]_+.
\end{aligned}\]
Here \([z]_+=\max(z,0)\). A cap intersects in either zero or two horizontal edges, while the remaining vertical crossings show that the only possible generic polygon sizes are three, four and five.

**3. Integrate the pentagon offsets exactly.** Parametrize the northern unit hemisphere by
\[u=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta),\quad 0\le\theta\le\pi/2.\]
Within one of the six symmetry sectors \(0\le\phi\le\pi/3\), the three gap coefficients (with the common factor \(\sin\theta\) suppressed) are
\[R(\phi)=\sqrt3\cos(\phi-\pi/6),\quad G_1(\phi)=\sqrt3\sin\phi,\quad G_2(\phi)=\sqrt3\cos(\phi+\pi/6).\]
The elementary polar identity, for \(k\ge0\), is
\[\int_0^{\pi/2}[k\sin\theta-2h\cos\theta]_+\sin\theta\,d\theta=\frac{k}{2}\arctan\frac{k}{2h}.\]
Consequently, after exploiting the sixfold symmetry and normalization by \(\overline w_h\),
\[p_5(h)=\frac{6}{4\pi(h+c)}\int_0^{\pi/3}\left[R\arctan\frac R{2h}-G_1\arctan\frac{G_1}{2h}-G_2\arctan\frac{G_2}{2h}\right]d\phi.\]
Set \(t=2h\) and define
\[F_t(\beta)=\sqrt3\sin\beta\arctan\frac{\sqrt3\cos\beta}{t}+\sqrt{t^2+3}\arctan\left(\frac{t\tan\beta}{\sqrt{t^2+3}}\right)-t\beta\]
for \(0\le\beta<\pi/2\), continuously extended to \(\beta=\pi/2\) by \(F_t(\pi/2)=\pi(\sqrt{t^2+3}-t)/2\). Direct differentiation gives
\[F_t'(\beta)=\sqrt3\cos\beta\arctan\frac{\sqrt3\cos\beta}{t}.\]
The three sector integrals therefore combine to \(4F_t(\pi/6)-2F_t(\pi/2)\), so
\[p_5(h)=\frac{3}{\pi(h+c)}\left[2F_{2h}(\pi/6)-F_{2h}(\pi/2)\right]=\frac{3\Psi(h)}{\pi(h+c)}.\]
Together with the mean count and \(p_3+p_4+p_5=1\), this proves the three stated probabilities.

**4. Unique global pentagon optimum.** To establish uniqueness rather than infer it from a numerical graph, let
\[Q(t)=2F_t(\pi/6)-F_t(\pi/2),\qquad v_t(x)=\frac{3\cos^2x}{t^2+3\cos^2x},\quad t>0,\]
and define \(A(t)=\int_{\pi/6}^{\pi/2}v_t(x)\,dx\), \(B(t)=\int_0^{\pi/6}v_t(x)\,dx\). Differentiating under the integral gives
\[Q'(t)=A(t)-B(t).\]
For any \(t>0\), the logarithmic derivative \(\partial_t\log v_t(x)=-2t/(t^2+3\cos^2x)\) decreases strictly in \(x\in[0,\pi/2)\). Hence \(A'/A<B'/B<0\), and \(A/B\) is strictly decreasing. At \(t\downarrow0\), \(A/B\to2\); as \(t\to\infty\), the ratio tends to
\[\frac{\int_{\pi/6}^{\pi/2}\cos^2x\,dx}{\int_0^{\pi/6}\cos^2x\,dx}<1.\]
Thus \(Q\) increases to one unique maximum and then decreases. Moreover, while \(Q'\ge0\) one has \(A\ge B\), and therefore
\[Q''=A'-B'<0\]
because \(-A'/A>-B'/B>0\) and \(A\ge B\).
Now \(Q(0)=0\), \(Q'(0+)=\pi/6\), and \(Q(t)>0\) for \(t>0\). Writing \(\Psi(h)=Q(2h)\), the sign of \(p_5'(h)\) is the sign of
\[H(h)=(h+c)\Psi'(h)-\Psi(h).\]
On the interval where \(\Psi'\ge0\), \(H'(h)=(h+c)\Psi''(h)<0\). Also \(H(0+)=c\pi/3>0\), while at the unique zero of \(\Psi'\), \(H=-\Psi<0\). After that zero, \(H<0\) because \(\Psi'<0\) and \(\Psi>0\). There is exactly one zero of \(H\), and it is a strict global maximizer of \(p_5\).
For numerical evaluation one may use the exact elementary derivative
\[\Psi'(h)=\frac\pi3-\frac{2h}{S(h)}\left(\pi-4\arctan\frac{2h}{\sqrt3 S(h)}\right).\]
The unique root lies between \(0.40952\) and \(0.40953\); the decimals above are numerical evaluations, not additional exact claims.

**5. Aspect-ratio limits.** The previous integrals give \(Q(t)\sim (\pi/6)t\) as \(t\downarrow0\). As \(t\to\infty\),
\[Q'(t)\sim\frac{\pi-3\sqrt3}{4t^2},\qquad Q(t)\sim\frac{3\sqrt3-\pi}{4t},\]
using \(Q(\infty)=0\). Substitute \(t=2h\) in \(p_5=3Q(2h)/(\pi(h+c))\) to obtain both sharp limits.

## Verification
The included standalone `verify_prism.py` uses only the Python standard library. It compares the closed formula to a direct two-dimensional angular integration of the geometric overlap interval, tests the full side-count distribution by random unit normals and conditional offsets with the correct width weights, checks the closed-derivative sign bracket and confirms the sharp aspect-ratio coefficients. Run `python verify_prism.py` after extracting the embedded files. Its finite checks are diagnostic only; the proof above establishes the statements for every \(h>0\).

## Relationship to prior work
Brandenburg, De Loera and Meroni develop slicing-chamber decompositions and optimize individual affine sections; their theorems concern the combinatorial types and metric optimization of sections, not the invariant probability weights of the three polygonal types of a triangular prism. Van der Jagt, Jongbloed and Vittorietti formalize isotropic uniformly random hyperplanes and study densities of section volumes, not this discrete section-face-count law. In particular their directional-width weighting agrees with the measure fixed here.

An earlier stereology paper of Ohser and Mücklich studies regular-prism particle size/shape distributions and estimates stereological kernels by simulation. Its full text was not accessible in this comparison, so historical priority for the specific probability law is not exhaustively resolved. Konstantinova and Shchur study numerical angle distributions for sections including triangular prisms; their full article was also not inspected, and that work is treated as a priority risk rather than as proof of non-coverage. Distinct triangular-bipyramid and box section laws concern different polyhedra and cannot directly imply the formula here.

## Limitations
The exact statements hold only for **right equilateral triangular prisms** and the specified invariant affine-plane distribution. The unique optimizer is within this one-parameter similarity class, not an extremizer among all prisms or all polyhedra. The result does not determine section areas or angle distributions. Two potentially pertinent older/specialized stereology sources could not be materially inspected. The reviewed argument is mathematical and numerical, without independent external audit.

## References
1. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1 (first posted 2023-04-27), https://arxiv.org/abs/2304.14239.
2. T. van der Jagt, G. Jongbloed, M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, arXiv:2305.02864 (first posted 2023-05-04), https://arxiv.org/abs/2305.02864.
3. J. Ohser, F. Mücklich, *Stereology for some classes of polyhedrons*, Advances in Applied Probability **27** (1995), 384–396, https://doi.org/10.2307/1427832 (abstract inspected; full text unavailable).
4. E. P. Konstantinova, L. N. Shchur, *Algorithm for density of angle distribution in random sections of polyhedron*, Expert Systems with Applications **235** (2024), 121195, https://doi.org/10.1016/j.eswa.2023.121195 (abstract inspected; full text unavailable).
