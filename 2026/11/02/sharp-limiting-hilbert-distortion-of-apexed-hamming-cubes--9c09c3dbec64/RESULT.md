# Sharp limiting Hilbert distortion of apexed Hamming cubes

## Finding
For each integer \(d\ge2\), let \(Q_d\) be the graph of binary strings of length \(d\), adjacent when they differ in one coordinate. Form its *graph cone* \(G_d=K_1\vee Q_d\) by adjoining a new vertex \(o\) connected by a unit edge to every cube vertex. Give \(G_d\) the unweighted shortest-path metric. For its least distortion into a real Hilbert space, the following bounds hold without any target-dimension restriction:
\[
\sqrt{\frac{8(d-1)}{3d}}\ \le\ c_2(G_d)\ \le\ \sqrt{\frac83}.
\]
Both bounds together yield the **sharp limiting distortion**
\[
\lim_{d\to\infty}c_2(G_d)=\sqrt{\frac83}.
\]
A closed-form feature map attains the uniform upper bound. Moreover, for each finite \(d\), an explicitly specified linear program involving only \(d+1\) nonnegative real variables determines \(c_2(G_d)^2\) exactly; its formulation appears below. These statements concern one and the same metric-embedding invariant, not the Banach--Mazur distance of a Lipschitz-free space.

## Assumptions and scope
A map \(f:X\to H\) to a real Hilbert space has distortion at most \(C\ge1\) if it can be scaled so that
\[
 d_X(x,y)\le\|f(x)-f(y)\|\le C\,d_X(x,y)
\]
for all distinct \(x,y\); \(c_2(X)\) is the infimum of admissible \(C\). All Hilbert target dimensions are allowed. For cube vertices \(x,y\in\{0,1\}^d\) at Hamming distance \(k\), the graph metric is \(1\) if \(k=1\), and \(2\) if \(k\ge2\); every cube vertex lies at graph distance \(1\) from the new apex \(o\). The assertions hold for all integers \(d\ge2\), including \(d=2\). No equality of the upper bound at a fixed finite \(d\) is claimed.

## Proof
**Upper bound and explicit embedding.** In \(\mathbb R^2\), choose unit vectors \(u_0=(1,0)\) and \(u_1=(1/2,\sqrt3/2)\), whose inner product is \(1/2\). Let \(H_d=(\mathbb R^2)^{\otimes d}\) with its Euclidean tensor-product inner product, and set
\[
 f(o)=0,\qquad
 f(x)=\sqrt{8/3}\,\bigotimes_{i=1}^d u_{x_i}.
\]
Every base image has squared norm \(8/3\). If two binary words differ in exactly \(k\) coordinates, their inner product is \((8/3)2^{-k}\), so their squared Euclidean separation is
\[
 \|f(x)-f(y)\|^2=\frac{16}{3}(1-2^{-k}).
\]
For \(k=1\), this is \(8/3\); for every \(k\ge2\), it lies in \([4,16/3)\). Together with \(\|f(x)-f(o)\|^2=8/3\), these inequalities show that \(f\) is noncontracting and has distortion \(\sqrt{8/3}\) (the expansion is attained on every apex edge and every cube edge). Thus the upper bound is valid for every \(d\).

**Lower bound for arbitrary Hilbert embeddings.** Fix \(d\ge2\), and take any noncontracting embedding with distortion \(C\). Translate its apex image to the origin, write its cube images as a Hilbert-valued function \(v(x)\), and put \(t=C^2\). For all \(x\), the apex edges give \(\|v(x)\|^2\le t\). For every coordinate \(i\), ordinary cube edges give \(\|v(x)-v(x\oplus e_i)\|^2\le t\). For all distinct \(i,j\), two-bit flips are at graph distance \(2\), so
\[
 \|v(x)-v(x\oplus e_i\oplus e_j)\|^2\ge4.
\]
Here \(\oplus\) means binary coordinate addition. For each \(S\subseteq\{1,\ldots,d\}\), use the normalized Walsh coefficient
\[
 \widehat v(S)=2^{-d}\sum_{x\in\{0,1\}^d}(-1)^{\sum_{i\in S}x_i}v(x),
 \qquad w_S=\|\widehat v(S)\|^2\ge0.
\]
Hilbert-valued Parseval yields \(R:=\sum_S w_S=\mathbb E_x\|v(x)\|^2\le t\). Set \(U:=\sum_S|S|w_S\) and \(V:=\sum_S|S|^2w_S\). Averaging squared edge lengths over uniformly chosen \(x\) and \(i\) gives \(4U/d\le t\), hence \(U\le dt/4\). Averaging squared two-bit-flip distances over uniformly chosen \(x\) and unordered \(\{i,j\}\) gives the **identity**
\[
 \mathbb E_{x,i<j}\|v(x)-v(x\oplus e_i\oplus e_j)\|^2
 =\frac{8}{d(d-1)}(dU-V).
\]
Indeed a Walsh character of weight \(j\) changes sign under exactly \(j(d-j)\) unordered two-bit flips, producing a squared increment of \(4\), and averaging produces the coefficient \(8j(d-j)/(d(d-1))\). Cauchy--Schwarz gives \(U^2\le RV\le tV\), so \(V\ge U^2/t\). Since \(0\le U\le dt/4\), the concave function \(dU-U^2/t\) is increasing throughout the allowed interval; therefore
\[
 dU-V\le dU-U^2/t\le \frac{3d^2t}{16}.
\]
The two-bit-flip lower bound now implies
\[
 4\le \frac{8}{d(d-1)}\frac{3d^2t}{16}
 =\frac{3dt}{2(d-1)},
 \quad\text{so}\quad t\ge\frac{8(d-1)}{3d}.
\]
This proof applies to every Hilbert space, every embedding, and every integer \(d\ge2\). Combining it with the explicit upper construction proves the claimed limit by squeezing. In particular, the limiting constant is an exact value, not an extrapolation from finite computations.

