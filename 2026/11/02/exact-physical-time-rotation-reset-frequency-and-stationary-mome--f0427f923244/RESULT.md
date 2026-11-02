# Exact physical-time rotation, reset frequency and stationary moments in a discontinuous hysteresis map

## Finding
For a two-branch parameter region of a planar map with discontinuous hysteresis, the entire original-time dynamics on a natural non-equilibrium recurrent family, rather than just the Poincaré return map, is explicitly measurably conjugate to a rigid irrational rotation. The conjugacy yields its invariant probability, exact reset frequency, all polynomial moments and an exact bounded-discrepancy law for the physical return clock.

Define \(\Psi(u)=u\) for \(|u|\le1\), and \(\Psi(u)=0\) for \(|u|>1\). Consider
\[
F(x,s)=\bigl(\lambda x+\alpha s,\ \Psi(s+\lambda x+\alpha s-x)\bigr),\qquad \alpha=\beta-\lambda.
\]
Under the assumptions below, put
\[
q=\frac1{1-\lambda},\quad \mu=-\lambda q,\quad \nu=\beta+\mu,\quad L=\log\frac\nu\mu,\quad
\theta=\frac{\log(\nu/q)}{L},\quad h=2-\theta.
\]
The invariant recurrent family consists of the reset states
\[
A_\sigma(z)=(\sigma\mu e^{Lz},0),\qquad 0\le z<1,\quad \sigma\in\{-1,1\},
\]
and the intermediate states
\[
B_\sigma(z)=(\lambda\sigma\mu e^{Lz},(\lambda-1)\sigma\mu e^{Lz}),
\qquad 0\le z<1-\theta,\quad\sigma\in\{-1,1\}.
\]
As usual for a discontinuous interval map, branch seams are interpreted through half-open intervals. We claim a measurable isomorphism on the union, modulo its finite seams and their countable preimages, with rotation by one unit on a circle of circumference \(2h\).

When \(\theta\) is irrational, the physical-time stationary measure is
\[
\boxed{\displaystyle
\Pi=\frac1{2(L+\log(q/\mu))}\sum_{\sigma=\pm1}\left(
\int_\mu^\nu\delta_{(\sigma t,0)}\frac{dt}{t}
+\int_\mu^q\delta_{(\lambda\sigma t,(\lambda-1)\sigma t)}\frac{dt}{t}\right).}
\]
In particular, \(\Pi\{s=0\}=1/h\). Denoting the original state coordinates by \(X,S\), their first moments vanish and their second moments are
\[
\begin{aligned}
\mathbb E_\Pi[X^2]&=\frac{\nu^2-\mu^2+\lambda^2(q^2-\mu^2)}{2(L+\log(q/\mu))},\\
\mathbb E_\Pi[S^2]&=\frac{(\lambda-1)^2(q^2-\mu^2)}{2(L+\log(q/\mu))},\\
\mathbb E_\Pi[XS]&=\frac{\lambda(\lambda-1)(q^2-\mu^2)}{2(L+\log(q/\mu))}.
\end{aligned}
\]
For every section starting coordinate \(z\in[0,1)\) whose orbit avoids branch seams, the original physical-time index of its \(n\)-th return to \(s=0\) is exactly
\[
\boxed{H_n=2n-\lfloor z+n\theta\rfloor,\qquad
|H_n-n(2-\theta)|<1.}
\]
The rotation is irrational for example at \(\lambda=-1/2\), \(\beta=2\), where \(\mu=1/3\), \(q=2/3\), \(\nu=7/3\) and \(\theta=\log(7/2)/\log7\). Rationality of this last quotient would force a positive power of \(7/2\) to equal an integer power of \(7\), contradicting unique prime factorization.

## Assumptions and scope
Fix \(-1<\lambda<0\), \(\beta>1\) and \(-\lambda(\beta+1)>1\). Then \(0<\mu<q<\nu\), \(0<\theta<1\) and the first section-return takes one or two physical steps on \([\mu,\nu]\), respectively. Assume \(\theta\notin\mathbb Q\) for unique ergodicity. The theorem concerns starting points in the indicated compactly bounded recurrent family away from seam preimages; it does not classify arbitrary points on the equilibrium segment, nor claim the full strip is uniquely ergodic. The invariant measure and the isomorphism are measurable, not topological at cut points.

