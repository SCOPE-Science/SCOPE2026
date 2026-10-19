# Exact two-to-four actuator thresholds on weighted cyclic prisms

## Finding
Let \(G_{n,w}\) be a cylindrical prism consisting of two copies of the unit-conductance cycle \(C_n\) joined at corresponding vertices by edges of conductance \(w>0\). For every integer \(n\ge3\), let \(m_n(w)\) be the smallest number of independently actuated vertices needed for controllability of the negative graph-Laplacian dynamics. Write
\[
K=\lfloor n/2\rfloor,\qquad c_j=\cos(2\pi j/n),\qquad
I_n=\begin{cases}\{1,\ldots,K\},&n\ \text{odd},\\\{1,\ldots,K-1\},&n\ \text{even},\end{cases}
\]
and define the finite positive weight sets
\[
\mathcal R_n=\{c_j-c_k:0\le j<k\le K\},\qquad
\mathcal Q_n=\{c_j-c_k:j<k,\ j,k\in I_n\}.
\]
Then the **exact minimum number of distinct node actuators**, for every \(n\ge3\) and \(w>0\), is
\[
\boxed{m_n(w)=\begin{cases}
4,&w\in\mathcal Q_n,\\
3,&w\in\mathcal R_n\setminus(\mathcal Q_n\cup\{2\}),\\
2,&\text{otherwise}.
\end{cases}}
\]
The case \(w=2\) is a single-to-single harmonic collision occurring only for even \(n\); it does not increase the minimum. Four actuators are first necessary at \(n=5\), \(w=\sqrt5/2\). For fixed \(n\) the exceptional weights are finite; the generic minimum is two.

Moreover, in the two-actuator regimes, *every* controllable pair is characterized. Normalize the first vertex to layer zero, position zero, and write the second vertex as layer \(t\in\{0,1\}\), position \(d\in\{0,\ldots,K\}\), using spatial reflection; the vertices must be distinct. Write \(\sigma=(-1)^t\). The pair is controllable **if and only if**
\[
\boxed{\gcd(n,2d)=\gcd(n,2)}
\]
and, only when \(n\) is even and \(w=2\), also \(\sigma\ne(-1)^d\).

## Assumptions and scope
The vertex set is \(\{(s,x):s\in\{0,1\},\ x\in\mathbb Z/n\mathbb Z\}\). Both rims have undirected unit-conductance edges from \((s,x)\) to \((s,x+1)\); each rung from \((0,x)\) to \((1,x)\) has conductance \(w>0\). There are no other edges. The symmetric, positive-semidefinite combinatorial Laplacian is \(L_{n,w}\). For a vertex set \(S\), the real continuous-time system is
\[
\dot z=-L_{n,w}z+B_Su,
\]
where the columns of \(B_S\) are the corresponding distinct standard coordinate vectors and each column receives a separate unrestricted scalar input. Controllability is the ordinary Kalman/PBH notion on the full \(2n\)-dimensional state space. The theorem does not concern edge actuators, positivity-constrained inputs, or nonlinear network dynamics.

## Proof
**Spectral splitting.** With vertices ordered by layer, write
\[
L_{n,w}=\begin{pmatrix}L(C_n)+wI&-wI\\-wI&L(C_n)+wI\end{pmatrix}.
\]
The symmetric and antisymmetric layer factors \((1,1)\) and \((1,-1)\) yield the respective eigenvalues \(\lambda_j=2-2c_j\) and \(\lambda_j+2w\), for \(j=0,\ldots,K\). The real spatial eigenspace \(H_j\) has dimension two for \(j\in I_n\), spanned by \(\cos(2\pi jx/n)\) and \(\sin(2\pi jx/n)\); it is one-dimensional at \(j=0\) and at \(j=K\) for even \(n\). The \(\lambda_j\) are strictly increasing with \(j\) in this range.

**Complete collision list and the lower bound.** A cross-layer eigenvalue coincidence is exactly
\[
\lambda_j+2w=\lambda_k\quad\Longleftrightarrow\quad
w=c_j-c_k>0,\qquad 0\le j<k\le K.
\]
Different \(j\) never coincide within a fixed layer parity, so a common eigenspace has dimension \(\dim H_j+\dim H_k\) at such a coincidence; otherwise its dimension is \(\dim H_j\). A double-to-double coincidence occurs exactly for \(w\in\mathcal Q_n\), giving dimension four. At any other coincidence the dimension is three unless both participating modes are simple. Both modes are simple only for even \(n\), with \((j,k)=(0,K)\), and then \(w=c_0-c_K=2\), giving dimension two. Independently of collisions, every \(n\ge3\) has an interior cycle frequency, hence an eigenspace of dimension at least two. Thus the largest Laplacian eigenspace has dimension exactly the displayed piecewise value. For a symmetric operator, the PBH criterion requires the input matrix to have at least as many columns as this dimension. This proves the lower bound.

