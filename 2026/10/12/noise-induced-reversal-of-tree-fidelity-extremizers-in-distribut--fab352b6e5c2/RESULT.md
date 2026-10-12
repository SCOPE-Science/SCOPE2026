# Noise-induced reversal of tree-fidelity extremizers in distributed graph states
## Finding
Consider the exact resource-qubit noise model of Dutta's graph-state distribution protocol: each target tree \(T\) has \(n\ge4\) data vertices and one entangled resource pair per edge, so \(2(n-1)\) resource qubits. Independent identical noise acts on the resource qubits **after** the local walk \(\mathrm{CZ}\) gate and **before** the measurement Hadamard. Data qubits, all gates, and readout are ideal. The corrected-state fidelity is taken against the graph state associated with that same tree.

For any real \(q\in[-1/3,1]\), set
\[
\Psi_q(T)=2^{-n}\prod_{v\in V(T)}\bigl(1+q^{\deg_T(v)}\bigr).
\]
The source proves that its resource-depolarization fidelity is \(F_{\mathrm{dep}}(T,p)=\Psi_{1-4p/3}(T)\) and its resource-phase-damping fidelity is \(F_{\mathrm{pd}}(T,p)=\Psi_{\sqrt{1-p}}(T)\).

The **exact extremal tree phase diagram** is as follows.

For resource depolarization with \(0<p<3/4\),
\[
\boxed{\Psi_q(P_n)\le\Psi_q(T)\le\Psi_q(K_{1,n-1}),\qquad q=1-4p/3>0.}
\]
Equality on the left holds only for the path \(P_n\), and equality on the right only for the star \(K_{1,n-1}\), up to graph isomorphism.

For resource depolarization with \(3/4<p\le1\), the ordering **reverses**:
\[
\boxed{\Psi_q(K_{1,n-1})\le\Psi_q(T)\le\Psi_q(P_n),\qquad q=1-4p/3<0.}
\]
Again the two equality cases characterize the indicated trees. At \(p=0\), every tree has fidelity one; at the completely depolarizing point \(p=3/4\), every tree has fidelity \(2^{-n}\).

For phase damping, the source's parameter is \(q=\sqrt{1-p}\), so the path-minimal and star-maximal ordering holds for every \(0<p<1\). At \(p=0\), every tree has fidelity one, and at \(p=1\), every tree has fidelity \(2^{-n}\).

The exact endpoint values for a given \(q\) are
\[
\Psi_q(P_n)=2^{-n}(1+q)^2(1+q^2)^{n-2},
\qquad
\Psi_q(K_{1,n-1})=2^{-n}(1+q)^{n-1}(1+q^{n-1}).
\]

A hardware-motivated restriction has an even simpler exact classification. Among abstract trees satisfying the **necessary degree constraint** \(\Delta(T)\le3\), let \(k\) be the number of degree-three vertices. Every integer
\[
0\le k\le\left\lfloor\frac{n-2}{2}\right\rfloor
\]
is realizable by some tree, and the fidelity is
\[
\boxed{\Psi_q(T)=2^{-n}(1+q)^{k+2}(1+q^2)^{n-2-2k}(1+q^3)^k.}
\]
Increasing \(k\) by one changes the fidelity by the exact factor
\[
\boxed{\frac{\Psi_q(k+1)}{\Psi_q(k)}
=\frac{(1+q)(1+q^3)}{(1+q^2)^2}
=1+\frac{q(1-q)^2}{(1+q^2)^2}.}
\]
Thus \(k=\lfloor(n-2)/2\rfloor\) is optimal for positive \(q\) and worst for negative \(q\); \(k=0\), the path, has the reverse position. For \(q=0\) or \(q=1\), the branch count makes no difference. Distinct subcubic tree shapes with the same \(k\) have equal fidelity in this model; neither extremal class is necessarily one unique graph.

For example, at \(n=8\), depolarization \(p=0.5\) gives approximately \(0.0292772\) for the star and \(0.0130672\) for the path, whereas \(p=0.95\) gives approximately \(0.00044548\) for the star and \(0.00317227\) for the path.

