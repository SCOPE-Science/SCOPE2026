# Two-statistic Fourier sampling law for symmetric-group conjugacy classes

## Finding

For every integer \(n\ge4\), let \(G=S_n\), and let \(\mathcal H_n\subset\ell^2(G)\) be the complete Peter--Weyl block of the standard irreducible representation, of dimension \((n-1)^2\). Equip \(\ell^2(G)\) with counting measure. For any conjugacy class \(C\subset G\), let \(P\) project orthogonally onto \(\mathcal H_n\), and let \(K_C=PM_{\mathbf1_C}P\vert_{\mathcal H_n}\).

Let \(c_r\) be the number of cycles of length \(r\) in a permutation representing \(C\), and set \(f=c_1\), \(t=c_2\), and \(M=|C|\). Put
\[
\begin{aligned}
(D_0,D_1,D_2,D_3)&=\left(1,n-1,\frac{n(n-3)}2,\frac{(n-1)(n-2)}2\right),\\
R_0&=\frac{(f-1)^2}{n-1},\qquad R_1=\frac{f(n-f)}{n-2},\\
R_3&=\frac{n-f-2t}{2},\qquad R_2=n-1-R_0-R_1-R_3.
\end{aligned}
\]
Then each \(R_j\) is nonnegative and the **entire concentration spectrum** is
\[
\boxed{\quad\operatorname{spec}(K_C)=\bigsqcup_{j=0}^{3}\left\{\left(\frac{(n-1)M}{n!}\frac{R_j}{D_j}\right)^{[D_j]}\right\}.\quad}
\]
The superscript in brackets denotes multiplicity; zero and coincident eigenvalues must be counted with their total multiplicities. In particular, after division by the class density \(M/n!\), the four sector eigenvalues depend on the conjugacy class **only through the two counts \(f\) and \(t\)**. The class density itself can depend on other cycle lengths.

For \(n\ge5\), restriction to \(C\) is injective on \(\mathcal H_n\) if and only if \(C\) has **at least two fixed points and at least one cycle of length at least three**. For \(n=4\), no conjugacy class gives injective restriction. The precise null sectors are described below.

## Assumptions and scope

The vector space of complex-valued functions on \(S_n\) has inner product \(\langle h_1,h_2\rangle=\sum_{g\in S_n}h_1(g)\overline{h_2(g)}\). The symmetric group acts by its real orthogonal standard representation \(\rho\) on \(V=\mathbf1^\perp\subset\mathbb C^n\), where \(\mathbf1=(1,\ldots,1)\). Thus \(\dim V=n-1\). The Fourier block \(\mathcal H_n\) is the span of all matrix coefficients \(g\mapsto \langle \rho(g)u,v\rangle\), \(u,v\in V\); its dimension is \((n-1)^2\).

For the conjugacy class of cycle type \((c_1,c_2,\ldots,c_n)\), its size is \(M=n!/\prod_{r=1}^n r^{c_r}c_r!\). Restriction means the linear map \(\mathcal R_C:\mathcal H_n\to\ell^2(C)\), \(h\mapsto h\vert_C\). Its squared singular values are the eigenvalues of \(K_C=\mathcal R_C^*\mathcal R_C\). Empty or degenerate spectral sectors are not silently discarded: all displayed multiplicities are valid for \(n=4\), with appropriate zeros.

## Proof

**Step 1: the conjugation-orbit frame.** Let \(d=n-1\). Schur orthogonality identifies the Fourier block isometrically with \(\operatorname{End}(V)\), endowed with Hilbert--Schmidt inner product, by mapping \(A\) to \(g\mapsto\sqrt{d/n!}\,\operatorname{tr}(A^*\rho(g))\) (interpreted as a conjugate-linear isometry under this coefficient convention). Consequently, its concentration operator corresponds to
\[
T_C=\frac d{n!}\sum_{g\in C}|\rho(g)\rangle\langle\rho(g)|
\]
acting on \(\operatorname{End}(V)\). Since \(C\) is closed under conjugation, \(T_C\) commutes with the conjugation action \(A\mapsto\rho(h)A\rho(h)^{-1}\).

