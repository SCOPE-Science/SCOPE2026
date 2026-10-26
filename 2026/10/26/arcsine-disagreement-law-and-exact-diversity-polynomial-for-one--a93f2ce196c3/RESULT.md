# Arcsine disagreement law and exact diversity polynomial for one-attacker argumentation

## Finding
Let \(F=(V,R)\) be a finite nonempty abstract argumentation framework in which every vertex has at most one attacker. Write \(\operatorname{Stab}(F)\) for its Dung-stable extensions and let
\[
D_F(y)=\sum_{E,H\in\operatorname{Stab}(F)}y^{|E\triangle H|}.
\]
Pairs are ordered, and identical pairs are included. Suppose the weak components with directed cycles have even cycle lengths and respective **whole-component** cardinalities \(s_1,\ldots,s_c\), including trees attached to those cycles.

**Exact diversity and existence.** An odd directed cycle, including a self-attack, makes the stable-extension set empty. Otherwise
\[
\boxed{D_F(y)=2^c\prod_{i=1}^{c}(1+y^{s_i}).}
\]
Components with no directed cycle contribute a factor of one. Thus the realized distances, including zero, are exactly the subset sums of \(s_1,\ldots,s_c\), and \(\lvert\operatorname{Stab}(F)\rvert=2^c\). Coincident subset sums are correctly counted with multiplicity in the polynomial.

