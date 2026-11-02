# A circular multiset-word spectrum for a nonmonotone chain pattern

## Finding
Let \(\mathcal A=\{1,\ldots,a\}\) be any finite totally ordered alphabet, with commuting indeterminates \(\mathbf x=(x_1,\ldots,x_a)\). Write \(e_j(\mathbf x)=\sum_{1\le i_1<\cdots<i_j\le a}x_{i_1}\cdots x_{i_j}\) and \(e_j=0\) for \(j>a\). For \(n\ge1\), take a word \(w=w_1\cdots w_n\) on positions indexed modulo \(n\). A cyclic occurrence of the five-letter pattern \(12435\) begins at a position \(i\) when \((w_i,\ldots,w_{i+4})\), read modulo \(n\), comprises five distinct letters in that order pattern. For \(n<5\) stipulate no occurrence. Denote the number by \(c_p(w)\), and put \(t=y-1\).

Define the formal series
\[
A(z,t,\mathbf x)=ze_1(\mathbf x)+\sum_{r\ge1}\ \sum_{(d_1,\ldots,d_{r-1})\in\{3,4\}^{r-1}}t^r z^{5+\sum_jd_j}e_{5+\sum_jd_j}(\mathbf x).
\]
Then the complete multivariate cardinality-and-content distribution is
\[
\boxed{\sum_{n\ge1}z^n\sum_{w\in\mathcal A^n}y^{c_p(w)}\prod_{j=1}^nx_{w_j}=
\left.\frac{z\,\partial_z A(z,t,\mathbf x)}{1-A(z,t,\mathbf x)}\right|_{t=y-1}.}
\]
Exactly the same identity holds for \(p=13245\). In particular, for each fixed content vector \((m_1,\ldots,m_a)\), the polynomial in \(y\) is unchanged under every permutation of the entries of that vector. Positions are indexed; words identified up to rotation are not counted here.

## Assumptions and scope
All words have positive length. The ordered alphabet is finite and may contain unused letters. Counts include all labelled choices of the cyclic origin, even when a word has a nontrivial rotational stabilizer. The pattern always requires five pairwise distinct letters, so no occurrence exists at length less than five. The identity is a formal power series in \(z\) with polynomial coefficients in \(y,\mathbf x\), requiring no analytic convergence.

## Proof
Mark an arbitrary subset \(M\) of the cyclic occurrences in a word. Expanding \(y^{c_p(w)}=(1+t)^{c_p(w)}\) amounts to giving a factor \(t\) for each marked occurrence. For both patterns, two marked starts can overlap consistently at clockwise shifts \(3\) or \(4\) only: prefix--suffix standardisations differ at shifts \(1\) and \(2\). Every compatible overlapping chain with consecutive shifts in \(\{3,4\}\) imposes one **total order** on all its letters. To see the extension explicitly, a shift \(4\) shares the old final letter (the old largest letter) with the next occurrence's first (smallest) letter, so all four new letters are larger. At shift \(3\), the overlapping old last two positions are the next pattern's first two positions. For \(12435\), their relative ranks are \(1,2\), and the three new letters are placed in the unique remaining ranks \(3,4,5\). For \(13245\), the old final two positions are in increasing order, and the next pattern's first two ranks are \(1,3\); the new first position fills rank \(2\), and the other new positions fill ranks \(4,5\). In each case, the new occurrence's last letter is greater than the old last letter. An induction proves the unique total order and the strict increase of last-letter values along every chain.

There cannot be a cyclic chain of marked occurrences for which *every* clockwise gap between successive starts is \(3\) or \(4\). Such a chain would force the last letters of those occurrences to increase strictly all the way around the cycle back to the first. Hence every nonempty marked configuration has at least one gap of \(5\) or more and breaks canonically into cyclically arranged proper marked chains, separated by zero or more uncovered singleton positions. A chain of \(r\) occurrences with overlap gaps \(d_1,\ldots,d_{r-1}\in\{3,4\}\) occupies \(\ell=5+\sum d_j\) consecutive positions. Its total-order property implies that for each choice of \(\ell\) distinct alphabet letters exactly one letter assignment satisfies all marked constraints; its content weight is therefore \(e_\ell(\mathbf x)\). A singleton position contributes \(e_1(\mathbf x)\). These are precisely the atomic summands of \(A\), whose \(t\)-degree records marked occurrences.

Finally, the generating series of a cyclically ordered sequence of nonempty atoms, with the underlying positions indexed and one position distinguished as index \(1\), is \(z\partial_z[-\log(1-A)]=z(\partial_z A)/(1-A)\). Indeed, expanding \(-\log(1-A)=\sum_{k\ge1} A^k/k\) counts cyclic lists of \(k\) atoms; differentiating and multiplying by \(z\) marks any one of the \(n\) positions in a resulting length-\(n\) circular word. The decomposition is canonical, so it has neither omissions nor multiplicity. This proves the claimed series. As all its coefficients in \(\mathbf x\) are symmetric functions, permuting letter multiplicities cannot change the occurrence polynomial. The argument uses the same allowed overlaps and single-chain enumerators for the two displayed patterns.

## Verification
The accompanying standalone script `verification/cyclic_patterns_check.py` independently enumerates both pattern-occurrence histograms for six small multiset content types, totaling \(447{,}720\) examined words. It also computes the marked-coefficient expansion of the stated series by exact rational dynamic programming, checks all coefficients, and checks overlap consistency for \(126\) chain instances through six marked occurrences. Sample outputs for eight distinct letters are \(37640\) words with zero occurrences, \(2672\) with one, and \(8\) with two, for either pattern. These finite checks do not establish the theorem for arbitrary lengths; the preceding decomposition does.

## Relationship to prior work
Chen, Fang and Kitaev (arXiv:2602.13566, February 2026) formulated stability questions for consecutive patterns on linear multiset words. Li's September 2026 working paper `Stable Consecutive Patterns and Chain Clusters` proves a chain-cluster characterization of stability for *linear* multiset words and identifies nonmonotone stable examples including \(12435\); neither linear stability nor its occurrence-position refinement is claimed here as new. Elizalde and Sagan (arXiv:2107.04717) treat consecutive-pattern occurrences on circular **permutations with distinct entries** and give general circular-to-linear transformations; their theorem does not give content-refined cyclic-word distributions with arbitrary repeated letters. The present identity explicitly enumerates the wraparound contributions for the multiset setting, including all multiplicities. It is also compatible with the elementary reverse-complement symmetry relating the two patterns, combined with multiplicity stability. Historical priority beyond the examined sources is not conclusively established.

## Limitations
This is an ordinary, indexed-position enumeration, not an enumeration of necklaces modulo rotations. The explicit series here is for the two displayed five-letter patterns; a universal cyclic stability theorem for all chain patterns has not been proved. One closely relevant September 2026 paper was inspectable through its published abstract and metadata, not its complete primary manuscript, leaving possible implicit coverage in that paper or earlier general cyclic-cluster literature. No independent mathematical audit has been performed.

## References
1. S. Chen, H. Fang, S. Kitaev, *Stable patterns on permutations of multisets*, arXiv:2602.13566 (first public February 2026).
2. A. C. Li, *Stable Consecutive Patterns and Chain Clusters*, Zenodo DOI:10.5281/zenodo.22568329, first public September 7, 2026; public abstract at https://crabresearch.com/research/stable-chain-patterns .
3. S. Elizalde and B. Sagan, *Consecutive patterns in circular permutations*, arXiv:2107.04717 (2021).