For \(n\ge4\), the conjugation module is multiplicity-free:
\[
\operatorname{End}(V)\simeq S^{(n)}\oplus S^{(n-1,1)}\oplus S^{(n-2,2)}\oplus S^{(n-2,1,1)}.
\]
Denote these mutually orthogonal invariant sectors by \(W_0,W_1,W_2,W_3\) in this order. Their dimensions are exactly \(D_0,D_1,D_2,D_3\). Schur's lemma makes \(T_C\) a scalar on each sector. Let \(\sigma\in C\), and let \(Q_j\) be the orthogonal projection onto \(W_j\). The trace on \(W_j\) of the rank-one sum is \(M\|Q_j\rho(\sigma)\|_{HS}^2\), so its scalar is exactly
\[
\frac{dM}{n!}\frac{\|Q_j\rho(\sigma)\|_{HS}^2}{D_j}.
\]
Thus it remains to compute the four squared sector energies.

**Step 2: scalar sector.** On the one-dimensional space spanned by \(I_V\), orthogonal projection gives
\[
\|Q_0\rho(\sigma)\|_{HS}^2=\frac{|\operatorname{tr}\rho(\sigma)|^2}{d}=\frac{(f-1)^2}{n-1}=R_0.
\]
Here \(\operatorname{tr}\rho(\sigma)=f-1\).

**Step 3: alternating sector.** The sector \(W_3\) consists of skew-symmetric endomorphisms of \(V\). Since the permutation matrices are real orthogonal,
\[
\|Q_3\rho(\sigma)\|_{HS}^2=\left\|\frac{\rho(\sigma)-\rho(\sigma)^T}{2}\right\|_{HS}^2=\frac{d-\operatorname{tr}(\rho(\sigma)^2)}2.
\]
The permutation \(\sigma^2\) fixes precisely \(f+2t\) points. Hence \(\operatorname{tr}(\rho(\sigma)^2)=f+2t-1\) and the alternating energy equals \(R_3=(n-f-2t)/2\).

**Step 4: symmetric standard sector.** Let \(P_V=I_n-\mathbf1\mathbf1^T/n\) and, for \(x\in\mathbf1^\perp\), define \(U(x)=P_V\operatorname{diag}(x)P_V\vert_V\). This map parametrizes \(W_1\). A direct calculation with the entries of \(P_V\) yields
\[
\langle U(x),U(y)\rangle_{HS}=\frac{n-2}{n}\langle x,y\rangle.
\]
Pairing \(U(x)\) with the permutation operator gives exactly \(\sum_{i:\sigma(i)=i}\overline{x_i}\). Its representing vector in \(\mathbf1^\perp\) is the centered fixed-point indicator, of squared norm \(f-f^2/n=f(n-f)/n\). Dividing by \((n-2)/n\) gives
\[
\|Q_1\rho(\sigma)\|_{HS}^2=\frac{f(n-f)}{n-2}=R_1.
\]

**Step 5: final sector and positivity.** The four sectors are mutually orthogonal and \(\|\rho(\sigma)\|_{HS}^2=d\). Thus \(\|Q_2\rho(\sigma)\|_{HS}^2=d-R_0-R_1-R_3=R_2\ge0\). Steps 1--5 establish the full spectrum, with no asymptotic assumptions.

