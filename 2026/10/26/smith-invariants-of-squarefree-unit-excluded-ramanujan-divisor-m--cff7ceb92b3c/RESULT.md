# Smith invariants of squarefree unit-excluded Ramanujan divisor matrices

## Finding

Let \(n\) be a squarefree positive integer with \(r=\omega(n)\ge2\) distinct prime factors, and put \(h=2^{r-1}\). Index rows and columns by the set \(P_n=\{d:d\mid n,\ d>1\}\) of all divisors other than one (including \(n\)). The *Ramanujan divisor matrix with the unit removed* is the \((2^r-1)\)-square integral matrix \(K_n=(c_d(e))_{d,e\in P_n}\), where

\[
c_d(e)=\sum_{k\mid\gcd(d,e)}k\mu(d/k)
\]

is the classical Ramanujan sum and \(\mu\) is the Möbius function. Then the complete Smith normal form over \(\mathbb Z\), with positive invariant factors in divisibility order, is

\[
\boxed{\operatorname{SNF}(K_n)=\operatorname{diag}(\underbrace{1,\ldots,1}_{h},\underbrace{n,\ldots,n}_{h-2},n\varphi(n)).}
\]

In particular,

\[
\operatorname{coker}(K_n)\cong (\mathbb Z/n\mathbb Z)^{h-2}\oplus\mathbb Z/(n\varphi(n))\mathbb Z,
\]

and for every positive integer \(m\), the number of vectors \(x\in(\mathbb Z/m\mathbb Z)^{2^r-1}\) satisfying \(K_nx\equiv0\pmod m\) is exactly

\[
\boxed{\gcd(n,m)^{h-2}\gcd(n\varphi(n),m).}
\]

The one-prime squarefree boundary is different: for \(n=p\) prime, \(K_p=[p-1]\).

## Assumptions and scope

The theorem applies to every squarefree \(n\) with at least two distinct prime factors; neither primality restrictions such as \(2\mid n\) nor constraints on pairwise differences are imposed. Row and column order is arbitrary and does not affect the Smith invariants. The index set omits \(1\) but *includes* \(n\), so this is the principal minor of the full divisor-indexed matrix obtained by deleting the unit row and column. The Smith normal form is taken over the integers, not over a field. The notation \(\varphi(n)\) denotes Euler's totient function.

## Proof

**Integral incidence reduction.** Index all vectors by \(P_n\) in divisibility-compatible order. Define integer matrices \(H=(\mu(d/k)\mathbf1_{k\mid d})_{d,k\in P_n}\), \(Z=(\mathbf1_{k\mid e})_{k,e\in P_n}\), and the diagonal matrix \(D=\operatorname{diag}(d)_{d\in P_n}\). Both incidence matrices are triangular with ones on the diagonal, hence unimodular. Set \(u=(\mu(d))_{d\in P_n}\) and let \(\mathbf1\) be the all-ones column. The divisor expression for Ramanujan sums gives

\[
K_n=HDZ+u\mathbf1^T.
\]

Because \(\sum_{k\mid d,\ k>1}\mu(k)=-1\) for \(d>1\), Möbius inversion yields \(H^{-1}u=-\mathbf1\). Similarly, \(\mathbf1^TZ^{-1}=-u^T\). Thus the integral Smith form of \(K_n\) equals that of the much simpler rank-one perturbation

\[
B=H^{-1}K_nZ^{-1}=D+\mathbf1u^T.
\]

**Determinant.** Since \(n\) is squarefree, each prime divisor of \(n\) occurs in exactly \(h\) members of \(P_n\). Therefore \(\det D=n^h\). The matrix determinant lemma and the identity \(\sum_{d\mid n}\mu(d)/d=\varphi(n)/n\) give

\[
\det B=n^h\left(1+\sum_{d\in P_n}\frac{\mu(d)}d\right)=n^{h-1}\varphi(n).
\]

In particular the matrix is nonsingular.

**Primes not dividing \(n\).** Let \(\ell\nmid n\). The diagonal \(D\) is invertible over \(\mathbb F_\ell\), so the rank-one perturbation \(B\) has kernel dimension at most one modulo \(\ell\). The determinant formula shows that among its positive \(\ell\)-adic Smith exponents, there is at most one, necessarily \(v_\ell(\varphi(n))\) when positive.

**Primes dividing \(n\).** Fix \(p\mid n\). Partition the index set into \(A=\{d\in P_n:p\nmid d\}\) of size \(h-1\), and \(T=\{d\in P_n:p\mid d\}\) of size \(h\). For a column \(x\), write \(t=u^Tx\). The congruence \(Bx=0\pmod p\) reads \(t=0\) on all rows indexed by \(T\), then \(d x_d+t=0\) for \(d\in A\). Hence the right kernel modulo \(p\) is exactly

\[
X=\{x:x_A=0,\ \sum_{d\in T}\mu(d)x_d=0\},\quad \dim X=h-1.
\]

