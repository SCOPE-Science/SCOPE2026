# The affine groups AGL(1,q) are BI-groups

## Statement

For a finite group \(G\) and an inverse-closed subset \(S\subseteq G\setminus\{1\}\), write
\[
M_\nu^S=\left\{\sum_{s\in S}\chi(s):\chi\in\operatorname{Irr}(G),\ \chi(1)=\nu\right\}.
\]
Following Abdollahi--Zallaghi, \(G\) is a **BI-group** if isomorphic Cayley graphs
\(\operatorname{Cay}(G,S)\cong\operatorname{Cay}(G,T)\) always satisfy
\(M_\nu^S=M_\nu^T\) for every \(\nu\).

**Theorem.** Suppose \(G\) has exactly one nonlinear complex irreducible character
\(\chi\), of degree \(d>1\), and exactly \(d\) linear irreducible characters. Then
\(G\) is a BI-group.

By Seitz's classification of finite groups with one nonlinear irreducible character,
this gives the following structural consequence.

**Corollary 1.** Every finite Frobenius group with exactly one nonlinear irreducible
character is a BI-group. Equivalently, for every prime power \(q\ge 3\),
\[
\operatorname{AGL}(1,q)=\mathbb F_q^+\rtimes \mathbb F_q^\times
\]
is a BI-group.

There are consequently infinitely many nonabelian BI-groups that are not CI-groups.
For example, if \(q\) is a prime with \(q\equiv1\pmod{25}\), then
\(\operatorname{AGL}(1,q)\) is BI but not CI.

## Proof

It is enough to treat connected Cayley graphs: Abdollahi--Zallaghi's connected-complement
reduction (their Proposition 2.5) shows that a finite group is BI once the required
invariance is known for its connected Cayley graphs.

Let \(S=S^{-1}\subseteq G\setminus\{1\}\) generate \(G\), and put
\(\Gamma=\operatorname{Cay}(G,S)\). For a linear character \(\lambda\), set
\[
a_\lambda(S)=\sum_{s\in S}\lambda(s).
\]
Let \(\rho\) afford the unique nonlinear character \(\chi\), and let
\(\mu_1,\dots,\mu_d\) be the eigenvalues, with multiplicity, of the Hermitian matrix
\[
B_S=\sum_{s\in S}\rho(s).
\]
The regular representation decomposes into each irreducible representation with
multiplicity equal to its degree. Hence the adjacency spectrum of \(\Gamma\) consists
of

- the \(d\) numbers \(a_\lambda(S)\), one from each linear character; and
- the numbers \(\mu_1,\dots,\mu_d\), each repeated \(d\) times.

For a real eigenvalue \(\alpha\), let \(m_S(\alpha)\) be its multiplicity in the
adjacency spectrum and let
\[
\ell_S(\alpha)=\#\{\lambda\in\operatorname{Irr}(G):\lambda(1)=1,
\ a_\lambda(S)=\alpha\}.
\]
Then
\[
m_S(\alpha)\equiv \ell_S(\alpha)\pmod d. \tag{1}
\]
We claim that \(0\le \ell_S(\alpha)<d\) for every \(\alpha\). The only possible
failure would be \(\ell_S(\alpha)=d\), meaning that all linear character sums are
\(\alpha\). The principal character is linear, so then \(\alpha=|S|\). But a connected
\(|S|\)-regular graph has \(|S|\) as a simple eigenvalue, whereas
\(\ell_S(|S|)=d>1\), a contradiction. Therefore \(\ell_S(\alpha)\) is exactly the
least nonnegative residue of \(m_S(\alpha)\) modulo \(d\).

Thus the graph spectrum determines the **multiset**
\[
L_S=\bigl\{a_\lambda(S):\lambda(1)=1\bigr\}, \tag{2}
\]
and in particular determines \(M_1^S\).

It also determines the unique nonlinear character sum. Indeed, the adjacency matrix
has zero diagonal, so its trace is zero. Taking traces in the regular-representation
decomposition gives
\[
0=\sum_{\lambda(1)=1} a_\lambda(S)+d\,\chi(S),
\qquad
\chi(S):=\sum_{s\in S}\chi(s).
\]
Consequently
\[
\chi(S)=-\frac1d\sum_{\lambda(1)=1}a_\lambda(S), \tag{3}
\]
which is determined by the multiset (2). Hence the spectrum determines both
\(M_1^S\) and the singleton \(M_d^S=\{\chi(S)\}\); all other \(M_\nu^S\) are empty.
Isomorphic Cayley graphs are cospectral, so every connected Cayley graph of \(G\) is a
BI-graph, proving the theorem.

