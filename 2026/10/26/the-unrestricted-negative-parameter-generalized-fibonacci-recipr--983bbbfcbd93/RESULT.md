# The unrestricted negative-parameter generalized Fibonacci reciprocal-tail floor

## Finding

For integers \(s>t\ge1\) with \((s,t)\ne(2,1)\), let \(U_0=0\), \(U_1=1\), and \(U_{j+2}=sU_{j+1}-tU_j\) for all integers \(j\ge0\). For every pair of integers \(n,r\ge1\), the positive tail \(S_{n,r}=\sum_{k=n}^{\infty}1/U_{rk}\) converges and obeys

\[\boxed{\left\lfloor S_{n,r}^{-1}\right\rfloor=U_{rn}-U_{r(n-1)}-1.}\]

The result resolves the *first* identity of Conjecture 4.6 of Amdeberhan, Chen, Moll and Sagan without a largeness hypothesis. It makes no assertion about their separate reciprocal-square identity.

## Assumptions and scope

The parameters \(s,t,n,r\) are integers satisfying \(s>t\ge1\), \((s,t)\ne(2,1)\), and \(n,r\ge1\). This is the specialization \(f_j(s,-t)\) in the source papers. The excluded degenerate pair \((2,1)\) would give \(U_j=j\) and a divergent harmonic tail; its exclusion implies \(s\ge3\). All terms \(U_j\) with \(j\ge1\) are strictly positive. Both \(n=1\) and \(r=1\) are included, as are \((s,t)=(3,2)\) and parameter pairs with \(t=s-1\).

## Proof

Put \(\lambda=\sqrt{s^2-4t}\), \(\alpha=(s+\lambda)/2\), and \(\beta=(s-\lambda)/2\). Since \(1\le t\le s-1\), we have \(\lambda\ge s-2>0\), \(\alpha\ge s-1\ge2\), and \(0<\beta\le1\). Binet's identity is

\[U_j=\frac{\alpha^j-\beta^j}{\lambda}.\]

Write \(A=\alpha^r\ge2\), \(B=\beta^r\in(0,1]\), \(S=\sum_{k=n}^{\infty}1/U_{rk}\), and \(D=U_{rn}-U_{r(n-1)}\). Thus

\[S=\lambda\sum_{k=n}^{\infty}\frac1{A^k-B^k},\qquad D=\frac{A^{n-1}(A-1)+B^{n-1}(1-B)}{\lambda}.\]

The displayed expression for \(S\) proves convergence: its terms are eventually bounded by a constant times \(A^{-k}\). Define the geometric comparator

\[G=\lambda\sum_{k=n}^{\infty}A^{-k}=\frac{\lambda A^{1-n}}{A-1}.\]

Since \(0<B<A\), the correction \(E=S-G\) is strictly positive, and \(G^{-1}=A^{n-1}(A-1)/\lambda\le D\). It follows that \(S^{-1}<D\).

For every \(k\ge n\), the exact difference of summands is

\[\frac1{A^k-B^k}-\frac1{A^k}=\frac{(B/A^2)^k}{1-(B/A)^k}.\]

Because \(0<B/A<1\), replacing the denominator by \(1-B/A\) and summing a geometric series gives

\[0<E\le \frac{\lambda(B/A^2)^n}{(1-B/A^2)(1-B/A)}.\]

Moreover \(S>G>0\), so \(G^{-1}-S^{-1}=E/(GS)<E/G^2\). Direct substitution yields

\[0<G^{-1}-S^{-1}<\frac{(A-1)^2 A B^n}{\lambda(A^2-B)(A-B)}.\]

Subtracting \(S^{-1}\) from \(D\) therefore gives the uniform error estimate

\[0<D-S^{-1}<\frac{B^{n-1}}{\lambda}\left(1-B+\frac{(A-1)^2AB}{(A^2-B)(A-B)}\right).\tag{1}\]

For fixed \(A\ge2\), the function \(h(B)=(A-1)^2AB/((A^2-B)(A-B))\) is strictly increasing on \(0<B\le1\): its numerator increases and both positive denominator factors decrease. Consequently

\[0<h(B)\le h(1)=\frac A{A+1}<1.\]

