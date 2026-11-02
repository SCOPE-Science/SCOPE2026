# Sharp two-cycle resonance towers in a fixed-point-free sine-memory map

## Finding

For real parameters \(\alpha>0\) and \(\beta>0\), consider the smooth planar map
\[
F_{\alpha,\beta}(x,y)=\bigl(\alpha\cos x+\beta x\sin(\pi y),\ y+x\bigr),\qquad (x,y)\in\mathbb R^2.
\]
It is fixed-point-free for every positive forcing \(\alpha\). There is a sharp threshold in its *primitive period-two* dynamics:

**Theorem.** If \(0<\beta\le1\), no primitive two-cycle exists anywhere in the real plane. If \(\beta>1\), for each \(\alpha>0\) there is a number \(\delta_\beta>0\) such that for all sufficiently large positive integers \(n\), precisely one positive first coordinate of a primitive two-cycle lies in each interval \((2n-\delta_\beta,2n)\) and \((2n,2n+\delta_\beta)\), **counting the two-cycle modulo vertical translations of length two**. If \(u_n^-\) and \(u_n^+\) denote those coordinates, then
\[
u_n^\pm=2n\pm\frac{\alpha|\cos(2n)|}{\pi n\sqrt{\beta^2-1}}+O_{\alpha,\beta}(n^{-2}).\]
Each such first coordinate gives one two-cycle modulo \(y\mapsto y+2\), and all its integer vertical translates are distinct real-plane two-cycles. In particular, the positive-gain regime \(\beta>1\) has primitive two-cycles of unbounded first-coordinate amplitude for **every** \(\alpha>0\).

This is a local count in two resonance intervals for each sufficiently large \(n\), not an exhaustive global census of every possible two-cycle.

## Assumptions and scope

The map acts on the *entire real plane*, without reducing \(x\) modulo a period or restricting to a numerically observed attractor. The independent parameters obey \(\alpha>0\), \(\beta>0\). A primitive period-two orbit is an unordered pair of distinct real points \(P,Q\) with \(F(P)=Q\) and \(F(Q)=P\). Equivalence under \(y\mapsto y+2\) is used only for the local uniqueness statement; the translated orbits remain distinct on \(\mathbb R^2\). Constants in the big-O statement may depend on \(\alpha,\beta\), but not on \(n\), and the assertion covers all sufficiently large integers \(n\), including those with \(|\cos(2n)|\) exceptionally small.

## Proof

**1. Exact two-cycle reduction.** Fixed points would require \(x=0\) from the second component, and then the first component would require \(\alpha=0\), impossible. Let \((u,y)\mapsto(v,y+u)\mapsto(u,y)\) be a primitive two-cycle. The second component gives \(v=-u\) and \(u\ne0\). Swap the points so that \(u>0\), and put \(z=y+u/2\). The orbit is
\[
P=(u,z-u/2),\qquad Q=(-u,z+u/2).
\]
Adding and subtracting the two first-coordinate equations gives the **necessary and sufficient** pair
\[
\alpha\cos u=\beta u\cos(\pi z)\sin(\pi u/2),
\qquad 1=-\beta\sin(\pi z)\cos(\pi u/2). \tag{1}
\]
This also shows that \(z\mapsto z+2m\), \(m\in\mathbb Z\), gives further distinct geometric cycles.

**2. Sharp exclusion.** The second identity in (1) forces \(\beta\ge1\). At \(\beta=1\), equality in the bound \(|\sin(\pi z)\cos(\pi u/2)|\le1\) forces \(u=2k\) for some positive integer \(k\) and \(\cos(\pi z)=0\). The first identity would then demand \(\cos(2k)=0\), which is impossible: it would imply \(2k=(j+1/2)\pi\) and hence that \(\pi\) is rational. Thus \(\beta=1\) also has no primitive two-cycle.

**3. Exact resonance equation and reconstruction.** Fix \(\beta>1\). Squaring (1) and using \(\sin^2(\pi z)+\cos^2(\pi z)=1\) produces, wherever both denominators are nonzero,
\[
\alpha^2\cos^2u
=u^2\sin^2(\pi u/2)\left(\beta^2-\sec^2(\pi u/2)\right).\tag{2}
\]
Let \(u=2n\pm t\), with \(t>0\) small, and define
\[
\Phi_\beta(t)=\sin(\pi t/2)\sqrt{\beta^2-\sec^2(\pi t/2)}.
\]
The square root is positive for sufficiently small \(t\), and (2) is then equivalent to
\[
(2n\pm t)\Phi_\beta(t)=\alpha|\cos(2n\pm t)|.\tag{3}
\]
A positive solution of (3) does give a genuine two-cycle: set
\[
S_z=-\frac1{\beta\cos(\pi u/2)},\qquad
C_z=\frac{\alpha\cos u}{\beta u\sin(\pi u/2)}.
\]
Equation (2) says exactly that \(S_z^2+C_z^2=1\), so there is a **unique** \(z\pmod 2\) with \(\sin(\pi z)=S_z\) and \(\cos(\pi z)=C_z\). Substituting back into (1) proves both return identities. There is no squaring-induced extraneous orbit.

