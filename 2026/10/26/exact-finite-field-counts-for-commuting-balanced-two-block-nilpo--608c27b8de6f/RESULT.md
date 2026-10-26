# Exact finite-field counts for commuting balanced two-block nilpotents

## Finding

Fix integers \(n\ge3\) and \(q\ge2\), where \(q\) is a prime power of characteristic \(p\). Let \(J_s\) denote the size-\(s\) nilpotent Jordan block over \(k=\mathbb F_q\), and put \(J=J_{n+1}\oplus J_{n-1}\). Define
\[
N_{n,q}=\#\{Y\in M_{2n}(k):YJ=JY,\ Y\text{ nilpotent of Jordan type }(n,n)\}.
\]
Then, writing \(g_-=\gcd(n,q-1)\), \(g_+=\gcd(n,q+1)\), and \(\delta=\mathbf1_{p\nmid n}\),
\[
\boxed{N_{n,q}=q^{4n-8}(q-1)^2\left(q-\frac{g_-+g_+}{2}+\delta\right).}
\]
There are exactly \(q^{4n-4}\) nilpotent matrices commuting with \(J\), so division by this quantity gives the exact conditional density. In particular, the count is zero precisely when the exponent of \(\mathrm{PGL}_2(k)\) divides \(n\), recovering the field-sensitive existence criterion in Britnell--Wildon, Proposition 4.7.

## Assumptions and scope

All matrices and vector spaces are over a finite field \(k=\mathbb F_q\). The theorem counts individual matrices \(Y\) commuting with one fixed representative \(J\), not simultaneous-similarity orbits and not pairs \((J,Y)\) with a varying first member. The nilpotency assumption is essential. The lower bound \(n\ge3\) makes both diagonal first-order coefficients independent parameters; the two-by-two reduction in this form is not asserted for \(n=2\).

## Proof

**Step 1: the centralizer and its free parameters.** Regard the vector space as the \(k[t]\)-module
\[
V=k[t]/(t^{n+1})\oplus k[t]/(t^{n-1}),
\]
where multiplication by \(t\) acts as \(J\). A commuting endomorphism \(Y\) is uniquely a two-by-two polynomial matrix with diagonal entries \(a(t)\pmod{t^{n+1}}\), \(d(t)\pmod{t^{n-1}}\), off-diagonal entries \(t^2b(t)\pmod{t^{n+1}}\) (short-to-long) and \(c(t)\pmod{t^{n-1}}\) (long-to-short). It is nilpotent if and only if \(a(0)=d(0)=0\): modulo the radical of the endomorphism algebra the diagonal constant terms give its two scalar simple factors. Thus \(a\) has \(n\) free coefficients, \(d\) has \(n-2\), and \(b,c\) have \(n-1\) each, for a total of \(4n-4\). In particular the nilpotent centralizer has \(q^{4n-4}\) elements.

**Step 2: a four-parameter Jordan-type criterion.** Let \(\alpha=[t]a(t)\), \(\delta=[t]d(t)\), \(\beta=b(0)\), and \(\gamma=c(0)\), and set
\[
H=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}.
\]
For the standard filtered Jordan basis, all intermediate two-dimensional graded maps induced by \(Y\) are \(H\), while the extreme maps are its first column and first row. The kernel has dimension two exactly when \(H\) is invertible. To see the forward implication, invertible intermediate graded maps prevent a kernel vector from having a nonzero component above the lowest filtration level; in that level, the first row has one-dimensional kernel, together with the bottom Jordan vector. Conversely, singular \(H\) yields a nontrivial kernel vector in the second filtration level; subtracting a suitable vector in the first level produces a third independent kernel vector (if the first row vanishes, the first level already yields at least three). This is the explicit filtration argument given in Britnell--Wildon, Proposition 4.7.

For invertible \(H\), \(Y\) has exactly two Jordan blocks. Also \(Y^{n+1}=0\), because \(Y\) strictly lowers the filtration of length \(n+1\). Therefore only types \((n+1,n-1)\) and \((n,n)\) are possible. On the highest cyclic vector, the coefficient of the lowest Jordan vector in \(Y^n\) is
\[
(1,0)H^{n-2}H^2(1,0)^T=(H^n)_{11}.
\]
Equivalently, compose the first row, \(n-2\) internal maps, and first column, obtaining \((H^n)_{11}\). Hence \(Y\) has type \((n,n)\) if and only if \(H\in\mathrm{GL}_2(k)\) and \((H^n)_{11}=0\). Each choice of \(H\) has exactly \(q^{4n-8}\) lifts from the remaining freely chosen coefficients. It remains to count
\[
T_{n,q}=\#\{H\in\mathrm{GL}_2(k):(H^n)_{11}=0\}.
\]

