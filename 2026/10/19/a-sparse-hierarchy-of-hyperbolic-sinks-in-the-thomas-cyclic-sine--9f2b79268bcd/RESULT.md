# A sparse hierarchy of hyperbolic sinks in the Thomas cyclic sine flow

## Finding

Consider the three-dimensional cyclic differential equation
\[
\dot x=\sin y-bx,\qquad \dot y=\sin z-by,\qquad \dot z=\sin x-bz,\qquad b>0.
\]
A *nonzero synchronous hyperbolic sink* is an equilibrium \((u,u,u)\) with \(u\ne0\) whose three Jacobian eigenvalues have strictly negative real parts. For integers \(k\ge0\), put \(v_k=(2k+\tfrac12)\pi\). For \(k\ge1\), let \(f_k\) be the unique solution of \(\tan f_k=f_k\) in \((2k\pi,v_k)\); set \(f_0=0\). Let \(h_k\) be the unique solution of \(\tan h_k=-h_k/2\) in \((v_k,(2k+1)\pi)\). Define
\[
F_0=1,\quad F_k=\frac1{\sqrt{1+f_k^2}}\ (k\ge1),\qquad
H_k=\frac1{\sqrt{4+h_k^2}}\ (k\ge0).
\]
Then the set of damping values admitting such a sink is **exactly**
\[
\mathcal S=\bigsqcup_{k=0}^{\infty}(H_k,F_k).
\]
The intervals are pairwise disjoint, with \(F_{k+1}<H_k\). For each \(b\in\mathcal S\), the system has **exactly two** nonzero synchronous hyperbolic sinks, related by sign reversal; for \(b\notin\mathcal S\), it has none. The endpoints, which have a zero or purely imaginary eigenvalue, are excluded by the term *hyperbolic sink*.

There is a sharp quantitative sparsity law. As \(k\to\infty\),
\[
F_k-H_k=\frac{9}{2v_k^3}+O(v_k^{-5}),
\]
and, for Lebesgue measure on damping values,
\[
\boxed{\bigl|\mathcal S\cap(0,\varepsilon)\bigr|
=\frac{9}{8\pi}\,\varepsilon^2+O(\varepsilon^3)
\qquad(\varepsilon\downarrow0).}
\]
In particular, there are infinitely many disjoint damping windows approaching zero, but the fraction of sufficiently small damping parameters supporting a nonzero synchronous hyperbolic sink tends to zero.

## Assumptions and scope

The parameter \(b\) is any positive real number; \(k\) ranges over all nonnegative integers. No assumption is made concerning nonsynchronous equilibria, non-equilibrium attractors, or recurrent dynamics. Statements about stability are strictly linear hyperbolic conclusions for the full three-dimensional vector field, not stability only within the synchronous diagonal. The asymptotic uses the positive lobe midpoints \(v_k\to\infty\), and the measure law has an absolute remainder constant for all sufficiently small positive \(\varepsilon\).

## Proof

**1. Spectrum and synchronization.** Synchronous equilibria satisfy \(\sin u=bu\), and the vector field is odd, so their nonzero values come in pairs \(\pm u\). At \((u,u,u)\), let \(c=\cos u\). The Jacobian is a cyclic permutation matrix multiplied by \(c\), minus \(bI\). Since a cyclic three-permutation has eigenvalues \(1\) and \(e^{\pm2\pi i/3}\), the three eigenvalues are
\[
\lambda_0=c-b,\qquad \lambda_\pm=-b-\frac c2\pm i\frac{\sqrt3}{2}c.
\]
Hence the equilibrium is a full-space hyperbolic sink if and only if \(c<b\) and \(c>-2b\).

