# Odd Jordan ladders and a sharp \(15/16\) last-step law for honeycomb parity dynamics

## Finding
Let \(k=2^a\) with integer \(a\ge0\), and set \(L=3k\). On the cubic bipartite honeycomb torus \(H_k\) defined below, let \(F_k\) synchronously replace each binary vertex value by the XOR of its three neighbors. The finite-dimensional system has the following exact decomposition over \(\mathbb F_2\): a periodic (invertible) subspace of dimension \(14k^2\), and a nilpotent subspace with **four Jordan blocks of every odd length** \(1,3,\ldots,2k-1\), with no other nilpotent blocks. Consequently:

* There are exactly \(2^{14k^2}\) recurrent configurations, and each recurrent configuration is reached from precisely \(2^{4k^2}\) initial states after all transients have passed.
* The sharp largest transient length, counting synchronous updates until the first periodic configuration, is \(2k-1\).
* Define \(\rho_{2t}=4(k-t)^2\) for \(0\le t\le k\), and \(\rho_{2t+1}=4(k-t-1)(k-t)\) for \(0\le t<k\); take \(\rho_s=0\) for \(s\ge2k-1\). Exactly \(2^{18k^2-\rho_s}\) configurations have transient length at most \(s\) for every integer \(s\ge0\).
* Exactly \(15/16\) of all \(2^{18k^2}\) configurations have transient length **equal to** \(2k-1\).

The exact number having transient length \(s>0\) is the difference of the two cumulative counts at \(s\) and \(s-1\).

## Assumptions and scope
Indices \(i,j\) are taken modulo \(L\). Vertices are \(A_{i,j}\) and \(B_{i,j}\), for every ordered pair \((i,j)\). The edges are exactly
\[
A_{i,j}\sim B_{i,j},\qquad A_{i,j}\sim B_{i-1,j},\qquad A_{i,j}\sim B_{i,j-1}.
\]
Thus \(H_k\) has \(2L^2=18k^2\) vertices and is a simple connected cubic quotient of the planar honeycomb lattice. A configuration lies in \(\mathbb F_2^{V(H_k)}\), and
\[
(F_k z)(v)=\sum_{u\sim v}z(u)\pmod2.
\]
A state is recurrent precisely when it lies on a finite periodic orbit; its transient length is the least nonnegative update count at which a recurrent state appears. All configuration counts are for labelled vertex positions, without quotienting by graph automorphisms.

## Proof
**1. Exact two-sublattice symbol.** Identify each layer with
\[
R=\mathbb F_2[X^{\pm1},Y^{\pm1}]/(X^L-1,Y^L-1).
\]
Encoding coefficients at positions \((i,j)\) by \(X^iY^j\), the update becomes
\[
F_k=\begin{pmatrix}0&P\\Q&0\end{pmatrix},\quad
P=1+X+Y,\quad Q=1+X^{-1}+Y^{-1}.
\]
The two Laurent symbols correspond to the three specified undirected neighbors in opposite directions.

**2. Separate two singular frequency cells.** Extend scalars to \(\mathbb F_4\) and choose \(\omega\) with \(\omega^2+\omega+1=0\). As \(k=2^a\), the Frobenius identity gives
\[
X^{3k}-1=(X^3-1)^k,
\]
and similarly in \(Y\). The Chinese remainder decomposition gives nine local rings, one for each \((\alpha,\beta)\in\{1,\omega,\omega^2\}^2\), each isomorphic to
\[
\mathbb F_4[u,v]/(u^k,v^k)
\]
with \(X=\alpha+u\) and \(Y=\beta+v\). Among these nine pairs, \(1+\alpha+\beta=0\) holds only for \((\omega,\omega^2)\) and \((\omega^2,\omega)\). On precisely these two pairs both \(P\) and \(Q\) have zero constant term. On the other seven, both are units, so the update is invertible there. The seven unit factors contribute \(7\cdot2k^2=14k^2\) to the dimension over the scalar extension, hence also over \(\mathbb F_2\).

**3. Local coordinate independence.** At either singular root, \(P=u+v\), while \(Q=1+(\alpha+u)^{-1}+(\beta+v)^{-1}\). The Jacobian of \((P,Q)\) with respect to \((u,v)\) at the origin has determinant
\[
\beta^{-2}+\alpha^{-2}=\beta+\alpha=1.
\]
The map is therefore a change of formal local coordinates. Moreover \(P^k=Q^k=0\) because each has no constant term and \(k\) is a power of two. Since their linear parts span the cotangent space, the finite local algebra is exactly
\[
\mathbb F_4[p,q]/(p^k,q^k),\qquad p=P,\ q=Q.
\]
This follows from the formal inverse-function theorem, or by induction in the nilpotent maximal ideal; source and target have the same dimension \(k^2\).

