# Fixed-dimensional Segre duals: Fibonacci mass and a \(1/\sqrt5\) defect mode

## Finding
For integers \(n\ge2\) and \(1\le a\le b\) with \(a+b=n\), let \(X_{a,b}=\mathbb P^a\times\mathbb P^b\) in its Segre embedding. Then \(X_{a,b}^{\vee}\) is the determinantal variety of \((a+1)\times(b+1)\) matrices of rank at most \(a\); hence \(\operatorname{codim}X_{a,b}^{\vee}=b-a+1\), its dual defect is \(\delta=b-a\), and \(\deg X_{a,b}^{\vee}=\binom{b+1}{a}\). At fixed total dimension \(n\), put \(d_n(a)=\binom{n-a+1}{a}\) for \(1\le a\le\lfloor n/2\rfloor\) and
\[\alpha_n=\frac{5n+2-\sqrt{5n^2+20n+24}}{10}.\]
The successive ratios of \(d_n(a)\) are strictly decreasing. If \(\alpha_n\notin\mathbb Z\), the unique maximizing split is \(a=\lceil\alpha_n\rceil\); if \(\alpha_n\in\mathbb Z\), exactly the adjacent splits \(a=\alpha_n\) and \(a=\alpha_n+1\) tie. Thus every maximizing split has \(\delta/n\to1/\sqrt5\). Moreover
\[\sum_{a=1}^{\lfloor n/2\rfloor}\deg X_{a,n-a}^{\vee}=F_{n+2}-1-\mathbf 1_{n\text{ odd}},\]
where \(F_0=0,F_1=1\). Consequently, if \(M_n\) denotes the largest dual degree among these fixed-dimensional two-factor Segre varieties, then \(\lim_{n\to\infty}M_n^{1/n}=(1+\sqrt5)/2\).\n\n## Assumptions and scope
Work over an algebraically closed field. The Segre embedding is the standard embedding of \(\mathbb P(U)\times\mathbb P(V)\) into \(\mathbb P(U\otimes V)\), with \(\dim U=a+1\), \(\dim V=b+1\), and \(1\le a\le b\). The projective dual \(X^\vee\) is the Zariski closure of tangent hyperplanes. Its dual defect is \(\delta=\operatorname{{codim}}(X^\vee)-1\). Degree is the ordinary projective degree in the dual projective space. The fixed-dimension comparison ranges over unordered nontrivial two-factor splits \(a+b=n\) with \(a\le b\).

## Proof
Identify a hyperplane in \(\mathbb P(U\otimes V)\) with a bilinear form \(A\in U^*\otimes V^*\), equivalently a linear map \(A:U\to V^*\). At a Segre point \([u\otimes v]\), the affine tangent space is \(U\otimes v+u\otimes V\). The hyperplane \(A\) contains that tangent space exactly when \(A(u,-)=0\) and \(A(-,v)=0\). Such nonzero \(u\) and \(v\) exist exactly when \(\operatorname{{rank}}A\le a\). Hence \(X_{a,b}^\vee\) is the determinantal rank-drop locus \(\operatorname{{rank}}A\le a\). Its codimension is \((a+1-a)(b+1-a)=b-a+1\), agreeing with the classical Segre dual-dimension theorem, so \(\delta=b-a\).

On the ambient dual projective space, the universal matrix is a bundle map
\[U\otimes\mathcal O(-1)\longrightarrow V^*\otimes\mathcal O.\]
For the locus where its rank is at most \(a\), the Giambelli--Thom--Porteous formula reduces, because the rank drops by one on the source side, to the Chern class
\[c_{b-a+1}\!\left(V^*\otimes\mathcal O-U\otimes\mathcal O(-1)\right).
\]
Writing \(H=c_1(\mathcal O(1))\), its total Chern class is \((1-H)^{-(a+1)}\), so the coefficient of \(H^{b-a+1}\) is
\[\binom{a+(b-a+1)}{b-a+1}=\binom{b+1}{a}.\]
This is the degree of \(X_{a,b}^\vee\).

