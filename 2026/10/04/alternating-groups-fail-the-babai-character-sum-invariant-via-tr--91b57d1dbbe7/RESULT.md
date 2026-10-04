# Alternating groups fail the Babai character-sum invariant via triangle Cayley graphs

## Finding

For every integer \(n\ge7\), the alternating group \(A_n\) is not a BI-group.

Let
\[
x=(1\,2\,3),
\qquad
y=(1\,2\,3)(4\,5\,6)
\]
in \(A_n\), and let
\[
S=\{x,x^{-1}\},
\qquad
T=\{y,y^{-1}\}.
\]
Both \(x\) and \(y\) have order \(3\). Therefore
\[
\operatorname{Cay}(A_n,S)
\cong
\frac{|A_n|}{3}K_3
\cong
\operatorname{Cay}(A_n,T).
\]

Let \(\chi\) be the standard irreducible character of \(A_n\), obtained from the natural permutation character by removing the trivial constituent. For every \(n\ge7\), \(\chi\) is the unique irreducible character of degree \(n-1\). Since
\[
\chi(g)=|\operatorname{Fix}(g)|-1,
\]
the two character sums are
\[
\sum_{s\in S}\chi(s)=2(n-4)
\]
and
\[
\sum_{t\in T}\chi(t)=2(n-7).
\]
They differ by \(6\). Consequently
\[
M^S_{n-1}\ne M^T_{n-1},
\]
even though the two Cayley graphs are isomorphic. Thus \(A_n\) is not a BI-group for every \(n\ge7\).

The boundary \(n=6\) is not covered: degree \(5\) is not unique in \(A_6\), so the singleton-character-set argument used here does not apply.

## Assumptions and scope

For a finite group \(G\) and an inverse-closed subset \(S\subseteq G\setminus\{1\}\), write
\[
\operatorname{Cay}(G,S)
\]
for the simple undirected Cayley graph. For a positive integer \(\nu\), define
\[
M^S_\nu
=
\left\{
\sum_{s\in S}\psi(s):
\psi\in\operatorname{Irr}(G),\ \psi(1)=\nu
\right\}.
\]
A BI-group is a finite group \(G\) such that whenever
\[
\operatorname{Cay}(G,S)\cong\operatorname{Cay}(G,T),
\]
one has
\[
M^S_\nu=M^T_\nu
\]
for every \(\nu\).

No connectedness or generating-set hypothesis is part of this definition. The witnesses here are deliberately disconnected: each is a disjoint union of triangles.

The only representation-theoretic input beyond the elementary standard-character formula is uniqueness of the degree-\(n-1\) irreducible character of \(A_n\) for \(n\ge7\). For \(n\ge9\) this follows from the classical small-degree results of Rasala together with restriction from \(S_n\) to \(A_n\); the cases \(n=7,8\) are checked directly by the hook-length classification and are replayed in the verification artifact.

## Proof

Both \(x\) and \(y\) are even permutations of order \(3\), so \(S\) and \(T\) are inverse-closed two-element subsets of \(A_n\setminus\{1\}\).

For any element \(g\) of order \(3\), the Cayley graph
\[
\operatorname{Cay}(G,\{g,g^{-1}\})
\]
has connected components equal to the right cosets of \(\langle g\rangle\). Each component is a \(3\)-cycle, hence a copy of \(K_3\). Therefore
\[
\operatorname{Cay}(A_n,S)
\cong
\frac{|A_n|}{3}K_3
\cong
\operatorname{Cay}(A_n,T).
\]

The natural permutation character of \(A_n\) is
\[
1+\chi,
\]
where \(\chi\) is the standard character of degree \(n-1\). Hence
\[
\chi(g)=|\operatorname{Fix}(g)|-1.
\]

A \(3\)-cycle fixes exactly \(n-3\) points, so
\[
\chi(x)=\chi(x^{-1})=n-4.
\]
A product of two disjoint \(3\)-cycles fixes exactly \(n-6\) points, so
\[
\chi(y)=\chi(y^{-1})=n-7.
\]
Thus
\[
\sum_{s\in S}\chi(s)=2(n-4),
\qquad
\sum_{t\in T}\chi(t)=2(n-7).
\]

