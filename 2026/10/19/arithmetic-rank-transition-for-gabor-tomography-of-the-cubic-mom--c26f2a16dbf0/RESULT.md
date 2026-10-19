# Arithmetic rank transition for Gabor tomography of the cubic moment curve

## Finding

Let \(p\ge5\) be prime, \(G=\mathbb F_p^3\), and \(C=\{(t,t^2,t^3):t\in\mathbb F_p\}\). For the unit vector \(g=p^{-1/2}\mathbf1_C\in\mathbb C^G\), let \(\mathcal L_g\) be the complex-linear map taking a matrix \(H\) to all \(p^6\) Gabor-projector traces \(\operatorname{tr}(H\,\Pi_{u,v}gg^*\Pi_{u,v}^*)\), with \(u,v\in G\) and \(\Pi_{u,v}=M_vT_u\).

**The exact complex rank is**
\[
\operatorname{rank}\mathcal L_g
=p^3\bigl(p(p-1)+1\bigr)-Z_p,
\qquad
Z_p=\begin{cases}p-1,&p\equiv1\pmod3,\\p^2-1,&p\equiv2\pmod3.\end{cases}
\]
In particular, the kernel dimension is \(p^6-p^3(p(p-1)+1)+Z_p\). The theorem also gives an explicit Weyl-operator basis of this entire kernel, not merely its dimension.

Set
\[
D_*=\bigl\{(h,h(2t+h),h(3t^2+3th+h^2)):
 h\in\mathbb F_p^\times,\ t\in\mathbb F_p\bigr\}.
\]
Define the exceptional frequency set
\[
Z=\{(\alpha,0,0):\alpha\in\mathbb F_p^\times\}
\ \cup\ \begin{cases}
\varnothing,&p\equiv1\pmod3,\\
\{(\beta^2/(3\gamma),\beta,\gamma):\beta\in\mathbb F_p,\ \gamma\in\mathbb F_p^\times\},&p\equiv2\pmod3.
\end{cases}
\]
Here every quotient denotes multiplication by a multiplicative inverse in \(\mathbb F_p\). Put \(W_{h,\xi}=M_\xi T_h\). Then an exact complex basis of \(\ker\mathcal L_g\) is
\[
\{W_{h,\xi}:h\in G\setminus(D_*\cup\{0\}),\ \xi\in G\}
\ \cup\ \{W_{0,\xi}:\xi\in Z\}.
\]
For every nonzero shift \(h\in D_*\) and any frequency \(\xi\in G\), the corresponding normalized Weyl direction has singular value \(\sqrt p\) for \(\mathcal L_g\) (with unnormalized output Euclidean norm). There are precisely \(p^4(p-1)\) such directions, although zero-shift directions may have coincident numerical singular values.

## Assumptions and scope

Only **prime fields** of characteristic at least five are included. Addition, subtraction, multiplication, and reciprocals in displayed finite-field coordinates take place modulo \(p\). The character is \(\psi(s)=e^{2\pi i s/p}\); modulation means \((M_vf)(x)=\psi(v\cdot x)f(x)\), and translation means \((T_uf)(x)=f(x-u)\). The domain of \(\mathcal L_g\) is the full complex vector space of \(p^3\)-by-\(p^3\) matrices, not merely matrices of rank one or two. Singular values refer to the Hilbert–Schmidt domain norm and the ordinary Euclidean output norm.

The theorem determines **linear operator-tomography rank and the full Weyl kernel**. Because sparse Gabor windows can have rank-two matrices in this kernel, no assertion of nonlinear pure-state phase-retrieval injectivity is made.

## Proof

**1. Weyl reduction.** The \(p^6\) matrices \(W_{h,\xi}=M_\xi T_h\) are an orthogonal complex basis of matrices on \(\mathbb C^G\), each of Hilbert–Schmidt norm \(p^{3/2}\). Their commutation law gives, for every \((u,v)\in G^2\),
\[
\mathcal L_g(W_{h,\xi})(u,v)
=\psi(\xi\cdot u-v\cdot h)A_g(h,\xi),
\quad A_g(h,\xi)=\langle g,W_{h,\xi}g\rangle.
\]
Distinct Weyl directions therefore yield orthogonal output characters. Each Weyl direction lies in the kernel precisely when \(A_g(h,\xi)=0\), and all other directions contribute rank one. The corresponding singular value is \(p^{3/2}|A_g(h,\xi)|\). No assumption of nonlinear signal recoverability is needed for this linear algebra identity.

**2. Translation intersections.** Directly from the indicator-window definition, up to an immaterial unit-modulus factor depending on convention,
\[
A_g(h,\xi)=p^{-1}\sum_{x\in C\cap(C+h)}\psi(\xi\cdot x).
\]
A nonzero difference of two curve points equals
\[
(t+h,t^2+2th+h^2,t^3+3t^2h+3th^2+h^3)-(t,t^2,t^3),
\]
with its first coordinate \(h\ne0\). Its second coordinate determines \(t\) uniquely because \(2h\ne0\). Thus \(C-C=\{0\}\cup D_*\), \(|D_*|=p(p-1)\), and every \(h\in D_*\) has **exactly one** ordered difference representation. Consequently every frequency has nonzero ambiguity for \(h\in D_*\), with \(|A_g(h,\xi)|=1/p\), and every frequency has zero ambiguity for shifts outside \(\{0\}\cup D_*\). This proves the asserted singular-value band and its \(p^4(p-1)\) Weyl directions.

