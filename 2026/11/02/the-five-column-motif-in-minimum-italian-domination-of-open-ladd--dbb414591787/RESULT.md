# The five-column motif in minimum Italian domination of open ladders

## Finding

For every integer \(n\ge2\), let \(L_n=P_2\square P_n\) be the open two-row ladder, with two ordered rows and \(n\) labelled columns. An Italian dominating function \(f:V(L_n)\to\{0,1,2\}\) assigns total weight \(\sum_v f(v)\), subject to each zero-labelled vertex having neighbours whose labels sum to at least two. Let \(a_n\) be the number of functions of minimum possible weight. Then the minimum weight is \(n\), and

\[
\boxed{a_n=2[x^{n-2}]\frac{1}{1-x-x^2-x^5}}\quad(n\ge2).
\]

Moreover, all minimum functions are canonically encoded by a choice of one of two row orientations and a composition of \(n-2\) into parts belonging to \(\{1,2,5\}\). Thus the ordinary generating function is \(2x^2/(1-x-x^2-x^5)\). The first counts, for \(n=2,3,\ldots,11\), are \(2,2,4,6,10,18,30,52,88,150\). For \(n\ge7\), the counts satisfy \(a_n=a_{n-1}+a_{n-2}+a_{n-5}\), with the initial five values above. Their exponential growth constant is the unique real number \(\rho>1\) satisfying \(\rho^5-\rho^4-\rho^3-1=0\), approximately \(1.70490277604165\).

## Assumptions and scope

Columns are distinguished by position, and top and bottom rows are distinguished. An outer ladder has open ends, not periodic boundary conditions. The enumeration counts distinct vertex labellings, not symmetry orbits, and allows the label two. No assumption about an initially selected or positive subset is made. The published minimum-weight value is credited to earlier work; the enumeration and complete structural classification are the claims assessed here.

## Proof

**Finite-state reduction.** Enumerate the nine column labels lexicographically:

\[
D=(00,01,02,10,11,12,20,21,22),
\]

with indices \(0,\ldots,8\). Write \(w(b)\) for the sum of a column's two entries. For indices \(a,b,c\), define \(\operatorname{ok}(a,b,c)\) to mean that, for each row \(r\in\{0,1\}\) with \(b_r=0\),
\[
a_r+b_{1-r}+c_r\ge2.
\]

The fictitious zero column \(D_0=00\) is used at both ends. A labelling with successive columns \(c_1,\ldots,c_n\) is valid if and only if \(\operatorname{ok}(0,c_1,c_2)\), all the interior triple tests hold, and \(\operatorname{ok}(c_{n-1},c_n,0)\).

**A finite lower-bound certificate.** Define the integer potential \(h(a,b)\) by the following explicit matrix, with row and column indices ordered as \(D\):

```text
          00  01  02  10  11  12  20  21  22
00         0   0   1   0   1   1   1   1   2
01        -1   0   1   0   1   2   1   2   3
02         0   1   2   1   2   3   2   3   4
10        -1   0   1   0   1   2   1   2   3
11         0   1   2   1   2   3   2   3   4
12         0   1   2   1   2   3   2   3   4
20         0   1   2   1   2   3   2   3   4
21         0   1   2   1   2   3   2   3   4
22         1   2   3   2   3   4   3   4   5
```

Direct finite inspection proves all three implications:

\[
\begin{aligned}
\operatorname{ok}(0,a,b)&\implies w(a)+w(b)-2\ge h(a,b),\\
\operatorname{ok}(a,b,c)&\implies h(a,b)+w(c)-1\ge h(b,c),\\
\operatorname{ok}(a,b,0)&\implies h(a,b)\ge0.
\end{aligned}
\]

The included standalone checker reconstructs all \(9^3=729\) interior cases and both boundary tests from the displayed matrix; these are finite integer inequalities, not a numerical approximation. Summing the inequalities across any valid \(n\)-column labelling gives

\[
\sum_{j=1}^{n}w(c_j)-n\ge h(c_{n-1},c_n)\ge0.
\]

