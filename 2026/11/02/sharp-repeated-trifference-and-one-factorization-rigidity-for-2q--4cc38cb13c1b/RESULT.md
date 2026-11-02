# Sharp repeated trifference and one-factorization rigidity for \(2q\) codewords

## Finding
For every integer \(q\ge3\), consider an unordered set \(C\) of exactly \(2q\) distinct words of length \(2q-1\) over a fixed \(q\)-symbol alphabet. For each triple of different codewords, let its **separation multiplicity** be the number of coordinates where its three symbols are pairwise different. Then the largest possible minimum separation multiplicity is exactly \(2q-4\). Moreover, \(C\) attains this upper bound **if and only if** each coordinate partitions the \(2q\) codewords into \(q\) disjoint equal-symbol pairs, and the resulting \(2q-1\) perfect matchings constitute a one-factorization of the complete graph \(K_{2q}\). The characterization includes all optimal codes, and every one-factorization supplies optimal codes by independently labeling its pairs at each coordinate.

In particular, for ternary length-five codes with six codewords and separation multiplicity at least two, there are exactly **\(7776\) distinct labeled codebooks** (sets of six distinct words, with five fixed coordinate positions and fixed symbol names). Every such codebook is equivalent under coordinate permutations and independent symbol permutations to every other; the induced factorization of \(K_6\) is unique up to relabeling the six messages. The numerical value \(T(5,2)=6\) itself was already reported by Bishnoi and collaborators; the new statements here are the equality-case classification, general-\(q\) rigidity, and exact optimizer count.

## Assumptions and scope
Here \(q\) is an integer, not necessarily a prime power; \(q\ge3\). The alphabet is a set of \(q\) symbols, and the code may be nonlinear. A coordinate separates a triple when its three values are all distinct. A one-factor of \(K_{2q}\) is a partition of its vertices into \(q\) edges. A one-factorization is a partition of the entire edge set into \(2q-1\) one-factors. Fixed-coordinate labeled codebooks are compared by literal equality of sets of words, not by equivalence under symmetry. The theorem optimizes the separation **multiplicity for a prescribed number of codewords and coordinates**; it does not claim that \(2q\) is the largest possible number of codewords at this multiplicity for every \(q\).

## Proof
**Step 1: Sharp average bound.** At a coordinate, let the occupancies of the \(q\) symbols be nonnegative integers \(a_1,\ldots,a_q\) with \(\sum_j a_j=2q\). The number of codeword triples separated at that coordinate is the degree-three elementary symmetric sum
\[
e_3(a_1,\ldots,a_q)=\sum_{1\le i<j<k\le q}a_ia_ja_k.
\]
Maclaurin's inequality gives \(e_3\le\binom q3(2q/q)^3=8\binom q3\), with equality exactly for \(a_1=\cdots=a_q=2\). For \(q=3\), the equality statement follows also from AM-GM. Summing over \(N=2q-1\) coordinates and dividing by \(\binom{2q}3\) possible triples, the mean separation multiplicity is at most
\[
\frac{(2q-1)8\binom q3}{\binom{2q}3}=2q-4.
\]
Thus the minimum is at most \(2q-4\). If it equals this value, the upper bound for the sum and lower bound on every summand are simultaneously equalities: **each coordinate has exactly two occurrences of each symbol, and each triple is separated at exactly \(2q-4\) coordinates**. Hence its number of nonseparating coordinates is exactly three.

**Step 2: Determine the pair multiplicities.** For each coordinate, join the two codewords bearing each given symbol. This is a perfect matching \(M_i\) on the \(2q\) codewords. Let \(m_{uv}\) denote the number of \(M_i\) containing the edge \(\{u,v\}\). For any three distinct messages \(u,v,w\), a matching contains at most one of the three edges between them. Thus the three nonseparating coordinates are counted without overlap and
\[
m_{uv}+m_{uw}+m_{vw}=3. \tag{1}
\]
Every vertex appears once per perfect matching, giving \(\sum_{w\ne u}m_{uw}=N=2q-1\). Fix \(u\ne v\) and sum (1) over all \(w\notin\{u,v\}\):
\[
(2q-2)m_{uv}+(N-m_{uv})+(N-m_{uv})=3(2q-2).
\]
Since \(N=2q-1\), this reduces to \((2q-4)m_{uv}=2q-4\). For \(q\ge3\), therefore \(m_{uv}=1\). Each edge occurs in exactly one matching, so the matchings form a one-factorization. The characterization needs no linearity or extra regularity assumption.