**Exact finite mapping ensemble and limiting law.** For each \(n\ge2\), choose from triples \((f,E,H)\), where \(f:[n]\to[n]\), each vertex \(v\) has the single attacker \(f(v)\), and \(E,H\) are an ordered pair of stable extensions of the resulting framework. Each admissible triple has equal probability. Let \(T(z)\) be the rooted-labelled-tree exponential generating function and \(Q(z)\) the indicated series:
\[
T(z)=ze^{T(z)},\qquad Q(z)=\frac1{1-T(z)^2}=\sum_{m\ge0}q_mz^m.
\]
Then the complete bivariate exponential generating function is
\[
\boxed{\sum_{n\ge0}\frac{z^n}{n!}\sum_{f:[n]\to[n]}D_f(y)=Q(z)Q(zy).}
\]
Here the size-zero summand is the conventional empty mapping with one empty pair; actual random ensembles are taken only for \(n\ge2\). Therefore
\[
\boxed{\#\{(f,E,H):|E\triangle H|=k\}=n!q_kq_{n-k}}
\]
for every \(0\le k\le n\), with \(q_0=1,q_1=0\). For \(m\ge2\), an explicit positive finite sum is
\[
q_m=\sum_{j=1}^{\lfloor m/2\rfloor}
\frac{2j}{m}\frac{m^{m-2j}}{(m-2j)!}.
\]
If \(H_n=|E\triangle H|\) under the uniform-triple law, then
\[
\boxed{\frac{H_n}{n}\ \xrightarrow{d}\ \operatorname{Beta}\!\left(\frac12,\frac12\right)}
\]
with limiting density \(t\mapsto1/(\pi\sqrt{t(1-t)})\) for \(0<t<1\).

## Assumptions and scope
A stable extension is a conflict-free set that attacks every vertex outside it. Self-attacks are permitted in the formal class. The indegree restriction concerns the **number of attackers**, not the number of targets attacked. Both rooted outward trees and even cyclic components with arbitrary attached outward trees occur. The deterministic formula covers all finite nonempty frameworks in this class.

The random ensemble uses functions chosen with their complete stable-extension **pairs**: it is uniform on all triples \((f,E,H)\) of the indicated sort. Equivalently, a function with \(c\) even-cycle components and no odd cycles is sampled with weight \(4^c\), then a pair of its stable extensions is selected uniformly. This is **not** uniform sampling of \(f\) conditioned on existence of some stable extension. The arcsine conclusion must not be transferred to that different sampling scheme without further proof.

## Proof
**1. Componentwise stable assignments.** Let \(p(v)\) be the unique attacker of \(v\), if one exists, and let \(x_v\) be its indicator of membership in a candidate extension. Conflict-freeness and external attack coverage are jointly equivalent to
\[
x_v=1-x_{p(v)}\quad\text{if }p(v)\text{ exists},
\qquad x_v=1\quad\text{otherwise}.
\]
Indeed, an included vertex cannot have its attacker included, and an excluded vertex must have an included attacker. Conversely these local equations imply both global stable-extension conditions. The directed graph following the attacker function has in each weak component one cycle or one terminal undefined parent. An undefined parent fixes the unique assignment on its entire component. A cycle forces alternating membership. If the cycle length is odd this is impossible; if even, either of its two alternating phases propagates uniquely throughout every attached tree. The two phases differ at **every** vertex in that whole weak component. Therefore any two global extensions differ on the union of some subset of even-cycle components, whose sizes are \(s_i\). Each such component contributes exactly two choices with no disagreement and exactly two choices with disagreement of size \(s_i\), so its ordered-pair polynomial is \(2+2y^{s_i}\). Multiplication over independent components proves the diversity formula and the enumeration \(2^c\).

**2. Labelled random-map construction.** Every function \(f:[n]\to[n]\) decomposes uniquely into an unordered collection of components, each a directed cycle of labelled rooted trees (edges pointing from a vertex to its attacker). The rooted tree EGF is \(T=ze^T\). The standard labelled-cycle rule gives an unweighted directed cycle of length \(\ell\) the EGF \(T(z)^\ell/\ell\). Odd-cycle components contribute no stable pairs. An even cycle of length \(2j\) contributes two ordered pairs of equal phases and two ordered pairs of opposite phases. In the former case none of its vertices count toward the disagreement variable; in the latter **all** vertices count. Thus its weighted component EGF equals
\[
\frac{2}{2j}\bigl(T(z)^{2j}+T(zy)^{2j}\bigr).
\]
The labelled SET construction multiplies components and yields
\[
\exp\left(\sum_{j\ge1}\frac{T(z)^{2j}+T(zy)^{2j}}{j}\right)
=\frac1{(1-T(z)^2)(1-T(zy)^2)}.
\]
This proves the exact bivariate identity. Multiplying the two ordinary power series on the right gives \(n!q_kq_{n-k}\) for fixed \((n,k)\). To obtain the finite formula for \(q_m\), expand \(Q(z)=\sum_{j\ge0}T(z)^{2j}\) and apply the Lagrange inversion identity \([z^m]T(z)^r=(r/m)[u^{m-r}]e^{mu}\) for \(1\le r\le m\).

**3. Coefficient asymptotics.** The tree function has dominant singularity \(\rho=e^{-1}\) with the standard square-root expansion in a slit neighbourhood
\[
T(z)=1-\sqrt{2(1-ez)}+O(1-ez).
\]
Consequently
\[
Q(z)=\frac{1}{2\sqrt2}(1-ez)^{-1/2}+O(1),
\]
and the standard singularity-transfer theorem gives
\[
q_m\sim\frac{e^m}{2\sqrt{2\pi m}},\qquad
\sum_{k=0}^{n}q_kq_{n-k}=[z^n]Q(z)^2\sim\frac{e^n}{8}.
\]
For any fixed \(t\in(0,1)\), whenever \(k/n\to t\), division yields the local asymptotic
\[
\Pr(H_n=k)=\frac{q_kq_{n-k}}{[z^n]Q(z)^2}
\sim\frac{1}{\pi n\sqrt{t(1-t)}}.
\]
To justify convergence of the whole distribution, not merely pointwise local convergence away from endpoints, the asymptotic also implies a uniform bound \(q_m\le C e^m/\sqrt{m+1}\) for all nonnegative \(m\). Therefore for \(0<\varepsilon<1/2\), the total normalized mass with \(k\le\varepsilon n\) or \(k\ge(1-\varepsilon)n\) is bounded by \(O(\sqrt\varepsilon)\), uniformly for all sufficiently large \(n\). On the complementary interval the local asymptotic is uniform by standard coefficient estimates, so Riemann sums converge to the stated beta density. Letting \(\varepsilon\downarrow0\) completes weak convergence.

## Verification
A standalone, standard-library-only script, `checker.py`, exhaustively enumerates every parent choice (including no attacker) for all sizes \(1\le n\le5\), independently constructs all stable extensions by the defining Boolean equations, and compares their ordered-pair disagreement histogram against the component prediction. For functional mappings without unattacked vertices it additionally compares the aggregated histogram with \(n!q_kq_{n-k}\), computing \(q_m\) as exact rational coefficients. The packaged script returned `ALL_CHECKS_OK` over 8,496 independent checks. Its finite tests corroborate, but do not replace, the general combinatorial and analytic proofs.

At size five the exact full-mapping pair counts, by disagreement \(k\), are \(1480\) at \(k=0\), \(240\) at \(k=2\), \(240\) at \(k=3\), and \(1480\) at \(k=5\), with zero elsewhere. The four nonzero classes sum to 3,440 ordered pairs across all 3,125 maps.

## Relationship to prior work
Fichte, Hecher, Mahmood and Wang introduced symmetric-difference diversity for abstract argumentation and analysed decision and optimization complexity across semantics. Their May 2026 paper supplies the motivating diversity notion and standard stable semantics, not a one-attacker distance polynomial or a mapping-weighted limiting law. Trinh, Benhamou and Risch (2025) related argumentation extensions to fixed points of Boolean networks and derived cycle-based **upper bounds** for extension counts; their cycle perspective overlaps the deterministic starting point, but does not give the exact disagreement enumerator or random-pair law. The tree/cycle decomposition of random maps, labelled exponential-formula enumeration, Lagrange inversion and square-root singularity transfer are standard, as explained by Flajolet and Odlyzko (1989), rather than separately new contributions here. Combining these ingredients yields the exact diversity distribution and its non-Gaussian limiting form for this logical semantics. Novelty is asserted only relative to the inspected statements, not as absolute priority.

## Limitations
The random limit uses a **pair-size-biased** uniform-triple ensemble, not a uniform framework conditional on existence or a uniformly sampled extension alone. It does not cover unrestricted attack indegrees, nonstable semantics, or conditional selection of two distinct stable extensions. The exact classification assumes finite graphs. Historical results on fixed points of negative Boolean networks and older random-map component-size statistics could imply related formulations; no independence or absolute literature exhaustion is claimed. The separate finite checker is not an infinite certificate.

## References
1. J. K. Fichte, M. Hecher, Y. Mahmood and Z. Wang, *Diversity of Extensions in Abstract Argumentation*, arXiv:2605.13332v1 (first submitted May 13, 2026), https://arxiv.org/abs/2605.13332 .
2. V.-G. Trinh, B. Benhamou and V. Risch, *Graphical Analysis of Abstract Argumentation Frameworks via Boolean Networks*, ICAART 2025, 745–756, DOI:10.5220/0013346400003890, https://www.scitepress.org/publishedPapers/2025/133464/pdf/index.html .
3. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, in *Advances in Cryptology—EUROCRYPT 1989*, 329–354; accessible text at https://scispace.com/pdf/random-mapping-statistics-yjuqfvoh87.pdf .
