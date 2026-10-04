# Exact stationary circle and forced slab excursions in the Sprott F flow
## Finding
Consider the generalized Sprott F flow
\[
\dot x=y+z,\qquad \dot y=-x+ay,\qquad \dot z=x^2-bz,
\]
with \(a>0\) and \(b>0\). For every compactly supported invariant probability measure \(\mu\),
\[
\mathbb E_\mu[x^2\mid z]=bz
\]
for \(\mu\)-almost every \(z\), and
\[
\mathbb E_\mu\!\left[\left(x+\frac{b}{2a}\right)^2\right]=\left(\frac{b}{2a}\right)^2.
\]
Writing \(m=\mathbb E_\mu[z]\), the same stationary identities give
\[
\mathbb E_\mu[x]=-am,\qquad \mathbb E_\mu[x^2]=bm,\qquad
\operatorname{Var}_\mu(x)=a^2m\left(\frac{b}{a^2}-m\right),
\]
so \(0\le m\le b/a^2\). Equality at \(m=0\) occurs only for the equilibrium \(E_0=(0,0,0)\), and equality at \(m=b/a^2\) occurs only for \(E_1=(-b/a,-b/a^2,b/a^2)\).

Unless \(\mu\) is a convex combination of \(\delta_{E_0}\) and \(\delta_{E_1}\), it assigns positive mass to both
\[
-\frac{b}{a}<x<0
\]
and
\[
x<-\frac{b}{a}\quad\text{or}\quad x>0.
\]
Every nonconstant periodic orbit therefore remains in \(z>0\), enters the open slab \(-b/a<x<0\), and also exits the closed slab \(-b/a\le x\le0\).

For the canonical Sprott F parameters \(a=1/2\), \(b=1\), this becomes
\[
\mathbb E[(x+1)^2]=1,\qquad 0\le\mathbb E[z]\le4,
\]
with equilibria \(E_0=(0,0,0)\) and \(E_1=(-2,-4,4)\).

## Assumptions and scope
The vector field is the two-parameter normalization of Sprott's Case F with positive parameters. The theorem concerns compactly supported invariant probability measures and periodic trajectories. No claim is made about existence, uniqueness, stability, mixing, entropy, or the size of any chaotic attractor.

The canonical Case F was publicly listed in 1994. Sprott's later two-parameter normalization explicitly gives the equations above and displays stable-equilibrium, periodic, chaotic, and unbounded regions in parameter space.

## Proof
Let \(L\) be the Lie derivative of the flow. Invariance gives \(\int L\phi\,d\mu=0\) for every continuously differentiable \(\phi\) on a neighborhood of the compact support.

First,
\[
Lx=y+z,\qquad Ly=-x+ay,\qquad Lz=x^2-bz.
\]
Taking expectations gives
\[
\mathbb E[y]=-m,\qquad \mathbb E[x]=-am,\qquad \mathbb E[x^2]=bm.
\]
Hence
\[
\operatorname{Var}(x)=bm-a^2m^2=a^2m\left(\frac{b}{a^2}-m\right).
\]

There is also a single affine coboundary behind the stationary circle. With
\[
\Phi=z+bx-\frac{b}{a}y,
\]
a direct calculation yields
\[
L\Phi=x^2+\frac{b}{a}x
=\left(x+\frac{b}{2a}\right)^2-\left(\frac{b}{2a}\right)^2.
\]
Integration proves the circle identity.

