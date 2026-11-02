# Sharp two-seed adoption-completion reversal on the five-site path

## Finding
On the path \(P_5=1-2-3-4-5\), suppose exactly two vertices are initially adopted and the other three adopt irrevocably at independent exponential rates \(a+b k\), with \(a,b>0\) and \(k\) the number of already-adopted neighbors. Write \(T_{ij}\) for the mean completion time when seeds are \(i,j\), and set \(x=b/a\). Then the exact critical ratio is
\[
x_* = \frac{11+\sqrt{249}}8=3.3474667297\ldots.
\]
When \(0<x<x_*\), only the two endpoints \(\{1,5\}\) minimize \(T\). At equality, precisely \(\{1,5\}\), \(\{1,4\}\), and \(\{2,5\}\) tie. For \(x>x_*\), precisely \(\{1,4\}\) and \(\{2,5\}\) minimize \(T\). For paths on \(2,3,4\) vertices, the endpoints are always optimal (strictly so on \(3,4\) vertices when \(b>0\)). Thus five is the smallest path order displaying this reversal with two seeds.

## Assumptions and scope
All edges are undirected and carry the same imitation rate \(b>0\). Every unadopted vertex has spontaneous adoption hazard \(a>0\) independent of neighbors; additionally, each adopted neighbor contributes \(b\). Conditional adoption clocks are independent, and adoption is irreversible. There is no discount, cessation, vertex heterogeneity, or budget-dependent change in \(a,b\). The objective is the *mean time until every vertex has adopted*, not mean number adopted at a fixed horizon or adoption-peak time. Every unordered pair of distinct vertices is admissible. Time is measured in units \(1/a\); every conclusion holds for all positive finite \(a,b\).

## Proof
For each occupied set \(S\subseteq\{1,\ldots,n\}\), write \(u(S)=a\mathbb E[T\mid S]\). For \(v\notin S\), let \(k_S(v)\) be the number of neighbors of \(v\) in \(S\) and \(r_v(S)=1+x k_S(v)\). The memoryless exponential race gives the finite acyclic recurrence
\[
u(S)=\frac{1+\sum_{v\notin S}r_v(S)u(S\cup\{v\})}{\sum_{v\notin S}r_v(S)},\quad u(\{1,\ldots,n\})=0.
\]
It is exact; all denominators are positive for \(x>0\). Evaluation in descending occupied-set cardinality produces the following complete reflection-class table for five vertices. All displayed functions equal \(aT_{ij}\):

| Initial seeds | Exact expression |
|---|---|
| \(\{1,2\}\) | \(\frac{36x^4+158x^3+261x^2+180x+44}{2(x+1)(x+2)(x+3)(2x+1)(3x+2)}\) |
| \(\{1,3\}\) | \(\frac{74x^3+185x^2+156x+44}{6(x+1)(x+2)(2x+1)(3x+2)}\) |
| \(\{1,4\}\) | \(\frac{52x^2+67x+22}{6(x+1)(2x+1)(3x+2)}\) |
| \(\{1,5\}\) | \(\frac{12x+11}{2(2x+1)(2x+3)}\) |
| \(\{2,3\}\) | \(\frac{54x^4+221x^3+325x^2+200x+44}{2(x+1)(x+2)(2x+1)(2x+3)(3x+2)}\) |
| \(\{2,4\}\) | \(\frac{76x^3+150x^2+99x+22}{2(x+1)(2x+1)(3x+2)(4x+3)}\) |

The remaining pairs have reflected values, so \(T_{25}=T_{14}\), \(T_{35}=T_{13}\), \(T_{45}=T_{12}\), and \(T_{34}=T_{23}\). For each pair \(\{1,2\},\{1,3\},\{2,3\},\{2,4\}\), subtracting **each** of \(u(\{1,4\})\) and \(u(\{1,5\})\) gives a rational function whose numerator is a nonzero polynomial in \(x\) with nonnegative coefficients and whose denominator is a product of strictly positive linear factors. For clarity, the numerators (up to a positive constant) for comparison with \(\{1,4\}\) are respectively
\[
x(56x^3+147x^2+114x+28),\quad x^2(11x+7),\quad x(58x^3+165x^2+150x+44),\quad x(5x+4).
\]
For comparison with \(\{1,5\}\), they are respectively
\[
x(36x^4+151x^3+236x^2+168x+44),\quad x(5x+4)(8x^2+13x+4),\quad x(9x^3+28x^2+30x+10),\quad x(8x^3+48x^2+53x+16).
\]
The attached exact-arithmetic script `verify.py` reconstructs every denominator and equality. Therefore only the pairs \(\{1,4\}\), \(\{2,5\}\), and \(\{1,5\}\) can minimize the completion time, with the first two tied by reflection. Their remaining comparison simplifies to
\[
a(T_{15}-T_{14})=\frac{x(4x^2-11x-8)}{6(x+1)(2x+1)(2x+3)(3x+2)}.
\]
The quadratic has exactly one positive root \(x_*=(11+\sqrt{249})/8\), is negative below that root, and positive above it, proving the five-vertex classification with all strictness and equality cases.

