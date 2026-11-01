# Degree distribution of the wheel acyclic-orientation flip graph

## Finding

For every integer \(m\ge3\), let \(W_{m+1}=K_1\vee C_m\), with a named hub and a cyclically labelled rim. Define \(\mathcal A_m\) to have one vertex for each acyclic orientation of all \(2m\) edges and an edge between two orientations exactly when they differ by reversing one directed edge and both orientations remain acyclic. Let
\[
D_m(z)=\sum_{\omega\in V(\mathcal A_m)}z^{\deg_{\mathcal A_m}(\omega)}.
\]
Write \([x^r]F(x)\) for the coefficient of \(x^r\) in a formal power series, and put \(Q(x,z)=1-2x+(1-z)x^2\). Then the **entire degree polynomial**, for every \(m\ge3\), is
\[
\boxed{D_m(z)=z^m\left(4m+2m(m-3)z+4\sum_{j=2}^{\lfloor m/2\rfloor}\binom m{2j}z^j+m\sum_{j=1}^{\lfloor m/2\rfloor}\frac1j[x^{m-2j}]Q(x,z)^{-2j}\right).}
\]
Empty sums are zero. In particular, the minimum degree is \(m\), and the exact number of degree-\(m\) vertices (the simple vertices of the associated \(m\)-dimensional graphical zonotope) is
\[
\boxed{s_m=4m+m\sum_{j=1}^{\lfloor m/2\rfloor}\frac1j\binom{m+2j-1}{m-2j}.}
\]
More strikingly, if the Lucas numbers are defined by \(L_0=2\), \(L_1=1\), and \(L_{r+2}=L_{r+1}+L_r\), this binomial sum simplifies to
\[
\boxed{s_m=L_{2m}+4m-4+2\cos(m\pi/3).}
\]
The proportion of acyclic orientations giving simple zonotope vertices consequently decreases exponentially, asymptotic to \(\bigl((3+\sqrt5)/6\bigr)^m\).

For \(m=3\), the flip graph is \(3\)-regular on \(24\) orientations. For every \(m\ge4\), its maximum degree is \(m+\lfloor m/2\rfloor\), with exactly \(4\) attaining orientations if \(m\) is even and exactly \(4m\) if \(m\) is odd. The number of flip-graph vertices is the previously known \(3^m-3\), and its edge count, also implied by general graphical-zonotope face formulas, is
\[
|E(\mathcal A_m)|=m(5\cdot3^{m-2}-3).
\]
The contribution asserted here is the vertex-by-vertex degree distribution and its sharp minimum/maximum classifications, not the previously known total orientation count or general face-count identities.

## Assumptions and scope

All graphs are finite, simple and undirected before orienting. The wheel has rim vertices \(v_0,\dots,v_{m-1}\), indexed modulo \(m\), and hub \(h\). Orientations keep these labelled edges distinct. A move reverses one edge only; simultaneous flips are not allowed. A directed edge \(u\to v\) is **flippable** precisely when deleting that directed edge leaves no directed path from \(u\) to \(v\); otherwise the reversal creates a directed cycle. In the polynomial above, the exponent is the number of individually flippable edges. The statement holds for each integer \(m\ge3\), with no asymptotic or genericity assumption.

## Proof

**1. Spoke/rim encoding.** Call a rim vertex type \(A\) when its spoke is \(h\to v\), and type \(B\) when its spoke is \(v\to h\). For two consecutive rim vertices of different types, acyclicity forces their rim edge to point from type \(B\) to type \(A\), since the other direction would close a directed hub triangle. When both endpoint types coincide, that rim edge is independently orientable. If both types occur, these constraints suffice for acyclicity: no directed path along the rim can cross from an \(A\)-run to a \(B\)-run, and the rim cycle cannot be consistently directed. If all spokes have one type, every rim orientation is allowed except the two directed rim cycles. These facts also give \(|V(\mathcal A_m)|=3^m-3\), already established in the literature.

**2. Exact local flip criterion.** Suppose both spoke types occur and there are \(k\) cyclic runs, necessarily an even positive integer. Each of the \(k\) between-run rim edges is directed \(B\to A\) and cannot be flipped, because a second path \(B\to h\to A\) exists. Every within-run rim edge can be flipped: a competing path through the hub would require a forbidden \(A\to B\) crossing or an impossible spoke direction; a long competing path around the rim also crosses a forbidden boundary. For an \(A\)-vertex, its spoke is flippable exactly when no within-run rim edge enters it, i.e. when it is a source of the oriented path induced by its \(A\)-run. Dually, for a \(B\)-run the flippable spokes occur at sinks of its oriented path. Hence if the run lengths are \(\ell_1,\ldots,\ell_k\) and the respective numbers of sources or sinks are \(s_1,\ldots,s_k\), the orientation degree is exactly
\[
\deg=m-k+\sum_{i=1}^k s_i.
\]

