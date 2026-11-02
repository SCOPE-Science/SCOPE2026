# Exact enumeration of complement-pair-free binary cyclic words at factor length four

## Finding

Let \(A_n\) count marked binary circular words of length \(n\ge 1\) having no pair of complementary length-four cyclic factors. Define \(T_r(n)\) for integer \(r\ge2\) by
\[
T_r(n)=\begin{cases}1&1\le n<r,\\r+1&n=r,\\T_r(n-1)+T_r(n-r)&n>r.\end{cases}
\]
Then, for every \(n\ge1\),
\[
\boxed{A_n=4T_7(n)+2T_3(n)-4.}
\]
Equivalently, the ordinary generating function is
\[
\sum_{n\ge1}A_nz^n=
\frac{4z(1+7z^6)}{1-z-z^7}+
\frac{2z(1+3z^2)}{1-z-z^3}-\frac{4z}{1-z}.
\]
The number of these words containing both \(00\) and \(11\) as cyclic factors is exactly \(4(T_7(n)-1)\). Consequently, such words first occur at length \(7\), when exactly \(28\) marked words, forming four rotation orbits, contain both doublets. The exponential growth constant of \(A_n\) is the positive root \(\rho_3>1\) of \(\rho_3^3-\rho_3^2-1=0\); more precisely \(A_n=2\rho_3^n+O(\rho_7^n)\), where \(\rho_7>1\) satisfies \(\rho_7^7-\rho_7^6-1=0\).

## Assumptions and scope

A *marked circular word* is a function from \(\mathbb Z/n\mathbb Z\) to \(\{0,1\}\). Cyclic shifts are counted as different words when their indexed sequences differ; no quotient by rotation or complementation is taken. Even when \(n<4\), a length-four factor is formed using periodic extension, so the definition includes short circular words without exceptional conventions. The complement \(\overline{u}\) exchanges zero and one in every coordinate. A word is admissible exactly if there is no length-four factor \(u\) for which both \(u\) and \(\overline{u}\) occur among its \(n\) cyclic starting positions.

The result concerns the complete unrestricted binary cyclic avoidance class; it imposes no critical-exponent, balance, or run constraint. The classification below uses the order-three binary de Bruijn digraph, with eight three-bit vertices and sixteen four-bit edges, and is valid uniformly in \(n\).

## Proof

**Step 1 — a finite collection of six covering graphs.** Identify a four-bit factor with the integer \(e\in\{0,\ldots,15\}\). It represents the directed edge \(\lfloor e/2\rfloor\to(e\bmod8)\) in the order-three binary de Bruijn graph. Bitwise complementation sends \(e\) to \(15-e\), giving eight disjoint pairs. Let \(F_i\) be the directed edge sets below (with each entry written as the decimal code of its four-bit edge):

```
F0: 0,1,2,5,6,8,11,12
F1: 0,1,3,4,6,8,10,13
F2: 2,5,7,9,11,12,14,15
F3: 3,4,7,9,10,13,14,15
F4: 0,1,2,4,8,9
F5: 6,7,11,13,14,15
```

No \(F_i\) contains complementary edges. Conversely, any admissible cyclic word determines a closed walk in some graph which chooses precisely one edge from each of the eight complementary edge pairs: extend its encountered factors to any such orientation. There are exactly \(2^8=256\) oriented graphs. A closed walk is contained in one strongly connected component, including a singleton component only if it carries a loop. The finite enumeration lemma says that in every one of those 256 graphs, the internal edges of each cycle-carrying strongly connected component are contained in at least one of the six \(F_i\). Hence every admissible cyclic word belongs to at least one of these six subshifts.

The lemma is independently replayable with `python3 verify.py`. Its core finite algorithm is: iterate the eight choices of complementary orientation as eight bits; build the eight-vertex adjacency lists; compute mutual reachability for all eight vertices; determine every cycle-carrying strongly connected component and its internal edges; then check its edge-set inclusion in one of the displayed six lists. The script exhausts all 256 cases (324 cycle-carrying components), so this is a finite lemma for *all* word lengths rather than a bounded-length experiment.

**Step 2 — intersections of the six graph languages.** For any two distinct \(F_i\) and \(F_j\), the intersection digraph has no directed cycle other than possibly the loops corresponding to \(0000\) and \(1111\). This is verified for all \(\binom 62=15\) intersections by the same eight-vertex strongly connected-component procedure. Thus two graph languages can share only the two constant cyclic words. The all-zero word belongs to exactly \(F_0,F_1,F_4\), while the all-one word belongs to exactly \(F_2,F_3,F_5\). Summing six counts therefore overcounts the two constant words twice each; the correction is \(-4\).

