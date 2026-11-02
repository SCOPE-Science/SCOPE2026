# Exact arclength-distance law and likelihood-ratio ordering for projective-plane incidence networks

## Finding

Let \(\Pi\) be **any** finite projective plane of order \(q\geq 2\), including a non-Desarguesian plane when one exists. Replace every incidence edge of its point–line graph by an interval of length \(1\), and choose two independent points \(X,Y\) uniformly with respect to total edge arclength. Write \(D_q=d(X,Y)\) for the intrinsic shortest-path distance and \(m=(q+1)(q^2+q+1)\) for the number of edges.

**Exact complete distribution.** The law is absolutely continuous, supported on \([0,3]\), with density
\[
 f_q(t)=\frac{2q^j}{m}\bigl[1+(q-1)(t-j)\bigr],\qquad j<t<j+1,\quad j\in\{0,1,2\}.
\]
The three pieces agree at their common boundaries; the value assigned to the density at an integer is immaterial. Equivalently, the cumulative distribution is \(0\) below \(0\), \(1\) above \(3\), and
\[
 F_q(t)=\frac1m\begin{cases}
 2t+(q-1)t^2,&0\le t\le1,\\
 1+2q\left(1-\frac{(2-t)^2}{2}\right)+q^2(t-1)^2,&1\le t\le2,\\
 1+2q+2q^2\left(1-\frac{(3-t)^2}{2}\right)+q^3(t-2)^2,&2\le t\le3.
 \end{cases}
\]
The expressions match exactly at \(t=1,2\).

**All-order comparison.** If \(2\le q<r\) are orders for which projective planes exist, then \(f_r(t)/f_q(t)\) is strictly increasing on \((0,3)\). Thus \(D_r\) strictly dominates \(D_q\) in first-order stochastic order:
\[
 F_r(t)<F_q(t)\qquad(0<t<3).
\]
The mean, second moment, variance, and one-Wasserstein separation are
\[
 \begin{aligned}
 \mu_q=\mathbb E D_q&=\frac{(2q+1)^3}{3m},\\
 \mathbb E D_q^2&=\frac{43q^3+50q^2+14q+1}{6m},\\
 \operatorname{Var}(D_q)&=\frac{(q^2+4q+1)(q^4+20q^3+39q^2+20q+1)}{18m^2},\\
 W_1\bigl(\mathcal L(D_q),\mathcal L(D_r)\bigr)&=\mu_r-\mu_q.
 \end{aligned}
\]
For \(0<\varepsilon<1\), the exact maximal-distance tail is
\[
 \Pr(D_q>3-\varepsilon)=\frac{2q^3\varepsilon-q^2(q-1)\varepsilon^2}{m}.
\]
As \(q\) tends to infinity through existing projective-plane orders (for instance prime powers), the distributions converge in total variation to the triangular density \(2(t-2)\mathbf1_{(2,3)}(t)\). In fact the total-variation distance is at most \((2q^2+2q+1)/m\).

## Assumptions and scope

A finite projective plane of order \(q\) has \(v=q^2+q+1\) points and \(v\) lines; every line contains exactly \(q+1\) points, every point is on exactly \(q+1\) lines, any distinct points determine one line, and any distinct lines intersect in one point. Its incidence graph has two vertex classes (points and lines), with one edge precisely when the point lies on the line. All \(m=v(q+1)\) edges have exactly unit length. Arclength-uniform means choosing an edge uniformly among the \(m\) edges and then independently choosing a uniform coordinate on that edge. The two sampled points are independent. Distances use the entire continuous metric graph, not only its vertices. Nothing asserts existence of a plane for a prohibited or unknown order.

## Proof

**1. Four ordered-edge classes.** Fix an incidence edge \(e=(p,\ell)\). There is \(1\) identical edge and exactly \(2q\) other edges sharing an endpoint. An edge \(f=(p',\ell')\) disjoint from \(e\) may have a cross incidence \(p\in\ell'\), which gives \(q\) choices for \(\ell'\ne\ell\) and, on each such line, \(q\) choices for \(p'\ne p\), hence \(q^2\) edges. The symmetric cross incidence \(p'\in\ell\) gives another \(q^2\). Both cross incidences cannot simultaneously hold, since two distinct points have a unique common line. All remaining \(m-1-2q-2q^2=q^3\) edges are disjoint with no cross incidence. These counts are the same for every choice of \(e\), without any transitivity assumption on the plane.

