# A universal \(k^{-1/2}\) law for Tjurina numbers of repeated Thom–Sebastiani sums

## Finding
Let \(f\in\mathbb C\{x_1,\ldots,x_m\}\), \(m\ge2\), define an isolated hypersurface singularity at the origin, with \(f(0)=0\) and \(df(0)=0\). Set \(A_f=\mathbb C\{\boldsymbol{x}\}/J_f\), \(\mu=\dim_{\mathbb C}A_f\), and let \(N\) be multiplication by the class of \(f\) in \(A_f\). Its nilpotent Jordan blocks have lengths \(\ell_1,\ldots,\ell_s\). For each integer \(k\ge1\), let \(F_k\) be the sum of \(k\) copies of \(f\) in disjoint groups of variables. Define the symmetric Laurent polynomial
\[
\chi_f(z)=\sum_{i=1}^{s}\sum_{a=0}^{\ell_i-1}z^{\ell_i-1-2a}.
\]
Then the **exact Tjurina number of every iterated sum** is
\[
\boxed{\tau(F_k)=[z^0]\chi_f(z)^k+[z^1]\chi_f(z)^k,\qquad\mu(F_k)=\mu^k.}
\]
If \(f\notin J_f\), put
\[
\sigma_f^2=\frac{1}{3\mu}\sum_{i=1}^s\ell_i(\ell_i^2-1)>0.
\]
The sharp asymptotic is
\[
\boxed{\lim_{k\to\infty}\sqrt{k}\,\frac{\tau(F_k)}{\mu(F_k)}=\sqrt{\frac{2}{\pi\sigma_f^2}}.}
\]
If \(f\in J_f\), instead \(\tau(F_k)=\mu(F_k)=\mu^k\) for every \(k\).

For an isolated plane-curve germ, the Briançon–Skoda containment \(f^2\in J_f\) gives the more explicit formula
\[
\boxed{\tau(F_k)=([z^0]+[z^1])\bigl((2\tau-\mu)+(\mu-\tau)(z+z^{-1})\bigr)^k.}
\]
In the non-quasihomogeneous case \(\mu>\tau\), the limit becomes
\[
\boxed{\lim_{k\to\infty}\sqrt{k}\,\frac{\tau(F_k)}{\mu^k}=\sqrt{\frac{\mu}{\pi(\mu-\tau)}}.}
\]
Thus the Tjurina-to-Milnor ratio along repeated separated sums has a universal inverse-square-root exponent, despite the usual pairwise Tjurina nonmultiplicativity.

## Assumptions and scope
All rings and tensor products are over \(\mathbb C\). The germ has an isolated critical point, so its Milnor algebra is finite-dimensional and local Artinian. The powers \(F_k\) are separated-variable sums, not ordinary polynomial powers. The asymptotic varies the number of independent variable groups \(k\) while holding the original analytic germ fixed. The coefficient extraction \([z^j]\) takes the coefficient of \(z^j\) in a Laurent polynomial. No claim is made in positive characteristic or for nonisolated singularities.

## Proof
**1. Reduction to nilpotent tensor sums.** The separated Jacobian equations give the canonical algebra isomorphism
\[
A_{F_k}\simeq A_f^{\otimes k},\quad [F_k]=\sum_{j=1}^k 1\otimes\cdots\otimes[f]\otimes\cdots\otimes1.
\]
Since \(f\) lies in the maximal ideal of the Artinian local algebra, multiplication by \([f]\) is nilpotent. By the definition of the Tjurina algebra,
\[
\tau(F_k)=\dim_{\mathbb C}\operatorname{coker}\!\left(\sum_{j=1}^k N_j\right),\qquad\mu(F_k)=\mu^k.
\]

**2. Exact character formula.** Over \(\mathbb C\), a nilpotent Jordan block of size \(\ell\) is conjugate to the standard raising operator on the irreducible \(\mathfrak{sl}_2\)-representation of highest weight \(\ell-1\). Equip the underlying vector space of \(A_f\) with the direct sum of these representations, choosing the raising operator to equal \(N\). The usual coproduct raising operator on its \(k\)-fold tensor power equals \(\sum_jN_j\). Complete reducibility of finite-dimensional \(\mathfrak{sl}_2\)-representations implies that the dimension of its cokernel is the number of irreducible summands: each irreducible has exactly one highest-weight vector, and exactly one vector of weight zero *or* one (but not both). The weight character of the chosen representation is \(\chi_f(z)\), and its tensor-power character is \(\chi_f(z)^k\). Hence the number of summands is exactly \([z^0]\chi_f(z)^k+[z^1]\chi_f(z)^k\), as asserted. This also proves the formula for all \(k\), not just the experimentally checked values.