**4. Two unique large resonances.** Write
\[
\kappa_\beta=\frac\pi2\sqrt{\beta^2-1}>0.
\]
Taylor expansion at zero gives \(\Phi_\beta(t)=\kappa_\beta t+O_\beta(t^3)\) and \(\Phi_\beta'(0)=\kappa_\beta\). Choose \(0<\delta_\beta<1/2\), small enough that the square root is real and \(\Phi_\beta'(t)\ge\kappa_\beta/2\) on \([0,\delta_\beta]\). For \(s\in\{-1,+1\}\), define
\[
R_{n,s}(t)=(2n+s t)\Phi_\beta(t)-\alpha|\cos(2n+s t)|.
\]
At \(t=0\), \(R_{n,s}(0)=-\alpha|\cos(2n)|<0\), again because \(\pi\) is irrational. At \(t=\delta_\beta\), \(R_{n,s}(\delta_\beta)\ge(2n-\delta_\beta)\Phi_\beta(\delta_\beta)-\alpha>0\) for all large \(n\). Moreover \(|\cos|\) is globally 1-Lipschitz, so for \(t_2>t_1\) the increase in \(R_{n,s}\) is bounded below by
\[
\left((2n-\delta_\beta)\frac{\kappa_\beta}{2}
-\Phi_\beta(\delta_\beta)-\alpha\right)(t_2-t_1),
\]
which is positive for all sufficiently large \(n\). Consequently each sign has exactly one root \(t_{n,s}\in(0,\delta_\beta)\). These give two different positive \(u\) coordinates, one on each side of \(2n\). Distinct \(n\) yield disjoint windows after the choice \(\delta_\beta<1/2\).

**5. Sharp location law.** The lower derivative bound and (3) imply \(t_{n,s}=O_{\alpha,\beta}(n^{-1})\). Inserting this into the Taylor expansion and using the 1-Lipschitz property of \(|\cos|\) gives
\[
2n\kappa_\beta t_{n,s}
=\alpha|\cos(2n)|+O_{\alpha,\beta}(n^{-1}).
\]
Since \(2\kappa_\beta=\pi\sqrt{\beta^2-1}\), division by \(n\) proves the stated \(O(n^{-2})\) positional error, uniformly in all integer phases \(2n\).

## Verification

The accompanying `verify.py` uses 75-digit mpmath arithmetic to reconstruct 32 distinct two-cycle representatives at four parameter pairs, including the article's sine-memory example \((\alpha,\beta)=(0.05,1.82)\). It checks both full-map returns and the leading resonance-location estimate. Running `python verify.py` from this package prints four parameter-level PASS messages and a total PASS line. This is a *finite consistency test*; steps 1–5 above give the infinite proof. The code does not enumerate all cycles outside the two asserted local resonance windows.

## Relationship to prior work

Almatroud and Pham, *Building Fixed Point-Free Maps with Memristor* (2023), introduce this precise sine-memory example as their third fixed-point-free map (FPFM3) in Table 1 and investigate iterative plots. They do not state a sharp all-positive-forcing two-cycle threshold, the high-amplitude resonance towers, or the uniform phase-sensitive \(n^{-1}\) displacement law. Bao and collaborators (2020) study a different discrete memristor map with a line of equilibria; its periodic behavior does not imply the theorem. Related analytical two-cycle classifications of the quadratic-memory and absolute-memory variants concern **different functions of the memory coordinate**, without the sine model's periodic lifts and remote resonances. Searches for equivalent formulations and stronger coverings did not identify the present claim; this is an evidence-limited novelty assessment, not a proof that no prior publication exists.

## Limitations

The theorem asserts existence and local uniqueness of two-cycle branches **near positive even integers for sufficiently large indices**. It does not classify all finite-amplitude two-cycles, attractors, stability multipliers, basin geometry or the map's higher periods. The unbounded periodic towers may lie far outside bounded numerically sampled attractors. An unindexed analysis of the exact sine-memory example remains a possible publication-priority risk.

## References

1. O. A. Almatroud and V.-T. Pham, *Building Fixed Point-Free Maps with Memristor*, Mathematics 11 (2023), article 1319; published March 9, 2023, DOI: 10.3390/math11061319. In particular, Section 2 equation (1) and Table 1, FPFM3.
2. B.-C. Bao, H. Li, H. Wu, X. Zhang and M. Chen, *Hyperchaos in a second-order discrete memristor-based map model*, Electronics Letters 56 (2020), 769–770, DOI: 10.1049/el.2020.1172.
