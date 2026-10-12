# Trace fibers of invertible matrix centralizers over every finite field

## Finding

Let \(q=p^e\) be a prime power and let \(A\in M_n(\mathbb F_q)\), where \(n\ge1\). Let \(T_A(b)\) count the matrices \(X\in\mathrm{GL}_n(\mathbb F_q)\) such that \(AX=XA\) and \(\operatorname{tr}X=b\).

For each monic irreducible \(f\) occurring in the rational canonical form of \(A\), write \(m_{f,s}\) for the multiplicity of its elementary divisor \(f^s\), and put \(d_f=\deg f\), \(Q_f=q^{d_f}\). Let \(I\) be the finite set of pairs \((f,s)\) with \(m_{f,s}>0\). Define
\[
D=\sum_f d_f\sum_{s,t\ge1}m_{f,s}m_{f,t}\min(s,t),\qquad
r=D-\sum_{(f,s)\in I}d_fm_{f,s}^2,
\]
\[
G=q^r\prod_{(f,s)\in I}|\mathrm{GL}_{m_{f,s}}(\mathbb F_{Q_f})|.
\]
Here \(|\mathrm{GL}_m(\mathbb F_Q)|=\prod_{j=0}^{m-1}(Q^m-Q^j)\). The number \(G\) equals the order of the invertible centralizer of \(A\).

If \(p\mid s\) for every \((f,s)\in I\), then
\[
T_A(0)=G,\qquad T_A(b)=0\quad(b\ne0).
\]
Otherwise define the signed integer
\[
B=q^r
\prod_{\substack{(f,s)\in I\\p\nmid s}}
(-1)^{m_{f,s}}Q_f^{\binom{m_{f,s}}2}
\prod_{\substack{(f,s)\in I\\p\mid s}}
|\mathrm{GL}_{m_{f,s}}(\mathbb F_{Q_f})|.
\]
Then the **complete trace-fiber distribution** is
\[
\boxed{\ T_A(0)=\frac{G+(q-1)B}{q},\qquad
T_A(b)=\frac{G-B}{q}\quad\text{for every }b\in\mathbb F_q^\times.\ }
\]
In particular, all nonzero trace fibers are equal, and their difference from the zero-trace fiber is exactly \(B\). The signed bias is determined by the elementary-divisor data and the divisibility of block lengths by the characteristic. No assumption of diagonalizability, distinct elementary divisors, or odd characteristic is needed.

## Assumptions and scope

All matrices and their traces are over \(\mathbb F_q\). The index \(s\) always ranges over positive integers, and absent elementary divisors have multiplicity zero. The polynomial \(f\) ranges over **distinct monic irreducibles**, not merely their degrees; thus different irreducibles of equal degree contribute separate factors. The ring \(\mathbb F_q[t]\) acts on \(V=\mathbb F_q^n\) by \(t\cdot v=Av\). Write \(\mathcal C(A)=\operatorname{End}_{\mathbb F_q[t]}(V)\). Its unit group is the invertible centralizer of \(A\).

These are exact counts for each individual \(A\) in every finite dimension. They are not asymptotic estimates and do not assert that the nonzero fibers are necessarily nonempty (for a small field they can vanish). The case of \(n=0\) is excluded.

## Proof

**1. Endomorphism dimension and semisimple quotient.** The rational canonical decomposition gives
\[
V\cong\bigoplus_f\bigoplus_{s\ge1}
\big(\mathbb F_q[t]/(f^s)\big)^{m_{f,s}}.
\]
Maps between modules with distinct irreducible factors vanish. For a fixed \(f\), a homomorphism from a cyclic \(f^s\)-module into an \(f^t\)-module is determined by an element killed by \(f^s\), so its \(\mathbb F_q\)-dimension is \(d_f\min(s,t)\). It follows that \(\dim_{\mathbb F_q}\mathcal C(A)=D\).