**2. All positive roots and their stability.** If \(u>0\) satisfies \(\sin u=bu>0\), it lies in a positive sine lobe \((2k\pi,(2k+1)\pi)\). Define \(g(u)=\sin u/u\). On \((0,\pi)\), \(g\) decreases strictly from \(1\) to \(0\), because \(u\cos u-\sin u<0\). Thus it has one positive root for \(0<b<1\), with \(\cos u<b\). On each higher positive lobe, \(g'(u)=(u\cos u-\sin u)/u^2\). The numerator has derivative \(-u\sin u<0\), starts positive at \(u=2k\pi\), and ends negative. It vanishes only once at \(f_k\in(2k\pi,v_k)\). Thus for \(b<F_k=g(f_k)\) there are two roots, one on the increasing and one on the decreasing side, while at \(b=F_k\) the roots coalesce. At an increasing-side root, \(c>b\) and \(\lambda_0>0\), so it cannot be a sink. On the decreasing side, \(c<b\) always.

For a decreasing-side root with \(u\le v_k\), one has \(c\ge0\), so also \(c>-2b\). For \(u\in(v_k,(2k+1)\pi)\), the condition \(c>-2g(u)\) is equivalent, after multiplication by \(u>0\), to \(u\cos u+2\sin u>0\). Dividing by the strictly negative cosine gives \(\tan u<-u/2\). The strictly increasing function \(\tan u+u/2\) runs from \(-\infty\) to a positive value on this interval, and has exactly one zero \(h_k\). It follows that the decreasing root is a hyperbolic sink precisely for \(u<h_k\), equivalently \(b>H_k=g(h_k)\). At \(u=h_k\), \(\cos h_k=-2b\) and the conjugate pair has zero real part. This proves the window formula for each lobe, including \(k=0\), with \(f_0=0\) and \(F_0=1\).

**3. Pairwise disjointness and exact count.** The definitions give \(f_{k+1}>2(k+1)\pi\) and \(h_k<(2k+1)\pi\). Consequently
\[
1+f_{k+1}^2>1+4(k+1)^2\pi^2>4+(2k+1)^2\pi^2>4+h_k^2,
\]
so \(F_{k+1}<H_k\). As the windows are disjoint, at most one positive synchronous equilibrium is a hyperbolic sink for any fixed \(b\), and its negative partner is also a sink; inside each window they both exist. Outside their union there are none. The origin is excluded regardless of its stability.

**4. Window asymptotics.** Write \(v=v_k\). At the left turning point \(f_k=v-\delta_F\), the equation \(\tan f_k=f_k\) becomes \(\cot\delta_F=v-\delta_F\), implying \(\delta_F=v^{-1}+O(v^{-3})\) from the Laurent expansion of cotangent at zero. Similarly \(h_k=v+\delta_H\) and \(\tan h_k=-h_k/2\) give \(\cot\delta_H=(v+\delta_H)/2\), hence \(\delta_H=2v^{-1}+O(v^{-3})\). Taylor expansion of the exact endpoint formulas yields
\[
F_k=v^{-1}+\tfrac12v^{-3}+O(v^{-5}),\qquad
H_k=v^{-1}-4v^{-3}+O(v^{-5}).
\]
Subtracting proves \(F_k-H_k=\tfrac92v^{-3}+O(v^{-5})\).

**5. Total damping measure near zero.** Since \(F_k,H_k=v_k^{-1}+O(v_k^{-3})\) and \(v_{k+1}-v_k=2\pi\), the intervals lying wholly below \(\varepsilon\) correspond to \(v_k>\varepsilon^{-1}+O(\varepsilon)\), up to at most one endpoint-straddling interval. Such a partial window has length \(O(\varepsilon^3)\). By comparison of the decreasing function \(v^{-3}\) with its integral over the arithmetic progression,
\[
\sum_{v_k\ge \varepsilon^{-1}+O(1)}v_k^{-3}
=\frac1{2\pi}\int_{\varepsilon^{-1}}^\infty v^{-3}\,dv+O(\varepsilon^3)
=\frac{\varepsilon^2}{4\pi}+O(\varepsilon^3).
\]
The accumulated \(O(v_k^{-5})\) error is \(O(\varepsilon^4)\). Multiplication by \(9/2\) gives the claimed sharp coefficient \(9/(8\pi)\). This completes the proof.

## Verification

The accompanying `verify.py` uses only Python's standard library. Run `python3 verify.py` to reproduce high-precision bracketed solutions for the first twelve windows, check their disjointness, root identities and negative eigenvalue real parts, and confirm the asymptotic width scale at separated large indices. These **finite checks are supplementary**; the proof of the infinite classification and measure coefficient is analytic above. For the first higher lobe the numerical endpoints are approximately \(H_1=0.119910744243336\) and \(F_1=0.128374553525899\). At the principal lobe, \(H_0\approx0.328990102242739\) and \(F_0=1\). The conjugate eigenvalue pair at a right endpoint obeys \(\lambda_\pm=\pm i\sqrt3\,b\); along its equilibrium branch, its real part crosses with derivative \(-1-h_k^2/6<0\).

## Relationship to prior work

Thomas introduced the cyclic sine feedback flow and its labyrinth dynamics [1]. Sprott and Chlouverakis [2, pp. 2097–2099] explicitly give the synchronization equation, the cyclic Jacobian spectral relation and the principal conjugate-eigenvalue crossing. These established equations imply the *pointwise* spectral tests used in Steps 1–2, and are not presented here as discoveries. The additional claim here is the complete, globally indexed and pairwise-disjoint family of **full-space sink intervals**, the exact number of such sinks for every positive damping, and especially the sharp \(\varepsilon^2\) Lebesgue-measure law with its constant \(9/(8\pi)\). The full text of [2] was compared for this more precise hierarchy. The 1999 text [1] was not accessible in full, and historical priority for the interval-and-measure classification therefore remains uncertain.

## Limitations

The classification concerns only **nonzero synchronous hyperbolic equilibria** of this exact three-dimensional Thomas vector field. It neither excludes nonsynchronous sinks nor characterizes chaotic or periodic attractors. At \(b=H_k\) or \(b=F_k\) the relevant eigenvalues touch the imaginary axis, so no nonlinear stability assertion is made there; the terms “Hopf-type spectral crossing” and “fold” do not certify any nonlinear periodic-orbit bifurcation. The asymptotic is about parameter-set Lebesgue measure, not about the probability of observing a given dynamical attractor under a chosen distribution of initial conditions.

## References

[1] R. Thomas, “Deterministic Chaos Seen in Terms of Feedback Circuits: Analysis, Synthesis, ‘Labyrinth Chaos’,” *International Journal of Bifurcation and Chaos* **9** (1999), 1889–1905. DOI: 10.1142/S0218127499001383.

[2] J. C. Sprott and K. E. Chlouverakis, “Labyrinth Chaos,” *International Journal of Bifurcation and Chaos* **17** (2007), 2097–2108. DOI: 10.1142/S0218127407018245. Lawful author manuscript: https://sprott.physics.wisc.edu/pubs/paper302.pdf.

[3] E. McDonald and S. R. Choudhury, “The Thomas Attractor with and without Delay: Complex Dynamics to Amplitude Death,” *Dynamics of Nature and Complex Systems* (2020), DOI: 10.5890/DNC.2020.03.003 (abstract inspected; full text not used for exclusion).
