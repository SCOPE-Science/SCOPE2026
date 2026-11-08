# A mod-three pseudo-Frobenius spectrum for four consecutive repunits

## Finding

For every integer base \(b\ge 2\) and every integer \(n\ge5\), put
\[
R_j=\sum_{i=0}^{j-1}b^i=\frac{b^j-1}{b-1},\qquad S=\langle R_n,R_{n+1},R_{n+2},R_{n+3}\rangle.
\]
Let \(F=F(S)\) be the largest gap and let \(\operatorname{PF}(S)\) be the set of pseudo-Frobenius numbers. Then
\[
\boxed{\operatorname{PF}(S)=
\begin{cases}
\{F,F-1\},&n\equiv0\pmod3,\\
\{F,F-1,F-2\},&n\equiv1\pmod3,\\
\{F,F-(R_{n+2}+1)\},&n\equiv2\pmod3.
\end{cases}}
\]
Consequently the type is \(2,3,2\) in these three respective congruence classes. In the third class the gap between the two pseudo-Frobenius numbers grows without bound, unlike the consecutive spectra in the first two classes. The \(n\equiv0\pmod3\) branch is already covered by the divisible-multiplicity theorem of Liu--Xin--Ye--Yin; the new content is the other two branches and the uniform three-class classification for the *four-generator truncation*.

## Assumptions and scope

All semigroups consist of nonnegative integer combinations, including zero. A pseudo-Frobenius number is an integer \(z\notin S\) such that \(z+s\in S\) for every nonzero \(s\in S\). The type is \(|\operatorname{PF}(S)|\). The starting index satisfies \(n\ge5\): this excludes the full four-generator repunit semigroup at \(n=4\), for which an earlier full-length classification already applies. For \(n\ge5\), the four terms are a truncation of the \(n\)-generator repunit semigroup.

To determine \(F\) explicitly if desired, set
\[
a=R_n,\quad q=b+1,\quad h=b^2+b+1,\quad c=(b-1)a+1,
\]
and for \(t\ge0\) write \(t=zh+yq+x\), where \(z=\lfloor t/h\rfloor\), \(y=\lfloor (t\bmod h)/q\rfloor\) and \(x=t\bmod q\). Put \(L(t)=z+y+x\) and \(W(t)=aL(t)+ct\). Then \(F=W(a-1)-a\). This formula is an instance of the existing general Frobenius/greedy-Apéry framework, not a separate novelty claim.

## Proof

**1. Greedy coin lemma.** The three auxiliary denominations \(1,q,h\) have the property that the least possible number of coins in any representation of \(t\ge0\) is exactly \(L(t)\). Indeed, from any coin representation with \(x\) ones, \(y\) copies of \(q\), and \(z\) copies of \(h\), apply the following transformations whenever possible: replace \(q\) ones with one \(q\)-coin (decreasing the coin count by \(b\)); replace \(q\) copies of a \(q\)-coin with one \(h\)-coin and \(b\) ones (preserving the count because \(q^2=h+b\)); and replace \(b\) copies of a \(q\)-coin together with one \(1\)-coin with one \(h\)-coin (decreasing the count by \(b\), because \(bq+1=h\)). Termination follows by lexicographically decreasing (coin count, number of \(q\)-coins) whenever the count is unchanged. At termination, \(0\le x\le b\), \(0\le y\le b\), and \(y=b\) forces \(x=0\). These conditions are exactly the unique greedy expansion \(t=zh+yq+x\) with \(0\le yq+x<h\). Thus no transformation increases the coin count and the greedy count is minimal.