The finite-dimensional algebra \(\mathcal C(A)\) has a canonical semisimple quotient
\[
\mathcal C(A)/J(\mathcal C(A))\cong
\prod_{(f,s)\in I}M_{m_{f,s}}(\mathbb F_{Q_f}).
\]
To see this concretely, take each diagonal block of endomorphisms among cyclic summands of **the same** length \(s\), and reduce its entries modulo \(f\). The maps between unequal lengths give zero in this quotient: their two-way compositions on a length-\(s\) cyclic module are divisible by \(f\) whenever the other length differs. This defines a surjective algebra homomorphism onto the indicated product, and its kernel is nilpotent (all simple cyclic-type heads have been removed), hence the Jacobson radical. The same fact follows from the Krull–Schmidt decomposition of a finite-length module and the local endomorphism rings of its indecomposable summands. The kernel therefore has dimension \(r\).

In a finite-dimensional algebra an element is invertible if and only if its image in the quotient by the Jacobson radical is invertible. Each tuple of invertible residue matrices has exactly \(q^r\) lifts; hence the group order is \(G\).

**2. The trace survives only through the quotient.** Denote the quotient coordinate of \(X\in\mathcal C(A)\) at \((f,s)\) by \(U_{f,s}\in M_{m_{f,s}}(\mathbb F_{Q_f})\). Off-diagonal maps between cyclic summands contribute no ordinary matrix trace. On the sum of length-\(s\) cyclic modules, each diagonal endomorphism preserves the \(f\)-adic filtration. Every one of its \(s\) successive quotients is a vector space over \(\mathbb F_{Q_f}\) and is acted on by \(U_{f,s}\). Additivity of trace across a preserved filtration gives the exact identity
\[
\operatorname{tr}_{\mathbb F_q}(X)
=\sum_{(f,s)\in I}s\,
\operatorname{Tr}_{\mathbb F_{Q_f}/\mathbb F_q}
\!\left(\operatorname{tr}_{\mathbb F_{Q_f}}U_{f,s}\right).
\tag{1}
\]
In particular, all contributions with \(p\mid s\) vanish. If every length is divisible by \(p\), (1) proves the first case of the theorem directly.

**3. A matrix-group additive-character identity.** Let \(K\) be any finite field with \(Q\) elements and let \(\theta:K\to\mathbb C^\times\) be any nontrivial additive character. For every positive integer \(m\),
\[
\sum_{U\in\mathrm{GL}_m(K)}\theta(\operatorname{tr}U)
=(-1)^m Q^{\binom m2}.
\tag{2}
\]
For completeness, let \(W=K^m\). The Möbius function of the subspace lattice from zero to a subspace \(L\) of dimension \(j\) is \((-1)^jQ^{\binom j2}\). Expanding the indicator of an invertible endomorphism through the subspaces of its kernel, the left side of (2) equals
\[
\sum_{L\le W}(-1)^{\dim L}Q^{\binom{\dim L}2}
\sum_{Y\in\operatorname{End}_K(W),\,L\subseteq\ker Y}
\theta(\operatorname{tr}Y).
\]
For each proper \(L<W\), the inner sum is zero: the corresponding space of endomorphisms contains a rank-one operator with nonzero trace (choose a functional vanishing on \(L\) and a vector on which it takes value one), so its additive-character sum vanishes. Only \(L=W\) remains, and the sole endomorphism there is zero. This proves (2) without invoking a character table.

**4. Fourier evaluation and inversion.** Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\). For each \(a\in\mathbb F_q^\times\), the sum
\[
S(a)=\sum_{X\in\mathcal C(A)^\times}
\psi\big(a\operatorname{tr}X\big)
\]
factors, by (1) and the quotient fibers of Step 1, into \(q^r\) times one sum over each invertible residue factor. For \(p\mid s\), that factor is the entire group order. For \(p\nmid s\), the character \(u\mapsto\psi(as\operatorname{Tr}_{\mathbb F_{Q_f}/\mathbb F_q}u)\) on \(\mathbb F_{Q_f}\) is nontrivial: \(as\ne0\), and the finite-field trace map is surjective. Identity (2) now gives \(S(a)=B\), **independently of the nonzero** \(a\). Also \(S(0)=G\). Additive Fourier inversion yields
\[
T_A(b)=\frac1q\sum_{a\in\mathbb F_q}S(a)\psi(-ab)
=\begin{cases}
\big(G+(q-1)B\big)/q,& b=0,\\
\big(G-B\big)/q,&b\ne0.
\end{cases}
\]
All steps hold for any finite-field characteristic and prove that the displayed expressions are nonnegative integers. \(\square\)

