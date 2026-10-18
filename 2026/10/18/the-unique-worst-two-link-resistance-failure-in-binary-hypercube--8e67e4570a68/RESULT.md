# The unique worst two-link resistance failure in binary hypercubes

## Finding

Let \(Q_d\) be the graph on the binary strings \(\{0,1\}^d\), adjacent precisely when they differ in one coordinate, with every edge assigned unit conductance. For every integer \(d\ge3\) and every pair \(E_0\) of distinct edges, let \(K_d(E_0)\) be the Kirchhoff index (the sum of unordered-pair effective resistances) of \(Q_d-E_0\). The graph stays connected.

**Theorem.** Exactly the pairs of edges incident to a common vertex maximize \(K_d(E_0)\). There are precisely \(2^d\binom d2\) maximizing unordered edge pairs. Any disjoint pair yields a strictly smaller Kirchhoff index.

Put \(N=2^d\), and define
\[
 r=\frac{2}{N}\sum_{j=0}^{d-1}\frac{\binom{d-1}{j}}{j+1},\quad
 s=\frac{1}{N}\sum_{j=0}^{d-1}\frac{\binom{d-1}{j}}{(j+1)^2},\quad c=1-r,
\]
\[
 t_T=\frac{2}{N}\int_0^1 z(1+z)^{d-2}\,dz,\qquad
 u_T=\frac{1}{N}\int_0^1 z(-\log z)(1+z)^{d-2}\,dz.
\]
Then the exact maximum is
\[
 \max_{|E_0|=2}K_d(E_0)
 =N\sum_{k=1}^{d}\frac{\binom dk}{2k}
   +2N\frac{cs+t_Tu_T}{c^2-t_T^2}.
\]
All quantities are rational numbers. The special case \(d=3\) has a strict gap of \(8/35\) in Kirchhoff index between incident-edge deletion and the best disjoint-edge deletion.

## Assumptions and scope

The graph is undirected, finite, unweighted and simple; deletions remove exactly two *distinct* edges without changing other conductances. The Kirchhoff index is \(\mathrm{Kf}(G)=\sum_{\{x,y\}\subset V(G)}R_{xy}\), where \(R_{xy}\) is the electrical effective resistance with unit resistors. Equivalently, if \(L\) is the combinatorial graph Laplacian on a connected \(N\)-vertex graph and \(G=L^+\) is its Moore–Penrose inverse, \(\mathrm{Kf}(G)=N\operatorname{tr}L^+\). (The graph and the pseudoinverse are distinguished by context.) The lower bound \(d\ge3\) is essential: deleting two edges from \(Q_2\) can disconnect it.

## Proof

**1. Exact two-edge deletion identity.** Orient the removed edges arbitrarily, with incidence columns \(b_e,b_f\). The hypercube is \(d\)-edge-connected, so deleting two edges leaves it connected when \(d\ge3\). Let \(G=L^+\) and \(H=G^2\). Edge transitivity gives \(b_e^{\mathsf T}Gb_e=b_f^{\mathsf T}Gb_f=r\) and \(b_e^{\mathsf T}Hb_e=b_f^{\mathsf T}Hb_f=s\). Put \(t=b_e^{\mathsf T}Gb_f\), \(u=b_e^{\mathsf T}Hb_f\), and \(c=1-r\). Applying the rank-two inverse identity to \(L-b_eb_e^{\mathsf T}-b_fb_f^{\mathsf T}\) on the zero-mean subspace yields
\[
 K_d(\{e,f\})-\mathrm{Kf}(Q_d)
  =2N\frac{cs+tu}{c^2-t^2}.
 \tag{1}
\]
The matrix \(I-[b_e,b_f]^{\mathsf T}G[b_e,b_f]\) is positive definite because the deleted graph is connected; in particular \(c>|t|\). Reorienting the second edge changes both \(t\) and \(u\) by one sign and does not change (1).

**2. Complete cross-correlation classification.** The Walsh characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) are Laplacian eigenvectors with eigenvalue \(2|S|\). Direct Fourier summation gives the stated \(r\) and \(s\). By translating and permuting coordinates, every pair of *parallel* distinct edges is specified by an integer \(j\in\{1,\ldots,d-1\}\), the Hamming distance of their bases on the other coordinates; the absolute correlations are
\[
 |t|=\frac2N\int_0^1(1-z)^j(1+z)^{d-1-j}\,dz,\qquad
 |u|=\frac1N\int_0^1(-\log z)(1-z)^j(1+z)^{d-1-j}\,dz.
 \tag{2}
\]
For *perpendicular* edges, there is an integer \(j\in\{0,\ldots,d-2\}\) measuring the separation on the remaining coordinates, and
\[
 |t|=\frac2N\int_0^1z(1-z)^j(1+z)^{d-2-j}\,dz,\qquad
 |u|=\frac1N\int_0^1z(-\log z)(1-z)^j(1+z)^{d-2-j}\,dz.
 \tag{3}
\]
In both cases, the actual correlations \(t,u\) have the same sign (the integral kernels are positive); hence \(tu=|t||u|\). Each integral in (2) and (3) strictly decreases as \(j\) increases: its integrand is multiplied by \((1-z)/(1+z)<1\). Therefore, within parallel pairs the most damaging configuration is \(j=1\), two opposite parallel edges of a square; within perpendicular pairs it is \(j=0\), two incident edges.