## Assumptions and scope
All graph comparisons are among **different target tree graph states on the same number of parties**, not different circuits preparing a fixed target graph state. Every tree consumes exactly \(n-1\) elementary entangled pairs in this protocol, so the resource-pair count is held fixed. The noise acts only at the location specified in the source. No gate errors, correlated errors, data-qubit decoherence, measurement errors, or choice of physical hardware layout are included.

The depolarization channel uses the source's Pauli convention
\[
\mathcal E_p(\rho)=(1-p)\rho+\frac p3\sum_{P\in\{X,Y,Z\}}P\rho P,
\qquad 0\le p\le1.
\]
At \(p=3/4\) this is completely depolarizing, while at \(p>3/4\) its Pauli contraction coefficient \(q=1-4p/3\) is negative but the channel remains completely positive in the entire stated interval. This high-noise regime is part of the stated model; no extrapolation to unphysical channel strengths is made.

The degree-three restriction is necessary for SWAP-free native execution on a maximum-degree-three coupling architecture in the source, **not sufficient** for embedding. The optimal abstract degree sequences therefore do not assert that a given device can realize every such tree without routing.

## Proof
The source's independent resource-qubit error-parity argument proves the degree-product formulas above. Our task is to optimize that fixed objective over tree degree sequences. A tree has positive integer degrees \(d_1,\ldots,d_n\) with
\[
\sum_{i=1}^n d_i=2n-2.
\]
Put \(t_i=d_i-1\). Then \(t_i\ge0\) are integers with
\[
\sum_{i=1}^n t_i=n-2.
\]
Conversely, every such vector is the excess-degree sequence of a tree: a Prüfer word with vertex \(i\) appearing \(t_i\) times realizes precisely these degrees.

**Positive-contraction regime.** Suppose \(0<q<1\). The function
\[
f_q(s)=\log(1+q^s)
\]
is strictly convex for real \(s\ge1\), since
\[
f_q''(s)=\frac{(\log q)^2q^s}{(1+q^s)^2}>0.
\]
Every nonnegative integer vector summing to \(n-2\) is majorized by the star excess vector
\[
(n-2,0,\ldots,0)
\]
and majorizes the path excess vector
\[
(\underbrace{1,\ldots,1}_{n-2},0,0).
\]
The second assertion follows because any nonzero excess is at least one, so concentrating any excess into fewer components moves upward in integer majorization. Karamata's inequality, applied to \(f_q(t_i+1)\), now gives
\[
\log\Psi_q(P_n)\le\log\Psi_q(T)\le\log\Psi_q(K_{1,n-1}).
\]
Strict convexity gives equality only for the corresponding degree multiset. The unique tree with degrees \(n-1,1,\ldots,1\) is the star, and the unique tree with two degree-one vertices and all remaining degrees two is the path.

**Negative-contraction regime.** Suppose \(-1/3\le q<0\), and write \(q=-r\), so \(0<r\le1/3\). Relative to the common all-degree-one factor, define for positive integer \(t\)
\[
h_r(t)=\log\frac{1+(-r)^{t+1}}{1-r},
\qquad h_r(0)=0.
\]
Then
\[
\log\Psi_{-r}(T)=n\log\frac{1-r}{2}+\sum_{i:t_i>0}h_r(t_i).
\]
All \(h_r(t)\) are strictly positive, and
\[
h_r(2)\le h_r(t)\le h_r(1)
\qquad(t\ge1).
\]
Indeed, among the numerators \(1+(-r)^{t+1}\) for \(t\ge1\), the largest is \(1+r^2\) at \(t=1\), and the smallest is \(1-r^3\) at \(t=2\).

For the path, exactly \(n-2\) excess coordinates equal one. Any other tree has fewer than \(n-2\) positive excess coordinates; since each contributes at most \(h_r(1)>0\), its logarithmic fidelity is strictly smaller. Thus the path is the unique maximizer.

For the star, exactly one excess coordinate equals \(n-2\), so its excess contribution is \(h_r(n-2)\le h_r(1)\). Every nonstar tree has at least two positive excess coordinates and hence contributes at least \(2h_r(2)\). The inequality between these is strict because
\[
(1-r)(1+r+r^2)^2-(1+r^2)
=r(1+r)(1-r-r^3)>0
\]
for \(0<r\le1/3\). This is exactly the exponential inequality \(2h_r(2)>h_r(1)\). Hence every nonstar tree has strictly larger fidelity than the star, proving the reversed order and its equality cases.

