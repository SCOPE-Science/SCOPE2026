# Total domination polynomial and unique-cover band of Kneser graphs

## Finding

Let \(n\ge5\) and let \(G_n=KG(n,2)\), with one vertex for each two-element subset of \([n]\) and adjacency exactly for disjoint pairs. Let \(T_n(z)\) be the total domination polynomial: the coefficient of \(z^k\) counts subsets of \(k\) vertices having an adjacent selected vertex at **every** vertex, including selected ones. The following formulas determine all coefficients exactly.

Use \(\binom ab=0\) when \(b<0\) or \(b>a\), put \(m=\binom n2\), and let
\[
S_r(z)=\sum_{j=3}^{r}\binom rj z^j\qquad(r\ge0).
\]
Define the low-degree obstruction polynomial
\[
\begin{aligned}
C_n(z)={}&1+\binom n2z
+\left(3\binom n3+3\binom n4\right)z^2\\
&+\left(\binom n3+12\binom n4+30\binom n5\right)z^3\\
&+\left(3\binom n4+60\binom n5+90\binom n6\right)z^4,
\end{aligned}
\]
the one-hub obstruction polynomial
\[
H_n(z)=n\left[\left(1+\binom{n-1}{2}z\right)S_{n-1}(z)
+(n-1)\binom{n-2}{2}z^2S_{n-2}(z)\right],
\]
and the two-hub obstruction polynomial
\[
Q_n(z)=\binom n2\sum_{\epsilon=0}^{1}\sum_{\substack{a,b,c,d\ge0;\ a+b+c+d=n-2\\
\epsilon+a+c\ge3;\ \epsilon+b+c\ge3}}
\frac{(n-2)!}{a!b!c!d!}\,z^{\epsilon+a+b+2c}.
\]
Then the complete polynomial is
\[
\boxed{T_n(z)=(1+z)^m-C_n(z)-H_n(z)-Q_n(z).}
\]

**Unique-cover band.** For every \(n\ge5\) and integer \(k\) satisfying \(n+1\le k\le m\), the number of subsets of size \(k\) that are **not** total dominating is exactly
\[
\boxed{\binom n2\binom{2n-3}{k}}.
\]
Consequently
\[
\boxed{[z^k]T_n(z)=\binom{m}{k}-\binom n2\binom{2n-3}{k}\quad(n+1\le k\le m).}
\]
In particular, every subset with at least \(2n-2\) vertices is total dominating, whereas precisely \(\binom n2\) subsets of size \(2n-3\) fail. In the stated band, each failure has a **unique** two-element transversal of the corresponding edge family.

## Assumptions and scope

All graphs are finite, simple and labeled. A selected vertex family \(D\subseteq V(G_n)\) is regarded as an edge set of a spanning graph \(F=([n],D)\), which may have isolated vertices. A vertex cover (or transversal) of \(F\) meets every edge of \(F\); write \(\tau(F)\) for its minimum cardinality, with \(\tau(F)=0\) when \(D=\varnothing\). An empty graph on the unused labels has no effect on the enumeration. The formula covers **all** subsets, not only inclusion-minimal or minimum-cardinality sets.

The scope \(n\ge5\) is essential for the stated lower extremal interpretation. At \(n=4\), the graph \(KG(4,2)\) is three disjoint edges and \(T_4(z)=z^6\); at \(n=3\), the Kneser graph is edgeless and has no total dominating set.

## Proof

**1. Convert total domination to a transversal obstruction.** For every pair \(e\in\binom{[n]}2\), total domination demands an edge \(f\in D\) disjoint from \(e\). Its failure is equivalent to a pair \(e\) meeting every edge of \(D\). Thus
\[
D\text{ total dominates }G_n\quad\Longleftrightarrow\quad\tau(F)\ge3.
\]
There are \((1+z)^m\) weighted edge subsets of \(K_n\). We must subtract precisely the graphs with \(\tau(F)\le2\).

**2. Classify by high-degree vertices.** If a graph \(F\) admits a two-vertex cover, every vertex of degree at least three belongs to *every* such cover: excluding that vertex would require at least three of its neighbors in a cover of size two. Hence there are at most two degree-at-least-three vertices. Call these vertices hubs.

