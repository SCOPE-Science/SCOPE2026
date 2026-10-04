# A subfield-trivial character forces monomial compressed Fourier transforms in quadratic fields
## Finding
Let \(p\) be an odd prime and let \(m\ge4\) divide \(p+1\), with \(m<p+1\). Set
\[
K=\mathbb F_{p^2},\qquad H=(K^\times)^m.
\]
Then \(H\) is the unique index-\(m\) subgroup of \(K^\times\), and
\[
\mathbb F_p^\times\subset H,\qquad
\left|H/\mathbb F_p^\times\right|=\frac{p+1}{m}.
\]

Let \(\chi:H\to\mathbb C^\times\) be nontrivial and trivial on \(\mathbb F_p^\times\). For the standard unnormalized compressed Fourier matrix
\[
M_{\chi}(r,s)=\varepsilon_s(u_{\chi,r})
=\sum_{h\in H}\chi(h)\,
\exp\!\left(\frac{2\pi i}{p}\operatorname{Tr}_{K/\mathbb F_p}(shr)\right),
\]
with \(r\) and \(s\) ranging over representatives of the nonzero \(H\)-orbits, exactly one entry in each row and exactly one entry in each column is nonzero. Every nonzero entry has modulus \(p\). Consequently
\[
|\det M_{\chi}|=p^m,
\]
while exactly \(m^2-m\) of its \(1\times1\) minors vanish. Thus the compressed Fourier matrix fails the nonvanishing-minors property in the strongest possible entrywise way compatible with invertibility.

There are exactly
\[
\frac{p+1}{m}-1
\]
such nontrivial characters \(\chi\).

## Assumptions and scope
The Fourier matrix convention is the unnormalized convention used in the compressed-transform formula
\[
\varepsilon_s(u_{\chi,r})=\sum_{h\in H}\chi(h)\varepsilon(shr).
\]
Multiplying the full matrix, rows, or columns by nonzero scalars does not affect the support pattern or the nonvanishing-minors conclusion.

The theorem is restricted to quadratic extensions \(K=\mathbb F_{p^2}\), indices \(m\ge4\) satisfying \(m\mid p+1\) and \(m<p+1\), and nontrivial characters that are trivial on the prime-field multiplicative subgroup. It does not classify the remaining characters of \(H\), nor indices not dividing \(p+1\).

## Proof
Because \(K^\times\) is cyclic of order \((p-1)(p+1)\), and \(m\mid p+1\), the subgroup
\[
\mathbb F_p^\times
\]
is contained in \(H\). The quotient \(H/\mathbb F_p^\times\) therefore has order \((p+1)/m\). A character of \(H\) is trivial on \(\mathbb F_p^\times\) exactly when it descends to this quotient, so the number of eligible nontrivial characters is \((p+1)/m-1\).

Fix one such \(\chi\). Write
\[
\psi(x)=\exp\!\left(\frac{2\pi i}{p}\operatorname{Tr}_{K/\mathbb F_p}(x)\right).
\]
For \(z\in K^\times\), define
\[
A(z)=\sum_{h\in H}\chi(h)\psi(zh).
\]
The matrix entry with orbit representatives \(r,s\) is \(A(rs)\).

Partition \(H\) into the one-dimensional \(\mathbb F_p\)-subspaces contained in it. Since \(\mathbb F_p^\times\subset H\), these nonzero projective lines are the cosets \(t\mathbb F_p^\times\), with \(t\) ranging over \(H/\mathbb F_p^\times\). The character \(\chi\) is constant on each such line.

The trace kernel
\[
L_0=\{x\in K:\operatorname{Tr}_{K/\mathbb F_p}(x)=0\}
\]
is one-dimensional over \(\mathbb F_p\). Thus \(L_0^\times\) is exactly one projective line. For a line \(t\mathbb F_p^\times\),
\[
\sum_{c\in\mathbb F_p^\times}\psi(ztc)
=
\begin{cases}
p-1,&zt\in L_0,\\
-1,&zt\notin L_0.
\end{cases}
\]
The first case occurs for exactly one line in the coset \(zH\) if \(zH\) contains \(L_0^\times\), and for no line otherwise.