The noise channel substitutions now give the complete depolarization phase diagram and the phase-damping order. The constant cases \(q=1\) and \(q=0\) follow by direct substitution in the product.

**Maximum-degree-three classification.** If every tree degree is in \(\{1,2,3\}\), let \(n_1,n_2,n_3\) denote the counts of these degrees. The tree degree sum implies \(n_1=n_3+2\), and hence with \(k=n_3\),
\[
(n_1,n_2,n_3)=(k+2,n-2-2k,k),
\qquad0\le k\le\left\lfloor\frac{n-2}{2}\right\rfloor.
\]
Every allowed \(k\) is realized by the Prüfer degree-sequence construction just noted. Substituting those degree counts into the source product yields the claimed closed form. Taking the quotient for consecutive \(k\) and expanding the numerator gives
\[
(1+q)(1+q^3)-(1+q^2)^2=q(1-q)^2.
\]
The quotient is greater than one for \(0<q<1\), less than one for \(-1/3\le q<0\), and equal to one for \(q=0\) or \(q=1\). This proves the exact branch-count extremizers.

## Verification
The proof establishes all tree sizes analytically and does not extrapolate from finite enumeration. The bundled standalone checker enumerates the Prüfer words of all labeled trees with \(4\le n\le7\) (\(18,244\) sequences), verifies the sharp path/star bounds and their strict equality cases for rational positive and negative \(q\), and checks the subcubic branch-count formula. Exact rational arithmetic is used throughout. The polynomial comparison for the negative regime and branch multiplier are also replayed at representative rational inputs. These finite calculations are corroborative and do not certify the infinite theorem independently.

## Relationship to prior work
Dutta's *Universal Z-only Correction for Distributing Arbitrary Graph States in Quantum Networks* establishes both resource-qubit fidelity products in its Theorems 15 and 16 and explicitly notes the degree dependence. Its Remark 17 calculates the \(n=4\) positive-noise star/path comparison, and Remark 20 interprets degree concentration in the range up to the completely depolarizing point. Those formulas and observations are prior ingredients, not new claims here. The source does **not** classify all tree extremizers at every physical depolarization rate, identify the reversal at \(p=3/4\), prove its strict equality cases, or give the degree-three exact branch-count phase classification. The maximum-degree-three condition originates in its separate native-embedding theorem, which is necessary rather than sufficient.

Tanizawa et al., *Fidelity-estimation method for graph states with depolarizing noise*, and Numajiri et al., *Phase Transitions and Noise Robustness of Quantum Graph States*, study Pauli noise acting on **data qubits of already prepared graph states**. Their corresponding stabilizer sums and partition-function analyses are not the same resource-qubit channel; Dutta's Remark 19 compares these models explicitly. Neither provides the claimed extremal theorem for the distribution resource registers.

The positive-contraction extremal step uses standard strict convexity and integer majorization. The new structural assertion is the exact all-physical-range phase boundary, including the negative-contraction reversal and the degree-three constrained family. The proof does not claim that majorization itself is novel.

## Limitations
These are idealized resource-register fidelities for different target trees, not measurements of real hardware performance. A larger predicted fidelity for a star in this model can coexist with a smaller **measured** fidelity than a path, because gate counts, native connectivity, and correlated errors contribute outside this model; the source explicitly reports such an experimental reversal. The degree-three result does not prove SWAP-free embeddability or optimize hardware placement. No analogous extrema are asserted for arbitrary graphs with cycles, other noise placements, or arbitrary non-Pauli correlated channels.

## References
1. S. Dutta, *Universal Z-only Correction for Distributing Arbitrary Graph States in Quantum Networks*, arXiv:2604.02169 (first public 2026-04-02; relevant full-text Theorems 15--16 and Remarks 17--20 in v7).
2. T. Tanizawa, Y. Takeuchi, S. Yamashika, R. Yoshii and S. Tsuchiya, *Fidelity-estimation method for graph states with depolarizing noise*, Physical Review Research 5, 043260 (2023), DOI 10.1103/PhysRevResearch.5.043260.
3. T. Numajiri, S. Yamashika, T. Tanizawa, R. Yoshii, Y. Takeuchi and S. Tsuchiya, *Phase Transitions and Noise Robustness of Quantum Graph States*, arXiv:2510.00548.
