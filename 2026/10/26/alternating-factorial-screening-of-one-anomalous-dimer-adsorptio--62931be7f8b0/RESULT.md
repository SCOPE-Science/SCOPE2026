# Alternating factorial screening of one anomalous dimer-adsorption bond

## Finding

Consider irreversible nearest-neighbor dimer adsorption on the initially vacant integer lattice. Every edge attempts deposition at unit rate, except the edge joining vertices 0 and 1, whose rate is \(\lambda>0\). An attempt succeeds exactly when both incident vertices are vacant, after which they remain occupied. Let \(p_j(\lambda)\) be the probability that the edge joining \(j\) and \(j+1\) eventually carries a dimer. Write \(p_*=(1-e^{-2})/2\) for the homogeneous edge-occupation probability.

For every \(\lambda>0\), the defect-edge probability is exactly
\[
p_0(\lambda)=e^{-2}\int_0^1\lambda x^{\lambda-1}e^{2x}\,dx.
\]
For every integer \(j\ge1\), the full spatial response is
\[
 p_j(\lambda)-p_*=
 \frac{(-1)^{j-1}e^{-2}}{(j-1)!}
 \int_0^1\int_0^x e^{x+y}
 (1-\lambda x^{\lambda-1})(x-y)^{j-1}\,dy\,dx.
 \tag{1}
\]
Reflection about the midpoint of the anomalous edge gives \(p_{-j}(\lambda)=p_j(\lambda)\) for \(j\ge1\); note that the reflection sends edge index \(j\) to \(-j\), when the anomalous edge is regarded as index zero and the distance label of other edges is the number of edges beyond it.

For all \(\lambda\ne1\) and all \(j\ge1\), the response is strictly sign-alternating:
\[
 \operatorname{sgn}(p_j(\lambda)-p_*)=(-1)^j\operatorname{sgn}(\lambda-1),
 \qquad \operatorname{sgn}(p_0(\lambda)-p_*)=\operatorname{sgn}(\lambda-1).
 \tag{2}
\]
It obeys the uniform bound \(|p_j(\lambda)-p_*|\le1/j!\). More sharply, **for each fixed \(\lambda\ne1\)**,
\[
 \boxed{\displaystyle
 p_j(\lambda)-p_*
 \sim \frac{(-1)^j(\lambda-1)e^{-1}}{(j+1)!}
 \quad(j\to\infty).}
 \tag{3}
\]
Thus a single kinetic defect induces an exact alternating response whose amplitude has an explicitly determined factorial-distance tail. Equation (3) is an asymptotic in distance at fixed defect rate, not an estimate uniform in \(\lambda\).

## Assumptions and scope

The state space is \(\mathbb Z\) with edge \(e_i=\{i,i+1\}\). For each integer \(i\), use an independent homogeneous Poisson attempt process of rate \(r_i\), where \(r_0=\lambda\) and \(r_i=1\) otherwise. Every vertex starts vacant. At an arrival at \(e_i\), deposit a permanent dimer only if both endpoints are vacant; failed arrivals make no change. Successful deposition at an edge occurs at most once. The infinite-volume process is defined by its graphical local limit; every finite set of edges has a well-defined final state. All assertions concern the probability of permanent occupation **of an edge**, rather than the probability that its endpoints are occupied by possibly different dimers.

The exact formulas hold for all real \(\lambda>0\) and every integer \(j\ge0\). Both the nonzero sign and the sharp asymptotic require \(\lambda\ne1\); at \(\lambda=1\) all responses vanish identically. No spatial periodicity or finite-volume thermodynamic approximation is assumed.

## Proof

**Graphical construction and the first clock.** Assign every edge an independent first-attempt time \(T_i\sim\operatorname{Exp}(r_i)\). If its first attempt fails because an endpoint is occupied, every later attempt also fails. Thus the final dimer matching is exactly the random greedy matching obtained by processing edges in increasing first-attempt times. For any fixed finite horizon, a decision depending on a finite region can be influenced from outside a distance \(k\) only along a chain of at least \(k\) strictly decreasing attempt times. With \(R=\max(1,\lambda)\), the probability of such a chain up to time \(t\) is bounded by a constant times \(2^k(Rt)^k/k!\). This tends to zero, and letting the horizon increase gives an almost-surely well-defined infinite-volume matching. The same argument justifies decoupling the two half-lines when a given edge is removed.

