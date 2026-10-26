# Oscillating coverage of the first perturbed Moser–de Bruijn digital sumset

## Finding

Let \(M\) be the nonnegative integers whose base-four digits all belong to \(\{0,1\}\). Set
\[
S=M+6M=\{x+6y:x,y\in M\},\qquad F(N)=\#\{0\le n<N:n\in S\}.
\]
Every \(n\in S\) has **exactly one** ordered representation \(n=x+6y\) with \(x,y\in M\). For each integer \(L\ge1\),
\[
\boxed{F(4^L)=\frac{4^L}{2},\qquad F(2\cdot4^L)=\frac{4^{L+1}+2}{3}.}
\]
Therefore the natural density of \(S\) fails to exist, since
\[
\lim_{L\to\infty}\frac{F(4^L)}{4^L}=\frac12,
\qquad
\lim_{L\to\infty}\frac{F(2\cdot4^L)}{2\cdot4^L}=\frac23.
\]
These limits along two explicit subsequences do **not** assert that the global lower and upper densities equal those values.

## Assumptions and scope

The set \(M\) is the Moser–de Bruijn sequence including zero, equivalently
\[
M=\left\{\sum_{j\ge0}\epsilon_j4^j:\epsilon_j\in\{0,1\},\ \epsilon_j=0\text{ for all but finitely many }j\right\}.
\]
All numbers and counting cutoffs are nonnegative integers, and \(L\ge1\). Here \([0,N)\) means the integers from zero through \(N-1\). The coefficient six is the smallest integer strictly greater than two for which the four one-place weights \(0,1,c,c+1\) are pairwise distinct modulo four: for \(c=6\) they reduce to \(0,1,2,3\). Thus this is the first nontrivial coefficient preserving the local uniqueness of the classical \(M+2M\) representation.

## Proof

**1. Uniqueness.** Each pair \((x,y)\in M^2\) is specified by base-four digits \((\epsilon_j,\eta_j)\in\{0,1\}^2\), and
\[
x+6y=\sum_{j\ge0}(\epsilon_j+6\eta_j)4^j.
\]
At any digit position the possible coefficients are \(0,1,6,7\), whose residues modulo four are pairwise distinct. If two such finite digit-pair strings differed, take the least position at which they differ. Reducing the difference of their sums divided by the corresponding power of four modulo four gives a nonzero residue, contradicting equality. Hence distinct pairs never have the same sum, and every member of \(S\) has exactly one representation.

**2. Exact carry automaton.** To read the base-four digits \(d_0,d_1,\ldots\) of an integer from least significant to most significant, start with carry \(c_0=0\) and solve uniquely for digits \(\epsilon_j,\eta_j\in\{0,1\}\) and a nonnegative carry \(c_{j+1}\) in
\[
\epsilon_j+6\eta_j+c_j=d_j+4c_{j+1}.
\]
For each carry \(c_j\in\{0,1,2\}\) and each \(d_j\in\{0,1,2,3\}\), the four possible digit coefficients exhaust the residue classes modulo four, giving one solution. Direct substitution shows that the outgoing carry always lies in \(\{0,1,2\}\). The transition table below gives \(c_{j+1}\), with rows indexed by \(c_j\) and columns by \(d_j\):
\[
T=\begin{pmatrix}
0&0&1&1\\
2&0&0&1\\
2&2&0&0
\end{pmatrix}.
\]
For \(0\le n<4^L\), pad its base-four expansion with zeros to exactly \(L\) digits. Then \(n\in S\) if and only if this algorithm ends with zero carry: if the carry is zero, its chosen digits yield a valid representation by elements of \(M\); conversely a representation of \(n<4^L\) cannot use digit positions at or above \(L\), as the summands are nonnegative, so its outgoing carry is zero. This is an exact finite membership criterion, not an asymptotic approximation.

**3. Counting complete blocks.** Let \(a_L,b_L,c_L\) count the \(L\)-digit words (including leading zeroes) whose final carries are respectively \(0,1,2\). From the transition table the count-transfer matrix is
\[
A=\begin{pmatrix}2&2&0\\2&1&1\\2&0&2\end{pmatrix},
\qquad (a_0,b_0,c_0)=(1,0,0),
\qquad (a_{L+1},b_{L+1},c_{L+1})=(a_L,b_L,c_L)A.
\]
Each input carry admits exactly two digits resulting in zero carry. Hence, because \(a_L+b_L+c_L=4^L\),
\[
a_{L+1}=2\cdot4^L.
\]
In particular \(a_L=4^L/2\) for all \(L\ge1\). The count for carry one satisfies \(b_{L+1}=2a_L+b_L=4^L+b_L\) for \(L\ge1\), with \(b_1=2\). Summation gives
\[
b_L=2+\sum_{j=1}^{L-1}4^j=\frac{4^L+2}{3}.
\]
Thus \(F(4^L)=a_L=4^L/2\).

