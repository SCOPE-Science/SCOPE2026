# Fiberwise density of \(\beta_0(H)\) along fixed polar factors
## Finding
Let \(H\) be an infinite-dimensional separable complex Hilbert space. Write \(\beta(H)\) for the bounded operators whose restrictions to every nonzero reducing subspace attain their norm, and
\[
\beta_0(H)=\{T\in\mathcal B(H): |T|\in\beta(H)\}.
\]
For every \(T\in\mathcal B(H)\) and every \(\varepsilon>0\), if \(T=U|T|\) is the polar decomposition, there is \(S\in\beta_0(H)\) satisfying
\[
\|S-T\|<\varepsilon,\qquad \|S\|=\|T\|,\qquad N(S)=N(T),
\]
such that \(S=U|S|\) is the polar decomposition with the same partial isometry \(U\), and \(|S|\) is a positive finite-spectrum operator in \(W^*(|T|)\). In particular, the finite-spectrum-modulus part of \(\beta_0(H)\) is norm dense in \(\mathcal B(H)\), and the approximation may be performed inside the polar fiber of the target operator.

## Assumptions and scope
The Hilbert space is the infinite-dimensional separable complex Hilbert space used in the focal source. The polar decomposition convention is the unique \(T=U|T|\) with \(N(U)=N(T)\). The assertion concerns operator-norm approximation. It does not claim that the perturbation \(S-T\) is compact or finite rank.

## Proof
If \(T=0\), take \(S=0\). Assume \(T\ne0\), put \(M=\|T\|\), and let \(H_0=N(T)^\perp\). On \(H_0\), set \(A=|T||_{H_0}\). Then \(A\ge0\), \(N(A)=\{0\}\), \(\|A\|=M\), and the spectral projection of \(A\) at \(0\) is zero.

Choose a finite Borel partition \(\Delta_1,\ldots,\Delta_m\) of \(\sigma(A)\setminus\{0\}\) such that each cell has diameter less than \(\varepsilon\). Choose positive representatives \(a_j\in\Delta_j\), arranging that the cell containing \(M\) has representative \(M\). Define
\[
A_\varepsilon=\sum_{j=1}^m a_j E_A(\Delta_j).
\]
Because \(E_A(\{0\})=0\), the projections in this sum add to \(I_{H_0}\). Hence \(A_\varepsilon\) is positive, has finite spectrum, is bounded below by \(\min_j a_j>0\), and therefore has zero kernel. The chosen top representative gives \(\|A_\varepsilon\|=M\). Spectral calculus gives
\[
\|A-A_\varepsilon\|<\varepsilon.
\]
Moreover, \(A_\varepsilon\) is a bounded Borel function of \(A\).

With respect to \(H=N(T)\oplus H_0\), set \(B=0\oplus A_\varepsilon\) and \(S=UB\). Then \(B\ge0\), \(B\in W^*(|T|)\), \(N(B)=N(T)\), and \(\|B\|=M\). Since \(U^*U=P_{H_0}\) and the support projection of \(B\) is \(P_{H_0}\),
\[
S^*S=BU^*UB=B^2,
\]
so \(|S|=B\). The equality of support projections also shows that \(S=U|S|\) is the polar decomposition, not merely a factorization. Consequently \(N(S)=N(B)=N(T)\) and \(\|S\|=\|B\|=\|T\|\).

The focal source proves that every self-adjoint finite-spectrum operator belongs to \(\beta(H)\). Therefore \(|S|=B\in\beta(H)\), and the definition of \(\beta_0(H)\) gives \(S\in\beta_0(H)\). Finally, \(B-|T|\) has range in \(H_0\), where \(U\) is isometric, hence
\[
\|S-T\|=\|U(B-|T|)\|=\|B-|T|\|=\|A_\varepsilon-A\|<\varepsilon.
\]
This proves all asserted properties.

## Verification
The proof uses the spectral theorem and the polar decomposition only. The critical support check is \(E_A(\{0\})=0\) on \(H_0\), which permits the cell adjacent to zero to receive a strictly positive representative without changing the kernel. Choosing \(M\) as the representative of the top spectral cell preserves the norm exactly. Positivity and kernel preservation make the original partial isometry \(U\) the actual polar factor of \(S\). No finite experiment or numerical approximation is used as proof.

## Relationship to prior work
Su and Zhang define \(\beta_0(H)\) and prove density of the larger class \(\beta(H)\). Their Section 8 approximates the modulus by a finite-spectrum self-adjoint operator and consequently constructs an approximant whose modulus has finite spectrum. Thus their proof already implies the unstructured corollary that \(\beta_0(H)\) is dense. The present finding is the stronger fiberwise statement: the finite-spectrum approximation is chosen positive and support preserving, with the top spectral value fixed, so that the polar partial isometry, kernel, and operator norm are all preserved simultaneously.

Ramesh and Osaka introduced and developed the reducing-subspace norm-attainment class and its spectral structure. The located statements from that earlier literature concern structure and spectral properties rather than this polar-fiber approximation theorem.

## Limitations
The construction uses bounded Borel spectral calculus and does not assert that \(|S|\) lies in the norm-continuous functional calculus \(C^*(|T|)\). The perturbation need not be compact or finite rank. The result preserves the polar partial isometry, kernel, and norm, but it does not preserve finer spectral multiplicities or the range itself.

## References
[1] Z. Su and Y. Zhang, *The Stability and Density of Norm Attaining Operators on Reducing Subspaces*, arXiv:2609.37621v1, 2026; v2 inspected for Section 8 and the corrected definition of \(\beta_0(H)\).

[2] G. Ramesh and H. Osaka, *On a subclass of norm attaining operators*, Acta Sci. Math. (Szeged) 87 (2021), DOI 10.14232/actasm-020-426-9.

[3] G. Ramesh and H. Osaka, *On operators which attain their norm on every reducing subspace*, Ann. Funct. Anal. 13 (2022), DOI 10.1007/s43034-022-00167-8.
