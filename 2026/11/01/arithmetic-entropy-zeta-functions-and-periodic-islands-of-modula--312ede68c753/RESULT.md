# Arithmetic entropy, zeta functions, and periodic islands of modular connect-the-dots maps

## Finding
For integers \(n\ge3\) and \(1\le q<n\), linearly interpolate the permutation of integer points \(j\mapsto(j+q)\bmod n\) to a continuous map \(F_{n,q}:[0,n-1]\to[0,n-1]\). Write \(d=\gcd(n,q)\), \(m=n/d\), \(r=m-1\). Let \(\lambda_r\) be the largest real root of
\[
t^r=1+t+\cdots+t^{r-1}.
\]
For \(r=1\), the root is \(1\); for \(r\ge2\), it is uniquely greater than \(1\).

**Theorem.** The entropy, the Markov polynomial, and the periodic-island structure are
\[
h_{\mathrm{top}}(F_{n,q})=\log\lambda_{m-1},\qquad
\det(tI-M)=\left(t^{m-1}-\sum_{j=0}^{m-2}t^j\right)(t^m-1)^{d-1}.
\]
There are exactly \((d-1)m\) unit Markov intervals on which \(F_{n,q}^{m}\) is the identity; the interiors of those intervals have least period \(m\). Every nonempty open interval on which some positive iterate is the identity lies within the union of these neutral cycles. Their total length is \((d-1)m=n-m\). When \(d>1\) and \(m>2\), positive topological entropy coexists with positive-Lebesgue-measure periodic islands.

