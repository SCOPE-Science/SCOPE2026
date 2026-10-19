# Five minimal-fort orbits and eleven minimum-zero-forcing orbits of \(Q_4\)

## Finding

**Theorem (complete orbit-resolved fort/forcing classification).** Let \(Q_4\) be the four-dimensional binary hypercube, with sixteen vertices. Its inclusion-minimal forts form exactly **five** orbits under its full automorphism group of order \(384\): two orbits of four-vertex forts, of sizes \(16\) and \(12\); one orbit of six-vertex forts, of size \(32\); and two orbits of eight-vertex forts, of sizes \(192\) and \(96\). Thus the already-known total \(348\) separates into the exact spectrum \(28,32,288\) at cardinalities \(4,6,8\).

The ordinary zero-forcing polynomial is
\[
\mathcal Z_{Q_4}(z)=2360z^{8}+6016z^{9}+6240z^{10}+4032z^{11}+1792z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\]
Among the \(21137\) zero-forcing sets, exactly \(2360\) are inclusion-minimal. They all have size \(8\), making \(Q_4\) **well-forced**, and break into exactly **eleven** symmetry orbits with orbit-size multiset \(\{8,48,96,96,192,192,192,384,384,384,384}\). Under simultaneous synchronous color changes, the \(2360\) minimum sets have propagation-time counts \(8,816,1152,384\) at times \(1,2,3,4\), respectively.

The explicit labeled representatives and their orbit sizes are in `CLASSIFICATION.json`; its binary mask \(m\) means the vertex set \(\{v:0\le v<16,\;\text{bit}_v(m)=1}\).

## Assumptions and scope

Vertices are four-bit vectors indexed by the integers \(0,\ldots,15\), with an edge precisely when two labels differ in one bit. A fort is a **nonempty** set \(F\) for which no vertex outside \(F\) has exactly one neighbor inside \(F\). A fort is *inclusion-minimal* if no nonempty proper subset is a fort; it need not be smallest by size. A zero-forcing set is an initially black set from which repeated application of the ordinary rule (a black vertex with exactly one white neighbor colors that neighbor black) colors every vertex. 'Minimum' means smallest size, while 'inclusion-minimal' forbids any proper zero-forcing subset. Synchronous propagation time is the number of rounds when all currently available forces are applied simultaneously; it is not an asynchronous chronological extremum. All conclusions are for this one finite graph and ordinary, not skew or positive-semidefinite, zero forcing.

## Proof

**1. Fort duality.** An initial set \(S\) fails to force exactly when its complement contains a fort. In one direction, a nonempty all-white fort cannot lose its first white vertex to a black forcing neighbor, because that neighbor has zero or at least two neighbors in the fort. In the other direction, if ordinary forcing stops short, the nonempty set of remaining white vertices has no outside vertex with exactly one neighbor inside it, and hence is a fort. Accordingly \(S\) is zero forcing if and only if it meets every inclusion-minimal fort.

**2. An exhaustive, exact recurrence.** Represent a subset by its sixteen-bit mask \(m\). The neighbor mask of label \(v\) is the bitwise union of \(v\oplus1\), \(v\oplus2\), \(v\oplus4\), and \(v\oplus8\). Let \(f(m)\) be the Boolean predicate that the nonempty labeled subset \(m\) is a fort (check every outside vertex against the four-bit neighbor mask). Define \(h(0)=\mathrm{false}\) and, in increasing integer mask order, compute
\[
h(m)=f(m)\lor\bigvee_{v\in m}h\bigl(m\setminus\{v\}\bigr).
\]
This recurrence is valid because every nonempty subfort is either all of \(m\), or a subset of one of its single-vertex deletions. Consequently, \(m\) is inclusion-minimal as a fort precisely if \(f(m)\) holds and all \(h(m\setminus\{v\})\) are false; note that merely checking that the immediate deletions themselves are not forts would be insufficient. For every black mask \(s\), the duality in Step 1 gives the exact test \(\neg h((2^{16}-1)\mathbin{\mathrm{xor}}s)\). The verifier loops over **every one** of the \(65536\) masks, obtains the five-orbit minimal-fort table and every coefficient above, and finds exactly \(2360\) inclusion-minimal black sets of size \(8\). This is exhaustive finite verification, not an inference from a sample.

**3. Independent direct forcing computation.** Independently construct neighbor masks by XOR bit flips. For each of the \(65536\) initial black sets, concurrently add every sole white neighbor of each current black vertex, or stop if none exists; at most sixteen additions can occur. The direct implementation obtains precisely the polynomial and minimum-set list in Step 2. `verify_crosscheck.py` tests equality of the two Boolean decisions for **every** mask. The direct method separately measures simultaneous propagation times, producing the stated four counts. It checks inclusion-minimality using all one-vertex deletions, which is sufficient here because zero-forcing sets are upward closed.