For Corollary 1, Seitz proved that a finite group with exactly one nonlinear
irreducible character is either an extraspecial \(2\)-group or a Frobenius group with
an elementary abelian kernel \(G'\) and a cyclic complement \(H\) satisfying
\(|H|=|G'|-1\). In the Frobenius case the number of linear characters is
\(|G:G'|=|H|\). If \(d\) is the degree of the unique nonlinear character, then the
sum-of-squares formula gives
\[
|G|=|H|+d^2=|G'|\,|H|=(|H|+1)|H|,
\]
so \(d=|H|\). The theorem applies. Such a group is the standard sharply
2-transitive affine group \(\operatorname{AGL}(1,q)\), with \(q=|G'|\).

Finally, the standard CI-group Sylow restriction recalled as Theorem 5.5 by
Abdollahi--Zallaghi (citing Babai--Frankl) says that a Sylow \(p\)-subgroup of a
finite CI-group must be elementary abelian, or cyclic of order \(p^a\) with both
\(p\le3\) and \(a\le3\), or quaternion of order \(8\). If a prime \(q\equiv1\pmod{25}\), the cyclic complement
of \(\operatorname{AGL}(1,q)\) has a Sylow \(5\)-subgroup of order at least \(25\),
so the group is not CI. Dirichlet's theorem supplies infinitely many such primes.

## Context and significance

Babai asked in 1979 whether the sets \(M_\nu^S\) are graph invariants. Abdollahi and
Zallaghi gave counterexamples in 2015 and formulated the problem of determining the
finite BI-groups. Their 2019 follow-up proved, by separate character-table and spectrum
case analyses, that two nonabelian non-CI groups of orders \(20\) and \(42\) are BI and
listed all BI-groups of order at most \(30\). Those two examples are
\(\operatorname{AGL}(1,5)\) and \(\operatorname{AGL}(1,7)\).

The theorem above replaces those isolated calculations by a degree-multiplicity
mechanism: nonlinear spectral multiplicities vanish modulo \(d\), while connectedness
prevents the only ambiguous residue \(d\) among the linear contributions. Combined
with the trace identity, this recovers the unique nonlinear character sum as well.
This yields the full cyclic-complement Frobenius branch in Seitz's classification, equivalently the groups \(\operatorname{AGL}(1,q)\), and, together with standard CI-group
restrictions, an infinite BI-but-not-CI subfamily.

## Limitations

The argument does not cover the other branch of Seitz's classification, namely
extraspecial \(2\)-groups. There the number of linear characters is \(d^2\), not \(d\),
so multiplicities modulo \(d\) no longer recover the linear-character contribution.
The result concerns simple undirected Cayley graphs, matching the BI-group convention
used by Abdollahi--Zallaghi in their 2019 paper; no claim is made here for arbitrary
Cayley digraphs.

Originality is asserted only to the best of our knowledge. The 2019 paper was checked
in full and treats the order-20 and order-42 Frobenius groups separately, without a
general ratio-one Frobenius or \(\operatorname{AGL}(1,q)\) theorem. Targeted searches
through current literature located no equivalent general BI result. A recent 2026 paper
on Ramanujan normal Cayley graphs of ratio-one Frobenius groups concerns a different
spectral classification and does not supply this BI criterion.

## References

1. L. Babai, *Spectra of Cayley graphs*, J. Combin. Theory Ser. B 27 (1979), 180--189. DOI: https://doi.org/10.1016/0095-8956(79)90079-0
2. A. Abdollahi and M. Zallaghi, *Character Sums for Cayley Graphs*, Comm. Algebra 43 (2015), 5159--5167. DOI: https://doi.org/10.1080/00927872.2014.967398
3. A. Abdollahi and M. Zallaghi, *Non-Abelian finite groups whose character sums are invariant but are not Cayley isomorphism*, J. Algebra Appl. 18 (2019), 1950013. DOI: https://doi.org/10.1142/S0219498819500130 ; arXiv: https://arxiv.org/abs/1710.04446
4. G. M. Seitz, *Finite groups having only one irreducible representation of degree greater than one*, Proc. Amer. Math. Soc. 19 (1968), 459--461. DOI: https://doi.org/10.1090/S0002-9939-1968-0222160-X
5. L. Babai and P. Frankl, *Isomorphisms of Cayley graphs I*, Colloq. Math. Soc. J. Bolyai 18 (1976), 35--52.
6. M.-H. Kang and C.-J. Yang, *Ramanujan Cayley Graphs with Normal Connection Sets in Ratio-One Frobenius Groups*, arXiv:2608.19905 (2026): https://arxiv.org/abs/2608.19905
