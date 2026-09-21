# Exact diagonal balance and compact-recurrence bounds for the Halvorsen flow

Consider the four-parameter cyclic Halvorsen system
\[
\begin{aligned}
\dot x&=-ax-by-cz-dy^2,\\
\dot y&=-ay-bz-cx-dz^2,\\
\dot z&=-az-bx-cy-dx^2,
\end{aligned}
\]
with real parameters and \(d\ne0\). Write
\[
\sigma=a+b+c,\qquad S=x+y+z,\qquad Q=x^2+y^2+z^2,
\]
and let \({\bf 1}=(1,1,1)\).

## Result

The scalar diagonal coordinate satisfies the exact identities
\[
\dot S=-\sigma S-dQ
\]
and, after completing the square,
\[
\dot S=\frac{3\sigma^2}{4d}
-d\left\|X+\frac{\sigma}{2d}{\bf 1}\right\|^2,
\qquad X=(x,y,z).
\]
These identities impose global restrictions on every bounded recurrent regime.

### 1. Exact mean-square sphere law

If a solution is defined and bounded for all \(t\ge0\), then
\[
\lim_{T\to\infty}\frac1T\int_0^T
\left\|X(t)+\frac{\sigma}{2d}{\bf 1}\right\|^2\,dt
=\frac{3\sigma^2}{4d^2}.
\]
Thus every bounded long-time regime has the same mean-square distance from the midpoint of the two diagonal equilibria
\[
O=(0,0,0),\qquad E=-\frac{\sigma}{d}{\bf 1}.
\]
Equivalently, every compactly supported invariant probability measure \(\mu\) satisfies
\[
\int \left\|X+\frac{\sigma}{2d}{\bf 1}\right\|^2\,d\mu
=\frac{3\sigma^2}{4d^2}.
\]

### 2. Critical surface \(\sigma=0\): collapse of bounded recurrence

When \(\sigma=0\),
\[
\dot S=-dQ.
\]
Every solution that is defined and bounded for all \(t\ge0\) converges to the origin.
Moreover, the origin is the only bounded complete trajectory. Consequently, the only compact invariant set is \(\{O\}\), and the only compactly supported invariant probability measure is \(\delta_O\).

This is a global statement on the same parameter surface on which the two diagonal equilibria coalesce.

### 3. Sharp diagonal slab for \(\sigma\ne0\)

Assume \(\sigma\ne0\), and define
\[
v=\frac{dS}{\sigma}.
\]
Every bounded complete trajectory obeys the sharp pointwise restriction
\[
-3\le v(t)\le0\qquad\text{for all }t\in\mathbb R,
\]
or equivalently
\[
-3\le\frac{d(x+y+z)}{a+b+c}\le0.
\]
The two boundary hyperplanes are rigid: a bounded complete trajectory can meet \(v=0\) only at \(O\), and it can meet \(v=-3\) only at \(E\). Hence every non-equilibrium compact invariant set lies in the open slab
\[
-3<\frac{d(x+y+z)}{a+b+c}<0.
\]
Both constants are sharp because the two diagonal equilibria lie on the two boundary hyperplanes.

### 4. Uniform second-moment collapse near the critical surface

For every compactly supported invariant probability measure and \(\sigma\ne0\),
\[
0\le\int Q\,d\mu\le3\left(\frac{\sigma}{d}\right)^2.
\]
The lower equality holds only for \(\delta_O\), and the upper equality holds only for \(\delta_E\).
Therefore every family of compactly supported invariant measures with fixed \(d\ne0\) collapses to the origin in second moment as \(\sigma\to0\):
\[
\left(\int \|X\|^2\,d\mu\right)^{1/2}
\le \sqrt3\,\left|\frac{\sigma}{d}\right|.
\]
In particular, periodic or chaotic invariant regimes cannot retain a finite RMS amplitude while approaching the transcritical surface \(a+b+c=0\).

For the standard Halvorsen equations \(b=c=4\), \(d=1\), one has \(\sigma=a+8\). Any compact invariant set at \(a\ne-8\) is therefore contained in
\[
-3(a+8)\le x+y+z\le0
\]
when \(a+8>0\) (with the equivalent ratio form above valid without sign conventions), and every bounded long-time regime satisfies
\[
\left\langle
\left\|X+\frac{a+8}{2}{\bf 1}\right\|^2
\right\rangle
=\frac{3(a+8)^2}{4}.
\]
At \(a=-8\), no nontrivial compact invariant set exists.

## Proof

Summing the three equations gives
\[
\dot S=-\sigma S-dQ.
\]
Since
\[
\left\|X+\frac{\sigma}{2d}{\bf 1}\right\|^2
=Q+\frac{\sigma}{d}S+\frac{3\sigma^2}{4d^2},
\]
the completed-square identity follows immediately.

For any bounded forward trajectory, integration gives
\[
\frac1T\int_0^T
\left\|X+\frac{\sigma}{2d}{\bf 1}\right\|^2dt
=\frac{3\sigma^2}{4d^2}
-\frac{S(T)-S(0)}{dT},
\]
and the last term tends to zero. Integrating the generator identity against a compactly supported invariant probability measure gives the measure version.

