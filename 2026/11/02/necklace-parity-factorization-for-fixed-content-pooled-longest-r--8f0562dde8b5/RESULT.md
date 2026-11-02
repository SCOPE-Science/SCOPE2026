# Necklace-parity factorization for fixed-content pooled longest-read reconstruction

## Finding

Fix an alphabet of \(q\ge 2\) labeled symbols and a length-\(n\) content vector \(\mathbf c=(c_0,\ldots,c_{q-1})\) with \(n=\sum_i c_i\ge 2\), \(c_i\ge 0\), and at least two positive entries. A source is an unordered **multiset** \(M\) of exactly \(k\ge 0\) words of content \(\mathbf c\), allowing repetitions. Its observation \(\mathcal R(M)\) is the unordered multiset, **with multiplicities**, of both ordered length-\((n-1)\) reads from every source word: its prefix and suffix. A read does not carry a prefix/suffix label or source identity.

Write \(T=\dfrac{n!}{\prod_i c_i!}\). For any even divisor \(d\) of \(n\), put \(t=n/d\). If \(t\) divides every \(c_i\), define
\[
\nu_{\mathbf c}(d)=\frac{1}{d}\sum_{h\mid\gcd(c_0/t,\ldots,c_{q-1}/t)}\mu(h)\frac{(d/h)!}{\prod_i(c_i/(th))!};
\]
otherwise put \(\nu_{\mathbf c}(d)=0\). Here \(\mu\) is the ordinary number-theoretic Möbius function; zeros in the content vector contribute \(0!=1\) and do not alter the gcd.

Let \(A_{\mathbf c,k}\) be the number of distinct observations \(\mathcal R(M)\), and let \(S_{\mathbf c,k}\) be the number of observations having exactly one source multiset. Then the following rational generating functions hold as formal power series:
\[
\boxed{\sum_{k\ge0} A_{\mathbf c,k}z^k=(1-z)^{-T}\prod_{\substack{d\mid n\\2\mid d}}(1-z^{d/2})^{\nu_{\mathbf c}(d)}}
\]
and
\[
\boxed{\sum_{k\ge0} S_{\mathbf c,k}z^k=(1-z)^{-T}\prod_{\substack{d\mid n\\2\mid d}}(1-z^{d/2})^{2\nu_{\mathbf c}(d)}.}
\]
Thus \(A_{\mathbf c,k}\) is exactly the largest cardinality of a zero-error reconstruction code restricted to size-\(k\) source multisets with content \(\mathbf c\): select one multiset from each observation class.

The **entire ambiguity mechanism** is determined by cyclic rotation orbits of words. A primitive odd-length orbit is uniquely reconstructible. For an even orbit of size \(d=2r\), label its edge multiplicities cyclically \(a_0,\ldots,a_{d-1}\). If \(m_{\rm even}=\min_j a_{2j}\) and \(m_{\rm odd}=\min_j a_{2j+1}\), this component has precisely \(m_{\rm even}+m_{\rm odd}+1\) feasible source-multiset representations for its read profile. Representations from distinct rotation orbits multiply.

If \(n\) is odd, every profile is uniquely reconstructible for every \(k\). If \(n\) is even, set \(g=\gcd(c_0,\ldots,c_{q-1})\); let \(t_*\) be the largest positive divisor of \(g\) for which \(n/t_*\) is even, and set \(d_*=n/t_*\). Then \(\nu_{\mathbf c}(d_*)>0\), all profiles are unique for \(k<d_*/2\), and at \(k=d_*/2\) there are exactly \(\nu_{\mathbf c}(d_*)\) ambiguous profiles, each with exactly two source multisets.

For example, with three symbols and content \(\mathbf c=(1,1,2)\), there are \(T=12\) words and exactly three primitive even rotation orbits of length four. At pool size \(k=2\), there are \(A_{\mathbf c,2}=75\) profiles, of which \(S_{\mathbf c,2}=72\) are singleton; the other three have exactly two preimages. With content \(\mathbf c=(2,2,2)\), there are fourteen length-six even rotation orbits and no shorter even orbit, so the first ambiguous profiles arise at pool size three: exactly fourteen ambiguous profiles.

## Assumptions and scope

The observation contains precisely two reads per source word, including duplicate reads when a word has equal prefix and suffix. Strings are ordered sequences; the source collection is an unordered multiset and its elements may be repeated. Every source word has exactly the same specified content. The alphabet is labeled, not quotiented by symbol permutations, and the observation retains the full order of symbols inside each read. Code size means the number of distinguishable **multisets**, not the number of distinguishable individual words and not a noisy-channel rate. The convention \(k=0\) yields one empty source and one empty profile. We exclude single-symbol compositions: for those the sole possible source word trivially makes all profiles unique.