**Exact finite-dimensional linear-program characterization.** Let \(\binom ab=0\) when \(b<0\) or \(b>a\), and for \(0\le j,k\le d\) define the normalized binary Krawtchouk values
\[
 \kappa_{j,d}(k)=\frac{1}{\binom dj}
 \sum_{r=0}^{j}(-1)^r\binom kr\binom{d-k}{j-r}.
\]
For fixed \(d\), minimize \(t\) over real \(t,w_1,\ldots,w_d\) subject to \(w_j\ge0\),
\[
 1\le\sum_{j=1}^dw_j\le t,\qquad
 1\le a_1\le t,\qquad
 4\le a_k\le4t\ (2\le k\le d),
\]
where \(a_k=2\sum_{j=1}^d w_j(1-\kappa_{j,d}(k))\). Its minimum equals \(c_2(G_d)^2\). To see this, translate an arbitrary embedding so that its apex is zero and average its positive-semidefinite Gram matrix over the cube's coordinate translations and permutations. The averaged matrix remains positive semidefinite and satisfies all the pairwise lower and upper squared-distance inequalities; by Fourier diagonalization it is a nonnegative mixture of the Walsh degree kernels, with mass \(w_j\) at degree \(j\). A potential degree-zero mass affects only squared distances to the apex. It can be discarded because \(a_2\ge4\) and \(a_2\le4\sum_{j\ge1}w_j\) already force the remaining mass to be at least \(1\). Conversely, each feasible nonnegative mixture is a real positive-semidefinite Gram matrix, hence defines Hilbert vectors with precisely the indicated orbitwise squared distances and apex at zero. This establishes equality of the two optima; no symmetry of an optimal embedding has been assumed in advance.

## Verification
The accompanying standalone Python 3 script `VERIFY.py` uses only exact rational arithmetic and the standard library. It checks the tensor construction's distance inequalities, the normalized degree-one and degree-two Walsh formulas, and a finite collection of Parseval-energy identities; execution reports `CHECK_OK exact_rational_assertions= 4030 dimensions_tensor=2..40 dimensions_fourier=2..40`. The unrestricted lower and upper proofs above, rather than this finite test, establish the claimed infinite family and limiting constant.

## Relationship to prior work
Robertson (2023, arXiv:2309.16070) develops distorted negative type and treats the ordinary Hamming-cube metric and complete bipartite metrics, but not the graph-cone metric whose longer Hamming distances are truncated to two. The ordinary cube has distortion growing as \(\sqrt d\), whereas the cone family's distortion converges to a constant. Vallentin (2005, arXiv:math/0509716) and Cioabă--Gupta--Ihringer--Kurihara (2021, arXiv:2109.09708) develop spectral results for distance-regular graphs; the cone here is not distance regular because its apex and cube vertices have different degrees when \(d\ge2\). Linial and Magen study products of cycles and expanders, including ordinary cubes; the added universal vertex changes the metric and the relevant optimization. The finite LP uses standard symmetry and positive-kernel principles, but the sharp asymptotic constant follows from the particular first/two-shell Fourier energy comparison and the matching tensor construction. No priority assertion is made for general Fourier or semidefinite-programming methods.

## Limitations
The theorem proves sharp asymptotics, not an explicit closed-form value of \(c_2(G_d)\) for every finite \(d\). The LP characterization is exact but may still require finite optimization. The tensor construction uses dimension \(2^d\), with no dimension-minimality claim. The scope is binary cubes, an unweighted universal hub, and real Hilbert targets. Search-based historical originality remains provisional: synonymous earlier formulations or not fully indexed literature may exist. No independent mathematical audit has been performed.

## References
- G. Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, first arXiv version September 27, 2023, arXiv:2309.16070.
- F. Vallentin, *Optimal Embeddings of Distance Regular Graphs into Euclidean Spaces*, arXiv:math/0509716 (first version September 30, 2005).
- S. M. Cioabă, H. Gupta, F. Ihringer, H. Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, arXiv:2109.09708 (first version September 20, 2021).
- N. Linial and A. Magen, *Least-Distortion Euclidean Embeddings of Graphs: Products of Cycles and Expanders*, manuscript dated June 12, 2001; author's publicly available PDF at https://www.cs.toronto.edu/~avner/papers/least-distortion.pdf.
