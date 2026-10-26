# Two thermal correlation reversals in a frustrated five-path Ising network

## Finding

A zero-field, equal-bond-magnitude Ising network can be anticorrelated at both high and low temperatures yet positively correlated at intermediate temperatures. An explicit five-path example has **exactly two**, not merely at least two, thermal sign reversals; extending its two longest antiferromagnetic paths preserves at least two reversals. In contrast, a network of at most three internally disjoint paths with the same bond magnitude cannot have two such reversals.

Precisely, join two distinct vertices \(u,v\) by five internally vertex-disjoint simple paths of lengths \((2,3,4,d,e)\), where \(9\le d<e\) are integers. Assign bond couplings with absolute value \(J>0\) so that the products of their signs along the five paths are \((-1,+1,+1,-1,-1)\), in that order. For \(T>0\), let \(C_{d,e}(T)=\langle\sigma_u\sigma_v\rangle_T\) denote their zero-field Gibbs correlation, with Boltzmann's constant set to one. **For every \(9\le d<e\), this correlation has at least two distinct sign-changing zeros at finite positive temperatures.**

For the base instance \((d,e)=(9,10)\), there are **exactly two** zeros. Writing \(t=\tanh(J/T)\), their positions are the two simple roots in \((0,1)\) of

\[
Q(t)=t^{18}+t^{16}+t^{14}-t^{13}+t^{12}+t^{10}+t^8+t^6-t^5-t^3-t+1.
\]

They satisfy \(0.7<t_1<0.75<t_2<0.8\), approximately \(t_1=0.706737737193050\) and \(t_2=0.799199522193006\). The correlation is negative on \((0,t_1)\), positive on \((t_1,t_2)\), and negative on \((t_2,1)\). Since \(t\) increases as temperature decreases, these are respectively the high-, intermediate-, and low-temperature regimes. The corresponding temperatures are approximately \(1.135543098\,J\) and \(0.912081971\,J\).

## Assumptions and scope

All graphs are finite, simple, connected, and have no edges other than the five disjoint-terminal paths. Each vertex carries a spin \(\sigma_x\in\{-1,+1\}\). The Hamiltonian is

\[
H(\sigma)=-J\sum_{\{x,y\}\in E}\varepsilon_{xy}\sigma_x\sigma_y,
\qquad \varepsilon_{xy}\in\{-1,+1\},\quad J>0.
\]

There is no magnetic field; all edges have the *same absolute coupling magnitude*. The only information relevant to the endpoint correlation is the sign product on each path. Three of the five path products are negative, including that of the shortest path. This defines a frustrated signed graph, because cycles made from paths with opposite sign products have negative sign product. No infinite-volume phase transition is asserted.

The comparison theorem for at most three paths concerns the same finite-temperature, equal-magnitude, zero-field setup, with any nonzero positive integer path lengths realizing a simple graph, and arbitrary path sign products. It states that the terminal correlation either has fixed sign (possibly identically zero) or changes sign at most once on \(0<T<\infty\).

## Proof

**Path elimination.** Put \(t=\tanh(J/T)\). On any path of length \(\ell\) with coupling sign product \(s\in\{\pm1\}\), summing over all internal spins gives a positive constant independent of \(\sigma_u,\sigma_v\), times \(1+s t^\ell\sigma_u\sigma_v\). To check this, expand every Boltzmann edge factor as \(\cosh(J/T)(1+\varepsilon_{xy}t\sigma_x\sigma_y)\); summing internal spins kills every proper nonempty edge subset of a path, leaving the empty subset and the whole path. Internal spins of distinct paths are disjoint, so the conditional endpoint weights multiply.

Consequently, for arbitrary path lengths \(\ell_i\) and sign products \(s_i\), the exact correlation is

\[
C(t)=\frac{P_+(t)-P_-(t)}{P_+(t)+P_-(t)},\qquad
P_\pm(t)=\prod_i(1\pm s_it^{\ell_i}).
\]

Every factor is positive for \(0<t<1\), so the denominator is strictly positive. Equivalently, \(C(t)=\tanh\bigl(\sum_i s_i\operatorname{arctanh}(t^{\ell_i})\bigr)\).

**All extended instances have at least two reversals.** For lengths \((2,3,4,d,e)\) and signs \((-1,+1,+1,-1,-1)\), the effective coupling is

\[
F_{d,e}(t)=-\operatorname{arctanh}(t^2)+\operatorname{arctanh}(t^3)+\operatorname{arctanh}(t^4)-\operatorname{arctanh}(t^d)-\operatorname{arctanh}(t^e).
\]

As \(t\downarrow0\), \(F_{d,e}(t)=-t^2+O(t^3)<0\). As \(t\uparrow1\), the coefficient of the diverging term \(\frac12\log(1/(1-t))\) is \(-1+1+1-1-1=-1\), hence \(F_{d,e}(t)\to-\infty\). At \(t=3/4\), exact integer evaluation of the rational expression \(P_+-P_-\) is strictly positive for \((d,e)=(9,10)\). Because \(0<t<1\), increasing either of the two longest negative path lengths strictly decreases its negative \(\operatorname{arctanh}(t^\ell)\) contribution in magnitude. Therefore \(F_{d,e}(3/4)>0\) for every \(9\le d<e\). Continuity gives at least one crossing below \(3/4\) and one above it, both necessarily finite and sign-changing.

