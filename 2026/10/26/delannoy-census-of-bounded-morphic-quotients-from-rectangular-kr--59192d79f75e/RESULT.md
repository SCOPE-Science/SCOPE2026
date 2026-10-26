# Delannoy census of bounded-morphic quotients from rectangular Kripke grids to the diamond

## Finding
For positive integers \(a,b\), the number of indexed surjective bounded morphisms from the product of the \(a\)-world and \(b\)-world reflexive chains to the four-world Boolean diamond is
\[
F(a,b)=\sum_{k=2}^{\min(a,b)}(2^k-2)\binom ak\binom bk
=D(a,b)-2\binom{a+b}{a}+1.
\]
Here \(D(a,b)=\sum_k 2^k\binom ak\binom bk\) is a Delannoy number. There are no maps for \(\min(a,b)<2\). In particular, \(F(2,b)=b(b-1)\), \(F(3,b)=b^3-b\), and \(F(n,n)\) for \(n=2,3,4,5,6\) equals \(2,24,182,1180,7142\).

## Assumptions and scope
The source is \(P_{a,b}=\{0,\ldots,a-1\}\times\{0,\ldots,b-1\}\) with coordinatewise ordering, considered as a reflexive, transitive Kripke frame. The target is \(B_2=\mathcal P(\{1,2\})\) ordered by inclusion, with two *distinguished* incomparable middle worlds. A surjective bounded morphism is an order-preserving surjection satisfying \(f(\uparrow x)=\uparrow f(x)\) for every source point. The count is of maps, not of maps modulo automorphisms. Empty source dimensions and non-reflexive accessibility are excluded.

## Proof
An order-preserving map to \(B_2\) consists of the characteristic functions of two upsets. Regard the first coordinate as a row index \(i\) and the second as a column index \(j\). For column \(j\), write \(r_j,s_j\in\{0,\ldots,a\}\) for the first rows where the two respective bits become one; the value \(a\) means that bit is absent from the column. Both threshold sequences are weakly decreasing in \(j\). Set \(m_j=\min(r_j,s_j)\) and \(M_j=\max(r_j,s_j)\).

A surjective bounded morphism maps the least source world to the least target world and the greatest source world to the greatest target world. Its back condition at a world with one positive bit is automatic once the greatest world maps to the top. At a world with no positive bit the back condition asks for extensions of both singleton colours. Consider a maximal zero-coloured world. Its two immediate covers (up one row or right one column) must have the two different singleton colours: any zero world with only one immediate cover cannot reach the two incomparable singleton images through monotonicity, and if the two covers had the same singleton image, the other singleton could never appear above it. Conversely, if every maximal zero has two such differently coloured covers, every zero world has both kinds of extension; thus the back condition holds everywhere.

