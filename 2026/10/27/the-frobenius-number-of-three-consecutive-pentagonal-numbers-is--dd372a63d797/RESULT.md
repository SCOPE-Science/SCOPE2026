# The Frobenius number of three consecutive pentagonal numbers is eventually cubic with period six

## Finding
Let \(P(n)=n(3n-1)/2\) be the \(n\)-th pentagonal number and \(g_n=g(P(n),P(n+1),P(n+2))\) the Frobenius number of the indicated triple. For every integer \(n\ge48\), the following table determines \(g_n\) exactly:

| \(n\bmod6\) | \(g_n\) |
|:---:|:---|
| \(0\) | \(\frac{21n^3-4n^2-41n-36}{6}\) |
| \(1\) | \(\frac{21n^3+29n^2+14n-16}{6}\) |
| \(2\) | \(\frac{51n^3+139n^2+132n+8}{12}\) |
| \(3\) | \(\frac{21n^3+44n^2+35n-6}{6}\) |
| \(4\) | \(\frac{45n^3+135n^2+158n+28}{12}\) |
| \(5\) | \(\frac{87n^3+292n^2+343n+78}{12}\) |

In fact the proof determines every element of the Apéry set of the numerical semigroup relative to its smallest generator, not only the maximum.

## Assumptions and scope
All integers \(n\ge48\) are covered; nothing is asserted here about the minimum possible eventual threshold or a uniform formula at smaller \(n\). Write \(a=P(n)\), \(b=P(n+1)\), \(c=P(n+2)\), \(H=\langle a,b,c\rangle=\{xa+yb+zc:x,y,z\in\mathbb Z_{\ge0}\}\). The Frobenius number is \(g_n=\max(\mathbb Z_{\ge0}\setminus H)\). The classical Apéry set \(\operatorname{Ap}(H,a)\) consists of minimal elements of \(H\) in the \(a\) residue classes and \(g_n=\max\operatorname{Ap}(H,a)-a\). Since \(a+c-2b=3\) and \(a\equiv n\), \(b\equiv n+1\pmod3\), we have \(\gcd(a,b,c)=1\); thus these concepts are defined.

## Proof
For each \(n\ge48\), let \(r\in\{0,1,2,3,4,5\}\) denote its residue modulo \(6\). Define integers \(u,v,U,V\) as follows:

| \(r\) | \(u\) | \(v\) | \(U\) | \(V\) |
|:---:|:---|:---|:---|:---|
| \(0\) | \(n-6\) | \(4n/3\) | \(7n/6-1\) | \(n\) |
| \(1\) | \((n-7)/2\) | \((11n+1)/6\) | \((5n+7)/3\) | \((n-1)/2\) |
| \(2\) | \((n-8)/3\) | \((7n+1)/3\) | \((5n+8)/2\) | \((n-2)/3\) |
| \(3\) | \((n-7)/2\) | \(5n/3\) | \((11n+9)/6\) | \((n-1)/2\) |
| \(4\) | \((n-46)/6\) | \((7n+2)/3\) | \((5n+4)/6\) | \((5n+1)/3\) |
| \(5\) | \((n-11)/6\) | \((14n+5)/3\) | \((9n+23)/2\) | \((n-5)/6\) |

In the stated range these are nonnegative integers and \(0\le u<U\), \(0\le V<v\). Let the finite lattice-point staircase be
\[
\mathcal S=\{(i,j)\in\mathbb Z_{\ge0}^2: i\le u, j\le v\}\cup\{(i,j)\in\mathbb Z_{\ge0}^2:i\le U,j\le V\}.
\]
Its cardinality is \((u+1)(v+1)+(U-u)(V+1)=a\) in each of the six rows, by direct substitution.

We claim \(\{ib+jc:(i,j)\in\mathcal S\}=\operatorname{Ap}(H,a)\). The complement of \(\mathcal S\) in \(\mathbb Z_{\ge0}^2\) is generated upward, coordinatewise, by the three minimal pairs \((U+1,0)\), \((u+1,V+1)\), \((0,v+1)\). The following three exact relations hold for the corresponding weighted sums:
\[
(U+1)b-(v-V)c=k_1a,\quad (u+1)b+(V+1)c=k_2a,\quad (v+1)c-(U-u)b=k_3a.
\]
The quotients, obtained by substituting the table, are:

| \(r\) | \(k_1\) | \(k_2\) | \(k_3\) |
|:---:|:---|:---|:---|
| \(0\) | \((5n+6)/6\) | \(2(n+1)\) | \((7n+6)/6\) |
| \(1\) | \((n+2)/3\) | \(n+1\) | \((2n+1)/3\) |
| \(2\) | \((n+2)/2\) | \(2(n+1)/3\) | \((n-2)/6\) |
| \(3\) | \((2n+3)/3\) | \(n+1\) | \(n/3\) |
| \(4\) | \((n+2)/6\) | \((11n+10)/6\) | \((5n+4)/3\) |
| \(5\) | \(1\) | \((n+1)/3\) | \((n-2)/3\) |