**The base instance has exactly two.** Direct expansion of the exact correlation numerator at \((d,e)=(9,10)\) factors as

\[
P_+(t)-P_-(t)=-2t^2(1-t^2)^2(1+t^2+t^4)Q(t).
\]

All factors outside \(Q\) have strict, fixed sign on \((0,1)\). Under the bijection \(t=z/(1+z)\) from \(z>0\) to \(0<t<1\), the polynomial \(R(z)=(1+z)^{18}Q(z/(1+z))\) has coefficients in ascending degree order

\[
\begin{split}
(1,17,136,679,2365,6082,11909,18017,21088,18820,\;\\
12267,5145,630,-805,-614,-195,-15,10,4).
\end{split}
\]

There are exactly two sign changes in this coefficient sequence. Descartes' rule of signs therefore bounds the number of positive roots of \(R\), counting multiplicity, by two. Exact rational substitution gives the signs of \(C(t)\) at \(t=7/10,3/4,4/5\) as negative, positive, negative. The intermediate-value theorem forces two different zeros in \((0,1)\). Hence there are precisely two, both simple, and there can be no further zero or tangency in the open interval. This proves the claimed complete thermal sign pattern.

**Why three paths cannot do this.** The result is immediate for at most two paths since \(\operatorname{arctanh}(t^\ell)\) strictly decreases with \(\ell\) at fixed \(0<t<1\). For exactly three paths with mixed signs, interchange signs if necessary so that two are positive and one negative, of length \(c\). If \(c\) is no shorter than one positive path, that path's positive effective coupling dominates the negative one pointwise, so the net effective coupling stays positive. Otherwise both positive path lengths \(a,b\) exceed \(c\). The correlation numerator then has the sign of

\[
t^a+t^b-t^c-t^{a+b+c}.
\]

The polynomial has at most two positive roots by Descartes' rule: coefficients in exponent order have signs \(-,+,+,-\), with possible merging of coincident positive exponents. One root is \(t=1\), and it is simple because the derivative there equals \(-2c\). Thus there is at most one root in \((0,1)\), proving the three-path obstruction. Configurations with all sign products equal never cross zero.

## Verification

The accompanying `verify.py` uses only Python's standard library and exact integer/rational arithmetic. It reconstructs the numerator and the factorization, computes the complete coefficient sequence of \(R\), verifies its two sign variations, and independently checks all three rational sign witnesses. It enumerates every Ising spin configuration of two smaller three-path graphs and compares the direct Gibbs calculation against the general path-elimination formula; it also tests the extension inequality on a finite parameter grid. All checks passed when run from the packaged file. The polynomial sign-variation argument and the continuity argument, rather than the finite grid or root approximations, certify the statements for all allowed lengths and temperatures.

## Relationship to prior work

Tanaka and Miyashita, arXiv:1003.0200, studied frustration-induced nonmonotone thermal correlations for a decorated bond system with a single competing antiferromagnetic direct bond and multiple ferromagnetic length-two paths. Their full text, especially Section II.1 and equations (1)–(4), supplies the most immediate motivation and makes a one-crossing thermal correlation a known precedent. Their specific equal-path decoration does not contain two independent negative long paths and does not imply the claimed twice-reversing equal-magnitude five-path example.

Kobayashi, Fukumoto, and Oguchi, arXiv:0901.3181, studied an Ising model on iterated frustrated diamond hierarchical lattices using effective-coupling recursions; Sections 2–4 describe a different graph and coupling topology, and do not give the explicit five-path sign chart or the two-root certificate here. Jaščur, Štubňa, Szałowski, and Balcerzak, arXiv:1604.03576, examined frustrated decorated mixed-spin lattices with additional multisite interactions and reentrant thermodynamic behavior; that is a different Hamiltonian and observable.

Series/parallel reduction itself is standard and is not claimed as new. The assessed point is the **two distinct thermal sign inversions with all bond magnitudes equal, their exact exhaustive root certificate, and an infinite family of simple frustrated networks realizing the phenomenon**. No claim of all-graph minimality or exhaustive historical priority is made.

## Limitations

The example has 25 vertices, zero external field, two terminals, and a very specific path-sign pattern. The extension proves at least two reversals, not exactly two, when the two longest path lengths are changed. The three-path comparison does not classify every four-path network. There is no infinite-volume phase transition, universality claim, or result for arbitrary bond magnitudes. The root certificate proves zeros of the endpoint correlation only. A broader, potentially unlocated theorem on series-parallel signed-Ising correlations could subsume the construction; independent literature assessment has not been performed.

## References

1. H. Kobayashi, Y. Fukumoto, A. Oguchi, *Frustrated Ising Model on a Diamond Hierarchical Lattice*, arXiv:0901.3181, first public January 21, 2009. https://arxiv.org/abs/0901.3181
2. S. Tanaka, S. Miyashita, *Non-monotonic Dynamics in Frustrated Ising Model with Time-Dependent Transverse Field*, arXiv:1003.0200, first public February 28, 2010. https://arxiv.org/abs/1003.0200
3. M. Jaščur, V. Štubňa, K. Szałowski, T. Balcerzak, *Frustration in an exactly solvable mixed-spin Ising model with bilinear and three-site four-spin interactions on a decorated square lattice*, arXiv:1604.03576, first public April 12, 2016. https://arxiv.org/abs/1604.03576
