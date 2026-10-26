# Sharp local fiber masses for quadratic characteristic polynomials, including the dyadic cases

## Finding
For every integer pair \(T,D\), prime \(p\), and exponent \(e\ge1\), let \(f(X)=X^2-TX+D\) and count the matrices with characteristic polynomial \(f\) over \(\mathbb Z/p^e\mathbb Z\):
\[
N_e(f;p)=\#\{A\in M_2(\mathbb Z/p^e\mathbb Z):\operatorname{tr}A=T,\ \det A=D\}.
\]
Let \(R_r(f;p)=\#\{x\bmod p^r:f(x)\equiv0\pmod{p^r}\}\). Then the exact finite-level formula is
\[
\boxed{N_e=(p^e-p^{e-1})\left(p^e+\sum_{r=1}^{e}p^{e-r}R_r\right)+p^{e-1}R_e.}
\]
The normalized limit \(\lambda_p(f)=\lim_{e\to\infty}p^{-2e}N_e\) exists and obeys the sharp inequalities
\[
\boxed{1-p^{-1}\le\lambda_p(f)\le1+p^{-1}.}
\]
Equality on the left holds precisely when \(f\) has no root modulo \(p\); equality on the right holds precisely when \(f\) splits over \(\mathbb Q_p\), including repeated factors.

**Odd-prime classification.** Put \(\Delta=T^2-4D\). If \(\Delta\) is a square in \(\mathbb Q_p\) (including zero), then \(\lambda_p=(p+1)/p\). Otherwise let \(v_p(\Delta)=2s\) or \(2s+1\). Respectively,
\[
\boxed{\lambda_p=(p+1)/p-2/p^{s+1},\qquad
\lambda_p=(p+1)/p-(p+1)/p^{s+2}.}
\]

**Dyadic classification.** If \(T\) is odd, then \(\lambda_2=3/2\) for even \(D\), and \(\lambda_2=1/2\) for odd \(D\). If \(T\) is even, put \(c=(T/2)^2-D\). If \(c\) is a square in \(\mathbb Q_2\), including zero, then \(\lambda_2=3/2\). Otherwise write \(c=2^v u\) with \(u\) odd and \(s=\lfloor v/2\rfloor\). Then
\[
\boxed{\lambda_2=\begin{cases}
3/2-2^{-(s+1)},&v\text{ even and }u\equiv5\pmod8,\\
3/2-3/2^{s+2},&\text{otherwise}.
\end{cases}}
\]
This distinguishes the two inequivalent dyadic nonsplit proximity strata.

## Assumptions and scope
All equalities in the matrix definition and the finite formulas are congruences in \(\mathbb Z/p^e\mathbb Z\); no invertibility or squarefreeness is assumed. The limit keeps \(p,T,D\) fixed and lets \(e\) tend to infinity. For a nonzero \(p\)-adic integer \(z\), \(v_p(z)\) is the normalized valuation with \(v_p(p)=1\). The valuation extends uniquely to algebraic extensions of \(\mathbb Q_p\). A quadratic polynomial splits when both roots belong to \(\mathbb Q_p\).

## Proof
Write a matrix as \(\left(\begin{smallmatrix}a&b\\c&T-a\end{smallmatrix}\right)\). Its determinant condition is \(bc\equiv-f(a)\pmod{p^e}\). For a nonzero residue of valuation \(j<e\), the number of ordered pairs \((b,c)\) with product equal to that residue is \((j+1)\varphi(p^e)\). Indeed, if \(v_p(b)=k\le j\), the number of such \(b\) is \(\varphi(p^{e-k})\), and each has exactly \(p^k\) compatible values of \(c\), giving \(\varphi(p^e)\) for each \(k\). For product zero there are \(e\varphi(p^e)+p^e=(e+1)\varphi(p^e)+p^{e-1}\) pairs. Therefore
\[
N_e=\varphi(p^e)\sum_{a\bmod p^e}(1+\min(e,v_p(f(a))))+p^{e-1}R_e.
\]
Using \(\sum_a\min(e,v_p(f(a)))=\sum_{r=1}^e p^{e-r}R_r\) proves the finite identity. In particular,
\[
p^{-2e}N_e=(1-p^{-1})\left(1+\sum_{r=1}^{e}p^{-r}R_r\right)+p^{-e-1}R_e.
\]

Let \(\alpha,\beta\) be the roots of \(f\) in an algebraic closure of \(\mathbb Q_p\). They are integral over \(\mathbb Z_p\). For \(x\in\mathbb Z_p\),
\(v_p(f(x))=v_p(x-\alpha)+v_p(x-\beta)\).
The two integrals of these summands over normalized Haar measure on \(\mathbb Z_p\) agree by Galois symmetry (and trivially if the roots are already in \(\mathbb Q_p\)). If a root \(\alpha\) lies in \(\mathbb Z_p\), its average distance valuation is \(\sum_{j\ge1}p^{-j}=1/(p-1)\). Otherwise choose \(a_0\in\mathbb Z_p\) maximizing \(t=\max_{a\in\mathbb Z_p}v_p(a-\alpha)<\infty\). Compactness and discreteness of the valuation in the quadratic extension ensure existence. The ultrametric inequality and maximality imply for every \(x\in\mathbb Z_p\) that
\[
v_p(x-\alpha)=\min\{v_p(x-a_0),t\}.
\]
Indeed, unequal arguments have the minimum valuation, whereas a cancellation producing a value above \(t\) would contradict maximality. Consequently the integral of this valuation is
\[
H_p(t)=\sum_{j=1}^{\lfloor t\rfloor}p^{-j}+(t-\lfloor t\rfloor)p^{-\lfloor t\rfloor-1},
\qquad H_p(\infty)=1/(p-1).
\]
The nonnegative integer-valued functions \(\min(e,v_p(f(x)))\) increase to \(v_p(f(x))\), and \(\sum_{r=1}^e p^{-r}R_r\) is their integral. Moreover \(p^{-e}R_e\to0\) because the nested zero neighborhoods decrease to the finite zero set of \(f\), of Haar measure zero. Monotone convergence and the integrability just established give
\[
\boxed{\lambda_p(f)=(1-p^{-1})\bigl(1+2H_p(t)\bigr),}
\]
where \(t=\infty\) exactly when \(f\) has a \(p\)-adic root. Since \(H_p(t)\ge0\), with equality precisely when \(t=0\), the lower endpoint is attained exactly when \(f\) has no root modulo \(p\). The upper endpoint corresponds to \(t=\infty\), equivalently to a splitting polynomial. This also proves existence and both sharp bounds.

For odd \(p\), translation by \(T/2\) reduces the root pair to \(\pm\sqrt{\Delta}/2\). If the discriminant is nonsquare with even valuation \(2s\), a closest integer has root-distance exponent \(t=s\), because the unit residue is nonsquare. For odd valuation \(2s+1\), the closest distance is \(t=s+1/2\). Substitution in \(H_p\) gives the stated formulas; square discriminants split.

For \(p=2\), odd \(T\) gives \(f(X)\equiv X^2+X+D\pmod2\). This is split with simple roots for even \(D\), and has no root for odd \(D\). For even \(T\), translation by \(T/2\) gives \(Y^2-c\). If \(c=2^vu\) is nonsquare with odd \(v=2s+1\), closest root-distance exponent is \(t=s+1/2\). If \(v=2s\), the unit \(u\) is square precisely when \(u\equiv1\pmod8\). For \(u\equiv3,7\pmod8\), all odd squares are \(1\pmod8\), so \(v_2(y^2-u)=1\), giving \(t=s+1/2\). For \(u\equiv5\pmod8\), one instead has \(v_2(y^2-u)=2\), hence \(t=s+1\). Here conjugate distances are equal because the root is not in \(\mathbb Q_2\). Substitution yields the two dyadic formulas. All cases, including \(c=0\), are covered.

## Verification
Run \(`python3 matrix_density_verifier.py`\). A direct three-coordinate enumeration independently evaluates \(N_e\) for 500 choices of prime, exponent, trace and determinant, using only integer congruences; these agree with the divisor/root formula. Twenty-two further configurations compare the explicit rational local classification against high-level normalized finite counts, including the repeated-root, split, unramified, ramified, and dyadic cases. The reported check is `CERTIFICATE_OK exact_finite_fibers= 500 local_classification_samples= 22`. The program is finite evidence only; the limit and sharpness follow from the proof above.

## Relationship to prior work
Browning, Gundlach and Sawin (2026), arXiv:2610.18226v1, study global integral matrices of fixed characteristic polynomial and use prime-field Fourier analysis. Guria (2024), arXiv:2410.04632v1, studies smoothed integral counts for quadratic characteristic polynomials and root congruence sums; her theorem does not assert the ramified prime-power fiber classification. Reiner's classical work counts matrices over finite fields, which gives the first congruence level but does not specify general ramified lifts. In particular, finite-field counts together with smooth Hensel lifting settle only the cases with squarefree reduction; the dyadic and non-squarefree strata here are not consequences of those statements alone. The invariant addresses local rather than global integral counting.

## Limitations
No asymptotic formula for globally height-bounded integer matrices is claimed; this is an exact local statement. Finite tests do not certify universal correctness. A broader older treatment of matrix fibers over complete discrete valuation rings or of local quadratic-form representation densities might imply these formulas without using the same terminology; this is an unresolved originality risk. No independent mathematical audit has been performed.

## References
1. T. Browning, F. Gundlach, W. Sawin, *Counting matrices with given characteristic polynomial*, arXiv:2610.18226v1 (first posted 2026-10-13), https://arxiv.org/abs/2610.18226.
2. R. Guria, *Counting 2 by 2 integer matrices with fixed trace and determinant*, arXiv:2410.04632v1 (2024), https://arxiv.org/abs/2410.04632.
3. I. Reiner, *On the number of matrices with given characteristic polynomial*, Illinois Journal of Mathematics 5 (1961), 324–329.
4. F. Sato and Y. Hironaka, *Local densities of representations of quadratic forms over p-adic integers (the non-dyadic case)*, Journal of Number Theory 83 (2000), 106–136. This is adjacent general local-density literature, not a claimed proof of the matrix formulas above.