Because \(\chi\) induces a nontrivial character on \(H/\mathbb F_p^\times\),
\[
\sum_{t\in H/\mathbb F_p^\times}\chi(t)=0.
\]
If \(zH\) does not contain \(L_0^\times\), every projective-line contribution has the factor \(-1\), hence \(A(z)=0\). If \(zH\) contains \(L_0^\times\), let \(t_0\mathbb F_p^\times\) be the unique line with \(zt_0\in L_0^\times\). Then
\[
A(z)
=(p-1)\chi(t_0)-\sum_{t\ne t_0}\chi(t)
=p\chi(t_0).
\]
Therefore
\[
|A(z)|=
\begin{cases}
p,&zH=L_0^\times H,\\
0,&zH\ne L_0^\times H.
\end{cases}
\]

The nonzero \(H\)-orbits form the cyclic quotient \(K^\times/H\) of order \(m\). For a fixed row orbit \(sH\), the condition that \(rsH\) equal the distinguished orbit \(L_0^\times H\) selects exactly one column orbit \(rH\), and conversely. Hence the compressed matrix is monomial. Its \(m\) nonzero entries all have modulus \(p\), so its determinant has modulus \(p^m\), while the other \(m^2-m\) entries are zero.

## Verification
The accompanying `verify.py` uses exact finite-field arithmetic in quadratic models \(\mathbb F_p[\alpha]\) and checks the projective-line mechanism for every admissible index \(m\ge4\) for
\[
p\in\{7,11,19,23,31,43,47,59\}.
\]
For each pair \((p,m)\), it constructs a primitive element, the index-\(m\) subgroup \(H\), the embedded subgroup \(\mathbb F_p^\times\), and all \(m\) nonzero \(H\)-orbits. It verifies that the trace-zero projective line belongs to exactly one orbit and that each other orbit contains none, so the derived character sum has exactly the monomial support pattern. It also verifies the quotient size \((p+1)/m\) and the count of eligible nontrivial characters.

The program prints `VERIFY_OK`. These finite checks are consistency tests. The universal result is proved by the projective-line argument above.

## Relationship to prior work
Garcia, Karaali, and Katz introduced compressed Fourier matrices and proved the general entry formula in terms of Gaussian sums. They also proved that when \(H\) is contained in a proper subfield, every character fails the nonvanishing-minors property. That obstruction does not apply here: for \(m<p+1\),
\[
|H|=\frac{p^2-1}{m}>p-1,
\]
so \(H\) is not contained in the only proper subfield \(\mathbb F_p\) of \(K=\mathbb F_{p^2}\).

Their complete non-prime-field results treat indices \(2\) and \(3\). Díaz Padilla's 2023 thesis records finite index-\(4\) computations for \(\mathbb F_{49}\) and \(\mathbb F_{25}\), and explicitly leaves larger-index characterizations for both trivial and nontrivial characters as an open direction. The theorem here supplies a uniform infinite family for every index \(m\ge4\): whenever \(p\equiv-1\pmod m\) and \(m<p+1\), all nontrivial characters descending through \(H/\mathbb F_p^\times\) produce a monomial compressed matrix.

Targeted searches for the phrases "compressed Fourier monomial matrix", "character trivial on \(\mathbb F_p^\times\)", "trace-zero line compressed Fourier", and the parameter condition \(m\mid p+1\) found no published statement implying this larger-index result.

## Limitations
No claim is made that the displayed family exhausts all larger-index failures. Characters nontrivial on \(\mathbb F_p^\times\) can have very different compressed matrices. The literature search cannot exclude an unindexed result phrased entirely in relative Gauss-sum language.

The theorem concerns the nonvanishing-minors property, not a full classification of support-equality cases for the associated uncertainty principle.

## References
1. S. R. Garcia, G. Karaali, and D. J. Katz, "An improved uncertainty principle for functions with symmetry," arXiv:1807.07648, first posted 19 July 2018.
2. D. F. Díaz Padilla, "An Uncertainty Principle for Functions with Symmetries over Finite Fields," bachelor's thesis, Pontificia Universidad Javeriana, 2023.
3. D. F. Díaz Padilla and J. A. Ochoa Arango, "On an uncertainty principle for small index subgroups of finite fields," arXiv:2310.09992, first posted 16 October 2023.
