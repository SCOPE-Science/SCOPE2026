# Characteristic-five Ciani quartics: exact \(5\)-rank strata and eight superspecial parameter triples

## Finding

Over \(\mathbb F_{25}\), among the geometrically smooth coordinate-marked Ciani quartics
\[
C_{r,s,t}:\ X^4+Y^4+Z^4+rX^2Y^2+sY^2Z^2+tZ^2X^2=0,
\qquad (r,s,t)\in\mathbb F_{25}^3,
\]
the numbers of coefficient triples of Jacobian \(5\)-rank \(0,1,2,3\), respectively, are
\[
\boxed{8,\quad96,\quad1110,\quad10469}.
\]
These are \(11683\) smooth coefficient triples in all; the other \(3942\) triples give geometrically singular plane quartics. The \(a\)-number is \(3\) minus the \(5\)-rank for every smooth member.

Over the algebraic closure, **all** smooth superspecial triples in the normalized three-parameter Ciani family are precisely
\[
\boxed{(r,s,t)=(\epsilon_1a,\epsilon_2a,\epsilon_3a),\quad
\epsilon_i\in\{1,-1\},\quad \epsilon_1\epsilon_2\epsilon_3=1,\quad a^2-2a-2=0.}
\]
They are eight distinct **ordered coefficient triples**, all defined over \(\mathbb F_{25}\) and none over \(\mathbb F_5\). These are not asserted to represent eight distinct abstract isomorphism classes of curves. Over \(\mathbb F_5\), the smooth coefficient-triple counts are \(12\) of rank \(1\) and \(11\) of rank \(3\), with none of ranks \(0\) or \(2\).

## Assumptions and scope

All finite-field arithmetic has characteristic \(5\). Coefficient triples are ordered and the three pure quartic coefficients are fixed equal to \(1\); equivalence under arbitrary projective coordinate changes is **not** imposed. All rank statements are for the Jacobian of the smooth geometrically connected genus-three curve. Geometric smoothness is equivalent to
\[
(r^2-4)(s^2-4)(t^2-4)(r^2+s^2+t^2-rst-4)\ne0.
\]
The \(5\)-rank means the dimension of the maximal étale subgroup of geometric \(5\)-torsion; the \(a\)-number is the dimension of \(\mathrm{Hom}(\alpha_5,\mathrm{Jac}(C)[5])\).

## Proof

