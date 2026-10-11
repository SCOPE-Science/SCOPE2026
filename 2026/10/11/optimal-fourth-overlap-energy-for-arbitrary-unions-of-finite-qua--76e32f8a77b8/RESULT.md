# Optimal fourth-overlap energy for arbitrary unions of finite quadratic-chirp bases

## Finding
For every odd integer \(N\geq3\), let \(\zeta_N=\exp(2\pi i/N)\) and, for \(a,b,x\in\mathbb Z_N\), define the unit vector
\[
 v_{a,b}(x)=N^{-1/2}\zeta_N^{a x^2+b x}\in\mathbb C^N.
\]
For each fixed slope \(a\), the set \(\mathcal B_a=\{v_{a,b}:b\in\mathbb Z_N\}\) is an orthonormal basis. Given \(A\subseteq\mathbb Z_N\), define its **fourth-overlap energy** (the second projective frame potential)
\[
 \Phi_2(A)=\sum_{a,c\in A}\ \sum_{b,d\in\mathbb Z_N}
 |\langle v_{a,b},v_{c,d}\rangle|^4.
\]
For a positive divisor \(m\mid N\), write \(r=m q_m+s_m\), with \(0\le s_m<m\), and set
\[
 C_m(r)=(m-s_m)\binom{q_m}{2}+s_m\binom{q_m+1}{2}.
\]
**Theorem.** For every integer \(1\le r\le N\),
\[
 \boxed{\min_{A\subseteq\mathbb Z_N,\ |A|=r}\Phi_2(A)
 =rN+2\sum_{m\mid N}\varphi(m)C_m(r).}
\]
Every interval of \(r\) consecutive slopes modulo \(N\) attains the minimum. Moreover, **these are not the only minimizers**: the complete equality criterion is that, for every divisor \(m\mid N\), the cardinalities
\[
 n_m(t)=|\{a\in A:a\equiv t\pmod m\}|\quad(t\in\mathbb Z_m)
\]
are either \(\lfloor r/m\rfloor\) or \(\lceil r/m\rceil\). For every slope set, the following is an exact nonnegative deficit identity:
\[
 \boxed{\Phi_2(A)-\min_{|B|=r}\Phi_2(B)
 =2\sum_{m\mid N}\varphi(m)
 \left(\sum_{t\in\mathbb Z_m}\binom{n_m(t)}2-C_m(r)\right).}
\]
In particular the minimum simultaneously optimizes the two-base overlap distribution across all divisors of the cyclic dimension, not just a pairwise coherence bound.

## Assumptions and scope
The dimension \(N\) is odd and at least three; \(A\) is an unordered set of \(r\) distinct residues with \(1\le r\le N\). All chirp vectors have unit Euclidean norm, and the inner product is the standard Hermitian one. The potential counts ordered pairs of all \(rN\) vectors, including the diagonal. The totient satisfies \(\sum_{m\mid g}\varphi(m)=g\) for every positive integer \(g\). No assertion is made for even \(N\), repeated slopes, weighted bases, or optimization over bases outside this prescribed chirp family.

## Proof
**1. Exact cross-basis moment.** For distinct slopes \(a,c\), write \(d=a-c\) and \(g=\gcd(d,N)\). Use modulation indices \(b,e\) and write \(\ell=b-e\). Their inner product, up to conjugation, is the normalized quadratic Gauss sum
\[
 N^{-1}G_N(d,\ell),\qquad G_N(d,\ell)=\sum_{x\in\mathbb Z_N}\zeta_N^{d x^2+\ell x}.
\]
Let \(M=N/g\). Translating the summation index by \(M\) multiplies the sum by \(\exp(2\pi i\ell/g)\), so the sum vanishes unless \(g\mid\ell\). If \(g\mid\ell\), splitting the sum into \(g\) copies gives \(G_N(d,\ell)=gG_M(d/g,\ell/g)\). Since \(M\) is odd and \(d/g\) is invertible modulo \(M\), the change of variables \((x,y)\mapsto(x-y,x+y)\) is invertible, and additive-character orthogonality gives
\[
 |G_M(d/g,\ell/g)|^2
 =\sum_{u,v\in\mathbb Z_M}\zeta_M^{(d/g)uv+(\ell/g)u}=M.
\]
Consequently
\[
 |\langle v_{a,b},v_{c,e}\rangle|^2
 =\begin{cases}g/N,& b\equiv e\pmod g,\\0,&\text{otherwise}.\end{cases}
\]
There are exactly \(N^2/g\) ordered modulation pairs satisfying the congruence; hence
\[
 \sum_{b,e\in\mathbb Z_N}|\langle v_{a,b},v_{c,e}\rangle|^4=g.
\]
For equal slopes the modulation vectors form an orthonormal basis and contribute \(N\) to the potential. It follows that
\[
 \Phi_2(A)=rN+2\sum_{\{a,c\}\subseteq A}\gcd(a-c,N).
\]

