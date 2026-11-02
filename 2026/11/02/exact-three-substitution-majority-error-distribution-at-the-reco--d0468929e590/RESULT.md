# Exact three-substitution majority-error distribution at the reconstruction threshold

## Finding

Fix an integer \(k\ge7\). Transmit a binary word of length \(k\) and observe an **unordered set of distinct** received words, each obtained by changing **exactly three** coordinates. Put
\[
 b=\binom{k-2}{2},\qquad N=2b+1,\qquad H=b+1,\qquad M=\binom{k}{3}.
\]
Here \(N\) is the already known optimal worst-case reconstruction threshold for three substitutions; we investigate the *pointwise majority decoder*, not optimal decoding. For \(0\le r\le k\), write \(E_r(k)\) for the number of \(N\)-element observation sets on which this decoder makes **exactly** \(r\) erroneous coordinate decisions. The result is independent of the transmitted word.

Define \(\binom ab=0\) whenever \(b<0\) or \(b>a\), and define the two finite sums
\[
 T_1(k)=\sum_{d=H}^{\binom{k-1}{2}}\binom{\binom{k-1}{2}}d\binom{\binom{k-1}{3}}{N-d},
\]
\[
 T_2(k)=\sum_{x=1}^{k-2}\binom{k-2}x
 \sum_{i=0}^{x-1}\sum_{j=0}^{x-1}
 \binom bi\binom bj\binom{\binom{k-2}{3}}{1-x+i+j}.
\]
Let \(F_1=T_1(k)\), \(F_2=T_2(k)\), and introduce the following **complete exceptional values**:
\[
\begin{array}{c|cc}
 k&F_3&F_4\\\hline
 7&951125&4531\\
 8&16003008&0\\
 \ge9&0&0
\end{array}
\]
For all \(j\ge5\), set \(F_j=0\). Thus \(F_j\) counts observation sets on which each of \(j\) **specified distinct** coordinates is decoded incorrectly. Put \(I_0=\binom M N\) and \(I_j=\binom kj F_j\) for \(1\le j\le4\). The **entire majority-error distribution** is
\[
 \boxed{E_r(k)=\sum_{j=r}^{4}(-1)^{j-r}\binom jr I_j,
 \qquad 0\le r\le4,}
\]
with \(E_r(k)=0\) for \(r>4\). For \(k\ge9\), only \(r=0,1,2\) occur, and one has the particularly short formulas
\[
 \boxed{E_2=\binom k2T_2,\quad
 E_1=kT_1-2\binom k2T_2,\quad
 E_0=\binom M N-kT_1+\binom k2T_2.}
\]
Every bound on the largest possible majority-error count is sharp: it is \(4\) when \(k=7\), \(3\) when \(k=8\), and \(2\) for every \(k\ge9\).

In particular, the numbers of sets on which majority voting fails (at least one erroneous coordinate) are \(1819700190\) at \(k=7\), \(649938525134752\) at \(k=8\), and \(5345935937652753076536\) at \(k=9\). **The first of these numbers was already tabulated in the motivating paper and is not claimed as new.** For a uniformly random \(N\)-subset of the exact-three output sphere,
\[
 \boxed{\log\Pr(\text{majority failure})
 =-\tfrac12 k^2\log k+O(k^2)\qquad (k\to\infty),}
\]
where logarithms are natural.

## Assumptions and scope

The alphabet is binary, errors change exactly three **different** positions per read, and all \(N\) observations are distinct. Majority voting is coordinatewise; since \(N\) is odd, no tie is possible. No probabilistic independence of individual read errors is assumed. The failure probability statement alone uses the uniform distribution over distinct \(N\)-element observation sets. Results do not concern four or more substitutions, nonbinary alphabets, repeated observations, or the proposed weighted-majority algorithm.

## Proof

