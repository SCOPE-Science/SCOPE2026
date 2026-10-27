# Idempotent rank profiles and a weak–strong split for partial star endomorphisms

## Finding

Let \(S_{m+1}=K_{1,m}\) be the loopless star with center \(0\) and \(m\geq 1\) labeled leaves. For any monoid \(M\) of partial transformations of its vertices, let
\[
E_M^{(m)}(z)=\sum_{\substack{f\in M\\ f^2=f}}z^{|\operatorname{im}f|}.
\]
Define the explicit polynomials
\[
 A_m(z)=\sum_{r=0}^{m}\binom mr(r+1)^{m-r}z^r,
 \qquad
 B_m(z)=\sum_{r=0}^{m}\binom mr(r+2)^{m-r}z^r.
\]
For all \(m\geq1\), the six standard partial graph-transformation monoids satisfy
\[
\begin{aligned}
 E_{\mathrm{PEnd}}^{(m)}(z)=E_{\mathrm{PsEnd}}^{(m)}(z)&=(1+z)A_m(z),\\
 E_{\mathrm{PwEnd}}^{(m)}(z)&=A_m(z)+zB_m(z)+m2^{m-1}z,\\
 E_{\mathrm{PswEnd}}^{(m)}(z)&=(1+z)A_m(z)+(2^m-1+m2^{m-1})z,\\
 E_{\mathrm{IEnd}}^{(m)}(z)=E_{\mathrm{PAut}}^{(m)}(z)&=(1+z)^{m+1}.
\end{aligned}
\]
More strongly, \(\mathrm{PEnd}(S_{m+1})\) and \(\mathrm{PsEnd}(S_{m+1})\) have **identical idempotent sets**, not just the same counts. Every idempotent in \(\mathrm{PswEnd}\setminus\mathrm{PEnd}\) has image rank one, while \(\mathrm{PwEnd}\setminus\mathrm{PswEnd}\) has idempotents of ranks greater than one for \(m\geq2\). The exact difference polynomials are
\[
 \begin{aligned}
 E_{\mathrm{PswEnd}}^{(m)}(z)-E_{\mathrm{PEnd}}^{(m)}(z)&=(2^m-1+m2^{m-1})z,\\
 E_{\mathrm{PwEnd}}^{(m)}(z)-E_{\mathrm{PswEnd}}^{(m)}(z)
 &=\sum_{r=1}^{m}\binom mr\big((r+2)^{m-r}-(r+1)^{m-r}\big)z^{r+1}.
 \end{aligned}
\]
Their exponential generating functions in the leaf count are
\[
 \sum_{m\geq0}A_m(z)\frac{t^m}{m!}=\exp(t+zt e^t),\qquad
 \sum_{m\geq0}B_m(z)\frac{t^m}{m!}=\exp(2t+zt e^t).
\]
Finally, with \(\#E(M)\) denoting the total number of idempotents,
\[
\lim_{m\to\infty}\frac{\#E(\mathrm{PsEnd}(S_{m+1}))}{\#E(\mathrm{PwEnd}(S_{m+1}))}=0,
\qquad
\lim_{m\to\infty}\frac{\#E(\mathrm{PEnd}(S_{m+1}))}{\#E(\mathrm{PswEnd}(S_{m+1}))}=1.
\]
Thus weak graph morphisms create an asymptotically dominant idempotent population absent from strong graph morphisms, whereas the additional idempotents permitted by the strong-weak condition are asymptotically negligible.

## Assumptions and scope

All stars are finite, undirected, loopless and labeled. A *partial transformation* \(f:D\to V\) has arbitrary domain \(D\subseteq V\); its image rank is \(|\operatorname{im}f|\). The empty transformation is an idempotent of rank zero. In \(\mathrm{PEnd}\), any edge with both ends in the domain must map to an edge; in \(\mathrm{PwEnd}\), the same is required only when the two images differ. In \(\mathrm{PsEnd}\), an unordered pair in the domain is an edge if and only if its image pair is an edge. In \(\mathrm{PswEnd}\), the equivalence applies to pairs that form edges and whose images differ. The injective partial endomorphism monoid is \(\mathrm{IEnd}\); partial graph automorphisms form \(\mathrm{PAut}\). These conventions agree with the cited 2024 source. In the formula for \(\mathrm{PswEnd}\), the intended condition is equivalently: for every two domain vertices \(u,v\), the statement “\(\{u,v\}\) is an edge and \(f(u)\ne f(v)\)” holds exactly when “\(\{f(u),f(v)\}\) is an edge” holds.

## Proof

**1. General idempotents.** For any partial transformation \(f:D\to V\), the identity \(f^2=f\) is equivalent to \(\operatorname{im}f\subseteq D\) and \(f(y)=y\) for every \(y\in\operatorname{im}f\). Indeed, equality as partial maps forces every image value to be in the domain, and evaluation at \(x\in D\) then yields \(f(f(x))=f(x)\); the converse is immediate. In particular, the image is precisely the fixed-point set inside \(D\).

**2. Center absent.** If \(0\notin D\), then the image of an idempotent cannot contain \(0\). Hence its domain and image lie in the edgeless leaf set, and it automatically belongs to all four noninjective graph-homomorphism monoids. Choose \(r\) fixed leaves, and, for each of the other \(m-r\) leaves, choose absence from the domain or one of the \(r\) fixed leaves as its image. This gives the contribution \(A_m(z)\), including the empty map at \(r=0\).

**3. Center fixed.** Suppose \(0\in D\) and \(f(0)=0\). Let \(R\) be the set of fixed leaves, with \(|R|=r\). For \(\mathrm{PEnd}\), all other included leaves must map into \(R\), not to \(0\), because an edge cannot collapse to a loop. There are \(\binom mr(r+1)^{m-r}\) such idempotents of rank \(r+1\). Every such map is also strong: center-leaf edges remain edges and pairs of leaves remain nonedges. Their contribution to either \(\mathrm{PEnd}\) or \(\mathrm{PsEnd}\) is \(zA_m(z)\).

For \(\mathrm{PwEnd}\), each nonfixed leaf can additionally map to the center, leaving \(r+2\) choices (absent, center, or one of the \(r\) fixed leaves). Thus the contribution is \(zB_m(z)\). In \(\mathrm{PswEnd}\), a fixed leaf in \(R\) and another leaf mapping to \(0\) would be a nonedge with adjacent images; this is forbidden. Consequently, if \(r\geq1\), every included leaf maps to \(R\), giving the same \(z(A_m(z)-1)\) contribution as the strict case. If \(r=0\), every leaf is absent or maps to \(0\), giving exactly \(2^m\) rank-one maps. The total center-fixed contribution to \(\mathrm{PswEnd}\) is \(z(A_m(z)-1+2^m)\).

**4. Center moves.** Suppose \(0\in D\) and \(f(0)=v\ne0\). Since \(f\) is idempotent, \(v\in D\) and \(f(v)=v\); also \(0\) is not fixed and hence cannot occur in the image. The edge \(\{0,v\}\) collapses, so there is no such strict or strong idempotent. The weak condition forces every included leaf to map either to \(0\) or to \(v\); idempotency rules out \(0\), so every included leaf maps to \(v\). Conversely, these maps satisfy both the weak and the strong-weak conditions. Choose \(v\) in \(m\) ways and include any subset of the other \(m-1\) leaves: there are \(m2^{m-1}\) rank-one maps.

**5. Injective cases and summation.** An injective idempotent partial map fixes every element of its domain, so it is a partial identity. Every partial identity is a graph partial automorphism. There are \(\binom{m+1}{r}\) of rank \(r\), giving \((1+z)^{m+1}\). Summing the three disjoint cases above proves all six polynomial identities, their equality of strict/strong idempotent sets, and the exact difference polynomials. The second difference is obtained by subtracting the \(r=0\) term \(2^m-1\) from \(B_m(z)-A_m(z)\). For \(m\geq2\), its coefficient of \(z^2\) is positive, proving the claimed higher-rank distinction.

**6. Exponential generating functions.** For \(c\in\{1,2\}\), write \(m=r+k\) and sum absolutely as a formal power series:
\[
\sum_{m\geq0}\sum_{r=0}^m\binom mr(r+c)^{m-r}z^r\frac{t^m}{m!}
=\sum_{r\geq0}\frac{(zt)^r}{r!}\exp((r+c)t)
=\exp(ct+zt e^t).
\]
This proves both asserted generating functions.

**7. Asymptotic dichotomy.** Put \(a_m=A_m(1)\) and \(b_m=B_m(1)\). First \(a_m/(m2^m)\to\infty\): taking \(r_0=\lfloor m/\log m\rfloor\) in the nonnegative sum for \(a_m\) shows
\[
\log a_m\geq(m-r_0)\log(r_0+1)
=m\log m-m\log\log m-O(m),
\]
which exceeds \(\log(m2^m)=O(m)\) by an unbounded multiple of \(m\). Hence
\[
\frac{2a_m}{2a_m+2^m-1+m2^{m-1}}\longrightarrow1.
\]
Next take \(R=\lceil m/\sqrt{\log m}\rceil\). The part of \(a_m\) with \(r>R\) is at most \((m+1)2^m(m+1)^{m-R}\). Comparing its logarithm, \(m\log m-m\sqrt{\log m}+O(m)\), with the preceding lower bound on \(\log a_m\), shows that this tail is \(o(a_m)\). For every \(r\leq R\),
\[
\frac{(r+2)^{m-r}}{(r+1)^{m-r}}
\geq\left(1+\frac1{R+1}\right)^{m-R}\longrightarrow\infty.
\]
Thus \(b_m/a_m\to\infty\). The identities \(\#E(\mathrm{PwEnd})=a_m+b_m+m2^{m-1}\) and \(\#E(\mathrm{PsEnd})=2a_m\) yield the other limit.

## Verification

The accompanying standalone script `verify_star_idempotents.py` independently enumerates all partial transformations on stars with \(1\leq m\leq6\) leaves. It tests idempotence and the defining edge-preservation predicates directly, builds rank histograms for each of the six monoids, and compares the results with the claimed formulas. The verified total-idempotent vectors in the order \((\mathrm{PEnd},\mathrm{PwEnd},\mathrm{PsEnd},\mathrm{PswEnd},\mathrm{IEnd},\mathrm{PAut})\) are:
\[
\begin{array}{c|rrrrrr}
m&\mathrm{PEnd}&\mathrm{PwEnd}&\mathrm{PsEnd}&\mathrm{PswEnd}&\mathrm{IEnd}&\mathrm{PAut}\\\hline
1&4&6&4&6&4&4\\
2&12&21&12&19&8&8\\
3&46&83&46&65&16&16\\
4&208&377&208&255&32&32\\
5&1074&1975&1074&1185&64&64\\
6&6200&11737&6200&6455&128&128
\end{array}
\]
The finite checks are not an infinite proof; Steps 1–7 supply the proof for all \(m\geq1\).

## Relationship to prior work

Dimitrova, Fernandes and Koppitz (arXiv:2401.11741, first posted 2024-01-22) define and structurally classify exactly these five partial star-endomorphism monoids, determine their cardinalities, regularity, Green relations and generating ranks, and describe the partial-automorphism submonoid. In particular, their Propositions 1.1, 1.4, 1.6 and 1.8 provide necessary and sufficient elementwise conditions, and their Section 3 notes the rank-one distinction between strong and strong-weak maps. These foundations make the present case decomposition possible. They do not give the six image-rank-refined idempotent polynomials, the simultaneous generating-function transform, or the asymptotic dichotomy proved here.

The follow-up full text Dimitrova–Fernandes–Koppitz, arXiv:2410.21084 (first posted 2024-10-28) develops presentations for the same monoids and is likewise a strong source for the underlying structure; no explicit idempotent rank census or asymptotic comparison was found in its accessible full text. The partial-isometry paper of Fernandes–Paulista, arXiv:2203.05504, treats the inverse monoid identified with \(\mathrm{PAut}\); its idempotents being partial identities is standard and is **not** claimed as novel in isolation. The ordinary partial-transformation idempotent polynomial \(A_m\) is similarly classical. The potential new content lies in the *simultaneous comparison*, exact weak/strong defect polynomial, and asymptotic separation across the star homomorphism conventions.

## Limitations

The stars are labeled and loopless, and the result is for the six stated transformation monoids. No corresponding theorem is asserted for arbitrary trees or unlabelled isomorphism classes. The asymptotic result establishes two limits but not a sharp equivalent for each total idempotent count. The literature priority assessment is limited to the inspected sources and database searches; an equivalent calculation under the terms graph retracts or partial retractions may exist. The counts over the inverse monoid and the elementary partial-transformation counting ingredient are known background, not independent novelty claims.

## References

1. I. Dimitrova, V. H. Fernandes, J. Koppitz, *On partial endomorphisms of a star graph*, arXiv:2401.11741 (2024-01-22), https://arxiv.org/abs/2401.11741 .
2. I. Dimitrova, V. H. Fernandes, J. Koppitz, *Presentations for monoids of partial endomorphisms of a star graph*, arXiv:2410.21084 (2024-10-28), https://arxiv.org/abs/2410.21084 .
3. V. H. Fernandes, T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504 (2022-03-10), https://arxiv.org/abs/2203.05504 .