**3. Path-source enumerator.** Let \(P_\ell(z)\) count orientations of a labelled path on \(\ell\ge1\) vertices by number of sources. Record each of its \(\ell-1\) edges as a right or left arrow; prepend a virtual left arrow and append a virtual right arrow. Sources are precisely transitions from a left arrow to a right arrow. If there are \(s\) sources then, because the virtual boundary symbols differ, there are exactly \(2s-1\) changes among the \(\ell\) adjacent sign pairs. Consequently
\[
P_\ell(z)=\sum_{s\ge1}\binom\ell{2s-1}z^s,
\qquad
B(x,z):=\sum_{\ell\ge1}P_\ell(z)x^\ell=\frac{zx}{1-2x+(1-z)x^2}.
\]
Reversing every arrow identifies the sink and source enumerators.

**4. Mixed spokes.** For fixed even \(k\), a cyclic binary spoke word with \(k\) runs is described by a choice of initial type (two possibilities), an initial run boundary (\(m\) choices) and an ordered positive composition \(\ell_1+\cdots+\ell_k=m\), divided by \(k\) because any run boundary can be the distinguished one. The within-run orientations are independent; across-run edges are forced. Thus the contribution for fixed \(k\) is
\[
\frac{2m}{k}z^{m-k}[x^m]B(x,z)^k.
\]
Writing \(k=2j\) and inserting the displayed rational expression for \(B\) gives
\[
M_m(z)=mz^m\sum_{j=1}^{\lfloor m/2\rfloor}\frac1j[x^{m-2j}]Q(x,z)^{-2j}.
\]

**5. Constant spokes and the only global correction.** Suppose every spoke points away from the hub, or every spoke points toward it. Let \(q\) be the number of cyclic runs of each direction among the rim arrows; the rim cannot be uniformly directed, so \(1\le q\le\lfloor m/2\rfloor\). There are precisely \(q\) flippable spokes (sources or sinks, respectively). A rim edge has a competing directed route only when all other \(m-1\) rim edges point in the reverse cyclic direction. Therefore one rim edge is unflippable exactly if a single rim edge points against all the others; write \(\varepsilon=1\) in this case and \(0\) otherwise. The orientation degree is
\[
\deg=m+q-\varepsilon.
\]
Among rim words with \(q=1\), exactly \(2m\) have \(\varepsilon=1\), and the remaining \(m(m-3)\) have \(\varepsilon=0\). For \(q\ge2\) there are \(2\binom m{2q}\) rim words, all with \(\varepsilon=0\). Both uniform spoke directions are allowed. The constant-spoke contribution is therefore
\[
C_m(z)=z^m\left(4m+2m(m-3)z+4\sum_{q=2}^{\lfloor m/2\rfloor}\binom m{2q}z^q\right).
\]
Adding \(C_m(z)+M_m(z)\) proves the boxed degree polynomial.

**6. Extremal degrees.** A nonempty oriented path always has at least one source or sink. Therefore each mixed-spoke run supplies at least one flippable spoke and its degree is at least \(m\). If a run has length \(\ell\), its sources or sinks number at most \(\lceil\ell/2\rceil\). For \(k\ge2\) runs, the mixed-spoke degree is at most \(\lfloor(3m-2)/2\rfloor\), strictly smaller than \(m+\lfloor m/2\rfloor\). Uniform spokes have degree \(m+q-\varepsilon\). For \(m\ge4\), the maximum \(q=\lfloor m/2\rfloor\) has \(\varepsilon=0\): the rim directions alternate for even \(m\) (two words), or have exactly one doubled direction for odd \(m\) (\(2m\) words). Multiplying by the two uniform spoke choices gives exactly \(4\) or \(4m\) maximizers. When \(m=3\), every nonconstant rim word has \(q=\varepsilon=1\), and the mixed formula gives degree \(3\) as well. For the minimum-degree coefficient, set \(z=0\) in \(Q(x,z)^{-2j}=(1-x)^{-4j}\) after extracting the prefactor \(z^m\), obtaining \([x^{m-2j}](1-x)^{-4j}=\binom{m+2j-1}{m-2j}\). This proves the binomial formula for \(s_m\). For the Lucas simplification, the degree-\(m\) contribution from mixed spokes comes by requiring exactly one source or sink in each run. Since \([z^1]P_\ell(z)=\ell\), its source-length series is \(R(x)=\sum_{\ell\ge1}\ell x^\ell=x/(1-x)^2\). Therefore
\[
\sum_{m\ge1}\frac{s_m-4m}{m}x^m=-\log(1-R(x)^2)
=-\log(1-3x+x^2)-\log(1-x+x^2)+4\log(1-x).
\]
The two reciprocal roots of \(1-3x+x^2\) are \(\alpha=(3+\sqrt5)/2\) and \(\beta=(3-\sqrt5)/2\), and those of \(1-x+x^2\) are \(e^{\pm i\pi/3}\). Extracting the coefficient and multiplying by \(m\) yields \(s_m=4m+\alpha^m+\beta^m+2\cos(m\pi/3)-4\). Since \(\alpha^m+\beta^m=L_{2m}\), the closed Lucas formula follows. The ratio \(s_m/(3^m-3)\) has the displayed exponential asymptotic because \(\beta\) has modulus below one and the remaining correction is linear or bounded.