**2. Divisor expansion.** The arithmetic identity \(g=\sum_{m\mid g}\varphi(m)\) yields
\[
 \sum_{\{a,c\}\subseteq A}\gcd(a-c,N)
 =\sum_{m\mid N}\varphi(m)
 \sum_{t\in\mathbb Z_m}\binom{n_m(t)}2.
\]
This is an exact identity for every set of distinct slopes; it does not assume balance.

**3. Simultaneous optimality and complete equality cases.** Among \(m\) nonnegative integers summing to \(r\), the sum of pair-collision counts \(\sum_t\binom{n_t}2\) is minimized exactly when the counts differ by at most one, with minimum \(C_m(r)\). Indeed, if \(n_i\ge n_j+2\), replacing \((n_i,n_j)\) by \((n_i-1,n_j+1)\) reduces the sum by \(n_i-n_j-1>0\). Since \(\varphi(m)>0\), the divisor expansion supplies the asserted lower bound and deficit, and equality requires balance for every divisor. The consecutive set \(A=\{0,1,\ldots,r-1\}\pmod N\) has balanced counts in every residue class modulo every \(m\mid N\), so it meets all lower bounds simultaneously. This proves the theorem and its equality characterization, including \(r=1\) and \(r=N\).

## Verification
Run `python check.py` using Python 3's standard library. The script (i) exhaustively checks all nonempty slope subsets in dimensions \(3,5,7,9,11,15\), including the equality criterion; (ii) checks exact congruence-totient formulas on random subsets in further odd dimensions up to \(105\); and (iii) directly computes finite Gauss sums and cross fourth moments in dimensions up to \(21\). The observed summary is `VERIFY_OK exhaustive_nonempty_subsets=35490 equality_cases=5532 randomized_sets=1980 exact_cross_moment_cases=3340 max_gauss_abs_squared_error=7.07e-12 status=PASS`. Numerical Gauss-sum checks have rounding error; the unbounded conclusion is established only by the proof above.

For example, with \(N=45\) and \(r=5\), the optimum is \(253\). The consecutive slopes \(\{0,1,2,3,4\}\) attain it: the pairwise gcd sum is \(14\). More generally, if \(p\) is the smallest prime divisor of \(N\), the optimum equals the ideal mutually-unbiased value \(rN+r(r-1)\) exactly for \(r\le p\): choosing \(r\) consecutive slopes gives pairwise coprime differences, while \(r>p\) forces a repeated residue modulo \(p\).

## Relationship to prior work
Casazza and Fickus, *Fourier Transforms of Finite Chirps* (2006), establish the underlying cyclic chirp Fourier magnitudes and analyze tight frames and maximum pairwise correlation. Their Proposition 5 supplies the essential quadratic Gauss-sum ingredient for odd dimensions but does not state the minimization of the aggregate fourth-overlap energy among an arbitrary number of selected chirp bases, its divisor formula, or its complete balancing equality criterion. Roy and Scott, *Weighted complex projective 2-designs from bases* (2007), give the broader projective-design context and general constraints for unions of bases, but not this arithmetic constrained-family optimum. The present objective is restricted to the specified chirp family; it does not establish optimality among all possible orthonormal-basis collections. The familiar arithmetic balancing method also occurs in distinct Fourier-frame problems, but those results do not directly compute this chirp cross-moment or its optimization.

## Limitations
The Gauss-magnitude calculation uses oddness essentially. Equality is characterized by an arithmetic condition rather than by a canonical list of sets modulo symmetry. This result provides a sharp exact potential only within the quadratic-chirp slope family and does not claim a new global projective-design lower bound. Historical equivalence in less directly indexed finite-chirp or design literature is a residual priority risk.

## References
1. P. G. Casazza and M. Fickus, “Fourier Transforms of Finite Chirps,” *EURASIP Journal on Applied Signal Processing* 2006, article 70204 (public publication date 2006-12-01), DOI: 10.1155/ASP/2006/70204. https://link.springer.com/content/pdf/10.1155/ASP/2006/70204.pdf
2. A. Roy and A. J. Scott, “Weighted complex projective 2-designs from bases: optimal state determination by orthogonal measurements,” *J. Math. Phys.* 48, 072110 (2007), arXiv:quant-ph/0703025 (first submitted 2007-03-03). https://arxiv.org/html/quant-ph/0703025v2
3. I. E. Shparlinski and A. Winterhof, “Constructions of Approximately Mutually Unbiased Bases,” *LATIN 2006*, LNCS 3887, pp. 793–799 (2006), DOI: 10.1007/11682462_72. https://doi.org/10.1007/11682462_72
