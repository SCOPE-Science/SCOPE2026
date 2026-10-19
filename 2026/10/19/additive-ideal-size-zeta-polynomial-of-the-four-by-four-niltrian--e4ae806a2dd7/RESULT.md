# Additive ideal-size zeta polynomial of the four-by-four niltriangular ring over every finite field

## Finding

For a prime \(p\), an integer \(m\ge 1\), and \(q=p^m\), let \(R=\mathfrak{ut}_4(\mathbf F_q)\) denote the six-dimensional associative (nonunital) ring of strictly upper triangular \(4\)-by-\(4\) matrices. Its **additive two-sided ideals** are additive subgroups \(I\le (R,+)\) stable under both left and right multiplication by every element of \(R\). These subgroups need not be \(\mathbf F_q\)-linear when \(m>1\). Define the size-refined polynomial
\[
F_{p,m}(z)=\sum_{I\triangleleft R}z^{\dim_{\mathbf F_p}I}.
\]
For \(d\ge0\), set \(G_d(z)=\sum_{j=0}^d{d\brack j}_p z^j\), where \({d\brack j}_p\) denotes the Gaussian binomial coefficient, with \({d\brack j}_p=0\) outside \(0\le j\le d\). Then, for every prime and positive extension degree,
\[
\boxed{F_{p,m}(z)=G_m(z)+z^m(G_{2m}(z)-1)+z^{3m}(G_{3m}(z)-1)
+2z^{2m}\sum_{r=0}^{m-1}{m\brack r}_p z^r\bigl(G_m(p^{m-r}z)-1\bigr).}
\]
In particular, for the first nonprime field \(\mathbf F_4\),
\[
\begin{aligned}
F_{2,2}(z)={}&1+3z+z^2+15z^3+35z^4+39z^5+69z^6\\
&+87z^7+651z^8+1395z^9+651z^{10}+63z^{11}+z^{12}.
\end{aligned}
\]
Consequently the ring over \(\mathbf F_4\) has exactly \(3011\) additive two-sided ideals, but only \(59\) of these are \(\mathbf F_4\)-linear. The prime-field (equivalently \(m=1\)) specialization gives \(F_{p,1}(1)=2p^2+5p+7\); that specialization is a comparison with prior prime-field theory, **not** a claimed new result.

## Assumptions and scope

The coefficient ring is exactly \(\mathbf F_{p^m}\); there is no restriction on the prime, including characteristic two. Ideals mean additive normal subgroups stable under two-sided products, rather than the narrower class of scalar-linear \(\mathbf F_q\)-subspaces. The exponent of \(z\) records \(\mathbf F_p\)-dimension, so its range is \(0\) through \(6m\). The result also enumerates ideals of the canonical two-sided radical brace associated with \(R\), via \(x\circ y=x+y+xy\).

## Proof

**1. Central-socle dichotomy.** Write \(a=E_{12},b=E_{23},c=E_{34},d=E_{13},e=E_{24},f=E_{14}\). The only nonzero basis products are \(ab=d\), \(bc=e\), \(ae=f\), and \(dc=f\). Let \(C=\mathbf F_q f\). It annihilates the ring on both sides, hence every additive \(\mathbf F_p\)-subspace of \(C\) is an ideal. If an ideal \(I\) contains \(v\notin C\), some one of the first five coordinates of \(v\) is nonzero. A nonzero \(a\)-coordinate yields \(v e\ne0\) in \(C\), a nonzero \(b\)-coordinate yields \((a v)c\ne0\) in \(C\), a nonzero \(c\)-coordinate yields \(d v\ne0\) in \(C\); if the first three are zero, a nonzero \(d\)-coordinate yields \(v c\ne0\) in \(C\), and otherwise a nonzero \(e\)-coordinate yields \(a v\ne0\) in \(C\). Since one may scale the outer ring multiplier by an arbitrary element of \(\mathbf F_q\), in each case all of \(C\) belongs to \(I\). Thus every ideal either lies inside \(C\), or contains \(C\). The latter are inverse images of additive two-sided ideals of \(B=R/C\). The overlap is the single ideal \(C\), so
\[
F_{p,m}(z)=G_m(z)+z^m\bigl(F_B(z)-1\bigr).
\]

**2. Two-step quotient.** In \(B\), set \(W=\mathbf F_q d\oplus\mathbf F_q e\) and \(U=\mathbf F_q a\oplus\mathbf F_q b\oplus\mathbf F_q c\); then \(W\) annihilates \(B\) and the only nonzero basic products are \(ab=d\), \(bc=e\). Let \(J\triangleleft B\). Set \(T=J\cap W\), and \(S=\operatorname{pr}_U(J)\). They are \(\mathbf F_p\)-subspaces, and \(J/T\) is the graph of a unique \(\mathbf F_p\)-linear map \(S\to W/T\). Conversely every such graph defines an ideal exactly when \(BS+SB\subseteq T\). For fixed \(T\), every admissible \(S\) therefore contributes \(p^{(2m-\dim_pT)\dim_pS}\) possible ideals.