**Step 6: exact rank criterion.** Let \(a=n-f\) be the number of moved points. Algebraic simplification gives
\[
R_2=t+\frac{a\bigl(2a+n^2-7n+6\bigr)}{2(n-1)(n-2)}.
\]
Either \(a=0\), or \(a=2\) and \(t=1\), or \(a\ge3\). For \(n\ge5\) and \(a\ge3\), the parenthesis is at least \((n-3)(n-4)>0\). Thus \(R_2=0\) precisely on the identity class when \(n\ge5\). For \(n=4\), direct substitution for the five cycle types shows \(R_2=0\) precisely for the identity and the three-cycle class. Furthermore, \(R_0=0\) exactly when \(f=1\); \(R_1=0\) exactly when \(f=0\) or \(f=n\); and \(R_3=0\) exactly when every cycle has length at most two. The simultaneous strict positivity of all four energies is therefore equivalent, for \(n\ge5\), to at least two fixed points together with one cycle of length at least three. Such a type does not exist for \(n=4\). This proves the restriction-injectivity assertions.

**Examples.** For a class consisting of \(n\)-cycles (\(n\ge4\)), the zero eigenvalue has multiplicity \(n-1\); the nonzero eigenvalues are \(M/n!\), of total multiplicity \(1+n(n-3)/2\), and \(nM/((n-2)n!)\), of multiplicity \((n-1)(n-2)/2\). If \(n\ge4\) is even and \(C\) consists of products of \(n/2\) disjoint transpositions, the restriction rank is \(1+n(n-3)/2\). The nonzero eigenvalues are \(M/n!\), multiplicity one, and \(2(n-2)M/((n-3)n!)\), multiplicity \(n(n-3)/2\). These consequences are instances of the single universal spectrum theorem, not separate claims.

## Verification

The accompanying standard-library Python script `artifacts/verify.py` constructs the permutation matrices and the exact Gram operator for **every conjugacy class** in \(S_n\) for \(4\le n\le7\). It avoids floating point: for each class it checks an integer annihilating polynomial on every standard coordinate and exact trace moments, sufficient to recover all eigenvalue multiplicities (by Vandermonde uniqueness). To reproduce, from the directory containing these files run `python3 artifacts/verify.py`. The expected terminal line is `VERIFY_OK conjugacy_classes=38 permutations=5904 n=4..7 exact_annihilating_polynomial_and_moment_multiplicities`. The finite verification corroborates the all-size proof; it does not replace it.

## Relationship to prior work

Scarabotti and Tolli's finite homogeneous-space harmonic analysis, especially their analysis of the ordered-pair permutation module in Section 3.2, supplies a closely related decomposition into symmetric and alternating constituents. Thill and Hassibi develop group Fourier frames and character-based Gram identities. Beck and Ghandehari construct group-theoretic Fourier-compatible frames on symmetric groups. These sources supply general representation and frame theory; their inspected statements do not give the all-conjugacy-class *spatial-restriction* spectrum with its two-cycle-statistic reduction and exact injectivity classification. The present result also simultaneously specializes to transposition and three-cycle class sampling, and should not be presented as rediscovering those separately treated cases.

## Limitations

This is a theorem about the complete standard Fourier block only, not arbitrary irreducible blocks or arbitrary unions or subsets of conjugacy classes. The two-statistic conclusion concerns eigenvalues **after class-density normalization**; the class size itself depends on the full cycle type. Finite checks through degree seven are not evidence for untested degrees without the analytic proof. The relationship to older representation-branching, orbit-frame, and permutation-matrix span formulas leaves a genuine possibility of equivalent prior formulations. No independent external validation has been performed; no exhaustive claim of historical priority is made.

## References

1. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533v1, first posted 2007-01-19, especially Section 3.2; https://arxiv.org/pdf/math/0701533 .
2. M. Thill and B. Hassibi, *Low-Coherence Frames from Group Fourier Matrices*, arXiv:1509.05739v1, first posted 2015-09-18, especially the group Fourier frame Gram identities in Section III; https://arxiv.org/pdf/1509.05739 .
3. J. Beck and M. Ghandehari, *Frames for Graph Signals on the Symmetric Group: A Representation Theoretic Approach*, arXiv:2203.03036v1, first posted 2022-03-06, especially Theorem III.6; https://arxiv.org/pdf/2203.03036 .
