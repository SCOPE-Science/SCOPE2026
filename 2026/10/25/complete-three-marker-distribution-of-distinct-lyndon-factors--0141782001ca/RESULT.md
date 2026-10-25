# Complete three-marker distribution of distinct Lyndon factors

## Finding

Use the ordered binary alphabet \(0<1\). A Lyndon factor is a nonempty **contiguous** factor strictly smaller than every nontrivial cyclic rotation of itself; distinct factors are counted once regardless of multiplicity. For nonnegative integers \(a,b,c,d\), put
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad m=a+b+c+d,
\]
and let \(L(w)\) denote the number of distinct Lyndon factors of \(w\). Then
\[
\boxed{L(w)=1+\mathbf1_{m>0}+\max(a,b,c)+(a-b)_++(b-c)_++(a-\max(b,c))_++\mathbf1_{a\ge b>c}},
\]
where \(x_+=\max(x,0)\) and each indicator is one when its subscript condition holds, zero otherwise. In particular, this formula includes adjacent ones, empty zero gaps, and the all-one word \(111\).

For every \(m,\ell\ge0\), let \(N_{m,\ell}\) count words with exactly three ones and \(m\) zeros for which \(L(w)=\ell\). The entire bivariate enumerator is the following rational function:
\[
\boxed{\mathcal F(z,y)=\sum_{m,\ell\ge0}N_{m,\ell}z^m y^\ell
=y+\frac{y^2}{1-z}\left(\frac{Q(z,y)}{1-z^3y}-1+z\right)},
\]
where
\[
\begin{aligned}
Q(z,y)={}&1+\frac{z^2(y^3+y^2)}{1-z^2y^2}+\frac{z^2y}{1-z^2y}
+\frac{zy^3}{1-zy^3}+\frac{zy^2}{1-zy^2}+\frac{zy}{1-zy}\\
&+z^3\left[
\frac{(1+y)y^5}{(1-z^2y^2)(1-zy^3)}
+\frac{y^4}{(1-z^2y^2)(1-zy^2)}
+\frac{y^3}{(1-z^2y)(1-zy^2)}\\
&\qquad\qquad+\frac{y^3}{(1-z^2y^2)(1-zy)}
+\frac{y^2}{(1-z^2y)(1-zy)}\right].
\end{aligned}
\]
All these identities hold as formal power series in \(z\) with coefficients in integer polynomials in \(y\).

If \(W_m\) is uniformly sampled from the \(\binom{m+3}{3}\) binary words containing exactly three ones and \(m\) zeros, then \(L(W_m)/m\) converges in distribution as \(m\to\infty\) to a continuous random variable \(X\), satisfying
\[
\boxed{\mathbb E X=\frac{19}{24},\quad
\mathbb E X^2=\frac{37}{45},\quad
\operatorname{Var}(X)=\frac{563}{2880}}.
\]
The complete limiting law is also specified by an equiprobable six-component uniform-simplex mixture in the proof; this is stronger than a moment statement.

## Assumptions and scope

The alphabet is fixed and ordered \(0<1\). Factors are linear, contiguous, nonempty, and different as strings; the Chen–Fox–Lyndon **factorization count** and scattered subsequences are different invariants and are not considered. All four gap parameters are arbitrary nonnegative integers. The finite histogram concerns **labeled linear words**, with no identifications by reversal, cyclic rotation, or complementation. The limiting statement uses uniform sampling within each fixed composition and does not address uniformly sampled unrestricted binary words.

## Proof

**One and two marked symbols.** Any non-singleton binary Lyndon word containing both letters begins with \(0\) and ends with \(1\): a rotation starting at \(0\) excludes a leading \(1\), and a terminal \(0\) would yield a proper suffix \(0\) lexicographically smaller than the word. The singleton factors contribute \(1+\mathbf1_{m>0}\). A mixed Lyndon factor with exactly one \(1\) has the form \(0^i1\) with \(i\ge1\). Such a string occurs exactly when \(i\le\max(a,b,c)\); hence its distinct-string contribution is \(\max(a,b,c)\).

