# Exact character spectrum of reciprocal-trace square incidence over finite fields

## Finding
For an odd prime power \(q\), put \(H=(\mathbb F_q^\times)^2\), \(Q=H\cup\{0\}\), and \(h=(q-1)/2\). For each nonzero parameter \(a\) consider the reciprocal trace map \(f_a(x)=x+a/x\) on \(\mathbb F_q^\times\). Define the binary matrix \(B\), with rows indexed by \(a\in\mathbb F_q^\times\) and columns indexed by \(u\in Q\), by
\[
 B_{a,u}=\mathbf 1\{\exists x\in\mathbb F_q^\times,\ t\in\mathbb F_q:\ t^2=u,\ f_a(x)=t\}.
\]
For \(G=B^{\mathsf T}B\) and the quadratic character \(\chi\) extended by \(\chi(0)=0\), we prove the exact entries
\[
G_{u,u}=h,\qquad G_{u,v}=\frac{q-3+(1+\chi(-1))\chi(u-v)}4\quad(u\ne v).
\]
When \(q\equiv3\pmod4\), the complete Gram spectrum is
\[
\left\{\frac{q^2-1}{8}\ (\text{once}),\quad\frac{q+1}{4}\ (\text{multiplicity }h)\right\}.
\]
When \(q\equiv1\pmod4\), it consists of two exceptional values
\[
\lambda_\pm=\frac h4\bigl(h+2\pm\sqrt{h^2+4}\bigr),
\]
and, once for each nontrivial multiplicative character \(\psi:H\to\mathbb C^\times\), the value
\[
\lambda_\psi=\frac{h+1}2+\frac12\sum_{t\in H}\psi(t)\chi(1-t).
\]
For any extension \(\eta:\mathbb F_q^\times\to\mathbb C^\times\) of \(\psi\), setting \(J(\alpha,\beta)=\sum_{z\in\mathbb F_q}\alpha(z)\beta(1-z)\) with nontrivial characters zero at zero, the same eigenvalue is
\[
\lambda_\psi=\frac{h+1}2+\frac14\bigl(J(\eta,\chi)+J(\eta\chi,\chi)\bigr).
\]
All eigenvalues are strictly positive. Hence **every such reciprocal-trace incidence matrix has full column rank**, with the complete arithmetic spectrum as displayed.

## Assumptions and scope
The field is \(\mathbb F_q\) for any odd prime power \(q\ge3\); \(a,x\) are nonzero and \(u\) ranges through the zero-inclusive quadratic residues \(Q\). A square-root parameter is considered only up to sign; the image condition is independent of the selected root since \(f_a(-x)=-f_a(x)\). The matrix is real with entries zero or one. The output comprises the multiset of eigenvalues of the column Gram matrix, including repetitions even if distinct characters give the same number.

## Proof
**1. The discriminant reformulation.** For fixed \(a\ne0\), the equation \(x+a/x=t\) is equivalent to \(x^2-tx+a=0\). In odd characteristic it has a field root precisely when \(t^2-4a\in Q\); any root is automatically nonzero because \(a\ne0\). Since \(u=t^2\), this gives the exact indicator
\[
B_{a,u}=\mathbf1_Q(u-4a),\qquad
\mathbf1_Q(y)=\frac{1+\chi(y)+\delta_0(y)}2.
\]
Here \(\delta_0\) denotes the indicator of zero.

**2. The Gram identity.** The map \(a\mapsto 4a\) permutes the nonzero field elements. For \(u=v\in Q\), the unrestricted translation sum of \(\mathbf1_Q(u-z)\) is \(|Q|=h+1\), and omitting \(z=0\) removes one, leaving \(G_{u,u}=h\). For distinct \(u,v\in Q\), expand the product of the indicators and use
\[
\sum_{z\in\mathbb F_q}\chi(u-z)=0,\qquad
\sum_{z\in\mathbb F_q}\chi(u-z)\chi(v-z)=-1,
\]
together with \(\sum_z\delta_0(u-z)\chi(v-z)=\chi(v-u)\). The unrestricted convolution is \([q+1+(1+\chi(-1))\chi(u-v)]/4\). Because \(u,v\in Q\), deleting \(z=0\) subtracts one. This proves the claimed formula. The standard mixed-character identity equals \(-1\) because after \(z=u+(v-u)t\) the sum becomes \(\chi((v-u)^2)\sum_t\chi(t(t-1))=-1\), a quadratic polynomial with two distinct roots.

**3. The skew case.** If \(q\equiv3\pmod4\), then \(\chi(-1)=-1\), so the offdiagonal Gram value is the constant \((q-3)/4\). Thus
\[
G=\frac{q+1}{4}I+\frac{q-3}{4}J,
\]
acting on \(h+1=(q+1)/2\) columns. Its two eigenvalues and their multiplicities follow directly. They are positive even at \(q=3\).