For \(n\ge7\), \(\chi\) is the unique irreducible character of degree \(n-1\). Hence
\[
M^S_{n-1}=\{2(n-4)\},
\qquad
M^T_{n-1}=\{2(n-7)\}.
\]
These sets are unequal. The defining BI condition therefore fails.

For completeness, the uniqueness statement for \(n=7,8\) can be read directly from the ordinary character degrees of \(A_n\). Irreducible characters of \(S_n\) are indexed by partitions. A non-self-conjugate partition and its conjugate restrict to the same irreducible character of \(A_n\), while a self-conjugate partition splits into two equal-degree characters. Hook-length computation gives exactly one degree \(6\) character for \(A_7\) and exactly one degree \(7\) character for \(A_8\). The packaged verifier reproduces these calculations from scratch.

## Verification

The included replay performs two independent finite checks.

First, it generates partitions of \(7\) and \(8\), computes the corresponding \(S_n\)-character degrees from the hook-length formula, applies the standard restriction/splitting rule to \(A_n\), and confirms that there is exactly one irreducible character of degree \(n-1\) in each case.

Second, it explicitly enumerates \(A_7\) and \(A_8\), constructs the two Cayley graphs from
\[
x=(1\,2\,3)
\]
and
\[
y=(1\,2\,3)(4\,5\,6),
\]
and checks that every connected component in each graph has exactly three vertices. It also checks the standard-character sums directly from fixed-point counts and verifies the constant difference \(6\).

The replay returns `VERIFY_OK`.

Finite computation is used only for the low-degree boundary checks \(n=7,8\), not for the uniform proof for \(n\ge9\).

## Relationship to prior work

Abdollahi and Zallaghi define BI-groups in the character-sum sense used here and explicitly ask which finite groups are BI-groups. Their 2017 preprint, later published in 2019, lists all BI-groups of order at most \(30\) and gives nonabelian BI examples outside the CI class.

Their earlier 2015 paper gives several non-BI families, including symmetric groups \(S_n\) for \(n\ge4\). That statement does not imply the present result: failure of the BI property need not pass from a group to an index-two subgroup, and a witness in \(S_n\) need not lie in \(A_n\).

The present construction gives a uniform witness inside \(A_n\) itself. Both connection sets have size \(2\), both resulting graphs are the same disjoint union of triangles, and the failure is detected by the unique standard character of degree \(n-1\).

Searches using the phrases “alternating group BI-group”, “Babai invariant alternating group”, “character sums Cayley alternating group”, “non-BI alternating group”, and equivalent \(A_n\) formulations did not locate this theorem. The closest database result found in the same BI-group line proves that the affine groups \(\operatorname{AGL}(1,q)\) are BI-groups, which is a different family and the opposite classification.

## Limitations

The theorem begins at \(n=7\). It does not classify the BI status of \(A_5\) or \(A_6\).

The proof relies on the uniqueness of the degree-\(n-1\) irreducible character. The \(n=7,8\) cases are independently checked in the package; the \(n\ge9\) uniqueness input is classical representation theory.

The full text of the 2015 predecessor article was not available through the public route checked during this comparison. Its public abstract and the later 2017 article's summary were inspected, so an equivalent alternating-group statement hidden in that inaccessible full text remains a residual bibliographic risk.

Failed searches do not prove novelty.

## References

1. A. Abdollahi and M. Zallaghi, “Non-abelian finite groups whose character sums are invariant but are not Cayley isomorphism,” arXiv:1710.04446v1, first public version 12 October 2017; *Journal of Algebra and Its Applications* 18 (2019). Primary MSC 20C15.
2. A. Abdollahi and M. Zallaghi, “Character sums for Cayley graphs,” *Communications in Algebra* 43 (2015), 5159–5167.
3. R. Rasala, “On the minimal degrees of characters of \(S_n\),” *Journal of Algebra* 45 (1977), 132–181.
