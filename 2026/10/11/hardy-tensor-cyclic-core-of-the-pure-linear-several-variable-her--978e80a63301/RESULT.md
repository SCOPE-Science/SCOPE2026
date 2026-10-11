# Hardy-tensor cyclic core of the pure linear several-variable Herglotz representation
## Finding
Let \(n\ge2\), \(b>0\), and \(j\in\{1,\ldots,n\}\). Consider the pure linear Herglotz--Nevanlinna function
\[
q(\boldsymbol z)=a+b z_j,
\]
with \(a\in\mathbb R\), in the explicit hyperplane model constructed by Avelin and Nedic. After deleting the zero summands, the ambient Hilbert space is
\[
\mathcal H_j=L^2\!\left(\mathbb R^{n-1},b\pi^{-(n-1)}\,d\boldsymbol s\right).
\]
For the reproducing-kernel vectors from their Theorem 6.3, the nonzero component is
\[
h_{\boldsymbol z}(\boldsymbol s)=\prod_{k\ne j}(s_k-\overline{z_k})^{-1},
\qquad \boldsymbol z\in\mathbb C_+^n.
\]
Then
\[
\overline{\operatorname{span}}\{h_{\boldsymbol z}:\boldsymbol z\in\mathbb C_+^n\}
=
\widehat{\bigotimes}_{k\ne j}H^2(\mathbb C_+)_{\partial}.
\]
This subspace is proper and has infinite codimension in \(\mathcal H_j\). Consequently, for every \(n\ge2\), the canonical ambient hyperplane realization of a nonzero pure linear term is not vector-cyclic: its exact vector-cyclic core is the product Hardy boundary space.

## Assumptions and scope
The Nevanlinna measure is zero, one coefficient \(b_j=b\) is positive, and all other linear coefficients vanish. Multiplying Lebesgue measure by \(b\pi^{-(n-1)}\) only rescales the Hilbert norm and does not change closed spans.

“Vector-cyclic core” means only the closed linear span of the representing kernel vectors. No assertion is made that the self-adjoint linear relations reduce this Hardy subspace. Thus the finding does not solve the stronger minimal-self-adjoint-relation realization problem posed by the source.

## Proof
In the source's pure-linear Case 3, the surviving hyperplane is \(R_j=\boldsymbol e_j^\perp\cong\mathbb R^{n-1}\) and the representing vector has component
\[
(v_{\boldsymbol w})_j(\boldsymbol s)=\prod_{k\ne j}(s_k-w_k)^{-1}.
\]
In the reproducing-kernel formulation of Theorem 6.3, the corresponding vector is
\[
h_{\boldsymbol z}(\boldsymbol s)=\prod_{k\ne j}(s_k-\overline{z_k})^{-1};
\]
the factor involving the supported \(j\)-coordinate cancels.

Identify
\[
L^2(\mathbb R^{n-1})\cong\widehat{\bigotimes}_{k\ne j}L^2(\mathbb R).
\]
For one variable, the boundary Hardy space \(H^2(\mathbb C_+)_{\partial}\) is the closed span in \(L^2(\mathbb R)\) of the Cauchy reproducing kernels
\[
k_z(t)=(t-\overline z)^{-1},\qquad z\in\mathbb C_+.
\]
Hence finite products of these kernels are dense in the Hilbert tensor product of the \(n-1\) Hardy factors. Those products are exactly the vectors \(h_{\boldsymbol z}\), proving the closed-span identity.

The standard Paley--Wiener/Hardy decomposition of \(L^2(\mathbb R)\) gives a nonzero infinite-dimensional opposite-Hardy orthogonal complement to \(H^2(\mathbb C_+)_{\partial}\). Tensoring one such orthogonal vector with arbitrary vectors in the remaining coordinates shows that the product Hardy subspace is proper and has infinite codimension. For \(n=2\), the opposite Hardy space itself is already an infinite-dimensional orthogonal complement.

## Verification
The focal source was inspected at the primary MSC statement, the pure-linear Case 3 construction, the hyperplane Hilbert space, the formula for \(v_{\boldsymbol w}\), Theorem 6.3, and the final discussion. The source explicitly notes density when resolvent parameters range over all of \(\mathbb C\setminus\mathbb R\), says an analogous extension is desirable, and separately asks whether the representation is minimal in a suitable sense.

The external analytic input is classical: Cauchy reproducing kernels span \(H^2(\mathbb C_+)\) densely, and dense factor sets have dense algebraic tensor product in the Hilbert tensor product. No finite computation is used as an infinite proof.

## Relationship to prior work
Avelin--Nedic provide the exact ambient hyperplane model and identify the associated RKHS with the closed span of their representing vectors, but they do not identify that span in the pure-linear case. The present statement identifies the upper-half-plane span exactly and shows that the ambient hyperplane \(L^2\)-space contains an infinite-dimensional orthogonal sector invisible to the representing vectors.

Oliva-Maza's half-plane Hardy-kernel work supplies the one-variable RKHS ingredient but does not concern the several-variable Herglotz--Nevanlinna linear-relation model. Nedic's earlier positive-semidefinite-function representation identifies the several-variable linear coefficients but predates and does not imply the cyclic-subspace statement for the 2026 construction.

## Limitations
This is an exact statement about the vector-generated subspace in the explicit pure-linear one-coordinate model. It does not prove that compressing the self-adjoint linear relations to the product Hardy space yields a self-adjoint representation, does not classify minimal relation realizations, and does not treat the coupled span when several linear coefficients or a nonzero Nevanlinna measure are present.

## References
1. E. Avelin and M. Nedic, *Operator representations of Herglotz-Nevanlinna functions in several variables*, arXiv:2610.04637v1, 3 October 2026.
2. J. Oliva-Maza, *On Hardy kernels as reproducing kernels*, Canadian Mathematical Bulletin 66 (2023), 428--442, DOI 10.4153/S0008439522000406.
3. M. Nedic, *Characterizations of Herglotz--Nevanlinna Functions Using Positive Semi-Definite Functions and the Nevanlinna Kernel in Several Variables*, Complex Analysis and Operator Theory 15 (2021), article 109, DOI 10.1007/s11785-021-01155-x.