**Simultaneously sharp upper bounds.** The following choices work at *every* \(n,w\) for which their stated size is the lower bound:
\[
S_2=\{(0,0),(0,1)\},\quad S_3=S_2\cup\{(1,0)\},\quad
S_4=S_3\cup\{(1,1)\}.
\]
For any interior \(j\), evaluation of the basis \((\cos(2\pi jx/n),\sin(2\pi jx/n))\) at \(x=0,1\) has determinant \(\sin(2\pi j/n)\ne0\). Thus the observations on both layers at positions zero and one separate both spatial harmonic coefficients in both layer parities, and \(S_4\) has full row rank on every eigenspace. For an eigenspace consisting of a two-dimensional harmonic of one parity and a one-dimensional harmonic of opposite parity, the restriction to \(S_3\) is a \(3\times3\) evaluation matrix whose determinant has absolute value \(2|\sin(2\pi j/n)|>0\). On every eigenspace of dimension at most two except the special simple-to-simple collision, observations on \(S_2\) have full row rank by the same sine determinant, or by nonvanishing on a one-dimensional mode. At the simple-to-simple collision \(n\) even, \(w=2\), the two basis vectors are a layer-symmetric alternating spatial vector and a layer-antisymmetric constant vector: their values at \((0,0)\) and \((0,1)\) form an invertible \(2\times2\) matrix. The PBH criterion therefore proves that \(S_{m_n(w)}\) is controllable, giving the matching upper bound.

**All two-site placements.** In the two-actuator regime, a pair, normalized as stated, restricted to the interior \(H_j\) of a single parity has evaluation determinant proportional to \(\sigma\sin(2\pi jd/n)\). Requiring this to be nonzero for each \(j\in I_n\) is equivalent to \(\gcd(n,2d)=\gcd(n,2)\): indeed, the first vanishing positive harmonic index is \(n/\gcd(n,2d)\). For odd \(n\), this index lies inside \(I_n\) exactly when \(\gcd(n,2d)>1\); for even \(n\) it lies inside exactly when \(\gcd(n,2d)>2\). Every simple noncolliding mode is nonzero at the first vertex. At the sole simple-to-simple collision \(w=2\) on even \(n\), the two basis vectors have normalized observations \((1,\sigma)\) and \((1,(-1)^d)\), so the additional determinant condition is \(\sigma\ne(-1)^d\). This completes the iff classification.

**First four-input dimension.** At \(n=3,4\) there is only one doubly degenerate spatial frequency, so \(\mathcal Q_n=\varnothing\). At \(n=5\), the interior frequencies are one and two, and \(\cos(2\pi/5)-\cos(4\pi/5)=\sqrt5/2\), proving the first four-actuator example.

## Verification
The standalone `verify.py` uses exact SymPy arithmetic to construct the full weighted Laplacian and determine Kalman ranks, testing 18 rational graph/weight/actuator configurations on sizes three through six. It also checks exactly the algebraic collision identity at \(n=5\), \(w=\sqrt5/2\). For example, on the six-rung prism with \(w=1\), three specified actuators have rank eleven instead of twelve, while the four-site set has full rank. At \(n=4\), \(w=2\), the two adjacent same-layer inputs have full rank, whereas an across-layer offset one fails. These finite tests corroborate but do not substitute for the preceding all-parameter PBH proof. Run `python verify.py` with SymPy installed.

## Relationship to prior work
Parlangeli and Notarstefano classify reachability for paths and cycles, including arithmetic restrictions on cycle leaders [1]. The Chapman–Nabi-Abdolyousefi–Mesbahi Cartesian-product papers supply general eigenspace and controllability conditions [2,3]; their general tests can in principle be specialized to this product but do not state the exact rung-conductance resonance partition or complete sharp vertex-actuator placements derived above. The grid-graph results of Notarstefano and Parlangeli [4] concern Cartesian products of **paths**, rather than the cyclic-prism family. The result here evaluates the spectral intersections and actuator restrictions explicitly for every order and every positive rung weight.

## Limitations
The proof applies only to uniform positive rung conductance and unit-weight cycles, independently actuated vertex inputs, and continuous-time linear Laplacian dynamics. It establishes Kalman controllability, not optimized Gramian conditioning or control energy. The matrix computations are finite spot checks, not exhaustive evidence for infinite graphs. No claim is made that the result has undergone independent review; analogous unindexed statements may exist.

## References
[1] R. Parlangeli and G. Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs*, arXiv:1109.3556v1, first posted 2011-09-16, https://arxiv.org/abs/1109.3556.

[2] A. Chapman, A. Nabi-Abdolyousefi, and M. Mesbahi, *On the Controllability and Observability of Cartesian Product Networks*, IEEE Conference on Decision and Control (2012), doi:10.1109/CDC.2012.6426230.

[3] A. Chapman, A. Nabi-Abdolyousefi, and M. Mesbahi, *Controllability and Observability of Network-of-Networks via Cartesian Products*, IEEE Transactions on Automatic Control 59 (2014), 2668–2679, doi:10.1109/TAC.2014.2328757.

[4] G. Notarstefano and R. Parlangeli, *Controllability and Observability of Grid Graphs via Reduction and Symmetries*, arXiv:1203.0129v1 (2012-03-01), https://arxiv.org/abs/1203.0129.
