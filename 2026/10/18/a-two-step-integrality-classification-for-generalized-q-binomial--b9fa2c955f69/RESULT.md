# A two-step integrality classification for generalized q-binomial ratios

## Finding

For positive integers \(n,k,j\), consider the rational function
\[
G_{n,k}(q,t)=\frac{1-q}{1-tq^{kn}}
\prod_{m=1}^{n}\frac{(1-q^{km})(1-tq^{km})}{(1-q^m)^2},
\qquad H_{n,k,j}(q)=G_{n,k}(q,q^j).
\]
The specialization \(j=2k\) has the **complete polynomiality and coefficient-positivity classification**
\[
\boxed{H_{n,k,2k}(q)\in\mathbb Z[q]
\quad\Longleftrightarrow\quad n\text{ is odd or }k\text{ is even}.}
\]
Whenever the rational function is a polynomial, all its coefficients are nonnegative integers. If \(n\ge2\) is even and \(k\) is odd, it instead has a simple pole at \(q=-1\), with
\[
\boxed{\lim_{q\to-1}(1+q)H_{n,k,2k}(q)=k^{n-1}.}
\]
These conclusions hold for **all** positive integer parameters, with no finite cutoff.

Consequently, the polynomiality criterion proposed for the general \(H_{n,k,j}\) in Straub–Moll–Amdeberhan (2008, Section 5), namely \(\gcd(n,j)\mid k\), is **not necessary**. In this two-step slice, its precise failure locus is
\[
\boxed{k\text{ even and }\nu_2(n)>\nu_2(k).}
\]
In particular, every even positive \(k\), with \((n,j)=(2k,2k)\), gives a counterexample. The smallest such example is \((n,k,j)=(4,2,4)\).

## Assumptions and scope

The variable \(q\) is an indeterminate. Polynomiality means membership in \(\mathbb Z[q]\), rather than formal power-series integrality or numerical integrality at particular \(q\). Parameters \(n,k,j\) are positive integers. Write
\[
[r]_{q^a}=1+q^a+\cdots+q^{a(r-1)}
=\frac{1-q^{ar}}{1-q^a},\qquad r,a\ge1.
\]
Empty products equal one. Theorem assertions concern only the natural two-step specialization \(j=2k\); they do not classify arbitrary \(j\).

## Proof

**1. Telescoping reduction.** Put \(Q_{n,k}(q)=\prod_{m=1}^{n}[k]_{q^m}\). Substitution \(t=q^{2k}\) into the defining formula and cancellation of the shifted factors give the rational-function identities
\[
\begin{aligned}
H_{n,k,2k}(q)
&=\frac{1-q}{1-q^{k(n+2)}}Q_{n,k}(q)^2
\prod_{m=1}^{n}\frac{1-q^{k(m+2)}}{1-q^{km}}\\
&=\frac{(1-q)(1-q^{k(n+1)})}{(1-q^{k})(1-q^{2k})}Q_{n,k}(q)^2\\
&=\boxed{\frac{[n+1]_{q^k}}{[2k]_q}\prod_{m=1}^{n}[k]_{q^m}^{\,2}}.
\end{aligned}
\]
The displayed cancellations are in \(\mathbb Q(q)\) and do not presume polynomiality. For \(n=1\), direct cancellation yields \(H_{1,k,2k}(q)=[k]_q\), a polynomial with nonnegative coefficients.

**2. Factorization for \(n\ge2\).** Set \(R_{n,k}(q)=\prod_{m=3}^n[k]_{q^m}\). The elementary identities
\[
[2k]_q=[k]_q(1+q^k),\qquad
[k]_{q^2}=\frac{[k]_q(1+q^k)}{1+q}
\]
produce
\[
\boxed{H_{n,k,2k}(q)=
\frac{[n+1]_{q^k}\,[k]_q^2\,[k]_{q^2}}{1+q}\,R_{n,k}(q)^2.}
\]
If \(n\ge3\) is odd, then \([n+1]_{q^k}=(1+q^k)[(n+1)/2]_{q^{2k}}\), so the last formula becomes
\[
\boxed{H_{n,k,2k}(q)=
[(n+1)/2]_{q^{2k}}[k]_q[k]_{q^2}^{\,2}
\prod_{m=3}^n[k]_{q^m}^{\,2}.}
\]
Every factor has nonnegative integer coefficients.