**Step 1: a diagonal Hasse–Witt computation.** The plane quartic is canonical. In characteristic \(5\), its Hasse–Witt matrix on the standard plane-quartic basis has off-diagonal entries zero: the monomials in the defining quartic have even exponents, while each off-diagonal required exponent vector has an odd component. The three diagonal entries are the coefficients of \(X^8Y^4Z^4\), \(X^4Y^8Z^4\), and \(X^4Y^4Z^8\) in the fourth power of the defining quartic. A direct multinomial expansion in \(\mathbb F_5[r,s,t]\) gives
\[
\begin{aligned}
h_1&=r^2t^2+2r^2-rst+s^2+2t^2+2,\\
h_2&=r^2s^2+2r^2-rst+2s^2+t^2+2,\\
h_3&=r^2-rst+s^2t^2+2s^2+2t^2+2.
\end{aligned}
\]
The Jacobian admits an isogeny of degree \(8\), prime to \(5\), to the product of its three elliptic involution quotients. In this case the three quantities \(h_i\) are their Hasse invariants, up to nonzero factors. For example, one elliptic quotient is presented by
\[
v^2=(r^2-4)u^4+(2rt-4s)u^2+(t^2-4),
\]
whose Hasse invariant is the middle coefficient of the square of its quartic right-hand side, namely
\[
(2rt-4s)^2+2(r^2-4)(t^2-4)=h_1
\]
in \(\mathbb F_5\). Thus
\[
\boxed{f_5(C_{r,s,t})=\#\{i:h_i\ne0\},\quad a(C_{r,s,t})=\#\{i:h_i=0\}.}
\]
The semilinearity of Hasse–Witt causes no issue: it is diagonal, so its stable rank equals its initial rank. Alternatively the degree-eight prime-to-five isogeny identifies the three elliptic \(5\)-torsion contributions.

**Step 2: the geometric rank-zero locus.** Subtracting the three Hasse invariants gives
\[
\begin{aligned}
h_1-h_2&=(t^2-s^2)(r^2+1),\\
h_2-h_3&=(r^2-t^2)(s^2+1),\\
h_3-h_1&=(s^2-r^2)(t^2+1).
\end{aligned}
\]
For smooth curves, \(r^2,s^2,t^2\ne4=-1\), so simultaneous vanishing forces \(r^2=s^2=t^2\). We can then choose \(a\) and signs of product \(1\) with \((r,s,t)=(\epsilon_1a,\epsilon_2a,\epsilon_3a)\). Each invariant reduces to
\[
a^4-a^3+2=(a-2)^2(a^2-2a-2).
\]
The root \(a=2\) gives singular quartics. The quadratic factor is irreducible over \(\mathbb F_5\), has two distinct roots in \(\mathbb F_{25}\), and for either root
\[
3a^2-a^3-4=3\ne0
\]
in \(\mathbb F_5\). Furthermore \(a^2\ne4\). Hence both roots produce smooth superspecial quartics and, with four even-sign choices each, exactly eight ordered triples. This is a geometric statement valid over the algebraic closure, not an inference from a finite-field search.

**Step 3: the complete \(\mathbb F_{25}\)-rational rank census.** Use the exact representation \(\mathbb F_{25}=\mathbb F_5[v]/(v^2-2)\). Iterate all \(25^3=15625\) ordered coefficient triples, reject a triple precisely when the smoothness product vanishes, and count the nonzero evaluations of the three \(h_i\). The supplied independent programs `verify_f25.py` and `verify_quotients.py` obtain exactly the table in the Finding, although the latter uses \(\mathbb F_5[w]/(w^2+w+1)\) and computes the three elliptic quotient Hasse invariants directly. This exhaustive finite-field step proves the **finite census only**; the geometric uniqueness in Step 2 is proved symbolically.

## Verification

From the directory containing the three standalone Python files, run

```bash
python3 verify_polynomial.py
python3 verify_f25.py
python3 verify_quotients.py
```

They require only the Python standard library. The exact successful outputs were

```text
POLYNOMIAL_VERIFY_OK 3
VERIFY_OK {0: 8, 1: 96, 2: 1110, 3: 10469} smooth 11683 singular 3942 roots [11, 16]
QUOTIENT_VERIFY_OK {0: 8, 1: 96, 2: 1110, 3: 10469} F5 {1: 12, 3: 11}
```

The polynomial checker reconstructs the Hasse coefficients from scratch, verifies the displayed difference factorization, and does not infer infinite-field statements from a finite-field test. The two finite-field checkers use different quadratic moduli and independently obtained formulas for the three invariants.

## Relationship to prior work

Ohashi (2022) supplies the normalized Ciani model, exact smoothness criterion, degree-eight prime-to-characteristic elliptic quotient decomposition, and the theorem that superspecial Ciani parameters are \(\mathbb F_{p^2}\)-rational. The present classification uses these established results; none is claimed as new. Ohashi's paper cites Brock's 1993 superspecial Ciani classification, which presents a meaningful historical-overlap risk for the *superspecial subclaim*.

Moriya and Kudo (2022) supply broader constructions and algorithms for genus-three Howe curves and decomposed Richelot isogenies, including superspecial enumeration methods. The arithmetic result here is the exact **joint full rank stratification across all smooth ordered \(\mathbb F_{25}\)-coefficients** together with a direct geometric proof of its rank-zero locus, not a new abstract isomorphism classification or new quotient-isogeny construction. Earlier genus-three superspecial class counts alone do not imply the ranks of non-superspecial marked coefficients.

## Limitations

The rank table is specific to the **fixed normalized coefficient family over \(\mathbb F_{25}\)**. Its entries count parameter triples, not geometrically or arithmetically distinct isomorphism classes. The superspecial-locus statement is geometric, but the full rank-stratum cardinalities are not asserted for larger extension fields. Historical completeness and priority cannot be certified: Brock's thesis could contain equivalent portions of the superspecial parameter calculation, and an unindexed marked-family table might cover part of the rank census. No independent external audit has been performed.

## References

1. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996 (initial public version 2022-01-31), sections 2–4. https://arxiv.org/abs/2201.12996
2. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926 (initial public version 2022-09-07), especially sections 3–5. https://arxiv.org/abs/2209.02926
3. N. Brock, *Superspecial curves of genera two and three*, thesis (1993), Theorem 3.15, cited by Ohashi; original full text was not obtained for this comparison.
