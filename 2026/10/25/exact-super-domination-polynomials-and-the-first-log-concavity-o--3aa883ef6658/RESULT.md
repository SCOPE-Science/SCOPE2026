# Exact super-domination polynomials and the first log-concavity obstruction among radius-two spider trees

## Finding

Let \(T_{a,b}\) be the radius-two spider with one center, \(a\) length-one arms and \(b\) length-two arms, for integers \(a,b\ge0\). For the super-domination polynomial \(\mathcal P_{a,b}(z)=\sum_{D\text{ super dominating}}z^{|D|}\), we prove

\[
\mathcal P_{a,b}(z)=\begin{cases}
z^{a+b}\bigl((a+1)(1+z)^b+z(2+z)^b\bigr),&a\ge1,\\
z^b\bigl((1+z)^b-1+z(2+z)^b\bigr),&a=0.
\end{cases}
\]

After removal of initial zero coefficients, the coefficient sequence is log-concave for **all** \(a\ge0\) whenever \(0\le b\le43\). The bound on \(b\) is sharp: at \(b=44\), \(a=2^{24}-1\), the shifted coefficients at indices \(20,21,22\) violate log-concavity. This is the first arm-length-two count admitting a counterexample, not a claim that every larger \(b\) fails.

## Assumptions and scope

Graphs are finite simple undirected trees, with each vertex distinguished. A subset \(D\subseteq V(G)\) is **super dominating** if every omitted vertex \(u\in V(G)\setminus D\) has a selected neighbor \(v\in D\) satisfying \(N_G(v)\cap(V(G)\setminus D)=\{u\}\). The empty omitted set is allowed, so the full vertex set is counted. The polynomial counts actual subsets, not isomorphism orbits. Log-concavity for nonnegative coefficients \(c_0,\ldots,c_d\) means \(c_k^2\ge c_{k-1}c_{k+1}\) at all internal indices after leading zeros have been stripped.

## Proof

Write the center as \(h\), its \(a\) adjacent leaves as \(\ell_j\), and each two-edge arm as \(h-v_i-w_i\). Partition super-dominating sets by whether \(h\) is selected.

**Center omitted.** Each direct leaf \(\ell_j\) must be selected. Also each endpoint \(w_i\) must be selected: if \(w_i\) were omitted, only \(v_i\) could witness it, but \(v_i\) is also adjacent to omitted \(h\), so it could not witness \(w_i\). Each \(v_i\) can then be chosen independently. If \(a\ge1\), a selected direct leaf witnesses \(h\). If \(a=0\), at least one intermediate vertex \(v_i\) must be selected to witness \(h\). The resulting contributions are \(z^{a+b}(1+z)^b\) and \(z^b((1+z)^b-1)\), respectively.

**Center selected.** At most one direct leaf can be omitted; otherwise neither omitted leaf has a unique witness. If none is omitted, every two-edge arm has exactly three allowed states for \((v_i,w_i)\): selected/omitted, omitted/selected, or selected/selected, contributing \(2z+z^2\) per arm. The total is \(z^{a+1}(2z+z^2)^b=z^{a+b+1}(2+z)^b\). If exactly one direct leaf is omitted, \(h\) must witness it, so every \(v_i\) must be selected and every \(w_i\) is arbitrary. Choosing the omitted direct leaf in \(a\) ways gives \(az^a(z+z^2)^b=az^{a+b}(1+z)^b\). All listed configurations satisfy the original definition, and every super-dominating set lies in one listed case. Summing proves the polynomial identities, including \(a=b=0\).