**7. Independent edge-count check.** For any simple graph \(G\), pairs of acyclic orientations connected by reversing a specified edge \(e\) are in bijection with acyclic orientations of the contracted graph \(G/e\), because the other arcs must permit both directions of \(e\). Contracting a wheel rim edge gives the wheel with one fewer rim vertex (the smallest case gives a triangle), with \(3^{m-1}-3\) acyclic orientations. Contracting a spoke gives a fan \(K_1\vee P_{m-1}\), whose successive simplicial ears yield \(2\cdot3^{m-2}\) orientations. Summation over the \(m\) rim edges and \(m\) spokes yields \(|E(\mathcal A_m)|=m(5\cdot3^{m-2}-3)\). This is a checksum rather than an independently claimed new general principle.

## Verification

The accompanying `verify_direct.py` constructs all orientations from scratch, recognizes directed cycles by topological sorting and tests each possible move by deleting that arc and checking directed reachability. It exhaustively checks every orientation for \(3\le m\le8\), including degree histograms, vertex counts, and edge-count identities. It makes no use of the proposed formula in deciding whether a flip is legal.

The separate `verify_formula.py` evaluates the claimed coefficient formula and independently enumerates ordered cyclic run-length compositions with their source polynomials for \(3\le m\le12\). These calculations agree exactly with one another and, in their shared range, with the direct orientation enumeration. The printed counts below are listed in ascending degree order:

| Rim length | Degree polynomial \(D_m(z)\) |
| --- | --- |
| \(3\) | \(24z^3\) |
| \(4\) | \(58z^4+16z^5+4z^6\) |
| \(5\) | \(140z^5+80z^6+20z^7\) |
| \(6\) | \(344z^6+300z^7+78z^8+4z^9\) |
| \(7\) | \(868z^7+980z^8+308z^9+28z^{10}\) |
| \(8\) | \(2234z^8+2992z^9+1184z^{10}+144z^{11}+4z^{12}\) |

The finite computations do not establish the infinite formula by themselves; Steps 1–7 provide an all-parameter proof.

## Relationship to prior work

Savage, Squire and West's *Gray Code Results for Acyclic Orientations* (1993) introduced and analysed the arc-flip graph, established the wheel orientation count \(3^m-3\), and explicitly described the forced rim-edge directions for any fixed spoke word. Those premises are acknowledged. Their treatment of wheels concerns Hamiltonian paths and non-Hamiltonicity, rather than their full vertex-degree distribution.

Grujić's *Counting faces of graphical zonotopes* (first public preprint April 23, 2016) gives the overall face polynomial, in particular counts of vertices and edges, from contractions and chromatic-symmetric-function specializations. A global face count does not determine how the edges are distributed among individual vertices. The proposed refinement is the closed degree polynomial and its extremal multiplicities, not the general zonotope face identity.

Exact wheel degree polynomials were also searched under the equivalent terms acyclic-orientation graphs, graphical-zonotope skeleton degrees, graphic-arrangement chamber walls, and simplicial chambers. No covering statement was identified in the checked material. Lack of a hit is not evidence of absolute historical uniqueness.

## Limitations

The theorem covers ordinary acyclic orientations of \(K_1\vee C_m\) under single-edge flips only; it does not treat strong orientations, source-to-sink flips, arbitrary coned graphs, multiple edges, or induced higher-dimensional face incidences. Counts refer to labelled vertices of the wheel (though the degree distribution itself is label-invariant). No claim is made about Hamiltonicity beyond prior results. The comparison with historic literature is limited to located records and available primary full texts; an unindexed equivalent degree formula remains possible. The computational tests are finite corroborations rather than independent mathematical certification.

## References

1. C. D. Savage, M. B. Squire, D. B. West, *Gray Code Results for Acyclic Orientations*, Congressus Numerantium 96 (1993), 185–204. Author-hosted full paper: https://dwest.web.illinois.edu/pubs/aograph.pdf .
2. V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931, first submitted 2016-04-23. https://arxiv.org/abs/1604.06931 .
3. R. P. Stanley, *Acyclic orientations of graphs*, Discrete Mathematics 5 (1973), 171–178. https://doi.org/10.1016/0012-365X(73)90108-8 .
