# Exact arbitrary-center intersections of limited-magnitude error balls
## Finding
Let \(1\le t\le n\), \(k_+\ge k_-\ge0\), and \(K=k_++k_-\ge1\). Write
\[\mathcal B=\{e\in\mathbb Z^n:-k_-\le e_i\le k_+,\ \operatorname{wt}(e)\le t\}.\]
For centers \(x,y\in\mathbb Z^n\), put \(d=y-x\). Define \(F_s(X,Y)\) by
\[F_0(X,Y)=1+KXY.\]
For \(0<|s|\le K\), let
\[\alpha_s=\mathbf 1_{[-k_-,k_+]}(s),\qquad \beta_s=\mathbf 1_{[-k_-,k_+]}(-s),\qquad \gamma_s=K+1-|s|-\alpha_s-\beta_s,\]
and set
\[F_s(X,Y)=\alpha_sX+\beta_sY+\gamma_sXY.\]
For \(|s|>K\), set \(F_s(X,Y)=0\). Then
\[|(x+\mathcal B)\cap(y+\mathcal B)|=\sum_{0\le p,q\le t}[X^pY^q]\prod_{i=1}^nF_{d_i}(X,Y).\]
Consequently, the exact intersection for arbitrary centers is computable by a truncated two-dimensional dynamic program in \(O(nt^2)\) arithmetic operations.

If \(d\) has exactly one nonzero coordinate, equal to \(s\) with \(1\le|s|\le K\), then
\[|(x+\mathcal B)\cap(y+\mathcal B)|=(K+1-|s|)V_{K+1}(n-1,t-1),\]
where
\[V_{K+1}(m,r)=\sum_{j=0}^{r}\binom mjK^j.\]
For \(|s|=1\), this specializes to the known global maximum \(K V_{K+1}(n-1,t-1)\).

## Assumptions and scope
The alphabet is the integer lattice \(\mathbb Z^n\). Each coordinate error lies in the interval \([-k_-,k_+]\), and at most \(t\) coordinates are nonzero. The result counts distinct common outputs of two translated error balls. It uses the full signed displacement vector \(d=y-x\); it does not claim that the intersection is determined by a scalar distance alone.

## Proof
Translate both centers by \(-x\), so the centers are \(0\) and \(d=y-x\). A common output has the form \(e=d+f\) with \(e,f\in\mathcal B\). Equivalently, for every coordinate \(i\),
\[e_i\in[-k_-,k_+]\cap\bigl(d_i+[-k_-,k_+]\bigr),\]
while the number of coordinates with \(e_i\ne0\) and the number with \(e_i-d_i\ne0\) are both at most \(t\).

Mark a nonzero coordinate of \(e\) by \(X\), and a nonzero coordinate of \(e-d\) by \(Y\). When \(d_i=0\), the common coordinate value is either zero, contributing \(1\), or one of the \(K\) nonzero allowed values, each contributing \(XY\). Hence the local factor is \(1+KXY\).

Now suppose \(0<|d_i|\le K\). The two integer intervals overlap in exactly \(K+1-|d_i|\) values. The special value \(e_i=d_i\), when it lies in \([-k_-,k_+]\), makes the second-center error zero and contributes \(X\); this accounts for \(\alpha_{d_i}\). The special value \(e_i=0\), when \(-d_i\in[-k_-,k_+]\), makes the first-center error zero and contributes \(Y\); this accounts for \(\beta_{d_i}\). Every remaining overlap value is nonzero relative to both centers and contributes \(XY\), giving coefficient \(\gamma_{d_i}\). If \(|d_i|>K\), the intervals are disjoint and there is no common output.

Coordinates are independent before the two support constraints are imposed, so multiplication of the local factors enumerates every common output exactly once, with the powers of \(X\) and \(Y\) recording the two support sizes. Summing coefficients with both exponents at most \(t\) proves the formula.

For a displacement supported on one coordinate, each admissible value in that coordinate consumes at least one unit of one support budget. The other \(n-1\) coordinates are shared coordinates and therefore contribute the same support to both centers. At most \(t-1\) of them may be nonzero. There are \(K+1-|s|\) admissible values at the displaced coordinate and \(V_{K+1}(n-1,t-1)\) choices on the remaining coordinates, proving the corollary.

## Verification
The accompanying verifier constructs every limited-magnitude ball directly for a finite exhaustive parameter grid, intersects translated balls for every displacement with coordinate differences in \([-K,K]\), and compares the direct count with the coefficient dynamic program. It also checks the one-coordinate corollary and the known global maximum on that grid. The computation is corroborative; the proof above is valid for all stated parameters.

## Relationship to prior work
Wei and Schwartz introduced the reconstruction problem around the same pair-intersection quantity and proved the global maximum over all pairs of centers, together with upper and lower bounds controlled by their distance parameters. The formula here instead retains the full signed displacement and gives the exact intersection for every pair of centers. For unit displacement, it reduces to their global-maximum formula. Earlier and later work on limited-magnitude-ball tilings addresses packing and tiling structure rather than this arbitrary-center coefficient enumerator.

## Limitations
The exact evaluator depends on the complete displacement vector, not only on a compressed distance statistic. The result does not by itself improve asymptotic code-density bounds, construct new reconstruction codes, or classify optimal packings. Its contribution is the exact pairwise ambiguity law and its direct dynamic-programming evaluation.

## References
H. Wei and M. Schwartz, “Sequence Reconstruction for Limited-Magnitude Errors,” arXiv:2108.09662v1; IEEE Transactions on Information Theory, 68(7), 2022, DOI:10.1109/TIT.2022.3159736.

H. Wei and M. Schwartz, “On Tilings of Asymmetric Limited-Magnitude Balls,” arXiv:2006.00198v1.

Y. Zhang, H. Lian, and G. Ge, “Complete characterization of lattice tilings of \(\mathbb Z^n\) by \(\mathcal B(n,2,1,1)\),” arXiv:2301.05834v1.