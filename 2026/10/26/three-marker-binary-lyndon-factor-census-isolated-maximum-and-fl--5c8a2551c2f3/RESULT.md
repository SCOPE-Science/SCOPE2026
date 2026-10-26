# Three-marker binary Lyndon-factor census, isolated maximum, and fluctuation law

## Finding

For a finite word, let \(L(w)\) be its number of **distinct nonempty Lyndon factors** (contiguous substrings that are primitive and strictly lexicographically smaller than every nontrivial cyclic rotation). The alphabet is ordered \(0<1\). For every binary word with exactly three ones write uniquely

\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0},\qquad m=a+b+c+d.
\]

Let \(x_+=\max(x,0)\) and let \(\mathbf1_E\) be the indicator of condition \(E\). If \(m\ge1\), then

\[
\boxed{L(w)=2+\max\{a,b,c\}+(a-b)_++(b-c)_++(a-\max\{b,c\})_++\mathbf1_{\{a\ge b>c\}}.}
\tag{1}
\]

The exceptional all-one word \(111\) has \(L(111)=1\).

Let \(S_m\) sum \(L(w)\) over all \(\binom{m+3}{3}\) binary words of length \(m+3\) with three ones. The exact aggregate generating function is

\[
\boxed{\sum_{m\ge0}S_mz^m=
\frac{1+11z+4z^2+3z^3-z^4+z^5+2z^6-3z^7+z^8}
{(1-z)^5(1+z)(1+z+z^2)}.}
\tag{2}
\]

Its initial coefficients, starting at \(m=0\), are \(1,14,44,106,215,391,655,1034,1555,2251\). The exact mean at each finite length is \(S_m/\binom{m+3}{3}\).

For every \(m\ge1\), the minimum of \(L\) is \(2\), attained only by \(1110^m\), and the maximum is \(3m+2\), attained only by \(0^m111\). For every \(m\ge4\), the second-largest attainable value is \(3m-1\), attained by precisely \(0^{m-1}1110\) and \(0^{m-1}1011\). In particular, for every \(m\ge4\), no word attains \(3m\) or \(3m+1\): the unique maximum is separated from the rest by a gap of three.

If \(W_m\) is uniformly sampled from the \(\binom{m+3}{3}\) length-\(m+3\) words of weight three, then

\[
\boxed{\mathbb E[L(W_m)]=\frac{19}{24}m+O(1),\qquad
\operatorname{Var}(L(W_m))=\frac{563}{2880}m^2+O(m).}
\tag{3}
\]

More exactly, \(L(W_m)/m\) converges in distribution to the explicit random variable

\[
F(A,B,C)=\max\{A,B,C\}+(A-B)_++(B-C)_++(A-\max\{B,C\})_+,
\]

where \((A,B,C,D)\) is uniform on the three-dimensional probability simplex \(A+B+C+D=1\) with nonnegative coordinates (Dirichlet\((1,1,1,1)\)). This is a nonconstant limiting law, with mean \(19/24\) and variance \(563/2880\).

## Assumptions and scope

All words are linear, not cyclic, and factors are contiguous, not scattered. Distinct factors are counted once regardless of occurrence multiplicity. The total order is \(0<1\); changing that order changes the answer. The exact results apply for every integer \(m\ge0\), with the boundary \(m=0\) handled separately. The limiting statements concern uniform sampling conditional on exactly three ones, as the number of zeros tends to infinity. No assertion is made about positive-density, arbitrary-alphabet, or unrestricted-composition words.

## Proof

**1. Classification by the number of ones.** A binary non-letter Lyndon word begins in \(0\) and ends in \(1\). Indeed, if it began in \(1\) while containing \(0\), a rotation beginning with \(0\) would be smaller; if it ended in \(0\), its proper suffix \(0\) would be smaller, contradicting the standard suffix characterization of Lyndon words.

The one-letter factors contribute \(1\) if \(m=0\), and \(2\) otherwise. A factor with exactly one \(1\) is Lyndon exactly when it is \(0^i1\) with \(i\ge1\). Its possible leading-zero lengths are precisely \(1\le i\le\max(a,b,c)\), so the one-one contribution beyond the letters is \(\max(a,b,c)\).

