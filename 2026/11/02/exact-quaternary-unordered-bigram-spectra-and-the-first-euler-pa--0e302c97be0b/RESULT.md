# Exact quaternary unordered-bigram spectra and the first Euler-parity obstruction

## Finding

Let \(\Sigma=\{0,1,2,3\}\). For each word \(w=w_0\cdots w_m\in\Sigma^{m+1}\), \(m\ge1\), observe the **multiset of compositions of its overlapping length-two factors**: for every \(0\le i\le j\le3\), retain the multiplicity \(c_{ij}(w)\) of adjacent positions carrying the unordered pair \(\{i,j\}\). Thus \(c_{ij}\) counts both orders when \(i<j\), while \(c_{ii}\) counts repetitions of \(i\). Let \(T_m\) denote the number of distinct ten-coordinate multiplicity profiles over all words of length \(m+1\), without fixed endpoints.

The exact generating function is
\[
\boxed{\sum_{m\ge1}T_m z^m=\frac{N(z)}{(1-z)^{10}(1+z)^4},}
\]
where
\[
\begin{aligned}
N(z)={}&10z-26z^2+22z^3+85z^4-120z^5-23z^6
 +178z^7-126z^8\\
&-70z^9+128z^{10}-30z^{11}-30z^{12}+20z^{13}-4z^{14}.
\end{aligned}
\]
The values for \(m=1,\ldots,12\) are
\[
10,34,116,367,1060,2782,6704,14963,31276,61738,116020,208848.
\]
For every \(m\ge1\), \(T_m\) is a degree-nine quasipolynomial of **exact period two**. In particular,
\[
\boxed{T_m=\frac{7}{8\cdot9!}m^9+O(m^8),\qquad
\lim_{m\to\infty}\frac{T_m}{\binom{m+9}{9}}=\frac78.}
\]
The exact optimal size of a zero-error code in which the decoder sees only this complete unordered length-two composition multiset equals \(T_m\): choose one representative word for each realizable profile.

## Assumptions and scope

Words are **linear**, not cyclic, and the alphabet consists of four **labeled** symbols. Factor positions overlap; multiplicities, including identical-letter pairs, are preserved. End symbols are not separately revealed. Word length is \(m+1\ge2\); words need not use every alphabet letter. A profile is a nonnegative integer vector \((c_{ij})_{0\le i\le j\le3}\) with total \(\sum c_{ij}=m\). Distinct vectors count as distinct observations, regardless of how many words produce each.

We use the following four-vertex multigraph model. The count \(c_{ij}\) describes \(c_{ij}\) undirected edges between vertices \(i,j\), with a loop when \(i=j\). An active vertex is incident to at least one edge, including a loop; connectivity is required only on the active vertices. Loops contribute two to degree. By the undirected Euler-trail criterion, this profile is realizable by a word exactly when its active graph is connected and the number of odd-degree vertices is zero or two.

## Proof

**1. Exact word--trail correspondence.** For any word, consecutive symbols trace an Euler trail of the edge multiset, so its profile is connected on active vertices and has zero or two odd-degree vertices. Conversely, in any such multigraph an Euler trail using each edge once exists; reading its vertex sequence gives a word of length \(m+1\) realizing the profile. Hence it suffices to count these edge-multiplicity vectors without weighting them by their numbers of Euler trails.

**2. Connected supports with at most three active vertices.** If exactly one vertex is active, the graph consists of at least one loop, giving \(4z/(1-z)\). If exactly two are active, their connecting nonloop edge multiplicity is positive and the two loop multiplicities are arbitrary, giving \(6z/(1-z)^3\). If exactly three are active, the underlying simple nonloop support must be a tree with two edges (three choices for a specified triple) or a triangle (one choice); the three loops are arbitrary. Summing over the four triples gives \(12z^2/(1-z)^5+4z^3/(1-z)^6\). Every connected graph on at most three vertices automatically has at most two odd vertices by the handshake lemma, so no parity subtraction is required here.