**Step 3: counting one similarity class at a time.** If \(H^n\) is scalar, its \((1,1)\) entry is nonzero, since \(H\) is invertible; such a class contributes nothing. Otherwise \(H^n\) is nonscalar. In dimension two, every nonscalar matrix has a two-dimensional commutant, and since the commutant of \(H\) is included in that of \(H^n\), the two commutants agree. Thus powering by \(n\) induces a bijection from the conjugacy class of \(H\) onto that of \(H^n\).

For a nonscalar invertible two-by-two matrix \(K\) of characteristic polynomial \(T^2-sT+d\), all members of its similarity class with top-left entry zero are precisely the matrices
\[
\begin{pmatrix}0&u\\-d/u&s\end{pmatrix},\qquad u\in k^\times.
\]
There are therefore exactly \(q-1\) such matrices per class. Consequently, \(T_{n,q}\) is \((q-1)\) times the number of nonscalar similarity classes whose \(n\)-th power remains nonscalar.

**Step 4: classify those classes.** Scalar classes contribute zero. Nonscalar Jordan classes with eigenvalue \(\lambda\in k^\times\) have representatives \(\lambda I+N\), where \(N^2=0\) and \(N\ne0\). Their powers are nonscalar exactly when \(p\nmid n\); this supplies \((q-1)\delta\) classes.

For split semisimple classes with two distinct nonzero eigenvalues \(\lambda,\mu\in k^\times\), the power is nonscalar just when \(\lambda^n\ne\mu^n\). The number of unordered pairs is
\[
\frac{(q-1)(q-1-g_-)}{2},
\]
since each fiber of the \(n\)-th power map on \(k^\times\) has size \(g_-\).

Finally, an irreducible quadratic class has eigenvalues \(\theta,\theta^q\) with \(\theta\in\mathbb F_{q^2}^\times\setminus k^\times\). Its power is scalar precisely when \(\theta^n\in k^\times\). The quotient \(\mathbb F_{q^2}^\times/k^\times\) is cyclic of order \(q+1\), so precisely \((q-1)(g_+-1)\) non-base-field elements have scalar \(n\)-th power. Dividing the remaining \((q-1)(q+1-g_+)\) elements by two for Frobenius pairs yields
\[
\frac{(q-1)(q+1-g_+)}{2}
\]
classes with nonscalar powers.

Adding these contributions, the class count equals
\[
(q-1)\left(q-\frac{g_-+g_+}{2}+\delta\right).
\]
Multiplying once by \((q-1)\) for zero top-left entry and once by \(q^{4n-8}\) for the higher centralizer coefficients proves the formula. Every reduction was valid over arbitrary finite fields, so no parity exception remains. \(\square\)

## Verification

The standalone Python program `check_two_block_commuters.py` uses exact modular arithmetic. It independently exhausts all two-by-two matrices over the prime fields of orders \(2,3,5,7,11\), at eight values of \(n\) per field (40 cases). It also constructs the full polynomial-centralizer matrix directly and exhaustively tests the rank and \(n\)-th power conditions in the cases \((n,q)=(3,2),(3,3),(4,2)\): respectively \(16\) of \(256\), \(648\) of \(6561\), and \(256\) of \(4096\) elements satisfy the theorem. Run `python3 check_two_block_commuters.py` with Python 3. The tests verify finite instances only; the proof above provides all-\(n\), all-prime-power generality.

## Relationship to prior work

Britnell and Wildon (2010), Proposition 4.7, previously proved the exact field-dependent **existence** condition for commuting nilpotent types \((n+1,n-1)\) and \((n,n)\); their filtration and two-by-two power criterion are used explicitly above. The contribution here is the exact number of individual commuting matrices in the balanced class, including its arithmetic dependence on both \(\gcd(n,q-1)\) and \(\gcd(n,q+1)\), and its normalized density. Hua (2023) gives canonical forms for indecomposable commuting nilpotent pairs with two unequal Jordan blocks; its classification is related but does not state the present cardinality formula. This is a claim about a new quantitative refinement, not a claim that the existence condition or the filtration reduction was previously unknown.

## Limitations

No distribution among the remaining Jordan types is claimed. The theorem does not count centralizer-conjugacy orbits and does not assert novelty of general simultaneous-similarity classifications. Published complete orbit parametrizations may support alternate derivations of the same finite-field counts; the priority search was bounded. The numerical verifier treats prime fields and finitely many orders, not all extension fields.

## References

1. John R. Britnell and Mark Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1 (6 January 2010), especially Proposition 4.7 and its proof. https://arxiv.org/abs/1001.0811
2. Jiuzhao Hua, *Canonical forms for a class of pairs of commuting nilpotent matrices under simultaneous similarity*, arXiv:2305.00176v1 (29 April 2023), Theorems 3.1-3.2. https://arxiv.org/abs/2305.00176