This condition gives a finite-state normal form. Initially, \(1\le m_0<M_0\le a\); there are exactly two choices of which bit has the smaller threshold. The unequal threshold state \((m,M)\) in a column with \(m>0\) can move to \((m,M')\) with \(m<M'\le M\) (a horizontal plateau of zeros), or to \((m',m)\) with \(0\le m'<m\) (a falling zero boundary, accompanied by switching the singleton colour). After \(m=0\), the state can move to \((0,M')\) with \(0\le M'\le M\), including \((0,0)\). The final column must have \(m=0\); this guarantees the top maps to the top. Every permitted transition realizes the cover condition, and all such maps are obtained uniquely by one initial orientation and one state path. The two orientations never coalesce as maps, even if both thresholds eventually become zero.

For \(0\le m<M\le a\), let \(G_{m,M}(z)\) enumerate completions by number of *additional* columns until a terminal state with \(m=0\). For \(m=0\), counting weakly decreasing threshold sequences gives
\[
G_{0,M}(z)=\frac{1}{(1-z)^{M+1}}.
\]
For \(m>0\), the normal form gives the recurrence
\[
G_{m,M}(z)=z\left(\sum_{v=m+1}^{M}G_{m,v}(z)
 +\sum_{u=0}^{m-1}G_{u,m}(z)\right).
\]
Put \(H_m(z)=\sum_{u=0}^{m-1}G_{u,m}(z)\). Subtracting successive values in the first sum yields
\[
G_{m,M}(z)=\frac{zH_m(z)}{(1-z)^{M-m}},\qquad
H_m(z)=\frac{(1+z)^{m-1}}{(1-z)^{m+1}}.
\]
For completeness, setting \(h_m=(1-z)^mH_m\), its recurrence is \(h_1=(1-z)^{-1}\) and \(h_m=(1-z)^{-1}+z\sum_{u=1}^{m-1}h_u\), which solves to \(h_m=(1+z)^{m-1}/(1-z)\). It follows that
\[
\sum_{b\ge1}F(a,b)z^{b-1}
=2\sum_{M=2}^{a}\frac{(1+z)^{M-1}-1}{(1-z)^{M+1}}.
\]
The expression on the right equals
\[
\sum_{k=2}^{a}(2^k-2)\binom ak\frac{z^{k-1}}{(1-z)^{k+1}}.
\]
Indeed the two expressions are zero when \(a=1\), and their differences between \(a\) and \(a-1\), after multiplication by \((1-z)^{a+1}\), both equal \(2((1+z)^{a-1}-1)\) by the binomial theorem. Extracting the coefficient of \(z^{b-1}\) and using \([z^{b-1}]z^{k-1}(1-z)^{-k-1}=\binom bk\) proves the first formula.

Finally, the standard Delannoy expression is \(D(a,b)=\sum_{k\ge0}2^k\binom ak\binom bk\), and Vandermonde's identity gives \(\sum_k\binom ak\binom bk=\binom{a+b}{a}\). Including the terms \(k=0,1\), the first count becomes \(D(a,b)-2\binom{a+b}{a}+1\), as claimed. Since the summand at \(k=2\) is positive exactly when both dimensions are at least two, the existence threshold follows.

## Verification
The independent Python program `check.py` exhaustively constructs pairs of upsets and tests surjectivity and each upward-cone lifting condition directly for every \(1\le a,b\le5\) (25 source sizes). It separately counts threshold-state paths and Delannoy lattice paths for every \(1\le a\le13\), \(1\le b\le19\) (247 sizes) and checks the diagonal values. Running `python3 check.py` prints `ALL_TESTS_PASS`. These finite tests support but do not establish the unlimited-parameter formulas, which are proved above.

## Relationship to prior work
The semantics and bounded-morphism definition are standard in intuitionistic and modal frame theory, for example in Bezhanishvili's 2006 dissertation. Delannoy paths and chain enumerations in rectangular lattices were studied by Caughman and coauthors (2011), and a distinct relationship of Gödel algebras to Delannoy paths was studied by Codara, D'Antona and Marra (2007). Their general background is not presented as new. The specific exact count of surjective p-morphisms from rectangular chain products to the four-world diamond, including the back condition, is the assertion here. A comparison of the available source material and related indexed results did not identify a statement covering this count.

## Limitations
The theorem does not concern all monotone maps, non-surjective maps, unlabelled source quotients, higher-dimensional chain products, or arbitrary target lattices. Relevant published papers on Delannoy enumerations were accessible in abstract rather than fully in their entirety, leaving possible implicit earlier coverage; no independent scientific audit has been carried out.

## References
- N. Bezhanishvili, *Lattices of intermediate and cylindric modal logics*, University of Amsterdam dissertation, defended 17 March 2006, https://eprints.illc.uva.nl/id/eprint/2049/1/DS-2006-02.text.pdf.
- J. Caughman, C. Dunn, C. Neudauer and M. Starr, *Counting lattice chains and Delannoy paths in higher dimensions*, *Discrete Mathematics* (2011), doi:10.1016/j.disc.2011.04.024.
- P. Codara, O. D'Antona and V. Marra, *Propositional Gödel Logic and Delannoy Paths* (2007), doi:10.1109/FUZZY.2007.4295542.