XOR translation lets the transmitted word be the all-zero word. Each received word is then the incidence vector of a three-element subset of \([k]\), so an observation set corresponds bijectively to a simple three-uniform hypergraph with \(k\) labeled vertices and \(N\) edges. At vertex \(v\), majority voting is erroneous exactly if its degree is strictly greater than \(N/2\), equivalently at least \(H=b+1\).

**One designated bad coordinate.** There are \(A=\binom{k-1}{2}\) triples containing that coordinate and \(B=\binom{k-1}{3}\) avoiding it. Selecting \(d\ge H\) containing triples and \(N-d\) avoiding ones gives precisely \(T_1(k)\).

**Two designated bad coordinates.** Classify triples as containing both (\(k-2\) choices), only the first (\(b\)), only the second (\(b\)), or neither (\(c=\binom{k-2}{3}\)). Suppose \(x\) containing-both triples are chosen. If \(i\) and \(j\) are the numbers of omitted first-only and second-only triples, the two degree constraints are exactly \(0\le i,j\le x-1\). The total-edge constraint forces exactly \(1-x+i+j\) selected neither-containing triples. Summing the four binomial factors gives \(T_2(k)\). In particular \(x\ge1\).

**No triple of errors for \(k\ge9\).** For any three designated vertices, the largest possible total incidence among \(N\) selected triples is obtained by taking first the unique triple incident to all three, then all \(3(k-3)\) triples incident to exactly two, and filling the rest with triples incident to exactly one. This upper bound is \(N+3k-7\). Three erroneous vertices would require at least \(3H\) incidences. Their difference is
\[
 3H-(N+3k-7)=\frac{(k-3)(k-8)}2>0
 \quad(k\ge9).
\]
At \(k=8\), four erroneous vertices would require \(64\) incidences; among \(31\) chosen triples the maximum possible total incidence on four fixed vertices is \(4\cdot3+24\cdot2+3=63\). At \(k=7\), five erroneous vertices require at least \(55\) incidences; among \(21\) chosen triples the maximum is \(10\cdot3+11\cdot2=52\). These prove the announced upper bounds.

**Exceptional triple and quadruple intersections.** At \(k=8\), three erroneous coordinates require \(3H=48\) total incidences; the incidence maximum is also \(48\). The selected hypergraph must therefore contain all \(16\) triples meeting a fixed three-set in at least two positions, plus exactly five of the ten triples containing *only* each prescribed vertex. The choices are independent, giving \(F_3(8)=\binom{10}{5}^3=16003008\).

For \(k=7\), with \(r\in\{3,4\}\), let \(m_S=\binom{7-r}{3-|S|}\) for \(S\subseteq[r]\), again with the zero convention. The exact finite product
\[
 P_r(z;u_1,\ldots,u_r)
 =\prod_{S\subseteq[r]}
   \left(1+z\prod_{j\in S}u_j\right)^{m_S}
\]
counts edge selections by cardinality and the degrees on \(r\) designated vertices. Consequently
\[
 F_r(7)=\sum_{d_1=11}^{15}\cdots\sum_{d_r=11}^{15}
 [z^{21}u_1^{d_1}\cdots u_r^{d_r}]P_r
\quad (r=3,4).
\]
Exact integer expansion gives \(F_3(7)=951125\) and \(F_4(7)=4531\). These evaluations are independently reproduced using both selected-edge and omitted-edge dynamic coefficient expansions in `verify_t3.py`, with no numerical approximation or heuristic pruning. All finite sums in this proof specify exact, terminating integer computations.

**Sharpness.** For \(k=7\), omit the 14 triples consisting of \(\{4,5,6\}\), all \(\{v,a,b\}\) for \(0\le v\le3\) and \(\{a,b\}\subset\{4,5,6\}\), and \(\{0,1,4\}\). Among the 21 remaining triples, vertices \(0,1,2,3\) have degrees \(11,11,12,12\), all erroneous. The \(k=8\) construction above attains three errors. For every \(k\ge9\), select all \(2b\) triples meeting a fixed pair of vertices in exactly one vertex, together with one of the \(k-2\) triples containing both; both coordinates then have degree \(b+1\). Thus the error-count ceilings are all attained.

