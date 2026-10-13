# A complete D-optimal single-sensor classification on weighted diffusion stars

## Finding

**Theorem.** Fix an integer \(m\ge2\). Let \(G\) be an undirected star on the hub \(0\) and leaves \(1,\ldots,m\), with strictly positive edge conductances \(w_1,\ldots,w_m\). Write its combinatorial weighted Laplacian as \(L\), and for each vertex \(j\) and horizon \(T>0\) define the full-state observability Gramian
\[
W_j(T)=\int_0^T e^{-tL}e_je_j^{\mathsf T}e^{-tL}\,dt.
\]
A D-optimal sensor maximizes \(\det W_j(T)\) among the \(m+1\) vertices.

If all conductances are pairwise distinct, every Gramian is positive definite, and for every \(T>0\)
\[
\frac{\det W_j(T)}{\det W_0(T)}=d_j^2,\qquad
 d_j=\frac{w_j^{m-1}}{\prod_{i\ne j}|w_j-w_i|},\qquad (1\le j\le m).
\]
Consequently, the exact D-optimal set is \(\operatorname{argmax}_{1\le j\le m}d_j\); the hub is strictly dominated by the leaf having the largest conductance, and the leaf having the smallest conductance is strictly dominated by the leaf having the second-smallest conductance. Moreover, for **every** rank \(r\in\{2,\ldots,m\}\), there exist distinct positive conductances whose unique D-optimal sensor is the leaf of \(r\)-th smallest conductance. The smallest star displaying a uniquely optimal non-largest-conductance leaf has three leaves (four vertices). An explicit instance is \((w_1,w_2,w_3)=(1,11/10,3)\), with relative determinant square-root scores \((1,5,121/19,45/19)\) for the hub and three leaves, respectively.

For arbitrary positive conductances, including repeated weights, the exact rank classification is as follows. If there is exactly **one** pair of equal leaf conductances and all remaining conductances are mutually distinct and different from that pair, exactly the two leaves in that pair have full-rank observability Gramians; their determinants are equal and positive, while every other candidate determinant is zero. If one conductance occurs at least three times, or two distinct conductance values each occur at least twice, all single-vertex Gramians are singular. In the latter case every determinant is zero, so this determinant objective does not distinguish sensor locations.

## Assumptions and scope

Dynamics are \(\dot x=-Lx\) in \(\mathbb R^{m+1}\), with direct observation \(y=x_j\) at exactly one vertex. The state includes the constant consensus mode; it is not projected out. Conductances are constant and positive; finite horizons are arbitrary but strictly positive. No noise model, second sensor, directed edge, or infinite-horizon full-state Gramian is asserted. The matrix \(L\) is given by \(L_{00}=\sum_iw_i\), \(L_{0i}=L_{i0}=-w_i\), \(L_{ii}=w_i\), and all other entries zero.

The D-optimality rule concerns \(\det W_j(T)\), not trace, minimum eigenvalue, pseudodeterminant, or the log determinant of a reduced disagreement-subspace Gramian. In the singular cases its value is exactly zero rather than a nonzero pseudodeterminant.

## Proof

**1. Simple spectrum and spectral determinant ratio.** First suppose all \(w_i\) are distinct. If \(Lv=\lambda v\), then the leaf equations are
\[
(w_i-\lambda)v_i=w_i v_0.
\]
The hub component \(v_0\) cannot vanish: otherwise at most one leaf coordinate could be nonzero (because the \(w_i\) are distinct), and the hub equation would force that coordinate to vanish too. Consequently no eigenvalue equals an edge weight, all eigenvectors have nonzero hub component, and every eigenspace is one-dimensional. Since \(L\) is real symmetric, its eigenvalues \(\lambda_0,\ldots,\lambda_m\) are simple and admit orthonormal eigenvectors \(v^{(k)}\).

