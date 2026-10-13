# Exact low-weight Roman-domination coefficients of cycle prisms

## Finding

Let \(P_n=C_n\square K_2\) be the cycle prism for an integer \(n\geq3\). A Roman dominating function is a labeling \(f:V(P_n)\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\). Write
\[
R_n(z)=\sum_{f\text{ Roman dominating}}z^{\sum_{v\in V(P_n)}f(v)}.
\]
For every \(n\geq4\), the two consecutive coefficients at weights \(n\) and \(n+1\) are exactly
\[
[z^n]R_n(z)=4\,\mathbf 1_{4\mid n},\qquad
[z^{n+1}]R_n(z)=\begin{cases}
6n,&n\equiv0\pmod4,\\
4n,&n\equiv1,3\pmod4,\\
2n,&n\equiv2\pmod4.
\end{cases}
\]
For the exceptional triangular prism \(n=3\), these coefficients are \([z^3]R_3(z)=0\) and \([z^4]R_3(z)=15\). In particular, the previously known minimum Roman weight is \(n\) when \(4\mid n\), and \(n+1\) otherwise. The number of minimum-weight functions is therefore \(4\) in the first case, \(2n\) for \(n\equiv2\pmod4\), \(4n\) for odd \(n\geq5\), and \(15\) for \(n=3\).

## Assumptions and scope

The graphs are finite, simple, labeled prisms with cyclic coordinates \(i\in\mathbb Z/n\mathbb Z\), two rail vertices in each column, two cycle edges per rail, and one rung edge. The theorem holds for every integer \(n\geq3\), and no assertion about differently twisted or higher-width ladders is made. Each labeling is counted once, without quotienting by graph automorphisms. The coefficient \([z^j]\) counts *all* valid labelings of total weight \(j\), not only those with labels \(0\) and \(2\).

## Proof

Enumerate the nine column labels as \(p=(p_0,p_1)\in\{0,1,2\}^2\), in lexicographic order, and use \(\iota(p)=3p_0+p_1\in\{0,\ldots,8\}\). Introduce \(81\) states \((p,q)\), where \(p,q\) are consecutive column labels. For three columns \(p,q,r\), let \(L(p,q,r)=1\) if and only if both of the following hold: whenever \(q_0=0\), at least one of \(p_0,q_1,r_0\) equals \(2\); whenever \(q_1=0\), at least one of \(p_1,q_0,r_1\) equals \(2\). Otherwise set \(L(p,q,r)=0\). Define an \(81\)-by-\(81\) polynomial matrix \(T(z)\) by
\[
T(z)_{(p,q),(q,r)}=L(p,q,r)z^{q_0+q_1},
\]
with zero entries elsewhere. Each valid cyclic sequence of \(n\) columns determines one closed walk of length \(n\), including its fixed first column; conversely every such walk determines exactly one valid Roman labeling. Hence, for \(n\geq3\),
\[
R_n(z)=\operatorname{tr}(T(z)^n).
\]

For a state \((p,q)\), define the integer potential \(h(p,q)\) by the following \(9\)-by-\(9\) table. Rows and columns are indexed by \(\iota(p)\) and \(\iota(q)\), respectively:

```text
-1 -1 -1 -1 -1 -1 -1 -1 -2
 0  0  0  0  0  0 -1 -1 -1
 0  0  0  0  0  0  0  0  0
 0  0 -1  0  0 -1  0  0 -1
 0  0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0  0
```

On each allowed transition \((p,q)\to(q,r)\), its reduced exponent
\[
e(p,q,r)=q_0+q_1-1+h(p,q)-h(q,r)
\]
is nonnegative. This is a finite inequality over all \(601\) allowed transitions, checked exactly by `verify.py`. Let \(B(z)\) be the transfer matrix using the monomial \(z^{e(p,q,r)}\) instead. For a closed walk, the potential differences telescope, giving
\[
\operatorname{tr}(B(z)^n)=z^{-n}R_n(z).
\]
Write \(B(z)=B_0+zB_1+z^2B_2+z^3B_3\), where the coefficient matrices have nonnegative integer entries. Since there are no negative exponents, coefficient extraction and cyclic invariance of trace give the two exact identities
\[
[z^n]R_n(z)=\operatorname{tr}(B_0^n),\qquad
[z^{n+1}]R_n(z)=n\operatorname{tr}(B_1B_0^{n-1}).
\]

