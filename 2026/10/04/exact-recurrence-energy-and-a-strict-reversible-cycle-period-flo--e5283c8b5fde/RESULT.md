# Exact recurrence energy and a strict reversible-cycle period floor in the Sprott D flow
## Finding
Consider the canonical Sprott D system
\[
\dot x=-y,\qquad
\dot y=x+z,\qquad
\dot z=xz+3y^2.
\]
Let
\[
R(x,y,z)=(-x,y,-z).
\]
The vector field is reversible in the exact sense
\[
f(Ru)=-R f(u).
\]

Every compactly supported invariant probability measure \(\mu\) satisfies
\[
\mathbb E_\mu[x^2]=4\,\mathbb E_\mu[y^2]
\]
and
\[
\mathbb E_\mu[xz]
=-3\,\mathbb E_\mu[y^2]
=-\frac34\,\mathbb E_\mu[x^2].
\]
Consequently every non-origin compact invariant measure assigns positive mass to
\[
\{xz<0\},
\]
and it assigns positive mass to both \(y>0\) and \(y<0\).

If \(\mu\) is also \(R\)-invariant and is not the origin measure, then
\[
\mathbb E_\mu[x]=\mathbb E_\mu[z]=0,
\]
and each of \(x,y,z\) assumes both signs on a set of positive \(\mu\)-measure.

Finally, every nonconstant periodic orbit whose image is invariant under \(R\) has least period
\[
P>4\pi.
\]

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the Sprott D flow and supported on compact subsets of \(\mathbb R^3\). The periodic-orbit statement concerns a nonconstant classical periodic solution whose image set is invariant under the reversing involution \(R\).

The equations are the canonical Case D equations published by Sprott in 1994. A later paper by Li and Sprott writes the same system after the linear relabeling
\[
(u,v,w)=(y,x,z)
\]
as
\[
\dot u=v+w,\qquad
\dot v=-u,\qquad
\dot w=3u^2+vw
\]
and explicitly identifies its time-reversal symmetry.

## Proof
For every polynomial \(h\), invariance gives
\[
\int Lh\,d\mu=0,
\]
where \(L\) is the generator.

From
\[
Lx=-y
\]
we obtain
\[
\mathbb E_\mu[y]=0.
\]
From
\[
Lz=xz+3y^2
\]
we obtain
\[
\mathbb E_\mu[xz]=-3\,\mathbb E_\mu[y^2].
\]
The key exact coboundary is
\[
L(xy-z)=x^2-4y^2.
\]
Therefore
\[
\mathbb E_\mu[x^2]=4\,\mathbb E_\mu[y^2].
\]
Combining the two identities gives
\[
\mathbb E_\mu[xz]=-\frac34\,\mathbb E_\mu[x^2].
\]

If \(\mu\) is not the origin measure, then \(\mathbb E_\mu[y^2]>0\). Indeed, if \(y=0\) almost surely, the energy identity gives \(x=0\) almost surely; then stationarity of \(yz\),
\[
L(yz)=xz+z^2+xyz+3y^3,
\]
gives \(\mathbb E_\mu[z^2]=0\). Thus non-origin measures have
\[
\mathbb E_\mu[xz]<0.
\]
A nonnegative random variable cannot have negative expectation, so \(xz<0\) has positive mass. Since \(\mathbb E_\mu[y]=0\) and \(y\) is not almost surely zero, both signs of \(y\) have positive mass.

Now suppose \(\mu\) is \(R\)-invariant. The functions \(x\) and \(z\) are odd under \(R\), so
\[
\mathbb E_\mu[x]=\mathbb E_\mu[z]=0.
\]
For a non-origin measure, \(\mathbb E_\mu[x^2]>0\), hence both signs of \(x\) occur. Also \(z\) cannot vanish almost surely: if it did, then
\[
0=\mathbb E_\mu[Lz]=3\mathbb E_\mu[y^2]
\]
would force the origin measure. Therefore \(\mathbb E_\mu[z^2]>0\), and the zero mean of \(z\) forces both signs of \(z\).