A mixed Lyndon factor containing exactly two \(1\)'s must use either the first two or the last two ones. The possible strings are \(0^i1\,0^b1\), with \(1\le i\le a\), or \(0^i1\,0^c1\), with \(1\le i\le b\). A word \(0^i1\,0^j1\) is Lyndon if and only if \(i>j\): the largest cyclic zero run must start the unique least rotation; equality makes the word a proper square. The two families of qualifying strings do not overlap, since the first has internal gap \(b\), the second gap \(c\), and if \(b=c\) the second family is empty. Their contributions are \((a-b)_+\) and \((b-c)_+\).

**Three marked symbols.** Every mixed factor containing all three ones and ending with \(1\) is \(0^i1\,0^b1\,0^c1\) with \(1\le i\le a\). Its distinct cyclic rotations beginning with zero are ordered by *reverse* lexicographic order of the cyclic zero-gap triples \((i,b,c)\), \((b,c,i)\), and \((c,i,b)\). Therefore it is Lyndon precisely if \(i>\max(b,c)\), or if \(i=b>c\). The all-equal case is periodic and excluded. The number of allowed \(i\)'s is \((a-\max(b,c))_++\mathbf1_{a\ge b>c}\). Adding disjoint one-, two-, and three-one factor families proves the individual-word formula.

**Full distribution.** Set
\[
H(a,b,c)=\max(a,b,c)+(a-b)_++(b-c)_++(a-\max(b,c))_++\mathbf1_{a\ge b>c}.
\]
The generating series \(S(z,y)=\sum_{a,b,c\ge0}z^{a+b+c}y^{H(a,b,c)}\) is obtained by partitioning the nonnegative triples according to their weak order. If all three coordinates equal \(t\), the contribution is \((1-z^3y)^{-1}\). For exactly two equal coordinates, parametrize the smaller gap by \(t\) and the difference by \(r\ge1\). For the six respective relations \(a=b>c\), \(a=c>b\), \(b=c>a\), \(a>b=c\), \(c>a=b\), and \(b>a=c\), the excess exponents in \(H\) over \(t\) are respectively \(2r+1\), \(2r\), \(r\), \(3r\), \(r\), and \(2r\), and the exponents of \(z\) over \(3t\) are respectively \(2r,2r,2r,r,r,r\). These give the six one-denominator terms in \(Q\).

If all coordinates are distinct, write their increasing values as \(t,t+r,t+r+s\), with \(r,s\ge1\). For the orders \(a>b>c\), \(a>c>b\), \(b>a>c\), \(b>c>a\), \(c>a>b\), and \(c>b>a\), the excess of \(H\) over \(t\) is respectively
\[
2r+3s+1,\quad2r+3s,\quad2r+2s,\quad r+2s,\quad2r+s,\quad r+s.
\]
All six have zero-count exponent \(3t+2r+s\). Summing geometric series in \(t,r,s\) gives exactly the five two-denominator terms in \(Q\) (the first two orders share a denominator and combine into \(1+y\)). Thus \(S=Q/(1-z^3y)\), with no overlapping cases.

For \(m=0\), the sole word is \(111\), with \(L=1\). When \(m>0\), the two letters contribute two singleton Lyndon factors. Summing over the unrestricted trailing zero gap \(d\) and carefully separating \(a=b=c=0\) gives
\[
\mathcal F(z,y)=y+\frac{y^2}{1-z}(S-1+z),
\]
as claimed. In particular, \(\mathcal F(z,1)=(1-z)^{-4}\), agreeing with the elementary count \(\binom{m+3}{3}\).

**Limit theorem and moments.** Uniform weak compositions \((a,b,c,d)\) of \(m\) scaled by \(1/m\) converge in distribution to the uniform distribution on the three-dimensional simplex \(\{(A,B,C,D)\ge0:A+B+C+D=1\}\). The indicators in \(L/m\) vanish uniformly. The continuous limit functional is
\[
G(A,B,C,D)=\max(A,B,C)+(A-B)_++(B-C)_++(A-\max(B,C))_+.
\]
Each strict ordering of \(A,B,C\) has limiting probability \(1/6\). On each ordering sector set \(u=\min(A,B,C)\), \(v=\operatorname{med}(A,B,C)-u\), \(s=\max(A,B,C)-\operatorname{med}(A,B,C)\), and \((U,V,W,D)=(3u,2v,s,D)\). Since \(U+V+W+D=1\) and this is an invertible linear transformation of constant Jacobian on each sector, conditional on a sector \((U,V,W,D)\) has the uniform Dirichlet\((1,1,1,1)\) law.

