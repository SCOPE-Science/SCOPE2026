# Twelve dyadic three-Abelian classes in the period-doubling word

## Finding

Let \(p=p_0p_1\cdots\) be the binary period-doubling fixed point of \(0\mapsto01\), \(1\mapsto00\), with \(p_0=0\). Two words are **3-Abelian equivalent** if they have the same numbers of occurrences of every contiguous word of length at most three. Let \(\mathcal P_p^{(3)}(n)\) denote the number of equivalence classes among length-\(n\) factors of \(p\).

**Theorem.** For every integer \(k\ge4\),
\[
\mathcal P_p^{(3)}(2^k)=12.
\]
More precisely, for \(n=2^k\) the 12 distinct classes correspond bijectively to the following triples: the number \(K\) of ones is either \(\lfloor n/3\rfloor\) or \(\lceil n/3\rceil\); independently, the ordered pair of length-two prefix and suffix belongs to
\[
\mathcal E=\{(01,01),(01,00),(00,01),(10,10),(10,00),(00,10)\}.
\]
Every one of the \(2\cdot6\) combinations occurs, and no other one does. In addition, for *every even* \(n\ge4\), two length-\(n\) factors are 3-Abelian equivalent **if and only if** they have the same number of ones and the same length-two prefix and suffix. Thus all length-three pattern counts are reconstructible from these three simple data.

## Assumptions and scope

All factors are contiguous factors of the one-sided *infinite* word \(p\). Distinct factor classes are counted once regardless of how many positions realize them. A prefix or suffix of length two consists of two binary symbols such as \(01\), not an integer. The theorem applies to \(k\ge4\); the smaller dyadic length \(8\) has only ten classes. The reconstruction lemma applies to even lengths \(n\ge4\), not to arbitrary binary words or odd lengths. Every public mathematical claim is justified below; computations supply checks, not a substitute for induction.

## Proof

**1. Structural identities.** From the substitution one has
\[
p_{2t}=0,\qquad p_{2t+1}=1-p_t \quad(t\ge0).
\]
In particular, \(p\) contains neither \(11\) nor \(0000\). The first exclusion is immediate because every substituted pair begins with zero. The second follows because a run of four zeros across two consecutive substituted pairs would require two adjacent parent symbols equal to one, impossible by the first exclusion. Consequently, a factor of length at least four contains a one, and between successive ones there are exactly one or three zeros: all ones lie at odd positions, and successive zeros of the parent word occur one or two positions apart.

**2. Reconstruct all triple counts at an even length.** Fix an even \(n\ge4\) and a length-\(n\) factor \(u\). Set \(K=|u|_1\), and write \(a,b\) for its prefix and suffix of length two. Let \(L,R\) denote its initial and final numbers of zeros, and let \(A\) be the number of internal gaps of *one* zero between consecutive ones (equivalently, \(|u|_{101}\)); let \(B\) be the number of internal gaps of three zeros. Then
\[
A+B=K-1,\qquad n=K+L+R+A+3B.
\]
Because \(n\) is even, the endpoint's parity is opposite the starting parity. Inspecting the two substitution alignments gives
\[
L+R=1+2\mathbf{1}_{a=00}+2\mathbf{1}_{b=00}.
\]
Indeed, if the factor starts at an even position then \(L=1+2\mathbf{1}_{a=00}\) and \(R=2\mathbf{1}_{b=00}\); if it starts at an odd position then \(L=2\mathbf{1}_{a=00}\) and \(R=1+2\mathbf{1}_{b=00}\). Hence the exact identity
\[
|u|_{101}=2K-1-\frac n2+\mathbf{1}_{a=00}+\mathbf{1}_{b=00}. \tag{1}
\]
All other possible length-three factors are \(000,001,010,100\); a factor containing \(11\) is impossible. To reconstruct their counts, put \(C_{xyz}=|u|_{xyz}\), \(N_{xy}=|u|_{xy}\), and use the elementary identities
\[
\begin{aligned}
N_{01}&=K-\mathbf{1}_{u_0=1},&N_{10}&=K-\mathbf{1}_{u_{n-1}=1},&N_{00}&=n-1-N_{01}-N_{10},\\
C_{010}&=K-\mathbf{1}_{u_0=1}-\mathbf{1}_{u_{n-1}=1},\\
C_{001}&=N_{01}-C_{101}-\mathbf{1}_{a=01},\\
C_{100}&=N_{10}-C_{101}-\mathbf{1}_{b=10},\\
C_{000}&=N_{00}-C_{001}-\mathbf{1}_{b=00}.
\end{aligned}
\]
These identities count transitions and discard precisely the excluded boundary transition. Thus \(K,a,b\) determine every count of patterns of length one, two, or three. Conversely, for words of length at least three, the triple counts determine the prefix and suffix of length two: for a length-two word \(v\), \(|u|_v-\sum_{x\in\{0,1\}}|u|_{vx}=\mathbf{1}_{b=v}\) and \(|u|_v-\sum_x|u|_{xv}=\mathbf{1}_{a=v}\). One-letter counts determine \(K\). This proves the stated equivalence criterion.

