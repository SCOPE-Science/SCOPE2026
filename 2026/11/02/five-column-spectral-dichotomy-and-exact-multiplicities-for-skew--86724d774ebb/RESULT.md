# Five-column spectral dichotomy and exact multiplicities for skew-conference tight frames

## Finding

Let \(N\ge8\) and let \(C\) be any real \(N\times N\) skew-symmetric conference matrix: \(C_{ii}=0\), \(C_{ij}\in\{-1,1\}\) for distinct indices, and \(CC^{\mathsf T}=(N-1)I\). Put \(p=N-1\) and \(G=I+iC/\sqrt p\). This is the unit-norm Gram matrix of an \((N/2,N)\) complex equiangular tight frame. Every five-element index set \(J\) has precisely one of two Gram spectra:

\[
\begin{aligned}
\mathsf A:\quad &1,\quad 1\pm\sqrt{(5+2\sqrt5)/p},\quad 1\pm\sqrt{(5-2\sqrt5)/p},\\
\mathsf B:\quad &1,\quad 1\pm\sqrt{7/p},\quad 1\pm\sqrt{3/p}.
\end{aligned}
\]

The numbers of five-element index sets having these spectra are **independent of the conference matrix** and exactly

\[
A_5=\frac{p(p-1)(p+1)(p-3)(p-7)}{320},\qquad
B_5=\frac{p(p-1)(p+1)^2(p-3)}{192}.
\]

Thus at \(N=8\) only class \(\mathsf B\) occurs. For every permitted \(N\ge12\) both classes occur. The sharp five-column restricted-isometry deviation is

\[
\delta_5=\max_{|J|=5}\|G_J-I\|_{\mathrm{op}}=
\begin{cases}
1,&N=8,\\
\sqrt{(5+2\sqrt5)/(N-1)},&N\ge12.
\end{cases}
\]

In particular, all five-column subframes are linearly independent for \(N\ge12\), whereas every five-column subframe of the order-eight example is dependent. For \(N\ge12\), the largest squared five-column condition number is \((1+\delta_5)/(1-\delta_5)\), attained precisely by class \(\mathsf A\).

## Assumptions and scope

The theorem applies to *every existing* real skew-symmetric conference matrix of order \(N\ge8\); no existence is asserted for all integers \(N\). Such matrices necessarily have orders divisible by four. The integer \(p=N-1\) need not be prime or a prime power. In particular, the Paley construction supplies matrices when \(p\equiv3\pmod4\) is a prime power; the reproducibility script tests prime-field examples. Gram eigenvalues count multiplicities and the two \(\pm\) signs in each class each contribute one eigenvalue. All norms and restricted-isometry constants use unit-norm columns.

## Proof

**Conference-frame normalization.** Skew symmetry and \(CC^{\mathsf T}=pI\) give \(C^2=-pI\). Consequently \(Q=iC/\sqrt p\) is Hermitian with \(Q^2=I\) and trace zero. Therefore \(G=I+Q\) has eigenvalue two with multiplicity \(N/2\) and zero with multiplicity \(N/2\); its diagonal entries are one and every off-diagonal entry has modulus \(1/\sqrt p\).

**Universal five-point dichotomy.** Fix \(J\) with five indices and put \(S=C_J\). Every four-by-four principal skew sign submatrix has Pfaffian \(s_{ab}s_{cd}-s_{ac}s_{bd}+s_{ad}s_{bc}\), a sum of three signs. Its square is either \(1\) or \(9\). Let \(r\) be the number of four-subsets of \(J\) for which the square is \(9\). The characteristic polynomial of \(S\) is

\[
\det(zI-S)=z(z^4+10z^2+5+8r).
\]

Writing its nonzero eigenvalues as \(\pm i\sqrt{\mu_1},\pm i\sqrt{\mu_2}\), one has \(\mu_1+\mu_2=10\) and \(\mu_1\mu_2=5+8r\). Reality gives \(100-4(5+8r)\ge0\), hence \(r\le2\). A parity refinement excludes \(r=1\): the integer matrix \(I+S\) has every entry odd, so subtracting its first row from each remaining row shows \(16\mid\det(I+S)\). But the characteristic-polynomial identity gives \(\det(I+S)=16+8r\), forcing \(r\) even. Thus \(r\in\{0,2\}\). For \(r=0\), the two squared frequencies are \(5\pm2\sqrt5\); for \(r=2\), they are \(7\) and \(3\). The asserted Gram eigenvalues now follow from \(G_J=I+iS/\sqrt p\).