If \(k\) is even, then \([k]_q=(1+q)[k/2]_{q^2}\). Thus, for every \(n\ge2\),
\[
\boxed{H_{n,k,2k}(q)=
[n+1]_{q^k}[2k]_q[k/2]_{q^2}^{\,2}
\prod_{m=3}^n[k]_{q^m}^{\,2}.}
\]
Again every factor has nonnegative integer coefficients. This proves both polynomiality branches, including their overlap.

**3. Exact obstruction for even \(n\) and odd \(k\).** In this case \([n+1]_{q^k}|_{q=-1}=1\), \([k]_q|_{q=-1}=1\), and \([k]_{q^2}|_{q=-1}=k\). Precisely \(n/2-1\) indices in \(\{3,\ldots,n\}\) are even; consequently \(R_{n,k}(-1)=k^{n/2-1}\). The numerator in the factorization of step 2 takes the nonzero value \(k^{n-1}\) at \(q=-1\). Division by \(1+q\) therefore gives the claimed simple pole and excludes polynomiality. Together with steps 1–2 this proves the if-and-only-if statement.

**4. Exact disagreement with the earlier predicted criterion.** In the specialization \(j=2k\), elementary prime valuations show that \(\gcd(n,2k)\mid k\) holds exactly when \(\nu_2(n)\le\nu_2(k)\). Every odd prime power dividing \(\gcd(n,2k)\) already divides \(k\), so only the extra factor of two matters. The proved condition is instead \(n\) odd or \(k\) even; the discrepancy is exactly \(k\) even with \(\nu_2(n)>\nu_2(k)\). For example
\[
H_{4,2,4}(q)=[5]_{q^2}[4]_q(1+q^3)^2(1+q^4)^2
\in\mathbb Z_{\ge0}[q],
\]
but \(\gcd(4,4)=4\nmid2\). More generally \(n=j=2k\) with any even \(k\) gives infinitely many counterexamples.

## Verification

The standalone script `VERIFY.py` uses exact integer polynomial arithmetic, without third-party dependencies. It checks the original rational-function numerator–denominator identity against the two factorizations for 48 polynomial instances with \(1\le n,k\le8\), and confirms agreement of the cyclotomic divisor exponents with the classification for 1,800 parameter pairs with \(1\le n\le60\), \(1\le k\le30\). It also tests the simple-pole residue formula algebraically on the small excluded cases. Run `python VERIFY.py`; the expected terminal prefix is `VERIFY_OK`. These checks supplement, but do not substitute for, the universal proof above.

## Relationship to prior work

Straub, Moll and Amdeberhan introduced the generalized rational functions \(G_{n,k}\) and \(H_{n,k,j}\) in Section 5 of their 2008 paper; their Theorem 4.1 concerns the \(j=1\) specialization, whereas their explicitly proposed general criterion \(\gcd(n,j)\mid k\) predicts non-polynomiality for the even-parameter family exhibited here. The present result is an evaluated, complete classification along the natural shifted specialization \(j=2k\), including coefficient positivity and an exact analytic obstruction, rather than a claim about all shifts.

The same conjecture appears again as Problem 14.5.2 in Straub's 2012 dissertation. The available passage corroborates the formulation but was not treated as a full-document exclusion of later results. Searches for aliases, the defining rational function, factorization, and the parameter criterion in a public mathematical research index and publicly searchable literature did not identify an equivalent classification. These searches do not prove uniqueness; a general q-factorial-ratio divisibility theorem or unindexed source could imply the result without matching its terminology.

## Limitations

The theorem applies only to \(j=2k\). It refutes necessity of the published criterion but makes no assertion about sufficiency outside this slice or a corrected global condition. Polynomiality is proved as an exact identity in \(\mathbb Z[q]\), not by finite testing. No independent external scientific audit has been performed; unindexed literature and stronger generalized divisibility theorems remain potential originality risks.

## References

1. A. Straub, V. H. Moll and T. Amdeberhan, *The p-adic valuation of k-central binomial coefficients*, arXiv:0811.2028v1 (first submitted 2008-11-13), Sections 4–5, especially equations (5.3), (5.6), (5.7), and the following Problem. https://arxiv.org/html/0811.2028v1 ; journal version: *Acta Arithmetica* 140 (2009), 31–42, DOI:10.4064/aa140-1-2.
2. A. Straub, *Arithmetic aspects of random walks and methods in definite integration*, Ph.D. dissertation (2012), Section 14.5, Problem 14.5.2 (relevant passage only consulted). https://arminstraub.com/downloads/pub/dissertation.pdf
