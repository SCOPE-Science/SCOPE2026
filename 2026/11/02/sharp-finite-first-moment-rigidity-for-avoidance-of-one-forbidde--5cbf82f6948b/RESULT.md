# Sharp finite first-moment rigidity for avoidance of one forbidden word

## Finding

Fix any finite alphabet \(\Sigma\) of cardinality \(q\ge2\), a distinguished symbol \(a\in\Sigma\), and a forbidden word \(w\in\Sigma^m\) of length \(m\ge1\). Let \(A_w(n,k)\) count words of length \(n\) avoiding \(w\) as a contiguous factor and containing exactly \(k\) copies of \(a\). Define the unweighted count \(N_w(n)=\sum_k A_w(n,k)\) and total marked-letter count \(M_w(n)=\sum_k kA_w(n,k)\). The empty word is included: \(N_w(0)=1\) and \(M_w(0)=0\).

**Finite-jet rigidity theorem.** For any two single forbidden words \(w,v\in\Sigma^m\), the following are equivalent:

1. \(N_w(n)=N_v(n)\) and \(M_w(n)=M_v(n)\) for every \(0\le n\le 2m-1\).
2. \(A_w(n,k)=A_v(n,k)\) for every \(n,k\ge0\).

The terminal length \(2m-1\) is necessary for each \(m\ge4\), already for \(q=2\). The restriction to **one** forbidden word also cannot simply be dropped: two forbidden sets can have identical \(N\) and \(M\) for every length without having identical marked-letter spectra.

## Assumptions and scope

All words are finite, linear and over one fixed alphabet. Factor avoidance is contiguous; overlapping occurrences are forbidden just as nonoverlapping ones are. The same distinguished letter is counted for both avoidance languages. There is exactly one forbidden word in the main theorem, and the two forbidden words have the same length. The theorem is exact, for all integer \(q\ge2\) and \(m\ge1\); it does not assume irreducibility or mixing of the corresponding infinite shift.

Set
\[
F_w(z,y)=\sum_{n,k\ge0}A_w(n,k)z^ny^k,\quad
H_w(z)=F_w(z,1),\quad
J_w(z)=\partial_yF_w(z,1).
\]

Let \(h_w\) be the number of copies of \(a\) in \(w\). For each \(1\le d<m\), write \(b_{w,d}=1\) precisely if the length-\(m-d\) prefix and suffix of \(w\) agree; otherwise let it be zero. Let \(r_{w,d}\) be the number of copies of \(a\) in the last \(d\) letters of \(w\). Define the weighted overlap polynomial
\[
C_w(z,y)=1+\sum_{d=1}^{m-1}b_{w,d}z^dy^{r_{w,d}},\quad
C_{0,w}(z)=C_w(z,1),\quad
C_{1,w}(z)=\partial_yC_w(z,1).
\]

## Proof

**1. Weighted cluster identity.** Give each letter \(a\) weight \(zy\) and each other letter weight \(z\). Inclusion-exclusion over marked occurrences of \(w\) counts avoiding words. A maximal overlapping cluster begins with one negatively marked \(w\) of weight \(-z^my^{h_w}\), and each subsequent negatively marked overlapping copy extends its predecessor by \(d\) symbols with signed weight \(-b_{w,d}z^dy^{r_{w,d}}\). Hence the generating function of clusters is \(-z^my^{h_w}/C_w(z,y)\). Every marked word decomposes uniquely as a sequence of single unmarked letters and overlapping clusters. Therefore, in formal power series,
\[
F_w(z,y)=\frac{C_w(z,y)}{(1-z(q-1+y))C_w(z,y)+z^my^{h_w}}
=\left(1-z(q-1+y)+\frac{z^my^{h_w}}{C_w(z,y)}\right)^{-1}.
\tag{1}
\]
All denominators have constant coefficient one, so formal inversion and differentiation are valid without analytic convergence assumptions.

**2. Recover unweighted overlaps from the finite counts.** Write \(D_w(z)=(1-qz)C_{0,w}(z)+z^m\). Setting \(y=1\) in (1) gives \(H_w=C_{0,w}/D_w\) and, by cross-multiplication,
\[
H_w(z)-H_v(z)=\frac{z^m\bigl(C_{0,w}(z)-C_{0,v}(z)\bigr)}{D_w(z)D_v(z)}.
\tag{2}
\]
The two \(C_0\) polynomials have degree at most \(m-1\); the factors in the denominator have constant coefficient one. Equality of the coefficients of \(H_w,H_v\) from length zero through \(2m-1\) therefore forces \(C_{0,w}=C_{0,v}=:C_0\). Consequently \(H_w=H_v=:H\) as full formal series.

**3. Recover the marked overlap data from the first moments.** Differentiating the reciprocal in (1) at \(y=1\) yields
\[
-\frac{J_w(z)}{H(z)^2}
=-z+z^m\left(\frac{h_w}{C_0(z)}-\frac{C_{1,w}(z)}{C_0(z)^2}\right).
\]
Taking the difference for \(w,v\),
\[
-\frac{J_w(z)-J_v(z)}{H(z)^2}
=\frac{z^m}{C_0(z)^2}
\left((h_w-h_v)C_0(z)-(C_{1,w}(z)-C_{1,v}(z))\right).
\tag{3}
\]
The polynomial in parentheses has degree at most \(m-1\); the other factors are invertible formal series with constant term one. Equality of the first moments through length \(2m-1\) therefore makes the polynomial identically zero. Its constant term is \(h_w-h_v\), since \(C_0(0)=1\) and both \(C_1\) polynomials have zero constant term. Thus \(h_w=h_v\) and \(C_{1,w}=C_{1,v}\).