A factor with exactly two ones that can be Lyndon has form \(0^i1\,0^j1\) with \(i\ge1\), and its two zero runs satisfy \(i>j\): if \(i<j\), rotation to the longer zero run decreases the word; if \(i=j\), it is a square. Such factors use either the first and second ones (\(j=b,\ 0\le i\le a\)), or the second and third ones (\(j=c,\ 0\le i\le b\)). They contribute respectively \((a-b)_+\) and \((b-c)_+\). There is no duplication between these lists: when \(b\ne c\) their internal gaps distinguish them; when \(b=c\), the second list is empty.

A factor containing all three ones must be \(0^i1\,0^b1\,0^c1\) for \(0\le i\le a\). To be the strictly smallest rotation, its initial zero run must be at least as long as either following run. If \(i>\max(b,c)\), it is strictly smallest. Among tied maxima, precisely \(i=b>c\) is still strictly smallest: comparing the two rotations beginning in the equal longest zero runs, the original has the longer next zero run. The cases \(i=c>b\) and \(i=b=c\) are excluded by the competing rotation (equality in the latter case implies nonprimitivity). Consequently the all-three-ones contribution is \((a-\max(b,c))_+ +\mathbf1_{\{a\ge b>c\}}\). Summing the disjoint one-count classes proves (1).

**2. Exact finite enumeration.** The contribution from the letter count is \(2/(1-z)^4-1\), since the zero-gap quadruples have generating function \((1-z)^{-4}\), with the all-one word contributing only one. The remaining contributions of the four terms in (1), summed over all nonnegative gap quadruples and weighted by \(z^{a+b+c+d}\), are respectively

\[
H_M(z)=\frac{1}{(1-z)^4}\left(\frac{3z}{1-z}-\frac{3z^2}{1-z^2}+\frac{z^3}{1-z^3}\right),
\]
\[
H_P(z)=\frac{2z}{(1-z)^4(1-z^2)},
\qquad
H_T(z)=\frac{z}{(1-z)^4}\left(\frac{2}{1-z^2}-\frac{1+z}{1-z^3}\right),
\]
\[
H_I(z)=\frac{z^2}{(1-z)^2(1-z^2)(1-z^3)}.
\]

For \(H_M\), expand \(\max(a,b,c)=\sum_{j\ge1}\mathbf1_{\{\max(a,b,c)\ge j\}}\) and apply inclusion-exclusion to three bounded zero gaps. For \(H_P\), write \(a=b+r\) or \(b=c+r\) with \(r\ge1\) and sum \(\sum_{r\ge1}rz^r=z/(1-z)^2\). For \(H_T\), likewise write \(a=\max(b,c)+r\) and use

\[
\sum_{b,c\ge0}z^{b+c+\max(b,c)}
=\frac{1}{1-z}\left(\frac{2}{1-z^2}-\frac{1+z}{1-z^3}\right).
\]

For \(H_I\), the indicator condition is parametrized by \(b=c+r\), \(a=b+s\), with \(r\ge1\), \(s\ge0\); the fourth gap is free. Thus \(G=2/(1-z)^4-1+H_M+H_P+H_T+H_I\), which simplifies algebraically to (2).

**3. Extremes and isolation.** For \(m\ge1\), (1) immediately gives \(L\ge2\), and equality requires \(a=b=c=0\). Let \(Q=L-2\). If \(a\ge b,c\), the formula reduces to \(Q=3a-b-c+\delta\), with \(\delta=\mathbf1_{\{a\ge b>c\}}\). Hence

\[
3m-Q=4b+4c+3d-\delta.
\]

This vanishes exactly at \((a,b,c,d)=(m,0,0,0)\). Otherwise, for \(m\ge4\), it is at least three, and equality holds exactly at \((m-1,0,0,1)\) and \((m-1,1,0,0)\). If instead \(b>a\) and \(b\ge c\), then \(Q=2b-c\le2m<3m-3\) for \(m\ge4\). In all remaining cases \(c\) is a largest run and \(Q=c+(a-b)_+\le a+c\le m<3m-3\). These inequalities prove the asserted extrema and runner-up classification. For \(m=1,2,3\), the maximum is still unique by the same case analysis or direct boundary substitution; the second-place classification is asserted only for \(m\ge4\).

**4. Limit law and exact leading moments.** The uniform zero-gap quadruple with sum \(m\), divided by \(m\), converges to uniform measure on the simplex. Formula (1), after division by \(m\), converges uniformly on the lattice (up to a bounded \(O(1/m)\) term) to \(F\), proving the distributional limit. The function \(F\) is bounded, piecewise linear, and Lipschitz on this compact simplex, so the first two lattice moments have \(O(1/m)\) errors relative to the limiting moments.

