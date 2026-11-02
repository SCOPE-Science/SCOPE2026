# Critical groups of all two-token graphs of connected cubic graphs on eight vertices

## Finding
Let \(G\) range over connected simple cubic graphs on eight vertices, and let \(F_2(G)\) be its ordinary two-token graph. For each vertex pair \(\{u,v\}\), a move replaces exactly one endpoint by an adjacent unoccupied vertex. The critical group \(K(F_2(G))\), defined by the cokernel of a reduced integer Laplacian, has precisely the five possibilities listed below, each belonging to one isomorphism class of \(G\). Every graph \(F_2(G)\) has 28 vertices, 72 edges, sixteen vertices of degree six and twelve of degree four; nevertheless its critical group distinguishes all five classes.

Here invariant factors \((d_1,\ldots,d_r)\) specify \(K(F_2(G))\cong\bigoplus_{i=1}^r\mathbb Z/d_i\mathbb Z\), omitting factors equal to one and preserving divisibility order. Graphs are identified by the explicit edge lists in `verify.py`, numbered G1 through G5:

| Class | Triangles of \(G\) | Nonunit invariant factors | Spanning trees of \(F_2(G)\) |
| --- | ---: | --- | ---: |
| G1 | 4 | \(2,2,4,4,8,8,136,12512,6193440\) | 43167562522951680 |
| G2 | 2 | \(2,2,4,4,36,936,33603216192\) | 72466814259560448 |
| G3 | 1 | \(10,3727350,2269956150\) | 84609210557025000 |
| G4 (three-cube) | 0 | \(2\) (six copies), \(4\) (two copies), \(8,16\), \(64\) (two copies), \(192\), \(960\) (two copies) | 94997804639846400 |
| G5 (Wagner graph) | 0 | \(2,2,4,4,16,1790768,53723040\) | 98514432916193280 |

In particular, the two triangle-free cubic graphs of order eight share these coarse token-graph size and degree data, but their critical groups have strikingly different prime supports: the three-cube token graph has only \(2,3,5\), whereas the Wagner token graph has \(2,3,5,7,59,271\).

## Assumptions and scope
All graphs are undirected, finite, simple and connected. A cubic graph has degree three at every vertex. For any graph \(H\), write \(L(H)=D(H)-A(H)\); deleting the same row and column gives a reduced Laplacian \(L'(H)\). The finite abelian critical group \(K(H)=\mathbb Z^{|V(H)|-1}/L'(H)\mathbb Z^{|V(H)|-1}\) is well defined up to isomorphism. Each entry in the theorem concerns exactly two indistinguishable noncolliding tokens. It is a complete statement for cubic graphs of order eight, not a general formula for other orders or token counts.

## Proof
**Exhaustion of base graphs.** The recurrence in `verify.py` chooses the first vertex \(u\) with remaining positive degree, selects precisely its required neighbors among vertices with greater labels and positive remaining degree, reduces their residual degrees, and repeats. Every labeled simple cubic graph is produced once, since the neighbors of the smallest unfinished vertex are determined uniquely. The 19,355 completed labeled simple graphs include 19,320 connected examples. Exact isomorphism testing of these connected graphs finds five classes, all represented by the five provided edge lists; the representatives are pairwise nonisomorphic. This exhausts every graph in the hypothesis.

**The token Laplacian.** Vertices of \(F_2(G)\) are all 28 pairs of base vertices. Each base edge \(uv\) permits six moves of a token along \(uv\), one for each location of the other token outside \(\{u,v\}\). Thus \(|E(F_2(G))|=12\cdot6=72\). At a pair \(\{u,v\}\) the degree is \(6-2\mathbf1_{uv\in E(G)}\). Exactly twelve pairs have degree four; the other sixteen have degree six. The explicit construction in both checkers follows this rule and produces the integer reduced Laplacian of order 27.

**Exact integer invariant factors.** For each reduced Laplacian \(A\), its Hermite normal form gives an exact positive determinant \(N\), equal to the spanning-tree count by the matrix-tree theorem. Factoring \(N=\prod p^{e_p}\) gives the complete list of primes that can occur in the cokernel. For each such \(p\), the checker works modulo \(p^{e_p+1}\) and repeatedly chooses an entry of minimum \(p\)-adic valuation \(v\) in the remaining submatrix. Row and column permutations move this entry to the first available diagonal position. As all other entries in the remaining block are divisible by \(p^v\), the unit part of the pivot has an inverse modulo \(p^{e_p+1-v}\). Elementary invertible row and column operations eliminate its column and row. This is diagonal reduction by invertible transformations over the local principal ring, so the resulting valuations are precisely the \(p\)-primary Smith valuations. The modulus has higher \(p\)-power than \(N\), preventing a nonzero invariant factor from being mistaken for zero. Sorting these valuations for each \(p\) and multiplying equal-ranked prime-power factors gives the integral invariant factors displayed above. The checker tests both the divisibility chain and equality of their product to \(N\).

**Independent arithmetic route.** The second checker directly reconstructs the token graph, computes \(\det(A)\) by exact fraction-free domain Gaussian elimination, then uses an independent local algorithm: peel off every unit pivot modulo \(p\), divide the residual matrix by \(p\), and repeat. The number peeled at layer \(k\) equals the number of Smith factors having valuation \(k\). This reconstructs the same lists for every class. The two exact determinant and local-Smith procedures do not infer an infinite statement from experiments; they certify a complete finite classification.

## Verification
With Python 3, NetworkX and SymPy installed, put `verify.py` and `verify_alt.py` together and run `python verify.py` followed by `python verify_alt.py`. The first enumerates all 19,355 labeled cubic graphs and groups the 19,320 connected ones into five isomorphism classes, generates all five token Laplacians, and certifies the critical groups using Hermite forms and modular diagonalization. The second independently constructs the five reduced Laplacians and verifies every determinant and invariant factor using fraction-free exact determinants and a local unit-rank filtration. Both programs terminate with distinct success markers. Their required libraries and full construction data are provided in the files; no external dataset is needed.

## Relationship to prior work
Fabila-Monroy et al. introduced and investigated token graphs in 2009, including connectivity, diameter, coloring, and Hamiltonian properties, but not this critical-group census. Dalfó et al. studied token-graph Laplacian spectra beginning in 2020: their spectral relationships can inform spanning-tree counts, but do not by themselves establish the integer Smith invariant factors for this five-class family. Critical groups and Smith forms of graph Laplacians are standard invariants, surveyed by Stanley. A prior explicit critical group for the two-token graph of the ten-vertex Petersen graph concerns a different base graph and does not imply any order-eight class in this theorem. The five-class base-graph census is known; the present contribution is the complete integral token-graph invariant table, not the enumeration of cubic graphs.

## Limitations
This result is an exact finite classification only for connected simple cubic base graphs of order eight. It does not establish a uniform symbolic Smith form for larger cubic orders, or optimality in an extremal class. No independent scholarly review has been performed. A logically equivalent prior table in literature or databases not located by the documented searches remains possible.

## References
1. R. Fabila-Monroy et al., *Token Graphs*, arXiv:0910.4774v1 (first public 2009-10-25), https://arxiv.org/abs/0910.4774 .
2. C. Dalfó et al., *On the Laplacian spectra of token graphs*, arXiv:2012.00808v1 (2020), https://arxiv.org/abs/2012.00808 .
3. R. P. Stanley, *Smith Normal Form in Combinatorics*, Journal of Combinatorial Theory A 144 (2016), 476–495, https://math.mit.edu/~rstan/papers/snf_survey.pdf .
