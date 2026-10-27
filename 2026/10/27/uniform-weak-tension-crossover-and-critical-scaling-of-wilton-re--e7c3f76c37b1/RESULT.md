# Uniform weak-tension crossover and critical scaling of Wilton resonance orders

## Finding
For the finite-depth, irrotational linear gravity–capillary dispersion relation, the entire hierarchy of fundamental-to-harmonic resonance wavenumbers has a universal two-parameter scaling law. Write the dimensionless surface-tension parameter as \(B=\sigma/(\rho g h^2)\), where the water depth \(h\), gravitational acceleration \(g\), surface tension \(\sigma\), and density \(\rho\) are strictly positive. For \(0<B<1/3\), put
\[
 f_B(x)=\frac{(1+Bx^2)\tanh x}{x},\quad f_B(0)=1.
\]
For each integer \(n\ge2\), let \(x_n(B)>0\) be the unique solution of \(f_B(x_n)=f_B(nx_n)\). This pre-existing existence-and-uniqueness fact is explicitly credited to the cited literature, and is not asserted as new. The following **joint scaling classification** holds.

**Fixed tension, high harmonic.** Let \(y_B>0\) be the unique nonzero solution of \(f_B(y_B)=1\). Then \(n x_n(B)\) increases strictly to \(y_B\), and, with \(f_B'(y_B)>0\),
\[
 x_n(B)=\frac{y_B}{n}+\frac{(B-1/3)y_B^2}{f_B'(y_B)n^3}+O_B(n^{-5}).
\]
Thus the shorter resonant wavelength approaches a finite limit, even as the fundamental resonant wavelength diverges.

**Approach to the critical tension.** With \(\delta=1/3-B\downarrow0\), the resonance roots satisfy the *uniform-in-harmonic-order* law
\[
 \sup_{n\ge2}\left|\frac{(n^2+1)x_n(B)^2}{45\delta}-1\right|=O(\delta).
\]
In particular the same critical coefficient works for every positive integer harmonic order, without fixing \(n\) before taking the limit.

**Weak-tension crossover.** Let \(X(\alpha)>0\) be the unique solution of
\[
 \alpha X(\alpha)^2=\tanh X(\alpha),\quad \alpha>0.
\]
Then
\[
 \lim_{B\downarrow0}\sup_{n\ge2}\left|\frac{x_n(B)}{X(nB)}-1\right|=0.
\]
The crossover has two genuinely different edges:
\[
 X(\alpha)\sim\alpha^{-1/2}\quad(\alpha\downarrow0),\qquad
 X(\alpha)\sim\alpha^{-1}\quad(\alpha\to\infty).
\]
The crossover parameter is the product of the harmonic order and the dimensionless tension, rather than either parameter separately.

## Assumptions and scope
All claims concern the **linear phase-speed matching equation** of two-dimensional irrotational, inviscid, incompressible gravity–capillary water waves with a flat bottom at finite positive depth, constant positive density, no background current, and positive gravity and surface tension. With physical wavenumber \(k>0\), the phase speed satisfies
\[
 c^2(k)=\left(\frac{g}{k}+\frac{\sigma k}{\rho}\right)\tanh(kh)=gh f_B(kh).
\]
The dimensionless fundamental wavenumber is \(x=kh\). Integer \(n\ge2\) represents the exact harmonic ratio, so a resonance means \(c(k)=c(nk)\). The limits are not claims about finite-amplitude traveling-wave existence, nonlinear coupling coefficients, or stability.

The range \(0<B<1/3\) is essential. At and above \(B=1/3\), the positive-wavenumber phase speed is monotone and the nontrivial harmonic resonances under discussion do not occur. Existence and uniqueness of each \(x_n(B)\), and the single-well shape of \(f_B\), are established in Martin (Lemma 3) and Hur–Johnson (Section 2). The novel assertion assessed here is the combined, sharp and uniform multi-order scaling law, not that antecedent theorem.

## Proof
**1. The already-known resonance branch and its geometry.** For each fixed \(0<B<1/3\), the cited single-well result provides a point \(s_B>0\) such that \(f_B\) strictly decreases from \(1\) to its unique minimum on \((0,s_B)\), and strictly increases to infinity on \((s_B,\infty)\). Thus \(f_B(y)=1\) has exactly one positive root \(y_B>s_B\), distinct from the limiting root at zero. The unique resonance for integer \(n\ge2\) straddles the minimum:
\[
 0<x_n<s_B<y_n:=nx_n<y_B.
\]
At \(y=y_n\), the function \(f_B(y/(n+1))\) is greater than \(f_B(y/n)=f_B(y)\), since both shorter arguments lie on the decreasing branch. At \(y=y_B\), however, \(f_B(y_B)=1>f_B(y_B/(n+1))\). By uniqueness of the resonance root for \(n+1\), it follows that \(y_n<y_{n+1}<y_B\). The increasing sequence converges to a positive limit \(y_\infty\). Since \(y_n/n\to0\), passing to the limit in \(f_B(y_n)=f_B(y_n/n)\) gives \(f_B(y_\infty)=1\), hence \(y_\infty=y_B\).

**2. Sharp fixed-tension correction.** The exact Taylor expansion around zero is
\[
 f_B(t)=1+(B-1/3)t^2+(2/15-B/3)t^4+O_B(t^6).
\]
Because \(f_B'(y_B)>0\), the matching equation and the limit in Step 1 first imply \(y_n-y_B=O_B(n^{-2})\). Expanding the two sides at \(y_B\) and zero respectively then gives
\[
 f_B'(y_B)(y_n-y_B)
   =(B-1/3)\frac{y_B^2}{n^2}+O_B(n^{-4}).
\]
Dividing by \(n\) yields precisely the claimed cubic correction and remainder \(O_B(n^{-5})\). The correction is strictly negative because \(B<1/3\) and \(f_B'(y_B)>0\).

**3. Uniform critical scaling.** Put \(\delta=1/3-B>0\). The expansion valid simultaneously as \(\delta,t\to0\) is
\[
 f_B(t)=1-\delta t^2+(1/45+\delta/3)t^4+O(t^6),
\]
with locally uniform remainder and its analytic divided differences. At critical tension \(B=1/3\), the strict inequality \(f_{1/3}(t)>1\) holds for every \(t>0\). Indeed,
\[
 (1+t^2/3)\sinh t-t\cosh t
 =\sum_{j=2}^{\infty}\frac{4j(j-1)}{3(2j+1)!}t^{2j+1}>0.
\]
The positive root \(y_B\) consequently tends to zero as \(B\uparrow1/3\): it remains bounded by growth of \(f_B\) at infinity, and any positive accumulation point would contradict that strict inequality. Inserting \(y_B\) in the expansion yields \(y_B^2=45\delta(1+O(\delta))\). In particular, \(0<y_n<y_B=O(\sqrt\delta)\) **uniformly** for every \(n\ge2\).

Now subtract the expansions at \(t=y_n\) and \(t=x_n=y_n/n\). Divide by \(y_n^2-x_n^2>0\). Every analytic term of order six or greater contributes \(O(y_n^4)\) after the division, uniformly because \((y_n^{2j}-x_n^{2j})/(y_n^2-x_n^2)\) is a sum of nonnegative monomials bounded by \(j y_n^{2j-2}\). The resulting identity is
\[
 \delta=(1/45+\delta/3)(y_n^2+x_n^2)+O(y_n^4)
       =\frac{(n^2+1)x_n^2}{45}+O(\delta^2),
\]
where the final big-O constant is independent of \(n\). Division by \(\delta\) proves the uniform relative \(O(\delta)\) assertion.

**4. Unique universal crossover profile.** The function \(t\mapsto\tanh t/t^2\) decreases strictly from infinity to zero. For strictness, its derivative has numerator \(t\operatorname{sech}^2t-2\tanh t<0\), using \(t<\sinh t\cosh t\). Hence \(X(\alpha)\) is well defined and continuous for all \(\alpha>0\). The claimed limits of \(X\) follow directly by inserting \(\tanh X\sim X\) at zero and \(\tanh X\to1\) at infinity.

Introduce the exact matching residual
\[
 F_{B,n}(x)=n(1+Bx^2)\tanh x-(1+Bn^2x^2)\tanh(nx).
\]
For \(B<1/3\), \(F_{B,n}(x)>0\) for sufficiently small positive \(x\), is negative for sufficiently large \(x\), and has exactly one positive zero \(x_n(B)\) by the antecedent uniqueness result. It therefore has positive sign below that zero and negative sign above it.

It suffices to establish uniform convergence by contradiction. If it failed, some sequence \(B_j\downarrow0\) and integers \(n_j\ge2\) would have a relative error bounded away from zero. Pass to a subsequence where \(\alpha_j=n_jB_j\) converges in the compactified interval \([0,\infty]\). For each case below, we bracket the unique zero between test values and then let their relative multiplicative offsets approach one.

If \(\alpha_j\to0\), take \(x=c/\sqrt{\alpha_j}\), for arbitrary fixed \(c>0\). Both \(x\) and \(n_jx\) diverge. A direct substitution and the exponentially small error in \(\tanh x\to1\) give
\[
 \frac{F_{B_j,n_j}(c/\sqrt{\alpha_j})}{n_j-1}\longrightarrow1-c^2.
\]
The error is uniform even if \(n_j\) changes, since \(n_j/(n_j-1)\le2\). Testing fixed \(c<1\) and \(c>1\) shows \(x_{n_j}(B_j)\sqrt{\alpha_j}\to1\). As \(X(\alpha_j)\sqrt{\alpha_j}\to1\), the desired relative ratio tends to one.

If \(\alpha_j\to\alpha_0\in(0,\infty)\), necessarily \(n_j\to\infty\). For every fixed test \(x=c>0\), divide the exact residual by \(n_j\) and obtain
\[
 n_j^{-1}F_{B_j,n_j}(c)\longrightarrow\tanh c-\alpha_0c^2.
\]
This limit has exactly one positive zero, at \(X(\alpha_0)\), with the positive/negative signs on its two sides. Bracketing gives \(x_{n_j}(B_j)\to X(\alpha_0)\), and continuity of \(X\) finishes the case.

Finally, if \(\alpha_j\to\infty\), put \(x=c/\alpha_j\). Then \(x\to0\), whereas \(n_jx=c/B_j\to\infty\), and direct substitution yields
\[
 B_jF_{B_j,n_j}(c/\alpha_j)\longrightarrow c-c^2.
\]
Again, bracketing at arbitrary fixed \(c<1\) and \(c>1\) proves \(\alpha_j x_{n_j}(B_j)\to1\). Since \(\alpha_jX(\alpha_j)\to1\), the relative ratio tends to one. All possible subsequences yield convergence, contradicting the original failure of uniformity.

## Verification
The accompanying standalone Python program `verify.py` uses only the standard library. Its independent calculations of phase-speed matching and the exact residual agree across seeded random parameter points. It verifies strict growth of the high-harmonic wavenumber, cubic asymptotic coefficients at large fixed harmonic order, near-critical scaling with multiple harmonic orders, and weak-tension crossover over six orders of magnitude in harmonic index. Its run printed `VERIFICATION_OK 329`. These finite floating-point checks **do not establish** either uniform limit: those rest on Steps 1–4.

To reproduce: from the directory containing these files, run `python3 verify.py` (Python 3.9 or later). The code's tests avoid the extreme underflow domain where ordinary double precision is inadequate; the theorem itself is not restricted by floating-point precision.

## Relationship to prior work
Martin's 2012 preprint of a 2013 article, Lemma 3, provides the strictly decreasing sequence of unique fundamental-to-harmonic resonance roots for a more general dispersion relation involving constant vorticity. Hur and Johnson (2015), Section 2, explicitly invoke that lemma for the irrotational capillary–gravity Whitham dispersion and state that the resonance wavenumbers decrease to zero. These established results are **premises**, not discoveries in this note. Trichtchenko, Deconinck and Wilkening (2015) analyze the Wilton ripple resonance and nonlinear wave stability. Langer, Trichtchenko and Akers (2024) analyze *high-order nonlinear perturbation expansions* for resonant model equations; their order-counting theorems and high-order comparisons differ from uniform finite-depth wavenumber scaling in the dimensionless tension.

The additional assertions proved here are the finite nonzero limit and cubic approach of the resonant *short-wave* wavenumber, an all-order uniform critical-tension law, and especially the all-order weak-tension crossover as the harmonic index varies with \(B\). A literature search and material comparison of the accessible primary texts did not identify these jointly stated quantitative laws, but no search establishes absolute priority.

## Limitations
The parameter \(B\) is the **surface-tension-to-gravity** dimensionless ratio \(\sigma/(\rho gh^2)\); some conventions reserve “Bond number” for its reciprocal. The singular limits here concern linear phase-speed coincidence, not finite-amplitude bifurcation, nonlinear Wilton-ripple existence, stability or experimental noise. The big-O coefficient in the fixed-tension expansion may deteriorate as \(B\downarrow0\) or \(B\uparrow1/3\); the other two assertions handle those singular regimes separately. No convergence *rate* is claimed for the global weak-tension supremum, only convergence to zero. The historically extensive water-wave literature leaves residual priority uncertainty even after examining the primary papers below.

## References
1. C.-I. Martin, “Local bifurcation and regularity for steady periodic capillary–gravity water waves with constant vorticity,” *Nonlinear Analysis: Real World Applications* 14 (2013), 131–149; author's preprint (dated May 18, 2012) at https://mat.univie.ac.at/~cmartin/capigravi.pdf, Lemma 3 and its proof.
2. V. M. Hur and M. A. Johnson, “Modulational instability in the Whitham equation with surface tension and vorticity,” arXiv:1506.07560, first publicly posted June 24, 2015; especially Section 2 and the discussion of the resonant sequence.
3. O. Trichtchenko, B. Deconinck and J. Wilkening, “The instability of Wilton ripples,” arXiv:1512.01562 (2015); Sections 1–2.
4. R. Langer, O. Trichtchenko and B. Akers, “Wilton Ripples with High-Order Resonances in Weakly Nonlinear Models,” *Water Waves* 6 (2024), 97–126, doi:10.1007/s42286-024-00086-2; Sections 2–5, Conclusions and Appendix B.