For the conditional identity, choose a continuously differentiable \(H\) and write \(h=H'\). Then
\[
L(H(z))=h(z)(x^2-bz).
\]
Because the \(z\)-projection of the support is compact, arbitrary continuous test functions on it arise this way after extension. Therefore \(\mathbb E[x^2-bz\mid z]=0\), which is the stated heightwise law.

Every point of a compact invariant set lies on a bounded complete trajectory. Variation of constants in the \(z\)-equation gives
\[
z(t)=e^{-bT}z(t-T)+\int_0^T e^{-bs}x(t-s)^2\,ds.
\]
Letting \(T\to\infty\) gives
\[
z(t)=\int_0^\infty e^{-bs}x(t-s)^2\,ds\ge0.
\]
If \(z(t_0)=0\), the integral forces \(x(t)=0\) for every \(t\le t_0\). The equations then force \(y(t)=z(t)=0\), and uniqueness gives the origin trajectory. Thus every non-origin bounded complete trajectory has \(z(t)>0\).

The two equilibria follow directly from \(y=-z\), \(x=ay=-az\), and
\[
z(a^2z-b)=0.
\]
If \(m=0\), then \(\mathbb E[x^2]=0\), and invariance forces \(E_0\). If \(m=b/a^2\), then \(\operatorname{Var}(x)=0\), so \(x=-b/a\) on the support; invariance then forces \(E_1\).

Finally put \(c=b/(2a)\). The circle identity says \(\mathbb E[(x+c)^2]=c^2\). On \(-b/a<x<0\), one has \((x+c)^2<c^2\); on the strict exterior one has \((x+c)^2>c^2\). If either side had zero mass, equality of the mean would force \((x+c)^2=c^2\) almost surely, hence \(x\in\{0,-b/a}\) on the invariant support. Continuity of each orbit then keeps \(x\) on one of those two values, and the equations force the corresponding equilibrium. Thus only equilibrium mixtures avoid the two-sided excursion. A nonconstant periodic orbit cannot support such a mixture, so its orbit measure gives the periodic consequence.

## Verification
The included `verify.py` uses exact rational sparse-polynomial arithmetic. It checks the denominator-cleared coboundary identity
\[
aL\!\left(z+bx-\frac{b}{a}y\right)=ax^2+bx,
\]
the equilibrium factorization \(z(a^2z-b)\), and the two canonical equilibria at \(a=1/2\), \(b=1\). Its recorded output is `VERIFY_OK`.

The measure-theoretic steps are analytic: invariance of compactly supported measures, conditional expectation against continuous \(z\)-tests, variation of constants, and continuity of complete trajectories.

## Relationship to prior work
Sprott's 1994 paper introduced the simple chaotic-flow collection; the author's Case F listing gives the canonical equations \(\dot x=y+z\), \(\dot y=-x+0.5y\), \(\dot z=x^2-z\). The 2013 parameter-space note gives the exact two-parameter normalization used here and classifies sampled behavior as stable equilibrium, periodic limit cycle, chaotic strange attractor, or unbounded orbit.

A later synchronization survey tabulates the canonical Sprott F equilibria \((-2,-4,4)\) and \((0,0,0)\), consistent with the endpoint states above. Targeted searches of published-finding corpus for the exact vector field, stationary circle, conditional law, and slab excursion found no Sprott F record; the closest hits were analogous stationary-balance results for different flows, which do not imply this theorem.

## Limitations
The result does not prove that a non-equilibrium compact invariant set exists for a given \(a,b\), nor does it characterize its topology or stability. The conditional identity is an almost-everywhere statement with respect to the stationary \(z\)-marginal. The originality check is bounded by indexed and accessible literature; the 1994 publisher full text was not available in this inspection, so the comparison to that paper uses its verified bibliographic record plus Sprott's public Case F listing rather than a claim of full-paper exclusion.

## References
1. J. C. Sprott, *Some simple chaotic flows*, Physical Review E 50, R647-R650 (1994), DOI: 10.1103/PhysRevE.50.R647. Published 1 August 1994.
2. J. C. Sprott, *Simple Chaotic Flow GIF Animations*, public Case F equation listing: https://sprott.physics.wisc.edu/simplest.htm
3. J. C. Sprott, *Dynamic Regions in Simple Chaotic Flows*, 27 April 2013, modified 1 September 2014: https://sprott.physics.wisc.edu/technote/regions.htm
4. *On the synchronization techniques of chaotic oscillators and their FPGA-based implementation for secure image transmission*, PMCID: PMC6364889 (canonical Sprott equilibrium table).