## Verification

The included dependency-free `verify.py` constructs the full linear commutant by solving \(AX=XA\), independently enumerates every commuting matrix for each selected small-field example, tests invertibility by Gaussian elimination, and tallies its ordinary matrix trace. Separately it computes the proposed closed formula from the elementary-divisor description of the test matrix. It confirms all fiber counts in **45 cases** over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), covering scalar matrices, single and mixed Jordan blocks, distinct eigenvalues, and irreducible quadratic and cubic factors (including a squared quadratic factor). The output ends in `VERIFY_OK`.

Run with `python3 verify.py` using Python 3 and no additional packages. These calculations are exhaustive **within each displayed example**, not an enumeration of all similarity classes or a proof in arbitrary dimension. The all-fields proof is Steps 1–4 above.

Two boundaries help check the normalization. If \(A\) consists of one length-\(p\) nilpotent block in characteristic \(p\), its invertible centralizer has trace identically zero. If \(A\) is scalar, \(\mathcal C(A)^\times=\mathrm{GL}_n(\mathbb F_q)\), and the formula specializes to the established all-invertible-matrix trace count of Li and Hu.

## Relationship to prior work

Britnell and Wildon [1] develop finite-field commuting class types and centralizer structure. Their §3.1, in particular Proposition 3.5, describes the block-length multiplicities in centralizer-module composition factors and §3.2 determines attainable **determinants** of centralizer elements. These are relevant structural antecedents to Steps 1–2 but do not provide the numerical trace fibers of the centralizer unit group. Li and Hu [2], Theorems 2.1 and 3.1, evaluate additive matrix-group Gauss sums and completely count trace fibers in \(\mathrm{GL}_n(\mathbb F_q)\), which is precisely the scalar-\(A\) special case; these results are explicitly credited. Mingueza, Montoro and Roca [3], especially §§4–6, give explicit centralizer blocks over arbitrary fields and dimension and determinant calculations; their full open-access text does not give a trace-fiber distribution. The theorem synthesizes centralizer-type data with additive character sums for an **arbitrary** rational canonical type. A related software reference [4] tabulates centralizer algebra dimension and group order, not the trace-fiber distribution.

## Limitations

This is a finite-field theorem for **invertible elements of the ordinary centralizer**; it does not enumerate trace fibers with an additional determinant constraint, nor count conjugacy classes within those fibers. The proof depends on the classical semisimple-quotient description of endomorphism algebras of finite-length modules and the elementary additive-character identity (2), which is independently proved here. Although close primary articles and available published search records have been checked, a corresponding formula could exist under another terminology or in unindexed literature. No independent external audit has been performed.

## References

[1] J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, originally publicly posted 2010-01-06. Full text: https://ar5iv.labs.arxiv.org/html/1001.0811. Especially §3.1–3.2, Propositions 3.5–3.6 and Theorem 3.1.

[2] Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513 (2011). Full text: https://arxiv.org/pdf/1105.4513. Especially Theorems 2.1 and 3.1.

[3] D. Mingueza, M. E. Montoro and A. Roca, *The centralizer of an endomorphism over an arbitrary field*, arXiv:1909.06198 (2019). Full text: https://arxiv.org/pdf/1909.06198. Especially §§4–6, including Theorem 6.1 and §6.1–6.2.

[4] SageMath documentation, *Similarity class types of matrices with entries in a finite field*, `centralizer_algebra_dim` and `centralizer_group_cardinality`. https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/similarity_class_type.html.
