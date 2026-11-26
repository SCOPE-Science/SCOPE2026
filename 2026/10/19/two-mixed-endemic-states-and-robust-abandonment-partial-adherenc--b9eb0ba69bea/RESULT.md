# An explicit basin separator between two endemic adherence outcomes

## Finding

For the rational parameter example below of the autonomous SIRS–replicator model, the lower of the two mixed endemic equilibria is a hyperbolic saddle. Its two unstable branches converge, respectively, to the endemic no-adherence and endemic partial-adherence sinks. Thus the saddle's local stable manifold separates their two basins in a neighborhood of the saddle. These connections and local separation persist under sufficiently small parameter perturbations. The statement is about where the unstable branches actually go, not just about the linear stability types of the three equilibria.

More explicitly, an invariant tube around the positive endemic response curve gives certified open sets of initial conditions in the two basins. Within the tube, adherence decreases monotonically to zero on the lower side of the saddle and increases monotonically to the upper mixed equilibrium on the upper side. No claim about the entire basin boundary is made.

## Model and parameter choice

Let \(S,I,R\ge0\), \(S+I+R=1\), and \(0\le x\le1\). The model is
\[
\begin{aligned}
\dot S&=\mu-\beta b(x)SI+\delta R-\mu S,\\
\dot I&=\beta b(x)SI-(\gamma+\mu)I,\\
\dot R&=\gamma I-(\mu+\delta)R,\\
\dot x&=h(x)\big[-c+a\xi\beta I(1-ex)+\kappa(2x-1)\big],\qquad
b(x)=(1-ax)(1-ex),\quad h(x)=\varepsilon x(1-x).
\end{aligned}
\]
Use the exact parameters
\[
(\mu,\delta,\gamma,\beta,a,e,\xi,c,\kappa,\varepsilon)
=\left(\frac1{10},\frac9{10},1,\frac{33}{10},\frac9{10},\frac1{10},\frac{800}{297},\frac{503}{300},1,\frac1{100}\right).
\]
For \(0\le x\le13/50\), the endemic response at fixed \(x\) is \(S_*(x)=1/[3b(x)]\), \(I_*(x)=R_*(x)=E(x)=(1-S_*(x))/2\). Define the behavioral response on this curve by
\[
G(x)=-c+8(1-x/10)E(x)+(2x-1)
=\frac{1440x^2-409x+10}{100(9x-10)}.
\]
The two roots are \(x_\pm=(409\pm\sqrt{109681})/2880\), with \(27/1000<x_-<28/1000\) and \(257/1000<x_+<258/1000\). The brackets follow by substitution into the numerator (signs \(+,-,-,+\) in increasing order). The denominator is strictly negative throughout the interval. Consequently \(G<0\) on \([0,x_-)\), \(G>0\) on \((x_-,x_+)\), and \(G'(x_-) >0>G'(x_+)\). Let \(p_0,p_-,p_+\) be the points on the endemic response curve with \(x=0,x_-,x_+\), respectively. In particular \(p_0\) has \(S=I=R=1/3\), not zero infection.

## Proof

### Hyperbolicity