**3. No hubs.** If the maximum degree is at most two, each nontrivial component is a path or cycle. The vertex-cover number is additive on components, equals \(\lfloor r/2\rfloor\) for a path on \(r\) vertices, and equals \(\lceil r/2\rceil\) for a cycle on \(r\) vertices. The complete possibilities with cover number at most two, apart from isolated vertices, are

| Components | Edges | Number on \([n]\) |
| --- | ---: | ---: |
| empty | 0 | \(1\) |
| \(K_2\) | 1 | \(\binom n2\) |
| \(P_3\) | 2 | \(3\binom n3\) |
| \(2K_2\) | 2 | \(3\binom n4\) |
| \(C_3\) | 3 | \(\binom n3\) |
| \(P_4\) | 3 | \(12\binom n4\) |
| \(P_3\cup K_2\) | 3 | \(30\binom n5\) |
| \(C_4\) | 4 | \(3\binom n4\) |
| \(P_5\) | 4 | \(60\binom n5\) |
| \(2P_3\) | 4 | \(90\binom n6\) |

Here \(P_r\) denotes the path with \(r\) vertices, and \(C_r\) the cycle. The table proves \(C_n(z)\), including the factors accounting for automorphisms of the path components.

**4. Exactly one hub.** Let it be \(v\). Since every two-cover must contain \(v\), the residual graph \(F-v\) has cover number at most one. It is therefore either empty or a star (with isolated vertices). Because every other vertex has degree at most two, this residual star can contain only zero, one, or two edges. For zero edges, freely choose at least three of the \(n-1\) edges incident to \(v\), giving \(nS_{n-1}(z)\). For one residual edge, choose its two endpoints in \(\binom{n-1}{2}\) ways and again choose the incident edges to \(v\), giving \(n\binom{n-1}{2}zS_{n-1}(z)\). For two residual edges, choose a three-vertex path in \(3\binom{n-1}{3}=(n-1)\binom{n-2}{2}\) ways. Its center cannot be adjacent to \(v\), since then it would be a second hub. The other \(n-2\) incident edges may be selected, at least three of them; this gives the final term in \(H_n(z)\). These cases are mutually exclusive.

**5. Exactly two hubs.** Call them \(p,q\). By the mandatory-hub observation, \(\{p,q\}\) is the unique two-vertex cover, and every edge touches \(p\) or \(q\). Let \(\epsilon\in\{0,1\}\) indicate whether \(pq\) is present. Partition the other \(n-2\) labeled vertices into four categories: \(a\) adjacent only to \(p\), \(b\) only to \(q\), \(c\) to both, and \(d\) to neither. The hub degrees are \(\epsilon+a+c\) and \(\epsilon+b+c\), both at least three, and the number of edges is \(\epsilon+a+b+2c\). The multinomial count, times \(\binom n2\) choices of the unordered hub pair, proves \(Q_n(z)\). The cases of zero, one, and two hubs partition all non-total-dominating families without repetition, giving the first boxed identity.

**6. Unique-cover high-cardinality band.** Fix any two-cover \(\{p,q\}\). Its allowable edge universe has precisely \(2n-3\) edges. If either \(p\) or \(q\) has degree at most two, the other hub is incident with at most \(n-1\) edges, and their union has at most \(n\) distinct edges (accounting for the possible common edge \(pq\)). Hence any two-covered graph with at least \(n+1\) edges has both \(p\) and \(q\) of degree at least three. They belong to every two-cover, so the covering pair is unique. Conversely, every choice of at least \(n+1\) edges from the \(2n-3\)-edge universe has both hubs of degree at least three, by the same bound. Therefore there are exactly \(\binom n2\binom{2n-3}{k}\) failures of size \(k\) in the stated range. Above \(2n-3\) there are none. This proves the remaining identities for every \(n\ge5\).