Direct integer matrix multiplication from the displayed transition definition and potential yields the **entrywise identity** \(B_0^3=B_0^7\). The required initial traces are
\[
\begin{aligned}
\big(\operatorname{tr}(B_0^3),\ldots,\operatorname{tr}(B_0^6)\big)&=(0,4,0,0),\\
\big(\operatorname{tr}(B_1B_0^2),\ldots,\operatorname{tr}(B_1B_0^6)\big)&=(5,6,4,2,4).
\end{aligned}
\]
These are exact small matrix identities, not estimates. Multiplication of \(B_0^3=B_0^7\) by further powers proves that \(B_0^k=B_0^{k+4}\) for every \(k\geq3\). Thus the first trace sequence is four-periodic for \(n\geq3\), and the second is four-periodic from \(n\geq4\). Substitution yields every displayed coefficient formula, including the \(n=3\) exception. Since \(B(z)\) has nonnegative exponents, no Roman dominating function can have weight below \(n\). Positivity of the listed first available coefficient proves the minimum-weight statement, independently of its earlier proof in the literature.

## Verification

`verify.py` uses only Python's standard library. From the given graph definition and potential table it generates all \(601\) allowed transitions, checks all reduced exponents, constructs the exact integer matrices \(B_0,B_1\), checks \(B_0^3=B_0^7\) entry by entry, and recomputes every initial trace. It also independently enumerates all vertex labelings and all cyclic column words for \(n=3,4,5,6\), comparing **all** polynomial coefficients; the combined direct search covers \(597780\) vertex labelings. It checks the theorem's periodic coefficient formulas through \(n=100\) as supplementary finite confirmation. The unrestricted proof is the exact matrix identity plus its algebraic consequence, not this finite enumeration.

Run `python3 verify.py` from the directory containing the file. The program prints four `VERIFY_OK` lines or raises an assertion on any failure.

## Relationship to prior work

Pavlič and Žerovnik (2012, Section 5.3 and Figure 13) established the **minimum Roman-domination weight** of \(C_n\square P_2\): \(n\) for multiples of four, and \(n+1\) otherwise. Their explicit constructions are consistent with the present result, but the inspected theorem and accompanying figures do not count all optimal functions or give the next-weight coefficient. Deepak G. and collaborators (2021) introduced the Roman-domination polynomial and computed it for several other graph families and operations; their stated formulas do not specialize to the cycle prism. Allagan and collaborators (2026) count ordinary *minimum dominating vertex subsets* in prisms, not Roman \(\{0,1,2\}\)-labelings. For example, their published count is \(10\) ordinary minimum dominating subsets for \(n=5\), whereas the present Roman count is \(20\); for \(n=6\) those counts are \(51\) and \(12\), respectively. Therefore ordinary domination enumeration does not directly cover the stated Roman coefficient laws.

## Limitations

The calculation establishes only the two indicated consecutive coefficients and an exact transfer representation of the full Roman polynomial; it does **not** present a simplified closed rational form for the entire polynomial sequence. These formulas do not classify individual optimal functions up to dihedral or rail-exchange symmetry. Searches cannot exclude all equivalently formulated older enumerations, and independent mathematical audit has not been performed. No claim of priority or independent certification is made.

## References

1. P. Pavlič and J. Žerovnik, *Roman Domination Number of the Cartesian Products of Paths and Cycles*, Electronic Journal of Combinatorics 19(3), P19 (2012), published 2012-08-09, DOI 10.37236/2595. https://www.combinatorics.org/ojs/index.php/eljc/article/download/2595/pdf
2. Deepak G., Indiramma M. H., N. D. Soner, and Anwar Alwardi, *On the Roman Domination Polynomial of Graphs*, Bulletin of the International Mathematical Virtual Institute 11(2), 355–365 (2021). https://www.imvibl.org/buletin/bulletin_imvi_11_2_2021/bulletin_imvi_11_2_2021_355_365.pdf
3. J. Allagan, V. Deriglazov, R. N. Lopez-Bonilla, and K. Pereyra, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words* (2026), DOI 10.1155/ijmm/1411005; precursor arXiv:2601.03488. https://onlinelibrary.wiley.com/doi/10.1155/ijmm/1411005