Put \(\Phi_{ab}(T)=\int_0^T e^{-(\lambda_a+\lambda_b)t}\,dt\). The Gramian diagonalized in this eigenbasis has entries \(v_j^{(a)}\Phi_{ab}(T)v_j^{(b)}\). The kernel matrix \(\Phi(T)\) is positive definite: for a nonzero vector \(c\), its quadratic form is the integral of \(\bigl(\sum_a c_a e^{-\lambda_a t}\bigr)^2\), which cannot vanish identically on any positive-length interval because the exponentials have distinct real exponents. Thus
\[
\det W_j(T)=\det\Phi(T)\prod_{a=0}^{m}\bigl(v_j^{(a)}\bigr)^2>0.
\]
The leaf eigenvector relation gives \(v_j^{(a)}/v_0^{(a)}=w_j/(w_j-\lambda_a)\). Evaluating the characteristic polynomial at \(w_j\) by expanding \(w_j I-L\) first along leaf row \(j\), then along leaf column \(j\), gives
\[
\left|\prod_{a=0}^{m}(w_j-\lambda_a)\right|=w_j^2\prod_{i\ne j}|w_j-w_i|.
\]
Substitution proves the determinant-ratio formula and positive definiteness, without computing any eigenvalue or horizon integral.

**2. Exact Krylov determinants at coincident conductances.** Define \(\mathcal O_j\) as the square observability matrix with rows \(e_j^{\mathsf T}L^k\) for \(k=0,\ldots,m\). The continuous-time Gramian is nonsingular if and only if \(\mathcal O_j\) is nonsingular: if a vector lies in the Gramian nullspace then the analytic function \(e_j^{\mathsf T}e^{-tL}x\) vanishes over a positive interval, so all derivatives at zero vanish; the Cayley–Hamilton theorem handles the remaining powers. The reverse implication is immediate.

For the hub, remove the first row and hub column of \(\mathcal O_0\). Writing \(a_k=(L^k)_{00}\), the leaf entries satisfy
\[
(L^{k+1})_{0i}=w_i\bigl((L^k)_{0i}-a_k\bigr),\quad (L^0)_{0i}=0.
\]
Hence for \(k=1,\ldots,m\), the polynomial \((L^k)_{0i}\) has leading term \(-w_i^k\) and lower-degree terms shared across leaf columns. Elementary row operations reduce the minor to the Vandermonde matrix of powers \(w_i,w_i^2,\ldots,w_i^m\). Thus the **exact absolute determinant identity**, valid without distinctness, is
\[
|\det\mathcal O_0|=\Bigl(\prod_{i=1}^m w_i\Bigr)\prod_{a<b}|w_a-w_b|.
\]
For pairwise distinct weights, the same eigenbasis factorization applied to the square observability matrices gives
\[
\frac{|\det\mathcal O_j|}{|\det\mathcal O_0|}=d_j.
\]
Combining the two identities and cancelling all factors involving \(w_j\) yields
\[
|\det\mathcal O_j|=\Bigl(\prod_{i=1}^{m}w_i\Bigr)w_j^{m-1}
\prod_{\substack{a<b\\ a,b\ne j}}|w_a-w_b|.
\]
Both sides are continuous in all weights, and equality holds on the dense set of distinct conductances; it therefore holds for every positive weight assignment. It follows that the hub is observable exactly when all weights differ, whereas leaf \(j\) is observable exactly when the **other** \(m-1\) conductances are pairwise distinct. This gives the entire repeated-weight classification. When there is exactly one duplicate pair, swapping those two leaves is a weighted-graph automorphism and proves their Gramian determinants equal.

**3. Hub domination and the smallest-leaf exclusion.** For distinct conductances, let \(w_m\) be the largest after increasing reindexing. Every factor in \(\prod_{i<m}(w_m-w_i)\) lies strictly between zero and \(w_m\), so \(d_m>1\); the hub cannot maximize. Moreover,
\[
\frac{d_2}{d_1}=\Bigl(\frac{w_2}{w_1}\Bigr)^{m-1}
\prod_{k=3}^{m}\frac{w_k-w_1}{w_k-w_2}>1
\]
for \(0<w_1<w_2<\cdots<w_m\), with the empty product interpreted as one. This rules out rank one.