**2. The Apéry set.** The three generators after \(a\) have the exact form
\[
R_{n+j}=a+c\frac{b^j-1}{b-1}\quad(j=1,2,3),
\]
corresponding to the auxiliary denominations \(1,q,h\). For any fixed auxiliary sum \(t\), the minimum possible semigroup expression without separate \(a\)-coins is \(W(t)=aL(t)+ct\). Because the greedy digits change under \(t\mapsto t+1\) so that
\[
L(t+1)-L(t)\in\{1,1-b\},
\]
we have \(W(t+1)-W(t)\ge c-(b-1)a=1\). Since \(c\equiv1\pmod a\), a representation in residue \(r\pmod a\) has auxiliary sum \(t=r+\ell a\) for some \(\ell\ge0\); monotonicity proves that its minimal value is \(W(r)\). Hence
\[
\operatorname{Ap}(S,a)=\{W(t):0\le t<a\}.
\]

**3. Maximality reduces to one-coin steps.** We establish the exact criterion
\[
W(t)\text{ is maximal in }\operatorname{Ap}(S,a)
\quad\Longleftrightarrow\quad
\forall d\in\{1,q,h\}:\ t+d\ge a\ \text{or}\ L(t+d)\ne L(t)+1.
\tag{*}
\]
To see this, suppose \(W(u)=W(t)+\sum_{j=1}^m(a+cd_j)\) with \(m\ge1\) and \(d_j\in\{1,q,h\}\); separate multiples of \(a\) cannot occur because \(W(u)\) is an Apéry element. Put \(T=t+\sum_jd_j=u+\ell a\) with \(\ell\ge0\). Comparing the \(a\)-parts in \(W\) gives \(L(u)=L(t)+m+c\ell\). But \(L(u)\le u<a<c\), so \(\ell=0\). Since the minimum-coin function is subadditive, equality \(L(u)=L(t)+m\) forces each successive prefix of the added coins to increase \(L\) by precisely one. In particular, a single admissible step in \((*)\) must exist. Conversely any such step yields \(W(t+d)-W(t)=a+cd\in S\), establishing the criterion. The standard Apéry-maximal characterization of pseudo-Frobenius numbers then gives \(\operatorname{PF}(S)=\{W(t)-a:W(t)\text{ maximal}\}\).

**4. The three terminal patterns.** The residue of \(a=R_n\) modulo \(h=R_3\) is respectively \(0,1,q\) as \(n\equiv0,1,2\pmod3\). This follows by grouping base-\(b\) digits in blocks of three: if \(n=3m\) and \(T=1+b^3+\cdots+b^{3(m-1)}\), then the three corresponding values of \(a\) are \(hT\), \(hbT+1\), and \(hb^2T+q\).

Write \(a=hQ+r\), with \(r\in\{0,1,q\}\). By \((*)\), a maximal index must satisfy \(t\ge a-h\), since otherwise adding \(h\) increases the optimal coin count by one. The remaining terminal slab consists of indices \((Q-1)h+s\) with \(r\le s<h\), and (if \(r>0\)) \(Qh+s\) with \(0\le s<r\). Write \(s=yq+x\) in greedy form. Adding \(1\) increases \(L\) by one except when \(x=b\) or \((y,x)=(b,0)\). Adding \(q\) increases \(L\) by one except when \(y=b-1\) and \(x\ge1\). Applying these conditions and the upper bound \(t+d<a\) gives exactly the following *complete* maximal-index table:

| \(r=a\bmod h\) | Maximal Apéry indices \(t\) |
| --- | --- |
| \(0\) | \(a-2,\ a-1\) |
| \(1\) | \(a-3,\ a-2,\ a-1\) |
| \(q\) | \(a-q-2,\ a-1\) |

For completeness, on the lower terminal slab the \(+1\) test leaves only greedy pairs \((y,x)=(b-1,b)\) or \((b,0)\); the \(+q\) test retains both for \(r=0,1\) but only \((b-1,b)\) for \(r=q\). On the upper slab, \(r=1\) leaves only its endpoint \(Qh\), while \(r=q\) leaves only \(Qh+b\). This proves the table without assuming that any computer enumeration is exhaustive.

