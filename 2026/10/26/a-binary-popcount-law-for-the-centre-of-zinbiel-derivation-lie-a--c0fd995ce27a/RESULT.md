# A binary popcount law for the centre of Zinbiel derivation Lie algebras

## Finding
For every integer \(n\geq2\) and every field \(k\), define the \(n\)-dimensional one-generated null-filiform Zinbiel algebra \(Z_n(k)\) by the multiplication in the next section. Let \(\mathfrak d_n(k)=\operatorname{Der}_k(Z_n(k))\), equipped with the commutator bracket. The centre of this **derivation Lie algebra**, not the subspace of derivations with image in the centre of \(Z_n(k)\), is as follows.

* If \(\operatorname{char}k=0\), the centre is zero.
* If \(\operatorname{char}k=p\) for an odd prime \(p\), the centre is spanned by \(\partial_n\) exactly when \(n\equiv1\pmod p\), and is zero otherwise.
* If \(\operatorname{char}k=2\), put \(s(i)=\nu_2(i+1)\) for odd \(i\). Then
\[
 Z(\mathfrak d_n(k))=\operatorname{span}_k\{\partial_i:1\leq i\leq n,\ i\text{ odd},\ n\leq i+2^{s(i)}-2\}.
\]
In particular, writing \(t=\nu_2(n+2)\) and \(\operatorname{popcount}(m)\) for the number of ones in the binary expansion of a nonnegative integer,
\[
 \dim_k Z(\mathfrak d_n(k))=
 \operatorname{popcount}\!\left(\left\lfloor\frac{n+1}{2^{t+1}}\right\rfloor\right)
 \qquad(\operatorname{char}k=2).
\]
The binary centre dimension is unbounded: at \(n=2^r-3\) it equals \(r-1\) for every \(r\geq3\), whereas in every odd characteristic it is at most one.

## Assumptions and scope
The ground field may be finite, infinite, or nonperfect. Binomial coefficients are ordinary integers reduced in \(k\); no factorial is inverted in \(k\). Let \(e_1,\ldots,e_n\) be a basis and set
\[
 e_a\circ e_b=\binom{a+b-1}{b}e_{a+b}\quad(a+b\leq n),\qquad
 e_a\circ e_b=0\quad(a+b>n).
\]
The identity \((x\circ y)\circ z=x\circ(y\circ z)+x\circ(z\circ y)\) holds integrally for these coefficients and therefore in every characteristic. Since \(e_1\circ e_j=e_{j+1}\), the algebra is one-generated with the expected null-filiform filtration. Throughout, \(\nu_2(m)\) is the exponent of two dividing the positive integer \(m\). For each \(1\leq h\leq n\), define
\[
 \partial_h(e_m)=
 \begin{cases}
 \binom{m+h-1}{m-1}e_{m+h-1},&m+h-1\leq n,\\
 0,&m+h-1>n.
 \end{cases}
\]

## Proof
**1. All derivations and their brackets.** Applying the derivation rule to \(e_{m+1}=e_1\circ e_m\) shows inductively that every derivation is uniquely determined by its value on \(e_1\). The displayed maps \(\partial_h\) satisfy the derivation rule, by the following integer identity for all positive \(a,b,h\):
\[
 \binom{a+b-1}{b}\binom{a+b+h-1}{a+b-1}
 =\binom{a+h-1}{a-1}\binom{a+b+h-2}{b}
 +\binom{b+h-1}{b-1}\binom{a+b+h-2}{b+h-1}.
\]
Indeed, after multiplying out the factorial expressions over the rational numbers, the two terms on the right have respective numerators proportional to \(a+h-1\) and \(b\), whose sum is \(a+b+h-1\); since the identity is between integers it survives reduction modulo every prime. Out-of-range terms are zero on both sides by grading. Because \(\partial_h(e_1)=e_h\), the maps \(\partial_1,\ldots,\partial_n\) form a basis for \(\mathfrak d_n(k)\). Evaluating the commutator on \(e_1\), and again using uniqueness of a derivation determined by \(e_1\), yields
\[
 [\partial_i,\partial_j]=
 \left(\binom{i+j-1}{j-1}-\binom{i+j-1}{i-1}\right)\partial_{i+j-1}
 \quad(i+j-1\leq n),
\]
with zero bracket if the subscript exceeds \(n\). For any fixed \(j\), the possible nonzero terms \([\partial_i,\partial_j]\) have distinct output subscripts as \(i\) varies. Therefore an arbitrary linear combination is central exactly when each of its contributing homogeneous basis derivations is central.

**2. Characteristic zero and odd characteristic.** The special bracket \([\partial_i,\partial_1]=(1-i)\partial_i\) forces a central basis element to have \(i=1\) in characteristic zero and \(i\equiv1\pmod p\) in characteristic \(p\). In characteristic zero \([\partial_1,\partial_2]=\partial_2\ne0\), because \(n\ge2\); hence the centre is zero. For odd \(p\), whenever \(i<n\) and \(i\equiv1\pmod p\),
\[
 [\partial_i,\partial_2]=\frac{(i+1)(2-i)}2\,\partial_{i+1}
 =\partial_{i+1}\ne0
\]
(the fraction is an integer, and division by two is legitimate for odd \(p\)). Thus only \(\partial_n\) can be central, and the first bracket test says precisely \(n\equiv1\pmod p\).

