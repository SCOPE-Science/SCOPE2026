# Every positive integer occurs infinitely often as a consecutive Stern-polynomial resultant

## Finding

Define the Stern polynomials \(B_n(t)\in\mathbb Z[t]\) by \(B_0(t)=0\), \(B_1(t)=1\), and, for every integer \(n\ge1\),
\[
B_{2n}(t)=tB_n(t),\qquad B_{2n+1}(t)=B_n(t)+B_{n+1}(t).
\]
For \(n\ge1\), let \(D_n=|\operatorname{Res}_t(B_n,B_{n+1})|\), using the ordinary Sylvester resultant with the actual polynomial degrees.

**Resultant classification.** Write \(e_n=\deg B_n\), \(\lambda_n=\operatorname{lc}(B_n)\), and \(c_n=\max(e_n,e_{n+1})\). Then \(D_1=1\), \(|e_n-e_{n+1}|\le1\), and for every \(n\ge1\),
\[
D_{2n}=D_n\lambda_n^{c_n-e_{n+1}},\qquad
D_{2n+1}=D_n\lambda_{n+1}^{c_n-e_n}.
\]
These recursions, together with the defining Stern recurrence, determine the absolute resultant at every index.

**Exact realization and infinite multiplicity.** For every integer \(m\ge1\), set
\[
N_m=\frac{7\cdot4^m+5}{3}.
\]
Then \(N_m\) is an integer and
\[
\boxed{\left|\operatorname{Res}_t(B_{N_m},B_{N_m+1})\right|=m.}
\]
In fact, setting \(a_{m,0}=2N_m\) and \(a_{m,j+1}=4a_{m,j}+1\) for \(j\ge0\), one has \(D_{a_{m,j}}=m\) for every \(j\ge0\). Thus every positive integer occurs infinitely often in the absolute-resultant sequence.

## Assumptions and scope

All indices \(n,m\) are positive integers; \(t\) is an indeterminate. The resultant is computed in \(\mathbb Z\), with the degrees of the two actual, nonzero polynomials. Leading coefficients are positive integers. The theorem concerns the absolute resultant, not its sign. No unproved hypothesis on primes or zeros is used.

## Proof

**1. Boundary values and degree gap.** Induction on the defining recurrence gives \(B_n(0)=1\) for odd positive \(n\) and \(B_n(0)=0\) for positive even \(n\). Hence \(B_n(0)+B_{n+1}(0)=1\). All nonzero Stern polynomials have nonnegative coefficients and positive leading coefficients. If \(e_n\) and \(e_{n+1}\) differ by at most one, the degree pairs at indices \(2n\) and \(2n+1\) are respectively
\[
(e_n+1,\max(e_n,e_{n+1}))\quad\text{and}\quad
(\max(e_n,e_{n+1}),e_{n+1}+1).
\]
Both retain the degree-gap bound. The base pair \((B_1,B_2)=(1,t)\) has degrees \((0,1)\), completing the induction.

**2. Exact resultant recursion.** Put \(A=B_n\), \(C=B_{n+1}\), \(H=A+C\), and write \(a=\deg A\), \(b=\deg C\), \(c=\max(a,b)=\deg H\). By the product property of resultants and the constant-term identity,
\[
|\operatorname{Res}(tA,H)|
=|\operatorname{Res}(t,H)|\,|\operatorname{Res}(A,H)|
=|\operatorname{Res}(A,H)|.
\]
Evaluation at the complex roots of \(A\), with multiplicities (or the corresponding universal polynomial identity), gives
\[
\operatorname{Res}(A,H)=\operatorname{lc}(A)^{c-b}\operatorname{Res}(A,C),
\]
since \(H\equiv C\pmod A\) and the leading-coefficient exponent changes by \(c-b\). This proves the first recursion. Likewise,
\[
|\operatorname{Res}(H,tC)|=|\operatorname{Res}(H,C)|
=\operatorname{lc}(C)^{c-a}|\operatorname{Res}(A,C)|,
\]
where symmetry of the resultant affects only its sign. This proves the second recursion. The base resultant of \((1,t)\) is \(1\), and the recursions preserve positivity, so all consecutive resultants are nonzero.

