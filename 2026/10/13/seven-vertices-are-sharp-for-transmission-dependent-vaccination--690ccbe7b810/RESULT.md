# Seven vertices are sharp for transmission-dependent vaccination against three-case outbreaks

## Finding

**Theorem (sharp minimum order and exact switch).** Let \(T\) be any finite simple undirected tree with \(2\le n\le7\) vertices. Vaccinate exactly one vertex \(v\) by removing it before exposure. Independently retain each edge of the remaining forest with probability \(p\in(0,1)\), choose one outbreak seed uniformly from the remaining \(n-1\) vertices, and let \(R_v(p)\) be the probability that the seed's open-edge component contains at least three vertices. For every tree of order \(2\le n\le6\), a single vertex minimizes \(R_v(p)\) simultaneously for all \(p\in(0,1)\). Exactly one of the eleven unlabelled trees of order seven lacks a parameter-independent optimum.

The exceptional tree consists of two degree-three hubs joined through one degree-two bridge vertex, with two leaves attached to each hub. For a bridge \(c\), hub \(h\), or leaf \(\ell\), the exact risk is
\[
R_c(p)=p^2,\qquad
R_h(p)=\frac{p^2(9-5p)}6,\qquad
R_\ell(p)=\frac{p^2(15-11p+2p^2)}6.
\]
Consequently, the bridge is uniquely optimal for \(0<p<3/5\), the bridge and both hubs are tied at \(p=3/5\), and exactly the two hubs are optimal for \(3/5<p<1\). Every leaf is strictly worse than every hub and the bridge for all \(p\in(0,1)\). Thus seven is the minimum network order for a change in the best one-dose vaccination site under this three-case tail-risk objective.

## Assumptions and scope

The contact network is a simple undirected tree, the vaccine gives complete immunity to exactly one preselected individual and removes its incident contacts, all surviving edges are independently open with a common \(p\in(0,1)\), and the seed is uniform **after vaccination** over the \(n-1\) susceptible individuals. The outbreak size is the size of the seed-containing open-edge component. These rules give the independent-contact Reed–Frost bond-percolation model; they do not assert independent outgoing transmissions for continuous-time Markov SIR with a shared infectious period. The threshold is the event \(|\text{outbreak}|\ge3\), not the expectation or variance of outbreak size, nor the probability of reaching a prescribed fraction of a large population.

## Proof

**Exact probability formula.** Let \(F=T-v\), let \(N=n-1\), and write \(d_x\) for the degree of \(x\) in \(F\). For a uniformly chosen seed \(x\), its open component has size one precisely when all \(d_x\) incident edges are closed, with probability \((1-p)^{d_x}\). It has size exactly two precisely when some neighbor \(y\) is connected by the single open edge \(xy\) and all other edges incident to \(x\) or \(y\) are closed. The events for different \(y\) are disjoint. Because \(F\) is a forest there are no triangles, and the probability for a given \(y\) is \(p(1-p)^{d_x+d_y-2}\). Thus, for every finite tree and every \(p\in[0,1]\),
\[
N R_v(p)=\sum_{x\in V(F)}\left[1-(1-p)^{d_x}-p\sum_{y\sim_F x}(1-p)^{d_x+d_y-2}\right]. \tag{1}
\]
The formula is exact, without asymptotic approximation, and provides an integer-coefficient polynomial after multiplication by \(N\).

**Exhaustive proof through seven vertices.** Prüfer's bijection generates exactly \(n^{n-2}\) distinct labeled trees on \(n\) vertices; the edge cases \(n=2\) and \(n=3\) are included. The standalone verification code enumerates all such trees for every \(n\in\{2,3,4,5,6,7\}\), groups them by a canonical unrooted-tree encoding (iterated removal of leaves to the unique center or two centers, with sorted recursively encoded rooted branches), and selects one representative from each isomorphism class. It obtains exactly \(1,1,2,3,6,11\) classes, respectively: \(24\) in total, from \(18{,}248\) labeled trees.