Minimality follows by the same recurrence. For \(P_3\), \(a(T_{12}-T_{13})=x/[(x+1)(2x+1)]>0\). For \(P_4\), comparisons with the endpoint pair \(\{1,4\}\), one representative for each nonendpoint reflection class, are
\[
\begin{aligned}
a(T_{12}-T_{14})&=\frac{x(4x+3)}{2(x+1)(x+2)(2x+1)},\\
a(T_{13}-T_{14})&=\frac{x}{2(x+1)(3x+2)},\\
a(T_{23}-T_{14})&=\frac{x}{(x+1)(2x+1)}.
\end{aligned}
\]
All are strictly positive for \(x>0\). On two vertices, both seeds are already adopted and the completion time is zero. This exhausts smaller path orders.

## Verification
Run `python3 verify.py` with Python 3.9 or later; the script is entirely standard-library, evaluates exact rational functions of \(x\), checks all six five-vertex formulas and eight strict pair comparisons symbolically, reconstructs the three- and four-site boundary identities, and independently evaluates all two-seed states for \(n=3,4,5\) at eight positive rational parameter values. It reports `PASS: 37 symbolic identities/positivity statements and 152 independent exact-rational cross-checks.` These finite tests supplement, rather than substitute for, the exact algebraic recurrence and sign proof. At \(x=1\), \(aT_{15}=23/30\) and \(aT_{14}=47/60\), so endpoints win; at larger ratios the sign flips at \(x_*\).

## Relationship to prior work
Bass (1969) establishes a population-level innovation/imitator adoption hazard and its well-mixed diffusion curve. It does not optimize two vertex seeds on a fixed path or the finite Markov completion time. Kreindler and Young (2014) study network diffusion and convergence bounds in a distinct social-choice model, without this exact irreversible Bass five-path optimization. Bertotti and Modanese (2019) analyze heterogeneous mean-field Bass diffusion on scale-free networks and *adoption-peak time*, not exact all-adopted hitting time from two selected seeds. Rossman and Fisher (2021) examine centrality-based seeds under advertising, a closely related intervention question, by network simulations; their abstract and accessible content do not establish the present exact threshold, although incomplete full-text access leaves a priority risk. The structural relationship is to finite-state irreversible pure-birth processes, for which the recurrence above is standard; the asserted new content is the complete parametric optimizer and its minimal five-node switching boundary, not the recursion or the Bass mechanism itself.

## Limitations
The result holds only for homogeneous five-site paths with precisely two seeded adopters and positive constant adoption hazards. It does not imply optimal seed placement for general graphs, altered objective functions, noisy detection, strategic influence, or empirically measured marketing outcomes. A derivation may be equivalent to an earlier exhaustive small-graph or optimal seeding study not found in the inspected literature; scientific priority has not been independently certified.

## References
1. Frank M. Bass, *A New Product Growth for Model Consumer Durables*, *Management Science* 15 (1969), 215–227. https://doi.org/10.1287/mnsc.15.5.215 (publisher issue records public availability January 1, 1969).
2. Gabriel E. Kreindler and H. Peyton Young, *Rapid innovation diffusion in social networks*, *PNAS* (2014). https://doi.org/10.1073/pnas.1400842111.
3. M. L. Bertotti and G. Modanese, *The Bass Diffusion Model on Finite Barabási–Albert Networks*, *Complexity* (2019). https://doi.org/10.1155/2019/6352657.
4. Gabriel Rossman and Jacob C. Fisher, *Network hubs cease to be influential in the presence of low levels of advertising*, *PNAS* 118 (2021), e2013391118. https://doi.org/10.1073/pnas.2013391118.
