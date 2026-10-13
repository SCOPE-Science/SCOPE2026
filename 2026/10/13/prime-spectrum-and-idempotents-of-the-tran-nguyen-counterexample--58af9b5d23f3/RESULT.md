# Prime spectrum and idempotents of the Tran–Nguyen counterexample ring
## Finding
Let \(k=\overline{\mathbb Q}\), \(A=k[x,y,z]\), and let \(X\subset k^3\setminus\{0\}\) be the countable Zariski-dense set in Tran and Nguyen's construction. Put \(\Omega=X\times\mathbb N\), let \(D=k^{(\Omega)}\) be the ring of finitely supported functions, and let \(\iota:A\to k^\Omega\) send a polynomial to its restriction to \(X\), repeated constantly along each fiber \(\{p\}\times\mathbb N\). For
\[
R=\iota(A)+D\subset k^\Omega,
\]
write \(M_\omega=\ker(\operatorname{ev}_\omega:R\to k)\). Then
\[
\operatorname{Spec}R=\{M_\omega:\omega\in\Omega\}\;\sqcup\;\{D+\iota(\mathfrak p):\mathfrak p\in\operatorname{Spec}A\}.
\]
Each \(M_\omega\) is both minimal and maximal and is an isolated clopen point. The ideal \(D\) is the remaining minimal prime, and \(V(D)\cong\operatorname{Spec}A\). Hence
\[
\operatorname{Min}R=\{D\}\cup\{M_\omega:\omega\in\Omega\},\qquad \dim R=3.
\]
The idempotents are exactly
\[
\operatorname{Idem}(R)=\{\chi_F,1-\chi_F:F\subset\Omega\text{ finite}\}.
\]
Thus the irreducible components are the affine three-dimensional component \(V(D)\) and the isolated singleton components \(\{M_\omega\}\), whereas the clopen subsets form only the finite–cofinite Boolean algebra on the isolated points.

## Assumptions and scope
The statement concerns the specific countable reduced non-McCoy ring constructed in arXiv:2610.00116v1. Only two properties of its geometric input are used in the spectrum and idempotent arguments: \(X\) is Zariski dense in \(k^3\), and every point of \(X\) is repeated on an infinite fiber in \(\Omega\). The stronger incidence properties of \(X\) are needed by Tran and Nguyen for the annihilator and \((A_2)\) properties, but not for the classification proved here.

## Proof
First, \(\iota(A)\cap D=0\). If \(\iota(f)\) has finite support and \(f(p)\ne0\) for some \(p\in X\), then \(\iota(f)\) is nonzero at every point of the infinite fiber \(\{p\}\times\mathbb N\), a contradiction. Thus \(f\) vanishes on all of \(X\), and Zariski density gives \(f=0\). Therefore
\[
R/D\cong A.
\]
Every prime containing \(D\) is consequently the inverse image of a unique \(\mathfrak p\in\operatorname{Spec}A\), namely \(D+\iota(\mathfrak p)\).

For \(\omega\in\Omega\), let \(\delta_\omega\in D\) be the coordinate idempotent. Suppose \(P\in\operatorname{Spec}R\) does not contain \(D\). If \(\omega\ne\nu\), then \(\delta_\omega\delta_\nu=0\), so primality implies that at most one coordinate idempotent can lie outside \(P\). At least one must lie outside \(P\), because the \(\delta_\omega\) span \(D\) as a \(k\)-vector space. Hence there is a unique \(\omega\) with \(\delta_\omega\notin P\). From
\[
\delta_\omega(1-\delta_\omega)=0
\]
and primality, \(1-\delta_\omega\in P\). If \(r(\omega)=0\), then \(r\delta_\omega=0\), so
\[
r=r(1-\delta_\omega)\in P.
\]
Thus \(M_\omega\subseteq P\). Evaluation at \(\omega\) maps \(R\) onto \(k\), so \(M_\omega\) is maximal; therefore \(P=M_\omega\). This proves the spectrum decomposition.

