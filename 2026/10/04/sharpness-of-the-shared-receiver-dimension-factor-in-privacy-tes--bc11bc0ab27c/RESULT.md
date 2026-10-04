# Sharpness of the shared-receiver dimension factor in privacy-test overlap
## Finding
For every pair of positive integers \(M\) and \(d\), the upper bound
\[
\|PQ\|\le \min\{1,d/M\}
\]
for two decoded privacy-test projections sharing a receiver subsystem of dimension \(d\) is attained exactly. The construction uses only untwisted privacy tests, a one-dimensional sender shield, receiver systems \(X,Y\) of dimension \(M\), receiver shields of dimension \(d\), and basis-permutation unitary decoders. Consequently the factor \(d/M\) is not an artifact of the partial-trace estimate in the proof of the recent overlap lemma: neither its coefficient nor its linear dependence on the shared receiver dimension can be improved uniformly under the lemma's hypotheses.

## Assumptions and scope
Let \(K,K_1,K_2,X,Y\) have dimension \(M\), and let \(C,T_1,T_2\) have dimension \(d\). The sender shield is one-dimensional. Write
\[
|\Phi_M\rangle=M^{-1/2}\sum_{j=0}^{M-1}|j\rangle|j\rangle,
\]
and let the undecoded privacy test be the rank-one projection onto \(|\Phi_M\rangle\) on the two key registers, tensored with the identity on the receiver shield. Let \(D_1:X\otimes C\to K_1\otimes T_1\) and \(D_2:C\otimes Y\to K_2\otimes T_2\) be unitaries. The decoded projections \(P\) and \(Q\) act on \(K\otimes X\otimes C\otimes Y\), with the unused private receiver factor left invariant.

The claim concerns the operator overlap lemma itself. It does not assert that every channel or every communication code realizes this extremal geometry, nor does it improve the strong-converse exponent proved in the motivating paper.

## Proof
Set \(r=\min\{M,d\}\). Choose basis vectors \(|0\rangle_X\), \(|0\rangle_Y\), and \(|0\rangle_{T_i}\). Define partial actions of the two decoders by
\[
D_1\bigl(|0\rangle_X|j\rangle_C\bigr)=|j\rangle_{K_1}|0\rangle_{T_1},\qquad
D_2\bigl(|j\rangle_C|0\rangle_Y\bigr)=|j\rangle_{K_2}|0\rangle_{T_2}
\]
for \(0\le j<r\). These prescribed input and output basis vectors are pairwise distinct.

If \(d<M\), then for every \(d\le j<M\) choose a distinct basis vector \(|x_j\rangle_X|c_j\rangle_C\) with \(x_j\ne0\), and prescribe
\[
D_1\bigl(|x_j\rangle_X|c_j\rangle_C\bigr)=|j\rangle_{K_1}|0\rangle_{T_1}.
\]
There are enough such vectors because \((M-1)d\ge M-d\). Complete both partial maps arbitrarily to bijections of the remaining computational bases; this gives permutation unitaries. When \(d\ge M\), the first set of prescriptions already covers every output vector \(|j\rangle_{K_i}|0\rangle_{T_i}\) needed below, and again extends to a permutation unitary.

Consider the normalized range vectors
\[
|\psi\rangle=\frac1{\sqrt M}\sum_{j=0}^{M-1}|j\rangle_K\,D_1^\dagger\bigl(|j\rangle_{K_1}|0\rangle_{T_1}\bigr)\,|0\rangle_Y,
\]
\[
|\varphi\rangle=\frac1{\sqrt M}\sum_{j=0}^{M-1}|j\rangle_K\,|0\rangle_X\,D_2^\dagger\bigl(|j\rangle_{K_2}|0\rangle_{T_2}\bigr).
\]
By construction, \(|\psi\rangle\in\operatorname{ran}P\) and \(|\varphi\rangle\in\operatorname{ran}Q\). For \(j<r\), the corresponding receiver basis vector in both sums is exactly \(|0\rangle_X|j\rangle_C|0\rangle_Y\). If \(d<M\) and \(j\ge r=d\), the inverse image under \(D_1\) has an \(X\)-component orthogonal to \(|0\rangle_X\), so that term has zero inner product with the \(Q\)-range vector. Hence
\[
\langle\psi|\varphi\rangle=\frac rM=\min\{1,d/M\}.
\]
For orthogonal projections, any two unit vectors in their ranges give \(\|PQ\|\ge |\langle\psi|\varphi\rangle|\). The published privacy-test overlap lemma gives the reverse inequality \(\|PQ\|\le\min\{1,d/M\}\). Equality follows.

## Verification
The accompanying `verify.py` constructs the permutation decoders explicitly for representative regimes \(d<M\), \(d=M\), and \(d>M\). It builds orthonormal bases for the two decoded privacy-test ranges and checks both the designated witness inner product and the largest singular value of the range-overlap matrix. The replayed checks return `VERIFY_OK` for all included cases. These finite computations corroborate the construction; the proof above establishes the statement for all positive integers \(M,d\).

## Relationship to prior work
Wilde, arXiv:2609.32515v1, proves the general upper bound \(\|PQ\|\le\min\{1,d_C/M\}\) for decoded privacy tests with a shared receiver subsystem \(C\), independently of shield dimensions. Inspection of its overlap lemma and proof found the upper bound and the partial-trace mechanism producing the factor \(d_C\), but no equality family or sharpness statement. The present construction calibrates that new operator estimate exactly.

Kondra, Brinster, Kampermann, Bruß, and Wyderka, arXiv:2608.01308v1, prove an analogous Bell-target decoder-placement upper bound used by the later private-communication proof. The same permutation construction also attains its single-shared-factor bound. Wilde, Tomamichel, and Berta, arXiv:1602.08898v1, introduced privacy-test converse methods, but that work does not contain the shared-receiver decoder-placement estimate.

## Limitations
The result is a sharpness theorem for the local projection-overlap ingredient. It does not prove optimality of the complete strong-converse exponent, because later averaging, filtering, entropy, or channel-specific steps may introduce additional slack. The construction uses receiver shields of dimension \(d\); it does not classify equality cases under smaller shield constraints. An equivalent elementary projector construction could exist in older operator-algebra or tensor-network language that was not surfaced by the inspected searches.

## References
1. M. M. Wilde, *An exponential strong converse for private communication over degradable quantum channels*, arXiv:2609.32515v1 (2026).
2. T. V. Kondra, R. Brinster, H. Kampermann, D. Bruß, and N. Wyderka, *Sharp Quantum Capacity Thresholds: Exponential Strong Converses for Degradable and Antidegradable Channels*, arXiv:2608.01308v1 (2026).
3. M. M. Wilde, M. Tomamichel, and M. Berta, *Converse bounds for private communication over quantum channels*, arXiv:1602.08898v1 (2016).
