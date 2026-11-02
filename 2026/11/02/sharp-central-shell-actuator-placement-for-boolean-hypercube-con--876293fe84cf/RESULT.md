# Sharp central-shell actuator placement for Boolean hypercube consensus

## Finding

For every integer \(d\ge1\), let \(Q_d\) be the unweighted, undirected Boolean hypercube on \(\{0,1\}^d\), let \(L_d=dI-A_d\) be its graph Laplacian, and consider \(\dot z=-L_dz+B_Uu\), where the columns of \(B_U\) are separate standard coordinate vectors indexed by the controlled vertices \(U\). Then the exact minimum cardinality of a controllable vertex set is

\[
\min\{|U|:(-L_d,B_U)\text{ is controllable}\}=\binom{d}{\lfloor d/2\rfloor}.
\]

An optimal set is given explicitly. When \(d=2m+1\) is odd, take the central Hamming sphere

\[
U_{2m+1}=\{x\in\{0,1\}^{2m+1}:|x|=m\}.
\]

When \(d=2m\) is even, fix one coordinate at zero, and take the two middle Hamming layers of that \((2m-1)\)-dimensional face:

\[
U_{2m}=\{(0,x):x\in\{0,1\}^{2m-1},\ |x|\in\{m-1,m\}\}.
\]

In particular, the minimum fraction of controlled vertices is asymptotic to \(\sqrt{2/(\pi d)}\). The theorem includes \(d=1\) and \(d=2\).

## Assumptions and scope

The cube has one unit-weight, undirected edge for each single-bit flip. The controlled vertices each receive one independent, continuously variable scalar input; the input matrix is an unsigned coordinate selector. This is exact finite-dimensional Kalman controllability of the full linear consensus system (not merely reachability of the average). The result does not assert robustness to arbitrary edge-weight perturbations, noise, finite-horizon control-energy bounds, or controllability by one input wired to multiple vertices.

For \(x\in\{0,1\}^d\), \(|x|\) is its Hamming weight; \(A_d\) is the adjacency operator. All statements are over the real numbers.

## Proof

**1. Sharp lower bound.** For each subset \(S\subseteq\{1,\ldots,d\}\), the Walsh character \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\) satisfies

\[
A_d\chi_S=(d-2|S|)\chi_S,
\qquad L_d\chi_S=2|S|\chi_S.
\]

These characters form an orthogonal basis, so the eigenspace associated with the eigenvalue \(2k\) of \(L_d\) has dimension \(\binom dk\). The PBH test for a real symmetric state matrix states that controllability is equivalent to the absence of a nonzero eigenvector vanishing on all controlled vertices. Consequently, every coordinate-selector input set must have at least \(\max_k\binom dk=\binom{d}{\lfloor d/2\rfloor}\) vertices.

**2. Incidence injectivity.** On rank \(r\) subsets of a \(t\)-element set, let \(U_r\) send a function to the sum over its rank-\(r\) subfaces of each rank-\(r+1\) set, and set \(D_{r+1}=U_r^{\mathsf T}\). Directly counting diagonal and off-diagonal terms gives

\[
D_{r+1}U_r-U_{r-1}D_r=(t-2r)I.
\]

With \(U_{-1}D_0=0\), taking an inner product yields

\[
\|U_rf\|_2^2=\|D_rf\|_2^2+(t-2r)\|f\|_2^2.
\]

Thus \(U_r\) is injective whenever \(r<t/2\), including \(r=0\).

**3. Central-sphere uniqueness in odd dimension.** Let \(t=2m+1\), and let \(f\) be any eigenvector of \(A_t\) vanishing on the shell \(|x|=m\). For some \(k\), \(f\) is a linear combination of Walsh characters all of degree \(k\). Therefore the bitwise complement \(\bar x\) obeys \(f(\bar x)=(-1)^k f(x)\). Consequently, \(f\) also vanishes on the complementary shell \(|x|=m+1\). At every vertex of weight \(m\), the adjacency eigen-equation and the vanishing on shell \(m+1\) give \(U_{m-1}f_{m-1}=0\). Step 2 implies \(f_{m-1}=0\). Complement symmetry now gives \(f_{m+2}=0\). Iterating the same argument through shells \(m-1,m-2,\ldots,1\) annihilates all shells. For \(m=0\), the two shells are already the entire graph. Hence the central shell determines every adjacency eigenvector uniquely, for every odd \(t\ge1\). The specified odd-dimensional \(U_t\) therefore satisfies PBH.

