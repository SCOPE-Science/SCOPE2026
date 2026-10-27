# Four ones suffice for unbounded binary three-deck ambiguity

## Finding

For a finite binary word \(w\), let \(c_{abc}(w)\) denote the number of scattered subsequences equal to \(abc\), where \(a,b,c\in\{0,1\}\). The **three-deck** is the ordered vector of all eight counts. For integers \(n\ge3\) and \(0\le r\le n\), let \(M_r(n)\) be the greatest cardinality of any three-deck equivalence class among binary words of length \(n\) with exactly \(r\) ones.

**Theorem (sharp support threshold).** For every \(n\ge3\),
\[
M_r(n)=1\quad(0\le r\le\min\{2,n\}),\qquad M_3(n)\le2\quad(n\ge3).
\]
For \(n\ge7\), \(M_3(n)=2\). In contrast, for every \(n\ge124\),
\[
M_4(n)\ge1+\left\lfloor\log_6\left(\frac{n-4}{20}\right)\right\rfloor.
\]
In particular, the maximum fiber size of a fixed-length three-deck remains bounded when the number of ones is at most three, but is unbounded as length grows with exactly four ones.

## Assumptions and scope

Words are finite and linear, the alphabet is exactly \(\{0,1\}\), all three-deck counts retain multiplicity, and scattered subsequences need not be contiguous. The source length \(n\) is fixed and known. Three-deck equality is equivalent to three-binomial equivalence at fixed length \(n\ge3\), because shorter subword multiplicities are reconstructible from the length-three counts. The statement does not claim an optimal upper bound on \(M_4(n)\) or an exhaustive classification at weight four.

## Proof

**1. Reconstruction of shorter subword counts.** For a binary word \(u\) of length \(j<3\), summing the three-deck counts over all deletions of \(3-j\) positions from the indexed triples gives
\[
\binom{n-j}{3-j}c_u(w)=\sum_{|t|=3}\binom{t}{u}c_t(w).
\]
Every scattered occurrence of \(u\) extends to a length-three indexed occurrence in exactly \(\binom{n-j}{3-j}\) ways, proving the identity. Thus the deck recovers the number \(r\) of ones and the number of occurrences of \(01\).

**2. Moment description of a sparse word.** Write the positions of the \(r\) ones using the nondecreasing numbers \(0\le z_1\le\cdots\le z_r\le m\), where \(m=n-r\) and \(z_i\) is the number of zeros preceding the \(i\)-th one. Define
\[
S_0=\sum_{i=1}^{r}z_i,\qquad S_1=\sum_{i=1}^{r}i z_i,\qquad S_2=\sum_{i=1}^{r}z_i^2.
\]
Directly counting the choices of zeros on either side of the selected ones gives the eight complete three-deck coordinates:
\[
\begin{aligned}
c_{000}&=\binom{m}{3},&c_{001}&=(S_2-S_0)/2,\\
c_{010}&=mS_0-S_2,&c_{011}&=rS_0-S_1,\\
c_{100}&=\bigl(rm(m-1)-2mS_0+S_2+S_0\bigr)/2,&c_{101}&=2S_1-(r+1)S_0,\\
c_{110}&=\binom{r}{2}m-S_1+S_0,&c_{111}&=\binom{r}{3}.
\end{aligned}
\]
The recovered count \(c_{01}=S_0\), together with \(c_{011}\) and \(c_{001}\), determines \(S_0,S_1,S_2\). Conversely, for fixed \(m,r\), these three moments determine the whole three-deck by the displayed identities.

**3. At most three ones.** For \(r=0\) there is one word. For \(r=1\), \(z_1=S_0\). For \(r=2\), the two linear equations for \(S_0,S_1\) uniquely determine \(z_1,z_2\). For \(r=3\), those equations restrict any solution to a one-dimensional real affine line with direction \((1,-2,1)\). Along that line, \(S_2\) is a strictly convex quadratic with leading coefficient \(6\), so a prescribed value has at most two solutions, even before integrality and ordering are imposed. The two distinct words `0110001` and `1000110` both have deck \((4,6,6,3,6,6,3,1)\); appending the same number of zeros preserves three-deck equality and distinctness. Hence the bound two is attained at every length \(n\ge7\).

