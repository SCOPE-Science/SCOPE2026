# Exact one-step reachability, inversion, and density spectrum of the cyclic traffic automaton

## Finding
For every integer \(n\ge1\), let \(F_n\) be the synchronous elementary cellular automaton Rule 184 acting on the binary ring \(\{0,1\}^n\). The complete one-step image is the circular pattern-avoidance language
\[
\operatorname{Im} F_n=\{y\in\{0,1\}^n:\text{no cyclic length-four window of }y\text{ is }1100\}.
\]
More strongly, the reflected traffic rule \(G_n\) (Rule 226) satisfies \(F_n(G_n(y))=y\) **if and only if** \(y\) has no cyclic occurrence of \(1100\). Thus an explicit radius-one predecessor selector exists on the entire image, not merely a decision procedure.

Write \(R_{n,k}\) for the number of attainable length-\(n\) images containing exactly \(k\) ones. With binomial coefficients interpreted as zero outside their natural integer range,
\[
R_{n,k}=\sum_{j=0}^{\lfloor n/4\rfloor}(-1)^j
 \frac{n}{n-3j}\binom{n-3j}{j}\binom{n-4j}{k-2j},\qquad n\ge1,\quad 0\le k\le n.
\]
The complete density-refined rational generating function is
\[
\sum_{n\ge1}\sum_{k=0}^{n}R_{n,k}z^nu^k
 =\frac{(1+u)z-4u^2z^4}{1-(1+u)z+u^2z^4}.
\]
In particular, \(R_n=\sum_kR_{n,k}\) starts \(2,4,8,12,22,40,72,132,242,444,816,1500\), satisfies \(R_n=2R_{n-1}-R_{n-4}\) for \(n\ge5\), and has the exact form
\[
R_n=1+\lambda^n+\alpha^n+\overline\alpha^n,
\]
where \(\lambda\) is the unique real root greater than one of \(x^3-x^2-x-1=0\), and \(\alpha,\overline\alpha\) are its conjugate roots. Consequently, \(R_n\sim\lambda^n\) and \(R_n/2^n\sim(\lambda/2)^n\), where \(\lambda\approx1.8392867552\).

## Assumptions and scope
Positions are indexed in \(\mathbb Z/n\mathbb Z\); the rules use simultaneous updates and wrap-around even when \(n<4\). For binary arguments \(a,b,c\), set
\[
f(a,b,c)=(b\wedge c)\vee(a\wedge\neg b),\qquad
 g(a,b,c)=(a\wedge b)\vee(c\wedge\neg b).
\]
Then \(F_n(x)_i=f(x_{i-1},x_i,x_{i+1})\) and \(G_n(y)_i=g(y_{i-1},y_i,y_{i+1})\). A cyclic length-four window beginning at \(i\) is \(y_i y_{i+1}y_{i+2}y_{i+3}\); repeated positions count for short rings. All enumerations count **indexed** ring configurations, rather than rotation classes. The variable \(u\) records the exact number of occupied cells; it is not a probability.

## Proof
**1. Necessity, by the local image language.** For an arbitrary six-bit input window \(a_0\cdots a_5\), the consecutive four output bits are \(f(a_0,a_1,a_2),f(a_1,a_2,a_3),f(a_2,a_3,a_4),f(a_3,a_4,a_5)\). Direct application of the displayed Boolean rule to all \(64\) inputs gives exactly the fifteen words in \(\{0,1\}^4\setminus\{1100\}\). This is a finite, complete truth-table lemma (reproducibly checked in the accompanying script). Every cyclic four-output window arises from such a six-input window, with repeated sites allowed, so no image contains \(1100\).

**2. Sufficiency and canonical inverse, by a second complete local lemma.** At any position of the composite \(F_nG_n\), the output depends on the five-bit input context \(abcde\). Exhausting the \(32\) possible contexts in the two displayed Boolean formulas gives the exact discrepancy list
\[
\{abcde:f(g(a,b,c),g(b,c,d),g(c,d,e))\ne c\}
 =\{01100,11000,11001,11100\}.
\]
Every listed context contains \(1100\). Conversely, any occurrence \(1100\) at positions \(i,i+1,i+2,i+3\) causes a discrepancy: the context centered at \(i+1\), with its unknown preceding bit, is either \(01100\) or \(11100\); the context centered at \(i+2\), with its unknown following bit, is either \(11000\) or \(11001\). These statements remain valid with periodic repeated indices. Therefore \(F_nG_n(y)=y\) exactly for cyclic \(1100\)-avoiding configurations. Necessity from Step 1 plus sufficiency here proves the image theorem.

