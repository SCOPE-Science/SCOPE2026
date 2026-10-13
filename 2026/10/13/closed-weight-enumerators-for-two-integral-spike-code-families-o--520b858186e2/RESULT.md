# Closed weight enumerators for two integral spike-code families over \(\mathbb Z/q\mathbb Z\)

## Finding
For every pair of integers \(k,q\geq2\), let \(R=\mathbb Z/q\mathbb Z\) and let \(J_k\) denote the all-one square matrix. Consider the two length-\(2k\) and length-\(2k+1\) linear codes over \(R\) generated respectively by
\[
G_N=[I_k\mid J_k-I_k],\qquad G_Z=[I_k\mid J_k-I_k\mid\mathbf1].
\]
Their ordinary Hamming-weight enumerators \(W_C(z)=\sum_{c\in C}z^{\operatorname{wt}(c)}\) admit the following uniform closed form. Set
\[
T_{k,q}=\sum_{j=0}^{k}\binom kj\gcd(q,j-1),\qquad \gcd(q,0)=q,
\]
\[
A_{k,q}(z)=\frac1q\sum_{j=0}^{k}\binom kj\bigl((q-1)^j+(q-1)(-1)^j\bigr)z^{2j},
\]
\[
B_{k,q}(z)=\frac{(q-1)(2+(q-2)z)^k+\bigl(qT_{k,q}-(2q-1)2^k\bigr)(1-z)^k}{q}.
\]
Then, for all \(k,q\geq2\),
\[
\boxed{W_{N_k(q)}(z)=A_{k,q}(z)+z^kB_{k,q}(z)},\qquad
\boxed{W_{Z_k(q)}(z)=A_{k,q}(z)+z^{k+1}B_{k,q}(z)}.
\]
These are identities in \(\mathbb Z[z]\), including composite moduli; the coefficients are nonnegative counts. The formulas provide every Hamming-weight multiplicity using a single binomial-gcd statistic and polynomial expansions rather than enumerating messages or all column subsets.

## Assumptions and scope
The alphabet is the residue *ring* \(R=\mathbb Z/q\mathbb Z\), not the field of order \(q\) when \(q\) is composite. Coordinates are counted as nonzero in \(R\). Both displayed integral matrices reduce modulo \(q\); their first \(k\) columns form an identity matrix, so every message \(u\in R^k\) gives a distinct codeword. The statement concerns only these two generator matrices and all integers \(k,q\ge2\); it makes no assertion about arbitrary spike representations or code equivalences.

## Proof
For a message \(u=(u_1,\dots,u_k)\), put \(s=\sum_i u_i\in R\). Its two codewords are respectively
\[
(u_1,\ldots,u_k,s-u_1,\ldots,s-u_k),\qquad
(u_1,\ldots,u_k,s-u_1,\ldots,s-u_k,s).
\]
Partition messages into \(s=0\) and \(s\ne0\).

If \(s=0\), the two positions associated to \(u_i\) contribute weight \(2\) for \(u_i\ne0\), otherwise weight \(0\); the appended coordinate is zero. The number of \(j\)-tuples of nonzero elements of \(R\) summing to zero is
\[
M_j=\frac{(q-1)^j+(q-1)(-1)^j}{q}.
\]
Indeed, apply character orthogonality in the additive cyclic group of \(R\): the trivial additive character contributes \((q-1)^j\), and each of its other \(q-1\) characters has sum \(-1\) over nonzero residues. Choosing the \(j\) nonzero positions yields exactly \(A_{k,q}(z)\).