**4. Full symmetry and orbit completeness.** Every map \(x\mapsto a\oplus\sigma(x)\), with \(a\) any four-bit vector and \(\sigma\) any permutation of the four coordinates, preserves adjacency. Conversely any graph automorphism is determined by the image of vertex \(0\) (sixteen possibilities) and its bijection on the four neighbors: images of all remaining vertices are then determined inductively by their already-mapped predecessors at smaller Hamming distance. Thus the automorphism group has exactly \(16\cdot24=384\) elements. The verifiers enumerate all these distinct maps; for each least remaining representative, they compute its complete image orbit, assert every image is in the target family, and remove it. The orbit lists in `CLASSIFICATION.json` have sizes summing to \(348\) and \(2360\), respectively, and therefore exhaust both families without multiplicity.

## Verification

Run `python3 verify_forcing.py`, `python3 verify_forts.py`, and `python3 verify_crosscheck.py` in one directory with standard Python. The first uses direct synchronous coloring, the second an independent adjacency-matrix fort test and full downward-subset recurrence, and the third verifies all \(65536\) Boolean decisions agree. Both independently enumerate the \(384\) cube automorphisms, with distinct coordinate-permutation implementations. Output assertions include all coefficients, size spectra, orbit sizes, minimum sets and propagation times. `CLASSIFICATION.json` contains all orbit representatives and aggregate certificates; it depends only on the explicit sixteen-label convention. The scripts are complete finite verifiers rather than logs or a claim of independent mathematical certification.

## Relationship to prior work

The foundational AIM work [1], first publicly available on **26 November 2007**, established the scalar hypercube equality \(Z(Q_d)=2^{d-1}\); therefore the scalar \(Z(Q_4)=8\) is **not new**. Boyer et al. [2] established the zero-forcing polynomial framework, but their inspected full text does not discuss hypercubes. Becker et al. [3] established general minimal-fort results and constructions, not this orbit table.

Brimkov, Cameron and Grubbs [4, Sections 3–6] already classified the \(28\) smallest forts of \(Q_4\) into two types, constructed at least \(60\) inclusion-minimal forts and, in their **Conclusion**, explicitly reported the computational total of **348** inclusion-minimal forts. That total is already covered and is only independently reproduced here. Their paper explicitly leaves the complete structural classification of minimal forts and complete enumeration of minimum zero-forcing sets unresolved. The retained addition is the **complete five-orbit fort spectrum, eleven-orbit minimum forcing classification, well-forcedness, and propagation-time multiplicities**, together with a transparent certificate.

Lawrence's 2023 thesis [5, Chapter 5, Figure 5.2], related to Curtis et al. [6], already displays an **exact** probability curve for random zero forcing on the sixteen-vertex hypercube. As an exact function of the sampling probability that curve implicitly determines the zero-forcing polynomial, so the polynomial alone is **not** asserted as an independently unprecedented invariant. Neither the plotted curve nor the accompanying analysis supplies the eleven symmetry classes, the complete minimal-fort structural spectrum, or well-forcedness. The explicit coefficient table is included to make the orbit classification reproducible and numerically testable.

## Limitations

No statement is made for hypercubes of dimension other than four, nor about asymptotic formulas, all graph isomorphism classes, or asynchronous minimum propagation time. Exhaustive finite checking establishes this labeled graph exactly; it is not a general infinite-graph proof. The older scalar, twenty-eight minimum-fort count, and total \(348\) are prior-covered. Published-code supplements and unindexed historical calculations could still contain the same finer orbit classification; independent priority and mathematical audits have not occurred. These limits do not weaken the finite statement above.

## References

1. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra Appl. 428 (2008), 1628–1648, doi:10.1016/j.laa.2007.10.009 (available online 2007-11-26).
2. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910 (2018), Discrete Applied Math. 258 (2019), 35–48.
3. P. Becker et al., *On the number of minimal forts of a graph*, arXiv:2404.05963 (2024).
4. B. Brimkov, T. R. Cameron and O. Grubbs, *On the forts and related parameters of the hypercube graph*, arXiv:2507.10826 (2025).
5. R. S. Lawrence, *Simplicial Reaction Networks and Dynamics on Graphs*, University of California Berkeley dissertation (2023), Chapter 5, Figure 5.2, https://escholarship.org/uc/item/5tb6c0t8.
6. B. Curtis et al., *Zero forcing with random sets*, arXiv:2208.12899 (2022).
