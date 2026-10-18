# A sharp period-four folding transition in a planar tent family

## Finding

Let \(\Omega=\{(x,y):0\le x\le2,\ 0\le y\le\min(x,2-x)\}\). For the two-dimensional expanding tent family
\[
\Phi_t(x,y)=\begin{cases}
t(x+y,x-y),&x\le1,\\
t(2-x+y,2-x-y),&x\ge1,
\end{cases}
\qquad \tau\le t\le1,
\]
where \(\tau=2^{-1/2}(1+\sqrt2)^{1/4}\), let \(\theta\) be the unique root in \((\tau,1)\) of
\[P(t)=4t^4-2t-1=0.\]
Then the number of distinct primitive period-four orbits, counted modulo cyclic rotation, is exactly
\[
N_4(t)=\begin{cases}
1,&\tau\le t<\theta,\\
2,&t=\theta,\\
3,&\theta<t\le1.
\end{cases}
\]
In fact \(0.9175<\theta<0.918\). For all \(t\in[\tau,1]\), there are exactly two fixed points and exactly one primitive period-two orbit, so
\[
\#\operatorname{Fix}(\Phi_t^4)=
\begin{cases}8,&\tau\le t<\theta,\\12,&t=\theta,\\16,&\theta<t\le1.\end{cases}
\]
The only primitive four-cycle before the threshold has cyclic branch itinerary \(0001\). Above the threshold two more four-cycles have itineraries \(0011\) and \(0111\). At the threshold the latter itineraries describe **one and the same** primitive four-cycle because the shared second point lies on the folding line \(x=1\). Every period-four orbit avoiding the fold is repelling: its four-step derivative is a scalar \(4t^4>1\) times an orthogonal matrix.

## Assumptions and scope

The domain is the *closed* triangle \(\Omega\), and \(t\in[\tau,1]\). The formula is continuous on its fold \(x=1\), since both branch formulas agree there. It maps \(\Omega\) into itself: each full branch maps its half-triangle onto \(\Omega\) at \(t=1\), and scaling about the origin by \(0<t\le1\) preserves the convex triangle. A periodic orbit is primitive period four if its least positive period is four. Two representations related by cyclic rotation count as one orbit. A point on \(x=1\) is admitted to **both** symbolic branches when enumerating itineraries, with no artificial double-counting of the actual geometric orbit. The symbol \(0\) means use the \(x\le1\) branch, and \(1\) means use the \(x\ge1\) branch. No statement is made here about prime periods exceeding four, global dynamics, or invariant densities.

## Proof

**1. Exhaustive affine returns.** Define
\[
A_0=t\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad b_0=\binom00,\qquad
A_1=t\begin{pmatrix}-1&1\\-1&-1\end{pmatrix},\quad b_1=t\binom22.
\]
For a finite word \(w=w_0\cdots w_{n-1}\), its *formal* return is \(z\mapsto M_wz+c_w\), obtained by composing \(z\mapsto A_{w_j}z+b_{w_j}\) in temporal order. Any actual periodic orbit with this itinerary necessarily solves \((I-M_w)z=c_w\). Every word of length four is a cyclic rotation of exactly one of the six binary necklaces \(0000,0001,0011,0101,0111,1111\). Their determinants \(\det(I-M_w)\), in that order, are
\[
\begin{gathered}
(2t^2-1)^2(2t^2+1)^2,\\
-(2t^2-1)(2t^2+1)(2t^2-2t+1)(2t^2+2t+1),\\
16t^8+1,\\
(2t^2-1)^2(2t^2+1)^2,\\
-(2t^2-1)(2t^2+1)(2t^2-2t+1)(2t^2+2t+1),\\
(2t^2-2t+1)^2(2t^2+2t+1)^2.
\end{gathered}
\]
Since \(t\ge\tau>1/\sqrt2\), none vanishes. Thus **each** necklace has at most one affine return candidate; this covers all possible period-four points, including crease points. It also precludes nonisolated families of period-dividing-four points.

**2. The two short periods.** The one-letter words yield exactly the fixed points
\[
(0,0),\qquad \left(\frac{2t(2t+1)}{2t^2+2t+1},\frac{2t}{2t^2+2t+1}\right).
\]
The only primitive two-cycle is given by the left-side starting point
\[
z_{01}(t)=\left(\frac{2t}{2t^2+1},\frac{2t}{2t^2+1}\right),
\]
which maps to the right-side point \((4t^2/(2t^2+1),0)\). The other two-letter necklaces give the fixed points already listed. The decisive left/right inequalities are strict because \(2t^2-1>0\) and \(2t^2-2t+1>0\). Therefore the four-letter necklaces \(0000\), \(1111\) and \(0101\) contribute only these shorter orbits.