Now let \(\sigma=0\). If a forward trajectory is bounded, then \(S\) is bounded and monotone and
\[
\int_0^\infty Q(t)\,dt<\infty.
\]
On a bounded trajectory the polynomial vector field is bounded, so \(Q'(t)=2X(t)\cdot\dot X(t)\) is bounded. Hence \(Q\) is uniformly continuous; a nonnegative uniformly continuous integrable function tends to zero. Thus \(Q(t)\to0\), so \(X(t)\to O\). If the trajectory is bounded and complete, the same argument on the whole real line gives \(Q(t)\to0\) as \(t\to\pm\infty\). Consequently \(S(t)\to0\) at both ends. Since \(S\) is monotone, it must be identically zero, and then \(Q\equiv0\). This proves the critical complete-orbit and compact-invariance claims.

Assume next \(\sigma\ne0\). For a bounded complete trajectory, variation of constants gives, when \(\sigma>0\),
\[
S(t)=-d\int_{-\infty}^t e^{-\sigma(t-s)}Q(s)\,ds,
\]
while for \(\sigma<0\), writing \(\alpha=-\sigma>0\), boundedness in forward time gives
\[
S(t)=d\int_t^\infty e^{-\alpha(s-t)}Q(s)\,ds.
\]
In either case
\[
v(t)=\frac{dS(t)}{\sigma}\le0.
\]
By Cauchy--Schwarz,
\[
Q\ge\frac{S^2}{3}=\frac{\sigma^2}{3d^2}v^2.
\]
Since
\[
v'=-\sigma v-\frac{d^2}{\sigma}Q,
\]
for \(\sigma>0\) one has
\[
v'\le-\frac{\sigma}{3}v(v+3).
\]
If \(v<-3\), then \(r=-v>3\) satisfies
\[
r'\ge\frac{\sigma}{3}r(r-3),
\]
whose comparison equation diverges in finite positive time, contradicting bounded completeness. For \(\sigma<0\), the same comparison applied in reversed time gives the identical lower bound \(v\ge-3\). Thus \(-3\le v\le0\).

At \(v=-3\), equality in the Cauchy--Schwarz estimate is necessary to avoid crossing the forbidden side of the boundary in the relevant time direction. Equality requires \(x=y=z=S/3=-\sigma/d\), namely \(E\). At \(v=0\), the corresponding variation-of-constants integral vanishes, forcing \(Q=0\) and hence \(O\). This proves boundary rigidity.

Finally, invariance gives
\[
0=-\sigma\int S\,d\mu-d\int Q\,d\mu,
\]
so
\[
\int Q\,d\mu
=-\frac{\sigma}{d}\int S\,d\mu
=-\frac{\sigma^2}{d^2}\int v\,d\mu.
\]
The slab bound \(-3\le v\le0\) yields
\[
0\le\int Q\,d\mu\le3\frac{\sigma^2}{d^2}.
\]
The equality cases follow from the boundary rigidity just proved.

## Context and originality boundary

Sprott documented the standard cyclic Halvorsen flow in 1997 and exhibited its period-doubling route to chaos. Later work emphasized dissipativity, Lyapunov exponents, adaptive control, synchronization, numerical prediction, and applications. A 2025 study treated the four-parameter cyclic form written above, analyzed equilibrium stability, and proved local transcritical bifurcation when \(a=-b-c\), together with local Hopf bifurcations on other parameter surfaces.

The contribution here is restricted to the exact diagonal balance mechanism and its global consequences: the mean-square sphere law for every bounded forward regime, the sharp slab for every bounded complete orbit, the disappearance of all nontrivial compact invariant sets on \(a+b+c=0\), and the explicit second-moment collapse bound for compactly supported invariant measures approaching that surface.

No located source states these global balance, slab, or invariant-measure results. The 2025 bifurcation paper was inspected in full text: its analysis is local around equilibria and its conclusion concerns equilibrium stability, transcritical bifurcation, Hopf bifurcation, and bifurcating periodic orbits. Searches within that paper for bounded/global/invariant/sphere/mean terminology found no corresponding global result.

The full text of Vaidyanathan and Azar (2016), DOI 10.1007/978-3-319-30340-6_10, was not inspected. Its abstract states dissipativity, instability of the origin, Lyapunov exponents, adaptive control, and synchronization; because it is a substantial qualitative study of the Halvorsen flow, it remains the strongest inaccessible prior-coverage risk. Sprott's later books were also not inspected directly beyond accessible descriptions and the 2025 paper's citations to them; they are a secondary residual risk for elementary identities of the standard or generalized system.

## Reproducibility

`artifacts/verify_halvorsen_balance.py` symbolically verifies the summed balance, the completed-square identity, and the diagonal equilibrium. `artifacts/verification.txt` records the zero residuals.

## References

1. J. C. Sprott, “A Symmetric Chaotic Flow,” University of Wisconsin web note, 12 August 1997, revised 9 July 2004. https://sprott.physics.wisc.edu/chaos/symmetry.htm
2. S. Vaidyanathan and A. T. Azar, “Adaptive Control and Synchronization of Halvorsen Circulant Chaotic Systems,” in *Advances in Chaos Theory and Intelligent Control*, 2016, pp. 225–247. DOI: https://doi.org/10.1007/978-3-319-30340-6_10
3. K. B. Othman and A. A. Jalal, “Hopf Bifurcation Analysis of the Halvorsen System,” *Zanco Journal of Pure and Applied Sciences* 37(6) (2025), 35–46. DOI: https://doi.org/10.21271/ZJPAS.37.6.4
