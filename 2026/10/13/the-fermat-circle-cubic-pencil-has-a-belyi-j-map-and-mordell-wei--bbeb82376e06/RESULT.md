# The Fermat–circle cubic pencil has a Belyi \(j\)-map and Mordell–Weil rank three

## Finding

Over \(\mathbb C\), consider the projective pencil
\[
C_t:\quad X^3+Y^3-Z^3+tZ(X^2+Y^2-Z^2)=0,
\qquad t\in\mathbb P^1,
\]
where \(t=\infty\) denotes \(Z(X^2+Y^2-Z^2)=0\). Let \(S\to\mathbb P^1\) be the surface obtained by resolving the pencil's base points. Then \(S\) is a relatively minimal rational elliptic surface with a section. Its complete singular-fiber configuration is
\[
\begin{array}{c|c}
\text{parameter}&\text{Kodaira type}\\ \hline
-\frac32&I_4\\
3&I_2\\
\infty&I_2\\
-1&I_1\\
8t^3-27t-27=0&3I_1
\end{array}
\]
(the three roots in the last line are distinct). Its elliptic generic fiber over \(\mathbb C(t)\) has Mordell–Weil rank exactly \(3\).

Its rational modular invariant is
\[
\boxed{j(t)=\frac{4096t^{12}}{(t-3)^2(t+1)(2t+3)^4(8t^3-27t-27)}}.
\]
This is a degree-\(12\) Belyi map, ramified only over \(0\), \(1728\), and \(\infty\), with respective ramification partitions
\[
(12),\qquad (2,2,2,2,2,2),\qquad (4,2,2,1,1,1,1).
\]

## Assumptions and scope

All surfaces, curves, base points, and fibers are geometric objects over \(\mathbb C\). The parameter is the projective ratio of the Fermat cubic and homogenized circle equations. Falkensteiner and Sendra's original homotopy parameter \(\lambda\) satisfies \(t=\lambda/(1-\lambda)\); its projective completion includes \(t=-1\), corresponding to \(\lambda=\infty\). A fiber type is asserted after resolution of *all* proper and infinitely near base points, not merely from the singularities of the plane member.

The stated rank is the geometric rank over \(\mathbb C(t)\). It is not a claim about the arithmetic Mordell–Weil group over \(\mathbb Q(t)\), about torsion, or about explicit generators.

## Proof

**1. Base locus and elliptic surface.** Write \(G=X^3+Y^3-Z^3\) and \(H=Z(X^2+Y^2-Z^2)\). On \(Z=0\), the equation \(G=0\) has three distinct roots \(X^3+Y^3=0\), transverse to the line. On \(Z=1\), set \(s=x+y\), \(p=xy\). The equation \(H=0\) gives \(p=(s^2-1)/2\); substituting into \(G=0\) gives
\[
-\frac12(s-1)^2(s+2)=0.
\]
The two points with \(s=-2\), \(p=3/2\) are simple. The two points with \(s=1\), \(p=0\) are \((1,0)\), \((0,1)\), each of intersection multiplicity \(2\). Thus there are seven proper base points accounting for nine intersections.

Near \((1,0)\), put \(x=1+u\), \(y=v\). The two generators are
\[
G=3u+3u^2+u^3+v^3,\qquad H=2u+u^2+v^2.
\]
They share the tangent \(u=0\). On the first blow-up chart \(u=mv\), their proper transforms are \(G/v\), \(H/v\); their gradients at \((m,v)=(0,0)\) are independent, with determinant \(3\). Therefore exactly one additional blow-up resolves the unique infinitely near common base point. The computation at \((0,1)\) is symmetric. Blowing up all nine (including these two infinitely near) produces a basepoint-free genus-one pencil: the member at \(t=0\) is a smooth cubic, and an exceptional divisor over any simple base point is a section. The resulting smooth surface is rational with Picard number \(\rho(S)=10\), and the fiber divisor equals \(-K_S\).

**2. Classification of singular plane members.** For finite \(t\), on \(Z=1\) let
\[
f_t(x,y)=x^3+y^3-1+t(x^2+y^2-1).
\]
The critical equations are \(x(3x+2t)=y(3y+2t)=0\). Evaluating \(f_t\) at the only four possibilities \((0,0)\), \((-2t/3,0)\), \((0,-2t/3)\), \((-2t/3,-2t/3)\) gives, respectively,
\[
-(t+1),\quad \frac{(t-3)(2t+3)^2}{27},\quad
\frac{(t-3)(2t+3)^2}{27},\quad
\frac{8t^3-27t-27}{27}.
\]
There is no singularity on the line at infinity for finite \(t\), because the two partial derivatives there include \(3X^2\) and \(3Y^2\). The cubic \(8t^3-27t-27\) is squarefree and has no root among \(-1\), \(3\), and \(-3/2\). The Hessian at every listed singular point is diagonal with entries \(6x+2t\), \(6y+2t\), both nonzero. All are ordinary nodes. Thus \(t=-1\) and the three cubic roots give precisely four irreducible nodal fibers \(I_1\).

At \(t=3\), the member factors as
\[
(X+Y+2Z)(X^2-XY+XZ+Y^2+YZ-2Z^2),
\]
with smooth line and conic meeting transversely at two points outside the base locus. Its resolved fiber is \(I_2\). At \(t=\infty\), the line \(Z=0\) and conic \(X^2+Y^2-Z^2=0\) meet transversely at \([1:\pm i:0]\), not at base points, yielding a second \(I_2\).