Now fix \(n=a+b\) and set \(d_n(a)=\binom{n-a+1}{a}\). Whenever \(a+1\le\lfloor n/2\rfloor\),
\[\frac{d_n(a+1)}{d_n(a)}=
\frac{(n-2a+1)(n-2a)}{(a+1)(n-a+1)}.\]
This ratio is at least one exactly when
\[q_n(a)=5a^2-(5n+2)a+n^2-1\ge0.\]
The two real roots of \(q_n\) are
\[\frac{5n+2\pm\sqrt{5n^2+20n+24}}{10}.\]
The larger root is greater than \(n/2\), so only the smaller root \(\alpha_n\) can occur in the admissible range. Also the successive ratios strictly decrease. Indeed, if \(n=2a+t+2\) with \(t\ge0\), then after clearing the positive denominator, the difference between consecutive ratios is
\[4a^2t+6a^2+4at^2+22at+24a+t^3+10t^2+29t+24>0.\]
Therefore the sequence increases until the ratio crosses one and decreases afterwards. This gives the stated unique maximum, except when \(\alpha_n\) is an integer, when the ratio at \(a=\alpha_n\) equals one and exactly two adjacent terms tie. Since
\[\frac{\alpha_n}{n}\longrightarrow\frac{5-\sqrt5}{10},\]
any maximizing \(a\) satisfies
\[\frac{b-a}{n}=1-2\frac an\longrightarrow\frac1{\sqrt5}.\]

Finally, the classical Fibonacci coefficient identity
\[\sum_{a\ge0}\binom{n-a+1}{a}=F_{n+2}\]
follows directly from Pascal's recurrence. The term \(a=0\) contributes one. If \(n\) is odd, the last term in the full identity has \(a=(n+1)/2>b=(n-1)/2\) and also contributes one; if \(n\) is even there is no such excluded term. This proves
\[\sum_{a=1}^{\lfloor n/2\rfloor}d_n(a)=F_{n+2}-1-\mathbf 1_{n\text{{ odd}}}.\]
If \(T_n\) denotes this sum and \(M_n=\max_a d_n(a)\), then
\[\frac{T_n}{\lfloor n/2\rfloor}\le M_n\le T_n.\]
Binet's formula gives \(T_n^{1/n}\to(1+\sqrt5)/2\), and the polynomial factor \(\lfloor n/2\rfloor\) disappears after taking \(n\)-th roots, proving the last assertion.

## Verification
The bundled script `artifacts/verify.py` uses exact integer arithmetic. It checks, for every \(2\le n\le1000\), the degree sequence, the sign criterion for each successive ratio, strict decrease of the ratios after exact cross-multiplication, the predicted maximizing set, and the Fibonacci total. It also records the first integer-root tie cases. These finite checks are regression tests for the symbolic proof above; they are not substitutes for the all-\(n\) argument.

## Relationship to prior work
Kaji proves the general codimension criterion for duals of Segre varieties and, in the two-factor case, gives \(\operatorname{{codim}}X^\vee=b-a+1\) when \(b>a\); the balanced case is the determinant hypersurface. Fulton gives the Giambelli--Thom--Porteous formula for rank-degeneracy loci, which yields the degree \(\binom{b+1}{a}\) here. Ottaviani--Sodomaco--Ventura study asymptotics of dual degrees for Segre products, emphasizing non-defective hyperdeterminants and other stabilization regimes. The fixed-total-dimension defective/non-defective tradeoff, its exact mode, the limiting defect ratio \(1/\sqrt5\), and the Fibonacci total above were not found in the inspected sources or targeted searches.

## Limitations
The result concerns only two-factor Segre varieties with their standard Segre polarization. The originality assessment is literature-bounded: classical ingredients are known, and an unindexed source could conceivably have combined them in this exact fixed-dimension form. No claim is made about higher-factor Segre products, ED degree, singularity structure of the dual, or finer asymptotics beyond the exponential base for \(M_n\).

## References
1. W. Fulton, *Flags, Schubert polynomials, degeneracy loci, and determinantal formulas*, Duke Math. J. 65 (1992), 381--420. doi:10.1215/S0012-7094-92-06516-1.
2. H. Kaji, *On the Duals of Segre Varieties*, Geom. Dedicata 99 (2003), 221--229. doi:10.1023/A:1024968503486.
3. G. Ottaviani, L. Sodomaco, E. Ventura, *Asymptotics of degrees and ED degrees of Segre products*, Adv. Appl. Math. 130 (2021), 102242. arXiv:2008.11670.