Let \(\gamma\) now be a nonconstant \(R\)-invariant periodic orbit with least period \(P\), and let \(\mu_\gamma\) be normalized time measure on that orbit. Setwise \(R\)-invariance implies \(R_*\mu_\gamma=\mu_\gamma\), so
\[
\int_0^P x(t)\,dt=0.
\]
The stationary energy identity on the orbit is
\[
\int_0^P x(t)^2\,dt
=4\int_0^P y(t)^2\,dt
=4\int_0^P \dot x(t)^2\,dt.
\]
Wirtinger's inequality for the zero-mean periodic function \(x\) gives
\[
\int_0^P \dot x(t)^2\,dt
\ge
\left(\frac{2\pi}{P}\right)^2
\int_0^P x(t)^2\,dt.
\]
Hence
\[
\frac14\ge\left(\frac{2\pi}{P}\right)^2,
\]
so
\[
P\ge4\pi.
\]

Equality in Wirtinger's inequality would make \(x\) a nonzero first harmonic and therefore
\[
x''=-\frac14x,\qquad
x'''=-\frac14x'.
\]
Eliminating \(y,z\) from the Sprott D equations gives the scalar jerk equation
\[
x'''-x x''+x'-x^2+3(x')^2=0.
\]
Under the equality conditions this reduces pointwise to
\[
x'-x^2+4(x')^2=0.
\]
Multiply by \(x'\) and integrate over a full period. Periodicity gives
\[
\int_0^P x^2x'\,dt=0,
\]
and for a first harmonic
\[
\int_0^P (x')^3\,dt=0.
\]
Therefore
\[
\int_0^P (x')^2\,dt=0,
\]
contradicting nonconstancy. Thus equality is impossible and
\[
P>4\pi.
\]

## Verification
The accompanying standard-library checker uses exact sparse-polynomial arithmetic over rational coefficients. It verifies
\[
L(xy-z)=x^2-4y^2,
\]
\[
Lz=xz+3y^2,
\]
the reversibility identity
\[
f(Ru)=-Rf(u),
\]
and the eliminated jerk equation
\[
x'''-x x''+x'-x^2+3(x')^2=0.
\]
It also checks the algebraic reduction of the equality case. The stored checker output is `VERIFY_OK`.

The period argument is analytic rather than experimental: the only external theorem used is the classical equality case of Wirtinger's inequality for periodic zero-mean functions.

## Relationship to prior work
Sprott's original Case D listing gives exactly the displayed canonical equations and highlights the unusual coexistence of time-reversal invariance with dissipation through a symmetric attractor/repellor pair.

Li and Sprott later study the same system after a linear relabeling. Their full text identifies Sprott D as the simplest time-reversible rotationally invariant system, writes its one-parameter extension, and for the canonical coefficient gives a strange attractor together with its Lyapunov spectrum. Their purpose is to transform attractor/repellor pairs by inserting a plane of equilibria, not to derive invariant-measure energy identities or a least-period obstruction for reversing-symmetric cycles.

Perdahçı and Hacınlıyan use Sprott systems as normal-form benchmarks and explicitly discuss the Sprott D linearized spectrum and Lyapunov spectrum. Their analysis concerns normal forms, resonances, and Lyapunov exponents rather than the exact global stationary identities above.

Targeted semantic searches using Sprott D, time-reversible Sprott D, stationary energy, invariant measure, reversible periodic orbit, and period-bound formulations found no statement that implies the final theorem. The closest indexed results concern analogous balance and period laws for different vector fields.

## Limitations
The strict period bound is proved only for periodic orbits whose image is invariant under the reversing involution \(R\). A non-symmetric periodic orbit, if present, occurs with its distinct time-reversed partner and is not covered by the \(4\pi\) argument because its \(x\)-mean need not vanish.

The invariant-measure identities do not by themselves prove existence of the chaotic attractor or repellor and do not classify all compact invariant sets.

The 1994 publisher page and Sprott's public Case D listing were inspected for the canonical equations and historical description. The 2017 same-object article was inspected in full at the Sprott D section. The 2003 normal-form article was inspected through a public full-text rendering. A differently phrased or unindexed older period theorem could still escape targeted search.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Simple Chaotic Flow GIF Animations,” Case D listing, https://sprott.physics.wisc.edu/simplest.htm.
3. C. Li and J. C. Sprott, “How to Bridge Attractors and Repellors,” International Journal of Bifurcation and Chaos 27, 1750149 (2017), DOI 10.1142/S0218127417501498.
4. N. Z. Perdahçı and A. Hacınlıyan, “Normal forms and nonlocal chaotic behavior in Sprott systems,” International Journal of Engineering Science 41, 1085–1108 (2003), DOI 10.1016/S0020-7225(02)00325-7.
5. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 1271–1281 (2004), DOI 10.1016/j.chaos.2003.12.054.