**3. Sharp asymptotic.** Give each individual exponent appearing in \(\chi_f\) probability \(1/\mu\), respecting multiplicity. This defines a symmetric, finite-support integer-valued random variable \(W\) of mean zero and variance
\[
\operatorname{Var}(W)=\frac1\mu\sum_i\sum_{a=0}^{\ell_i-1}(\ell_i-1-2a)^2=\frac1{3\mu}\sum_i\ell_i(\ell_i^2-1)=\sigma_f^2.
\]
The variance is positive precisely when some Jordan block has length at least two, equivalently \(f\notin J_f\). Let \(S_k\) be a sum of \(k\) independent copies of \(W\). The exact formula reads
\[
\tau(F_k)/\mu^k=\Pr(S_k=0)+\Pr(S_k=1).
\]
The support of \(W\) has lattice span one if it includes both parities, and otherwise span two (because any block of length at least two has weights separated by two). The lattice local central limit theorem yields
\[
\Pr(S_k=0)+\Pr(S_k=1)=\frac{2}{\sqrt{2\pi\sigma_f^2 k}}+o(k^{-1/2}).
\]
Indeed, with span one, both fixed neighboring coefficients have the Gaussian leading term. With span two, exactly one of zero and one has the correct parity for each \(k\), and its leading mass has the extra lattice-span factor two. This proves the sharp constant. If every block has length one, \(N=0\) and the exact coefficient formula gives \(\tau(F_k)=\mu^k\).

**4. Plane-curve specialization.** For a plane-curve germ, the Briançon–Skoda containment \(f^2\in J_f\) forces \(N^2=0\). Let \(b=\operatorname{rank}N=\mu-\tau\). Its Jordan decomposition consists of \(b\) blocks of size two and \(\tau-b=2\tau-\mu\) blocks of size one. Substituting their character yields the stated Laurent-polynomial formula and \(\sigma_f^2=2b/\mu\). Both numerical statements follow immediately.

**5. A concrete non-quasihomogeneous family.** Consider the isolated plane-curve germ \(f=x^4+y^5+x^2y^3\). Give \(x,y\) weights \(5,4\). The weighted initial terms of \(f_x=4x^3+2xy^3\) and \(f_y=5y^4+3x^2y^2\) are \(4x^3\) and \(5y^4\), which are relatively prime. The associated graded Milnor algebra is \(\mathbb C[x,y]/(x^3,y^4)\); hence \(\mu=12\) and its highest-weight monomial \(x^2y^3\) is a nonzero socle class. In \(A_f\), the derivative relations give
\[
[f]=[x^4+y^5+x^2y^3]=-\frac1{10}[x^2y^3].
\]
Thus \(N\) has rank exactly one and square zero, so \(\tau=11\), its Jordan lengths are \(2,1,\ldots,1\) (ten ones), and
\[
\tau(F_k)=([z^0]+[z^1])(10+z+z^{-1})^k,
\quad (\tau(F_1),\tau(F_2),\tau(F_3))=(11,122,1363),
\]
\[
\lim_{k\to\infty}\sqrt{k}\,\tau(F_k)/12^k=\sqrt{12/\pi}.
\]
This gives a fully explicit isolated singularity realizing the nontrivial regime.

## Verification
The accompanying standalone `verify.py` performs exact integer coefficient calculations and checks the equality with independently formed finite Kronecker-sum matrices over a large prime for several Jordan block systems and small tensor powers. It checks the plane-curve special values above and the derivative reduction identity. Executing it from the actual packaged file produces `VERIFY_OK`. These computations are finite checks; the arbitrary-\(k\) statement and the asymptotic follow from the algebraic representation argument and the lattice local central limit theorem, respectively.

## Relationship to prior work
Zheng and Zuo, arXiv:2610.08290v1 (2026), Proposition 5.1 and Theorem B, establish the **two-factor** Jordan-block formula for Tjurina numbers and a filtered Thom–Sebastiani defect theorem. Almirón, arXiv:2205.12806v1 (2022; journal version 2023), establishes a two-factor Tjurina formula and bounds. The two-factor results and the standard representation-theoretic and probabilistic tools are prior work, not new assertions here. The present claim is the exact **all-fold tensor-character identity** together with the sharp universal inverse-square-root **large-number-of-summands** law and its explicit plane-curve specialization. No equivalent all-fold asymptotic was found in the inspected material or targeted searches; that negative search is not a proof of historical priority.

## Limitations
The proof is restricted to complex isolated hypersurface germs; it does not yield finite-characteristic asymptotics, general analytic deformations with coupled variables, or filtered Tjurina subspectra. The constant depends on the full nilpotent Jordan partition in general, not only on \(\mu\) and \(\tau\); for plane curves the square-zero property makes those two numbers sufficient. The asymptotic does not bound the ratio uniformly over changing base germs. Independently checking historical novelty remains desirable.

## References
1. S. Zheng and H. Zuo, *Hodge–Tjurina Numbers, Tjurina Spectra, and Thom–Sebastiani Formulas*, arXiv:2610.08290v1 (first posted 2026-10-06), especially Section 5, Proposition 5.1.
2. P. Almirón, *The Tjurina Number for Sebastiani–Thom Type Isolated Hypersurface Singularities*, arXiv:2205.12806v1 (2022), *Mediterranean Journal of Mathematics* 20 (2023), article 258, doi:10.1007/s00009-023-02458-3.
3. J. Briançon and H. Skoda, *Sur la clôture intégrale d’un idéal de germes de fonctions holomorphes en un point de* \(\mathbb C^n\), C. R. Acad. Sci. Paris 278 (1974), 949–951 (classical containment used for plane curves).
4. Classical finite-dimensional \(\mathfrak{sl}_2\) representation theory (Clebsch–Gordan and complete reducibility) and the lattice local central limit theorem.
