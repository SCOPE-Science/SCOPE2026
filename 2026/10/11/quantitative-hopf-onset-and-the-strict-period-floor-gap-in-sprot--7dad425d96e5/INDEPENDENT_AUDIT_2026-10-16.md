# Independent mathematical audit

## correctness

PASS

For a>0 fixed, b crossing zero, transform Sprott Q via s=y,x=s'+s,z=-s''-s' to jerk s'''+(1-b)s''+(a-b)s'+as+s²=0. At the origin the characteristic polynomial is (lambda+1)(lambda²-b lambda+a); simple pair crosses with positive real speed 1/2 and the third eigenvalue stays -1. An explicitly normalized quadratic Hopf calculation yields l1=-(8a+1)/(a^(3/2)(a+1)(4a+1))<0. Independent Lindstedt/Fourier first/second harmonics give beta=(8a+1)/(2a(a+1)(4a+1))>0 and frequency shift delta=-(26a+5)/(12a^(3/2)(a+1)(4a+1)), yielding asserted stable branch, physical amplitude M_y²=2a(a+1)(4a+1)/(8a+1)b+O(b^(3/2)), mean y=-(a+1)(4a+1)/(8a+1)b+o(b), and period T=(2pi/sqrt a)[1+(26a+5)b/(6a(8a+1))+O_a(b²)]. Multiplying jerk by s' and integrating yields ∫s''²=(a-b)∫s'², so Wirtinger forces all nonconstant cycles T>2pi/sqrt(a-b), with strictness from s² generating second harmonic. The new gap coefficient is 2pi(a+1)/(3a^(3/2)(8a+1))b>0. Independently checked eigenvectors, l1, Fourier constants and gap algebra in SymPy. Infinite local existence relies on nondegenerate Hopf theorem, not simulation.

## originality

PASS

Sprott 1994 paper (full four pages visually read) introduces numerical chaotic flows, and the later parameter atlas (read) describes numerics, not all-a analytic Hopf period/amplitude derivatives. A published Resultary Q source of Oct 4 proves the exact UNIVERSAL period floor T>2pi/sqrt(a-b): this part is explicitly covered and NOT novelty. Another Sprott-S source proves a critical supercritical Hopf and limiting period at an equivalent critical jerk, but under the Q unfolding BOTH transformed S parameters and physical time vary. Thus the S sign and floor do not imply the Q first-order physical y-amplitude, b-period derivative or strictly positive gap coefficient. This comparison explicitly grants known components and accepts only the surviving exact quantitative branch calculation; full Mendes 2021 equivalence paper is uninspected and residual risk remains.

## value

PASS

All-a>0 first-order period and physical amplitude laws for a classical polynomial flow provide analytic predictions near the origin and quantify how a known universal period constraint fails to be attained by the emerging stable cycle. The sharp strictly positive gap slope addresses a natural extremal/bifurcation boundary rather than a textbook eigenvalue check. The already-known floor and shared critical Hopf sign are not counted as separate contributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