Each \(k_i\) is a *positive integer* in the specified residue class. Thus any lattice pair outside \(\mathcal S\) has one of the three forbidden generators as a coordinatewise summand and can be replaced, respectively, using \((U+1,0)\mapsto(0,v-V)\), \((u+1,V+1)\mapsto(0,0)\), or \((0,v+1)\mapsto(U-u,0)\). These replacements preserve the weighted sum modulo \(a\), are nonnegative, and strictly *decrease* that weighted sum by \(k_i a>0\). Repeating terminates in \(\mathcal S\). Because \(\gcd(a,b,c)=1\), each residue class modulo \(a\) is represented by some nonnegative combination of \(b,c\); hence it is represented in \(\mathcal S\). Since \(|\mathcal S|=a\), there is exactly one such pair per residue. Every pair outside has strictly greater weight than its reduction to the unique pair within, proving the Apéry assertion. In particular the maximum occurs at one of the two corners \((u,v)\), \((U,V)\):
\[
g_n=\max\{ub+vc,Ub+Vc\}-a.\]

Substitution yields the six first-corner polynomials \(G_{r,1}\), second-corner polynomials \(G_{r,2}\), and their differences \(12(G_{r,1}-G_{r,2})\):

| \(r\) | \(12(G_{r,1}-G_{r,2})\) | Larger corner for \(n\ge48\) |
|:---:|:---|:---|
| \(0\) | \(3n^3-73n^2-132n-60\) | \((u,v)\) |
| \(1\) | \(3n^3-40n^2-65n-30\) | \((u,v)\) |
| \(2\) | \(-3n^3-35n^2-40n-20\) | \((U,V)\) |
| \(3\) | \(-3n^3-44n^2-63n-30\) | \((U,V)\) |
| \(4\) | \(-4(5n+4)(6n+5)\) | \((U,V)\) |
| \(5\) | \(3n^3-28n^2-17n-10\) | \((u,v)\) |

All signs in the last column hold for \(n\ge48\): the three positive cubic expressions have the form \(n^2(3n-A)-Bn-C\) with \((A,B,C)\in\{(73,132,60),(40,65,30),(28,17,10)\}\), manifestly positive in this range; the others are negative. Expanding the winning corner gives exactly the six displayed cubics, completing the proof.

## Verification
The standalone `verify.py` checks all six staircase cardinality identities, reduction identities, integrality, positivity, winning-corner formulas and exact Frobenius values against an independent shortest-path Apéry computation on \(48\le n\le100\), with additional separated samples. Polynomial identities are verified as degree-at-most-three identities at four points per residue class, not inferred from finite experiments: the maximum degree bound follows explicitly from the displayed quadratic generators and linear corners. The script uses only Python standard-library integer arithmetic and may be run as `python3 verify.py`.

## Relationship to prior work
OEIS A069757 records these Frobenius numbers as a sequence (first authored April 5, 2002) and supplies an explicit finite table through \(n=1000\), but its publicly displayed entry does not give the all-parameter formulas proved here. Lepilov, O'Rourke and Swanson (2014) give eventual polynomial formulas for triples of consecutive *squares and cubes*, not pentagonal numbers. Komatsu (2022) gives formulas for *triangular-number* triples. The Rødseth–Apéry methodology and general parametric-quasipolynomial phenomena are established prior art; the precise six pentagonal formulas and staircase parameters are the claimed contribution, not the framework. Relevant comparisons include numerical consequences (finite tables) versus a uniform theorem; a finite prefix is not a proof for every \(n\).

## Limitations
The result does not cover \(n<48\), prove that the threshold \(48\) is optimal, address higher polygonal orders, or determine generalized \(p\)-Frobenius numbers. It has not undergone independent mathematical review. A hard-to-index earlier formula outside the inspected sources remains possible; searches alone cannot rule that out.

## References
1. V. A. Sapko, “Frobenius number of the numerical semigroup generated by three consecutive pentagonal numbers,” *OEIS A069757*, initial entry April 5, 2002, https://oeis.org/A069757.
2. M. Lepilov, J. O'Rourke and I. Swanson, “Frobenius numbers of numerical semigroups generated by three consecutive squares or cubes,” manuscript dated October 22, 2014, https://www.math.purdue.edu/~iswanso/LepilovORourkeSwanson.pdf.
3. T. Komatsu, “The Frobenius number for sequences of triangular numbers associated with number of solutions,” arXiv:2206.13054 (2022), https://arxiv.org/abs/2206.13054.
4. R. Yin, J. Mu and T. Komatsu, “The p-Frobenius Number for the Triple of the Generalized Star Numbers,” preprint, July 29, 2024, https://www.preprints.org/manuscript/202407.2280/v1.
