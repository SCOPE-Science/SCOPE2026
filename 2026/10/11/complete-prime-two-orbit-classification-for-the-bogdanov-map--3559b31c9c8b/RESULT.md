# Complete prime-two orbit classification for the Bogdanov map

## Finding

Consider the real quadratic Bogdanov family
\[
 F_{k,\mu,\varepsilon}(x,y)=(x+Y,Y),\qquad
 Y=(1+\varepsilon+\mu x)y+kx(x-1),
 \qquad(k,\mu,\varepsilon)\in\mathbb R^3.
\]
A *prime-two point* satisfies \(F^2(p)=p\) and \(F(p)\ne p\); two such points are one orbit when they are images of each other.

**Theorem (complete classification).** Put \(S=u+v\) and \(d=v-u\) for the consecutive first coordinates of a prime-two orbit. The two points, in suitable cyclic order, are
\[
 ((S-d)/2,-d),\qquad ((S+d)/2,d),\qquad d\ne0.
\]
Such an orbit exists if and only if
\[
 (k+\mu)S=k-4-2\varepsilon,
 \qquad (k+2\mu)d^2=kS(2-S),\qquad d\in\mathbb R\setminus\{0\}.
 \tag{1}
\]
In particular the complete parameter classification is as follows.

1. If \(k\ne0\) and \(\mu\ne-k,-k/2\), set
   \[
   S=\frac{k-4-2\varepsilon}{k+\mu},\qquad
   R=\frac{kS(2-S)}{k+2\mu}.
   \]
   There is exactly **one** distinct prime-two orbit when \(R>0\), namely the pair given in the theorem with \(d=\sqrt R\). There are **none** when \(R\le0\).
2. If \(k\ne0\), \(\mu=-k/2\), and \(\varepsilon=(k-4)/2\), **every point** of the line \(y=2x\), except the fixed point \((0,0)\), has least period two. On this line \(F(x,2x)=(-x,-2x)\). There are no other prime-two points.
3. If \(k\ne0\), \(\mu=-k/2\), and \(\varepsilon=-2\), **every point** of the line \(y=2x-2\), except the fixed point \((1,0)\), has least period two. On this line \(F(x,2x-2)=(2-x,2-2x)\). There are no other prime-two points.
4. If \(k\ne0\), \(\mu=-k\), and \(\varepsilon=(k-4)/2\), **every point** on the hyperbola
   \[
   2x^2-2xy-2x+y=0
   \]
   except the fixed points \((0,0)\) and \((1,0)\), has least period two. Equivalently this curve is \(y=2x(x-1)/(2x-1)\). On it, \(F\) acts by the Möbius involution \(x\mapsto x/(2x-1)\). No other points have least period two.
5. In all other cases with \(k\ne0\), \(\mu=-k/2\) or \(\mu=-k\), there are **no** prime-two points. For \(k=0\), prime-two points exist only at \((\mu,\varepsilon)=(0,-2)\), where \(F(x,y)=(x-y,-y)\) and all points with \(y\ne0\) have least period two.

Thus away from three parameter curves the number of distinct prime-two orbits is zero or one; **on each of the three curves there are uncountably many**. The curves coalesce at \((k,\mu,\varepsilon)=(0,0,-2)\), where \(F^2\) is globally the identity. Every orbit on any of the three smooth exceptional invariant curves has a unit multiplier tangent to its curve for \(F^2\); individual such orbits are not hyperbolic.

## Assumptions and scope

All phase variables and parameters are real. The map is polynomial and globally defined, with no positivity or dissipativity restriction. The classification counts *least* period two, not fixed points or higher periods. At the exceptional line and hyperbola cases the excluded fixed points are the only points on the indicated curves that fail the least-period-two condition. The parameter value \(k=0\) is included explicitly, rather than inferred by dividing by \(k\).

## Proof

Let \((u,y_0)\mapsto(v,y_1)\mapsto(u,y_0)\) be a prime-two orbit. The first coordinate update gives \(y_1=v-u=d\) and \(y_0=u-v=-d\); consequently \(d\ne0\). Applying the second-coordinate update at both points yields **exactly**
\[
 d(2+\varepsilon+\mu u)=ku(u-1),\qquad
 -d(2+\varepsilon+\mu v)=kv(v-1). \tag{2}
\]
Substitute \(u=(S-d)/2\) and \(v=(S+d)/2\). The difference of the two equations in (2), divided by nonzero \(d\), and their sum respectively give (1). Conversely the sum and difference can be reversed (because \(d\ne0\)), so (1) implies both updates in (2). This proves the claimed necessary-and-sufficient correspondence without extraneous roots.