**4. Exact ranks and Jordan types.** In each singular local factor, the update is
\[
N=\begin{pmatrix}0&p\\q&0\end{pmatrix}.
\]
Its even iterate \(N^{2t}\) has both diagonal entries \((pq)^t\), so its local rank is \(2(k-t)^2\). Its odd iterate \(N^{2t+1}\) has off-diagonal multipliers \(p^{t+1}q^t\) and \(p^tq^{t+1}\), giving rank \(2(k-t-1)(k-t)\). These statements hold for the valid nonnegative parameter ranges, and all later ranks are zero. Summing over the two singular roots gives the \(\mathbb F_2\) ranks
\[
\rho_{2t}=4(k-t)^2,\qquad \rho_{2t+1}=4(k-t-1)(k-t).
\]
Extending scalars preserves matrix rank, so there is no extra factor for \(\mathbb F_4\). Successive rank differences show that the nilpotent Jordan blocks occur four times in every odd length \(1,3,\ldots,2k-1\), and never in even lengths. In particular \(\rho_{2k-2}=4\) and \(\rho_{2k-1}=0\), making \(2k-1\) the sharp nilpotence and transient index.

**5. Recurrent and transient counts.** The Fitting decomposition is the direct sum of the \(14k^2\)-dimensional invertible component and the \(4k^2\)-dimensional nilpotent component. On a finite vector space, every invertible orbit is periodic. The states of transient length at most \(s\) are precisely those with nilpotent component in \(\ker N^s\). Therefore their number is \(2^{14k^2+(4k^2-\rho_s)}=2^{18k^2-\rho_s}\). The nilpotent kernel after complete convergence has size \(2^{4k^2}\), the attraction fibre size for any recurrent state. Since \(\rho_{2k-2}=4\), precisely \(2^{18k^2}-2^{18k^2-4}\) states need the final step. Dividing by the total gives \(15/16\), as claimed.

## Verification
A standalone C++17 checker in `verification/verify.cpp` builds each labelled undirected graph directly from the edge rule, repeatedly computes all columns of the binary adjacency powers, and performs independent Gaussian elimination over \(\mathbb F_2\). It checks all predicted ranks for \(k\in\{1,2,4,8\}\), corresponding to 18, 72, 288 and 1152 vertices and all stages through \(2k\). For \(k=1\), it additionally exhausts all \(262144\) states and confirms that exactly \(16384\) lie in the recurrent image and \(245760\) have one-step transient. Compile with `g++ -O3 -std=c++17 verification/verify.cpp -o verify` and run `./verify`. Recorded output is `verification/verify.out`, ending in `HONEYCOMB_VERIFY_OK`. These checks test the proof but do not replace the all-\(a\) algebraic argument.

## Relationship to prior work
The honeycomb Bloch-symbol and its two ordinary zero-mode frequencies are classical; Hasegawa, Konno, Nakano and Kohmoto derive them for a complex tight-binding Hamiltonian [1]. Bulitko [2] provides a group-convolution framework for finite additive cellular automata. Gajardo and Goles [3] study a three-state universal vertex-honeycomb rule; that rule is not binary XOR. The 2011 work [5] uses ternary-state hexagonal cells and null boundaries, rather than the periodic cubic vertex-honeycomb graph. Kirby, Mallion and Pollak [4] investigate ordinary toroidal-polyhex adjacency spectra. The present theorem instead concerns characteristic-two powers of the adjacency map, its nilpotent Jordan lengths and the exact transient count of every labelled binary configuration. No stronger equivalent statement was identified in the inspected source material; nonidentification is not proof of historical uniqueness.

## Limitations
The theorem is restricted to untwisted square honeycomb quotients of side length \(3\cdot2^a\), with synchronous undirected neighbor XOR over \(\mathbb F_2\). It does not determine the lengths of individual recurrent cycles, arbitrary toroidal-polyhex twist parameters, asymmetric circumferences or other fields. The full 1993 toroidal-polyhex article and the full 2001 three-state article were not inspected, leaving a limited possibility of hidden historical overlap. The sample computations alone cannot establish any infinite-family conclusion.

## References
1. Y. Hasegawa, R. Konno, H. Nakano and M. Kohmoto, *Zero modes of tight binding electrons on the honeycomb lattice*, arXiv:cond-mat/0604433, initial public preprint 2006-04-19. https://arxiv.org/abs/cond-mat/0604433
2. V. Bulitko, *Isomorphisms of Additive Cellular Automata on Finite Groups*, arXiv:0812.0111, initial public preprint 2008-11-29. https://arxiv.org/abs/0812.0111
3. A. Gajardo and E. Goles, *Universal cellular automaton over a hexagonal tiling with 3 states*, *International Journal of Algebra and Computation* 11 (2001), 335–354. https://doi.org/10.1142/S0218196701000486
4. E. C. Kirby, R. B. Mallion and P. Pollak, *Toroidal polyhexes*, *Journal of the Chemical Society, Faraday Transactions* 89 (1993), 1945–1953. https://doi.org/10.1039/FT9938901945
5. *Structure and reversibility of 2D hexagonal cellular automata*, *Computers & Mathematics with Applications* 62 (2011), 4161–4169. https://doi.org/10.1016/j.camwa.2011.09.066