Likewise the left kernel of \(B\) is exactly

\[
Y=\{y:y_A=0,\ \sum_{d\in T}y_d=0\},\quad\dim Y=h-1.
\]

Use the following elementary first-order Smith principle. For any nonsingular integral matrix whose left and right kernels modulo \(p\) are \(Y\) and \(X\), the bilinear form

\[
\beta(y,x)=\frac{y^TBx}{p}\pmod p,\qquad y\in Y,\ x\in X,
\]

computed with arbitrary integer lifts, is well-defined. Its rank is exactly the number of positive \(p\)-adic Smith exponents equal to \(1\). Indeed changing a lift by a multiple of \(p\) leaves the quotient unchanged modulo \(p\) because the opposite vector belongs to a kernel; after invertible row and column operations over the localization \(\mathbb Z_{(p)}\), the assertion is immediate for a diagonal Smith matrix: \(p\) contributes one and any higher power contributes zero.

For the present \(B\), the rank-one term in \(y^TBx=(y^TDx)+(\mathbf1^Ty)(u^Tx)\) is divisible by \(p^2\) for \(x\in X\), \(y\in Y\). Therefore \(\beta\) is the restriction to two hyperplanes of the nondegenerate weighted diagonal pairing

\[
\beta(y,x)=\sum_{d\in T}(d/p)y_dx_d\pmod p.
\]

Each \(d/p\) is a unit modulo \(p\), by squarefreeness. In a vector space of dimension \(h\), restricting an invertible diagonal pairing to two hyperplanes leaves radical dimension at most one: the annihilator of either hyperplane under a nondegenerate form is one-dimensional. Thus \(\operatorname{rank}\beta\ge h-2\). Since \(\dim X=h-1\), at least \(h-2\) of the \(h-1\) positive \(p\)-adic Smith exponents equal \(1\), with at most one greater than \(1\). Their sum equals

\[
v_p(\det B)=h-1+v_p(\varphi(n)).
\]

Consequently their multiset is \(\{1\text{ repeated }h-2\text{ times},\ 1+v_p(\varphi(n))\}\), including when the last exponent equals one.

**Global assembly.** Every prime \(p\mid n\) divides exactly \(h-1\) Smith invariant factors; their local exponents are as just found. Every prime \(\ell\nmid n\) divides at most the largest invariant factor, to exponent \(v_\ell(\varphi(n))\). Uniqueness of the ordered integer Smith chain therefore yields \(h\) units, \(h-2\) copies of \(n\), and one copy of \(n\varphi(n)\). The cokernel decomposition follows from Smith normal form, and the congruence-kernel formula follows by counting solutions to one scalar congruence for each invariant factor. This proves the theorem.

## Verification

The included `verify.py` independently computes the gcd-divisor Ramanujan sums, both incidence matrices and the unimodular equivalence, and then computes exact integer Smith forms using SymPy for 46 squarefree integers. It includes the cases \(n=6\), \(n=30\), and \(n=210\), whose Smith lists are respectively \((1,1,12)\), \((1,1,1,1,30,30,240)\), and eight ones followed by six copies of \(210\) and \(10080\). Execute `python verify.py`; successful execution prints `VERIFY_OK`. This finite check supports, but does not replace, the preceding proof for every squarefree \(n\).

## Relationship to prior work

Ramanujan sums and their use as spectra of integral circulant graphs are classical. Sander and Sander (2011, 2015) study divisor-indexed Ramanujan eigenvalues and associated spectral injectivity/energy problems. Schlage-Puchta (2021) considers the full divisor-indexed Ramanujan-sum matrix and establishes a nonzero determinant via divisor manipulations. The principal deletion of the unit row and column changes the integral cokernel: the full matrix's diagonal incidence reduction does not supply the reduced matrix's Smith invariant factors. The theorem here derives those factors, including their precise prime-power allocation, for all squarefree integers. Comparison of the accessible literature did not uncover this particular reduced integral classification; it does not prove absolute priority.

## Limitations

The explicit invariant factors are proved only for squarefree \(n\); non-squarefree moduli are not classified. The result concerns a specific unit-excluded principal matrix, not arbitrary principal minors or graph adjacency matrices. Earlier unindexed or inaccessible work could contain an equivalent formula. The finite verification uses SymPy for exact Smith forms and is not evidence of the universal statement without the proof above.

## References

1. J. W. Sander and T. Sander, *Integral circulant graphs of prime power order with maximal energy*, arXiv:1112.3205v1 (first public version: 14 December 2011), https://arxiv.org/abs/1112.3205.
2. J. W. Sander and T. Sander, *On So's conjecture for integral circulant graphs*, Applied Analysis and Discrete Mathematics **9** (2015), 59–72, DOI:10.2298/AADM150226009S.
3. J.-C. Schlage-Puchta, *A determinant involving Ramanujan sums and So's conjecture*, Archiv der Mathematik **117** (2021), 379–384, DOI:10.1007/s00013-021-01643-8.
