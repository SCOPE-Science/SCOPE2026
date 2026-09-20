# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The main estimate was checked from the spectral decomposition of
\[
Q=\sum_{j=1}^m|X_j|.
\]
For \(c=\lambda_k(Q)\), the bottom spectral subspace \(E\) has dimension
\(d-k+1\), its orthogonal complement has dimension \(k-1\), and
\(P_{E^\perp}QP_E=0\). The \(m-1\) leakage maps
\[
P_{E^\perp}|X_j||_E:E\to E^\perp
\]
have a common nonzero kernel whenever
\[
d-k+1-(m-1)(k-1)=d-mk+m\ge1.
\]
The vanishing of the sum of all leakage maps then forces the last leakage map to
vanish on the same vector. On that vector every \(|X_j|\) stays inside \(E\).

The compressed positive operators
\[
C_j=P_E|X_j||_E
\]
satisfy
\[
0\le C_j\le\sum_\ell C_\ell=Q|_E\le cI,
\]
so \(C_j^2\le cC_j\). This gives
\[
\sum_j\|X_jx\|^2
=\sum_j\|C_jx\|^2
\le c\langle Qx,x\rangle
\le c^2.
\]
The expansivity condition gives \(\|\sum_jX_jx\|\ge1\), while vector
Cauchy--Schwarz gives
\[
\left\|\sum_jX_jx\right\|^2\le m\sum_j\|X_jx\|^2.
\]
Therefore \(c\ge m^{-1/2}\). No commutativity, simultaneous diagonalization, or
complementability assertion is used.

The \(3\times3\) sharp family was checked algebraically. Its two relevant
\(2\times2\) positive blocks have determinants \(t^2\) and \(t^2+1\), respectively,
so the standard closed formula for a positive \(2\times2\) square root yields the
two diagonal entries of the \(\{e_1,e_2\}\) compression stated in `RESULT.md`.
Both tend to \(1/\sqrt2\). Cauchy interlacing gives the needed upper bound for the
middle eigenvalue, while the theorem supplies the matching lower bound.

For the \(2\times2\) filler, direct calculation gives trace \(2\sqrt{t^2+1}\) and
determinant \(1\) for \(|C_t|+|D_t|\), hence eigenvalues
\[
\sqrt{t^2+1}\pm t.
\]
The direct-sum eigenvalue counts in odd dimensions and in even dimensions at least
six then place the active \(3\times3\) middle eigenvalue exactly at the requested
median position asymptotically.

## Originality

The principal recent sources were compared at theorem/proposition level.

- Bourin--Lee, arXiv:2602.19607v1, Question 6.3 asks for median-eigenvalue lower
  bounds for both sums of ordinary moduli and sums of symmetric moduli under an
  expansivity assumption.
- Zhang, arXiv:2603.01046v1, Proposition 2.7 gives a two-summand \(3\times3\)
  example with ordinary-modulus middle eigenvalue about \(0.8835\), refuting the
  value \(1\), but does not state the positive sharp lower bound obtained here.
- Aouichaoui--Lee, arXiv:2609.20094v1, proves a \(1/2\) median lower bound for the
  symmetric-modulus problem. For ordinary moduli it gives a three-summand
  \(3\times3\) construction with arbitrarily small middle eigenvalue and notes
  Zhang's two-summand example; it does not give a two-summand lower bound.

Searches using ordinary modulus, expansive decomposition, median eigenvalue,
two-summand modulus inequalities, singular-value formulations, and the equivalent
dimension condition did not locate the theorem above or an equivalent sharp
\(1/\sqrt2\) two-summand median statement. The current SCOPE archive was also
checked by the source paper, mathematical object, and equivalent claim family,
with no overlapping record found.

The standard ingredients of the proof are excluded from the novelty claim:
spectral subspaces, rank-nullity, Cauchy--Schwarz, Cauchy interlacing, formulas for
\(2\times2\) positive square roots, and direct sums are classical. The claimed new
content is their combination into the dimension-leakage theorem for expansive
ordinary-modulus sums, the resulting two-summand sharp median lower bound, and the
explicit sharpness families.

No directly relevant inaccessible primary source was identified. The main
residual originality risk is older matrix-inequality or singular-value literature
that may encode the same bound under different terminology, especially results
about eigenvalues of sums of absolute values or decompositions of expansive
operators. The originality judgment is therefore to the best of our knowledge,
not a claim of exhaustive bibliographic coverage.

## Value

The result gives a positive and, except for the unresolved \(4\times4\) case in
the dimensional sharpness discussion, broadly sharp answer on the ordinary-modulus
side of a current matrix-analysis question. It also explains why the recent
three-summand counterexample does not contradict the two-summand phenomenon:
the common-kernel dimension changes exactly at
\[
d=m(k-1)+1.
\]
The general \(m,k,d\) form is reusable beyond the median case.

## Limitations

The constant \(m^{-1/2}\) is not claimed sharp for every admissible
\((d,m,k)\). The exact two-summand median constant in \(M_4\) is not determined.
No infinite-dimensional essential-spectrum analogue is established. The
bibliographic conclusion is limited by the possibility of older equivalent
results expressed in different matrix-inequality language.