For \(k\ne0\) and \(k+\mu\ne0\), the first equation in (1) fixes \(S\). If also \(k+2\mu\ne0\), the second fixes \(d^2=R\); a real nonzero \(d\) exists exactly for \(R>0\). The two signs of \(d\) only exchange the points, giving one orbit.

When \(\mu=-k/2\), the second equation in (1) becomes \(S(2-S)=0\), so \(S=0\) or \(S=2\). For \(S=0\), the first requires \(\varepsilon=(k-4)/2\) and leaves \(d\ne0\) arbitrary; its phase points lie on \(y=2x\). For \(S=2\), the first requires \(\varepsilon=-2\) and gives \(y=2x-2\). Each line is thus both exhaustive and filled by a pointwise reflection as asserted. Because \(k\ne0\), those two parameter conditions cannot coincide.

When \(\mu=-k\), the first equation forces \(\varepsilon=(k-4)/2\); the second then becomes \(d^2=S(S-2)\). Expressed at a point with \(x=u=(S-d)/2\), \(y=-d\), this identity is exactly \(2x^2-2xy-2x+y=0\). Solving for \(y\) shows that its real points have \(x\ne1/2\), and on the curve direct substitution gives \(F(x,y)=(x/(2x-1),-y)\). This transformation squares to the identity. Its only fixed points on the curve are \((0,0)\) and \((1,0)\), so all others have least period two. If the forced parameter equality fails, there is no such orbit.

Finally, if \(k=0\), equation (1) reads \(\mu S=-4-2\varepsilon\) and \(2\mu d^2=0\). Since \(d\ne0\), we must have \(\mu=0\), then \(\varepsilon=-2\); directly \(F(x,y)=(x-y,-y)\), an involution with exactly the fixed line \(y=0\). This exhausts all parameters.

For the tangent multiplier assertion, each exceptional curve is smooth, invariant under \(F\), and pointwise fixed under \(F^2\). Differentiating the identity \(F^2|_C=\mathrm{id}_C\) in a nonzero tangent direction yields eigenvalue \(1\) for \(D(F^2)\) on the tangent line. This also holds along the hyperbola, whose \(y\)-as-a-function-of-\(x\) parametrization has no real singularity.

## Verification

The accompanying `verify_period2.py` (Python 3, SymPy) uses exact polynomial algebra to check the two sum/difference identities, direct two-step invariance of all three exceptional curves, sample exact prime-two points in each family and a generic family, and the global involution at \((0,0,-2)\). Run with `python verify_period2.py` after installing `sympy` if necessary. Its finite exact examples are illustrative checks; exhaustive validity is established by the reversible algebra in the proof rather than by enumeration. Numerical parameter exploration is not used.

## Relationship to prior work

Arrowsmith, Cartwright, Lansbury, and Place introduced the standard Bogdanov-map presentation and studied bifurcations, invariant circles, and chaos [1]. Djellit and Boukemara [2] analyze this **same map** and give a local flip threshold \(\varepsilon=k/2-2\) for the origin, but their accessible full text and plotted dynamics do not provide a global least-period-two orbit classification across all three parameters or identify the three curves filled by periodic points. The local flip equality overlaps the parameter value on exceptional family (i), yet it does not by itself imply the required cancellation in the transverse \(\mu\)-parameter. Dénes and Makay [3] give numerical Bogdanov basin examples, not a parameter-wide algebraic census. The conservative Hénon conjugacy [1] addresses only a restricted parameter slice and does not imply the three exceptional loci.

## Limitations

No assertion is made about least periods three and higher, global attraction, chaos, basins, or structural persistence of the continuum of two-cycles under perturbations. The exceptional cycles have a unit multiplier and are nonhyperbolic. The original 1993 article [1] was available through abstract and bibliographic metadata only, not inspected in complete text, leaving a historical-priority risk despite full-text comparisons with [2] and [3]. The date recorded for the source is the first precisely verified arXiv public listing (22 February 1994), not the date of the 1993 journal volume or a later preprint revision.

## References

[1] D. K. Arrowsmith, J. H. E. Cartwright, A. N. Lansbury, and C. M. Place, *The Bogdanov Map: Bifurcations, Mode Locking, and Chaos in a Dissipative System*, International Journal of Bifurcation and Chaos **3** (1993), 803–842, DOI: `10.1142/S021812749300074X`, preprint `arxiv:chao-dyn/9402006`.

[2] I. Djellit and M. Boukemara, *Bifurcations and Attractors in Bogdanov Map* (2004), 323–338. Lawful open-access manuscript: `https://faculty.kfupm.edu.sa/math/akca/papers/djellit-i.pdf`.

[3] A. Dénes and G. Makay, *Attractors and basins of dynamical systems*, Electronic Journal of Qualitative Theory of Differential Equations (2011). Lawful open-access article: `https://www.math.u-szeged.hu/ejqtde/p564.pdf`.