We separate the only small-discriminant case. If \((s,t)\ne(3,2)\), then \(\lambda\ge2\): this follows from \(\lambda\ge s-2\) when \(s\ge4\), and \(\lambda=\sqrt5\) for \((s,t)=(3,1)\). Since \(B^{n-1}\le1\), estimate (1) is strictly below \(2/\lambda\le1\). For \((s,t)=(3,2)\), one has \(\lambda=1\), \(\beta=1\), hence \(B=1\), and (1) is strictly below \(A/(A+1)<1\). In all cases,

\[D-1<S^{-1}<D.\]

Finally \(D\) is an integer, proving \(\lfloor S^{-1}\rfloor=D-1\) for every permitted \(s,t,n,r\). \(\square\)

## Verification

A standalone standard-library program `verify.py` independently generates \(U_j\) from the integer recurrence and sandwiches each infinite reciprocal tail between exact rational bounds. It checks all \(7600\) quadruples with \(3\le s\le18\), \(1\le t<s\), \(1\le r\le5\), and \(1\le n\le10\). The lower bound sums a finite prefix; the upper bound adds a rigorous geometric tail, using \(U_{r(k+1)}> (s-1)^r U_{rk}\). The verifier checks \(1/D<S<1/(D-1)\) when \(D>1\), and \(1/D<S\) if \(D=1\). It reports `VERIFY_OK` after all exact-fraction checks. The finite test is independent corroboration, not the proof of the universal statement.

## Relationship to prior work

Amdeberhan, Chen, Moll and Sagan formulated the same all-parameter statement as the first part of Conjecture 4.6, with \(f_j(s,-t)\) notation [1]. Park's Theorem 18 proved that statement only when \(s,t\) are sufficiently large [2, Section 3]. The proof above closes that explicit parameter gap and supplies a quantitative comparator inequality, rather than merely a new special case.

Holliday and Komatsu [3], as quoted in Park's Theorem 16, analyzed the positive-second-coefficient recurrence. Kuhapatanakul [4] also assumes \(V_{j+1}=aV_j+bV_{j-1}\) with \(a,b>0\), so its floor and alternating-tail results do not imply the negative-second-coefficient statement. Yuan, He and Zhuo [5] treat higher reciprocal powers in the negative-coefficient case, principally the cubic power, and do not give this uniform first-power identity. The very different Fibonacci fifth-power and cubic reciprocal-tail results recorded in a mathematical research index concern other exponents and parameters; no implication of this first-power all-parameter claim was found. An equivalent argument in unlocated literature remains a residual originality risk.

## Limitations

Only the first reciprocal-power identity in Conjecture 4.6 is proved. The separate reciprocal-square conjecture, arbitrary signed/complex recurrence parameters and higher-order sequences are not addressed. Novelty is assessed against the checked sources, not certified by absence of search results. No independent mathematical audit has been performed.

## References

[1] T. Amdeberhan, X. Chen, V. H. Moll and B. E. Sagan, *Generalized Fibonacci polynomials and Fibonomial coefficients*, arXiv:1306.6511, first posted 2013-06-27, Conjecture 4.6. https://arxiv.org/abs/1306.6511

[2] S. Park, *Arithmetic properties of generalized Fibonacci sequences*, arXiv:1407.8086, first posted 2014-07-30, Section 3, Conjecture 2 and Theorem 18. https://arxiv.org/abs/1407.8086

[3] S. H. Holliday and T. Komatsu, *On the sum of reciprocal generalized Fibonacci numbers*, Integers 11 (2011), 441–455. https://doi.org/10.1515/integ.2011.031

[4] K. Kuhapatanakul, *On the sums of reciprocal generalized Fibonacci numbers*, Journal of Integer Sequences 16 (2013), Article 13.7.1. https://cs.uwaterloo.ca/journals/JIS/VOL16/Kuhapatanakul/kuha4.pdf

[5] P. Yuan, Z. He and J. Zhuo, *On the Sum of Reciprocal Generalized Fibonacci Numbers*, Abstract and Applied Analysis 2014, Article 402540. https://doi.org/10.1155/2014/402540
