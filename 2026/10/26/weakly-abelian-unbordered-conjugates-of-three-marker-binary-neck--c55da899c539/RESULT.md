# Weakly Abelian unbordered conjugates of three-marker binary necklaces

## Finding
Let \(w\) be a directed binary necklace (cyclic rotations identified, reversal **not** identified) containing **exactly three** occurrences of \(1\). Write its cyclic zero-gap triple as \((a,b,c)\in\mathbb Z_{\ge0}^{3}\), so a representative is \(1\,0^{a}1\,0^{b}1\,0^{c}\). Set \(m=a+b+c\) and \(\mu=m/3\). A finite word is *weakly Abelian unbordered* if it has no nonempty proper prefix and nonempty proper suffix with the same proportion of ones; the prefix and suffix lengths need not agree.

The number \(U_{\mathrm{wa}}(w)\) of **distinct** cyclic rotations that are weakly Abelian unbordered is exactly
\[
U_{\mathrm{wa}}(w)=\sum_{(x,y)\in\{(a,b),(b,c),(c,a)\}}\mathbf 1_{(x-\mu)(y-\mu)<0}.
\]
Equivalently, the two adjacent cyclic gap lengths at a rotation boundary must strictly straddle the mean zero gap; exactly one orientation of that boundary gives an eligible rotation. Hence \(U_{\mathrm{wa}}(w)\in\{0,1,2\}\). The value is zero precisely for equal gaps, one precisely when the three nonnegative gaps are distinct and form an arithmetic progression, and two in every other case.

For every \(m\ge0\), let \(C_j(m)\) count such directed necklaces with \(m\) zeros and \(U_{\mathrm{wa}}=j\), and put \(\delta_m=\mathbf 1_{3\mid m}\). Then the **complete distribution** is
\[
\begin{aligned}
C_0(m)&=\delta_m,\\
C_1(m)&=2\frac m3\,\delta_m,\\
C_2(m)&=\frac{\binom{m+2}{2}+2\delta_m}{3}-\delta_m-2\frac m3\,\delta_m,\\
C_j(m)&=0\quad(j\notin\{0,1,2\}).
\end{aligned}
\]
Here \(m\delta_m/3\) is integral. In particular, every necklace with \(m\not\equiv0\pmod3\) has exactly two weakly Abelian unbordered rotations; the same is true for all but a vanishing fraction of the necklaces as \(m\to\infty\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); three ones and an arbitrary nonnegative number of zeros are allowed. A necklace is directed/oriented, so only rotation is factored out. Distinct rotations are counted as distinct linear words, but repetitions of the same periodic linear word are counted once. Prefix/suffix frequency means the count of ones divided by the corresponding positive length, and both prefix and suffix must be shorter than the entire linear word. This differs from the usual Abelian border, which requires prefixes and suffixes of *equal* length.

## Proof
**1. A sharp three-marker linear criterion.** Consider
\[
v=1\,0^a1\,0^b1\,0^c,\qquad a,b\ge0,\ c\ge1,\quad m=a+b+c.
\]
We claim
\[
 v\text{ is weakly Abelian unbordered}\quad\Longleftrightarrow\quad 3a<m<3c.
\tag{1}
\]
Let \(n=m+3\), let \(s_i\) count ones in the prefix of length \(i\), and define its signed chord height \(H_i=ns_i-3i\). If \(3a<m<3c\), then every interior \(H_i\) is strictly positive. Indeed, \(H_i\) increases at ones, decreases across zero runs, and its only possibly nonpositive interior run-end minima are at the ends of the first and second zero gaps. Their values are \(m-3a\) and \(2m-3(a+b)=3c-m\); the last zero run terminates at \(H_n=0\), while its last *proper* prefix has \(H_{n-1}=3>0\). For every proper prefix \(p\), therefore, the density of ones in \(p\) exceeds \(3/n\). For every nonempty proper suffix \(s\), the density is strictly below \(3/n\), because the complementary nonempty proper prefix lies above that mean. No two such densities can agree.

Conversely, suppose \(3a\ge m\) or \(3c\le m\). We explicitly produce a weak Abelian border. If \(a\ge c\), the prefix of length \(c+1\) and the suffix of length \(c+1\) each contain exactly one one. Otherwise \(a<c\). If \(3a\ge m\), i.e. \(2a\ge b+c\), the prefix of length \(a+1\) contains one one, while the suffix of length \(2a+2\) contains exactly two: the lower inequality \(2a+2\ge b+c+2\) includes the final two ones, and the upper inequality \(2a+2\le a+b+c+2<n\) excludes the first one. Their densities agree. In the remaining case \(a<c\) and \(3c\le m\), i.e. \(2c\le a+b\), the prefix of length \(2c+2\) contains exactly the first two ones because \(a+2\le2c+2\le a+b+2\); the suffix of length \(c+1\) contains exactly the last one. Their densities again agree. All specified factors are nonempty and proper. This proves (1).

**2. All possible cyclic starts.** A weakly Abelian unbordered linear word of length greater than one has different first and last letters; otherwise its first and last one-letter factors are a weak Abelian border. Thus any eligible cyclic rotation starts at a \(10\) boundary (the \(1\) following a positive zero gap) or at a \(01\) boundary (the first zero following a \(1\)). No other start is possible.

