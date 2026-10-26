# Sharp delay of epidemic extinction after single-vertex vaccination

## Finding

In a finite directed, one-round-infective SIR network with one initially infectious seed, consider a *fixed* realization of successful contacts. Let \(T\) be the last generation in which anyone first becomes infected, with the seed infected in generation zero. Vaccinating one other vertex before introduction can increase \(T\), even though it cannot increase the set of infected individuals in this time-independent-contact model.

**Sharp population-size theorem.** On every \(n\)-vertex directed network and every fixed contact realization, the increase in \(T\) caused by vaccinating one initially susceptible vertex is at most \(\max\{0,n-4\}\). For \(n\le4\) it is never positive. For each \(n\ge5\) a deterministic directed network attains an increase of exactly \(n-4\), while vaccination removes precisely one infection.

**Stochastic five-person threshold.** Label five people \(s,v,a,b,t\), start infection at \(s\), and allow only the directed contacts \(s\to v\), \(s\to a\), \(v\to b\), \(v\to t\), \(a\to b\), and \(b\to t\). Independently, each directed contact succeeds with the same probability \(p\in[0,1]\). Let \(T_0\) be the last-infection generation without vaccination and \(T_v\) that after perfect pre-exposure vaccination of \(v\). Then

\[
\mathbb E[T_v]-\mathbb E[T_0]
=-p\bigl(p^5-p^4-3p^3+p+1\bigr).
\]

The quintic \(Q(p)=p^5-p^4-3p^3+p+1\) has precisely one root \(p_c\) in \((0,1)\), with \(0.83659<p_c<0.83660\). Hence vaccination strictly shortens the mean last-infection generation for \(0<p<p_c\), ties it at \(p=p_c\), and strictly *lengthens* it for \(p_c<p\le1\). At \(p=0\) both durations vanish. At \(p=1\), vaccination changes the last infection generation from \(2\) to \(3\), while preventing one infection. No vaccinated vertex increases any other vertex's probability of ever becoming infected in this model.

## Assumptions and scope

A contact graph is finite, directed, and loop-free, of order \(n\ge2\). The seed \(s\) is distinct from the vaccinated vertex \(v\). Every individual is infectious for exactly one generation following first infection and is thereafter permanently removed. Each edge has a fixed (calendar-time-independent) probability of transmitting if its source is infectious and its target susceptible. Successful edges are sampled independently at the beginning, and the same realization is used with and without vaccination (standard live-edge coupling). Perfect vaccination suppresses infection and onward transmission at \(v\). All other initial vertices are susceptible. For the sharp deterministic bound, edge probabilities may be arbitrary, including zero and one; for the five-person formula all six allowed edges share the one value \(p\).

For any live directed graph \(G\), write \(d_G(s,u)\) for the minimum number of live directed edges in a path from \(s\) to \(u\), and set it to infinity if there is no path. Then \(T(G)=\max\{d_G(s,u):d_G(s,u)<\infty\}\), so \(T(G)\) is a last-*infection* generation, not the first all-recovered generation. The latter is \(T(G)+1\), and the vaccination difference is unchanged. When vaccinated, all edges incident to \(v\) are deleted.

## Proof

**Live-edge reduction.** Each edge can be used at most once. Expose independently at the outset whether it would transmit. By induction on generations, exactly the vertices at directed distance \(j\) from \(s\) first become infectious in generation \(j\). Paths cannot spread through an already recovered vertex because a shorter path would have infected its endpoint earlier. Thus last-infection generation equals the maximum finite shortest-path distance, and vertex deletion cannot create an additional infected vertex.

**Universal upper bound.** In the vaccinated graph there are at most \(n-1\) vertices, so any finite shortest path from \(s\) uses at most \(n-2\) edges; hence \(T_v\le n-2\). If the original epidemic has \(T_0\le1\), every vertex infected after vaccination was either \(s\) or a direct live out-neighbor of \(s\), since vertex deletion never creates new reachability. Every such direct edge survives vaccination, so \(T_v\le1\), making a positive delay impossible. Therefore any positive delay must have \(T_0\ge2\); combining this with \(T_v\le n-2\) yields \(T_v-T_0\le n-4\). This also gives the nonpositive conclusion when \(n\le4\).

**Sharpness for every \(n\ge5\).** Use vertices \(s,v,x_1,\ldots,x_{n-2}\) and exactly the following deterministic arcs: \(s\to v\), \(s\to x_1\), the chain \(x_i\to x_{i+1}\) for \(1\le i<n-2\), and shortcuts \(v\to x_i\) for \(2\le i\le n-2\). Initially \(v\) and \(x_1\) are infected in generation one and all other \(x_i\) in generation two: \(T_0=2\). After vaccinating \(v\), the full chain alone infects \(x_i\) in generation \(i\); hence \(T_v=n-2\). Every \(x_i\) remains infected, and only the vaccinated \(v\) is spared. This realizes the bound.

**Exact five-person polynomial.** For the six-edge graph named above, conditioned on successful edges, the infection generation is their directed live-distance. By the tail-sum identity for integer-valued \(T\), \(\mathbb E[T]=\sum_{j\ge1}\Pr(T\ge j)\). Vaccinating \(v\) leaves only the three-edge chain \(s\to a\to b\to t\), giving

\[
\mathbb E[T_v]=p+p^2+p^3.
\]