**3. The three possible primitive four-cycles.** Solving the formal affine return for \(0001\), \(0011\), and \(0111\), respectively, gives the following first point of each cyclically represented orbit:
\[
\begin{aligned}
z_{0001}(t)&=\left(\frac{2t}{4t^4+1},\frac{2t}{4t^4+1}\right),\\
z_{0011}(t)&=\left(\frac{2t(8t^5-4t^4+1)}{16t^8+1},
\frac{2t(4t^4-2t+1)}{16t^8+1}\right),\\
z_{0111}(t)&=\left(\frac{2t}{2t^2+1},\frac{2t}{2t^2+2t+1}\right).
\end{aligned}
\]
All three points lie in \(\Omega\): each has nonnegative second coordinate and satisfies \(y\le x\), \(x+y\le2\). For the nontrivial \(0011\) case, these strict geometric inequalities follow from
\[
\begin{aligned}
y&=\frac{2t(4t^4-2t+1)}{16t^8+1}>0,\\
x-y&=\frac{4t^2(4t^4-4t^3+1)}{16t^8+1}>0,\\
2-x-y&=\frac{2(4t^4+4t^3+1)(4t^4-4t^3+2t^2-2t+1)}{16t^8+1}>0.
\end{aligned}
\]
The corresponding \(0111\) differences are \(y=2t/(2t^2+2t+1)\), \(x-y=4t^2/[(2t^2+1)(2t^2+2t+1)]\), and \(2-x-y=2(4t^4+2t^2+1)/[(2t^2+1)(2t^2+2t+1)]\), all positive. The \(0001\) seed lies on \(y=x\), with \(0<x<1\). The map-invariance of \(\Omega\) then puts each formal orbit's iterates in the triangle.

To test branch membership, write \(x_j\) for the first coordinate at time \(j\) along a formal word. For \(0001\) the three left-side differences \(x_j-1\) for \(j=0,1,2\) have strictly negative numerators, respectively \(-(4t^4-2t+1)\), \(-(2t^2-1)^2\), and \(-(4t^4-4t^3+1)\), over the common positive denominator \(4t^4+1\); the right-side difference at \(j=3\) is \((2t^2-1)(2t^2+1)/(4t^4+1)>0\). Therefore \(0001\) is always a strict primitive four-cycle.

For \(0011\), three of the four correct-side tests are always strict. Only the **second** point can violate the left-branch condition; its exact difference is
\[
x_1-1=-\frac{(2t^2-1)(2t^2-2t+1)P(t)}{16t^8+1}.
\]
For \(0111\), again all other tests are strict, but the second-point right-branch condition is
\[
x_1-1=\frac{P(t)}{(2t^2+1)(2t^2+2t+1)}.
\]
The three other first-coordinate branch tests for \\(0011\\), with \\(Q=16t^8+1\\), are
\[
\begin{aligned}
x_0-1&=-\frac{(2t^2-1)(2t^2-2t+1)(4t^4+4t^3-1)}{Q}<0,\\
x_2-1&=\frac{(2t^2-1)(2t^2+1)(4t^4-4t^3+1)}{Q}>0,\\
x_3-1&=\frac{(2t^2-1)(2t^2+1)(4t^4-2t+1)}{Q}>0.
\end{aligned}
\]
For \\(0111\\), the other three tests are
\[
\begin{aligned}
x_0-1&=-\frac{2t^2-2t+1}{2t^2+1}<0,\\
x_2-1&=\frac{2t^2-1}{2t^2+2t+1}>0,\\
x_3-1&=\frac{4t^4+4t^3-1}{(2t^2+1)(2t^2+2t+1)}>0.
\end{aligned}
\]
Thus both of these words are realized precisely when \\(P(t)\\ge0\\).

The missing inequalities are elementary: \(4t^4+4t^3-1>0\), \(4t^4-2t+1>0\) on the parameter interval, and \(4t^4-4t^3+1=1-4t^3(1-t)\ge37/64>0\) on \([0,1]\). In particular
\[
4t^4-4t^3+2t^2-2t+1=(2t^2-t)^2+(t-1)^2>0
\]
for \(t\in[\tau,1]\). All branch-sign factors above follow by exact multiplication of the two stated affine matrices; the accompanying rational verifier also checks the seed return equations and the switch identities at five independent rational parameters.