**4. One additional high digit.** All integers in \([0,2\cdot4^L)\) have an \(L\)-digit lower block and a digit at position \(L\) equal to zero or one. When that high digit is zero, only incoming carry zero becomes zero; when it is one, incoming carry zero or one becomes zero. Therefore
\[
F(2\cdot4^L)=a_L+(a_L+b_L)=2a_L+b_L
=4^L+\frac{4^L+2}{3}=\frac{4^{L+1}+2}{3}.
\]
Dividing by the two cutoff lengths establishes the distinct limiting ratios. A convergent natural density would have the same limit along every sequence of cutoffs tending to infinity. Therefore it does not exist.

## Verification

The accompanying standalone `verify.py` constructs \(M\) directly by testing base-four digits, independently enumerates **every** weighted pair with sum below \(131072\), verifies there are no representation collisions, compares the explicit carry automaton with direct enumeration for **every** integer in that range, and checks the two exact counting identities and all three carry-class counts at every length \(1\le L\le8\). Run with `python3 verify.py`. This exhaustive finite test corroborates the proof but is not the basis of the universal statements.

## Relationship to prior work

The Moser–de Bruijn digit set and the complete, unique decomposition \(M+2M=\mathbb N_0\) are classical; they are not asserted to be new. De Bruijn's 1964 *Some Direct Decompositions of the Set of Integers* treats a different **signed** problem, namely unique decompositions \(Ms_1-2Ns_2\) covering all integers for selected multiplier pairs; its listed good-pair criteria do not count the positive sumset \(M+6M\). Nathanson's *Cassels Bases* analyzes the Raikov–Stöhr construction and the ordinary coefficient-two additive basis. Neither source gives the two explicit weighted counts here.

General theories for asymptotic densities of automatic sequences (Peter, 2003) and output sums of digital transducers (Heuberger–Kropf–Prodinger, 2015) provide a much broader methodological framework. The specific carry table and the \(1/2\)-versus-\(2/3\) cutoff discrepancy require an explicit computation for this set; no equivalent formula was located in the sources checked. The neighboring OEIS entries A000695 and A126684 describe \(M\) and \(M\cup2M\), respectively, not the positive sumset \(M+6M\).

## Limitations

This statement is restricted to the coefficient six and the two displayed families of cutoffs. The proof does not determine global lower or upper natural density, logarithmic density, or general weighted coefficients. Possible implicit equivalent consequences of general automatic-sequence theorems, or unlocated sequence databases, remain originality risks. Independent mathematical review has not been performed.

## References

1. N. G. de Bruijn, “Some Direct Decompositions of the Set of Integers,” *Mathematics of Computation* 18 (1964), 537–546. DOI: 10.1090/S0025-5718-1964-0167447-9. Public full text: https://pure.tue.nl/ws/files/2084140/597531.pdf.
2. M. B. Nathanson, “Cassels Bases,” in *Additive Number Theory: Festschrift in Honor of the Sixtieth Birthday of Melvyn B. Nathanson* (2010), Section 3. https://www.theoryofnumbers.com/melnathanson/pdfs/nath2010-138.pdf.
3. *OEIS A000695*, “Moser–de Bruijn sequence”; signed commentary by Marc LeBrun dated 2001-02-07 documents the classical unique coefficient-two decomposition. https://oeis.org/A000695.
4. *OEIS A126684*, “Union of A000695 and 2*A000695.” https://oeis.org/A126684.
5. M. Peter, “The Asymptotic Distribution of Elements in Automatic Sequences,” *Theoretical Computer Science* 301 (2003), 285–312. DOI: 10.1016/S0304-3975(02)00587-X.
6. C. Heuberger, S. Kropf and H. Prodinger, “Output Sum of Transducers: Limiting Distribution and Periodic Fluctuation,” *Electronic Journal of Combinatorics* 22(2) (2015), P2.19. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p19/pdf/.
