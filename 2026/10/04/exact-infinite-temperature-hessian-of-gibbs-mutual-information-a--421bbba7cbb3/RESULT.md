# Exact infinite-temperature Hessian of Gibbs mutual information and a sharp boundary witness
## Finding
Let \(A\) and \(B\) be finite-dimensional quantum systems with dimensions \(d_A\) and \(d_B\), let \(d=d_A d_B\), and let \(H=H^\dagger\) act on \(A\otimes B\). Define the Gibbs state
\[
\rho_\beta=\frac{e^{-\beta H}}{\operatorname{Tr}(e^{-\beta H})}
\]
and the Hilbert--Schmidt interaction projection
\[
H_{\mathrm{int}}=H-\frac{\operatorname{Tr}_B H}{d_B}\otimes I_B-I_A\otimes\frac{\operatorname{Tr}_A H}{d_A}+\frac{\operatorname{Tr}H}{d}I_{AB}.
\]
Then, with natural logarithms,
\[
I(A:B)_{\rho_\beta}=\frac{\beta^2}{2d}\operatorname{Tr}(H_{\mathrm{int}}^2)+O(\beta^3)
\qquad(\beta\to0).
\]
Equivalently, the exact infinite-temperature Hessian is the squared normalized Hilbert--Schmidt norm of the component of \(H\) orthogonal to all one-sided Hamiltonians. In particular, the quadratic coefficient vanishes if and only if \(H\) is a sum of an \(A\)-only term, a \(B\)-only term, and a scalar; in that case \(\rho_\beta\) factorizes and the mutual information is identically zero for every \(\beta\).

For a qubit lattice written in the trace-orthogonal Pauli expansion \(H=\sum_P c_P P\), this becomes
\[
I(A:B)_{\rho_\beta}=\frac{\beta^2}{2}\sum_{P\,\mathrm{crosses}\,A|B}c_P^2+O(\beta^3),
\]
where a Pauli string crosses the cut when it is nonidentity on both sides. Thus the leading coefficient contains no bulk-only contribution.

The quadratic order and linear boundary scaling are simultaneously sharp. For \(m\) disjoint Ising bonds crossing the cut,
\[
H=-J\sum_{j=1}^{m} Z_j\otimes Z'_j,
\]
the Gibbs state is a product of bond states and exactly
\[
I(A:B)_{\rho_\beta}=m\bigl[x\tanh x-\log\cosh x\bigr],\qquad x=\beta J.
\]
Hence
\[
I(A:B)_{\rho_\beta}=\frac{mJ^2}{2}\beta^2+O(\beta^4),
\]
so neither the power \(\beta^2\) nor the linear dependence on the number of independent boundary bonds can be improved in general.

## Assumptions and scope
The theorem is finite-dimensional and concerns the von Neumann mutual information in nats. No locality assumption is needed for the Hessian formula. Locality enters only in interpreting \(H_{\mathrm{int}}\) as a boundary object: every Hamiltonian term supported wholly in \(A\) or wholly in \(B\) is annihilated by the interaction projection. The Pauli corollary uses the convention \(\operatorname{Tr}(PQ)=d\,\delta_{P,Q}\).

The result is asymptotic as \(\beta\to0\); it is not a uniform finite-temperature area-law bound and does not replace nonperturbative clustering arguments. The remainder is \(O(\beta^3)\) for each fixed finite-dimensional Hamiltonian. The Ising witness has an even expansion and therefore an \(O(\beta^4)\) remainder.

## Proof
Write
\[
h=H-\frac{\operatorname{Tr}H}{d}I_{AB}.
\]
A direct expansion of the normalized exponential gives
\[
\rho_\beta=\frac{I_{AB}}d-\frac{\beta}{d}h+O(\beta^2).
\]
For any traceless Hermitian \(X\) on an \(n\)-dimensional space,
\[
S\left(\frac{I_n}{n}+\varepsilon X+O(\varepsilon^2)\right)
=\log n-\frac{n\varepsilon^2}{2}\operatorname{Tr}(X^2)+O(\varepsilon^3).
\]
This is the second-order Taylor expansion of \(-\operatorname{Tr}(\rho\log\rho)\) at the maximally mixed state; the linear term vanishes on traceless directions.

Define the centered one-sided projections
\[
h_A=\frac{\operatorname{Tr}_B h}{d_B},\qquad
h_B=\frac{\operatorname{Tr}_A h}{d_A}.
\]
Taking partial traces of the Gibbs expansion yields
\[
\rho_{A,\beta}=\frac{I_A}{d_A}-\frac{\beta}{d_A}h_A+O(\beta^2),\qquad
\rho_{B,\beta}=\frac{I_B}{d_B}-\frac{\beta}{d_B}h_B+O(\beta^2).
\]
Applying the entropy expansion to the joint state and both marginals gives
\[
I(A:B)_{\rho_\beta}
=\frac{\beta^2}{2}\left[
\frac{\operatorname{Tr}(h^2)}d-
\frac{\operatorname{Tr}(h_A^2)}{d_A}-
\frac{\operatorname{Tr}(h_B^2)}{d_B}
\right]+O(\beta^3).
\]
Now decompose orthogonally in Hilbert--Schmidt inner product,
\[
h=h_A\otimes I_B+I_A\otimes h_B+H_{\mathrm{int}}.
\]
The three summands are pairwise orthogonal because \(h_A\), \(h_B\), and both partial traces of \(H_{\mathrm{int}}\) are traceless. Consequently,
\[
\frac{\operatorname{Tr}(h^2)}d
=\frac{\operatorname{Tr}(h_A^2)}{d_A}
+\frac{\operatorname{Tr}(h_B^2)}{d_B}
+\frac{\operatorname{Tr}(H_{\mathrm{int}}^2)}d,
\]
which proves the coefficient formula.