## Proof

**1. Reduction to disjoint rotation cycles.** Let \(u\) be a length-\((n-1)\) read that can occur for content \(\mathbf c\). Exactly one alphabet symbol, say \(a\), must be added to its content to recover \(\mathbf c\). Therefore there are exactly two full-content words involving this read, namely \(au\) and \(ua\); the former has suffix \(u\) and the latter has prefix \(u\). These two words are cyclic shifts. Identify a full-content word \(w\) with an edge from its prefix \(w_1\cdots w_{n-1}\) to its suffix \(w_2\cdots w_n\). Both endpoints have degree two in the underlying multigraph (counting incidences); the unique possible predecessor and successor of each edge are successive cyclic rotations of \(w\). Consequently, the entire full-content read graph is a disjoint union of undirected cycles, one for each cyclic rotation orbit. Its \(T\) edges are in bijection with all full-content words. This remains valid for a period-two orbit (two parallel edges) and for a period-one orbit (one loop).

**2. Fiber sizes.** On a cycle of length \(d\) label consecutive edges \(a_0,\ldots,a_{d-1}\), each a nonnegative integer giving the number of corresponding source words. At vertex \(i\), the observed read multiplicity is \(b_i=a_{i-1}+a_i\), with subscripts modulo \(d\). If another edge vector \(a'_i\) has the same vertex counts, subtraction gives \(a'_i-a_i=-(a'_{i-1}-a_{i-1})\). Going once around an odd cycle forces all differences zero; on an even cycle \(d=2r\), precisely the differences \(a'_i-a_i=(-1)^i s\), for an integer \(s\), are allowed. Nonnegativity is equivalent to \(-m_{\rm even}\le s\le m_{\rm odd}\). The number of distinct vectors is therefore \(m_{\rm even}+m_{\rm odd}+1\). Since the read vertices belonging to distinct rotation orbits are disjoint, their constraints are independent and their fiber multiplicities multiply.

**3. Canonical representatives and the two generating functions.** On each even cycle, subtract \(m_{\rm even}\) from every even-indexed edge count and add it to every odd-indexed edge count. This is the unique member of its fiber with minimum even-indexed count zero. The transformation preserves total source size because the two parity classes each have \(r\) edges. Hence a profile of that component is represented exactly once by a nonnegative edge vector in which at least one of the \(r\) even-indexed counts vanishes. All edge-count vectors have generating function \((1-z)^{-d}\); those with all \(r\) even counts strictly positive have generating function \(z^r(1-z)^{-d}\). Thus the local profile generating function is \((1-z^r)(1-z)^{-d}\).

In a canonical representative, the fiber size is \(1+\min_j a_{2j+1}\). It is singleton exactly when at least one odd-indexed edge count also vanishes. Inclusion-exclusion on the two disjoint parity classes gives local singleton-profile generating function \((1-z^r)^2(1-z)^{-d}\). Odd cycles contribute \((1-z)^{-d}\) to both series. Multiplying over all rotation orbits, with total edge count \(T\), gives both boxed product formulas.

**4. Exponents from primitive necklaces.** A rotation orbit of size \(d\) consists of repetitions of a primitive length-\(d\) word \(t=n/d\) times. Such an orbit can have content \(\mathbf c\) only when \(t\mid c_i\) for every symbol. The number of primitive words of reduced content \(\mathbf c/t\) is obtained by subtracting proper repetitions by Möbius inversion:
\[
\sum_{h\mid\gcd(c_0/t,\ldots,c_{q-1}/t)}\mu(h)\frac{(d/h)!}{\prod_i(c_i/(th))!}.
\]
Dividing by the size \(d\) of each primitive rotation orbit yields \(\nu_{\mathbf c}(d)\). This count is an integer by its necklace interpretation.

**5. First possible ambiguity.** An even cycle of length \(d=2r\) has a nonsingleton profile only if an edge-count representation can be shifted by one to a distinct nonnegative vector. That requires either all \(r\) even counts or all \(r\) odd counts positive, and hence at least \(r\) source words. Conversely, at source size exactly \(r\), the two alternating perfect matchings (one word on each parity-class edge, zero elsewhere) give the same read profile and no third source. The smallest feasible even primitive orbit size is \(d_*\) as stated: a period \(d\) of content \(\mathbf c\) must satisfy \(n/d\mid g\), and it must be even. The longest admissible repetition number is \(t_*\). There exists a primitive word with reduced content \(\mathbf c/t_*\): arrange the positive-symbol runs contiguously; because at least two symbols occur, its cyclic word has exactly one maximal circular run of each occurring symbol, which rules out a nontrivial power. Thus \(\nu_{\mathbf c}(d_*)\ge1\). At \(k=d_*/2\), the only ambiguous profiles are the two-matching profiles of these shortest even cycles, one per orbit, giving exactly \(\nu_{\mathbf c}(d_*)\) two-element fibers. If \(n\) is odd, none of its divisors is even, so every rotation cycle is odd and every profile is unique.

## Verification

The accompanying standalone `verify.py` uses two independent descriptions: direct enumeration of all fixed-content source multisets and their literal prefix/suffix-read multiplicities, and the Möbius product formulas. It additionally rotates words directly to check the claimed number of even primitive orbits. The tested finite parameter range includes binary compositions with total length at most eight and pool size at most three, ternary compositions with total length at most six and pool size at most three, and four-symbol compositions with total length at most five and pool size at most two; compositions with fewer than two occupied symbols are omitted. It checks \(687\) content/pool-size instances and \(602{,}425\) distinct source multisets and reports `VERIFY_OK`. The proof above, not finite enumeration, establishes the formulas for all parameters.

## Relationship to prior work

Yehezkeally, Marcovich and Yaakobi (2021, arXiv:2108.11725) define the multi-strand substring profile and study asymptotically efficient reconstruction codes; here their profile is specialized to length \(n-1\) while restricting the source compositions, and an exact finite-length image-and-singleton enumerator is derived. The later generalized reconstruction work (arXiv:2210.04471) likewise concerns reconstruction bounds and constructions, not this closed necklace-parity product. Sawada and Williams' fixed-content universal-cycle work provides the known shorthand/read-graph and necklace-cycle setting; the observation here is not a universal-cycle construction but a classification of pooled read-profile fibers and their enumerations. Gabrys, Pattabiraman and Milenkovic (arXiv:2110.02352) study pooled **prefix/suffix compositions**, whereas this result retains full read strings and uses only the two longest reads. Yang and Chen (arXiv:2411.03776) later consider several constant-weight strings with composition observations at all prefix/suffix lengths; those are different measurement maps.

The previously established two-symbol, single-marker case \(\mathbf c=(n-1,1)\) has the same parity phenomenon and a one-factor counting formula. It is a special case of the present theorem, **not** a new case here: for even \(n\), there is a single even cycle of length \(n\), and the profile series becomes \((1-z^{n/2})(1-z)^{-n}\). The present result handles arbitrary labeled alphabets and arbitrary content with many simultaneous even necklace cycles, giving the two distinct product formulas, the full multiplicative fiber mechanism and a sharp first-ambiguity census. These conclusions do not follow from that single-marker formula alone.

## Limitations

The proof assumes exact complete unordered read multiplicities, fixed common source content, and exactly the longest two overlapping reads per source. It does not address random or noisy sequencing, variable content between strands, unknown strand count, missing reads, or the computational complexity of enumerating exponentially many observation profiles. The known primitive-necklace and graph-incidence tools are part of the proof, not claimed as individually original. Possible equivalents expressed in graph-flow or cyclic-word terminology remain a literature-discovery risk; no independent scientific audit has been conducted.

## References

1. Yonatan Yehezkeally, Sagi Marcovich and Eitan Yaakobi, *Multi-strand Reconstruction from Substrings*, first public August 26, 2021, arXiv:2108.11725. https://arxiv.org/abs/2108.11725
2. Yonatan Yehezkeally, Daniella Bar-Lev, Sagi Marcovich and Eitan Yaakobi, *Generalized Unique Reconstruction from Substrings*, first public October 10, 2022, arXiv:2210.04471. https://arxiv.org/abs/2210.04471
3. Joe Sawada and Aaron Williams, *Constructing the first (and coolest) fixed-content universal cycle*, available full text. https://socs.uoguelph.ca/~sawada/papers/Cool_Fixed_Content_Ucycle.pdf
4. Ryan Gabrys, Srilakshmi Pattabiraman and Olgica Milenkovic, *Reconstruction of Sets of Strings from Prefix/Suffix Compositions*, first public October 5, 2021, arXiv:2110.02352. https://arxiv.org/abs/2110.02352
5. Yaoyu Yang and Zitan Chen, *Reconstruction of Multiple Strings of Constant Weight from Prefix–Suffix Compositions*, first public November 6, 2024, arXiv:2411.03776. https://arxiv.org/abs/2411.03776