**Homogeneous half-line cavity.** Let \(f(t)\) be the probability that the endpoint of a vacant semi-infinite chain remains vacant at time \(t\) under unit-rate dimer deposition. For \(m\ge1\), let \(F_m(t)\) denote the probability that its first \(m\) vertices remain vacant. Directly enumerating attempts that intersect that empty block gives
\[
 F_m'(t)=-(m-1)F_m(t)-F_{m+1}(t),\qquad F_m(0)=1.
\]
Indeed, \(m-1\) internal edges can deposit, and the one external edge at the remote boundary can deposit if an additional vertex is vacant. The functions
\[
 F_m(t)=e^{-(m-1)t}f(t),\qquad
 f(t)=\exp(e^{-t}-1),
\]
satisfy these equations. Uniqueness follows by finite-volume graphical construction and the uniform tail bound for dependent events, so this is the actual cavity vacancy probability. Equivalently, \(f'(t)=-e^{-t}f(t)\), \(f(0)=1\).

For a homogeneous edge, conditional on its first attempted deposition at time \(t\), its endpoints are vacant precisely when the two independent half-line cavities are vacant. Hence its success probability is
\[
 \int_0^\infty e^{-t}f(t)^2\,dt
 =e^{-2}\int_0^1e^{2x}\,dx=\frac{1-e^{-2}}2=p_*.
\]
With rate \(\lambda\) on edge zero, the same independence gives
\[
 p_0(\lambda)=\int_0^\infty\lambda e^{-\lambda t}f(t)^2\,dt
 =e^{-2}\int_0^1\lambda x^{\lambda-1}e^{2x}\,dx.
\]

**Exact localized cavity recurrence.** For \(j\ge1\), delete edge \(e_j\), and let \(q_j(t)\) denote the vacancy probability of its left endpoint \(j\) in the left half-chain containing all edges \(e_i\) with \(i<j\). The right endpoint sees an independent homogeneous half-line with vacancy probability \(f(t)\). Consequently
\[
 p_j(\lambda)=\int_0^\infty e^{-t}f(t)q_j(t)\,dt.
 \tag{4}
\]
The first left cavity has only the anomalous edge between its boundary vertex and the remainder, yielding
\[
 q_1(t)=1-\int_0^t\lambda e^{-\lambda s}f(s)\,ds.
\]
For \(j\ge1\), the added edge to the next boundary vertex has unit rate, so
\[
 q_{j+1}(t)=1-\int_0^t e^{-s}q_j(s)\,ds.
 \tag{5}
\]
Subtract the homogeneous identity \(f(t)=1-\int_0^t e^{-s}f(s)\,ds\), and write \(\delta_j=q_j-f\). We obtain
\[
 \delta_1(t)=\int_0^t f(s)(e^{-s}-\lambda e^{-\lambda s})\,ds,
 \qquad
 \delta_{j+1}(t)=-\int_0^t e^{-s}\delta_j(s)\,ds.
 \tag{6}
\]
Iterating the second Volterra operator gives
\[
 \delta_j(t)=\frac{(-1)^{j-1}}{(j-2)!}\int_0^t e^{-s}\delta_1(s)
 (e^{-s}-e^{-t})^{j-2}\,ds\qquad(j\ge2).
\]
Inserting this into (4), applying Tonelli to its positive and negative integrable parts, then substituting \(x=e^{-s}\), \(y=e^{-t}\), and simplifying the iterated Volterra kernel yields (1). The integrand is absolutely integrable even if \(0<\lambda<1\): its only power singularity at \(x=0\) is integrable.

**Strict alternating signs.** Put \(D_\lambda(t)=\int_0^t \lambda e^{-\lambda s}f(s)\,ds\). Using integration by parts,
\[
 D_\lambda(t)=f(t)(1-e^{-\lambda t})-\int_0^t f'(s)(1-e^{-\lambda s})\,ds.
\]
Because \(f(t)>0\) and \(f'(t)<0\) for \(t>0\), the right side is strictly increasing in \(\lambda\) for every fixed \(t>0\). Therefore \(\delta_1=q_1-f=D_1-D_\lambda\) has strict sign opposite to \(\lambda-1\) throughout \(t>0\). Successive applications of (6) reverse that sign, and the positive kernel in (4) preserves it. This gives the first part of (2). The defect-edge success probability is strictly increasing in its rate because its first clock gets stochastically earlier, while the independent, positive cavity factor \(f(t)^2\) is decreasing; hence the second part of (2).

**Uniform bound and sharp factorial coefficient.** All \(q_j\) and \(f\) are probabilities, so \(|\delta_1(t)|\le1\). By induction in (6),
\[
 |\delta_j(t)|\le\frac{(1-e^{-t})^{j-1}}{(j-1)!},
 \qquad
 |p_j-p_*|\le\frac1{j!}.
\]
For the sharper limit, write \(G_\lambda(x,y)=e^{x+y}(1-\lambda x^{\lambda-1})\). Since
\[
 \int_0^1\int_0^x(x-y)^{j-1}\,dy\,dx=\frac1{j(j+1)},
\]
the probability measure on the triangle with density proportional to \((x-y)^{j-1}\) concentrates at its unique maximizer \((x,y)=(1,0)\). Consequently,
\[
 j(j+1)\int_0^1\int_0^xG_\lambda(x,y)(x-y)^{j-1}\,dy\,dx
 \longrightarrow G_\lambda(1,0)=e(1-\lambda).
\]
The concentration remains valid for \(0<\lambda<1\), because the integrable singularity near \(x=0\) is separated from the maximizing corner and is exponentially suppressed after normalization. Multiplying by \((-1)^{j-1}e^{-2}/(j-1)!\) proves (3).

## Verification

The standalone script `verify_defect.py` independently computes exact rational random-greedy probabilities for finite paths by conditioning on their earliest available edge. It also evaluates (1) and the defect formula by quadrature, tests reflection and strict response alternation in the interior of long finite paths, compares finite and infinite values at fixed interior distances, and checks the predicted sharp factorial coefficient with a stable normalized triangular integral. Run with `python verify_defect.py`; dependencies are declared in `requirements.txt`.

Finite-path calculations are numerical and exact-rational consistency checks, not proofs of the infinite-volume statements. All infinite-volume steps and the factorial limit are proved above. The bounded-distance checks do not themselves establish the large-distance asymptotic.

## Relationship to prior work

Classical homogeneous one-dimensional random sequential dimer adsorption, treated by Flory and Cohen–Reiss and reviewed by Evans, gives the baseline jamming value. Lee's impurity analysis (arXiv:cond-mat/9701167, first public 1997-01-22) solves homogeneous deposition after randomly distributed preadsorbed impurities; its disorder is in the **initial configuration**, and it does not give the response to one changed **arrival rate on a designated edge**. Schmidt's density-functional treatment (2002) studies spatially inhomogeneous adsorption near boundaries but gives approximate density-functional predictions for higher-dimensional substrates rather than the exact lattice rate-defect response. Neugebauer and Taraskin (arXiv:0806.0131) study rates depending on neighboring occupancy under translation-invariant cooperative adsorption; those do not specify a single fixed edge with a different clock rate.

A directly relevant earlier article is Stacchiola et al., *Cooperative sequential adsorption processes on heterogeneous substrates* (1998), DOI 10.1063/1.475545. Its abstract explicitly states that exact one-dimensional heterogeneous dimer adsorption is treated. Its full text could not be obtained. The present specifically claimed advance is the strict **alternating-sign** response at every distance and **sharp fixed-rate factorial tail with coefficient \(e^{-1}(\lambda-1)\)** for a single kinetic defect. No assertion is made that general heterogeneous RSA is new, and the inaccessible paper remains a substantial priority risk; a more general theorem there could imply some or all of these formulas. This uncertainty is separate from the self-contained proof here. A related Stacchiola–Eggarter–Zgrablich work concerns periodically repeating patches, which do not include a solitary nonperiodic defect as a special finite-period instance.

## Limitations

The theorem concerns a single rate-anomalous edge on an infinite, initially vacant, one-dimensional lattice with irreversibly deposited nearest-neighbor dimers and independent memoryless attempt clocks. It does not classify multiple anomalies, arbitrary nonperiodic rate sequences, higher-dimensional lattices, fluctuating impurities, or correlation functions of distinct accepted edges. The factorial prefactor is asserted only at fixed \(\lambda\), not uniformly as \(\lambda\) varies with distance. Full-text inaccessibility of the close 1998 heterogeneous-dimer reference limits claims of historical priority; independent validation has not been performed.

## References

1. J. W. Lee, *Effects of Impurities in Random Sequential Adsorption on a One-Dimensional Substrate*, arXiv:cond-mat/9701167 (first posted January 22, 1997), https://arxiv.org/abs/cond-mat/9701167.
2. D. J. Stacchiola, M. Ciacera, C. Zuppa, T. P. Eggarter, and G. Zgrablich, *Cooperative sequential adsorption processes on heterogeneous substrates*, J. Chem. Phys. 108, 1730–1739 (1998), https://doi.org/10.1063/1.475545. Abstract inspected; full text inaccessible.
3. M. Schmidt, *Density functional theory for random sequential adsorption*, J. Phys.: Condens. Matter 14, 12119–12127 (2002), https://www.mschmidt.uni-bayreuth.de/pubs/MS33.pdf.
4. C. J. Neugebauer and S. N. Taraskin, *Cooperative sequential adsorption with nearest-neighbor exclusion and next-nearest neighbor interaction*, arXiv:0806.0131 (2008), https://arxiv.org/abs/0806.0131.
5. J. W. Evans, *Random and cooperative sequential adsorption*, Rev. Mod. Phys. 65, 1281–1329 (1993), https://doi.org/10.1103/RevModPhys.65.1281.