For each representative, formula (1) gives polynomials \(N R_v(p)\) for all vaccinee vertices. To certify a fixed optimal vertex \(v\), subtract its risk polynomial from each competitor \(u\)'s, obtaining \(f_{u,v}(p)\). Remove any initial power of \(p\), since \(p>0\), and write the remaining polynomial \(g(p)=\sum_{j=0}^m a_jp^j\). An exact sufficient certificate for \(g(p)\ge0\) throughout \(0\le p\le1\) is that every coefficient of \((1+t)^m g(t/(1+t))\) be nonnegative. These transformed coefficients are the integers
\[
b_k=\sum_{j=0}^{k} a_j\binom{m-j}{k-j},\qquad 0\le k\le m. \tag{2}
\]
Indeed \(t=p/(1-p)>0\) and the denominator \((1+t)^m\) is positive. Each of the \(23\) nonexceptional representative trees has a candidate \(v\) for which all transformed difference coefficients are nonnegative for every competitor; the executable code gives a finite, exhaustive exact certificate, not sampled parameter values. The exceptional representative has no such candidate; the explicit comparisons below establish that it truly has no fixed optimum (rather than merely failing the sufficient certificate).

**Exceptional shape and crossover.** Label its edges \(01,02,03,34,45,46\): hubs \(0,4\), bridge \(3\), and leaves \(1,2,5,6\). Direct substitution of these degrees into (1) gives the three polynomials in the theorem. Their exact differences factor as
\[
R_h(p)-R_c(p)=\frac{p^2(3-5p)}6,\qquad
R_\ell(p)-R_c(p)=\frac{p^2(1-p)(9-2p)}6,
\]
\[
R_\ell(p)-R_h(p)=\frac{p^2(6-6p+2p^2)}6.
\]
For \(0<p<1\), the last two quantities are strictly positive, while the first changes sign precisely once at \(p=3/5\). This proves both the complete optimizer set and the minimum-order assertion.

## Verification

Execute `python3 verify_tail_vax.py` with Python 3.10 or later and no nonstandard dependencies. The script independently enumerates all labeled Prüfer trees through seven vertices; identifies unlabeled shapes; builds each risk polynomial from local degrees; proves polynomial comparisons using integer coefficients from (2); and directly enumerates open-edge subsets for every vaccinee of the exceptional tree at five exact rational transmission probabilities. Expected output:

`VERIFY_OK shape_counts={2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11} exact_stable_shapes=23 exceptional_seven_shape=1 witness_reconstructions=35 crossover=3/5`

The enumeration is exhaustive **only** for trees of order at most seven. The polynomial certificate is exact for every real parameter in the stated open interval; the thirty-five independent reconstructions cross-check the formula but are not a substitute for the coefficient proof.

## Relationship to prior work

Schneider et al. study containment using limited immunization under percolation and large-network component-based criteria. Holme gives exact small-graph SIR investigations and compares node-importance criteria. Altarelli et al. optimize epidemic containment by message passing. These results motivate single-site containment and distinguish objectives; none of the inspected material supplies the minimum-order classification here for the **three-infection tail event** under a uniformly chosen post-vaccination seed. Optimizing expected outbreak size, detection probability, or the largest susceptible cluster does not imply the present optimizer sets because the objective functionals differ. A previously established but unlocated specialized classification for this exact event could nevertheless cover the theorem.

## Limitations

This finite theorem says nothing about the presence, count, or topology of changing optimizers for eight or more vertices, connected graphs with cycles, multiple vaccinees, heterogeneous or dependent contacts, uncertain or nonuniform seeds, or continuous-time SIR with shared recovery clocks. It concerns an idealized three-case threshold, not empirical vaccine efficacy or incidence reduction. The literature comparison is not a proof of absolute novelty; no independent mathematical audit has been performed.

## References

1. C. M. Schneider, T. Mihaljev, S. Havlin, H. J. Herrmann, *Suppressing Epidemics with a Limited Amount of Immunization Units*, arXiv:1102.1929, first public 2011-02-09. https://arxiv.org/abs/1102.1929
2. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456. https://arxiv.org/abs/1708.06456
3. F. Altarelli et al., *Containing Epidemic Outbreaks by Message-Passing Techniques*, *Physical Review X* 4, 021024 (2014). https://doi.org/10.1103/PhysRevX.4.021024