**4. Every other rank is possible.** Fix \(r\in\{2,\ldots,m\}\). Choose distinct lower conductances \(w_k\in(0,1/m)\) for \(k<r-1\), set \(w_{r-1}=1\), \(w_r=1+\varepsilon\), and choose distinct remaining conductances \(w_k>2\) for \(k>r\). All choices except \(\varepsilon>0\) are fixed. As \(\varepsilon\downarrow0\), both \(d_{r-1}\) and \(d_r\) grow proportionally to \(\varepsilon^{-1}\), while every other \(d_k\) stays bounded. The logarithmic ratio satisfies
\[
\left.\frac{d}{d\varepsilon}\log\frac{d_r}{d_{r-1}}\right|_{\varepsilon=0^+}
=(m-1)-\sum_{k\notin\{r-1,r\}}\frac{1}{1-w_k}.
\]
Terms with \(k>r\) are negative. Those with \(k<r-1\) are strictly less than \(m/(m-1)\). The displayed derivative therefore exceeds
\[
(m-1)-(r-2)\frac{m}{m-1}\ \ge\ \frac{1}{m-1}>0.
\]
Thus for sufficiently small positive \(\varepsilon\), \(d_r>d_{r-1}\) and both exceed every other leaf score. The hub score one is bounded too. Hence the rank-\(r\) leaf is uniquely D-optimal. For \(m=2\), rank two is the only possible unique optimal leaf; for \(m=3\), the rational example in the statement has rank two uniquely optimal. This completes the proof.

## Verification

The self-contained standard-library checker `verify.py` calculates exact rational Krylov determinants for 247 distinct/repeated-conductance instances with \(2\le m\le6\); all match the two algebraic determinant formulas. It also checks 44 constructive rank instances with \(2\le m\le9\) and all admissible nonminimum ranks. The recorded execution returned `VERIFY_OK`. These finite checks are diagnostics: the unrestricted dimension, positive real conductances, every horizon, and the boundary cases are proved by the preceding arguments, not inferred from enumeration.

## Relationship to prior work

Parlangeli and Notarstefano (arXiv:1109.3556, publicly submitted 2011-09-16) classify reachability and observability from nodes on **unweighted paths and cycles**; these results do not furnish the conductance-only star determinant rule. Xiang et al. (DOI 10.1155/2013/405034) discuss star symmetry and qualitative leader controllability in a different directed/heterogeneous model; they do not rank continuous-time single-coordinate star Gramians by D-optimal determinant. Summers and Lygeros (arXiv:1306.2491) introduce network Gramian placement metrics but focus on trace modularity, not this star-specific determinant law. Fitch and Leonard (DOI 10.1109/ECC.2016.7810511, Theorem 2) establish the important **general eigenvector-product principle** for log-volume leader selection in a disagreement-subspace framework. That principle is acknowledged as known, not claimed here; it does not itself provide the elementary conductance-only star formula, full-state finite-horizon ratios, coincident-weight rank classification, or all attainable optimal leaf ranks. Dilip (arXiv:1903.00456) treats discrete-time packet-loss Gramian invertibility and probabilistic placements rather than this weighted-star law.

## Limitations

Only positive symmetric star conductances and one direct scalar sensor are covered. The all-zero determinant regime is not a recommendation to place a sensor anywhere: it means that **no single vertex** yields full observability, so maximizing the ordinary determinant is uninformative. The one-leaf star (two vertices), excluded by \(m\ge2\), trivially ties hub and leaf. The positive eigenvalue-only infinite-horizon disagreement metric is not asserted identical as an absolute determinant; only the stated finite-horizon full-state ratios are proved. The star-specific simplification may be present in older control or interpolation literature under alternative language; the available literature comparison cannot certify uniqueness of discovery.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, first public submission 2011-09-16.
2. L. Xiang, J. J. H. Zhu, F. Chen and G. Chen, *Controllability of Weighted and Directed Networks with Nonidentical Node Dynamics*, Mathematical Problems in Engineering (2013), DOI: 10.1155/2013/405034, first published 2013-05-26.
3. T. H. Summers and J. Lygeros, *Optimal Sensor and Actuator Placement in Complex Dynamical Networks*, arXiv:1306.2491, first public submission 2013-06-11.
4. K. Fitch and N. E. Leonard, *Optimal leader selection for controllability and robustness in multi-agent networks*, European Control Conference (2016), DOI: 10.1109/ECC.2016.7810511, especially Theorem 2.
5. A. Sanand Amita Dilip, *Probabilistic state transfer, estimation and measures for optimal actuator/sensor placement for linear systems with packet dropouts*, arXiv:1903.00456, first public submission 2019-03-01.