Finally \(W(a-1)\) is the largest Apéry representative because \(W\) is strictly increasing. In the first two cases the displayed maximal indices yield consecutive \(W\)-values, since \(W\) increases by exactly one on these terminal steps. In the third case, \(L(a-1)-L(a-q-2)=2-b\) and \((a-1)-(a-q-2)=b+2\), whence
\[
W(a-1)-W(a-q-2)
=a(2-b)+c(b+2)=b^2a+b+2=R_{n+2}+1.
\]
Subtracting \(a\) from all maximal representatives proves the claimed pseudo-Frobenius spectra and types. \(\square\)

## Verification

The companion `verify_repunit_truncation.py` independently constructs Apéry representatives using Dijkstra's shortest-path algorithm on residues modulo \(a\), computes pseudo-Frobenius numbers by the generator-membership definition, and compares them against the predicted terminal indices. Exact-integer checks passed for 330 generic instances of \(a=hQ+r\) with \(r\in\{0,1,q\}\) and 31 actual consecutive-repunit instances with \(n\ge5\). Every tested Apéry representative matched the separately implemented greedy formula; every pseudo-Frobenius set matched the theorem. These are finite cross-checks, not the justification of the universal quantifiers, which is the proof above.

## Relationship to prior work

Liu, Xin, Ye and Yin (first publicly posted 2023-06-06) provide a general greedy description of Apéry representatives, formulas for the Frobenius number and genus, and a pseudo-Frobenius theorem for the specialized divisibility assumption \(a=m(b^k-1)/(b-1)\). At \(k=3\) that result covers exactly the \(n\equiv0\pmod3\) branch, not the two other branches. The present proof uses an independent one-coin maximality analysis to identify the precise exceptional boundary states in those other branches. An earlier short note by the same authors provides F/genus calculations, not the stated three-class type result.

Branco, Colaço and Ojeda's full generalized-repunit semigroup has \(n\) minimal generators and type \(n-1\); for \(n\ge5\) that is a different semigroup from the four-generator truncation here. Komatsu's work on generalized Frobenius representation counts for repunits addresses a distinct invariant and full-length or small-index cases. A related 2024 chapter by Komatsu and Yin considers triples of generalized repunits with two base parameters both greater than one; its full text could not be inspected, and it remains a literature-completeness risk, though the directly stated hypotheses exclude the ordinary repunit case studied here.

## Limitations

The result is a structural classification for exactly four consecutive ordinary base-\(b\) repunits beginning at \(n\ge5\); it does not assert analogous spectra for longer truncations, arbitrary starting values, or generalized two-base repunits. The Frobenius number itself is not claimed to be newly determined. No independent expert review or external certification has been performed. A stronger unindexed equivalence or an unforeseen deduction from the general published greedy-Apéry framework remains an originality risk.

## References

1. F. Liu, G. Xin, S. Ye, J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459, initial release 2023-06-06, especially Theorem 2.10 and Theorem 3.4. https://arxiv.org/abs/2306.03459
2. F. Liu, G. Xin, S. Ye, J. Yin, *A Note on Generalized Repunit Numerical Semigroups*, arXiv:2306.10738, initial release 2023-06-19. https://arxiv.org/abs/2306.10738
3. M. B. Branco, I. Colaço, I. Ojeda, *The Frobenius Problem for Generalized Repunit Numerical Semigroups*, Mediterranean Journal of Mathematics (2023), DOI 10.1007/s00009-022-02233-w. https://link.springer.com/article/10.1007/s00009-022-02233-w
4. T. Komatsu, *The Frobenius Number Associated with the Number of Representations for Sequences of Repunits*, Comptes Rendus Mathématique 361 (2023), 73–89, DOI 10.5802/crmath.394. https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.394/
5. T. Komatsu, R. Yin, *p-Numerical Semigroups of the Triples of the Sequence (a^n-b^n)/(a-b)*, Mathematical Methods for Engineering Applications (2024), DOI 10.1007/978-3-031-49218-1_2 (abstract checked; full text not available for inspection).