**4. Even-dimensional construction.** Let \(d=2m\) and \(t=d-1=2m-1\). Write cube vertices as \((b,x)\), where \(b\in\{0,1\}\), \(x\in\{0,1\}^t\). If an adjacency eigenvector \(F\) of \(Q_d\) has eigenvalue \(d-2k\), its restriction \(g(x)=F(0,x)\) decomposes as \(g=g_k+g_{k-1}\), where each \(g_j\) belongs to Walsh degree \(j\) on \(Q_t\); a nonexistent degree is interpreted as zero. Suppose \(F\) vanishes on \(U_d\). For each \(x\) of weight \(m-1\), both \(g(x)\) and \(g(\bar x)\) vanish, because the complement has weight \(m\). Since \(g_j(\bar x)=(-1)^j g_j(x)\), these two equations imply \(g_k(x)=g_{k-1}(x)=0\). By step 3, applied separately to these two eigenfunctions of the odd cube \(Q_t\), both functions vanish everywhere. Thus \(F(0,x)=0\) for every \(x\). The eigen-equation at \((0,x)\) is \(\lambda F(0,x)=F(1,x)+\sum_{y\sim x}F(0,y)\); hence \(F(1,x)=0\) for all \(x\). This proves PBH controllability of \(U_d\).

**5. Cardinality and sharpness.** The odd set has cardinality \(\binom{2m+1}m\). The even set has size \(2\binom{2m-1}{m-1}=\binom{2m}m\). Both attain the lower bound in step 1, proving minimality. The stated asymptotic fraction follows from Stirling's formula for the central binomial coefficient.

## Verification

The standalone script `verify.py`, using exact modular arithmetic over two prime fields, checks every Walsh eigenspace restriction rank for dimensions \(1\le d\le10\) and independently checks Kalman controllability matrices for dimensions \(1\le d\le5\). It records 130 spectral-rank and 10 direct Kalman-rank assertions. The universal conclusion relies on steps 1–5, not on finite computation.

Reproduce with `python verify.py` (requires Python 3 and NumPy). The modular computations are exact in their stated finite fields; they do not alone establish ranks for arbitrary dimensions or over all characteristics. Analytic PBH and incidence arguments establish the real result.

## Relationship to prior work

Rahmani–Ji–Mesbahi–Egerstedt (2009) examine symmetry and equitable partitions in multiagent controllability. Zhang–Camlibel–Cao (2011) establish controllability bounds for distance-regular graphs and a general sufficient leader selection of size \(N-\operatorname{diam}(G)\), with detailed specializations to cycles and complete graphs, not a minimum central-shell placement on hypercubes. The general maximum-eigenvalue-multiplicity principle in Yuan and collaborators (2013) provides an abstract driver-count framework, so the spectral multiplicity lower bound and the numerical minimum should not be interpreted as a new general multiplicity principle. The specialized contribution here is an explicit minimum *coordinate-vertex* actuator configuration in each dimension, supported by a shell-uniqueness argument. Dai (2023) develops general minimal-leader methods on other graph families. Mou–Zhang (2022) study sign-pattern robustness on *directed* hypercubes, a different class and criterion. No inspected result supplied these two parity-dependent vertex configurations.

## Limitations

The construction is one optimal family; uniqueness of optimal leader sets is neither claimed nor proved. Results for arbitrary anisotropic or directed cubes, observability with aggregate sensors, and quantitative control costs are not implied. Existence of an equivalent specialized statement in unindexed combinatorial or control literature remains a historical-overlap risk; independent review has not been conducted.

## References

1. A. Rahmani, M. Ji, M. Mesbahi, and M. Egerstedt, *Controllability of Multi-Agent Systems from a Graph-Theoretic Perspective*, SIAM Journal on Control and Optimization 48 (2009), 162–186. https://doi.org/10.1137/060674909 (first verified public online date 2009-02-11).
2. S. Zhang, M. K. Camlibel, and M. Cao, *Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies*, CDC/ECC (2011), 759–764. https://doi.org/10.1109/CDC.2011.6160658 ; publicly accessible manuscript https://skoge.folk.ntnu.no/prost/proceedings/cdc-ecc-2011/data/papers/0872.pdf.
3. Z.-Z. Yuan et al., *Exact Controllability of Complex Networks*, Nature Communications 4 (2013), article 2447. https://doi.org/10.1038/ncomms3447.
4. L. Dai, *Minimum Leader Selection for Controllability of Undirected Graphs with Leader–Follower Framework*, IET Control Theory & Applications 17 (2023), 505–515. https://doi.org/10.1049/cth2.12385.
5. G. Mou and Q. Zhang, *Signed Zero Forcing Number and Controllability for a Networks System with a Directed Hypercube*, MATEC Web of Conferences 355 (2022), 01012. https://doi.org/10.1051/matecconf/202235501012.