**3. A degree-tie ray.** Define \(u_0=2\) and \(u_{j+1}=4u_j+1\). Induction yields
\[
u_j=\frac{7\cdot4^j-1}{3}.
\]
We claim that \((B_{u_j},B_{u_j+1})\) has equal degrees \(j+1\), leading coefficients \((1,j+1)\), and \(D_{u_j}=1\). This holds for \(u_0=2\), where \((B_2,B_3)=(t,t+1)\). If the claim holds at \(u_j\), applying the even transformation to the pair gives degrees \((j+2,j+1)\) and leading coefficients \((1,j+2)\). Applying the odd transformation to this new pair, whose first degree is larger, gives an equal-degree pair of degree \(j+2\) with leading coefficients \((1,j+2)\). Both resultant multipliers from step 2 equal \(1\), proving the claim at \(u_{j+1}\).

**4. Every positive integer is attained.** Fix \(m\ge1\) and take \(u_{m-1}\). Its equal-degree pair has leading coefficients \((1,m)\) and resultant magnitude \(1\). One odd transformation, to index \(2u_{m-1}+1\), creates a pair with the second degree larger by one and second leading coefficient \(m\), without changing the absolute resultant. A second odd transformation, to index
\[
4u_{m-1}+3=\frac{7\cdot4^m+5}{3}=N_m,
\]
multiplies the absolute resultant by precisely \(m\). It leaves the second degree larger by one, hence \(D_{N_m}=m\).

**5. Infinitely many occurrences.** For any pair with the second degree exactly one larger, the even transformation produces a degree tie without changing the absolute resultant. For any degree-tie pair, the successive even and odd transformations, i.e. the index map \(v\mapsto4v+1\), preserve both a degree tie and the absolute resultant by step 2. Apply these operations to \(N_m\): the indices \(a_{m,0}=2N_m\) and \(a_{m,j+1}=4a_{m,j}+1\) are strictly increasing and all have absolute resultant \(m\). This proves infinite multiplicity.

## Verification

The accompanying standalone standard-library script `verification/verify.py` constructs each \(B_n\) from its coefficient recurrence, independently computes leading degrees and coefficients by a short binary recursion, and calculates integer Sylvester determinants using exact Bareiss elimination. A successful run compares 259 complete resultants at consecutive indices, checks the explicit values for \(1\le m\le16\), and checks four distinct repeated-value indices for each of those 16 witnesses. The finite replay checks the implementation and example range; the proof above establishes all positive indices.

The first values from the explicit realization are \((m,N_m,D_{N_m})=(1,11,1),(2,39,2),(3,151,3),(4,599,4),(5,2391,5)\).

## Relationship to prior work

Ulas and Ulas (2011) proved that consecutive Stern polynomials are coprime over \(\mathbb Q[t]\) (Corollary 2.6) and established related identities. Their coprimality statement determines only whether the resultant vanishes, not its absolute integer size. Gawron (2014) determined degree-equality patterns. Schinzel's *The Leading Coefficients of Stern Polynomials* (2016) concerns a complementary arithmetic invariant; its full text was not available for comparison. Dilcher and Tomkins (2018) studied factorization, square classes, and divisibility of the same polynomial family. The new assertion here is the complete binary resultant recursion and especially the explicit infinite attainment of **every** positive integer as an absolute resultant.

## Limitations

The result gives absolute values, not a signed closed formula. Divisibility of an integer resultant by a prime does **not** by itself imply that the reduced polynomials have a common root over a finite field, because leading degrees may fall on reduction. For example, \(B_{39}(t)\equiv t+1\pmod2\) and \(B_{40}(t)\equiv t^3\pmod2\) remain coprime although \(D_{39}=2\). A specialized leading-coefficient chapter could contain stronger overlapping formulas not evident from its accessible abstract, and equivalent coverage in other literature remains possible. No assertion about every finite-field common zero is made.

## References

1. M. Ulas and O. Ulas, *On certain arithmetic properties of Stern polynomials*, arXiv:1102.5109v1 (first posted 2011-02-24), especially Theorem 2.5 and Corollary 2.6.
2. M. Gawron, *A note on the arithmetic properties of Stern Polynomials*, arXiv:1401.3553v1 (2014-01-15).
3. A. Schinzel, *The Leading Coefficients of Stern Polynomials*, in *From Arithmetic to Zeta-Functions* (2016), doi:10.1007/978-3-319-28203-9_25.
4. K. Dilcher and H. Tomkins, *Square Classes and Divisibility Properties of Stern Polynomials*, *Integers* 18 (2018), article A29.