**2. Geodesic classification.** The graph distance between two distinct point vertices is \(2\), as is that between two distinct line vertices. A point and a line are at distance \(1\) if incident and \(3\) otherwise. An off-edge route between two interior points of the same edge is longer than their direct interval route, since the incidence graph has girth \(6\). For distinct edges, any path between interior points must pass through one endpoint of each edge. Thus their distance is the minimum of four affine expressions formed from endpoint distances, and the four edge classes admit the following conditional forms in independent uniform coordinates \(U,V\in[0,1]\):
\[
 \begin{array}{c|c|c}
 \text{class}&\text{multiplicity for each }e&\text{distance in law}\\\hline
 \text{same edge}&1&|U-V|\\
 \text{incident edges}&2q&U+V\\
 \text{one cross incidence}&2q^2&1+U+V\\
 \text{neither}&q^3&3-|U+V-1|
 \end{array}
\]
To see the third case, orient \(e\) from \(p\) to \(\ell\) and \(f\) from \(p'\) to \(\ell'\) so that \(p\in\ell'\). The four endpoint routes have lengths \(2+U-V\), \(2+U+V\), \(4-U-V\), \(4-U+V\); their minimum is \(2+U-V\), distributed as \(1+U+V\). In the fourth class the routes have lengths \(2+U+V\), \(4-U-V\), \(4+U-V\), \(4-U+V\), whose minimum is \(3-|U+V-1|\). For adjacent edges, the shared-endpoint route \(U+V\) beats all alternatives. These formulas also hold on boundaries by continuity.

**3. Mixture integration.** The four class probabilities are \((1,2q,2q^2,q^3)/m\). The first conditional distance has density \(2(1-t)\) on \((0,1)\); the next two are triangular densities of \(U+V\) and \(1+U+V\); the last has density \(2(t-2)\) on \((2,3)\). Summing yields the three stated affine density pieces. Integration supplies the CDF. The four conditional means are \(1/3,1,2,8/3\) and their second moments are \(1/6,7/6,25/6,43/6\). Weighted sums, followed by polynomial factorization, give all stated moments and the variance.

**4. Strict likelihood-ratio order.** Fix \(q<r\). For \(t=j+u\), \(j\in\{0,1,2\}\) and \(0<u<1\),
\[
 \frac{f_r(j+u)}{f_q(j+u)}=\frac{m_q}{m_r}\left(\frac rq\right)^j\frac{1+(r-1)u}{1+(q-1)u},
\]
where \(m_s=(s+1)(s^2+s+1)\). The derivative of the final fraction is \((r-q)/(1+(q-1)u)^2>0\), and its endpoint values give matching ratios at \(t=1,2\). Hence the likelihood ratio increases strictly on all \((0,3)\). Since the densities have equal total mass and are everywhere positive there, their CDFs satisfy strict stochastic ordering. The derivative of the continuous extension of the mean to real \(q>0\) is
\[
 \mu_q'=\frac{(q+2)^2(2q+1)^2}{3m^2}>0.
\]
The one-dimensional Wasserstein identity \(W_1=\int_0^3|F_q-F_r|\,dt\), together with strict ordering, gives the difference of means.

**5. Sharp tail and limiting law.** Integrate the last density from \(3-\varepsilon\) to \(3\) to obtain the exact quadratic tail. The fourth edge-pair class is a fixed law \(G\) with density \(2(t-2)\) on \((2,3)\), and its mixture weight is \(q^3/m\). Therefore \(\mathcal L(D_q)=(q^3/m)G+(1-q^3/m)H_q\) for some probability law \(H_q\), proving the asserted total-variation bound. The limit moments are consequently \(8/3\) and \(1/18\).

## Verification

The accompanying standalone `VERIFY.py` constructs the projective plane \(\mathrm{PG}(2,p)\) from normalized triples over prime fields \(p=2,3,5\), forms its entire incidence graph, computes all vertex distances by breadth-first search, and compares the four path-route minima with the four predicted formulas at \(25\) rational coordinate pairs **for every ordered edge pair**. It checks each edge's multiplicities and checks the displayed moment and monotonicity polynomials by integer polynomial arithmetic. The executable passed for \(q=2,3,5\): respectively \(11{,}025\), \(67{,}600\), and \(864{,}900\) exact endpoint-coordinate comparisons (\(943{,}525\) total). The theorem itself follows from the preceding finite-plane-axiom argument, not from the finite checks.

To reproduce with the standard Python 3 library, execute `python VERIFY.py` in the directory containing that file.

## Relationship to prior work

The finite-projective-plane incidence graph and its girth/degree/distance properties are classical; De Winter, Lazebnik, and Verstraëte (2008) study extremal structural properties of these graphs. Camarero and collaborators (2015, §3.1) give the **vertex-to-vertex** distance enumerator of the same graph; Madaras and Mockovčiaková (2013) give related discrete Wiener-index formulas. Neither discrete invariant is the continuous arclength-pair law here. General continuous-graph mean-distance methods appear in Garijo, Márquez, and Silveira (2021 preprint); they do not explicitly give this full finite-plane law, its strict likelihood-ratio ordering, or the exact Wasserstein separation. The earlier article by Doyle and Graver (1982) is relevant background for continuous graph distances but its full text was unavailable for the present comparison. The main claim concerns the full distribution and the all-order likelihood-ratio theorem, not priority for known vertex distances or generic integration principles.

## Limitations

The edge lengths must all equal \(1\); rescaling by a common length simply scales distances. The theorem is conditional on the existence of a projective plane of the stated order. The full text of one potentially relevant historical article was inaccessible, so historical priority cannot be certified conclusively. The numerical checks treat Desarguesian planes of three small prime orders; coverage of all planes, including non-Desarguesian ones, is supplied by the analytical proof using only projective-plane axioms. No independent external audit has been performed.

## References

1. S. De Winter, F. Lazebnik, and J. Verstraëte, “An Extremal Characterization of Projective Planes,” *Electronic Journal of Combinatorics* **15** (2008), R143. DOI: 10.37236/867. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v15i1r143
2. C. Camarero, C. Martínez, R. Vallejo, and R. Beivide, “Projective Networks: Topologies for Large Parallel Computer Systems,” arXiv:1512.07574v1 (2015-12-23), §3.1. https://arxiv.org/abs/1512.07574
3. T. Madaras and M. Mockovčiaková, “Notes on topological indices of graph and its complement,” *Opuscula Mathematica* **33** (2013), 107–115. DOI: 10.7494/OpMath.2013.33.1.107.
4. D. Garijo, A. Márquez, and C. Silveira, “Continuous Mean Distance of a Weighted Graph,” arXiv:2103.11676 (2021). https://arxiv.org/abs/2103.11676
5. P. G. Doyle and J. E. Graver, “Mean Distance for Shapes,” *Journal of Graph Theory* **6** (1982), 453–471. DOI: 10.1002/jgt.3190060410 (full text not inspected).