At each exponent \(1\le d<m\), the coefficient of \(z^d\) in \(C_0\) says whether the overlap exists. If it exists, the coefficient of \(z^d\) in \(C_1\) is exactly \(r_{w,d}\), the number of marked letters in the appended suffix. Therefore equality of \(C_0\) and \(C_1\) gives the **whole** weighted polynomials \(C_w(z,y)=C_v(z,y)\), not merely their first derivatives. With equal \(h_w,h_v\), identity (1) gives \(F_w=F_v\), proving equality of every \(A_w(n,k)\). Conversely, equality of the complete spectra immediately gives equality of all \(N\) and \(M\), including the stated finite prefix.

**4. A sharp infinite family.** For each \(m\ge4\), take the binary words \(w_m\) consisting of `011` followed by \(m-3\) zeros and \(v_m\) consisting of `1` followed by \(m-2\) zeros and a final `1`. Both have exactly two ones, and each has only the proper self-border of length one. In terms of the definitions above,
\[
C_{0,w_m}=C_{0,v_m}=1+z^{m-1},\quad
C_{1,w_m}=2z^{m-1},\quad
C_{1,v_m}=z^{m-1}.
\]
Equation (2) gives \(N_{w_m}(n)=N_{v_m}(n)\) at every length. Equation (3), using \(h_{w_m}=h_{v_m}=2\), gives
\[
J_{w_m}(z)-J_{v_m}(z)
=z^{2m-1}\frac{H(z)^2}{(1+z^{m-1})^2}
=z^{2m-1}+O(z^{2m}).
\]
Hence the first marked-letter totals agree through \(2m-2\), but differ by exactly one at \(2m-1\). In the smallest case \(m=4\), the forbidden words are `0110` and `1001`; at length seven their \(N\) values are both \(97\), whereas their \(M\) values are \(340\) and \(339\).

**5. Boundary with two forbidden words.** Over \(\{0,1\}\), the language avoiding both `00` and `11` consists of the two alternating words at each positive length; the language avoiding both `01` and `10` consists of the two constant words. Both have \(N(n)=2\) and \(M(n)=n\) for every \(n\ge1\), yet already at \(n=2\) their marked-one generating polynomials are \(2y\) and \(1+y^2\), respectively. Thus first-moment rigidity is special to the one-factor setup.

## Verification

`verify_forbidden.py` implements two separate exact computations for each single forbidden factor: suffix-state dynamic programming and the recurrence obtained by expanding (1), both with integer coefficients. They agree for all binary forbidden words of lengths one through eight and all ternary forbidden words of lengths one through four: \(630\) patterns total, through host lengths nineteen and fourteen, respectively. A third implementation directly enumerates surviving words for \(932\) pattern-length instances. The script compares finite first-jet equivalence classes with full spectra in the tested ranges and checks the sharp witnesses for every \(4\le m\le10\). Its separate two-pattern test confirms equal first moments but different spectra. Run:

```text
python3 verify_forbidden.py
```

The included `verification_output.txt` records the expected successful checks. These computations corroborate the symbolic argument but do not replace the proof for unbounded \(m,n,q\).

## Relationship to prior work

Bóna, Maga and Richey (2026), Fact 2.9 and Corollary 2.11, provide an exact bivariate avoidance generating function and show that the same weighted border polynomial implies the same full marked-letter distribution. Equation (1) here is that known single-word weighted-cluster identity in a finite-alphabet normalization. The **additional statement** proved here runs in the other direction: a finite prefix of just the unweighted counts and the first marked-letter totals already forces equality of the entire weighted border polynomials and thus the full spectra. It also proves an optimal length threshold and demonstrates failure for two forbidden patterns; no new cluster expansion is claimed.

Carrigan, Hollars and Rowland (2024) provide the classical unweighted border-length characterization of avoidant equivalence, but this does not identify the marked-letter exponents from first moments. Myers (2009) develops weighted forbidden-factor generating functions for general forbidden sets, but the same inverse first-moment criterion and sharp finite cutoff are not stated in the sections compared. The 2024 preprint of Chandgotia, Marcus, Richey and Wu focuses on unweighted avoidance invariants and conjugacy, not the stated inverse criterion. The literature comparison establishes a best-knowledge distinction, not independent priority certification.

## Limitations

The theorem requires equal forbidden-word lengths, one forbidden word per language, and one common distinguished letter. The sharp-cutoff construction covers every \(m\ge4\); no sharpness assertion is made here for lengths one through three. The proof gives equality of histograms and generating functions, but does not supply a canonical weight-preserving bijection. Computation is finite corroboration; independent review and comprehensive publication-priority verification have not been performed.

## References

1. M. Bóna, B. Maga, J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655, first submitted June 4, 2026; Fact 2.9 and Corollary 2.11. https://arxiv.org/abs/2606.06655
2. J. Carrigan, I. Hollars, E. Rowland, *A natural bijection for contiguous pattern avoidance in words*, arXiv:2212.08959; *Discrete Mathematics* 347 (2024), 113793. https://arxiv.org/abs/2212.08959
3. A. N. Myers, *Forbidden Substrings on Weighted Alphabets*, arXiv:0906.3763 (2009). https://arxiv.org/abs/0906.3763
4. N. Chandgotia, B. Marcus, J. Richey, C. Wu, *Shifts of finite type obtained by forbidding a single pattern*, arXiv:2409.09024 (2024). https://arxiv.org/abs/2409.09024
