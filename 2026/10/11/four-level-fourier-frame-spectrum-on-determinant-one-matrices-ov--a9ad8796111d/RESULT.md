# Four-level Fourier frame spectrum on determinant-one matrices over finite fields

## Finding
Let \(q\ge2\) be any prime power, \(F=\mathbb F_q\), and let \(\psi:F\to\mathbb C\) be any nontrivial unitary additive character. Set
\[
S=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in F^{2\times2}:ad-bc=1\right\},\qquad |S|=q(q^2-1).
\]
Define the \(4q-3\) functions on \(S\)
\[
\phi_0(M)=1,\qquad \phi_{j,u}(M)=\psi(u M_j),\quad
j\in\{a,b,c,d\},\quad u\in F^\times.
\]
Here the four matrix entries are separate coordinates and the inner product is the uniform-probability inner product \(\langle f,g\rangle=|S|^{-1}\sum_{M\in S}\overline{f(M)}g(M)\). Let \(G\) be the Hermitian Gram matrix indexed by these functions.

**Theorem.** The complete spectrum of \(G\), listing multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\displaystyle \mu_- =1-\frac{3q-5+\sqrt{9q^2-14q+9}}{2(q^2-1)}&1\\[3pt]
\displaystyle \frac{q}{q+1}&2q-2\\[3pt]
\displaystyle \mu_+=1-\frac{3q-5-\sqrt{9q^2-14q+9}}{2(q^2-1)}&1\\[3pt]
\displaystyle \frac{q}{q-1}&2q-3
\end{array}
\]
with strict ordering \(0<\mu_-<q/(q+1)<\mu_+<q/(q-1)\) for all \(q\ge2\). All eigenvalue multiplicities are valid also at \(q=2\). In particular, these characters are linearly independent on \(S\).

For every coefficient vector \(z\in\mathbb C^{4q-3}\), the following are the **sharp** lower and upper inequalities:
\[
\mu_-\sum_i|z_i|^2\ \le\ \frac{1}{q(q^2-1)}\sum_{M\in S}\left|\sum_i z_i\phi_i(M)\right|^2
\ \le\ \frac{q}{q-1}\sum_i|z_i|^2.
\]
The equality spaces at both endpoints, indeed all eigenspaces, are explicitly described below. The squared Riesz condition number is \(\frac{q}{(q-1)\mu_-}=1+\frac4q+O(q^{-2})\).

## Assumptions and scope
No parity assumption is made on \(q\); the theorem includes nonprime fields and characteristic two. The only character assumption is that \(\psi\) be a nontrivial additive character; the result is independent of its choice. The ambient \(F^4\) Fourier characters are restricted to the affine determinant-one locus \(S\), not Fourier characters of the nonabelian group \(\mathrm{SL}_2(F)\) itself. The constant character occurs once and each nonzero-frequency one-coordinate character occurs once.

For a constructive equality-space description put \(n=q-1\), \(\rho=(q^2-1)^{-1}\), and define \(m_j\) as the unit coefficient vector that is constant, of value \(n^{-1/2}\), on the \(n\) frequencies in coordinate \(j\) and zero elsewhere. Put \(e_0\) for the unit coefficient vector at the constant character. For \(\epsilon\in\{+1,-1\}\), define an \(n\)-by-\(n\) real matrix
\[
(K_\epsilon)_{u,v}=\sum_{t\in F^\times}\psi\left(ut+\epsilon v/t\right),\quad u,v\in F^\times.
\]
Let \(H=\{w\in\mathbb C^{F^\times}:\sum_{u\in F^\times}w_u=0\}\). All vector equalities below are in coefficient space, with unspecified blocks zero.

## Proof
**1. Exact Gram entries.** Every nonzero vector in a fixed row or column of a matrix in \(S\) has exactly \(q\) completions to a determinant-one matrix. Thus a nontrivial two-variable additive sum along two distinct entries sharing a row or column equals \(-q\). For a fixed entry \(a=t\), its completion count is \(q^2\) if \(t\ne0\) and \(q(q-1)\) if \(t=0\). A nontrivial one-coordinate additive sum consequently also equals \(-q\). Dividing by \(|S|\), the constant-to-nonzero-frequency and all distinct non-opposite Gram entries are \(-\rho\).

