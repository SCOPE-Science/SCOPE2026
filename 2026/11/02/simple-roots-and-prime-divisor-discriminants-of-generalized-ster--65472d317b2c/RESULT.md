# Simple roots and prime-divisor discriminants of generalized Stern polynomials

## Finding

For each integer \(t\ge2\), define the generalized Stern polynomials by
\[
A_{t,0}(X)=0,\quad A_{t,1}(X)=1,\quad
A_{t,2m}(X)=A_{t,m}(X^t),\quad
A_{t,2m+1}(X)=X A_{t,m}(X^t)+A_{t,m+1}(X^t)
\]
for integers \(m\ge1\). Every nonconstant polynomial in this family has only simple complex zeros, including every parameter \(t\ge3\) not covered by the classical simple-root theorem.

More precisely, write \(n=2^r u\) with \(u\) odd. For any index \(n\ge1\) with \(d=\deg A_{t,n}>0\) and every prime divisor \(p\mid t\),
\[
\boxed{\nu_p(\operatorname{Disc}(A_{t,n}))=r\,d\,\nu_p(t).}
\]
In particular, if \(n\) is odd and \(A_{t,n}\) is nonconstant, its discriminant is a unit at every prime dividing \(t\). If \(n\) is a power of two, then \(A_{t,n}=1\) and it has no zeros; the displayed formula is asserted only for positive degree.

An exact refinement (in absolute value) is, for \(D=\deg A_{t,u}>0\),
\[
\bigl|\operatorname{Disc}(A_{t,n})\bigr|
=t^{rDt^r}\bigl|\operatorname{Disc}(A_{t,u})\bigr|^{t^r}.
\]

## Assumptions and scope

The indices \(n\) and parameters \(t\) are positive integers with \(t\ge2\). Discriminants are the usual integer discriminants of monic polynomials, and \(\nu_p\) is the exponent of a rational prime \(p\) in a nonzero integer. Every \(A_{t,n}\) for \(n\ge1\) is monic with constant coefficient \(1\): the recursion preserves these properties because the two summands at odd indices occupy disjoint residue classes \(0\) and \(1\) modulo \(t\). The only constant polynomials in the positive-index family are those with \(n\) a power of two.

## Proof

**Step 1 (consecutive coprimality over every field).** For any field \(K\), show inductively that \(A_{t,m}\) and \(A_{t,m+1}\) are coprime in \(K[X]\) for all \(m\ge1\). The base pair is \((A_{t,1},A_{t,2})=(1,1)\). Write \(U=A_{t,m}(X^t)\) and \(V=A_{t,m+1}(X^t)\). If the original pair is coprime, a Bézout identity survives substitution \(X\mapsto X^t\), so \(\gcd(U,V)=1\). The two successor pairs are
\[
(A_{t,2m},A_{t,2m+1})=(U,XU+V),\qquad
(A_{t,2m+1},A_{t,2m+2})=(XU+V,V).
\]
Their entries remain coprime. Strong induction proves the assertion.

**Step 2 (odd-index discriminant units).** Fix any prime \(p\mid t\) and any odd index \(n=2m+1\ge3\). Differentiate the defining recurrence and reduce over \(\mathbb F_p[X]\). Because \(p\mid t\),
\[
A'_{t,2m+1}(X)\equiv A_{t,m}(X^t)\pmod p.
\]
The polynomial itself is \(X A_{t,m}(X^t)+A_{t,m+1}(X^t)\). By Step 1, these two polynomials have no common factor over \(\mathbb F_p\). Thus the reduction of the monic odd-index polynomial is separable, and its integer discriminant is nonzero modulo \(p\). As this holds for every \(p\mid t\),
\[
\gcd\bigl(\operatorname{Disc}(A_{t,2m+1}),t\bigr)=1.
\]
In particular, the odd-index polynomial is squarefree in characteristic zero.