**4. The symmetric case: the constant sector.** Assume \(q\equiv1\pmod4\), so \(\chi(-1)=1\) and \(h\) is even. Separate column zero from the \(h\) columns in \(H\). For \(u\ne0\), the zero-to-\(u\) entry is \(h/2\). For distinct \(u,v\in H\), setting \(t=v/u\),
\[
G_{u,v}=\frac{h-1}2+\frac12\chi(1-t).
\]
The classical quadratic Jacobi identity \(J(\chi,\chi)=-\chi(-1)=-1\) gives
\[
\sum_{t\in H}\chi(1-t)=\frac12\biggl(\sum_{t\ne0}\chi(1-t)+J(\chi,\chi)\biggr)=-1.
\]
Consequently every row in the \(H\)-by-\(H\) block has sum \(h^2/2\). On the orthonormal span of the zero coordinate and the constant unit vector on \(H\), the Gram operator is exactly
\[
\begin{pmatrix}h&h\sqrt h/2\\h\sqrt h/2&h^2/2\end{pmatrix}.
\]
Its characteristic polynomial has trace \(h(h+2)/2\) and determinant \(h^3/4\), yielding \(\lambda_\pm\) as stated.

**5. The nonconstant multiplicative sectors.** The \(H\)-block satisfies \(G_{u,v}=g(v/u)\), so a nontrivial character \(\psi\) of cyclic \(H\), extended by value zero in the separate column-zero coordinate, is an eigenvector. Since its sum on \(H\) vanishes, the eigenvalue is
\[
 h-\frac{h-1}2+\frac12\sum_{t\in H}\psi(t)\chi(1-t)=\lambda_\psi.
\]
An extension \(\eta\) of \(\psi\) to \(\mathbb F_q^\times\) exists because that group is cyclic and \(H\) has index two; its two extensions differ by \(\chi\). On nonzero elements, \(\mathbf1_H(t)\eta(t)=(\eta(t)+\eta\chi(t))/2\). Substituting into the character sum proves the Jacobi formula. These \(h-1\) character eigenvectors and the two-dimensional constant sector provide an orthogonal basis of all \(h+1\) columns.

**6. Positivity and rank.** Both \(\lambda_\pm\) are positive, since the constant-sector block has positive trace and determinant. For nontrivial \(\psi\), neither \(\eta\) nor \(\eta\chi\) nor their products with \(\chi\) is trivial. The classical Gauss-sum identity therefore gives \(|J(\eta,\chi)|=|J(\eta\chi,\chi)|=\sqrt q\). The character eigenvalue is real because \(\chi(1-t)=\chi(1-t^{-1})\) on \(H\). Hence
\[
\lambda_\psi\ge\frac{q+1}4-\frac{\sqrt q}2=\frac{(\sqrt q-1)^2}4>0.
\]
All Gram eigenvalues are positive, proving full column rank for every permitted \(q\). No numerical extrapolation enters the proof.

## Verification
Run \(\texttt{python3 verify.py}\) using Python's standard library. The independent routine first enumerates the actual images of \(x+a/x\), checks the discriminant reduction, constructs the binary incidence matrix, verifies every Gram entry, tests the constant-sector identities, and checks all multiplicative-character eigenvectors over sixteen explicitly constructed prime and prime-power fields. It returned:

```text
VERIFY_OK finite_fields= 16 individual_columns= 181 incidence_entries= 5112 square_character_spectra=validated
FIELDS 3,5,7,11,13,17,19,23,29,31,37,41,9,25,27,49
```
The computations are finite cross-checks; the proof applies to every odd prime power. The verifier does not claim to certify infinite ranges.

## Relationship to prior work
The reciprocal trace \(x+a/x\) is the classical Dickson-parametrization pattern; existing finite-field value-set and permutation-polynomial literature, including Shallue's 2012 survey, concerns individual maps or their polynomial descendants rather than the complete cross-parameter square-trace incidence spectrum. The Paley character matrix and its quadratic convolution are classical. Chandler–Sin–Xiang (2014) compute Smith and critical groups of the *full* Paley graph and use multiplicative characters and Jacobi sums; their eigenvalues, p-adic invariant factors, and character-action lemmas are acknowledged. The formula here instead diagonalizes a distinct **rectangular reciprocal-trace incidence matrix after restriction to the zero-inclusive square columns**, giving a two-parameter Gram kernel, both residue-class branches, and the exact square-restricted character spectrum. The unrestricted full-Paley spectrum does not determine principal-submatrix spectra. The novelty assessment is relative to inspected literature, not a proof of historical priority.

## Limitations
No result is claimed for even characteristic, arbitrary nonsquare-indexed columns, frequencies of individual trace values, or nonlinear perturbations of the reciprocal map. The formula provides Jacobi sums for nonconstant eigenvalues but does not evaluate every Jacobi sum in radicals. Earlier specialist literature on induced Paley subgraphs and classical Dickson value-set correlations may contain an equivalent result; one older plausible source (Chou–Gomez-Calderon–Mullen, 1988) was available only through its abstract, so absolute priority is unresolved. Independent mathematical validation has not been performed.

## References
- C. J. Shallue, *Permutation Polynomials of Finite Fields*, arXiv:1211.6044 (publicly posted 2012-11-23), especially Chapter 1. https://arxiv.org/abs/1211.6044
- D. B. Chandler, P. Sin, Q. Xiang, *The Smith and critical groups of Paley graphs*, arXiv:1401.8260 (first posted 2014-01-31), especially Sections 2–4. https://arxiv.org/abs/1401.8260
- A. Browne, R. Egan, P. Hegarty, P. Ó Catháin, *A Survey of the Hadamard Maximal Determinant Problem*, arXiv:2104.06756, Section 2.1. https://arxiv.org/abs/2104.06756
- W.-S. Chou, L. Gomez-Calderon, G. L. Mullen, *Value sets of Dickson polynomials over finite fields*, Journal of Number Theory (1988), DOI:10.1016/0022-314X(88)90006-6. Abstract available; full primary text not inspected.