For \(d=1\), the fixed-point set of every iterate is finite and the Artin–Mazur zeta function is exactly
\[
\zeta_{F_{n,q}}(z)=\exp\left(\sum_{k\ge1}\frac{\#\operatorname{Fix}(F_{n,q}^{k})}{k}z^k\right)
=\frac1{1-z-z^2-\cdots-z^{n-1}}.
\]
Furthermore, the lengths of the shortest directed Markov cycles containing each individual unit cell, sorted in increasing order, are \(1,2,\ldots,n-1\), independently of the coprime numerator \(q\).

## Assumptions and scope
The unit intervals are \(J_i=[i,i+1]\) for \(0\le i\le n-2\); boundary intersections have the ordinary closed-interval convention. The transition matrix \(M\) has \(M_{ij}=1\) exactly when \(F_{n,q}(J_i)\supseteq J_j\). A *periodic interval* means a nonempty open interval of points on which a fixed positive iterate acts identically. Entropy is topological entropy of the continuous compact-interval map. The zeta formula is asserted only when \(d=1\), since a neutral interval contributes infinitely many fixed points to an iterate when \(d>1\).

## Proof
**1. Unique fold and the exact graph.** Define \(w=n-q-1\). Direct interpolation gives the three formulas
\[
F_{n,q}(x)=\begin{cases}
x+q, &x\in J_i,\ i<w,\\
(n-1)(w+1-x), &x\in J_w,\\
x+q-n, &x\in J_i,\ i>w.
\end{cases}
\]
Thus every cell except \(J_w\) maps bijectively to a single cell, whose index is \((i+q)\bmod n\). The fold cell \(J_w\) covers *all* \(n-1\) cells. This is a finite Markov partition, including all map images of integer endpoints.

**2. Arithmetic decomposition of the transition graph.** Every deterministic edge preserves the index residue modulo \(d\). Among the indices \(0,\ldots,n-2\), all residue classes modulo \(d\) contain \(m\) indices except the class of \(n-1\), which contains \(m-1\). Since \(w=n-q-1\equiv n-1\pmod d\), precisely this shortened class contains the fold. The deterministic map \(i\mapsto(i+q)\bmod n\) is a cyclic permutation of all \(m\) integers in each residue class modulo \(d\). Removing the missing index \(n-1\) leaves a directed string on the \(m-1\) indices of the fold class, ending at \(w\). From \(w\), an edge returns to every cell, including each position of that string. This strongly connected component therefore has a single renewal hub and exactly one first-return path to the hub of each length \(1,2,\ldots,m-1\).

Each of the remaining \(d-1\) residue classes yields a closed deterministic directed cycle with exactly \(m\) cells. The fold component has outgoing edges toward these cycles, but no edge can return from any such cycle to the fold component. After permuting the vertices, \(M\) is block upper triangular with a renewal block and \(d-1\) directed-cycle blocks. The renewal block has characteristic polynomial \(t^{m-1}-(1+t+\cdots+t^{m-2})\), by its companion-matrix recursion; each deterministic cycle block has characteristic polynomial \(t^m-1\). Multiplication proves the displayed formula.

**3. Entropy and periodic islands.** For a continuous piecewise-monotone Markov interval map, topological entropy equals the logarithm of the spectral radius of the Markov transition matrix; this follows also from its exponential lap growth, which counts admissible traversals up to a polynomial boundary correction. The deterministic cycle blocks have spectral radius \(1\), while the renewal block has spectral radius \(\lambda_{m-1}\), by Perron–Frobenius theory (and the companion equation). This proves the entropy formula.

For a deterministic residue-class cycle, each restriction \(F_{n,q}|_{J_i}\) is a unit-slope integer translation. Therefore \(F_{n,q}^m|_{J_i}\) is an integer translation of \(J_i\) onto itself, hence is exactly the identity. Distinct cell indices along the \(m\)-cycle imply every interior point has least period \(m\). Conversely, a nonempty periodic open interval cannot contain an orbit segment passing through the interior of the fold cell: on every small subinterval with a definite itinerary using the fold at least once, the derivative of the appropriate iterate has modulus at least \(n-1>1\), incompatible with identity. Every interior periodic interval therefore follows a deterministic closed path, necessarily one of those \(d-1\) cycles. This establishes maximality and the exact total length \((d-1)m\).

**4. Coprime zeta function and cycle lengths.** Suppose \(d=1\). Every closed Markov path necessarily visits the fold, because after deleting the fold all remaining edges form a directed string and contain no cycle. Each length-\(k\) closed path produces a unique periodic point: compose the inverse monotone branches along the path; its contraction ratio is \((n-1)^{-s}<1\), where \(s\ge1\) is the number of fold visits. The Markov covering conditions ensure that the fixed point lies in every prescribed cell along its itinerary.

Different closed paths cannot represent the same periodic orbit point. Indeed an interior point has unambiguous cell membership. A periodic boundary point is an integer knot, and the knot permutation \(j\mapsto(j+q)\bmod n\) has one orbit of length \(n\), visiting the domain endpoints \(0\) and \(n-1\), which lie in unique Markov cells. Membership in an admissible closed path is determined forward from any such endpoint and hence uniquely for the whole orbit. Therefore \(\#\operatorname{Fix}(F_{n,q}^k)=\operatorname{tr}(M^k)\) for every positive integer \(k\). The formal identity \(\exp(\sum_{k\ge1}\operatorname{tr}(M^k)z^k/k)=1/\det(I-zM)\), combined with the coprime case of the characteristic polynomial, proves the zeta formula.

Finally, the unique shortest closed path through a vertex first follows the forced deterministic string to \(w\), then takes the direct hub edge back to the starting vertex. The \(n-1\) starting vertices occupy consecutive distinct positions along that string. Consequently their shortest cycle lengths are exactly \(1,2,\ldots,n-1\).

## Verification
Run `python rotation_family_checker.py` using the Python standard library. The deterministic script checks every pair \((n,q)\) with \(3\le n\le14\), including all slopes, knot images, graph edges, residue classes, algebraic identities on every neutral component, and the transition polynomial at two integer arguments. For all coprime pairs with \(3\le n\le8\), it enumerates every length-\(k\) closed itinerary for \(1\le k\le9\), solves the periodic-point affine equation exactly using rational arithmetic, checks admissibility and pairwise distinctness, and independently compares counts to matrix traces. It reports `PASS 90 (n,q) structural cases; 15932 exact periodic-address checks`. These are finite cross-checks; the universal theorem follows from the proof above, not from extrapolation of the tests.

## Relationship to prior work
The cyclic permutation \(j\mapsto(j+q)\bmod n\) is a classical *twist permutation* in interval dynamics. Geller and Misiurewicz analyze Farey–Lorenz permutations using a different, discontinuous canonical Lorenz extension; their Farey and itinerary results do not give the continuous affine interpolant's arithmetic entropy, zeta function, or periodic-island decomposition. Wang studies shortest cycles in interval-covering Markov graphs, presents an example for the one-step cyclic shift, and formulates a bound on ordered characteristic numbers. Here the upper bound is attained for *every* coprime cyclic shift, while the explicit full Markov decomposition also classifies noncoprime shifts. The entropy-from-adjacency and trace/determinant identities themselves are standard background tools rather than independently new statements.

## Limitations
No claim is made about smooth extensions, arbitrary interval permutations, general Lorenz maps, statistical mixing, or independent publication-priority certification. The exact Artin–Mazur zeta formula is restricted to coprime shifts. In noncoprime shifts the zeta series based on finite fixed-point counts is not defined at return times of the neutral intervals. No independent scientific audit has been performed.

## References
1. Y. Wang, *On an existence problem of periodic points in intervals whose images cover themselves*, arXiv:2205.07225v1 (2022), especially the characteristic sequence and cyclic permutation example. https://arxiv.org/abs/2205.07225
2. W. Geller and M. Misiurewicz, *Farey–Lorenz Permutations for Interval Maps*, International Journal of Bifurcation and Chaos, doi:10.1142/S0218127418500219 (2018). https://doi.org/10.1142/S0218127418500219
3. P. Bartłomiejczyk and collaborators, *Spike patterns and chaos in a map-based neuron model*, International Journal of Applied Mathematics and Computer Science, doi:10.34768/amcs-2023-0028 (2023). https://doi.org/10.34768/amcs-2023-0028