**Exact universal multiplicities.** Let \(B_4\) count four-element principal submatrices of \(C\) whose Pfaffian has squared magnitude nine. Expanding the coefficient of \(z^{N-4}\) in \(\det(zI-C)=(z^2+p)^{N/2}\) by principal minors yields

\[
\binom{N/2}{2}p^2=\binom N4+8B_4,
\qquad B_4=\frac{p(p-1)(p+1)^2}{96}.
\]

Every such four-subset belongs to \(N-4=p-3\) five-subsets, and every class-\(\mathsf B\) five-subset contains exactly two of them. Double counting therefore gives

\[
B_5=\frac{(p-3)B_4}{2}=\frac{p(p-1)(p+1)^2(p-3)}{192}.
\]

All remaining five-subsets are class \(\mathsf A\). Hence \(A_5=\binom{p+1}{5}-B_5=p(p-1)(p+1)(p-3)(p-7)/320\). The existence of \(N\ge12\) skew conference matrices is not assumed; whenever one exists, both displayed positive counts prove both classes occur. At \(p=7\), \(A_5=0\).

**Sharp norm and independence.** Among the two classes, the largest eigenvalue displacement from one is respectively \(\sqrt{(5+2\sqrt5)/p}\) and \(\sqrt{7/p}\). Since \(5+2\sqrt5>7\), class \(\mathsf A\) gives the sharp norm whenever it exists. At \(p=7\), only \(\mathsf B\) occurs and its smallest Gram eigenvalue is zero. When \(p\ge11\), every displayed eigenvalue is strictly positive, and the eigenvalue ratio is maximized by class \(\mathsf A\).

## Verification

The included `checker.py` reconstructs skew Paley conference matrices by Legendre symbols and checks \(C^2=-pI\). It independently tests all \(2^{10}=1024\) five-vertex skew sign patterns, their parity constraints, and the two spectral forms; then enumerates all five-column subsets for primes \(7,11,19,23,31\), confirming exact counts and representative Hermitian eigenvalues. It uses NumPy. Run `python checker.py` in the extracted package directory. The analytic argument above covers every finite size for which a skew conference matrix exists; the finite checker is corroboration and not an infinite proof.

## Relationship to prior work

Renes (2004) supplies the Paley tournament and related quadratic-residue equiangular tight-frame constructions; these matrices and their global two-eigenvalue property are not new. Hoffman and Solazzo (2011) study complex ETF erasures, especially three- and four-erasure robustness, but do not give these five-column spectral multiplicities. King (2025) identifies symmetry properties of Paley skew-conference ETFs and classifies higher-homogeneity possibilities, without the present five-column spectrum census. Haemers and Parsaei Majd (2021) explicitly exclude the skew-conference case from their study of symmetric spectra of principal submatrices. A related published four-column Paley harmonic-frame census addresses smaller minors, not the five-column Pfaffian parity exclusion and incidence counts. The new claim is the universal two-class five-column classification, its exact frequencies and the resulting sharp five-column norm.

## Limitations

This result does not classify the geometry or symmetry orbits of the two classes, and it does not determine six-column spectra. It assumes skew conference matrices already exist. Its novelty was assessed against accessible sources and semantically related published work, not certified exhaustive across historical literature. No independent mathematical audit or external validation has been performed.

## References

- J. M. Renes, *Equiangular Tight Frames from Paley Tournaments*, first publicly posted 2004-08-20, arXiv:math/0408287, https://arxiv.org/abs/math/0408287.
- T. R. Hoffman and J. P. Solazzo, *Complex Equiangular Tight Frames and Erasures*, first publicly posted 2011-07-08, arXiv:1107.2267, https://arxiv.org/html/1107.2267v1.
- W. H. Haemers and L. Parsaei Majd, *Spectral symmetry in conference matrices*, first published 2021-03-18, https://doi.org/10.1007/s10623-021-00858-8.
- E. J. King, *\(k\)-Homogeneous Equiangular Tight Frames*, first publicly posted 2025-04-30, arXiv:2505.00160, https://arxiv.org/abs/2505.00160.
- A. S. Bandeira, M. Fickus, D. G. Mixon, and P. Wong, *The Road to Deterministic Matrices with the Restricted Isometry Property*, first publicly posted 2012-02-06, arXiv:1202.1234, https://arxiv.org/abs/1202.1234.
- *Four-column spectral census and sharp distortion of Paley harmonic frames*, related published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-four-column-spectral-census-and-sharp-distortion-of-paley-harmon--318c7b91876e.
