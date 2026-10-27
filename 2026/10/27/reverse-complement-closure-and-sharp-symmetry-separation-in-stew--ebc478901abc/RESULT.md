# Reverse-complement closure and sharp symmetry separation in Stewart words

## Finding

Let \(\mathbf s\) be **any** infinite binary Stewart word, produced by successively filling periodic holes with an arbitrary sequence of length-three patterns consisting of one `0`, one `1`, and one `?` (with either binary choice at a possible exceptional permanently unfilled position). Write \(\mathcal L_n(\mathbf s)\) for its set of contiguous factors of length \(n\geq1\). For a binary word \(u\), write \(\overline u\) for bitwise complement, \(u^R\) for reversal, and \(\theta(u)=\overline{u^R}\).

**Theorem.** For every such Stewart word and every \(n\geq1\):

1. Its factor language is **closed under reverse-complement**: \(\theta(\mathcal L_n)=\mathcal L_n\).
2. The number of factors whose bitwise complement also occurs equals the number of factors whose ordinary reversal also occurs. Calling either count \(c(n)\), its exact universal spectrum is
   \[
   (c(1),c(2),c(3),c(4),c(5),c(6),c(7))=(2,4,6,6,6,6,2),\qquad c(n)=0\ \text{for all }n\geq8.
   \]
3. The cutoff is sharp: `0110110` and `1001001` are complementary, palindromic length-seven factors occurring in every Stewart word. No length-eight factor has either its complement or its reversal as another factor.

In particular, a single infinite factorial language is globally invariant under the *composition* of reversal and complementation, while neither constituent symmetry acts within its factors of any length at least eight. This is a statement about factor occurrence in the **same** Stewart word, not between different directive sequences.

## Assumptions and scope

The six admissible patterns are `01?`, `10?`, `0?1`, `1?0`, `?01`, and `?10`. Fix any infinite directive \((p_j)_{j\geq0}\) of these patterns. Number word positions from zero. If \(i=\sum_{j\geq0}d_j3^j\), find the least \(j\) for which \(d_j\) differs from the position \(h_j\in\{0,1,2\}\) of the `?` in \(p_j\), and put \(\mathbf s_i=p_j[d_j]\). If every digit is a hole digit, the exceptional symbol may be assigned either `0` or `1`, as allowed in the original Stewart-word definition. Every other position is well-defined at a finite stage. Factors are ordinary contiguous, noncircular factors; words are not identified under rotation or complement.

The result applies uniformly to all directive sequences, including nonperiodic sequences, and does not impose a repetition-free or balanced-word hypothesis.

## Proof

**1. Every short tail factor occurs.** At the first Toeplitz level, the periodic skeleton is a repetition of \(p_0\) with one hole per three symbols. The subsequence of hole positions forms the Stewart word specified by the tail directive. The tail takes both binary values infinitely often, since the next level itself places both values periodically. For any three consecutive positions of the first-level skeleton, the assigned values contain a `0` and a `1`; the hole is the third position. Cycling the starting residue and using both choices at holes proves that every Stewart word has exactly the four binary length-two factors and exactly the six nonconstant binary length-three factors
\[
\mathcal L_2=\{00,01,10,11\},\qquad
\mathcal L_3=\{001,010,011,100,101,110\}.
\]
(The absence of `000` and `111` follows because every length-three window contains the two fixed symbols at level one.) These facts hold for every tail directive as well.

**2. Complete length-eight factor sets.** Suppose first that the initial pattern is `01?`. For a length-eight window, its initial position modulo three is \(0\), \(1\), or \(2\). Replacing hole positions with consecutive symbols of the tail yields respectively
\[
\begin{aligned}
&\{\mathtt{01a01b01}:\ a,b\in\{0,1\}\},\\
&\{\mathtt{1a01b01c}:\ abc\in\{001,010,011,100,101,110\}\},\\
&\{\mathtt{a01b01c0}:\ abc\in\{001,010,011,100,101,110\}\}.
\end{aligned}
\]
These three displayed sets are pairwise disjoint and have sizes four, six, and six. Each displayed word occurs, because all required pairs and nonconstant triples occur in the tail. Explicitly, their union \(E\) consists of

`00100110`, `00110100`, `00110110`, `01001001`, `01001101`, `01101001`, `01101101`, `10010011`, `10011010`, `10011011`, `10100100`, `10100110`, `10110100`, `11010010`, `11010011`, `11011010`.

A direct comparison within this exhaustive 16-element set gives \(E\cap\overline E=\varnothing\). The first-level patterns `1?0` and `?01` are cyclic shifts of `01?`; because the three possible starting residues are all included, their length-eight factor sets are also \(E\). The other three first-level patterns are bitwise complements of these, and have the factor set \(\overline E\). Hence every Stewart word has exactly one of the two explicitly determined length-eight languages, and no length-eight factor co-occurs with its complement.