**3. Fixed-density inclusion–exclusion.** The word \(1100\) has no nonempty proper prefix equal to a suffix, so two *different* occurrences cannot overlap on the periodic circle. For \(n\ge4\), choose \(j\) possible starting positions for marked, nonoverlapping blocks of four sites; a standard cyclic spacing bijection counts their subsets as
\[
C_{n,j}=\frac{n}{n-3j}\binom{n-3j}{j}\qquad (0\le4j\le n).
\]
For clarity, distinguish one marked block, choose its initial site in \(n\) ways, and distribute the \(n-4j\) unused sites as \(j\) nonnegative gaps between successive blocks. This gives \(n\binom{n-3j-1}{j-1}/j\), equal to the stated \(C_{n,j}\). The empty selection has \(C_{n,0}=1\). Each block fixes two ones and two zeros, leaving \(n-4j\) free sites, of which \(k-2j\) must be ones. Inclusion–exclusion over occurrences gives precisely the formula for \(R_{n,k}\). For \(n<4\), there are no cyclic \(1100\) blocks, and the same formula reduces to \(\binom nk\).

**4. Bivariate transfer matrix.** Track the longest suffix that is a proper prefix of the forbidden pattern, using states \(\varepsilon,1,11,110\). An appended zero has weight \(1\) and an appended one has weight \(u\); discard transitions that complete \(1100\). In the listed order the transition matrix is
\[
A(u)=\begin{pmatrix}
1&u&0&0\\
1&0&u&0\\
0&0&u&1\\
0&u&0&0
\end{pmatrix}.
\]
Every cyclic word avoiding \(1100\) has a *unique* periodic path through this deterministic suffix machine: the state at a cut is the longest relevant suffix of its bi-infinite periodic past, determined by at most the preceding three bits. Conversely any closed path spells a cyclic word without the forbidden block. Consequently \(\sum_kR_{n,k}u^k=\operatorname{tr}(A(u)^n)\) for all \(n\ge1\). A direct determinant calculation gives \(\det(I-zA(u))=1-(1+u)z+u^2z^4\). The formal-matrix identity
\[
\sum_{n\ge1}\operatorname{tr}(A(u)^n)z^n
 =-z\frac{d}{dz}\log\det(I-zA(u))
\]
gives the stated rational generating function. Specializing \(u=1\), the denominator factors as \((1-z)(1-z-z^2-z^3)\), and the claims about recurrence, eigenvalues, and asymptotic follow. The complex roots have modulus less than one, so the leading term has coefficient one.

## Verification
The accompanying standalone standard-library program `verify.py` checks both complete local truth tables, exhaustively compares images and the forbidden-language criterion for all ring lengths \(1\) through \(13\), verifies the Rule-226 predecessor equivalence for every binary ring configuration in those lengths, and separately compares the fixed-weight inclusion–exclusion with transfer-matrix trace coefficients through length \(18\). It also checks the initial totals and linear recurrence. Run `python3 verify.py` beside this file; the expected terminal line is `VERIFY_OK`. All-length conclusions follow from Steps 1–4; finite tests are corroboration, not a substitute for proof.

## Relationship to prior work
Rule 184's number conservation, traffic interpretation and density dynamics are classical, notably in Fukś (1997) and Boccara–Fukś (1997/1998); the latter explicitly pairs Rule 184 with its reflected Rule 226. Their examined objectives are conservation and evolution rather than an exact periodic one-step image language together with a pointwise predecessor selector and fixed-density image spectrum. Kurka's treatment of Rule 184 discusses signal subshifts and limiting dynamics, a different dynamical object than \(\operatorname{Im}F_n\). The automata and inclusion–exclusion tools here are classical; novelty, if established, resides in the joint exact characterization and its density-sensitive consequences, **not** in the generic algorithms or identities. A comprehensive historical-priority claim is not made.

## Limitations
The result concerns deterministic synchronous one-step updates on fully periodic finite binary rings. It does not classify individual predecessor fiber sizes, multi-step images, asynchronous update schedules, boundaries other than cyclic, or other traffic rules. The asymptotic concerns a count of indexed reachable configurations, not a stochastic mixing rate. The proof is self-contained but has not undergone independent review; older obscure classifications of Rule 184 could affect historical priority.

## References
- H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules* (1997), arXiv:comp-gas/9703001, https://arxiv.org/abs/comp-gas/9703001. First arXiv posting 1997-03-07.
- N. Boccara and H. Fukś, *Cellular Automaton Rules Conserving the Number of Active Sites*, arXiv:adap-org/9712003 (initial posting 1997-12-12), https://arxiv.org/abs/adap-org/9712003; published in J. Phys. A 31 (1998), 6007–6018.
- P. Kůrka, *Topological Dynamics of One-Dimensional Cellular Automata*, https://doi.org/10.1007/978-0-387-30440-3_556 (Rule 184 signal examples).