For the six orders listed above, respectively, \(G\) is the scalar product of \((U,V,W,D)\) with the coefficient vectors
\[
\left(\tfrac13,1,3,0\right),\quad
\left(\tfrac13,1,3,0\right),\quad
\left(\tfrac13,1,2,0\right),\quad
\left(\tfrac13,\tfrac12,2,0\right),\quad
\left(\tfrac13,1,1,0\right),\quad
\left(\tfrac13,\tfrac12,1,0\right).
\]
This specifies the **entire law** of \(X\), not merely its moments. For a Dirichlet\((1,1,1,1)\) vector \(T\) and rational vector \(v\),
\[
\mathbb E\langle v,T\rangle=\frac{\sum_i v_i}{4},\qquad
\mathbb E\langle v,T\rangle^2=\frac{(\sum_i v_i)^2+\sum_i v_i^2}{20}.
\]
Averaging over the six sectors gives \(19/24\) and \(37/45\), hence variance \(563/2880\). Boundedness of \(L(W_m)/m\) for \(m\ge1\) allows convergence of these first two moments as well.

## Verification

The standalone `checker.py` separately enumerates all contiguous factors and checks the Lyndon condition by every proper rotation, independently of the gap formula. It checked 1,365 binary three-one words with up to eleven zeros. It also independently expands the rational bivariate formula and compares every coefficient for \(0\le m\le25\) against the complete 23,751-word gap census, including the totals \(\binom{m+3}{3}\). Finally, it recomputes the six Dirichlet-sector rational moment identities using exact fractions. Run `python3 checker.py` in the same directory as this document. These are finite checks; the proof above, rather than extrapolation from tests, supplies the all-length assertions and the distributional limit.

## Relationship to prior work

Saari's 2012 preprint *Lyndon Words and Fibonacci Numbers* (arXiv:1207.4233, first posted 17 July 2012) develops counting distinct Lyndon factors and extremal lower bounds for Lyndon words, especially Fibonacci words. Glen, Simpson and Smyth's *Counting Lyndon Factors* (arXiv:1701.00928, first posted 4 January 2017, journal 2017) determines unrestricted maximum factor counts and unrestricted-alphabet expectations. Their sorted-block extremal argument also covers the fixed-composition maximum for binary words, so **that maximum is not claimed as new**. The present result instead resolves the complete individual-word and bivariate-count distribution on the fixed-weight-three slice and its scaling law; these do not follow numerically from the unrestricted mean or maximum, and no equivalent three-marker formula was found in the inspected works. Bassino, Clément and Nicaud's 2004 investigation of prescribed standard right factors concerns a different factorization statistic.

## Limitations

An earlier equivalent sparse-slice distribution under different notation remains a historical-priority risk; source searches and the inspected literature do not constitute a proof of global novelty. The 2004 full text on fixed standard right factors was not fully available, although its accessible abstract and introduction concern a different object. The result applies to three ones, not general fixed weight or unrestricted random words, and the limiting law is specified by an exact mixture rather than a fully expanded piecewise cubic cumulative distribution function. No external independent mathematical audit has been performed.

## References

1. K. Saari, *Lyndon Words and Fibonacci Numbers*, arXiv:1207.4233 (first posted 17 July 2012), https://arxiv.org/abs/1207.4233.
2. A. Glen, J. Simpson, W. F. Smyth, *Counting Lyndon Factors*, arXiv:1701.00928 (first posted 4 January 2017); Electronic Journal of Combinatorics 24(3), P3.28 (2017), https://arxiv.org/abs/1701.00928.
3. F. Bassino, J. Clément, C. Nicaud, *Lyndon Words with a Fixed Standard Right Factor*, Proceedings of SODA 2004, pp. 653–654, DOI: 10.1145/982792.982891.