**3. A reflection of every finite Toeplitz skeleton.** At depth \(r\geq1\), put
\[
 H_r=\sum_{j=0}^{r-1}h_j3^j,\qquad Q_r=3^r.
\]
Exactly the positions congruent to \(H_r\pmod{Q_r}\) remain unresolved. The partial word of period \(Q_r\) is complemented by the index reflection \(i\mapsto2H_r-i\pmod{Q_r}\): a resolved position has a first base-three digit \(d_j\ne h_j\), and its reflected position has the same first unresolved prefix followed by digit \(2h_j-d_j\pmod3\). The two digits other than \(h_j\) are interchanged, so the assigned `0` and `1` are interchanged. Unresolved positions reflect to unresolved positions. This proves the reflection property for all \(r\) without assuming any periodicity of the directive.

Every finite factor \(u\) has an occurrence entirely assigned at some finite level. Indeed, choose \(r\) with \(Q_r>|u|\). An occurrence then meets at most one unresolved position. If it meets one, shift the occurrence by a suitable multiple of \(Q_r\). At the next level, among the three copies of that hole, one becomes `0` and another becomes `1`; choose the copy matching the original symbol. All already assigned positions are unchanged under this shift. This gives an occurrence completely assigned by level \(r+1\), including when the original occurrence met an exceptional permanently unfilled position.

Reflecting the resolved occurrence in the periodic depth-\(r+1\) skeleton and choosing a sufficiently large nonnegative representative modulo \(Q_{r+1}\) gives an occurrence of \(\overline{u^R}\) in the same infinite word. Thus \(\theta(\mathcal L_n)=\mathcal L_n\) for every \(n\).

**4. Exact small-length spectrum and all-length cutoff.** Every factor of length at most eight is the prefix of some occurring length-eight factor. Consequently the length-\(n\) factor set for \(1\le n\le8\) is obtained by taking all length-\(n\) prefixes of \(E\), or of \(\overline E\). The finite comparisons give the exact complement-overlap counts
\[
 c(1),\ldots,c(8)=2,4,6,6,6,6,2,0.
\]
For \(n>8\), a co-occurring complementary factor pair would have complementary length-eight prefixes, contradicting Step 2. Finally, reverse-complement closure from Step 3 implies, for each occurring \(u\),
\[
 \overline u\in\mathcal L_n\quad\Longleftrightarrow\quad u^R\in\mathcal L_n,
\]
by applying \(\theta\) to one of the two words. Hence the same exact counts and cutoff apply to reversal co-occurrence. The stated length-seven factors are in the prefix sets in both orientations and are complements of one another. This proves all assertions. \(\square\)

## Verification

Run `python3 verify_stewart_symmetry.py` with Python 3 and no third-party dependencies. The verifier independently constructs the length-eight factor sets from the two- and three-letter tail languages, checks both first-level orientations and all eight overlap counts, tests 1,296 independent short directive choices against explicit Toeplitz prefixes, and checks the finite-skeleton reflection identity at 111,150 residue positions. It also checks three independent directive sequences at factor lengths one through one hundred. It prints `STEWART_SYMMETRY_PASS` on success.

The computation is a reproducibility check of the finite classifications and reflection identity; the proof of the unbounded, arbitrary-directive claim is the uniform finite-skeleton argument in Steps 3–4, not extrapolation from a finite prefix.

## Relationship to prior work

Fici and Shallit (2021 preprint; 2022 journal article) introduced the Stewart-word framework in this form, proved that its factor complexity equals \(2n\), classified ordinary palindromic factors, and analyzed common factors between different directives. Their palindromic list ends at length seven, but the absence of two *distinct reversed factors* does not follow merely from the absence of long palindromes. The theorem here concerns a separate action of three word involutions on one fixed word's factor language, gives an exact overlap spectrum, and proves global reverse-complement closure.

Currie and coauthors (2022 preprint; revised 2023) study infinite binary words avoiding co-occurring complementary factors and classify repetition thresholds for classes defined by such avoidance. Their existence and extremal constructions do not identify the universal length-eight complement cutoff for Stewart words or the simultaneous closure under reverse-complement. No prior theorem on general complementary-factor avoidance is represented here as new.

## Limitations

The theorem is specific to the Stewart family and binary complementation. It does not assert that every binary language with complexity \(2n\) has these symmetries, does not count fixed points of the reverse-complement involution, and does not classify factors at arbitrary lengths beyond their symmetry properties. Search and source comparisons do not establish absolute uniqueness; an equivalent result in earlier work on generalized choral sequences or Toeplitz-factor antimorphisms could remain unlocated. The finding is a mathematical proof with finite supporting checks, not an independent audit or formal-machine certification.

## References

1. G. Fici and J. Shallit, *Properties of a Class of Toeplitz Words*, arXiv:2112.12125v1 (first public 2021-12-22); *Theoretical Computer Science* **922** (2022), 1–12, doi:10.1016/j.tcs.2022.04.006. In particular §§1–3, 6, 10–11.
2. J. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, and J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598v1 (first public 2022-09-20; revised 2023), doi:10.37236/11555. In particular §§1–3.
3. J. R. Noche, *On Stewart's Choral Sequence*, *Gibón* **8** (2008), 1–5, as cited by Fici–Shallit; older source not fully inspected for the present comparison.