At either mixed point put \(C=\beta bE\), \(A=1+C\), \(u=-\beta b'S_*E\), \(v=h\,8(1-x/10)\), and \(w=h(2-(4/5)E)\). In the coordinates \((S,I,x)\) the Jacobian and characteristic coefficients are
\[
J=\begin{pmatrix}-A&-2&u\\ C&0&-u\\0&v&w\end{pmatrix},\qquad
C_1=A-w,\quad C_2=2C-Aw+uv,\quad C_3=uv-2Cw=-2ChG'.
\]
Indeed, differentiating the fixed-\(x\) epidemic equations yields \(S_*'=u/C\) and \(E'=-u/(2C)\); the feedback derivative is then \(hG'=w+vE'\). On the interval of interest \(b>7/10\), \(E>1/4\), \(C>1/2\), \(A<3\), \(u,v>0\) at the mixed points, and \(0<w\le1/200\). These imply \(C_1,C_2>0\) and
\[
C_1 C_2-C_3=2AC-A^2w+Aw^2+uv(C-w)>1-9/200>0.
\]
The signs of \(G'\) give one eigenvalue in the open right half-plane at \(p_-\) and none at \(p_+\), by the cubic Routh test. Neither point has a purely imaginary or zero eigenvalue, since \(C_3\ne0\) and \(C_1C_2\ne C_3\). At \(p_0\), the epidemic block has negative trace and positive determinant, and the transverse eigenvalue is \(\varepsilon G(0)=-1/10000\). Thus \(p_0,p_+\) are sinks and \(p_-\) is a saddle with one-dimensional unstable manifold.

### Trapping tubes and their limits

Set \(D(x)=\beta b(x)\), \(C(x)=D(x)E(x)\), \(L(x)=8(1-x/10)\), and use the deviations \(y=I-E(x)\), \(z=R-E(x)\). Since \(\gamma=\mu+\delta=1\), the equations become
\[
\dot x=h(x)(G(x)+L(x)y),\qquad
\dot y=-D(x)(E(x)+y)(y+z)-E'(x)\dot x,\qquad
\dot z=y-z-E'(x)\dot x.
\]
Define \(r=(y^2+C(x)z^2)^{1/2}\). On either interval \(0<x<x_-\) or \(x_-<x<x_+\), consider the tube \(r\le |G(x)|/16\) in the biological state space. Because \(0<L\le8\), within the tube \(\dot x\) has the sign of \(G\) and
\[
\frac12 h|G|\le|\dot x|\le\frac32 h|G|\le \frac{3}{800}|G|.
\]

Here are uniform analytic bounds validating invariance. On \([0,13/50]\), one has
\[
\tfrac7{10}<b\le1,\quad |b'|\le1,\quad \tfrac12<C<2,\quad |C'|<2,\quad
D<4,\quad |E'|<\tfrac12,\quad |G'|<1,\quad |G|<\tfrac3{10}.
\]
For the first bounds use \(b=1-x+9x^2/100\), \(C=\beta(b-1/3)/2\), and \(E'=b'/(6b^2)\). For \(G'\) use \(8/5-(6/5)/(1-9x/10)^2\) with \(1-9x/10>3/4\), then use \(G(0)=-1/100\). Differentiating the norm gives
\[
\tfrac12\frac{d}{dt}r^2
=-Cy^2-Cz^2-Dy^2(y+z)-E'\dot x(y+Cz)+\tfrac12 C'\dot x z^2.
\]
In the tube, \(D(|y|+|z|)\le10r<3/16\). The first three terms are therefore at most \(-5r^2/16\); the remaining two are at most \((5/4)r|\dot x|+2r^2|\dot x|\). At \(r>0\), the speed bound yields
\[
\dot r\le -\tfrac3{10}r+\tfrac54|\dot x|.
\]
The same inequality holds for the upper right derivative at \(r=0\) by the deviation equations. On the tube wall \(r=|G|/16>0\), the outward derivative satisfies
\[
\frac{d}{dt}\big(r-|G|/16\big)
\le -\tfrac3{160}|G|+\big(\tfrac54+\tfrac1{16}\big)\tfrac3{800}|G|<0.
\]
Thus no trajectory starting in a tube can leave through its wall. The speed bound precludes reaching either forward endpoint in finite time (\(h=0\) at zero and \(G=0\) at \(x_+\), with smooth functions). Bounded monotone adherence then converges to zero in the lower tube and to \(x_+\) in the upper tube, since the lower speed bound is positive on any compact interior interval. In the upper tube \(r\to0\) by the wall bound. In the lower tube \(\dot x\to0\) by the speed bound and \(h(0)=0\); integrating the norm inequality gives \(r\to0\) as well. These limits prove the claimed convergence for the indicated initial conditions.

### Identification of both unstable branches

In each tube select starting points on the endemic response curve with adherence tending to \(x_-\) from that side. Fix an interior adherence slice on the same side and shift each trajectory's time origin to its unique crossing of the slice. The elapsed times from the chosen starting points to the slice tend to infinity: near \(x_-\) the upper speed bound is at most a constant times \(|x-x_-|\). The crossing points have a convergent subsequence in the compact slice. Continuous dependence gives a complete backward orbit from the limit point, within that tube for all finite negative times. Indeed the limiting orbit cannot reach a tube endpoint in finite backward time, by the same Lipschitz speed bounds, and for every finite interval the approximating orbits remain in the closed tube inequalities. Its backward adherence limit is \(x_-\), by the lower speed bound in the tube interior; then \(r\to0\) by the wall inequality. Thus it lies on the unstable manifold of \(p_-\). One orbit is on each side, giving both branches, and the tube convergence proves they go to the two different sinks.

For a hyperbolic saddle with a one-dimensional unstable direction, the local stable manifold has two sides. Points sufficiently close to the saddle on either side leave a local saddle neighborhood arbitrarily close to the corresponding unstable branch (the local saddle exit property, or the inclination lemma). Each branch has entered an open sink basin, so points on those sides belong to the corresponding basins after shrinking the neighborhood. For persistence, take a finite segment of each branch ending in a local attracting neighborhood of its sink. The equilibria and local unstable branches persist by hyperbolicity; continuous dependence keeps the two segments in the corresponding trapping neighborhoods at their endpoints for sufficiently small parameter changes. This preserves the asserted local separation. There is no claim that the full stable manifold is the entire global basin boundary.

## Reproducibility and relationship to previous work

The inequalities displayed above establish the invariant tubes and the two connections analytically; neither a small-parameter limit nor integration of a sample trajectory is the certificate. The existing `check.py` corroborates the equilibrium identities and strict local linear stability inequalities only. It does not check the new tube or connections.

Kumata, Ito and Yamamichi, *Voluntary nonpharmaceutical intervention as a feedback-evolving game*, [arXiv:2610.12519v1](https://arxiv.org/abs/2610.12519v1), introduce the model and equilibrium feedback. Their Fig. 3C illustrates the separation of no adherence and full adherence in numerical trajectories, not a saddle-to-sink connection theorem for two endemic sinks of which one has mixed adherence. The Resultary entry *Three is the sharp local-attractor capacity of a conformist behavioral SIRS model*, `2026/11/22/SCOPE-three-is-the-sharp-local-attractor-capacity-of-a-conformist-beha--862b1c9a80d4`, proves strict concavity on the positive endemic branch and gives a rational witness of the same local equilibrium pattern (with an additional disease-free sink). The mere mixed-state count and local bistability are not claimed as distinct results here. The present claim is the explicit orbit and basin-separation certificate for the specified parameters. It is a statement about a deterministic homogeneous model, not about actual interventions or populations.
