# An exact sharp front for a degenerate Fisher–KPP equation with nonlinear advection

## Finding

For every real \(k\), the equation

\[
u_t=(u u_x)_x-k u u_x+u(1-u),\qquad x\in\mathbb R,\ t>0,
\]

admits the weak sharp traveling wave

\[
u(x,t)=\phi_k(x-c_k t),\qquad
\phi_k(\xi)=\max\{1-e^{c_k\xi},0\},\qquad
c_k=\frac{k+\sqrt{k^2+8}}{4}.
\]

The speed is positive for every \(k\in\mathbb R\). The profile connects \(1\) at \(\xi\to-\infty\) to \(0\), and its support ends at the finite interface \(\xi=0\).

## Assumptions and scope

The diffusion coefficient is \(D(u)=u\), the reaction is \(g(u)=u(1-u)\), and the nonlinear advection term is \(-k u u_x\), with no restriction on the real parameter \(k\). A weak solution is meant in the distributional sense; the profile is continuous and piecewise smooth, and the diffusive flux \(u u_x\) is continuous across the front. This claim establishes existence of the displayed wave only. It does not classify all traveling waves or establish stability or convergence from general initial data.

## Proof

Set \(\xi=x-ct\). The traveling-wave equation is

\[
-c\phi'=(\phi\phi')'-k\phi\phi'+\phi(1-\phi).
\]

On \(\xi<0\), put \(q=e^{c\xi}\) and \(\phi=1-q\). Then \(\phi'=-cq\) and

\[
(\phi\phi')'=-c^2q+2c^2q^2,\qquad
-k\phi\phi'=kcq-kcq^2,\qquad
\phi(1-\phi)=q-q^2.
\]

The left side is \(c^2q\), while the right side is

\[
(-c^2+kc+1)q+(2c^2-kc-1)q^2.
\]

Choose the positive root of \(2c^2-kc-1=0\), namely

\[
c=\frac{k+\sqrt{k^2+8}}{4}.
\]

This identity makes the quadratic coefficient zero and gives \(-c^2+kc+1=c^2\), so the traveling-wave equation holds for \(\xi<0\). For \(\xi>0\), \(\phi=0\) and every term vanishes.

At \(\xi=0\), \(\phi\) is continuous and the flux \(\phi\phi'\) tends to zero from both sides. Also \(\phi\phi'=\tfrac12(\phi^2)'\) almost everywhere, with \(\phi^2\) having no derivative jump at the interface. Thus neither the diffusive flux derivative nor the nonlinear advection term creates an interface Dirac mass. The piecewise identity therefore holds distributionally. Finally, \(\sqrt{k^2+8}>|k|\), so \(c_k>0\) for all real \(k\).

## Verification

The proof is an exact coefficient comparison; no numerical approximation is used. The interface check uses the vanishing flux \(\phi_k\phi_k'\to0\) as \(\xi\uparrow0\). At \(k=0\), the formula reduces to the known degenerate Fisher–KPP sharp-front speed \(1/\sqrt2\). The result does not assert that no other weak traveling waves exist, nor does it separately prove minimality or spectral stability of \(c_k\).

## Relationship to prior work

Sánchez-Garduño and Pérez-Velázquez studied a general degenerate reaction–diffusion–advection equation with the same nonlinear advection term and reported numerical critical-speed fits for the illustrative family \(D(u)=u+\beta u^2\), \(\beta>0\). In the inspected text, that numerical subsection does not give a closed-form profile for the natural boundary case \(D(u)=u\). The present calculation gives an exact benchmark for that case and all real \(k\). Their general existence framework is broader than this explicit formula, so the claim is deliberately limited to the displayed profile and does not assert a new general existence theorem.

The no-advection case \(k=0\) is part of the established sharp-front literature for \(u_t=(u u_x)_x+u(1-u)\); it is not claimed as new. A 2026 preprint treats the no-advection family \(u_t=(u^n u_x)_x+u(1-u^n)\) and gives the minimal speed \(1/\sqrt{1+n}\), which agrees at \(n=1\), \(k=0\) but does not include the nonlinear advection term. Searches for the exact \(k\)-dependent formula did not identify a prior statement of this explicit subfamily; that absence alone is not treated as proof of novelty.

## Limitations

Only the exact weak traveling wave above is established. No full classification of other waves, global minimal-speed theorem, uniqueness theorem for all weak fronts, stability result, or convergence theorem is proved here. The explicit calculation applies to \(D(u)=u\) and \(g(u)=u(1-u)\); it does not supply a closed form for \(D(u)=u+\beta u^2\) when \(\beta>0\). A not-yet-located explicit formula in the older literature remains a residual originality risk.

## References

1. F. Sánchez-Garduño and J. Pérez-Velázquez, “Reactive-Diffusive-Advective Traveling Waves in a Family of Degenerate Nonlinear Equations,” *The Scientific World Journal* (2016), Article 5620839. First published 1 September 2016. DOI: 10.1155/2016/5620839. Full-text record: https://pmc.ncbi.nlm.nih.gov/articles/PMC5023851/.
2. J. A. Sherratt and B. P. Marchant, “Nonsharp Travelling Wave Fronts in the Fisher Equation with Degenerate Nonlinear Diffusion,” *Applied Mathematics Letters* 9(5) (1996), 33–38. DOI: 10.1016/0893-9659(96)00069-9. This is a no-advection comparison; its full text could not be retrieved during this run.
3. Z. Sattar, “Geometric desingularisation of the sharp-to-smooth travelling wave transition,” arXiv:2608.23489 (first public 24 August 2026). This is a post-cutoff, no-advection comparison, not the source date for the present claim.
