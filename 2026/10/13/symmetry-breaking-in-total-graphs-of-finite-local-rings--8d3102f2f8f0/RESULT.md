# Symmetry breaking in total graphs of finite local rings

## Finding

Let \(R\) be a finite commutative local ring that is not a field, with maximal ideal \(\mathfrak m\), \(m=|\mathfrak m|\), and \(q=|R/\mathfrak m|\). For the Anderson--Badawi total graph \(T(\Gamma(R))\), \[\operatorname{Det}(T(\Gamma(R)))=q(m-1),\qquad D(T(\Gamma(R)))=m+1,\]where \(\operatorname{Det}\) is the determining number and \(D\) the distinguishing number. Moreover, if the residue characteristic is \(2\), then \(\operatorname{Aut}(T(\Gamma(R)))\cong S_m\wr S_q\); if it is odd and \(t=(q-1)/2\), then \(\operatorname{Aut}(T(\Gamma(R)))\cong S_m\times(((S_m\times S_m)\rtimes C_2)\wr S_t)\).

Thus the two symmetry-breaking parameters have formulas independent of the parity split in the graph decomposition, even though the full automorphism group changes type with the residue characteristic.

## Assumptions and scope

Let \(R\) be a finite commutative local ring that is not a field, with maximal ideal \(\mathfrak m\). Put
\[
m=|\mathfrak m|,
\qquad
q=|R/\mathfrak m|.
\]
The total graph \(T(\Gamma(R))\) has vertex set \(R\), with distinct \(x,y\) adjacent exactly when \(x+y\) is a zero divisor.

Since \(R\) is finite local,
\[
Z(R)=\mathfrak m.
\]
Also \(m\ge q\). Indeed, \(\mathfrak m\) is nilpotent. If \(\mathfrak m=\mathfrak m^2\), nilpotence would force \(\mathfrak m=0\), contradicting the nonfield assumption. Hence \(\mathfrak m/\mathfrak m^2\) is a nonzero vector space over \(R/\mathfrak m\), so
\[
|\mathfrak m/\mathfrak m^2|\ge q
\]
and therefore \(m\ge q\).

## Proof

The standard total-graph structure theorem gives the complete decomposition.

If the residue characteristic is \(2\), then \(2\in\mathfrak m\). The zero-divisor coset \(\mathfrak m\) is a clique \(K_m\), and each of the \(q-1\) nonzero residue classes is another clique \(K_m\). Hence
\[
T(\Gamma(R))\cong qK_m.
\tag{1}
\]

If the residue characteristic is odd, then \(2\notin\mathfrak m\). The zero-divisor coset is \(K_m\), while every nonzero residue class pairs with its negative to form a \(K_{m,m}\). Therefore, with
\[
t=\frac{q-1}{2},
\]
one has
\[
T(\Gamma(R))
\cong
K_m\ \dot\cup\ tK_{m,m}.
\tag{2}
\]

From (1),
\[
\operatorname{Aut}(T(\Gamma(R)))
\cong
S_m\wr S_q
=
S_m^q\rtimes S_q.
\tag{3}
\]
From (2), the \(K_m\) component is not isomorphic to the \(K_{m,m}\) components because \(m\ge3\) in odd residue characteristic. Since
\[
\operatorname{Aut}(K_{m,m})
\cong
(S_m\times S_m)\rtimes C_2,
\]
we obtain
\[
\operatorname{Aut}(T(\Gamma(R)))
\cong
S_m\times
\left(
((S_m\times S_m)\rtimes C_2)\wr S_t
\right).
\tag{4}
\]

For the determining number, every clique \(K_m\) requires at least \(m-1\) fixed vertices: otherwise two unfixed vertices may be transposed. Likewise, each bipartition class of \(K_{m,m}\) requires at least \(m-1\) fixed vertices.

In the characteristic-two case there are \(q\) clique components, so
\[
\operatorname{Det}(T(\Gamma(R)))\ge q(m-1).
\]
Selecting all but one vertex from each clique kills every internal permutation and also fixes every component, proving equality.

In the odd case, the \(K_m\) component contributes \(m-1\), and the \(t\) bipartite components contribute
\[
t(2m-2).
\]
Thus
\[
\operatorname{Det}(T(\Gamma(R)))
=
(m-1)+t(2m-2)
=
q(m-1).
\tag{5}
\]

It remains to determine the distinguishing number.