**3. All connected four-vertex supports.** The number of connected labeled simple graphs on four vertices with respectively three, four, five, or six edges is \(16,15,6,1\). Indeed, the sixteen three-edge cases are trees (Cayley's formula), and every simple four-vertex graph with at least four edges is connected. Each selected nonloop edge has positive multiplicity, with generating function \(z/(1-z)\); the four loops are unrestricted. Ignoring parity, the four-active contribution is
\[
C_4(z)=\frac{16z^3}{(1-z)^7}+\frac{15z^4}{(1-z)^8}
+\frac{6z^5}{(1-z)^9}+\frac{z^6}{(1-z)^{10}}.
\]

**4. Exactly the forbidden four-odd profiles.** Write \(F\) for the simple graph of nonloop edges having **odd** positive multiplicity. The parity of a vertex's total multigraph degree is exactly its degree in \(F\), because loops add two and even nonloop multiplicities add even degrees. Of the \(2^6\) subgraphs of \(K_4\), exactly eight have all four degrees odd: the three perfect matchings, the four three-edge stars, and \(K_4\) itself. To see completeness, the incidence parity map of the connected \(K_4\) has rank three over \(\mathbb F_2\), hence each attainable even-cardinality odd-vertex set has \(2^{6-3}=8\) preimages; the eight listed graphs are distinct and exhaust this fiber.

An edge with odd positive multiplicity contributes \(O(z)=z/(1-z^2)\); an edge with positive even multiplicity contributes \(E(z)=z^2/(1-z^2)\). A non-\(F\) edge may either be absent or have positive even multiplicity, contributing \(1+E(z)\). For a matching, at least one of the four other edges must be present to connect the two matched pairs; its contribution is \(3O^2((1+E)^4-1)\). Every star already connects all vertices, contributing \(4O^3(1+E)^3\); \(K_4\) contributes \(O^6\). Four loop multiplicities are free, so the forbidden contribution is exactly
\[
B_4(z)=\frac{3O(z)^2((1+E(z))^4-1)+4O(z)^3(1+E(z))^3+O(z)^6}{(1-z)^4}.
\]
All these profiles have four active vertices and fail the Euler-trail parity test. Conversely, by the exhaustive parity-fiber argument, no other connected profile fails that test.

**5. Summation, algebra and asymptotics.** Combining the disjoint cases yields
\[
\sum_{m\ge1}T_mz^m=\frac{4z}{1-z}+\frac{6z}{(1-z)^3}
+\frac{12z^2}{(1-z)^5}+\frac{4z^3}{(1-z)^6}+C_4(z)-B_4(z).
\]
Substitute \(1+E(z)=1/(1-z^2)\), bring to a common denominator, and cancel factors; the result is exactly the stated \(N(z)/((1-z)^{10}(1+z)^4)\). Direct evaluation gives \(N(1)=14\) and \(N(-1)=-6\). Thus \(z=1\) is a pole of order ten with leading coefficient \(N(1)/2^4=7/8\), while \(z=-1\) is a genuine pole of order four. Partial fractions therefore give a degree-nine polynomial in \(m\) plus \((-1)^m\) times a nonzero degree-three polynomial (for \(m\ge1\)), proving exact quasipolynomial period two and the leading asymptotic coefficient. The unrestricted number of ten-coordinate nonnegative vectors of total \(m\) is \(\binom{m+9}{9}\); its leading coefficient is \(1/9!\), so the limiting feasible fraction is \(7/8\).

## Verification

Run `python3 verify.py` in the extracted package. The checker independently constructs unordered adjacent-pair profiles by literal enumeration of every four-letter word of lengths two through nine (349,520 words). Separately, it enumerates all nonnegative ten-edge multiplicity vectors of totals one through twelve (646,645 vectors), tests the undirected Euler criterion directly, and matches both enumerations against the reduced rational generating function using exact integer coefficients. It checks the twelve displayed values.

Recorded output:

`VERIFY_OK literal_lengths=2..9 literal_words=349520 graph_profiles_m=1..12 profile_vectors_tested=646645 rational_coefficients_m=1..12 exact_match=True`

The finite tests are corroborative and do not constitute the all-length proof, which is the exhaustive four-vertex support/parity classification above.

## Relationship to prior work

Ye and Elishco (2022) introduce the general \(r\)-length-limited substring **composition**-multiset model, including arbitrary alphabet sizes in their Section VIII, and construct reconstruction codes for growing \(r\). The present statistic is specifically the isolated length-two composition multiset on a quaternary alphabet; it does not include the singleton compositions supplied by the \(r\)-limited model. The distinction is strict: `010` and `101` have identical length-two unordered pair profiles, yet different singleton-composition counts. Their results do not specify this exact observation-space cardinality.

Gabrys and Milenkovic (2018) analyze **ordered** fixed-length substring multispectra and coded reconstruction, predominantly over a binary alphabet. Gupta and Mahdavifar (2022) consider the multiset of **all-length binary substring compositions**. These observation models differ both in retained orientation or read length and in alphabet size. The previously published exact **binary ordered** two-multispectrum enumeration resolves another, strictly different, special case. None of these checked results states the present quaternary unordered all-length rational function or the four-odd parity correction.

Jacquet, Knessl and Szpankowski (2010) count balanced **directed** Markov types arising from cyclic words. Their directed balanced-matrix model is distinct from the linear undirected trail profiles here; its cyclic asymptotics do not provide the quaternary unordered formula.

The general Euler-trail criterion and the classification of parity subgraphs of \(K_4\) are classical ingredients, not claims of novelty. What is asserted as the new, specific contribution is the all-length output-spectrum enumeration, exact period, and \(7/8\) asymptotic fraction for this four-letter observation model.

## Limitations

This result is restricted to four labeled symbols, complete and noiseless multiset observation of overlapping unordered adjacent pairs, and unrestricted word endpoints. It does not count the sizes of individual equivalence classes or address cyclic strings, missing reads, or error correction. The derivation uses classical Euler-trail theory. The literature search did not locate an equivalent exact formula, but older multigraph-enumeration tables or an unindexed specialization could contain the same count; novelty requires external assessment. Independent validation has not been performed.

## References

1. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963v1, first submitted 2022-08-31; Section VIII on the length-limited composition model. https://arxiv.org/abs/2208.14963
2. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v1 (2018). https://arxiv.org/abs/1804.04548
3. U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955v1 (2022). https://arxiv.org/abs/2201.09955
4. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768. https://dmtcs.episciences.org/2768
5. *Exact binary two-multispectrum code size and singleton classification*, published research note, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71
