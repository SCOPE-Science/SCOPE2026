# No degree-seven points on six Dickson–Guralnick–Zieve curves

## Finding

Let \(q\ge 3\) be a prime power and let \(\mathcal X_q\) denote the smooth projective normalization over \(\mathbb F_q\) of the Dickson–Guralnick–Zieve (DGZ) plane curve. For
\[
q\in\{3,5,17,19,31,47\},
\]
**the curve has no points over its seventh-degree extension**:
\[
\boxed{\mathcal X_q(\mathbb F_{q^7})=\varnothing.}
\]
In particular, it has no closed points of degree seven. The plane DGZ model also has no \(\mathbb F_{q^7}\)-points, by the one-branch-at-each-singularity correspondence of Giulietti–Korchmáros–Timpanella.

More generally, the proof supplies a coprime-Frobenius orbit obstruction: if \(7\nmid |\operatorname{PGL}(3,q)|\) and
\[
7|\operatorname{PGL}(3,q)|>q^7+1+2g_q q^{7/2},
\]
then \(\mathcal X_q(\mathbb F_{q^7})\) is empty, where
\[
g_q=\frac{q(q-1)(q^3-2q-2)}2+1.
\]
The displayed six fields satisfy both hypotheses. The theorem makes no assertion for other field sizes.

## Assumptions and scope

Write \(D_1\) and \(D_2\) for the Moore-type determinants whose columns are respectively
\[
(v,v^{[q]},v^{[q^3]})\quad\text{and}\quad(v,v^{[q]},v^{[q^2]}),
\]
where \(v=(X,Y,Z)^{\mathsf T}\) and exponentiation is coordinatewise. The polynomial \(D_1/D_2\), known to be homogeneous of degree \(q^3-q^2\), defines the integral DGZ plane curve. Its smooth projective normalization is \(\mathcal X_q\). These defining properties and the following group-action facts are established in [1]:

The group \(G_q=\operatorname{PGL}(3,\mathbb F_q)\) acts over \(\mathbb F_q\) on \(\mathcal X_q\), with
\[
|G_q|=q^3(q^3-1)(q^2-1).
\]
Its only geometric orbits with nontrivial point stabilizer are the orbits \(\Omega_2\) and \(\Omega_3\), consisting of points defined over \(\mathbb F_{q^2}\) and \(\mathbb F_{q^3}\), respectively. Moreover \(\mathcal X_q(\mathbb F_q)=\varnothing\), and \(\mathcal X_q\) has the genus \(g_q\) displayed above. Here "long" means an orbit of size \(|G_q|\), not merely an orbit larger than the short ones. This proof uses these specific published geometric facts, not an unverified classification of other curves.

## Proof

**Step 1 (short orbits cannot contribute).** Suppose \(P\in\mathcal X_q(\mathbb F_{q^7})\). A point in \(\Omega_2\) would be defined over both \(\mathbb F_{q^2}\) and \(\mathbb F_{q^7}\), and therefore over their intersection \(\mathbb F_q\), which is impossible. The same argument excludes \(\Omega_3\). Consequently the \(G_q\)-orbit \(\mathcal O=G_q P\) is long: it contains exactly \(|G_q|\) points, all defined over \(\mathbb F_{q^7}\).

**Step 2 (the coprime-Frobenius obstruction).** Let \(\varphi\) be the arithmetic \(q\)-Frobenius. Since \(G_q\) is defined over \(\mathbb F_q\), \(\varphi\) commutes with its action. The orbit \(\varphi(\mathcal O)\) is another long \(G_q\)-orbit. On \(\mathcal X_q(\mathbb F_{q^7})\), we have \(\varphi^7=1\); because seven is prime, the orbit of \(\mathcal O\) under \(\varphi\) has length one or seven.

If \(\varphi(\mathcal O)=\mathcal O\), there is a *unique* \(h\in G_q\) with \(\varphi(P)=hP\), uniqueness using freeness of the long orbit. By commutation, \(\varphi^j(P)=h^jP\) for every nonnegative integer \(j\). Hence \(h^7P=P\), and freeness implies \(h^7=1\). Whenever \(7\nmid |G_q|\), Lagrange's theorem forces \(h=1\); then \(P\) is \(\mathbb F_q\)-rational, contrary to the published point count. Thus \(\varphi\) must permute **seven distinct long orbits**. This gives the lower bound
\[
\#\mathcal X_q(\mathbb F_{q^7})\ge 7|G_q|.
\]
This seven-orbit amplification is essential: a single long orbit does not violate the Hasse–Weil bound for any of the six stated fields.