## Proof
The source's exact first-return formulas give \(q=1/(1-\lambda)\), \(\mu=-\lambda q\), \(\nu=\beta+\mu\). Our inequality \(-\lambda(\beta+1)>1\) says the next discontinuity lies below \(\mu\), so there are exactly two return branches. Direct substitution into \(F\) independently verifies, for \(t\in(\mu,q)\),
\[
F(\sigma t,0)=(\lambda\sigma t,(\lambda-1)\sigma t),\qquad
F^2(\sigma t,0)=(-\sigma(\nu/q)t,0).
\]
For \(t\in(q,\nu)\), the first step resets immediately:
\[
F(\sigma t,0)=(-\sigma(-\lambda)t,0).
\]
The equality \(\nu/q>1\) holds, and \(\log(\nu/q)=L\theta\); also \(\log(-\lambda)=\log(\mu/q)=-L(1-\theta)\). Thus, in logarithmic coordinate \(z=\log(t/\mu)/L\), the unsigned return is \(z\mapsto z+\theta\pmod1\), with return-time roof
\[
r(z)=\begin{cases}2,&0\le z<1-\theta,\\1,&1-\theta\le z<1.\end{cases}
\]
Every return also changes the sign \(\sigma\mapsto-\sigma\). More precisely, letting \(A_\sigma,B_\sigma\) have the definitions above, the complete one-step transitions are
\[
A_\sigma(z)\mapsto B_\sigma(z)\quad(z<1-\theta),\qquad
B_\sigma(z)\mapsto A_{-\sigma}(z+\theta),
\]
\[
A_\sigma(z)\mapsto A_{-\sigma}(z+\theta-1)\quad(z\ge1-\theta).
\]
Take a coordinate \(w\in[0,h)\) with \(w=z\) on \(A_\sigma\), and \(w=1+z\) on \(B_\sigma\). Set \(W=w\) when \(\sigma=+1\), and \(W=w+h\) when \(\sigma=-1\). The above three transitions all become, exactly,
\[
W\longmapsto W+1\pmod{2h}.
\]
Indeed a transition crosses \(w=h\) exactly when a section return flips the sign, so the two half-circles glue consistently. Since \(h=2-\theta\) is irrational, translation by one is an irrational rotation of circumference \(2h\), with unique normalized Haar measure and convergence of time averages for every Riemann-integrable observable away from exceptional seams. Pulling back the uniform \(W\) measure gives density \(dz/(2h)=dt/(2hLt)\) on each signed reset curve and each signed intermediate curve. As \(hL=L+\log(q/\mu)\), this is the displayed \(\Pi\). It is a probability measure because the total \(W\)-length is \(2h\). Invariance, ergodicity, and unique invariant probability within this recurrent family follow by measurable isomorphism (the boundaries have Haar measure zero). Integrating \(x^2\), \(s^2\) and \(xs\) over the four arcs yields the three expressions. Symmetry between \(\sigma=\pm1\) makes the first moments zero.

Finally the roof can be written \(r(z)=2-\lfloor z+\theta\rfloor\), for \(0\le z<1\). Over successive return phases \(z_j=\{z+j\theta\}\), its Birkhoff sum telescopes:
\[
H_n=\sum_{j=0}^{n-1}r(z_j)
=2n-\lfloor z+n\theta\rfloor.
\]
Consequently \(H_n-n(2-\theta)=\{z+n\theta\}-z\), which lies strictly between \(-1\) and \(1\). This is a uniform, all-horizon physical-clock law, not an asymptotic approximation. The inverse transformation also shows the spectrum of the time-one Koopman operator on the recurrent invariant probability space is pure point with eigenvalues \(e^{2\pi i k/(2h)}\), \(k\in\mathbb Z\).

## Verification
The standalone file `checker.py` computes the literal hysteresis update and independently unfolds the proposed rigid rotation for four parameter pairs. It verifies 80,000 one-step state identities at random rotation phases, and compares quadrature of moments and section occupation to the closed forms. These finite computations are corroboration; the infinite-time and exact statements follow from the branch identities and rotation proof above. Run `python checker.py` with Python 3.

## Relationship to prior work
Kryzhevich, Avrutin, Begun, Rachinskii and Tajbakhsh (2021, arXiv:2104.11825), Theorem 4 and Sections 8.1–8.3, derive the nonlinear section map, its logarithmic interval-translation conjugacy, and the fact that its two-interval regime yields a rigid circle rotation. The new statement keeps their exact model and return reduction as credited premises, but unfolds **the original physical one-step map**, including the sign flip and nonconstant roof. It identifies the complete one-step rotation, physical-time invariant probability, exact quadratic fluctuations and bounded original-clock discrepancy. These full-time objects are not stated in the inspected model discussion, where rotation applies to the Poincaré section only. Standard suspension and interval-exchange theory provides general tools, but does not by itself supply these explicit state-space formulas and the cancellation giving the precise time-one circle length.

## Limitations
The result applies only when \(-\lambda(\beta+1)>1\), and unique ergodicity requires the irrationality of \(\theta\). Branch seams and their preimages are excluded from orbitwise statements; finite exceptional trajectories require a separate endpoint convention. There is an equilibrium segment elsewhere in the original phase strip, so the entire physical map does not have a unique invariant probability. The spectral statement concerns the specified recurrent invariant component. All source and originality comparisons concern the materials inspected, not proof of global publication priority; independent validation remains outstanding.

## References
1. S. Kryzhevich, V. Avrutin, N. Begun, D. Rachinskii and K. Tajbakhsh, *Dynamics of Systems with a Discontinuous Hysteresis Operator and Interval Translation Maps*, arXiv:2104.11825 (first posted April 23, 2021); *Axioms* **10** (2021), article 80, DOI:10.3390/axioms10020080. In particular Sections 7–8 and Theorem 4.
2. S. Troubetzkoy, *Absence of mixing for interval translation mappings and some generalizations*, arXiv:2102.05904 (2021). General context on nonmixing for interval translations; not a full-time physical invariant formula for the present hysteresis map.
