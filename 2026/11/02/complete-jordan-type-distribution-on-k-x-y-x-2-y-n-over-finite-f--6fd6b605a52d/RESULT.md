# Complete Jordan-type distribution on \(k[x,y]/(x^2,y^n)\) over finite fields

## Finding
Let \(n\ge2\) and \(A_n=k[x,y]/(x^2,y^n)\). For every field \(k\) of positive characteristic \(p\), the Jordan block partition of multiplication by **every** element of \(A_n\) is determined by two truncated \(y\)-adic valuations and the characteristic, without reference to any other coefficients. Over a finite field \(k=\mathbb F_q\), this gives the complete exact distribution of the partitions realized by the \(q^{2n}\) multiplication operators. The theorem includes nonlinear, nonhomogeneous elements, not only linear forms.

Write an arbitrary element uniquely as \(f=\lambda+a(y)+xb(y)\), where \(\lambda\in k\), \(a(y)\in yk[y]/(y^n)\), and \(b(y)\in k[y]/(y^n)\). Set \(\alpha=\operatorname{ord}_y a\in\{1,\ldots,n\}\) and \(\beta=\operatorname{ord}_y b\in\{0,\ldots,n\}\), with the valuation of zero defined as \(n\). Put \(r_0=2n\). For each integer \(t\ge1\), define
\[
 u_t=\min(n,t\alpha),\qquad
 v_t=\begin{cases}n,&p\mid t,\\\min(n,(t-1)\alpha+\beta),&p\nmid t,\end{cases}\qquad
 d_t=\min(u_t,v_t),
\]
\[
 r_t=2n-\min(n,d_t)-\min(n,2u_t-d_t).
\]
Then \(r_t\) is exactly the rank of the \(t\)-th power of the nilpotent multiplication map \(N=m_{f-\lambda}\). We have \(r_{n+1}=r_{n+2}=0\). The number of blocks of size exactly \(t\) is
\[
 c_t(\alpha,\beta)=r_{t-1}-2r_t+r_{t+1}\qquad(1\le t\le n+1).
\]
The complete finite-field Jordan-type counting polynomial is
\[
 \mathcal J_{n,q}(z_1,\ldots,z_{n+1})
 =q\sum_{\alpha=1}^{n}\sum_{\beta=0}^{n}
 w_\alpha w_\beta\prod_{t=1}^{n+1}z_t^{c_t(\alpha,\beta)},\qquad
 w_j=\begin{cases}(q-1)q^{n-j-1},&j<n,\\1,&j=n.\end{cases}
\]
A coefficient counts precisely the elements whose multiplication operator has the indicated multiset of Jordan block sizes (with its scalar eigenvalue allowed to vary). All occurring partitions and their exact multiplicities follow from this finite formula, and \(\mathcal J_{n,q}(1,\ldots,1)=q^{2n}\).

For \(n\ge3\), there is a sharp characteristic-dependent top-stratum law. If \(p\nmid n\), the partition \((n+1,n-1)\) occurs exactly when \(\alpha=1,\beta=0\) and has multiplicity \((q-1)^2q^{2n-2}\); the partition \((n,n)\) occurs exactly when \(\alpha=1,\beta\ge1\) and has multiplicity \((q-1)q^{2n-2}\). If \(p\mid n\), the first partition is absent and \((n,n)\) occurs exactly for \(\alpha=1\), with multiplicity \((q-1)q^{2n-1}\). In particular, multiplication by \(x+y\) has type \((n+1,n-1)\) when \(p\nmid n\), and \((n,n)\) when \(p\mid n\).

## Assumptions and scope
The ground field has positive prime characteristic; no perfection assumption is required for the valuation formula. Counting statements require a finite field of cardinality \(q\). Multiplication means the regular representation of the commutative associative algebra on its underlying \(2n\)-dimensional vector space. Every multiplication map has the sole eigenvalue \(\lambda\), since the augmentation ideal is nilpotent. The Jordan partition is therefore that of the nilpotent part \(m_{f-\lambda}\). These are *actual elements* counted individually, not conjugacy or automorphism orbits. Throughout \(p\mid t\) means divisibility of the integer \(t\) by the field characteristic.

## Proof
First, the maximal ideal \((x,y)\) has nilpotence index \(n+1\); hence \(N^{n+1}=0\). Since \(x^2=0\), the binomial theorem gives the exact identity
\[
 (a+xb)^t=a^t+t\,x a^{t-1}b
\]
for all positive integers \(t\), with the integer coefficient interpreted in \(k\). Use the free rank-two \(R=k[y]/(y^n)\)-module basis \((1,x)\). Multiplication by this element has matrix
\[
 \begin{pmatrix}a^t&0\\t a^{t-1}b&a^t\end{pmatrix}.
\]
Over the principal ideal domain \(k[y]\), the first Smith valuation is the minimum of the truncated valuations of the entries, namely \(d_t\); the second is \(2u_t-d_t\) after truncation modulo \(y^n\). To see the formula even when a diagonal entry becomes zero modulo \(y^n\), lift each polynomial to \(k[y]\), apply elementary row and column operations to its two-by-two matrix, then cap each invariant-factor exponent at \(n\). If the diagonal is zero, the surviving off-diagonal entry yields one invariant factor and the other exponent is capped at \(n\). Each factor \(y^j\) acting on \(k[y]/(y^n)\) has rank \(n-\min(n,j)\). Adding the two ranks proves the displayed formula for \(r_t\).