Alternating the columns \(01\) and \(10\) gives a valid labelling with weight exactly \(n\). Hence the minimum is \(n\).

**Complete equality classification.** Equality holds precisely when the initial boundary inequality, every interior inequality, and the final inequality are all equalities. Regard each ordered pair of columns as one of the \(81\) states with state number \(9a+b\). Connect state \(9a+b\) to state \(9b+c\) if the middle feasibility test and the corresponding potential inequality both hold with equality. Retain only states reachable from a tight initial pair and able to reach a zero-potential final pair. Checking the same explicit finite inequalities yields the complete trimmed graph below. Its two initial and two final states are exactly \(12\) and \(28\).

```text
state -> successor states
 1 -> 12
 3 -> 28
 5 -> 45
 7 -> 63
 9 -> 7
10 -> 12
12 -> 27,28,30
27 -> 5
28 -> 9,10,12
30 -> 28
45 -> 3
63 -> 1
```

There are exactly twelve surviving states and sixteen arrows. Any route between one connector state \(12\) and the other \(28\) is an alternation of the following three directed excursions (together with their reflected counterparts):

```text
12 -> 28                             length 1
12 -> 30 -> 28                       length 2
12 -> 27 -> 5 -> 45 -> 3 -> 28       length 5

28 -> 12                             length 1
28 -> 10 -> 12                       length 2
28 -> 9 -> 7 -> 63 -> 1 -> 12        length 5
```

Each initial pair consumes exactly two columns, and each subsequent directed arrow appends exactly one column. Therefore every minimum labelling of length \(n\) is uniquely specified by one of the two choices of initial connector and a composition of the remaining \(n-2\) columns into excursion lengths \(1,2,5\). Conversely each such composition traces a valid tight route ending at a zero-potential connector, hence gives a minimum labelling. This proves the bijection, generating function and recurrence.

**Growth.** The rational generating function has a unique positive dominant pole at \(x=\rho^{-1}\), where \(1-x-x^2-x^5=0\). It is simple, and the triangle inequality excludes other roots on its modulus circle (the allowed exponents include consecutive one and two). Thus the exponential growth base is \(\rho\).

## Verification

Run `python3 verify.py` using a standard Python 3 interpreter. The program checks every local potential inequality, reconstructs the complete trimmed transition graph, verifies the composition-bijection counts through \(n=63\), independently computes exact minimum counts directly from unrestricted column transitions through \(n=60\), and exhaustively enumerates original vertex labellings through \(n=6\). Each finite verification is a check of a finite component of the proof; the all-\(n\) claim is derived by telescoping inequalities and the exact graph description.

## Relationship to prior work

Shao and Zhao's 2026 paper develops Italian-domination counting methods on paths, trees and cycles, with explicit graph-class algorithms and cycle coefficients; it does not state the enumeration of all minimum Italian functions on open ladders. Gardner's 2018 thesis specifically studies Italian domination on ladders and is credited with the minimum-weight parameter; its publicly accessible abstract describes minimum values rather than counts of all minimizing functions. Because the thesis full text could not be inspected, an equivalent enumeration there cannot be definitively excluded. The claim here is not the existence of generic finite-state enumeration, but the explicit complete length-\(1,2,5\) classification and resulting closed recurrence for the extremizers of an infinite ladder family.

## Limitations

The graph is the open two-row Cartesian ladder, not a cylindrical ladder, prism, Möbius ladder, or a wider grid. The formula concerns minimum-weight functions only, not the full Italian-domination polynomial. The finite certificate is reproducible but has no independent external mathematical audit. Historical priority remains provisional, especially because the 2018 thesis full text was inaccessible.

## References

1. Pingping Shao and Chengye Zhao, *Counting Weight-k Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108, first public version 2026-09-09, https://arxiv.org/abs/2610.00108 .
2. Bradley Gardner, *Italian Domination on Ladders and Related Products*, M.S. thesis, East Tennessee State University, 2018, https://dc.etsu.edu/etd/3509/ .