The previously established minimum sizes provide boundary checks: \(\gamma_t(KG(5,2))=4\), with ten minimum sets, and for \(n\ge6\), \(\gamma_t(KG(n,2))=3\), with exactly \(15\binom n6\) minimum sets (three pairwise disjoint edges of \(K_n\)). These minimum-cardinality facts are not claimed as new.

## Verification

The package includes two standalone exact checkers. Run `python3 verify.py` using Python 3.8 or later. It independently checks the formula against every subset of the edge set of \(K_n\) for \(3\le n\le6\), totaling \(33864\) subsets, and checks the high-cardinality band at every \(5\le n\le30\). The direct test uses every candidate two-vertex cover, not the hub-case decomposition.

For an independent implementation of the first nontrivial larger case, run `cc -O2 -std=c99 verify_n7.c -o verify_n7 && ./verify_n7`; the program exhausts all \(2^{21}=2097152\) edge subsets of \(K_7\), reporting the number with no two-vertex cover by cardinality. Its output agrees coefficient-by-coefficient with `polynomial(7)` from `verify.py`. The computations test finite cases; they do not substitute for Steps 1--6 of the proof.

As a check against the **previously published full Petersen polynomial** of Sanal and Vatsalya (2016), the special case \(KG(5,2)\) gives
\[
T_5(z)=10z^4+72z^5+140z^6+110z^7+45z^8+10z^9+z^{10}.
\]

## Relationship to prior work

Ivančo and Zelinka (1993) determine the domination, total-domination, and (total) domatic numbers of \(KG(n,2)\), including the known minimum total-dominating triples for \(n\ge6\). Hartman's 1997 thesis treats Kneser domination via blocking sets and states the general equivalence between total domination and absence of a fixed-size blocking set. Sanal and Vatsalya (published 25 March 2016, Theorem 3.6) already determine **every coefficient of the Petersen graph** \(KG(5,2)\); that special case is not new. Their general regular-graph Lemmas 3.4--3.5 also already imply the two topmost cardinality coefficients and the total-domination cutoff \(2n-2\) for this family, so these boundary consequences are not asserted as original. Hu and coauthors (arXiv:1607.00400v1, 1 July 2016) develop general reduction formulas and examples for paths, cycles and trees rather than the full \(KG(n,2)\) family. The claim here is the **complete all-order enumeration for \(n\ge6\)** from a disjoint high-degree classification, together with a unique-two-cover interpretation throughout the interior size band \(n+1\le k\le2n-4\), beyond the already-known top boundary. The exact formula also specializes consistently to the published \(n=5\) polynomial.

## Limitations

The proof applies to the two-element Kneser graphs only, and does not establish formulas for \(KG(n,r)\) when \(r\ge3\). Its \(n=5\) specialization and the uppermost coefficients for all orders are known from Sanal--Vatsalya (2016), so neither is separately claimed as novel. It counts labeled subsets; it does not classify their orbits under automorphisms. Literature searches found no matching all-order polynomial, but cannot exclude an earlier equivalent result under the terminology of two-transversal-free edge families or bounded-vertex-cover graph enumeration. No independent mathematical audit has been carried out.

## References

1. J. Ivančo and B. Zelinka, *Domination in Kneser graphs*, Mathematica Bohemica **118** (1993), 147--152, especially Theorem 3. https://dml.cz/bitstream/handle/10338.dmlcz/126050/MathBohem_118-1993-2_3.pdf
2. C. M. Hartman, *Extremal Problems in Graph Theory*, PhD thesis, University of Illinois at Urbana-Champaign (1997), Chapter 8, pp. 75--85. https://www.cs.uaf.edu/~hartman/thesis.pdf
3. S. Sanal and H. E. Vatsalya, *On Total Domination Polynomials of Certain Graphs*, Journal of Mathematics and System Science **6** (2016), 123--127, published 25 March 2016, DOI: 10.17265/2159-5291/2016.03.004. https://www.davidpublisher.com/Public/uploads/Contribute/56f9dc2771fbb.pdf
4. J. Hu, E. Shan, S. Wang, C. Wang and B. Wei, *Total domination polynomials of graphs*, arXiv:1607.00400v1 (1 July 2016). https://arxiv.org/pdf/1607.00400
