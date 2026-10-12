# Fixed-space spectra of split almost-abelian Lie algebra automorphisms over finite fields

## Finding
For every prime power \(q\), every nonempty \(\Lambda\subseteq\mathbb F_q^\times\), and every positive integer multiplicity \(s_\lambda\) for \(\lambda\in\Lambda\), the **complete fixed-space dimension distribution of the automorphism group** of the Lie algebra
\[
L=\mathbb F_q t\ltimes\bigoplus_{\lambda\in\Lambda}V_\lambda,\qquad
\dim V_\lambda=s_\lambda,\qquad
[t,v]=\lambda v\quad(v\in V_\lambda),\quad[V,V]=0
\]
has the explicit formula below. Set \(n=\sum_{\lambda\in\Lambda}s_\lambda\), and let \(H\subseteq\mathbb F_q^\times\) be the multiplicity-preserving scalar stabilizer of the spectrum: \(a\in H\) if and only if multiplying every \(\lambda\) by \(a\) permutes \(\Lambda\) and preserves all multiplicities.

Set \(G_0(q)=1\) and, for integers \(s\geq1\),
\[
G_s(q)=|\operatorname{GL}_s(\mathbb F_q)|=\prod_{i=0}^{s-1}(q^s-q^i).
\]
Write \({r\brack k}_q\) for the Gaussian binomial coefficient and put
\[
P_s(z)=\sum_{k=0}^s h_{s,k}(q)z^k,\qquad
h_{s,k}(q)={s\brack k}_q\sum_{j=0}^{s-k}
(-1)^j q^{\binom j2}{s-k\brack j}_q
q^{(k+j)(s-k-j)}G_{s-k-j}(q).
\]
Thus \(h_{s,k}(q)\) is the number of invertible \(s\)-dimensional linear maps whose \(1\)-eigenspace has dimension \(k\). Let
\[
U(z)=\prod_{\lambda\in\Lambda}P_{s_\lambda}(z).
\]
For \(a\in H\setminus\{1\}\), let \(\mathcal C(a)\) be the cycles of the scalar permutation \(\lambda\mapsto a^{-1}\lambda\) of \(\Lambda\); the common multiplicity on a cycle \(C\) is \(s_C\). Define
\[
W_a(z)=\prod_{C\in\mathcal C(a)}G_{s_C}(q)^{|C|-1}P_{s_C}(z).
\]
Then the full distribution polynomial is
\[
\boxed{\displaystyle
F_L(z)=q^n\sum_{a\in H\setminus\{1\}}W_a(z)
+\sum_{k=0}^n [z^k]U(z)\left((q^n-q^{n-k})z^k+q^{n-k}z^{k+1}\right).}
\]
For every integer \(0\leq r\leq n+1\), the coefficient \([z^r]F_L(z)\) is **exactly** the number of \(\Phi\in\operatorname{Aut}_{\mathbb F_q}(L)\) with \(\dim\ker(\Phi-I)=r\). In particular,
\[
F_L(1)=|\operatorname{Aut}(L)|=|H|q^n\prod_{\lambda\in\Lambda}G_{s_\lambda}(q),
\qquad [z^{n+1}]F_L(z)=1.
\]
All characteristic cases, including \(q=2\), are included.

## Assumptions and scope
The Lie bracket is extended bilinearly and alternatingly from the displayed relations. Since all eigenvalues in \(\Lambda\) are nonzero, \([L,L]=V\), so the abelian ideal \(V\) is characteristic. The endomorphism \(\operatorname{ad}(t)|_V\) is diagonalizable over the ground field and invertible. No irreducible nonsplit blocks, zero eigenvalues, or nonsemisimple Jordan blocks are covered. The coefficients count ground-field-linear Lie automorphisms, not semilinear maps. The convention \(P_0(z)=1\) is allowed in intermediate formulas, although each displayed multiplicity is positive. For \(q=2\), the scalar stabilizer is necessarily trivial. The bracket remains valid in characteristic two.

## Proof
**1. Automorphisms and the scalar stabilizer.** Because \(V=[L,L]\), every Lie automorphism has, relative to \(\mathbb F_q t\oplus V\), the block form
\[
\Phi=\begin{pmatrix}a&0\\w&S\end{pmatrix},\qquad
 a\in\mathbb F_q^\times,\ w\in V,\ S\in\operatorname{GL}(V).
\]
Writing \(T=\operatorname{ad}(t)|_V\), the bracket condition is exactly \(ST=aTS\). Conversely, for any such triple the displayed map is invertible and preserves all brackets because \(V\) is abelian. From \(ST=aTS\), \(S(V_\lambda)=V_{a^{-1}\lambda}\); hence \(a\in H\). For each \(a\in H\) the maps from a source eigenspace to its target are arbitrary invertible maps of the corresponding dimensions. Every \(w\in V\) is free. This proves the group-order statement.

**2. Nonidentity scalar and cycle products.** When \(a\ne1\), the first equation in \((\Phi-I)(c t+v)=0\) forces \(c=0\); thus its fixed-space dimension equals \(\dim\ker(S-I)\), independent of \(w\). On a scalar-permutation cycle \(C\) of length \(d\), a fixed vector is uniquely determined by its component in one eigenspace, which must be fixed by the cycle product \(B\in\operatorname{GL}_{s_C}(\mathbb F_q)\) of the \(d\) intervening isomorphisms. For each choice of \(B\), precisely \(G_{s_C}(q)^{d-1}\) block tuples have that product. Its fixed-space-count polynomial is therefore \(G_{s_C}(q)^{d-1}P_{s_C}(z)\). Different cycles are independent, yielding \(W_a(z)\). Multiplication by the \(q^n\) choices of \(w\) gives the first sum.