At \(t=-3/2\), the factorization is
\[
(X+Y-Z)\left(X^2-XY-\frac12XZ+Y^2-\frac12YZ-\frac12Z^2\right).
\]
The two branches meet transversely exactly at the double base points \((1,0)\) and \((0,1)\). At \((1,0)\), the local first-blow-up transform of this member, after dividing out the generic exceptional factor \(v\), is divisible by \(v\). Thus the first exceptional curve survives as a *vertical component*. The line and conic meet that exceptional at distinct slopes \(m=-1\) and \(m=1\), while the second base point is at \(m=0\). The same holds at \((0,1)\). After the second blow-ups, the two original components are disjoint and joined by two exceptional bridges, forming a cycle of four smooth rational curves: a fiber of type \(I_4\). In particular, counting only the two original plane nodes would give the incorrect fiber type.

No other singular fibers are possible by the exhaustive critical equations. The fiber Euler numbers sum to \(4+2+2+4=12\). The surface is relatively minimal: a vertical \((-1)\)-curve would have \(K_S\cdot E=0\) because \(K_S=-F\), contradicting adjunction \(2p_a(E)-2=E^2+K_S\cdot E=-1\).

**3. The invariant and its branching.** Put \(s=x+y\), \(d=x-y\), and \(w=(3s+2t)d\). From \(4f_t=s^3+2ts^2+(3s+2t)d^2-4(1+t)\) follows the birational double-cover quartic
\[
w^2=Q_t(s):=(3s+2t)\bigl(4(1+t)-s^3-2ts^2\bigr).
\]
For the standard binary-quartic invariants \(I=12ae-3bd+c^2\) and \(J=72ace+9bcd-27ad^2-27b^2e-2c^3\) of \(as^4+bs^3+cs^2+ds+e\), direct expansion gives
\[
I=16t^4,\qquad
J=16B(t),\qquad
B(t)=8t^6-216t^4-216t^3+729t^2+1458t+729.
\]
Writing \(D(t)=(t-3)^2(t+1)(2t+3)^4(8t^3-27t-27)\), one has
\[
4I^3-J^2=6912D(t),\qquad 4096t^{12}-1728D(t)=64B(t)^2.
\]
The classical formula \(j=1728\cdot4I^3/(4I^3-J^2)\) gives the asserted rational function. The degree is \(12\). The polynomial \(B\) has six simple zeros and is coprime to \(D\). The first equality identifies all poles; the second shows that the six zeros of \(B\) lie over \(1728\), each with multiplicity two. The unique preimage of \(0\) is \(t=0\) with multiplicity \(12\). The ramification contributions are \(11\), \(6\), and \(5\), totaling \(22=2\cdot12-2\); hence these are all branch points and \(j\) is Belyi.

**4. Geometric Mordell–Weil rank.** The only reducible fibers have respectively \(4\), \(2\), and \(2\) components, while the other four singular fibers are irreducible. By the Shioda–Tate formula for a relatively minimal elliptic surface with section,
\[
\operatorname{rank}E(\mathbb C(t))
=\rho(S)-2-\sum_v(m_v-1)
=10-2-(3+1+1)=3.
\]

## Verification

Run `python3 verify.py` with SymPy installed. It establishes the stated quartic identities, the complete Belyi branching polynomial identities, squarefreeness of the relevant polynomials, both reducible-fiber factorizations, intersections of their components, the nine-basepoint local calculation, and the exceptional bridge slopes. It also checks Euler and rank arithmetic. The geometric argument above, not the script alone, proves the resolution, relative minimality, and Kodaira types.

## Relationship to prior work

Falkensteiner and Sendra, *Rationality and Parametrizations of Algebraic Curves under Specializations*, Example 7.2, supply the Fermat-cubic/unit-circle homotopy and analyze specializations, including reducible members at \(\lambda=3/4\) and \(\lambda=3\). The present theorem instead identifies its complete resolved elliptic fibration, including infinitely near base points, the Belyi modular map and the geometric Mordell–Weil rank. Schütt and Shioda provide the general elliptic-surface and Shioda–Tate theorems used in the last step; they do not derive these data for this pencil. Miranda's classification lists possible rational-elliptic-surface fiber configurations, which does not identify this particular equation, its parameter locations, or its Belyi map. The existence of a configuration on some surface is not the explicit classification of this surface.

## Limitations

The statement is over \(\mathbb C\), with no classification of the Mordell–Weil torsion, explicit generators, arithmetic rank over \(\mathbb Q(t)\), or extensions to other characteristic. Although the \(j\)-map is explicit, no modular-subgroup realization or uniqueness of this dessin is asserted. A Belyi-map catalogue could conceivably contain an equivalent rational covering under a Möbius change; such a catalogue identification, by itself, would not establish the geometric fiber and base-point claims without comparison.

## References

1. S. Falkensteiner and J. R. Sendra, *Rationality and Parametrizations of Algebraic Curves under Specializations*, arXiv:2301.04933, first version 12 January 2023, Example 7.2. https://arxiv.org/pdf/2301.04933
2. M. Schütt and T. Shioda, *Elliptic Surfaces*, arXiv:0907.0298, especially Corollary 6.13 and Sections 5 and 10. https://arxiv.org/pdf/0907.0298
3. R. Miranda, *Persson's list of singular fibers for a rational elliptic surface*, Mathematische Zeitschrift **205** (1990), 191–211. https://www.math.colostate.edu/~miranda/preprints/Perssonslist.pdf
