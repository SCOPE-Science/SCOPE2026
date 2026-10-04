# A polynomial coboundary and stationary height gap in a hidden-attractor flow

## Finding
Consider the three-dimensional flow
\[
\dot x=z,\qquad
\dot y=-x-z,\qquad
\dot z=\frac{1}{10}x+5y-z+xy-\frac{3}{10}xz+a.
\]
For every compactly supported invariant probability measure \(\mu\), write
\[
\langle h\rangle=\int h\,d\mu,\qquad q=\langle x^2\rangle.
\]
Then
\[
\langle x\rangle=\langle z\rangle=\langle xz\rangle=0,
\qquad
\langle xy\rangle=-q,
\qquad
\langle yz\rangle=q,
\]
and the stationary mean height is fixed exactly by
\[
\boxed{\langle y\rangle=-\frac a5+\frac q5}.
\]
The mean law comes from the explicit polynomial coboundary
\[
G=z+\frac12(x+y)^2+\frac{11}{10}x+\frac{1}{10}y+\frac{3}{20}x^2,
\qquad
\frac{dG}{dt}=a+5y-x^2.
\]
There is also the sharp variance inequality
\[
\operatorname{Var}_{\mu}(y)\ge q,
\]
with equality if and only if \(\mu\) is the point mass at the equilibrium
\[
E_a=(0,-a/5,0).
\]
Therefore every non-equilibrium compact stationary state satisfies
\[
q>0,\qquad
\langle y\rangle>-\frac a5,
\qquad
\operatorname{Var}_{\mu}(y)>q
=5\left(\langle y\rangle+\frac a5\right),
\]
and gives positive invariant mass to \(y>-a/5\).

For a nonconstant periodic orbit of least period \(T\), the same statements hold with \(\langle\cdot\rangle\) replaced by the period average. In particular, if \(\bar y\) is its mean \(y\)-coordinate, then
\[
\max_{0\le t<T}|y(t)-\bar y|
>
\sqrt{5\left(\bar y+\frac a5\right)}.
\]
For the source's principal parameter \(a=1\), the stable equilibrium is \((0,-1/5,0)\), so any genuine non-equilibrium compact invariant state, including the reported hidden attractor if interpreted as such a state, must have mean \(y>-1/5\) and satisfy the stated strict fluctuation gap.

## Assumptions and scope
The result concerns the exact continuous-time vector field above and compactly supported invariant probability measures. Compact support guarantees that all polynomial observables used in the proof are integrable and that the standard generator identity \(\int Lh\,d\mu=0\) applies.

The algebraic identities hold for every real parameter \(a\). The source emphasizes \(a=1\) and studies continuation in approximately \(1\le a\le1.5\); no assertion here is made about existence, uniqueness, or basin geometry of a chaotic attractor for arbitrary \(a\).

The source's numerical hidden-attractor claim is not re-proved. The finding is instead an exact structural constraint on any compact invariant statistical state of the published ODE.

The primary classification is MSC 37D45, strange attractors and chaotic dynamics.

## Proof
Let \(L\) denote the Lie derivative along the vector field. Invariance of \(\mu\) gives \(\langle Lh\rangle=0\) for each polynomial observable below.

From \(Lx=z\) and \(Ly=-x-z\),
\[
\langle z\rangle=0,
\qquad
\langle x\rangle=0.
\]
From
\[
L\!\left(\frac{x^2}{2}\right)=xz,
\]
we get \(\langle xz\rangle=0\).

Next,
\[
L\!\left(\frac{(x+y)^2}{2}\right)
=(x+y)(\dot x+\dot y)
=-x(x+y),
\]
so
\[
\langle xy\rangle=-\langle x^2\rangle=-q.
\]
Also
\[
L(xy)=yz-x^2-xz,
\]
therefore
\[
\langle yz\rangle=q.
\]

The key pointwise identity is
\[
G=z+\frac12(x+y)^2+\frac{11}{10}x+\frac{1}{10}y+\frac{3}{20}x^2.
\]
Direct substitution into the vector field gives
\[
LG=a+5y-x^2.
\]
Averaging yields
\[
0=a+5\langle y\rangle-q,
\]
which is the boxed stationary height law.

For the variance statement, note that \(\langle x+y\rangle=\langle y\rangle\), and hence
\[
\operatorname{Var}_{\mu}(x+y)
=
\langle x^2\rangle+
\operatorname{Var}_{\mu}(y)+2\langle xy\rangle
=
\operatorname{Var}_{\mu}(y)-q.
\]
Thus \(\operatorname{Var}_{\mu}(y)\ge q\).

If equality holds, then \(x+y\) is constant on the support of \(\mu\). The support of an invariant probability measure is invariant under the flow, while
\[
\frac{d}{dt}(x+y)=-x.
\]
Hence \(x=0\) on the support. Invariance then forces \(z=\dot x=0\), and the third equation forces \(5y+a=0\). Therefore the support is the single equilibrium \(E_a\). Conversely, the equilibrium point mass gives equality. This also shows that every non-equilibrium invariant measure has \(q>0\), so all displayed strict inequalities follow.

For a periodic orbit, its normalized time measure is invariant. Finally,
\[
\max_t|y(t)-\bar y|^2
\ge \operatorname{Var}(y)
>q
=5\left(\bar y+\frac a5\right),
\]
which gives the periodic-orbit amplitude bound.

## Verification
The accompanying `artifacts/verify_stationary_gap.py` uses exact rational polynomial arithmetic from the Python standard library to reconstruct the vector field and verify the four Lie-derivative identities used in the proof, including
\[
LG=a+5y-x^2.
\]
Its recorded output is in `artifacts/verification_output.txt`.

As an independent numerical sanity check of scale only, a long integration from the source's displayed initial condition at \(a=1\) gives time averages consistent with the exact law to ordinary finite-time accuracy; this numerical observation is not used in the proof.

## Relationship to prior work
The 2018 source introduces the vector field, identifies the equilibrium \((0,-a/5,0)\), and studies a hidden chaotic attractor, bifurcations, Lyapunov exponents, entropy, parameter estimation, and a circuit realization. Its open-access full text does not state the polynomial coboundary, the stationary mean law, the covariance identities, or the variance rigidity above.

Targeted searches for the exact source title, equation, stationary-moment formulations, and the mean law found no published statement equivalent to this result. The closest published-results records located by semantic search establish stationary balance laws for other flows such as Rössler, Rikitake, Rabinovich–Fabrikant, and Shimizu–Morioka/Rucklidge; those vector fields and identities do not imply the present coboundary or its equilibrium-relative height gap.

## Limitations
The finding is conditional on compactly supported invariant probability measures and does not prove that the numerically displayed chaotic set is a rigorously established attractor. It does not determine the basin of the hidden attractor, its physical measure, Lyapunov spectrum, or bifurcation thresholds. The literature search was targeted rather than exhaustive, so an unindexed equivalent formulation remains a residual originality risk.

## References
1. T. Kapitaniak, S. A. Mohammadi, S. Mekhilef, F. E. Alsaadi, T. Hayat, V.-T. Pham, “A New Chaotic System with Stable Equilibrium: Entropy Analysis, Parameter Estimation, and Circuit Design,” *Entropy* 20 (2018), 670. DOI: 10.3390/e20090670. PMCID: PMC7513194.
2. The open-access article records publication on 5 September 2018 and gives the exact vector field, equilibrium calculation, parameter continuation, and circuit model used here.