**4. A two-dimensional moment-preserving lattice at four ones.** Fix \(k\ge1\), put \(R=6^k\), \(B=4R\), \(m=5B\), and consider, for \(0\le j\le k\), the Gaussian-type products in \(\mathbb Z[\sqrt{-5}]\)
\[
x_j+y_j\sqrt{-5}=(1+\sqrt{-5})^j(1-\sqrt{-5})^{k-j}.
\]
Taking norms gives \(x_j^2+5y_j^2=R\). Since \(R\) is even, \(x_j\) and \(y_j\) have the same parity. Thus each vector
\[
v_j=\frac12\bigl(x_j-y_j,\ 3y_j-x_j,\ -x_j-3y_j,\ x_j+y_j\bigr)
\]
consists of integers and satisfies
\[
\sum_{i=1}^{4}(v_j)_i=0,\qquad
\sum_{i=1}^{4}i(v_j)_i=0,\qquad
\sum_{i=1}^{4}(v_j)_i^2=R.
\]
Set \(z_{j,i}=iB+(v_j)_i\) for \(i\in\{1,2,3,4\}\). Because \(\lvert(v_j)_i\rvert\le\sqrt R\) and \(B=4R>2\sqrt R\),
\[
0<z_{j,1}<z_{j,2}<z_{j,3}<z_{j,4}<m.
\]
Consequently these are valid numbers of preceding zeros for four ones and yield the distinct candidate words
\[
w_j=0^{z_{j,1}}1\,0^{z_{j,2}-z_{j,1}}1\,0^{z_{j,3}-z_{j,2}}1\,0^{z_{j,4}-z_{j,3}}1\,0^{m-z_{j,4}}.
\]
Every word has length \(n_k=m+4=20\cdot6^k+4\). Their moments agree exactly:
\[
S_0=10B,\quad S_1=30B,\quad S_2=30B^2+R.
\]
Hence Step 2 proves that all \(w_j\) have the same three-deck, without depending on a finite computation.

**5. Pairwise distinctness.** Put \(\alpha=1+\sqrt{-5}\) and \(\bar\alpha=1-\sqrt{-5}\). If two products \(\alpha^j\bar\alpha^{k-j}\) were equal, \(\zeta=\alpha/\bar\alpha\) would be a root of unity. But
\[
\zeta+\zeta^{-1}=-\frac43.
\]
A root of unity and its inverse are algebraic integers, so their rational sum must be an integer; \(-4/3\) is not. Therefore all \(k+1\) pairs \((x_j,y_j)\), all moment vectors and all words are distinct. We have \(M_4(n_k)\ge k+1\).

**6. Every sufficiently large source length.** For \(n\ge124\), choose the largest integer \(k\ge1\) satisfying \(20\cdot6^k+4\le n\). Append \(n-n_k\) zeros to each \(w_j\). Their four zero-prefix coordinates are unchanged, their common zero count becomes \(m+n-n_k\), and their moments remain identical. The formula of Step 2 therefore proves three-deck equality after padding. Distinctness is preserved. The maximal choice of \(k\) yields the stated lower bound for \(M_4(n)\), completing the proof.

## Verification

The standalone `verify_three_deck.py` implements three independently interpretable computations: a dynamic-programming scattered-subsequence counter, a direct triple-index enumerator at short lengths, and the closed moment formula. The moment formula matched the dynamic counter for 2,372 binary words of length at most twelve having at most four ones; at lengths at most nine it also matched direct triple enumeration. The script checks the complete lower-support bounds for every weight \(0,1,2,3\) and every length from three to fourteen. It directly constructs and checks all \(k+1\) deck-identical words for \(k=1,2,3,4,5\), of lengths \(124,724,4324,25924,155524\). These tests do not replace the universal algebraic argument in Steps 1–6.

Reproduce using Python 3 standard library only: `python3 verify_three_deck.py`. The proof and checker do not require external databases or numerical floating-point approximations.

## Relationship to prior work

Rigo and Salimov (initially publicly available in 2013) introduced and analyzed the binomial-equivalence framework and the concatenation operation. Their principal finite binary class count is for two-binomial equivalence, while their three-binomial work concerns infinite-word complexity. Lejeune, Rigo and Rosenfeld study equivalence classes of finite words and general class-count asymptotics, including the two-binomial algorithm, but do not state the four-one growing three-deck fibers here. Chrisnata and collaborators enumerate the number of *distinct decks*, which is a different statistic from the **largest cardinality of one fixed deck's preimage** at fixed composition. OEIS A258585 records aggregate numbers of binary three-binomial classes and early ambiguous pairs, not the present lower bound at weight four. The present theorem isolates a change in fiber size at a specific support threshold and gives an explicit arithmetic witness family.

## Limitations

The logarithmic lower bound is not claimed optimal, the construction uses only a sparse subsequence of length parameters before padding, and the theorem does not classify all four-one fibers. Scientific priority cannot be established exhaustively by search; equivalent results may be unindexed or phrased under other reconstruction terminology. All assertions are mathematical/procedural results about the stated fixed-deck model; the testing ranges are strictly finite.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013 author preprint and long version, https://hdl.handle.net/2268/149313 (publicly available 2013-05-27).
2. M. Lejeune, M. Rigo and M. Rosenfeld, *On the Binomial Equivalence Classes of Finite Words*, arXiv:2001.11732 (2020), https://arxiv.org/abs/2001.11732.
3. J. Chrisnata, H. M. Kiah, S. Rao, A. Vardy, E. Yaakobi and H. Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, https://doi.org/10.1109/ISCIT.2019.8905191.
4. OEIS A258585, *Number of Equivalence Classes of 3-Binomial Complexity for Binary Words of Length n*, https://oeis.org/A258585.
