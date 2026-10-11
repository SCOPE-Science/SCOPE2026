# Truncation ranks recover the equivariant Floer torsion profile
## Finding
Let \(L\subset S^3\) be a based link with \(c\) components. Put
\[
R=\mathbb F_2[[q]],
\]
and let \(M(L)=\widehat{HF}_{\mathbb Z/2}(\Sigma(L),p)\) denote its equivariant Heegaard Floer homology over \(R\), with all gradings forgotten. The localization theorem for the branched-cover construction fixes the free rank at \(2^{c-1}\), so the structure theorem over the discrete valuation ring \(R\) gives
\[
M(L)\cong R^{2^{c-1}}\oplus\bigoplus_{j=1}^s R/(q^{a_j}),
\qquad a_j\ge1.
\]

Huang introduced, for every integer \(N\ge1\), the truncated theory with coefficients \(\mathbb F_2[q]/(q^N)\). Define its total dimension by
\[
h_N(L)=\dim_{\mathbb F_2}\widehat{HF}_{\mathbb Z/2}(\Sigma(L),p;\mathbb F_2[q]/(q^N)),
\qquad h_0(L)=0.
\]
Then
\[
h_N(L)=2^{c-1}N+2\sum_{j=1}^s\min(N,a_j).
\]
Equivalently, for \(\delta_N=h_N-h_{N-1}\),
\[
\delta_N=2^{c-1}+2\#\{j:a_j\ge N\}.
\]
Hence the increments are nonincreasing, congruent to \(2^{c-1}\) modulo \(2\), and eventually equal to \(2^{c-1}\). Their drops recover each torsion multiplicity exactly:
\[
\#\{j:a_j=N\}=\frac{\delta_N-\delta_{N+1}}2.
\]
Thus the single numerical sequence \(h_1,h_2,\ldots\) determines the complete ungraded \(R\)-module isomorphism type of \(M(L)\). In particular, for a knot every \(\delta_N\) is a positive odd integer and eventually equals \(1\).

## Assumptions and scope
The statement concerns the Borel equivariant Heegaard Floer complex used for double branched covers, with formal-power-series coefficient ring \(R=\mathbb F_2[[q]]\), exactly as in Huang's setup. Dimensions are total dimensions after forgetting the available gradings. No claim is made that the sequence recovers grading locations of the torsion summands, extension data in a richer category, or chain-level information.

The link is based because the branched-cover equivariant theory in the cited construction is an invariant of a pointed link. The number \(c\) denotes the number of link components.

## Proof
Let \(C=P(\widehat{CF}(\Sigma(L),p))\). Huang's Definition 1.1 and discussion of the branched-cover complex identify \(C\) as a finite-rank free \(R\)-complex, and Theorem 1.4 identifies the coefficient-
\(\mathbb F_2[q]/(q^N)\) theory with the homology of
\[
C\otimes_R R/(q^N).
\]
Since \(R\) is a discrete valuation ring, the finitely generated module \(H(C)\), with gradings forgotten, decomposes as
\[
R^r\oplus\bigoplus_{j=1}^sR/(q^{a_j}).
\]
Localization of the equivariant branched-cover theory identifies the generic rank with the dimension of
\[
(\mathbb F_2\oplus\mathbb F_2)^{\otimes(c-1)},
\]
so \(r=2^{c-1}\).

Apply the universal coefficient theorem to the free \(R\)-complex \(C\) and the module \(A_N=R/(q^N)\). After summing dimensions over the homological gradings, each free summand of \(H(C)\) contributes \(N\). A torsion summand \(R/(q^a)\) contributes
\[
\dim_{\mathbb F_2}(R/(q^a)\otimes_R A_N)=\min(a,N)
\]
from the tensor term and
\[
\dim_{\mathbb F_2}\operatorname{Tor}_1^R(R/(q^a),A_N)=\min(a,N)
\]
from the adjacent universal-coefficient term. Therefore
\[
h_N=rN+2\sum_j\min(N,a_j),
\]
which is the first formula.

Taking first differences gives
\[
\delta_N=r+2\sum_j\bigl(\min(N,a_j)-\min(N-1,a_j)\bigr)
=r+2\#\{j:a_j\ge N\}.
\]
The tail counts are nonincreasing and eventually zero. Taking one more difference gives
\[
\delta_N-\delta_{N+1}=2\#\{j:a_j=N\},
\]
which reconstructs the full multiset of exponents. The eventual value of \(\delta_N\) also recovers \(r\), so the entire ungraded module type is encoded by the truncation dimensions alone.

## Verification
The proof is algebraic rather than experimental. The critical checks are: \(R=\mathbb F_2[[q]]\) is a discrete valuation ring; Huang's truncated invariant is the homology after chain-level tensoring with \(R/(q^N)\); and the localization theorem fixes the free rank at \(2^{c-1}\). For a cyclic torsion summand, both the tensor and first-Tor dimensions are \(\min(a,N)\), which explains the factor of \(2\).

As internal consistency checks, the formula at large \(N\) has slope equal to the localization rank, while every second difference satisfies
\[
h_{N+1}-2h_N+h_{N-1}=-2\#\{j:a_j=N\}\le0.
\]
Thus any computed truncation table violating discrete concavity, the parity rule for first differences, or eventual slope \(2^{c-1}\) cannot arise from the stated equivariant theory.

## Relationship to prior work
Huang proves that for every \(N\ge1\) there is a spectral sequence from reduced Khovanov homology tensored with \(\mathbb F_2[q]/(q^N)\) to the truncated equivariant Heegaard Floer group. The inspected paper does not discuss torsion exponents, dimensions as a function of \(N\), discrete concavity, or reconstruction of the full ungraded module from those dimensions.

Hendricks--Lipshitz--Sarkar supply the equivariant branched-cover theory and its localization behavior; Seidel--Smith give the general localization framework and related free-versus-torsion rank constraints. Those sources motivate the module decomposition but do not state the all-truncation reconstruction formula above. Targeted searches for truncation-rank, torsion-exponent, universal-coefficient, and rank-increment formulations found no statement implying this result.

## Limitations
Only the ungraded \(R\)-module is recovered. Two equivariant Floer groups with the same ungraded cyclic decomposition but different gradings have the same sequence \(h_N\). The result is conditional on the standard finite-generation and localization properties of the cited equivariant branched-cover theory and does not identify the exponents for any particular link without additional computation.

The principal originality risk is that the universal-coefficient reconstruction may be regarded as implicit folklore once all truncations are considered. The inspected primary sources contain closely related module-theoretic ingredients but not the stated tomography or its exact finite-difference formulas.

## References
J. Huang, *Exact triangle and spectral sequence of the equivariant Floer homology of double branched covers*, arXiv:2609.38117v1, 2026. Definition 1.1 and Theorem 1.4 give the formal-power-series Borel complex and every truncated coefficient theory.

K. Hendricks, R. Lipshitz, and S. Sarkar, *A flexible construction of equivariant Floer homology and applications*, arXiv:1510.02449, Journal of Topology 9 (2016), 1153--1236. The branched-cover equivariant theory and localization spectral sequence determine the generic rank used here.

P. Seidel and I. Smith, *Localization for involutions in Floer cohomology*, arXiv:1002.2648, Geometric and Functional Analysis 20 (2010), 1464--1501. The general Borel-localization framework includes free-versus-torsion rank constraints.
