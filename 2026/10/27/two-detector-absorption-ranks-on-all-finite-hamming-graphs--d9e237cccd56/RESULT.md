# Two-detector capture on nonbinary Hamming graphs

## Finding

For every integer \(q\ge3\) and \(d\ge1\), place two strictly positive local irreversible absorbers at any distinct vertices \(u,v\) of the Hamming graph \(H(d,q)=K_q^{\square d}\). For continuous-time unit adjacency hopping, the subspace of states that are fully absorbed has dimension \(2d+1\), independent of the positive absorption rates and of the Hamming distance between \(u\) and \(v\). With a uniform initial vertex, eventual absorption has probability \((2d+1)/q^d\); if the initial vertex is uniform outside \(\{u,v\}\), it is \((2d-1)/(q^d-2)\).

There is an exact site-resolved law. Write \(a=\operatorname{dist}(x,u), b=\operatorname{dist}(x,v), h=\operatorname{dist}(u,v)\), and set
\[
 K_k(s)=\sum_{j=0}^k(-1)^j(q-1)^{k-j}\binom{s}{j}\binom{d-s}{k-j},\qquad B_k=\binom dk(q-1)^k,
\]
where out-of-range binomial coefficients vanish. The eventual absorption probability from \(x\) is
\[
 \eta_x=q^{-d}\left[1+\sum_{k=1}^d
 \frac{B_k(K_k(a)^2+K_k(b)^2)-2K_k(h)K_k(a)K_k(b)}{B_k^2-K_k(h)^2}\right].
\]
Every denominator is positive. Placement can therefore matter at individual sites even when the average is fixed: in \(H(2,3)\), with \(u=(0,0)\) and \(x=(2,0)\), the formula gives \(3/5\) at \(v=(1,0)\) and \(2/5\) at \(v=(1,1)\); both configurations have average \(5/9\).

## Assumptions and scope

The vertices are length-\(d\) words on \(q\) letters, adjacent if they differ in exactly one coordinate. There are exactly two distinct lossy sites, and the unnormalized evolution is \(U(t)=\exp(-itH_{\rm eff})\), where
\[
 H_{\rm eff}=A-\tfrac i2\Gamma,\qquad \Gamma=\gamma_u|u\rangle\langle u|+\gamma_v|v\rangle\langle v|,\qquad \gamma_u,\gamma_v>0.
\]
Here \(A\) is the unit adjacency matrix, the initial density matrix has trace one, and eventual absorption is \(1-\lim_{t\to\infty}\operatorname{tr}(U(t)\rho U(t)^\dagger)\). The model has no dephasing, disorder or replenishment. No finite-time or zero-loss statement is made.

## Proof

Let \(P_k\) be the eigenspace projectors of \(A\), with each distinct eigenvalue used once. Let \(\mathcal B\) be the orthogonal direct sum of the spans of \(P_k|u\rangle,P_k|v\rangle\). Then \(\mathcal B^\perp\) is the direct sum of the parts of each eigenspace orthogonal to both absorbers. Both spaces reduce \(A\) and the loss; on \(\mathcal B^\perp\) the evolution is unitary. An eigenvector \(z\ne0\) of the restriction of \(H_{\rm eff}\) to \(\mathcal B\) has eigenvalue with imaginary part \(-\langle z,\Gamma z\rangle/(2\|z\|^2)\). Equality to zero would put \(z\) in \(\ker\Gamma\) and make it an adjacency eigenvector orthogonal to both absorbers, contradicting \(z\in\mathcal B\). Thus the finite-dimensional exponential tends to zero on \(\mathcal B\), even for nondiagonalizable restrictions. In particular \(U(t)^\dagger U(t)\to I-P_{\mathcal B}\), so absorption is \(\operatorname{tr}(P_{\mathcal B}\rho)\).

On one coordinate, the adjacency of \(K_q\) has eigenvalues \(q-1,-1\), with projections \(C=J/q\) and \(D=I-C\), where \(J\) is the all-ones matrix. In the product, eigenvalue \(d(q-1)-qk\) has projector \(P_k\) given by summing tensors with \(D\) on exactly \(k\) coordinates and \(C\) elsewhere. Between two words at distance \(s\), a term with \(j\) differing coordinates chosen among its \(k\) factors contributes \(q^{-d}(-1)^j(q-1)^{k-j}\). Counting these choices gives \(\langle x|P_k|y\rangle=q^{-d}K_k(\operatorname{dist}(x,y))\).

The Gram matrix of the two projected absorber vectors at level \(k\) is therefore \(q^{-d}\begin{pmatrix}B_k&K_k(h)\\K_k(h)&B_k\end{pmatrix}\). At \(k=0\) it has rank one. For \(k\ge1\), if \(J_h\) counts differing coordinates in a uniform \(k\)-subset, the normalized off-diagonal is \(K_k(h)/B_k=\mathbb E[(-1/(q-1))^{J_h}]\). Since \(h\ge1\), the event \(J_h>0\) has positive probability, and its contribution has modulus strictly less than one because \(q\ge3\). Thus \(|K_k(h)|<B_k\), and every nonconstant level has rank two, including \(k=d\). The sum of the ranks is \(2d+1\).

Inverting each rank-two Gram block and applying it to \(q^{-d}(K_k(a),K_k(b))\) gives the indicated contribution to the squared projection of \(|x\rangle\). The constant level contributes \(q^{-d}\). The trace of the full projection gives the uniform average. Both monitored basis vectors already belong to \(\mathcal B\), so removing their contributions yields the outside-monitor average. In the boundary case \(d=1\), the rank is three and the uniform average is \(3/q\); the unmonitored sites are symmetric and each has probability \(1/(q-2)\).

## Relationship to prior work

The binary two-detector rank dichotomy and its sitewise Krawtchouk law were already established in [*Two absorbers on a quantum hypercube: antipodal redundancy and exact survival*](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-two-absorbers-on-a-quantum-hypercube-antipodal-redundancy-and-ex--e6d55236b096). That result and the single-absorber hypercube method of Novo et al. ([arXiv:1412.7209](https://arxiv.org/abs/1412.7209)) are prior work. The new assertion concerns the nonbinary product graphs: the placement-independent rank and explicit site probabilities for all alphabet sizes \(q\ge3\) and all dimensions. The bright-space projection method itself is not claimed as new. The later Resultary notes [on nonbinary Hamming graphs](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-placement-invariant-two-sink-quantum-capture-on-nonbinary-hammin--53f69c4afebe) and [on primitive distance-regular graphs](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-two-absorber-capture-on-primitive-distance-regular-quantum-netwo--1660beea2236) overlap with this nonbinary conclusion; the latter formulates a more general cosine-sequence capture law.

## Reproducibility

The accompanying `verify_two_monitor.py` includes finite checks of nonbinary ranks and site probabilities, along with binary comparison cases. It constructs the adjacency matrix and its spectral projections and compares against the exact formulas; one finite-time propagation example uses unequal positive rates in \(H(2,3)\). These numerical checks are corroboration only. The rank and limiting probabilities in the theorem follow from the proof for all \(q,d\).