**3. The dyadic induction.** Define \(\mathcal E_1=\{(0,0),(0,1),(1,0)\}\). For \(m=8\), every factor has two or three ones: any four-letter factor of \(p\) has between one and two ones (neither \(11\) nor \(0000\)), and either substitution alignment maps a four-letter parent's weight \(K\) to \(4-K\). Each of the six combinations of weight \(2\) or \(3\) with its two *endpoint letters* in \(\mathcal E_1\) occurs. Explicit witnesses, recorded as starting position / factor, are

```
K=2:  8 / 01000100    10 / 00010001     9 / 10001000
K=3:  3 / 00101010     0 / 01000101     1 / 10001010
```

Now assume for a dyadic \(m\ge8\) that every length-\(m\) factor has weight \(\lfloor m/3\rfloor\) or \(\lceil m/3\rceil\), and that all three endpoint-letter pairs in \(\mathcal E_1\) occur at **each** weight. Every length-\(2m\) factor starts at some position \(2t\) or \(2t+1\). Let \(v=p_t\cdots p_{t+m-1}\) be its parent length-\(m\) factor. Both alignments have \(m-|v|_1\) ones. At the even alignment the length-two prefix and suffix are \(0(1-p_t)\) and \(0(1-p_{t+m-1})\). At the odd alignment they are \((1-p_t)0\) and \((1-p_{t+m-1})0\). The odd window additionally uses the first symbol \(0\) of the next substituted pair, which neither alters its weight nor its last length-two suffix formula.

Consequently, the three possible parent endpoint pairs \((0,0),(0,1),(1,0)\) produce respectively, at even starts, \((01,01),(01,00),(00,01)\) and, at odd starts, \((10,10),(10,00),(00,10)\). These are exactly the six members of \(\mathcal E\), and all occur at each transformed weight. Since \(m\) is a power of two, the transformed pair of weights \(m-\lfloor m/3\rfloor\) and \(m-\lceil m/3\rceil\) equals \(\{\lfloor 2m/3\rfloor,\lceil 2m/3\rceil\}\). Moreover the six length-two boundary pairs have underlying endpoint-letter pairs covering all of \(\mathcal E_1\), hence the induction hypothesis holds again at \(2m\).

Starting from \(m=8\) establishes the precise \(2\times6\) signature classification for all \(n=2^k\) with \(k\ge4\). Section 2 proves that distinct signatures are precisely distinct 3-Abelian classes, completing the theorem.

## Verification

Execute `python3 verify_period_doubling.py` using Python's standard library. Its independent generators use direct substitution and the binary valuation formula for every one of the first 262,144 symbols. Sliding-window counters record actual length-three factor counts, not simply the reduced invariant. The program checks the reconstruction identity and the bijection between complete signatures and reduced signatures for 63 even lengths, and the twelve-class classification for ten dyadic scales up to length 4096. The run returned `VERIFY_OK independent_generation=262144 dyadic_scales=10 other_even_lengths=63`. These checks are finite; the all-scale proof is the preceding induction.

## Relationship to prior work

Karhumäki, Saarela and Zamboni introduced \(k\)-Abelian equivalence and complexity in 2013. Parreau, Rigo, Rowland and Vandomme (first preprint 2014, published 2015) proved 2-regularity for the **2-Abelian** complexity of the period-doubling word, not the present exact **3-Abelian** dyadic classes. In Vandomme's publicly available defense presentation, a graph and a tentative recurrence for the **Abelian** complexity of the **3-block coding** are displayed as a prospective study. Neither that conjectural assertion nor a finite plot supplies the exact 3-Abelian class classification, which also involves length-two boundary data. These distinctions are at the level of mathematical implications, not title differences.

## Limitations

No closed formula is claimed at all nondyadic lengths, no 2-regularity statement for the entire 3-Abelian complexity sequence is proved, and the 3-block-coding complexity is not independently classified here. The originality comparison covers identified accessible literature and database hits; exact equivalence in unindexed specialized work remains a residual risk. Finite verification cannot replace the proof. Independent scientific audit has not been performed.

## References

- J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104 (public January 22, 2013), https://arxiv.org/abs/1301.5104.
- A. Parreau, M. Rigo, E. Rowland, E. Vandomme, *A new approach to the 2-regularity of the ell-Abelian complexity of 2-automatic sequences*, arXiv:1405.3532 (public May 14, 2014), https://arxiv.org/abs/1405.3532.
- E. Vandomme, *Contributions to combinatorics on words in an abelian context and covering problems in graphs*, defense presentation, especially the 3-Abelian prospective study (slide 43/44), https://orbi.uliege.be/bitstream/2268/176364/2/these_defense_vandomme.pdf.