**Sharp log-concavity threshold.** For \(a\ge1\), factor out \(z^{a+b}\). Put \(t=a+1\) and define, with binomial coefficients outside their natural range taken as zero,
\[
A_k=\binom bk,\qquad B_k=2^{b-k+1}\binom b{k-1},\qquad c_k=tA_k+B_k,\quad 0\le k\le b+1.
\]
The inner expression \(L_k(t)=c_k^2-c_{k-1}c_{k+1}\), for \(1\le k\le b\), is the quadratic \(p_k t^2+q_k t+r_k\), where
\[
\begin{aligned}
p_k&=A_k^2-A_{k-1}A_{k+1},\\
q_k&=2A_k B_k-A_{k-1}B_{k+1}-A_{k+1}B_{k-1},\\
r_k&=B_k^2-B_{k-1}B_{k+1}.
\end{aligned}
\]
Both \(p_k,r_k\) are nonnegative by binomial log-concavity. The attached standalone exact integer verifier checks all \(946\) internal pairs \((b,k)\), \(0\le b\le43\), \(1\le k\le b\), and establishes \(q_k\ge0\) or \(q_k^2\le4p_kr_k\). This makes \(L_k(t)\ge0\) for **all real** \(t\ge0\) (the quadratic is nonnegative on the nonnegative half-line). Thus it proves the result for infinitely many \(a\) without sampling them. For \(a=0\), factor out \(z^{b+1}\) and obtain \(d_j=\binom b{j+1}+2^{b-j}\binom bj\), \(0\le j\le b\). The verifier independently establishes the \(903\) required adjacent inequalities for all \(b\le43\), again by exact integer arithmetic.

For \(b=44\), \(a=2^{24}-1\), the three shifted coefficients at indices \(20,21,22\) are
\[
(c_{20},c_{21},c_{22})=(76817877657622413312,63311437629908582400,52183972834348892160).
\]
Direct multiplication gives
\[
c_{20}c_{22}-c_{21}^2=323906111900267026871809275246673920>0,
\]
so \(c_{21}^2<c_{20}c_{22}\) and log-concavity fails. Together with the exhaustive symbolic b-bound this establishes sharpness.

## Verification

Run \(\texttt{python3 verify.py}\) using only Python standard-library integer arithmetic. The verifier directly enumerates all original-definition subsets for \(0\le a,b\le4\) (25 graphs and 21,142 subsets), checks every coefficient against the formula, proves 946 uniform-in-\(a\) quadratic conditions, checks 903 direct \(a=0\) inequalities, and reproduces the exact 44-arm counterexample. The expected output is in \(\texttt{verification\_output.txt}\). The global result relies on the disjoint case proof plus a finite **complete**, exact symbolic certificate; no finite experiment is passed off as an infinite proof.

## Relationship to prior work

Ghanbari, Jäger and Lehtilä's 2022 super domination work introduced relevant graph-family enumeration methods and minimum configurations; Bujtás, Ghanbari and Klavžar's 2023 paper established matching-based minimum super domination for trees. Those minimum values and the previously known minimum-configuration special cases are not claimed here as new. The contribution is the complete polynomial for every cardinality and the exact, uniform 43/44 boundary for coefficient log-concavity. A later 2024 chapter by Kaidash specifically studies super domination polynomials, but its full text was inaccessible; its abstract is not enough to exclude a covering formula. This residual priority risk should be kept in mind.

## Limitations

The sharp threshold is for this radius-two spider family, not all trees or other domination invariants. The 44-arm failure uses a very large number of length-one arms; no minimality of that secondary parameter is claimed. A certificate with 1,849 finite inequalities is computer-assisted but uses auditable exact formulas and unbounded-in-\(a\) reasoning. Bibliographic priority has not been independently confirmed, and independent scientific audit has not been performed.

## References

1. M. Ghanbari, J. Jäger, T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795v1, first publicly posted 2022-09-05, https://arxiv.org/abs/2209.01795.
2. Cs. Bujtás, M. Ghanbari, S. Klavžar, *Computational complexity aspects of super domination*, arXiv:2302.08862v1, https://arxiv.org/abs/2302.08862.
3. O. Kaidash, *Super Domination Polynomial of a Graph*, DOI 10.1007/978-3-031-73365-9_6 (2024), abstract inspected, full text not inspected.