Set \(S=A+B+C\). The Dirichlet aggregation property gives \(S\sim\operatorname{Beta}(3,1)\), independent of \((A,B,C)/S\sim\operatorname{Dirichlet}(1,1,1)\), with \(\mathbb E S=3/4\), \(\mathbb E S^2=3/5\). For the latter three-component vector, let its sorted values be \(X\le Y\le Z\), and put \(u=Y-X\), \(v=Z-Y\). Then

\[
X=\frac{1-2u-v}{3},\quad Y=\frac{1+u-v}{3},\quad Z=\frac{1+u+2v}{3},
\]

and \((u,v)\) has constant density \(4\) on \(u\ge0,\ v\ge0,\ 2u+v\le1\). On the six equally likely assignments of these sorted values to the three named coordinates, \(F/S\) is one of the six linear forms

\[
\frac{1+4u+8v}{3}\ (\text{twice}),\quad
\frac{1+4u+5v}{3},\quad
\frac{1+u+5v}{3},\quad
\frac{1+4u+2v}{3},\quad
\frac{1+u+2v}{3}.
\]

The elementary integrals give \(\mathbb Eu=1/6\), \(\mathbb Ev=1/3\), \(\mathbb Eu^2=\mathbb Euv=1/24\), \(\mathbb Ev^2=1/6\). Averaging the six forms and their squares yields conditional moments \(19/18\) and \(37/27\). Therefore

\[
\mathbb EF=\frac34\cdot\frac{19}{18}=\frac{19}{24},\qquad
\mathbb EF^2=\frac35\cdot\frac{37}{27}=\frac{37}{45},\qquad
\operatorname{Var}(F)=\frac{37}{45}-\left(\frac{19}{24}\right)^2=\frac{563}{2880}.
\]

The \(O(1/m)\) relative lattice-moment errors, and the bounded exceptional indicator in (1), yield (3).

## Verification

The standalone, dependency-free `check.py` directly enumerates all binary words with three ones at lengths \(3\) through \(20\), tests each distinct factor by comparing it to every nontrivial rotation, and checks (1) for **5,985** words. It separately enumerates all \(23,751\) gap quadruples of zero sum at most \(25\), verifies the rational generating-function coefficients through \(m=25\), and tests the isolated maximum and runner-up classification. It also verifies the exact rational first and second simplex moments from the six linear forms. Run `python3 check.py`. All checks passed. The infinite proof is the symbolic argument above, not the finite experiments.

## Relationship to prior work

Saari's *Lyndon Words and Fibonacci Numbers* (first public arXiv posting July 17, 2012) establishes the Lyndon-factor framework and sharp universal lower bounds for words that themselves are Lyndon, as well as results for Fibonacci and recurrent words. It does not give a fixed-content census for arbitrary words with exactly three ones. Glen, Simpson, and Smyth's *Counting Lyndon Factors* (first public preprint January 4, 2017) develops unrestricted-alphabet extremal and expectation formulas, and formulas for Christoffel words; in particular its unconditional expected distinct-factor count is **not** the conditional weight-three mean and does not determine the gap law (1), the isolated maximum, or (2)–(3). These published results are credited, not claimed here. The exact conditional enumeration and asymptotic moments are not supplied by the inspected sources; an earlier equivalent specialization elsewhere is still possible.

## Limitations

Historical uniqueness has not been proved. The result is for linear binary words with exactly three ones and ordered alphabet \(0<1\). The asymptotic variance is an asymptotic formula, not an exact finite variance identity. The finite checker does not certify the all-length proof; it reproduces nontrivial boundary cases and algebraic coefficients. No independent expert validation is asserted.

## References

1. K. Saari, *Lyndon Words and Fibonacci Numbers*, arXiv:1207.4233, initial submission 2012-07-17; journal version *Journal of Combinatorial Theory, Series A* 121 (2014). https://arxiv.org/abs/1207.4233
2. A. Glen, J. Simpson, and W. F. Smyth, *Counting Lyndon Factors*, arXiv:1701.00928, initial submission 2017-01-04; *Electronic Journal of Combinatorics* 24(3), P3.28 (2017), DOI:10.37236/6915. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p28/pdf/