The two pairs of opposite entries need separate treatment. For fixed \(a,d\), the number of solutions of \(bc=ad-1\) is \(q-1+q\mathbf1_{ad=1}\). The constant part makes no contribution when both Fourier frequencies are nonzero. Similarly, fixing \(b,c\) gives the count \(q-1+q\mathbf1_{bc=-1}\). With \(G_{ij}=\langle\phi_i,\phi_j\rangle\), the \((a,d)\) opposite-coordinate Gram block is \(\rho K_{-1}\), and the \((b,c)\) block is \(\rho K_{+1}\). Both matrices are real and symmetric, by \(t\mapsto-t\) and the substitution interchanging the two frequency parameters. Every diagonal coordinate block equals \((1+\rho)I-\rho J\), with \(J\) the all-ones matrix.

**2. Exact Kloosterman block identity.** For either sign, \(K_\epsilon\mathbf1=\mathbf1\). A double additive-orthogonality calculation gives
\[
K_\epsilon K_\epsilon^*=q^2I-(q+1)J.
\]
Indeed, after expanding the left-hand side and summing over nonzero second-frequency parameters, the inner sum is \(q\mathbf1_{t=t'}-1\); the resulting diagonal matrix entries are \(q(q-1)-1\), and off-diagonal entries are \(-q-1\). Since \(K_\epsilon\) is real symmetric, it preserves \(H\), and \(q^{-1}K_\epsilon:H\to H\) is unitary. This exact identity, rather than an estimate for individual Kloosterman sums, is the decisive step.

**3. Large multiplicity eigenspaces.** On the sum-zero coefficient blocks \(H\) in each coordinate, all rank-one \(J\) terms disappear. For \((a,d)\) the residual operator is
\[
\begin{pmatrix}(1+\rho)I&\rho K_{-1}\\\rho K_{-1}&(1+\rho)I\end{pmatrix},
\]
with the analogous \(K_{+1}\) block for \((b,c)\). Its eigenvectors at eigenvalue \(1+\rho\pm q\rho\) are exactly
\[
\left(w,\ \pm q^{-1}K_\epsilon w\right),\qquad w\in H.
\]
Each opposite pair contributes \(q-2\) dimensions to each sign. Since \(1+\rho-q\rho=q/(q+1)\) and \(1+\rho+q\rho=q/(q-1)\), this accounts for \(2(q-2)\) dimensions at each bulk eigenvalue. When \(q=2\), \(H=\{0\}\) and the same formula is vacuous.

**4. Five-dimensional mean-frequency block.** In the orthonormal basis \(e_0,m_a,m_b,m_c,m_d\), the constant-to-coordinate coupling is \(-\sqrt{q-1}\rho\). The coordinate block has diagonal \(1-(q-2)\rho\), opposite-coordinate entry \(+\rho\), and adjacent-coordinate entry \(-(q-1)\rho\). The orthogonal vectors
\[
\frac{m_a-m_d}{\sqrt2},\quad \frac{m_b-m_c}{\sqrt2}
\]
are eigenvectors at \(q/(q+1)\), and
\[
\frac{m_a-m_b-m_c+m_d}{2}
\]
is an eigenvector at \(q/(q-1)\). The remaining two-dimensional subspace is spanned by \(e_0\) and \(v=(m_a+m_b+m_c+m_d)/2\). Its matrix is
\[
B_q=\begin{pmatrix}
1&-2\sqrt{q-1}\rho\\
-2\sqrt{q-1}\rho&1-(3q-5)\rho
\end{pmatrix}.
\]
Its characteristic roots are precisely \(\mu_-\) and \(\mu_+\), each simple. An eigenvector for either root \(\mu\) is
\[
2\sqrt{q-1}\rho\,e_0+(1-\mu)v,
\]
which obeys the first row of \((B_q-\mu I)z=0\); the second follows from the characteristic equation. Together with the two opposite-pair constructions and three mean-frequency vectors, these exhaust coefficient space and explicitly classify every eigenspace.

**5. Ordering, positivity and sharpness.** The determinant of \(B_q\) is \(q(q-1)/(q+1)^2>0\), and its trace is positive, so \(\mu_->0\). Clearly \(\mu_+>1>q/(q+1)\). Furthermore
\[
\frac q{q+1}-\mu_- = \frac{q+\sqrt{9q^2-14q+9}-3}{2(q^2-1)}>0
\]
for \(q\ge2\), and
\[
\frac q{q-1}-\mu_+=\frac{5q-3-\sqrt{9q^2-14q+9}}{2(q^2-1)}>0,
\]
since \((5q-3)^2-(9q^2-14q+9)=16q(q-1)>0\). The sharp inequalities are the Rayleigh bounds for the now-completely-diagonalized positive definite Gram matrix. Equality in the upper bound occurs *exactly* on the direct sum of the two positive-sign opposite-pair spaces from step 3 and the line spanned by \((m_a-m_b-m_c+m_d)/2\); its dimension is \(2q-3\). Equality in the lower bound occurs *exactly* on the one-dimensional \(\mu_-\) eigenspace of \(B_q\) specified in step 4. Expanding the explicit roots as \(q\to\infty\) yields \(\mu_-=1-3/q+O(q^{-2})\) and the asserted Riesz condition-number asymptotic.

## Verification
The standalone script `check_sl2.py` independently constructs the fields of orders \(2,3,4,5,7,8,9,11\), enumerates every determinant-one matrix in each field, forms the restricted additive Fourier Gram matrix, and compares *all* numerical eigenvalues and their multiplicities against the theorem. It also checks the Kloosterman block identity for both signs. Execution with NumPy returned:

`VERIFY_OK tested_fields=[2, 3, 5, 7, 11, 4, 8, 9] sampled_matrices=3090 Fourier_columns=172 all_Kloosterman_unitarity=PASS all_Gram_entries=PASS all_equality_spaces=PASS all_Gram_spectra=PASS max_error=2e-15`

These are finite cross-checks, not an argument for all prime powers. The proof above supplies the arbitrary-field quantifiers and equality spaces.

## Relationship to prior work
Li and Hu, *Gauss sums over some matrix groups* (arXiv:1105.4513, Theorem 2.4), evaluate the ambient additive Fourier transform of special linear groups in terms of Kloosterman sums. This supplies a broader Fourier-transform ingredient, but does not itself give the spectrum, frame bounds, or full equality spaces of the selected first-coordinate family. In the present proof that transform is rederived in the particular rank-one and rank-two frequency cases; the further all-parameter Kloosterman block identity and five-dimensional decomposition yield the exact spectral classification.

Thill and Hassibi, *Low-Coherence Frames from Group Fourier Matrices* (arXiv:1509.05739, especially Section VII), construct nonabelian group-representation frames using character tables of \(\mathrm{SL}_2(F)\). This is a different Fourier transform and a different selected family: the functions here are restrictions of **additive ambient-coordinate** characters, with exactly \(4q-3\) columns, not matrix coefficients of representations of the nonabelian group. The 2014 conference predecessor, Thill--Muthukumar--Hassibi, *Frames from generalized group Fourier transforms and \(\mathrm{SL}_2(F_q)\)* (DOI:10.1109/ICASSP.2014.6854538), is relevant context but a full copy was not available for a direct comparison. These references are not assertions of historical novelty.

## Limitations
The conclusion applies only to the constant plus the four full one-coordinate additive-frequency families on determinant-one \(2\)-by-\(2\) matrices. It does not classify higher coordinate-interaction bands, other varieties, or general subsets of Fourier frequencies. Finite numerical tests do not establish the arbitrary-field theorem. The use of known special-linear Fourier sums creates a historical-priority risk: an equivalent diagonalization may exist in older frame or Kloosterman-matrix literature. No independent audit or exhaustive literature novelty certification is asserted here.

## References
1. Yan Li and Su Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513 (first submitted 2011-05-23), Theorem 2.4. https://arxiv.org/abs/1105.4513
2. Matthew Thill and Babak Hassibi, *Low-Coherence Frames from Group Fourier Matrices*, arXiv:1509.05739 (first submitted 2015-09-18), Section VII. https://arxiv.org/abs/1509.05739
3. Matthew Thill, Vidya Muthukumar and Babak Hassibi, *Frames from generalized group Fourier transforms and \(\mathrm{SL}_2(F_q)\)*, ICASSP 2014, DOI:10.1109/ICASSP.2014.6854538.