**3. Comparison of the two competing shapes.** Write the four positive correlations of these two configurations as \((t_P,u_P)\) and \((t_T,u_T)\); the latter are the theorem's integrals, while
\[
 t_P=\frac2N\int_0^1(1-z)(1+z)^{d-2}\,dz,\qquad
 u_P=\frac1N\int_0^1(1-z)(-\log z)(1+z)^{d-2}\,dz.
\]
For any fixed \(c>s>0\) and \(0<t<c\), the function \(F(t,u)=2(cs+tu)/(c^2-t^2)\) is strictly increasing in each of \(t>0\) and \(u>0\). Indeed, its derivative in \(u\) is \(2t/(c^2-t^2)>0\), and its derivative in \(t\) has the positive numerator \(2[u(c^2-t^2)+2t(cs+tu)]\).

First \(t_T>t_P\) for all \(d\ge3\). To see this, let \(\nu_d\) be the probability measure on \((0,1)\) with density proportional to \((1+z)^{d-2}\). Then \(t_T/t_P=\mathbb E_{\nu_d}[z]/(1-\mathbb E_{\nu_d}[z])\), and increasing \(d\) by one strictly increases this expectation by \(\operatorname{Var}_{\nu_d}(z)/(1+\mathbb E_{\nu_d}[z])\). At \(d=3\), the expectation already exceeds \(1/2\).

The ratio \(u_T/u_P\) also strictly increases with \(d\), by the identical variance argument under density proportional to \((-\log z)(1+z)^{d-2}\). Exact integration at \(d=5\) gives
\[
 (t_Tu_T-t_Pu_P)\big|_{d=5}=\frac{241}{491520}>0.
\]
Consequently \(t_Tu_T>t_Pu_P\) for *every* \(d\ge5\). Since also \(t_T>t_P\) and \(c>t_T\), both the numerator and reciprocal denominator in (1) strictly favor incident edges for \(d\ge5\).

For the two remaining dimensions, direct integration into (1) gives the following **per-vertex** increases, \(F(t_T,u_T)-F(t_P,u_P)\):
\[
 d=3:\quad \frac1{35},\qquad
 d=4:\quad\frac{299}{10540}.
\]
Both are positive. This proves a strict global comparison in every dimension.

**4. Equality and exact value.** Strict decrease with separation within each orientation class, together with the strict comparison in step 3, leaves only perpendicular edges sharing a vertex. Each such unordered pair has one unique common vertex, so their number is \(N\binom d2\). Finally, the Walsh eigenvalues yield \(\mathrm{Kf}(Q_d)=N\sum_{k=1}^d\binom dk/(2k)\); substitution of \((t_T,u_T)\) into (1) gives the maximum formula.

## Verification

The accompanying standalone `verify.py` uses Python's exact rational arithmetic, binomial integrals and Walsh sums. It checks the symbolic correlation formulas for dimensions three through eleven; enumerates **every** unordered pair of distinct edges in dimensions three, four and five; verifies the strict classification and counts; and independently computes the deleted-graph inverse in dimensions three and four. The reproducible command is `python3 verify.py` (Python 3 standard library). It prints `VERIFY_OK 7503 exact rational Fourier, rank-two, all-pair and direct-inverse identities`. Finite tests support but do not replace the proof for all dimensions.

## Relationship to prior work

Liu and colleagues computed the Kirchhoff index of intact hypercubes and their line, subdivision and total graphs [1]. Their Theorem 9 supplies the undeleted spectral baseline; their classification does not address optimization over pairs of failed edges. Liu and colleagues also studied Kirchhoff indices of *folded* hypercubes [2], another intact network family. Hamburger, Pippert and Weakley [3] posed hypercube edge-removal leverage for **shortest-path distance sums** (the Wiener index), not electrical resistance; their abstract describes a *minimum* leverage and a matching problem, rather than this maximum total-resistance problem. General rank-two Laplacian perturbation identities alone do not determine which edge pair is extremal. A different two-failure spectral-gap problem can favor square-opposite parallel edges, showing that optimizing the reciprocal-spectrum sum is not equivalent to minimizing the first positive Laplacian eigenvalue.

## Limitations

The assertion is limited to the ordinary unit-conductance binary hypercube and exactly two distinct lost links; weighted, directed and larger-failure-budget extensions are not claimed. The theorem is proved analytically, but this manuscript has not received an independent mathematical audit. An equivalent formulation in specialized failure-robustness literature not indexed in the compared sources cannot be ruled out.

## References

[1] J. Liu et al., “The Kirchhoff Index of Hypercubes and Related Complex Networks,” *Discrete Dynamics in Nature and Society* (2013), article 543189, DOI: 10.1155/2013/543189. First online 12 December 2013.

[2] J. Liu et al., “The Kirchhoff Index of Folded Hypercubes and Some Variant Networks,” *Mathematical Problems in Engineering* (2014), article 380874, DOI: 10.1155/2014/380874.

[3] P. Hamburger, R. E. Pippert, and W. D. Weakley, “On a leverage problem in the hypercube,” *Networks* 22 (1992), 435–439, DOI: 10.1002/net.3230220502.