**3. Exhaustive admissible pairs.** Put \(D=\mathbf F_q d\) and \(E=\mathbf F_q e\). The two products imply: if \(T\) does not contain all of \(D\), every vector of \(S\) has zero \(a\)- and \(b\)-coordinates; if \(T\) does not contain all of \(E\), every vector of \(S\) has zero \(b\)- and \(c\)-coordinates. Hence:

- If \(T\) contains neither \(D\) nor \(E\), then \(S=0\).
- If \(T\supseteq D\) but \(T\not\supseteq E\), then \(S\) is any \(\mathbf F_p\)-subspace of \(\mathbf F_q a\). The symmetric case exchanges \(D,a\) with \(E,c\).
- If \(T\supseteq D+E=W\), then \(T=W\) and \(S\) is any \(\mathbf F_p\)-subspace of all of \(U\).

All \(\mathbf F_p\)-subspaces \(T\subseteq W\) with \(S=0\) give \(G_{2m}(z)\). For \(T=W\) and \(S\ne0\) the contribution is \(z^{2m}(G_{3m}(z)-1)\). If \(D\subseteq T\) and \(E\not\subseteq T\), then \(T/D\subseteq W/D\) has some \(r\in\{0,\ldots,m-1\}\) and can be chosen in \({m\brack r}_p\) ways. A nonzero \(s\)-dimensional \(S\subseteq\mathbf F_q a\) is chosen in \({m\brack s}_p\) ways and permits \(p^{(m-r)s}\) graph maps. The total of these two symmetric cases is
\[
2\sum_{r=0}^{m-1}{m\brack r}_p z^{m+r}\bigl(G_m(p^{m-r}z)-1\bigr).
\]
Combining the three mutually disjoint contributions yields
\[
F_B(z)=G_{2m}(z)+z^{2m}(G_{3m}(z)-1)
+2\sum_{r=0}^{m-1}{m\brack r}_p z^{m+r}\bigl(G_m(p^{m-r}z)-1\bigr).
\]
Substitution in Step 1 proves the displayed formula, with no omitted ideals.

**4. Comparison of scalar-linear ideals.** Restricting all subgroup choices to \(\mathbf F_q\)-linear subspaces repeats the same classification with one-dimensional field coordinates. The number is \(2q^2+5q+7\). At \(q=4\) this is \(59\), whereas counting all additive ideals by the stated polynomial gives \(3011\).

## Verification

The standalone program `verify_gf4.py` represents \(\mathbf F_4\) by the binary polynomial basis with \(\alpha^2=\alpha+1\), and enumerates all additive two-sided ideals independently by generating principal ideals from the \(4096\) elements and taking joins. It obtains exactly \(3011\) ideals with the complete coefficient distribution above; it then directly tests both-sided multiplication closure of every one of them and counts exactly \(59\) scalar-linear ideals. The separate `verify_prime.py` enumerates all reduced-row-echelon subspaces for \(q=2,3\), directly tests multiplication closure, and obtains \(25\) and \(40\) ideals with the predicted size profiles. Both files use only the Python standard library. Run `python verify_gf4.py` and `python verify_prime.py` in a directory containing the embedded files. These finite enumerations check examples and do not replace the all-field proof.

## Relationship to prior work

Marberg's *A supercharacter analogue for normality* (arXiv:1005.4150, 2010), Section 4 and Theorem 4.1, develops the classification of supernormal subgroups/associative two-sided ideals for unitriangular groups and a counting formula **when the field order is prime**. The prime-field total \(2p^2+5p+7\) is consistent with, and not presented as independent of, this prior work. The distinctive result here is the exact \(\mathbf F_p\)-additive ideal-size distribution for all extension degrees \(m>1\); restricting to \(\mathbf F_q\)-linear subspaces misses thousands of ideals already at \(q=4\). Konovalov, Smoktunowicz and Vendramin's *On skew braces and their ideals* (arXiv:1804.04106, initial public version 2018-04-11) connects two-sided radical rings and brace ideals and motivates the invariant, without an inspected formula for this family. The two directions of ideal multiplication are essential: Lie ideals of the same underlying niltriangular vector space are a different invariant.

## Limitations

The result covers only \(4\)-by-\(4\) strictly upper triangular rings; no formula for arbitrary matrix size is claimed. An additive-ideal classification is not a classification of all normal subgroups of the corresponding unitriangular group. The originality assessment is based on inspected literature and indexed searches, not a proof of absence of equivalent statements in unindexed algebra-ideal literature. Verification for finite small fields is not exhaustive for general parameters. Independent mathematical auditing has not been performed.

## References

1. A. Konovalov, A. Smoktunowicz, L. Vendramin, *On skew braces and their ideals*, arXiv:1804.04106 (first public version 2018-04-11), DOI:10.1080/10586458.2018.1492476.
2. E. Marberg, *A supercharacter analogue for normality*, arXiv:1005.4150 (2010), especially Section 4, Theorem 4.1; DOI:10.1016/j.jalgebra.2011.02.019.
