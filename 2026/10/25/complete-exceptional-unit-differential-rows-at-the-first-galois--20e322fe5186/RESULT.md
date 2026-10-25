# Complete exceptional-unit differential rows at the first Galois-ring level

## Finding

For each odd integer \(m\ge 5\), write \(q=2^m\), and choose any odd integer \(r\) satisfying \(3\le r<m\) and \(\gcd(m,r)=1\). Consider the reduced binary polynomial \(P_{m,r}\) defined below. On the characteristic-four Galois ring \(R=\operatorname{GR}(4,m)\), let \(F\in R[X]\) be **any** coefficient lift of \(P_{m,r}\), even one of degree exceeding \(q-1\). For every \(a\in R\) with residue \(\bar a=1\), define

\[
\delta_F(a,b)=\#\{x\in R:F(x+a)-F(x)=b\}\qquad(b\in R).
\]

Then the **complete exceptional unit-direction row** is

\[
\delta_F(a,b)\in\{0,2q\}\quad\text{for every }b\in R,
\qquad\#\{b\in R:\delta_F(a,b)=2q\}=q/2.
\]

For each of its \(q/2\) nonzero cells, the input difference probability is exactly \(2/q\). The reductions of the occupied output cells comprise the affine trace-one hyperplane \(1+\ker\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}\). This distribution is independent of both the coefficient lift and the choice of \(a\) in its residue class.

## Assumptions and scope