**Step 3 (compare with Hasse–Weil).** The usual Hasse–Weil bound for a smooth genus-\(g_q\) curve over \(\mathbb F_{q^7}\) gives
\[
\#\mathcal X_q(\mathbb F_{q^7})\le q^7+1+2g_q q^{7/2}.
\]
Let \(U_q=q^7+1+\lfloor\sqrt{4g_q^2q^7}\rfloor\), an integer upper bound. Exact integer arithmetic gives:

| \(q\) | \(g_q\) | \(|G_q|\) | \(U_q\) | \(7|G_q|-U_q\) |
|---:|---:|---:|---:|---:|
| 3 | 58 | 5,616 | 7,612 | 31,700 |
| 5 | 1,131 | 372,000 | 710,374 | 1,893,626 |
| 17 | 663,273 | 6,950,204,928 | 27,281,939,483 | 21,369,495,013 |
| 19 | 1,166,050 | 16,934,047,920 | 70,618,269,583 | 47,920,065,857 |
| 31 | 13,823,056 | 851,974,934,400 | 4,613,152,978,276 | 1,350,671,562,524 |
| 47 | 112,128,888 | 23,800,278,205,248 | 160,127,618,114,208 | 6,474,329,322,528 |

For these \(q\), one has \(q\bmod 7\in\{3,5\}\). Since neither \(q^3-1\) nor \(q^2-1\) is divisible by seven when \(q\bmod 7\) has multiplicative order six, \(7\nmid |G_q|\). Every rightmost entry is positive. Steps 2 and 3 are contradictory if any \(\mathbb F_{q^7}\)-point exists. This proves the theorem.

**Step 4 (closed points).** A closed point of degree seven would furnish seven \(\mathbb F_{q^7}\)-points. Since none exist, there are no such closed points. Conversely the absence of degree-one points from [1] shows that emptiness over \(\mathbb F_{q^7}\) is precisely the absence of degree-seven points.

## Verification

Run \(\texttt{python3 verify_dgz_degree7.py}\) using the Python standard library. It recomputes the group and genus formulas, checks the six congruence and order conditions, and verifies each exact Hasse–Weil margin using integer square roots, without floating-point approximations. It also checks that all six fields are prime powers and are exactly the prime powers at most 47 congruent to 3 or 5 modulo 7.

An independent optional finite-field check of \(q=3\) is in \(\texttt{verify_dgz_f3_seven.cpp}\). Compile it with a C++17 compiler and run it. It works in \(\mathbb F_{3^7}=\mathbb F_3[t]/(t^7+t^3+t+1)\), evaluates the explicit 25-term affine quotient \(D_1/D_2\) by square-class reduction, and returns zero affine points. Its degree-18 part is \((x^6+y^6)(x^{12}+y^{12})\), which has no projective points at infinity because \(-1\) is nonsquare in \(\mathbb F_{3^7}\). This finite computation is a *corroborating special case*, not the proof for all six fields.

## Relationship to prior work

Giulietti–Korchmáros–Timpanella [1] establish the DGZ curve, its normalization, group, two short orbits, genus, and point counts over extension degrees 1–3. Borges–Korchmáros–Speziali [2], Section 7, extend the point counts to degrees 4–6, using group orbit sizes and Hasse–Weil bounds. Their recorded result includes the emptiness of degree-five points but does not assert the six new degree-seven emptiness statements.

The present comparison is by implication, not vocabulary: [2]'s *single*-long-orbit lower bound is insufficient for all six listed fields, because \(|G_q|<U_q\) in each case. The extra coprime-Frobenius argument forces seven entire orbits and supplies the decisive factor seven. No claim is made that general Frobenius-commutation or the Hasse–Weil bound is new; the new asserted application is the exact degree-seven vanishing across these six fields.

## Limitations

The method yields no claim for other \(q\), including \(q=2\) (when the group has order divisible by seven) or \(q=59\) (when this simple Hasse–Weil comparison is insufficient). It does not determine the full DGZ zeta function, nor the number of degree-seven points for arbitrarily large \(q\). Searches cannot exclude equivalent statements in older, unindexed literature. Independent mathematical verification has not been performed.

## References

[1] M. Giulietti, G. Korchmáros, M. Timpanella, *On the Dickson–Guralnick–Zieve curve*, arXiv:1805.05618 (first public version 2018-05-15); in particular Sections 4 and 7, Proposition 7.2, and the displayed genus and finite-field point counts. https://arxiv.org/abs/1805.05618

[2] H. Borges, G. Korchmáros, P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765 (first public version 2022-02-11), Section 7, Theorem 7.1 and its proof. https://arxiv.org/abs/2202.05765