Index the cyclic gaps as \(g_0,g_1,g_2\), with \(g_i\) following the \(i\)-th one. At the start on the \(i\)-th one, the linear representation has first zero gap \(g_i\) and last zero gap \(g_{i-1}\), so (1) says the rotation qualifies exactly when \(g_i<\mu<g_{i-1}\). At the first zero after that one, if \(g_i>0\), reverse the resulting linear word. The reversed word has first zero gap \(g_{i-1}\) and last gap \(g_i\); reversal preserves the weak Abelian-border property. Thus this rotation qualifies exactly when \(g_{i-1}<\mu<g_i\). Precisely one of the two boundary starts qualifies if those adjacent gaps lie on opposite sides of \(\mu\); neither qualifies otherwise. This yields the stated sum. In the equal-gap periodic case no start qualifies, so counting distinct rotations causes no exception.

**3. Possible values.** The three signed deviations \(a-\mu,b-\mu,c-\mu\) sum to zero. If all vanish, there is no strict crossing. If exactly one vanishes, the other two are nonzero and opposite; only their connecting cyclic edge crosses, giving one. Such triples are precisely three-term arithmetic progressions with distinct nonnegative terms. If none vanishes, both positive and negative deviations must occur and a three-cycle crosses from one sign to the other exactly twice. This proves the trichotomy.

**4. Enumeration.** Three-marker necklaces correspond bijectively to triples of nonnegative integers summing to \(m\), modulo cyclic permutation. Burnside's lemma gives a total of \((\binom{m+2}{2}+2\delta_m)/3\) classes: nonidentity cyclic permutations fix just the all-equal triple when \(3\mid m\). That same triple is the unique class with \(U_{\mathrm{wa}}=0\) in that case. A class with \(U_{\mathrm{wa}}=1\) has distinct gaps \((q-d,q,q+d)\), where \(m=3q\), \(q\ge1\), and \(1\le d\le q\). Each \(d\) gives two directed cyclic orderings, yielding \(2q\) classes. Subtraction from the total gives \(C_2\). Since the exceptional counts are \(O(m)\) while the total is \(\Theta(m^2)\), the final asymptotic assertion follows.

## Verification
The included standalone Python program `checker.py` computes weak Abelian border status **directly**, by reducing all proper prefix and suffix one-frequencies to exact integer pairs. It independently constructs distinct rotations and compares their count to the gap-crossing formula. It exhaustively checks every necklace with \(0\le m\le28\), tests 500 pseudorandom larger triples, and independently checks the entire distribution for \(0\le m\le149\). It additionally checks the published five-one counterexample to the unrestricted converse of the strict-chord criterion. Execute with `python3 checker.py`; only the Python standard library is needed. The proof, rather than the finite computations, establishes the arbitrary-length statement.

## Relationship to prior work
Charlier, Harju, Puzynina and Zamboni establish the general **sufficient** strict-chord condition for weak Abelian unborderedness (their Lemma 2, arXiv:1501.07464v1, 29 January 2015) and explicitly show that its converse fails in general. The new component here is a proof that the converse **does hold for three-one words of the relevant boundary form**, followed by a complete cyclic gap-mean classification and directed-necklace distribution; no general converse is claimed. Goč, Rampersad, Rigo and Salimov count **ordinary Abelian** unbordered words, for which matched prefix and suffix lengths are mandatory, so their Motzkin-path counts are not counts of weak Abelian unbordered conjugates. Clokie, Gabric and Shallit study **ordinary literal** unbordered conjugates, a different and weaker border relation. The trichotomy and distribution do not follow merely from the distinct literal-unbordered rotation count: e.g. gap triples \((0,1,2)\) and \((0,1,3)\) both have three literal-unbordered rotations but respectively one and two weakly Abelian unbordered rotations.

## Limitations
This theorem is restricted to exactly three ones over the binary alphabet and does not assert an analogous classification for larger marker counts, arbitrary alphabets, linear-word populations, or reversal-identified bracelets. Weakly Abelian unborderedness is strictly stronger than literal unborderedness. The strict-chord converse is *not* valid for arbitrary binary words: the five-one word `1110000011000` is weakly Abelian unbordered but has signed chord heights on both sides of zero, as already documented by Charlier and collaborators. Finite verification does not constitute an infinite proof; mathematical priority is subject to undiscovered equivalences or earlier sources.

## References
1. E. Charlier, T. Harju, S. Puzynina, L. Q. Zamboni, *Abelian bordered factors and periodicity*, arXiv:1501.07464v1 (first public 2015-01-29), Lemma 2 and its nonconverse example; later European Journal of Combinatorics 51 (2016), 407–418, doi:10.1016/j.ejc.2015.07.003.
2. D. Goč, N. Rampersad, M. Rigo, P. Salimov, *On the Number of Abelian Bordered Words (with an Example of Automatic Theorem-Proving)*, International Journal of Foundations of Computer Science 25 (2014), 1097–1110, doi:10.1142/S0129054114400267.
3. T. Clokie, D. Gabric, J. Shallit, *Circularly squarefree words and unbordered conjugates: a new approach*, arXiv:1904.08187v1 (2019); literal borders and cyclic conjugates, not weak Abelian borders.