**Step 3 — exact transfer determinants.** Let \(M_i\) be the \(8\times8\) adjacency matrix of \(F_i\), allowing an entry for every listed edge. The finite exact matrix identities are
\[
\det(I-zM_i)=\begin{cases}1-z-z^7,&0\le i\le3,\\1-z-z^3,&4\le i\le5.\end{cases}
\]
Both equalities are checked coefficient by coefficient, including all trailing zero coefficients, by Newton's identities applied to the eight integer power traces in `verify.py`. A marked circular word of length \(n\) compatible with \(F_i\) is a unique closed walk of length \(n\) with a distinguished initial position, so its count is \(\mathrm{tr}(M_i^n)\). The formal identity
\[
-\,z\frac{d}{dz}\log\det(I-zM_i)=\sum_{n\ge1}\mathrm{tr}(M_i^n)z^n
\]
then shows that these traces equal \(T_7(n)\) or \(T_3(n)\), respectively: for \(r=3,7\),
\[
-\,z\frac{d}{dz}\log(1-z-z^r)
=\frac{z(1+rz^{r-1})}{1-z-z^r}.
\]
Their coefficients satisfy precisely the displayed initial values and recurrence. Adding the four first-family traces, the two second-family traces, and subtracting the four constant-word overcounts proves the formula and generating function.

**Step 4 — doublets and growth.** Each of the four first-family graphs has one singleton constant loop and one oriented seven-edge cycle through that loop vertex. Every nonconstant closed walk in these graphs traverses the seven-edge cycle and therefore encounters both \(00\) and \(11\). Each of the last two families omits one of those two doublets. Since the six languages overlap only on constant words, the count with both doublets is exactly \(4(T_7(n)-1)\). The recurrence gives \(T_7(n)=1\) for \(n<7\) and \(T_7(7)=8\), giving \(28\) at \(n=7\); every such length-seven word is a shift of a distinct first-family seven-cycle. Each transfer graph is primitive on its recurrent class (it has a loop and a full cycle), so the Perron eigenvalue is the unique largest-modulus root of the corresponding renewal polynomial. The greater of the two Perron eigenvalues is \(\rho_3\), giving the claimed asymptotic; the remaining roots contribute terms bounded by \(O(\rho_7^n)\).

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It reconstructs every one of the 256 orientation graphs, checks all 324 cycle-carrying strongly connected components, checks all 15 pairwise intersections, and independently recomputes all six determinant identities with exact integer arithmetic. An independent direct enumeration of all \(2^n\) marked binary words for each \(4\le n\le16\) (131,056 total source instances) agrees with the formula and the doublet count; additional transfer-trace comparisons cover \(1\le n\le30\). The verified values of \(A_n\) for \(4\le n\le16\) are
\[
10,12,20,58,74,98,132,178,244,340,506,738,1066.
\]
To replay, place `verify.py` alongside this document and execute `python3 verify.py`, which prints `VERIFY_OK` and the counts. The finite machine certificate is used to establish finite graph identities and inclusion for *all lengths*. The brute-force word enumeration is an auxiliary check only, not an infinite proof.

## Relationship to prior work

Currie, Dvořáková, Ochem, Opočenská, Rampersad and Shallit study complement avoidance for infinite binary words, repetition thresholds and finite-word complexity conditions [1]. Their full accessible preprint, including Sections 2 and 5, concerns critical exponents, special morphic families and the existence of exponentially many words under additional power restrictions; the exact marked-circle length-four count and six-graph renewal decomposition above are not given there. The definition of forbidden complementary factors is shared, but the counting question and its exact formula are distinct.

Munarini and Zagaglia Salvi count circular binary strings avoiding both length-three zigzags \(010\) and \(101\) [2]; that excludes a different factor set. Hadjicostas and Zhang study single-pattern cyclic avoidance with multiset generalizations [3]; their accessible abstract discusses a conjectural framework for multiple forbidden patterns, not an explicit result for this complementary-factor family. General finite-state transfer-matrix counting is standard; the specific six-family covering lemma, overlap correction and derived exact enumeration are the substantive new assertions here.

## Limitations

This result counts *marked* circular words, not necklaces modulo rotation. No general formula for arbitrary forbidden-factor length or nonbinary alphabets is asserted. The 256-case finite classification and determinant checks require the accompanying executable certificate for straightforward independent replay; only the fixed graph identity is machine-checked, and the theorem is otherwise an elementary deduction. The primary complement-avoidance article and the accessible 2003 zigzag text were inspected in detail; the 2018 single-pattern article was available as an abstract rather than complete primary text, leaving an unassessed possibility of equivalent coverage in its general multiple-pattern discussion or an unindexed finite-state enumeration. The literature comparison is not a proof of global priority. No independent scientific validation has been performed.

## References

[1] J. D. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598, version 1 publicly dated 2022-09-20; Electronic Journal of Combinatorics 32(4) (2025), #P4.24. https://arxiv.org/abs/2209.09598 ; https://doi.org/10.37236/11555

[2] E. Munarini and N. Zagaglia Salvi, *Circular Binary Strings without Zigzags*, Integers 3 (2003), #A19. https://www.researchgate.net/publication/228396896_Circular_binary_strings_without_zigzags

[3] P. Hadjicostas and L. Zhang, *On Cyclic Strings Avoiding a Pattern*, Discrete Mathematics 341 (2018), 1662–1674. https://doi.org/10.1016/j.disc.2018.03.007 ; https://oasis.library.unlv.edu/math_fac_articles/54/