For a nilpotent Jordan block of size \(s\), the rank of its \(t\)-th power is \(\max(s-t,0)\); taking a second finite difference gives exactly the number \(c_t=r_{t-1}-2r_t+r_{t+1}\) of blocks of size \(t\). This proves that no coefficient beyond the two valuations affects the partition. For \(j<n\), exactly \((q-1)q^{n-j-1}\) elements of \(k[y]/(y^n)\) have valuation \(j\), while the zero element has valuation \(n\). The \(q\) possible constants and independent \(a,b\) choices prove the counting polynomial.

For the top-stratum law, both asserted partitions have exactly two blocks, so their first-power rank is \(2n-2\). If \(\alpha\ge2\), then \(u_1\ge2\); when \(\beta=0\), the rank formula gives \(r_1\le2n-\min(n,4)\le2n-3\), and when \(\beta\ge1\), it gives \(r_1\le2n-3\) as well. Therefore any asserted top partition forces \(\alpha=1\). If \(\alpha=1\), then \(a=y\) times a unit, and \(a^t\) has valuation \(t\) for \(t<n\). If \(\beta=0\), the off-diagonal entry of the \(n\)-th power is \(n x a^{n-1}b\), nonzero precisely when \(p\nmid n\); the rank sequence then yields \((n+1,n-1)\). Otherwise the \(n\)-th power vanishes, the rank sequence yields \((n,n)\), and these cases are exhaustive. The valuation-cell counts above give the stated multiplicities.

## Verification
The supplied standalone `checker.py` independently constructs the original multiplication matrices in the monomial basis, takes all matrix powers, and computes every rank by finite-field Gaussian elimination. It exhaustively enumerates all nilpotent parts \(a+xb\) for eleven configurations, including genuine extension fields \(\mathbb F_4\) and \(\mathbb F_9\), and verifies the full Jordan histogram with the free constant multiplier \(q\). The test configurations include dimensions \(n=2,3,4,5\) and characteristics \(2,3,5\). Run `python checker.py`; the reference output is in `checker_output.txt`, ending in `JORDAN_MULTIPLICATION_VALUATIONS_OK 11_EXHAUSTIVE_CONFIGURATIONS`. These finite checks do not prove the infinite theorem; the preceding Smith-form argument does.

For example, when \(n=3,q=3\), the partition \((3,2,1)\) occurs exactly \(108\) times; it arises from nonlinear multiplication by \(x+y^2\) and does not arise from any linear form in \(x,y\). When \(n=3,q=2\), the top partition \((4,2)\) occurs \(16\) times. The nonlinear example illustrates why the full-element census is not a reformulation of the classical linear-form problem.

## Relationship to prior work
Glasby, Praeger and Xia (2014) classify modular Jordan partitions for tensor products of Jordan blocks; the corresponding linear-form multiplication on a truncated polynomial algebra is a substantial antecedent. Iarrobino, Macias Marques and McDaniel (2018) develop general Jordan-type strata of Artinian algebras and consider nonlinear as well as linear elements; their qualitative framework and examples are prior work, not new here. Altafi, Iarrobino and Khatami (2018) classify possible Jordan partitions of *linear forms* in height-two complete intersections under the stated characteristic restrictions. The specifically assessed contribution is the exact all-element, all-\(n\), all-positive-characteristic, finite-field *multiplicity distribution*, including its valuation uniformity and sharp modular top-stratum transition. No claim is made that the general notion of Jordan type, linear-form tensor partitions, or small nonlinear examples are new.

## Limitations
The theorem treats the particular monomial complete intersections \(k[x,y]/(x^2,y^n)\), rather than arbitrary height-two complete intersections or other coefficient rings. It supplies multiplicities of Jordan partitions, not orbit classification under algebra automorphisms. The finite checker exhausts only the stated finite configurations. Historical publication priority has not been independently certified; an unlocated general enumeration theorem might imply some or all counts. Independent mathematical review has not been performed.

## References
1. S. P. Glasby, C. E. Praeger, B. Xia, *Decomposing modular tensor products, and periodicity of Jordan partitions*, arXiv:1401.2748v1 (public 2014-01-13), https://arxiv.org/abs/1401.2748.
2. A. Iarrobino, P. Macias Marques, C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383 (2018), https://arxiv.org/abs/1802.07383.
3. N. Altafi, A. Iarrobino, L. Khatami, *Complete intersection Jordan types in height two*, arXiv:1810.00716 (2018), https://arxiv.org/abs/1810.00716.