In characteristic two, an \(m\)-color distinguishing labeling is impossible. Each \(K_m\) component must use all \(m\) colors once, so any two of the \(q\ge2\) components can be exchanged color-preservingly. Hence
\[
D(T(\Gamma(R)))\ge m+1.
\]
With \(m+1\) colors, there are
\[
\binom{m+1}{m}=m+1
\]
different \(m\)-subsets of colors. Since \(q\le m\), assign a distinct color subset to each clique and use its colors injectively inside that clique. No nonidentity automorphism preserves the labeling. Therefore
\[
D(T(\Gamma(R)))=m+1.
\tag{6}
\]

In odd residue characteristic, one \(K_{m,m}\) component already forces at least \(m+1\) colors. With only \(m\) colors, injectivity on each side makes both sides use the same complete color set, and the color-matching interchange of the two sides survives.

For the upper bound, use \(m+1\) colors. An injective labeling of each side of a \(K_{m,m}\) component is specified by an \(m\)-subset of the color set. To forbid the side interchange, use two distinct \(m\)-subsets. Distinct components must receive distinct unordered pairs of such subsets. The number of available unordered pairs is
\[
\binom{\binom{m+1}{m}}{2}
=
\binom{m+1}{2}.
\]
Since \(q\le m\),
\[
t=\frac{q-1}{2}\le\frac{m-1}{2}<\binom{m+1}{2}.
\]
Thus all \(t\) bipartite components can receive different patterns. Color the \(K_m\) component injectively. This destroys every automorphism and proves
\[
D(T(\Gamma(R)))=m+1.
\tag{7}
\]

Equations (3)--(7) prove the finding.

## Verification

The accompanying `verify.py` was inspected from its actual packaged path before replay.

It directly constructs total graphs of
\[
\mathbb Z/4\mathbb Z,\quad
\mathbb Z/8\mathbb Z,\quad
\mathbb Z/9\mathbb Z
\]
from the definition \(x\sim y\iff x+y\in Z(R)\), verifies their component decompositions, exhaustively enumerates all graph automorphisms, and checks the predicted automorphism-group orders and determining numbers.

For \(\mathbb Z/4\mathbb Z\), it exhaustively tests all colorings up through three colors and verifies that the distinguishing number is \(3=m+1\).

For \(\mathbb Z/9\mathbb Z\), it checks the exact decomposition
\[
K_3\ \dot\cup\ K_{3,3},
\]
uses the complete-bipartite color-set obstruction to rule out three colors, and verifies an explicit four-color distinguishing labeling against every automorphism.

Exact replay output:

```text
Z/4Z: components OK, |Aut|=8, determining=2
Z/8Z: components OK, |Aut|=1152, determining=6
Z/9Z: components OK, |Aut|=432, determining=6
Z/4Z: distinguishing=3, witness= (0, 0, 1, 2)
Z/9Z: distinguishing=4 by exact K3,3 obstruction + verified witness
binomial pattern capacity checks OK
VERIFY_OK
```

The finite checks corroborate the general proof; the theorem itself follows from the residue-coset decomposition and the exact symmetry arguments above.

## Relationship to prior work

Anderson and Badawi introduced the total graph and proved the residue-coset decomposition when the zero divisors form an ideal. In the finite local case this gives precisely (1) and (2), so that decomposition is treated as prior structure, not as a new result.

Subsequent work on finite total graphs has studied connectivity, girth, Hamiltonicity, domination, paired domination, and related graph parameters. The checked literature did not state the determining number or distinguishing number of finite local total graphs, nor the uniform parity-independent formulas (5)--(7).

The distinguishing number was introduced by Albertson and Collins as a symmetry-breaking invariant. The proof here specializes that invariant to the repeated-clique and repeated-complete-bipartite structures forced by a finite local ring and uses the local-ring inequality \(m\ge q\) to collapse the apparent binomial thresholds to the exact value \(m+1\).

## Limitations

The ring is assumed finite, commutative, local, and nonfield.

Fields are excluded because singleton component classes change the determining-number formula.

For nonlocal rings the zero divisors need not be an ideal and the total graph can be connected; the present decomposition and formulas do not extend directly.

The graph automorphism group is generally much larger than the image of the ring automorphism group, and no claim is made about that image.

## References

1. D. F. Anderson and A. Badawi, “The total graph of a commutative ring,” *Journal of Algebra* 320 (2008), 2706–2719. DOI: 10.1016/j.jalgebra.2008.06.028. Available online 26 July 2008.
2. D. F. Anderson and A. Badawi, “On the total graph of a commutative ring without the zero element,” *Journal of Algebra and Its Applications* 11 (2012), 1250074. DOI: 10.1142/S0219498812500740. Mathematics Subject Classification begins with \(13A15\).
3. M. O. Albertson and K. L. Collins, “Symmetry breaking in graphs,” *Electronic Journal of Combinatorics* 3 (1996), R18. DOI: 10.37236/1242.