**Step 3: Converse and existence.** Given any one-factorization, assign independently at each factor its \(q\) edges bijectively to the \(q\) alphabet symbols, and give each vertex the symbol of its edge at that coordinate. Every pair of distinct vertices is together in exactly one factor, hence their words are distinct. For a triple \(u,v,w\), the three edges \(uv,uw,vw\) occur in three *different* matchings, and every other coordinate separates the triple. Its multiplicity is exactly \(N-3=2q-4\). Such factorizations exist for every \(q\): on vertices \(\{\infty\}\cup\mathbb Z/(2q-1)\), for each residue \(a\), use the matching with edge \(\{\infty,a\}\) and edges \(\{a+j,a-j\}\) for \(1\le j\le q-1\), interpreted modulo \(2q-1\). Every unordered edge occurs exactly once because \(2\) is invertible modulo the odd modulus.

**Step 4: Ternary census.** For \(q=3\), there are fifteen perfect matchings of the labeled complete graph \(K_6\). Direct exhaustive enumeration of the \(\binom{15}{5}=3003\) unordered five-matchings families yields exactly six one-factorizations. A separate enumeration of all \(6!\) vertex permutations shows that these six form one orbit. Every labeled one-factorization gives \(5!\) placements of its factors and \((3!)^5\) independent bijections from its pairs to the three fixed alphabet symbols, counted with six temporarily labeled messages. Each unordered codebook has exactly \(6!\) distinct message-labelings because its words are pairwise different. The exact count is therefore
\[
\frac{6\cdot5!\cdot(3!)^5}{6!}=7776.
\]
This count has no hidden symmetry division: factor order, symbol names, and message-labeling are treated separately. The full equality characterization implies this is a complete census, not just a family of constructions.

## Verification
The included standalone standard-library script `verify.py` enumerates all fifteen labeled perfect matchings of \(K_6\), all 3003 five-factor candidates, and all six resulting factorizations; checks every triple against the multiplicity-two condition; verifies one orbit under all 720 message permutations; and reconstructs the count 7776. It also checks explicit round-robin one-factorizations and all their codeword triples at \(q=3,4,5,6,7,8\). The verifier's full output is stored in `verification_output.txt` and is exactly replayable with `python verify.py`. These finite checks support the census and examples; **the all-\(q\) theorem follows from Steps 1–3 and not from numerical sampling**.

## Relationship to prior work
Bishnoi, Kielak, Kovács, Nagy, Somlai, Vizer, and Zheng introduced the generalized requirement of at least \(m\) separating coordinates for every triple and directly reported the exact numerical result \(T(5,2)=6\) (Section V.A of their 2025 preprint, subsequently published). Their reported maximum code size does not identify all six-word equality cases, give their labeled count, or state the all-alphabet one-factorization rigidity proved here. Older trifferent-code literature, including Kurz's short-length computations, emphasizes maximum cardinalities for the classical single-separation problem and does not directly supply this repeated-separation equality classification. The connection to classical one-factorizations gives a graph-theoretic description of **all** optimizers at this boundary, rather than only one exhibited code.

## Limitations
This theorem fixes both the number of codewords \(2q\) and the length \(2q-1\). It does not determine the maximum number of codewords for a prescribed general separation multiplicity, does not classify one-factorizations for arbitrary \(q\), and does not claim unique equivalence classes when \(q>3\). The exact ternary census relies on a complete finite search whose small program is provided. An equivalent equality-case theorem could conceivably be implicit in older perfect-hash-family or one-factorization literature; searches and the inspected motivating primary source have not established such prior coverage. No independent mathematical audit or priority certification is claimed.

## References
1. A. Bishnoi, B. Kielak, B. Kovács, Z. L. Nagy, G. Somlai, M. Vizer, and Z. Zheng, *The generalized trifference problem*, arXiv:2505.07706, first posted May 12, 2025. Published version DOI: 10.1109/TIT.2026.3665439. Section V.A gives \(T(5,2)=6\).
2. S. Kurz, *Trifferent codes with small lengths*, 2023 open-access preprint, https://epub.uni-bayreuth.de/id/eprint/7256/; later published in *Examples and Counterexamples* (2024). Background for the classical trifference maximum-size problem, not the present repeated-separation optimizer classification.