The basic open set \(D(\delta_\omega)\) contains only \(M_\omega\), while
\[
V(1-\delta_\omega)=\{M_\omega\}.
\]
Thus \(M_\omega\) is isolated and clopen. It is minimal because no other prime in the displayed classification can lie strictly below it. The ideal \(D\) is prime because \(R/D\cong A\) is a domain, and it is minimal because a prime strictly below \(D\) can be neither a coordinate prime nor the pullback of a nonzero prime of \(A\). The two types of primes are incomparable, so every nontrivial prime chain lies inside \(V(D)\), where it corresponds to a prime chain of \(A\). Since \(\dim A=3\), one obtains \(\dim R=3\).

It remains to classify idempotents. Write \(e=\iota(f)+d\) with \(f\in A\) and \(d\in D\), and assume \(e^2=e\). For any fixed \(p\in X\), the finite support of \(d\) leaves infinitely many \((p,j)\) with \(d(p,j)=0\); hence \(f(p)^2=f(p)\). Therefore \(f(f-1)\) vanishes on the Zariski-dense set \(X\). Since \(A\) is a domain, \(f=0\) or \(f=1\). If \(f=0\), then the finitely supported idempotent \(d\) is \(\chi_F\) for a finite set \(F\). If \(f=1\), then \(d(d+1)=0\) coordinatewise, so \(d=-\chi_F\) for a finite set \(F\), and \(e=1-\chi_F\). Conversely, all of these functions are idempotent. The description of clopen subsets follows from the standard idempotent–clopen correspondence.

## Verification
The prime classification was checked case-by-case against the two exhaustive alternatives \(D\subseteq P\) and \(D\nsubseteq P\). The only uses of the special construction are the quotient identity \(R/D\cong A\), the orthogonal coordinate idempotents in \(D\), the infinite repetition of every \(p\in X\), and Zariski density of \(X\). The dimension conclusion uses only \(\dim k[x,y,z]=3\). The idempotent argument is independent of any finite enumeration.

As a consistency check with the motivating context, Hong–Kim–Lee–Nielsen study the topology of \(\operatorname{Min}(R)\) for rings with annihilator conditions. The present classification exhibits the minimal primes explicitly rather than invoking a compactness criterion.

## Relationship to prior work
Tran and Nguyen define the function-ring template \(R=\Delta B+D\), prove the annihilator formula, construct the required Zariski-dense \(X\subset\mathbb A_k^3\setminus\{0\}\), and obtain a countable reduced ring satisfying the annihilator condition and \((A_2)\) but not \((A_3)\). Their paper does not state a classification of \(\operatorname{Spec}R\), \(\operatorname{Min}R\), the Krull dimension of the example, or its idempotents.

Hong, Kim, Lee, and Nielsen develop general relationships between annihilator conditions and minimal-prime spectra, including compactness criteria. Their results motivate computing \(\operatorname{Min}(R)\) for a new annihilator-condition example, but they predate this construction and do not identify its prime ideals or idempotents. Searches for the specific function-ring construction, its prime spectrum, and finite-support idempotents did not locate a stronger statement implying the displayed classification.

## Limitations
This is a structural theorem about Tran and Nguyen's particular ring, not a classification of all reduced rings satisfying the annihilator condition and \((A_2)\). No claim is made that every ring of the form \(\Delta B+k^{(X\times\mathbb N)}\) has the same dimension or the same quotient component; those depend on \(B\). The literature search cannot rule out an unindexed general theorem about prime spectra of rings with orthogonal-idempotent ideals, although no such source covering this exact conclusion was found.

## References
1. V.-H. Tran and T. M. Nguyen, *A Reduced Non-McCoy Ring with the Annihilator Condition and \((A_2)\)*, arXiv:2610.00116v1, 2026.
2. C. Y. Hong, N. K. Kim, Y. Lee, and P. P. Nielsen, *The Minimal Prime Spectrum of Rings with Annihilator Conditions*, Journal of Pure and Applied Algebra 213 (2009), DOI:10.1016/j.jpaa.2009.01.005.