**Step 3 (even indices and exact valuations).** Iterate the even-index recursion to obtain
\[
A_{t,2^r u}(X)=A_{t,u}(X^{t^r}).
\]
Let \(f=A_{t,u}\) have degree \(D>0\), set \(T=t^r\), and put \(g(X)=f(X^T)\). The roots of \(f\) are nonzero because \(f(0)=1\), and distinct by Step 2. The roots of \(g\) are their \(T\)-th roots, so they too are distinct over characteristic zero.

For any monic separable \(f\in\mathbb Z[X]\) of positive degree \(D\) with nonzero constant coefficient, the elementary resultant calculation from \(g'=TX^{T-1}f'(X^T)\) gives
\[
\bigl|\operatorname{Disc}(f(X^T))\bigr|
=T^{DT}\,|f(0)|^{T-1}\,|\operatorname{Disc}(f)|^T.
\]
This follows also by partitioning the roots of \(g\) into the \(T\) roots lying above each root of \(f\). Substituting \(f(0)=1\), \(T=t^r\), and \(d=DT\) yields
\[
\bigl|\operatorname{Disc}(A_{t,n})\bigr|
=t^{rd}\bigl|\operatorname{Disc}(A_{t,u})\bigr|^{t^r}.
\]
For \(p\mid t\), Step 2 makes the final factor a \(p\)-adic unit. Hence \(\nu_p(\operatorname{Disc}(A_{t,n}))=rd\nu_p(t)\), as required. The case \(n=2^r\) has polynomial \(1\), so is vacuous.

## Verification

A standalone Python/SymPy checker (included as `verify.py`) independently reconstructs the defining recursion and computes discriminants exactly. The executed finite check covered \(t\in\{2,3,4,5,6,8,9\}\), positive-degree indices \(3\le n\le43\) with polynomial degree at most \(65\), 113 polynomials, 124 prime-divisor valuations, and 74 odd-index modular separability comparisons. It reported:

`CHECK_OK t_values=7 squarefree_polynomials=113 valuations=124 odd_mod_prime_checks=74`

These are finite checks; the proof above supplies the universal quantifiers.

## Relationship to prior work

Dilcher and Ericksen introduced the general parameter family in *Hyperbinary Expansions and Stern Polynomials* (2015), equations (1.2)–(1.3), and established its coefficient structure. Their earlier *Reducibility and irreducibility of Stern (0,1)-polynomials* (2014), Proposition 19 and Proposition 20, already proves simple zeros and odd-index discriminant parity for **the specialization \(t=2\)**; that part is not claimed as new.

Their *Factors and Irreducibility of Generalized Stern Polynomials* (2015), Section 5, gives a cyclotomic-square-factor exclusion only for two special index families (Proposition 5.1) and a multiple-root exclusion for certain \(2^{k+1}\pm1\) indices under arithmetic restrictions on the parameter (Proposition 5.4). These do not imply the all-index, all-parameter discriminant valuation law above. The new method is consecutive-polynomial coprimality followed by reduction at **each prime divisor of \(t\)**, which removes the paper's restrictions even at parameters such as \(t=8\), \(t=9\), and \(t=25\).

## Limitations

The result proves separability in characteristic zero and fixes only the valuations at primes dividing the parameter. It does not determine the complete integer discriminant or its valuations at primes outside \(t\), the splitting fields, or individual root locations. No claim is made that the known \(t=2\) subcase is novel. Equivalent coverage in another publication not located by the searches remains possible.

## References

1. K. Dilcher and L. Ericksen, *Hyperbinary Expansions and Stern Polynomials*, Electronic Journal of Combinatorics **22** (2015), P2.24; first public date 2015-05-14. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p24/pdf/
2. K. Dilcher and L. Ericksen, *Factors and Irreducibility of Generalized Stern Polynomials*, Integers **15** (2015), A50; published 2015-12-11. https://www.maths.tcd.ie/EMIS/journals/INTEGERS/papers/p50/p50.pdf
3. K. Dilcher and L. Ericksen, *Reducibility and irreducibility of Stern (0,1)-polynomials*, Communications in Mathematics **22** (2014), 77–102. https://dml.cz/bitstream/handle/10338.dmlcz/143908/ActaOstrav_22-2014-1_7.pdf