**3. Characteristic two.** The first bracket test forces \(i\) odd. Write \(s=\nu_2(i+1)\ge1\), so the lowest \(s\) binary digits of \(i\) are ones and its digit in position \(s\) is zero. By Lucas's binomial parity criterion, \(\binom{i+j-1}{j-1}\) is odd exactly when the binary expansions of \(i\) and \(j-1\) have no overlapping ones; similarly \(\binom{i+j-1}{i-1}\) is odd exactly when \(i-1\) and \(j\) have no overlapping ones. For \(2\leq j<2^s\), both binomials are even: \(j-1\) meets a low one of \(i\), while a nonzero digit of \(j\) in position at least one meets a low one of \(i-1\). At \(j=1\) both binomials are odd and cancel. At \(j=2^s\), the first binomial is even but the second odd. Consequently the **first** nonzero bracket with \(\partial_i\), as \(j\) increases from one, occurs precisely at \(j=2^s\), provided that output degree is retained by the truncation. The allowable partners satisfy \(j\leq n-i+1\); hence
\[
 \partial_i\in Z(\mathfrak d_n(k))\ \Longleftrightarrow\ n-i+1<2^s
 \ \Longleftrightarrow\ n\leq i+2^s-2.
\]
This proves the exact characteristic-two central basis.

**4. Counting binary central degrees.** Put \(N=n+1\). For fixed \(s\ge1\), an index with \(\nu_2(i+1)=s\) has the unique form \(i=2^s(2u+1)-1\), \(u\ge0\). The two inequalities \(i\leq n\) and \(n\leq i+2^s-2\) are equivalent to
\[
 2^s(2u+1)\leq N,
 \qquad N+2\leq2^s(2u+2).
\]
Thus exactly one such central index exists if and only if binary digit \(s\) of \(N\) equals one and its lower \(s\) digits are **not** all ones. If \(t=\nu_2(N+1)=\nu_2(n+2)\), then \(t\) is precisely the number of trailing binary ones of \(N\). The admissible positions are the one-bits of \(N\) strictly above position \(t\). Their number is \(\operatorname{popcount}(\lfloor N/2^{t+1}\rfloor)\), as claimed. For \(n=2^r-3\), \(t=0\) and the argument of the popcount is \(2^{r-1}-1\), proving the unbounded growth assertion.

## Verification
The standalone file `check_zinbiel_center.py` requires only Python's standard library. Running `python check_zinbiel_center.py` gave `ZINBIEL_CENTRE_OK test_size_pairs= 360`. It checks the integral Zinbiel identity, the integral derivation identity, coefficientwise commutator formula, the exact central-basis criterion in 360 characteristic/size cases, and the binary popcount formula. In particular, over characteristic two, the central basis indices are \(\{7,11,13\}\) when \(n=13\), and \(\{15,23,27,29\}\) when \(n=29\). These finite checks corroborate the proof but do not substitute for the unrestricted Lucas argument.

## Relationship to prior work
The null-filiform Zinbiel family and its binomial multiplication are standard in the classification literature; neither their definition nor the one-generated property is claimed to be new. The 2013 and 2014 Zinbiel classification papers examine complex naturally graded algebra structures, not the centre of the derivation Lie algebra in positive characteristic. A later paper on central derivations of complex low-dimensional Zinbiel algebras uses a different invariant: maps from the algebra into its own centre. The present invariant is instead the centre of the **entire commutator Lie algebra of derivations**, in arbitrary dimension and characteristic. The commutator presentation is also isomorphic to the degree-\(n\) truncation of the positive divided-power Witt Lie algebra, via \(\partial_i\mapsto t^{(i)}\,\mathrm d/\mathrm dt\). The identification of this bracket is **not** claimed new: the centre theorem can equivalently be stated for that truncated positive Lie algebra. Searches under this Witt/Zassenhaus alias did not identify an arbitrary-truncation binary centre basis or popcount law, but a general modular Witt result could imply it. The characteristic-two popcount formula, its homogeneous central basis, and the unbounded comparison with odd characteristic were not located in the inspected sources. This is a bounded literature comparison, not a proof of universal publication priority.

## Limitations
The result applies to this specific one-generated null-filiform Zinbiel family. It does not classify centres of derivation algebras for all Zinbiel deformations or superalgebras. The proof does not require independent software certification, and no independent mathematical audit was performed. Indirect implication by an unlocated general theorem on truncated positive divided-power Witt algebras or modular operadic derivations cannot be excluded.

## References
1. J. Q. Adashev, L. M. Camacho, S. Gómez-Vidal, I. A. Karimjanov, *Naturally graded Zinbiel algebras with nilindex \(n-3\)*, arXiv:1303.5881 (first posted 2013-03-23), sections 1–2.
2. J. K. Adashev, M. Ladra, B. A. Omirov, *The classification of naturally graded Zinbiel algebras with characteristic sequence equal to \((n-p,p)\)*, arXiv:1410.7549 (first posted 2014-10-28), sections 2–3.
3. L. M. Camacho, A. Fernández Ouaridi, I. Kaygorodov, R. M. Navarro, *Zinbiel superalgebras*, arXiv:2304.00273 (first posted 2023-04-01), preliminary classification and null-filiform section.
4. I. Basdouri, J. Lerbet, B. Mosbahi, *Central derivations of low-dimensional Zinbiel algebras*, arXiv:2411.15642 (first posted 2024-11-23), definitions 2.5, 2.11 and section 3.