**4. Threshold and collision.** The polynomial \(P\) is strictly increasing on \([\tau,1]\), since \(P'(t)=16t^3-2>0\). Moreover \(P(\tau)=\sqrt2-2\tau<0\), whereas \(P(1)=1>0\). Therefore \(P\) has a unique root \(\theta\) in the parameter interval. Rational evaluation yields \(P(9175/10000)<0<P(918/1000)\).

At the root, the difference of the two displayed new seed points factors as
\[
\begin{aligned}
\bigl(z_{0011}-z_{0111}\bigr)_x
&=-\frac{4t^3(2t^2-2t+1)P(t)}{(2t^2+1)(16t^8+1)},\\
\bigl(z_{0011}-z_{0111}\bigr)_y
&=-\frac{4t^3(2t^2-1)P(t)}{(16t^8+1)(2t^2+2t+1)}.
\end{aligned}
\]
Hence they coincide **exactly** when \(t=\theta\). Their second point lies on \(x=1\), so both symbolic descriptions are valid for the same geometric orbit. The orbit is primitive: its initial point has \(x<1\), while its second iterate has \(x>1\), excluding period one or two. For \(t>\theta\), both seeds are different and the strict labels persist; for \(t<\theta\), neither word is admissible. This gives the stated \(1,2,3\) global four-cycle count and, together with the two shorter-period counts, the \(8,12,16\) fixed-four-iterate count.

Finally, away from \(x=1\), each branch linear part divided by \(\sqrt2t\) is orthogonal. The product of four branches is \(4t^4\) times an orthogonal matrix. Since \(4t^4>1\), every smooth primitive four-cycle is repelling. No smooth multiplier is assigned to the threshold orbit that hits the crease.

## Verification

The embedded `verify.py` uses only the Python standard library. Running `python3 verify.py` performs exact rational arithmetic on every cyclically distinct word of lengths one, two and four at five rational parameters on both sides of \(\theta\). It also checks the three seed formulas, the shared-point collision polynomial identities, branch membership in the whole triangle, and primitive-versus-shorter-period reduction. Its 129 exact checks pass. These are finite corroborations, not substitutes for the exhaustive six-necklace calculation and all-parameter polynomial sign proof above. The inequalities at the algebraic endpoint are derived symbolically rather than approximated numerically.

## Relationship to prior work

Alves and Etubi introduced their 2024 analysis of continuity properties for physical measures of this family, and the explicit triangle and branch maps are used as defined there. Pumariño, Rodríguez, Tatjer and Vigil (2014, 2015) introduced and investigated the planar tent/expanding-Baker setting, including chaotic attractors and a symbolic full-shift description at \(t=1\). That prior description already implies, or at minimum explains, the 16 fixed-four-iterate points at \(t=1\); this endpoint is **not** asserted to be new. Marqués-Lobeiras and collaborators' 2022 open-access preprint treats strictly invariant polygons for related two-parameter expanding-Baker maps, not an exact primitive four-cycle count along this parameter interval. The distinct contribution here is the *complete closed-parameter four-cycle census, exact interior algebraic transition, and two-itinerary identification at the nondifferentiable threshold*. Broad symbolic itinerary enumeration itself is standard.

## Limitations

The full 2015 Nonlinearity article could not be lawfully retrieved in this investigation after open/preprint attempts; its accessible abstract and the detailed 2022 account were inspected instead. The possibility of a differently formulated historical threshold result is a genuine priority risk. The 2022 related work is available in full, and no matching theorem was identified in its stated results and text. No classification of longer cycles, invariant measures or basins is claimed. At \(t=\theta\) the critical four-cycle intersects the fold, so an ordinary derivative-based stability assertion is intentionally omitted.

## References

1. J. F. Alves and O. R. Etubi, *Hölder continuity of invariant density and entropy for piecewise expanding maps*, first submitted 27 September 2024, arXiv:2409.18805v1; revised manuscript titled *Modulus of continuity of invariant densities and entropies for piecewise expanding maps*, arXiv:2409.18805v2, 2025. https://arxiv.org/abs/2409.18805
2. A. Pumariño, J. Á. Rodríguez, J. C. Tatjer and E. Vigil, *Expanding Baker Maps as models for the dynamics emerging from 3D-homoclinic bifurcations*, Discrete Contin. Dyn. Syst. B 19 (2014), 523–541, DOI:10.3934/dcdsb.2014.19.523.
3. A. Pumariño, J. Á. Rodríguez, J. C. Tatjer and E. Vigil, *Chaotic dynamics for two-dimensional tent maps*, Nonlinearity 28 (2015), 407–434, DOI:10.1088/0951-7715/28/2/407.
4. A. Marqués-Lobeiras, A. Pumariño, J. Á. Rodríguez and E. Vigil, *Strictly invariant sets for 2-D tent maps: 2-D strange attractors*, public preprint (2022), https://web.ma.utexas.edu/mp_arc/c/22/22-50.pdf; DOI:10.1007/s00574-022-00324-6.