Without vaccination, the following events characterize its three nonzero tails:

\[
\begin{aligned}
\Pr(T_0\ge1)&=2p-p^2,\\
\Pr(T_0\ge2)&=3p^2-p^3-2p^4+p^5,\\
\Pr(T_0\ge3)&=2p^3-p^4-2p^5+p^6.
\end{aligned}
\]

For the second tail, at least one of \(s\to v\to b\), \(s\to v\to t\), or \(s\to a\to b\) must transmit. For the third, \(b\to t\) transmits in generation three, \(b\) was reached by at least one two-edge route, and \(t\) was *not* already reached through \(s\to v\to t\) in generation two. Inclusion-exclusion on these six independent edges gives the displayed probabilities. Their sum is

\[
\mathbb E[T_0]=2p+2p^2+p^3-3p^4-p^5+p^6.
\]

Subtracting gives the claimed quintic expression. Finally, \(Q(0)=1\), \(Q(1)=-1\), and

\[
Q''(p)=2p(10p^2-6p-9)<0\quad(0<p<1).
\]

Indeed, \(10p^2-6p-9\) is convex and negative at both endpoints of \([0,1]\). Thus \(Q'\) is strictly decreasing, with \(Q'(0)=1\) and \(Q'(1)=-7\): \(Q\) first rises and then falls, crossing zero exactly once. Exact rational substitution at \(p=83659/100000\) and \(p=83660/100000\) brackets this zero. The sign of \(-pQ(p)\) proves the threshold classification.

## Verification

The standalone, standard-library-only program `verify.py` independently enumerates all \(2^6=64\) live-edge configurations of the five-person contact graph and recovers the exact polynomial coefficients. It exhaustively checks the no-positive-delay assertion for every directed graph on two, three, or four labeled vertices and every nonseed vaccinated vertex; confirms deterministic sharpness on the explicit families of sizes five through sixty; and checks 999 rational choices of \(p\) against the derived expectation formulas. The general upper bound and the root uniqueness use the written proofs and do not rely on finite computation.

Run with `python verify.py` in the directory containing this file and `verify.py`.

## Relationship to prior work

Floyd, Kay and Shapiro establish the directed live-edge coupling and shortest-path infection-time identity (their Lemma 3.5) and prove that pre-exposure vaccination cannot increase anyone else's ultimate infection probability under time-independent transmission. Those basic identities and the no-collateral-infection fact are prior results. They do not supply the present sharp \(n-4\) maximum increase of *last-infection generation*, its attaining family, or the five-person homogeneous-transmissibility quintic threshold.

Pulliam, Dushoff, Levin and Dobson previously demonstrate that population-level immunity can sometimes lengthen epidemics under turnover/reintroduction dynamics. Thus the broad phenomenon that interventions can lengthen epidemic duration is **not** claimed new. Their well-mixed turnover models neither give fixed-network shortest-path bounds nor evaluate the five-person Reed–Frost polynomial. Gutfraind proves monotonicity of *final outbreak size* in an allied discrete network model; final size and time to last infection are different observables. Holme (2013) explicitly links network epidemic extinction time to source eccentricity and studies its nonmonotone dependence on transmissibility, without assessing vertex vaccination, the exact worst-case delay, or the five-person intervention threshold. The present finding isolates their opposition at a sharp network-size boundary and a sharp stochastic transmission threshold.

## Limitations

The bound concerns a single vaccinated nonseed and a single infection seed with fixed one-generation infectious duration. The polynomial concerns exactly the specified six-edge directed graph, not all five-person graphs or undirected contacts. It neither implies an increase in infections nor recommends withholding vaccination; it illustrates a finite-model duration metric that need not improve monotonically. Real outbreaks have variable latent/infectious periods, contact changes, and different objectives. Literature comparisons are extensive but cannot certify historical priority against every graph-theoretic or epidemiological result; the original shortest-path representation is explicitly credited.

## References

1. Pulliam, J. R. C., Dushoff, J. G., Levin, S. A. and Dobson, A. P. (2007). *Epidemic Enhancement in Partially Immune Populations*. PLOS ONE 2(1):e165. Published 2007-01-17. DOI: 10.1371/journal.pone.0000165.
2. Floyd, W., Kay, L. and Shapiro, M. (2008). *Some Elementary Properties of SIR Networks or, Can I Get Sick because You Got Vaccinated?* Bulletin of Mathematical Biology 70:713–727. Online publication 2007-12-01. DOI: 10.1007/s11538-007-9275-0. Author full text: https://personal.math.vt.edu/floyd/research/papers/epidemics.pdf.
3. Gutfraind, A. (2011). *Monotonic and Non-Monotonic Epidemiological Models on Networks*. arXiv:1005.3470, originally submitted 2010-05-19; version 2 dated 2011-05-25.
4. Holme, P. (2013). *Extinction Times of Epidemic Outbreaks in Networks*. PLOS ONE 8(12):e84429. DOI: 10.1371/journal.pone.0084429. Full text: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0084429.
5. Rock, K., Brand, S., Moir, J. and Keeling, M. J. (2014). *Dynamics of Infectious Diseases*. Reports on Progress in Physics 77:026602. DOI: 10.1088/0034-4885/77/2/026602. Considered as broader duration-oriented background, not mathematical coverage of the claimed bound.
