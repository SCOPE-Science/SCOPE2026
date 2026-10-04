# Exact binary two-\(\mathrm{PAL}_2\) code sizes through length eight
## Finding

Let \(M(n)\) be the largest size of a binary length-\(n\) code correcting two unrestricted sequential palindromic duplications of length \(2\) (equivalently, at most two such duplications). Then \(M(2)=4\), \(M(3)=8\), \(M(4)=14\), \(M(5)=20\), \(M(6)=28\), \(M(7)=42\), and \(M(8)=66\). By the even-length alternating-complement conjugacy, the same seven values hold for binary reverse-complement duplications of length \(2\).

## Assumptions and scope

For a binary word \(x\), a length-\(2\) palindromic duplication at position \(i\) replaces the local factor \(ab\) by \(abba\). Let \(D^2(x)\) be the set of all words obtained by applying two such duplications sequentially, with the second duplication allowed to use symbols inserted by the first. Define the confusability graph \(G_n\) on \(\{0,1\}^n\) by joining distinct \(x,y\) when
\[
D^2(x)\cap D^2(y)
earnothing .
\]
A two-error-correcting code is exactly an independent set of \(G_n\). For this insertion-only channel, exact-two and at-most-two correction are equivalent.

The claim concerns every admissible binary source length through \(n=8\). Lengths \(2\) and \(3\) are collision-free; \(n=4,\ldots,8\) are the first five nontrivial instances.

## Proof

For each \(2\le n\le8\), the accompanying `artifacts/certificate.json` contains two finite certificates.

First, `witness` is a set of \(M(n)\) length-\(n\) words. Direct generation of every exact-two descendant verifies that the descendant sets of distinct witness words are disjoint. Hence
\[
lpha(G_n)\ge M(n).
\]

Second, `conflict_clique_cover` partitions all \(2^n\) binary words into exactly \(M(n)\) groups. Direct generation verifies that every two distinct words within one group have a common exact-two descendant. Thus every group is a clique of \(G_n\). An independent set can contain at most one vertex from each clique, so
\[
lpha(G_n)\le M(n).
\]

The lower and upper certificates therefore meet exactly. Their common values are
\[
4,\ 8,\ 14,\ 20,\ 28,\ 42,\ 66
\]
for \(n=2,3,\ldots,8\).

The recent channel theorem gives a coordinate-wise bijection between palindromic and reverse-complement duplication histories at every even duplication length. Applying it at length \(2\) preserves source length, code cardinality, and two-error confusability. Hence the same maxima hold for the binary reverse-complement channel.

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs every exact-two descendant set from the channel definition rather than trusting stored graph edges. For each \(n\), it checks that the witness has the stated size and pairwise-disjoint descendant spheres, that the clique-cover groups partition all \(2^n\) source words exactly once, and that every pair within every cover group is confusable. It also verifies the collision-free cases \(n=2,3\). Successful replay prints `VERIFY_OK`.

The upper bounds are certificate proofs, not solver status reports: once the stored clique partitions are checked against independently regenerated descendant sets, no optimization software is needed.

## Relationship to prior work

Zabokritskiy's 2026 paper defines exactly this confusability graph, proves that exact-two and at-most-two correction coincide, determines the largest exact-two descendant sphere for every even duplication length, and obtains codes by a general maximum-degree coloring argument. It explicitly leaves a factor-two asymptotic gap for binary two-error codes and highlights length \(2\) as a structurally special case. The paper does not give the independence numbers of the finite confusability graphs above.

Earlier work of Lenz, Wachter-Zeh, and Yaakobi develops palindromic and reverse-complement duplication codes primarily in the one-error regime, while Sun and Ge's 2026 constructions treat different regimes, including length-one reverse-complement duplications and arbitrary-length single-error questions. Those results do not determine the two-error length-\(2\) finite maxima here.

These exact values therefore provide the first finite benchmark table for the newly isolated binary two-error \(\mathrm{PAL}_2\) confusability problem, together with independently replayable upper and lower certificates.

## Limitations

The computation stops at source length \(8\); no recurrence, asymptotic formula, or claim for \(n\ge9\) is asserted. The certificates establish only maximum cardinality, not a classification of all maximum codes. The reverse-complement statement uses the published even-length conjugacy rather than a separate enumeration. Literature searches covered exact-size, confusability-graph, palindromic-duplication, reverse-complement-duplication, and small-length formulations, but an equivalent finite table under different terminology remains a residual originality risk.

## References

1. Aryeh Lev Zabokritskiy (Yohananov), *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779v1, first public version 2026-09-01.
2. Andreas Lenz, Antonia Wachter-Zeh, and Eitan Yaakobi, *Duplication-correcting codes*, Designs, Codes and Cryptography 87 (2019), 277–298, DOI 10.1007/s10623-018-0523-0.
3. Yubo Sun and Gennian Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151, 2026.