If \(H_{\mathrm{int}}=0\), then \(H=K_A\otimes I_B+I_A\otimes K_B+cI_{AB}\) for suitable Hermitian \(K_A,K_B\) and scalar \(c\). The two non-scalar summands commute, so the normalized exponential factorizes for every \(\beta\). Conversely, a nonzero \(H_{\mathrm{int}}\) has positive Hilbert--Schmidt norm and gives a strictly positive quadratic coefficient.

For qubits, the Pauli strings form an orthogonal basis. The interaction projection deletes exactly the strings that are identity on all of \(A\) or on all of \(B\), leaving precisely the strings nontrivial on both sides. Since \(\operatorname{Tr}(P^2)=d\), substitution gives the stated sum of squared crossing coefficients.

For the Ising witness, the \(m\) bond terms act on disjoint pairs and commute, so the Gibbs state factorizes across bonds. For one bond the two one-qubit marginals are maximally mixed, while the four joint probabilities are proportional to \(e^{xzz'}\). Its mutual information is therefore
\[
x\tanh x-\log\cosh x.
\]
Additivity of mutual information over tensor products gives the exact \(m\)-bond expression. Taylor expansion at \(x=0\) yields \(x^2/2+O(x^4)\).

## Verification
The bundled `verify.py` independently checks the algebraic projection identities, evaluates a deterministic noncommuting two-qubit Hamiltonian numerically and confirms convergence of \(I(A:B)_{\rho_\beta}/\beta^2\) to \(\operatorname{Tr}(H_{\mathrm{int}}^2)/(2d)\), checks the Pauli coefficient form, and verifies the exact Ising-bond expression and its quadratic limit. It prints `VERIFY_OK` on success.

These finite computations are consistency checks only. The theorem for arbitrary finite dimensions follows from the analytic entropy-Hessian argument above, not from numerical enumeration.

## Relationship to prior work
Yousefi and Rezakhani, arXiv:2609.32329, prove a nonperturbative high-temperature area law \(I(A:B)\leq \widetilde f(\beta)\beta^2|\partial_{AB}|\) below a clustering threshold. Their introduction explicitly notes that a perturbative expansion suggests an \(O(\beta^2)\) leading term but that higher coefficients can carry volume dependence; their proof therefore uses covariance identities and exponential clustering rather than extracting the exact perturbative coefficient. The formula above isolates that missing leading coefficient for every finite-dimensional bipartite Hamiltonian and shows directly that bulk-only Hamiltonian directions cancel at second order.

Earlier high-temperature mutual-information series, such as Singh, Hastings, Kallin, and Melko (2011), concern particular lattice models and critical scaling rather than a basis-free coefficient for an arbitrary finite-dimensional bipartite Hamiltonian. The harmonic/QFT high-temperature expansions of Katsinis and Pastras (2019--2020) are likewise model-specific and involve infinite-dimensional limits in which the infinite-temperature behavior can differ qualitatively.

The disjoint-bond family additionally supplies an exact witness that saturates the quadratic inverse-temperature order and linear boundary-size order asymptotically. Thus the recent nonperturbative \(\beta^2\) area-law scaling has a matching elementary sharpness mechanism at infinite temperature.

## Limitations
The coefficient is local in perturbative order, not a finite-temperature lower bound. A small or vanishing quadratic coefficient does not control higher-order behavior unless \(H_{\mathrm{int}}=0\), in which case exact factorization follows. For general local Hamiltonians, converting the coefficient into a uniform boundary-size bound still requires assumptions controlling the number, overlap, and normalization of interaction terms. No claim is made about thermodynamic-limit interchange with \(\beta\to0\), infinite-dimensional local Hilbert spaces, or optimal constants in the nonperturbative area law.

The originality assessment is limited by terminology: the entropy Hessian at the maximally mixed state is standard, and an equivalent interaction-projection formula may exist under different names. Targeted searches over Gibbs mutual information, high-temperature expansions, interaction projections, and Pauli crossing terms found no statement equivalent to the theorem-plus-sharpness witness, but absence from search is not a proof of uniqueness.

## References
1. A. Yousefi and A. T. Rezakhani, *Exact High-Temperature Quantum Area Law*, arXiv:2609.32329, first posted 2026-09-26.
2. R. R. P. Singh, M. B. Hastings, A. B. Kallin, and R. G. Melko, *Finite-Temperature Critical Behavior of Mutual Information*, Phys. Rev. Lett. 106, 135701 (2011), DOI 10.1103/PhysRevLett.106.135701; arXiv:1101.0430.
3. D. Katsinis and G. Pastras, *An Inverse Mass Expansion for the Mutual Information in Free Scalar QFT at Finite Temperature*, JHEP 02 (2020) 091, DOI 10.1007/JHEP02(2020)091; arXiv:1907.08508.