Let \(\mathbb F_q=\mathbb F_{2^m}\) and let the residue map \(R\twoheadrightarrow\mathbb F_q\) have kernel \(2R\), a set of \(q\) elements, so \(\#R=q^2\) and \(4=0\) in \(R\). Put

\[
V=\sum_{i=0}^{r-3}X^{2^i},\qquad
W=X^{2^{r-2}},\qquad
Y=X^{2^{m-2}},\qquad
Z=X^{2^{m-1}},
\]
\[
P_{m,r}=V+W+WV+WY+WZ+YV+YZ\in\mathbb F_2[X].
\]

The polynomial is the reduced representative introduced in Fukui's work, and its parameter restrictions are essential for the asserted two-element derivative fibres. The theorem concerns exactly characteristic \(4\), exceptional **unit** differences whose residue is \(1\), and coefficient lifts of this displayed polynomial, with no restrictions on the higher characteristic-four coefficients. No statement about the other unit or ideal directions, or about levels \(\operatorname{GR}(2^k,m)\) for \(k\ge3\), is made.

## Proof

**1. The exceptional derivative identity.** Each of \(V,W,Y,Z\) is additive over the binary field, and each takes the value \(1\) at \(X=1\): for \(V\) this uses the oddness of \(r-2\). Therefore their values at \(X+1\) are their values at \(X\) plus \(1\). Expanding the seven terms in \(P_{m,r}\), the two linear terms cancel in its first difference; in the remaining five products the occurrences of \(V\) and \(Z\) cancel, each of \(W\) and \(Y\) occurs three times, and the five constant terms yield \(1\). Consequently the following is a **polynomial identity**, not merely an equality of functions:

\[
P_{m,r}(X+1)+P_{m,r}(X)=1+W+Y=P_{m,r}'(X).
\tag{1}
\]

The derivative is \(1+K(X)\), where \(K(X)=X^{2^{r-2}}+X^{2^{m-2}}\) is additive. The equation \(K(t)=0\) is equivalent to \(t^{2^{r-2}}=t^{2^{m-2}}\); in \(\mathbb F_q\) it has precisely the solutions \(t=0,1\), since \(\gcd(m,m-r)=1\). Thus \(K\) has binary rank \(m-1\), and its image is the trace-zero hyperplane because the trace is fixed by Frobenius powers. As \(m\) is odd, \(\operatorname{Tr}(1)=1\), and hence

\[
P_{m,r}'(\mathbb F_q)=1+\ker\operatorname{Tr},\qquad
P_{m,r}'(s)=P_{m,r}'(t)\iff s\in\{t,t+1\}.
\tag{2}
\]

In particular, \(P_{m,r}'(X+1)=P_{m,r}'(X)\) as a polynomial identity.

**2. Invariance within residue classes.** For arbitrary \(F\in R[X]\) with \(\bar F=P_{m,r}\) and any fixed \(a\in R\) reducing to \(1\), let \(D(x)=F(x+a)-F(x)\). For every \(u\in R\), Taylor expansion by integer binomial coefficients and \((2u)^2=0\) give

\[
D(x+2u)-D(x)=2u\,[F'(x+a)-F'(x)].
\]

The bracket has residue \(P_{m,r}'(\bar x+1)-P_{m,r}'(\bar x)=0\) by (1); hence the right-hand side is zero in \(R\). Thus \(D\) is constant on each residue class modulo \(2R\), of cardinality \(q\).

**3. Pairing the two derivative fibres.** A second Taylor expansion, this time by \(2a\), yields

\[
\begin{aligned}
D(x+a)-D(x)
 &=F(x+2a)-2F(x+a)+F(x)\\
 &=2\bigl(aF'(x)-D(x)\bigr).
\end{aligned}
\]

By (1), the residue of the bracket is

\[
\bar a\,P_{m,r}'(\bar x)-\bigl(P_{m,r}(\bar x+1)-P_{m,r}(\bar x)\bigr)=0.
\]

Therefore \(D(x+a)=D(x)\) in \(R\). Combining this with Step 2, \(D\) takes one fixed value on the union of the two residue classes indexed by \(t\) and \(t+1\), and each such union contains exactly \(2q\) elements.

**4. No collision between distinct paired classes.** The residue of \(D(x)\) is, by (1), \(P_{m,r}'(\bar x)\). By (2), different unordered pairs \(\{t,t+1\}\) have different derivative values, and hence their \(D\)-values in \(R\) are different. There are exactly \(q/2\) pairs. Each occupied output has exactly \(2q\) preimages; all remaining outputs have none. Their reductions are exactly \(1+\ker\operatorname{Tr}\), as claimed. \(\square\)

## Verification

The included standalone program `check_gr4.py` performs two independent finite checks. It verifies the polynomial identity (1) by exact binary-polynomial arithmetic for all admissible \((m,r)\) with \(m\in\{5,7,9,11\}\). It separately constructs the size-\(1024\) ring \(\mathbb Z_4[t]/(t^5+t^2+1)\), a concrete model of \(\operatorname{GR}(4,5)\), and calculates all \(32\) unit-direction rows above \(1\) for the canonical lift and for two reproducible pseudorandom coefficient lifts. Each row has \(16\) nonzero entries of size \(64\). The program prints `CERTIFICATE_OK` upon success. Run `python3 check_gr4.py` in the directory containing the file; Python's standard library suffices. These tests are finite corroboration; the four proof steps above establish the theorem for all admissible parameters and all coefficient lifts.

## Relationship to prior work

Fukui, *Explicit reduced APN permutations: ramification and optimal Galois-ring lifts*, arXiv:2610.21178v1 (15 October 2026), introduces the family and gives its polynomial expression and two-to-one derivative (Theorem 3.1). Its Theorem 6.2 determines coefficient-lift rows in unit directions whose residues avoid \(\{0,1\}\), and in the top ideal, at all ring levels; explicitly, it uses only an upper bound for unit directions with residue \(1\). Its small-field tables at the first two levels give examples, not the all-parameter and all-lift theorem here. The present result fills that exceptional unit-direction case **at characteristic four only**, using the additional identity (1).

Rønjom and Sandrib, *On the differential uniformity of polynomials over Galois rings*, *Cryptography and Communications* (published 4 May 2026), Proposition 4(1), gives the general unit-direction upper bound \(\delta_F(a,b)\le 2q\) for these APN residues. That estimate does not identify the attained values, the output support or its universality across lifts. Their Theorem 3 supplies a global lower bound, not the exact exceptional unit row. Fukui, *Optimal Reduced Representatives of Quadratic APN Permutations in Odd Dimension*, arXiv:2610.21169v1 (15 October 2026), obtains broad lifting and optimality results, but its Section VIII similarly proves a global extremal count via row bounds, not this precise exceptional-row distribution. Bartoli and Stănică, arXiv:2608.30808, discuss the polynomial lifting criterion and related APN bounds rather than this row classification.

## Limitations

This result does **not** determine the higher-level exceptional rows for \(k\ge3\); indeed their behavior can differ. It does **not** classify all directions of an entire difference-distribution table, nor all derivative-optimal APN permutations. It uses a special derivative/difference identity of the displayed binary-coefficient family; that identity must not be assumed for arbitrary APN permutations. No claim of independent external validation is made. Unidentified prior treatments of the same conditional identity remain a residual originality risk.

## References

1. H. Fukui, *Explicit reduced APN permutations: ramification and optimal Galois-ring lifts*, arXiv:2610.21178v1 (2026-10-15), https://arxiv.org/html/2610.21178v1, Theorems 3.1 and 6.2 and Section 7.
2. S. Rønjom and A. Sandrib, *On the differential uniformity of polynomials over Galois rings*, *Cryptography and Communications* (2026-05-04), DOI:10.1007/s12095-026-00895-x, Section 3.
3. H. Fukui, *Optimal Reduced Representatives of Quadratic APN Permutations in Odd Dimension*, arXiv:2610.21169v1 (2026-10-15), https://arxiv.org/html/2610.21169v1, Section VIII.
4. D. Bartoli and P. Stănică, *Reduced polynomial lifts of APN permutations over Galois rings and effective non-APN bounds*, arXiv:2608.30808 (2026-08-31), https://arxiv.org/abs/2608.30808.