For \(s\ne0\), the pair \((u_i,s-u_i)\) has weight \(1\) when \(u_i\in\{0,s\}\), and weight \(2\) otherwise. Write \(t\) for the number of coordinates of the latter kind. The codeword weight is \(k+t\) for \(N\), and \(k+t+1\) for \(Z\). Fix \(s\ne0\) and let \(\zeta=e^{2\pi i/q}\). The root-of-unity filter for \(\sum u_i=s\) gives
\[
\sum_{\substack{u\in R^k\\\sum u_i=s}}z^{t(u,s)}
=\frac1q\left[(2+(q-2)z)^k+(1-z)^k
\sum_{a=1}^{q-1}\zeta^{-as}(1+\zeta^{as})^k\right].
\]
For each nontrivial character \(a\), the two choices \(u_i=0,s\) contribute \(1+\zeta^{as}\), while the other \(q-2\) residues contribute \(-z(1+\zeta^{as})\), proving the displayed factorization even when \(s\) is not a unit. Summing over \(s\ne0\), expand \((1+\zeta^{as})^k\) by the binomial theorem. For every integer \(j\),
\[
\sum_{a=1}^{q-1}\zeta^{a(j-1)s}=q\,\mathbf1_{(j-1)s=0}-1,
\]
and there are exactly \(\gcd(q,j-1)-1\) nonzero residues \(s\) satisfying \((j-1)s=0\). Hence
\[
\sum_{s=1}^{q-1}\sum_{a=1}^{q-1}\zeta^{-as}(1+\zeta^{as})^k
=\sum_{j=0}^{k}\binom kj\bigl(q\gcd(q,j-1)-(2q-1)\bigr)
=qT_{k,q}-(2q-1)2^k.
\]
This is exactly \(B_{k,q}(z)\); the two weight shifts complete the proof. Integrality and coefficient nonnegativity follow from the original counting interpretation. Moreover \(A_{k,q}(1)=q^{k-1}\) and \(B_{k,q}(1)=(q-1)q^{k-1}\), so both enumerators count all \(q^k\) distinct codewords.

## Verification
The standalone standard-library Python file `verify.py` constructs both original integer generator matrices and enumerates codewords over residue rings for \(52\) bounded parameter pairs. An independent dynamic program counts all message residues and the nonzero-sum weight strata for \(84\) parameter pairs. Both match the coefficient formula exactly. The script also checks the published \(N_4\) and \(Z_5\) table coefficients and recovers the published full-support coefficient identity. Run `python3 verify.py`; success prints `VERIFY_OK`. These finite tests supplement, but do not replace, the proof valid for all stated integers.

## Relationship to prior work
Imamura, Nakashima, and Saito introduce these two integral code families, explain their link with binary spikes, and provide the general column-subset Smith-normal-form framework for residue-code weight enumerators. Their Section 5 determines minimum distances and the full-support coefficients, while Sections 5–6 tabulate small fixed parameter values. Those results, their spike construction, and the general all-subsets counting method are prior work. The contribution here is a closed, all-weight, all-\(k,q\) expression compressed to the single arithmetic statistic \(T_{k,q}\), with a direct additive-character proof. The general coding-matroid/coboundary correspondence of Kuroda, Nakashima, and Tsujie is a further background framework; it does not itself state the displayed family-specific formula.

## Limitations
The claim is a closed expression for these two specific modular generator matrices. It does not prove a new minimum distance, previously unreported full-support count, or a new universal enumerator algorithm. The formal identity is exact over every residue ring \(\mathbb Z/q\mathbb Z\) with \(q\ge2\); no claims are made for distinct finite-field alphabets at composite prime-power order. Earlier equivalent closed forms, including those formulated as specialization of a Tutte or coboundary polynomial, cannot be categorically excluded by the literature search.

## References
1. K. Imamura, N. Nakashima, T. Saito, *Periodicity of weight enumerators for codes generated by an integral matrix*, arXiv:2601.21121 (first publicly posted 2026-01-28), especially Proposition 3.4, Section 5, and the examples in Section 6. https://arxiv.org/abs/2601.21121
2. A. Kuroda, N. Nakashima, S. Tsujie, *The Coboundary Quasi-Polynomials of Hyperplane Arrangements over Residually Finite Dedekind Domains*, arXiv:2512.10838 (2025), background coding/matroid enumerator formalism. https://arxiv.org/abs/2512.10838