**3. Identity scalar and translations.** When \(a=1\), the operator \(S\) is block diagonal on the eigenspaces. Its fixed-space dimension \(k=\dim\ker(S-I)\) has distribution \(U(z)\). The fixed-vector equations are
\[
(S-I)v=-c w.
\]
The image of \(S-I\) has cardinality \(q^{n-k}\). If \(w\in\operatorname{im}(S-I)\), the solution space has dimension \(k+1\); otherwise it has dimension \(k\). Exactly \(q^{n-k}\) of the \(q^n\) translations fall into the first case. Summing these two contributions for each \(k\) gives the second sum in the boxed formula.

**4. Explicit linear fixed-space coefficients.** Fix a \(k\)-dimensional subspace \(K\subseteq\mathbb F_q^s\). The number of invertible maps fixing \(K\) pointwise is \(q^{k(s-k)}G_{s-k}(q)\), since the map has block form \(\begin{psmallmatrix}I&X\\0&Y\end{psmallmatrix}\). The Möbius function of the finite lattice of subspaces assigns \((-1)^j q^{\binom j2}\) to a subspace of codimension difference \(j\). Applying Möbius inversion above \(K\), and multiplying by \({s\brack k}_q\) choices of \(K\), gives the displayed exact formula for \(h_{s,k}(q)\). This completes the proof for every prime power and multiplicity pattern.

## Verification
The standalone pure-Python program `verify.py` exhaustively enumerates ground-field matrices and their actual fixed-space dimensions. It checks 24 independently enumerated complete profiles—nine general-linear profiles and fifteen Lie-automorphism profiles—including unequal spectral supports, trivial and nontrivial scalar stabilizers, the characteristic-two field, and the quadratic extension field of order four. One larger extension-field case receives an additional formula-consistency check rather than full matrix enumeration. Five cyclic-support cases also enumerate the full automorphism matrices, including all translations; the remaining largest extension-field case checks the closed-form zero coefficient separately. The program prints `FINITE_CHECKS 25 VERIFY_OK` on successful completion. More precisely, ten arbitrary-spectrum profiles, five enumerated cyclic profiles, one non-exhaustive large-field formula check, and nine linear profiles together total twenty-five reported checks. The checker uses direct matrix rank rather than assuming the formula under test. These finite computations corroborate but do not replace the general proof.

For example, with \(q=3\), \(\Lambda=\{1,2\}\), and both multiplicities \(1\), the coefficients of \(F_L(z)\), from degree zero to three, are \((18,39,14,1)\), totaling \(72\). With \(q=5\), \(\Lambda=\{1,2\}\), and both multiplicities \(1\), the scalar stabilizer is trivial and the coefficients are \((0,345,54,1)\), totaling \(400\).

Run with a normal Python 3 installation as `python verify.py`. The program has no external package dependencies and takes only the installed standard library.

## Relationship to prior work
Burde and Dekimpe (2026) characterize the existence of fixed-point-free automorphisms in the centerless complex almost-abelian case using cyclotomic derivations, but do not give this complete finite-field distribution. Avetisyan (2016/2023), Proposition 9, determines the general block structure of automorphisms of indecomposable almost-abelian Lie algebras over arbitrary fields; our structural first step is a specialization of that established result, **not** a newly claimed automorphism-group classification. Arumugam, Dietrich and Glasby (2022/2023), Theorem 6.5, give the number-of-fixed-points distribution for permutation wreath-product actions, a powerful existing ingredient that covers the cycle-product component of the nonidentity-scalar sector. The theorem here combines those ingredients with explicit finite-field fixed-space Möbius coefficients and the separate, coupled translation correction in the identity-scalar sector to obtain the full distribution on the **entire Lie algebra**, including the distinguished one-dimensional quotient. None of those inspected statements supplies that final Lie-automorphism polynomial as stated. Earlier finite-linear-group enumerations may still admit an equivalent reformulation; this remains a literature risk.

## Limitations
Only split, diagonalizable, invertible defining endomorphisms are treated. This does not give the profile for a nonsplit or nilpotent defining endomorphism, nor classify fixed-point-free automorphisms of arbitrary solvable Lie algebras. The main claim is a finite-field exact counting identity with a mathematical proof, not an asserted independent review or certification. The finite checks are tests of examples rather than proofs of the infinitely many cases. The result may be recoverable by combining older general automorphism and wreath-action theorems; its precise standalone precedent status has not been independently certified.

## References
1. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916v1 (first public 2026-04-30), https://arxiv.org/abs/2604.27916 ; lawful full text https://homepage.univie.ac.at/dietrich.burde/papers/burde_83_fpf.pdf .
2. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365 (first public 2016-10-17; revised 2023), especially Proposition 9, https://arxiv.org/pdf/1610.05365 .
3. V. Arumugam, H. Dietrich and S. P. Glasby, *Derangements in wreath products of permutation groups*, arXiv:2207.01215 (2022), especially Theorem 6.5, https://arxiv.org/pdf/2207.01215 .