**3. Cyclotomic criterion at zero shift.** At \(h=0\),
\[
A_g(0,(\alpha,\beta,\gamma))
=p^{-1}\sum_{t\in\mathbb F_p}\psi(\alpha t+\beta t^2+\gamma t^3).
\]
For an arbitrary function \(f:\mathbb F_p\to\mathbb F_p\), let \(n_j\) be the number of solutions of \(f(t)=j\). If \(\sum_t\psi(f(t))=0\), the integer polynomial \(\sum_{j=0}^{p-1}n_jX^j\) vanishes at a primitive \(p\)-th root of unity. By the degree-\(p-1\) minimal polynomial \(1+X+\cdots+X^{p-1}\), its coefficients are all equal. Since their sum is \(p\), each is one. Conversely a permutation clearly has zero sum. Hence the zero-shift ambiguity vanishes **if and only if the polynomial \(\alpha t+\beta t^2+\gamma t^3\) permutes \(\mathbb F_p\)**.

**4. Complete cubic-permutation classification.** A degree-one polynomial permutes precisely when its linear coefficient is nonzero; a genuine quadratic never permutes in odd characteristic. For \(\gamma\ne0\), translating the variable by \(-\beta/(3\gamma)\), scaling the polynomial by \(\gamma^{-1}\), and removing a constant reduce permutation to that of \(t^3+ut\) with
\[
u=\gamma^{-1}\alpha-\frac{\beta^2}{3\gamma^2}.
\]
If \(u=0\), the cubic map permutes precisely when \(\gcd(3,p-1)=1\), i.e. \(p\equiv2\pmod3\). If \(u\ne0\), a collision at two distinct elements \(x,y\) is equivalent, on setting \(s=x+y\), \(v=x-y\ne0\), to
\[
3s^2+v^2=-4u.
\]
For any nonzero right-hand side \(c\), this binary quadratic equation has \(p-\chi(-3)\) solutions, where \(\chi\) is the Legendre character: sum \(1+\chi(c-3s^2)\) over \(s\), and use \(\sum_s\chi(s^2-a)=-1\) for \(a\ne0\). There are at least \(p-1\ge4\) solutions, while at most two have \(v=0\). Thus a solution with \(v\ne0\) exists, so \(t^3+ut\) is not a permutation when \(u\ne0\). This proves that the zero-shift frequencies are exactly \(Z\), with cardinality \(p-1\) or \(p^2-1\) as indicated.

**5. Count and kernel.** Every shift in \(D_*\) contributes \(p^3\) nonzero Weyl directions. At the zero shift, exactly \(p^3-|Z|\) survive. No other shifts survive. The rank is therefore \(p^3p(p-1)+p^3-|Z|\), exactly the stated formula; the complement gives the displayed kernel basis. Subtracting from the domain dimension \(p^6\) gives the claimed nullity.

## Verification

The standalone standard-library program `verify.py` uses exact finite-field arithmetic. It exhaustively enumerates the ordered cubic-curve differences, independently checks the proposed inversion of nonzero differences, detects zero-shift Fourier cancellation via root multiplicities (rather than floating-point near-zeros), and checks cubic-permutation collisions and the final rank formula over all eight primes \(5,7,11,13,17,19,23,29\). Run `python3 verify.py`; the reproduced output is in `verify_output.txt`. Finite checks test the formula at those primes; **the arbitrary-prime proof is the five-step argument above**, not the enumeration.

## Relationship to prior work

Bojarovska and Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (first posted 2015-03-19), establish the Weyl-coordinate approach to finite cyclic Gabor phase-retrieval lifting; their Theorem 2.3 describes full-rank bounds under a nonvanishing ambiguity hypothesis. Alaifari and Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296 (first posted 2019-01-12), develop related discrete ambiguity-function identities and stability questions. These are methodological antecedents. The present theorem concerns a three-dimensional prime-field cubic curve, where the ambiguity function has a large kernel and a previously unevaluated arithmetic zero-shift component.

Related indexed mathematical records give tomography ranks for **hyperbolic quadratic shells** and for **positive rational windows on a one-dimensional prime cycle**. The first has a different support variety and quadratic-character shift geometry; the second assumes a cyclic group of prime order, not \(\mathbb F_p^3\), and does not classify cubic permutation phases. Neither directly supplies this theorem's exact two-regime rank and Weyl kernel. Classical finite-field permutation facts are proved here and are not claimed as new in isolation.

## Limitations

The statement is restricted to prime fields, the full Gabor projector orbit, and linear operator tomography. It does not classify the numerical values of all nonzero cubic exponential sums or the entire singular spectrum at zero shift; it does not prove pure-state phase-retrieval injectivity, recovery stability for the nonzero singular directions, or any statement for nonprime fields. The arithmetic rank formula is derived from known Weyl diagonalization and an elementary but essential prime-field cubic-permutation classification; bibliographic novelty is qualified by the possibility of an unindexed equivalent calculation.

## References

1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (first public preprint 2015-03-19), J. Fourier Anal. Appl. **22** (2016), 542–567, DOI 10.1007/s00041-015-9431-0.
2. R. Alaifari and M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296 (first public preprint 2019-01-12), J. Fourier Anal. Appl. **27** (2021), article 6, DOI 10.1007/s00041-020-09802-1.
