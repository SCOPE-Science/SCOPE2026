# Support-aware correction sharpens the \(\{2,2,d\}\) mixed-dimensional Hamming example
## Finding
Consider a quantum error-correcting code on
\[
\mathcal H=\mathbb C^2\otimes\mathbb C^2\otimes\mathbb C^d,\qquad d\ge 5,
\]
with code dimension \(K\) and dimensional minimum distance \(D=5\). The source defines the dimensional weight of an error as the product of the local dimensions in its support and uses the sufficient estimate
\[
w_{\dim}(E_a^\dagger E_b)\le w_{\dim}(E_a)w_{\dim}(E_b)
\]
to conclude that \(T^2<D\) guarantees correction of all errors of dimensional weight at most \(T\).

For this particular architecture, however, the largest guaranteed threshold is at least \(T=4\), not merely \(T=2\). Every error with dimensional weight at most \(4\) acts only on the two-qubit block, so pairwise products of such errors remain supported on that same block and have dimensional weight at most \(4<5\). Hence the distance-\(5\) Knill--Laflamme conditions correct the entire two-qubit operator algebra.

For a code that is non-degenerate with respect to this correctable set, there are exactly
\[
1+2(2^2-1)+(2^2-1)^2=1+6+9=16
\]
basis errors supported inside the two-qubit block. Their error spaces are mutually orthogonal, so
\[
16K\le 4d,
\qquad\text{and therefore}\qquad
K\le \left\lfloor\frac d4\right\rfloor.
\]
This replaces the example's weaker count \(1+6=7\) and bound \(K\le\lfloor 4d/7\rfloor\).

The same source later compares that weaker Hamming ceiling with its pure-code Singleton bound \(K\le\lfloor d/4\rfloor\) and uses the gap to argue that an Hamming-bound-saturating code in this example would be forced to be impure. With the full guaranteed two-qubit error set counted, the non-degenerate Hamming upper bound is instead the same numerical ceiling \(\lfloor d/4\rfloor\). Thus that example-specific forced-impurity inference does not follow from the two bounds alone.

## Assumptions and scope
The local dimensions are exactly \(2,2,d\) with \(d\ge5\). Dimensional weight is
\[
w_{\dim}(E)=\prod_{i\in\operatorname{supp}(E)}D_i,
\]
with the empty support assigned weight \(1\). Dimensional minimum distance \(D=5\) means the Knill--Laflamme detection condition holds for every error-basis element of dimensional weight strictly below \(5\).

The Hamming count assumes non-degeneracy with respect to the full correctable set of operators supported on the two-qubit block, in the same geometric sense used by the source: distinct basis errors map the code space into mutually orthogonal \(K\)-dimensional subspaces.

## Proof
Let \(A\) denote the two-qubit subsystem. Its physical dimension is
\[
\dim A=2\cdot2=4.
\]
Because the remaining subsystem has local dimension \(d\ge5\), any support that contains the qudit has dimensional weight at least \(5\). Therefore an error has dimensional weight at most \(4\) if and only if its support is contained in \(A\).

Take any two error-basis elements \(E_a,E_b\) with dimensional weight at most \(4\). Both act trivially outside \(A\). Their product \(E_a^\dagger E_b\) also acts trivially outside \(A\); cancellations can only shrink its support. Hence
\[
w_{\dim}(E_a^\dagger E_b)\le\dim A=4<5=D.
\]
By the definition of dimensional minimum distance, every such product is detectable. The Knill--Laflamme correction criterion therefore holds for the full set of errors supported on \(A\). This proves correction of all errors with dimensional weight at most \(4\).

For the volume bound, an orthogonal local error basis on one qubit has \(4\) elements: one identity and \(3\) nonidentity elements. Tensoring the two qubit bases gives \(4^2=16\) operators on \(A\). Equivalently the exact-support count is \(1+6+9=16\). Under non-degeneracy, these produce \(16\) mutually orthogonal images of a \(K\)-dimensional code subspace in an ambient space of dimension \(4d\). Thus
\[
16K\le4d,
\]
which yields
\[
K\le\left\lfloor\frac d4\right\rfloor.
\]

## Verification
The argument is analytic and holds for every integer \(d\ge5\); no finite enumeration is used to infer the infinite statement. The key closure check is support-theoretic: the product of two operators supported inside the fixed two-qubit subsystem is again supported there. The count \(16=4^2\) is the dimension of the full operator basis on a \(4\)-dimensional subsystem.

A small standalone checker is included as `artifacts/verify.py`. It verifies the support classification and error-count arithmetic for any supplied integer \(d\ge5\). Its output is corroborative; the proof above establishes the all-\(d\) statement.

## Relationship to prior work
The current source states the general sufficient criterion \(T^2<D\), then in its \(\{2,2,d\}\), \(D=5\) example treats \(T=2\) as the maximum correctable threshold, counts only the identity and the six one-qubit nonidentity errors, and obtains \(K\le\lfloor4d/7\rfloor\).

Earlier mixed-dimensional work by Ball and Zhang states the stronger support-aware principle needed here: when the support is known and has physical dimension below the dimensional distance, errors supported there can be corrected. Applying the Knill--Laflamme condition directly to the two-qubit block gives the same conclusion independently.

Searches of the source identifier, the phrases “dimensional weight correction radius”, “support union”, “two qubits one qudit \(D=5\)”, and the claimed \(T^2<D\) threshold found no prior source-specific correction establishing the \(16K\le4d\) bound or the resulting collapse of the example's Hamming-versus-pure-Singleton gap.

## Limitations
The finding does not invalidate the mixed-dimensional MacWilliams identity, the general Singleton bounds, or Theorem 21 as a sufficient statement under its explicit hypothesis \(T^2<D\). It shows that the paper's use of that sufficient condition as a maximum threshold in the particular \(\{2,2,d\}\), \(D=5\) example is too restrictive.

No code construction is supplied, and the bound \(K\le\lfloor d/4\rfloor\) is not asserted to be attainable. The conclusion about impurity is correspondingly limited: the example's two displayed upper bounds no longer force impurity by a strict numerical gap.

## References
1. D. González-Lociga and S. Ball, “Mixed-dimensional quantum MacWilliams identity: Bounds for codes and absolutely maximally entangled states in heterogeneous systems,” arXiv:2604.25790v2; *Physical Review A* **114**, 022464 (2026), DOI:10.1103/fyq2-mpmm.
2. S. Ball and R. Zhang, “Error-correcting codes and absolutely maximally entangled states for mixed-dimensional Hilbert spaces,” arXiv:2510.17231v2; *Physical Review A* **113**, 012432 (2026), DOI:10.1103/yqck-92fb.
3. E. Knill and R. Laflamme, “Theory of quantum error-correcting codes,” *Physical Review A* **55**, 900–911 (1997).