**Distribution.** Let \(I_j\) count incidences of observation sets with \(j\)-subsets of their incorrectly decoded coordinate sets. Symmetry gives \(I_j=\binom kj F_j\). An observation set with exactly \(r\) bad coordinates contributes \(\binom rj\) to \(I_j\). Binomial inversion yields the displayed formula for \(E_r\).

**Asymptotics.** For any fixed coordinate, write \(P_1=F_1/\binom MN\) for its probability of a majority error. The union bound and containment give \(P_1\le P_{\mathrm{fail}}\le kP_1\). The \(d=H\) summand in \(T_1\) is a lower bound, while \(T_1\) has at most \(A+1\) summands, each bounded by \(2^A\binom B{N-H}\) for all sufficiently large \(k\) (since the binomial terms increase through the relevant range). The standard elementary binomial estimates for \(s=o(Q)\), \(\log\binom Qs=s\log(Q/s)+O(s)\), applied to \(B\asymp k^3\), \(N-H\sim k^2/2\), and \(M\asymp k^3\), \(N\sim k^2\), yield
\[
 \log F_1=\tfrac12 k^2\log k+O(k^2),\qquad
 \log\binom MN=k^2\log k+O(k^2).
\]
Together with the union bounds this proves the claimed probability exponent.

## Verification

Run `python3 verify_t3.py` from the extracted package. It uses only the Python standard library. The program evaluates the closed finite sums for \(k=7,\ldots,11\), compares them against **both** a selected-edge and a complementary omitted-edge expansion for each one- and two-vertex intersection, independently checks the exceptional higher intersections, applies binomial inversion, tests explicit sharpness witnesses, and performs 4,500 seeded direct hypergraph samples. Its exact output is supplied in `verification_output.txt`. The reference first-boundary majority-failure count for \(k=7\) matches Table III of the cited 2026 source. Direct random samples are supporting tests only; the proof is the combinatorial reduction and finite exact identities above.

## Relationship to prior work

Papadopoulou, Yehezkeally, Rameshwar and Wachter-Zeh establish \(N=2\binom{k-2}{t-1}+1\) as the optimal number of distinct exact-\(t\) views and determine the number of majority-vote failures for \(t=2\). Their Table III additionally gives an exhaustive **one-point** count for \(k=7,t=3,N=21\), reproduced here as a cross-check. Their Section III-C explicitly identifies counts for \(t>2\) as an open direction. The present result obtains the complete majority-Hamming-error *distribution* for \(t=3\), for every \(k\ge7\), including the first unreported threshold count at \(k=8\), all larger lengths via finite binomial sums, sharp error-number cutoffs and a super-exponential probability exponent. The earlier 2024 analysis of expected views describes numerical and recursive estimates rather than this complete distribution.

## Limitations

This is an exact result for fixed weight three at a specific observation count, not the complete observation-count profile or a guarantee for weighted majority voting. The exceptional finite coefficients are evaluated by reproducible integer coefficient arithmetic rather than a short hand-expanded decimal derivation. Earlier or unindexed hypergraph enumeration formulas might imply the result in different notation. Independent external mathematical and priority validation have not been performed.

## References

1. V. Papadopoulou, Y. Yehezkeally, V. A. Rameshwar and A. Wachter-Zeh, *When Majority-Vote Fails: Sequence Reconstruction under Fixed-Weight Substitutions*, arXiv:2610.30001v1, initially submitted 2026-10-21, https://arxiv.org/abs/2610.30001. In particular Section III-C and Table III.
2. V. Papadopoulou, V. A. Rameshwar and A. Wachter-Zeh, *On the Expected Number of Views Required for Fixed-Error Sequence Reconstruction*, 2024 IEEE Information Theory Workshop, DOI:10.1109/ITW61385.2024.10806938; abstract and conference record at https://portal.fis.tum.de/en/publications/on-the-expected-number-of-views-required-for-fixed-error-sequence/.
