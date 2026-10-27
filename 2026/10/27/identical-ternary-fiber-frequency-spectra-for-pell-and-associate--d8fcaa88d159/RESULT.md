# Identical ternary fiber-frequency spectra for Pell and associated Pell sequences

## Finding
Let \(P_0=0\), \(P_1=1\), and \(Q_0=Q_1=1\), with \(X_{n+2}=2X_{n+1}+X_n\) for \(X=P,Q\). For an integer \(k\geq1\), set \(M_k=3^k\) and \(L_k=8\cdot3^{k-1}\). For \(a\in\mathbb Z/M_k\mathbb Z\), define the exact fiber size
\[
\mu_{X,k}(a)=\#\{0\leq n<L_k:X_n\equiv a\pmod{M_k}\}.
\]
Both sequences have *least* period \(L_k\) modulo \(M_k\). Their fiber-size histograms are identical for every \(k\), with the following exact classification.

For \(k=1\), exactly one residue has multiplicity \(2\) and two residues have multiplicity \(3\). For \(k\geq2\), put \(h=k-2\) and
\[
s_h=1+\sum_{0\leq j,\ 2j<h}3^{h-2j-1}.
\]
For each \(X\in\{P,Q\}\), precisely \(3^k-2s_h\) residues have fiber size \(2\). For each integer \(j\geq0\) with \(2j<h\), precisely \(2\cdot3^{h-2j-1}\) residues have fiber size \(2+6\cdot3^j\). Finally, precisely two residues have fiber size \(2+3^{1+\lfloor h/2\rfloor}\). These multiplicities are distinct, so this is the full histogram. In particular every residue occurs, but the sequences have the same highly nonuniform frequency distribution.

## Assumptions and scope
All indices are nonnegative integers. A fiber is counted in one complete *least* period, not in a fixed arbitrary truncation or among infinite repetitions. The normalized associated Pell sequence used here is half the conventional even-valued Pell–Lucas sequence; multiplying all terms by \(2\), a unit modulo \(3^k\), only permutes residue labels, so it preserves the histogram. The theorem applies to every integer exponent \(k\geq1\), without an upper bound.

## Proof
**1. Eight progressions and their regular fibers.** Write
\[
A=\begin{pmatrix}0&1\\1&2\end{pmatrix},\qquad
A^8=\begin{pmatrix}169&408\\408&985\end{pmatrix}=I+3B,
\quad B=\begin{pmatrix}56&136\\136&328\end{pmatrix}.
\]
Modulo \(3\), \(A\) has order \(8\), while \(B\not\equiv0\). For \(X\in\{P,Q\}\), put \(c_{X,r}=(X_{r+8}-X_r)/3\pmod3\), where \(0\leq r<8\). Direct integer recurrence calculations give:

| \(r\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(P_r\bmod3\) | 0 | 1 | 2 | 2 | 0 | 2 | 1 | 1 |
| \(c_{P,r}\) | 1 | 1 | 0 | 1 | 2 | 2 | 0 | 2 |
| \(Q_r\bmod3\) | 1 | 1 | 0 | 1 | 2 | 2 | 0 | 2 |
| \(c_{Q,r}\) | 0 | 2 | 1 | 1 | 0 | 1 | 2 | 2 |

For any odd prime \(p=3\), elementary binomial expansion gives
\[
(I+3B)^{3^e}\equiv I+3^{e+1}B\pmod{3^{e+2}}\qquad(e\geq0).
\]
For every \(r\) with \(c_{X,r}\neq0\), it follows that
\[
X_{r+8(t+3^e)}-X_{r+8t}\equiv3^{e+1}c_{X,r}\pmod{3^{e+2}}
\]
for all \(t,e\geq0\). Successively choosing the ternary digits of \(t\) shows that \(t\mapsto X_{r+8t}\) maps \(\mathbb Z/3^{k-1}\mathbb Z\) *bijectively* onto the coset \(X_r+3\mathbb Z\pmod{3^k}\).

Thus six of the eight branches of each sequence are regular. For \(P\), the regular indices are \(r\in\{0,1,3,4,5,7\}\); for \(Q\), they are \(r\in\{1,2,3,5,6,7\}\). Each of the three residues modulo \(3\) is covered by exactly two regular branches. Consequently every residue modulo \(3^k\) gets exactly **two regular preimages**.

Since \(A^{8\cdot3^{k-1}}\equiv I\pmod{3^k}\), this is a period of both sequences. The initial \(8\)-cycle modulo \(3\) has least length \(8\). The unit difference on a regular branch forces its parameter \(t\) to have period exactly \(3^{k-1}\); hence no shorter overall period is possible, and \(L_k=8\cdot3^{k-1}\) is least.

**2. Two quadratic critical branches for \(P\).** The normalized Pell identity is
\[
Q_n^2-2P_n^2=(-1)^n.
\]
For \(r\in\{2,6\}\), the index \(n=r+8t\) is even and \(Q_n\equiv0\pmod3\). Since \(c_{Q,2}\) and \(c_{Q,6}\) are units, \(z=Q_n/3\) runs bijectively through \(\mathbb Z/3^{k-1}\mathbb Z\) as \(t\) does. There are exactly two roots \(\theta\in\mathbb Z_3\) of \(\theta^2=-1/2\), one congruent to \(1\) and the other to \(2\) modulo \(3\), by Hensel's lemma. On each branch, select the root \(\theta\equiv P_r\pmod3\). The Pell identity determines the branch uniquely:
\[
P_{r+8t}=\theta\sqrt{1-9z^2},
\]
where the square root is the unique one congruent to \(1\) modulo \(3\). Define
\[
w=z\sqrt{\frac{2}{1+\sqrt{1-9z^2}}}.
\]
Both nested square roots are well defined by binomial series over \(\mathbb Z_3\). The displayed map is of the form \(w=z+9H(z)\) with \(H\colon\mathbb Z_3\to\mathbb Z_3\) \(1\)-Lipschitz; it is therefore a bijective \(3\)-adic isometry, and it induces a permutation modulo every \(3^a\). Rationalizing the difference gives the exact identity
\[
P_{r+8t}=\theta-9\frac{\theta}{2}\,w^2.
\]
In particular, the two critical branches have disjoint images modulo \(3\) (one in each of the unit classes), and each reduces to a unit-scaled square map modulo \(3^{k-2}\).

**3. The same two quadratic critical branches for \(Q\).** The exceptional branches are now \(r\in\{0,4\}\), where \(P_n\equiv0\pmod3\). The unit values of \(c_{P,0}\) and \(c_{P,4}\) imply that \(z=P_n/3\) runs bijectively through \(\mathbb Z/3^{k-1}\mathbb Z\). Let \(\varepsilon=1\) for \(r=0\) and \(\varepsilon=-1\) for \(r=4\). Again the Pell identity forces the unique \(3\)-adic branch
\[
Q_{r+8t}=\varepsilon\sqrt{1+18z^2}.
\]
With
\[
w=z\sqrt{\frac{2}{1+\sqrt{1+18z^2}}},
\]
the map \(z\mapsto w\) is another bijective \(3\)-adic isometry (of the form \(z+9H(z)\)), and
\[
Q_{r+8t}=\varepsilon+9\varepsilon w^2.
\]
The two critical branches again occupy distinct classes modulo \(3\), with the same square-root multiplicities as the \(P\) branches. Hence the full fiber histograms are identical.

**4. Exact enumeration of square-map fibers.** For \(k\geq2\), write \(h=k-2\). In each critical branch, \(w\) traverses \(\mathbb Z/3^{k-1}\mathbb Z\); the image depends only on \(w\bmod3^h\). Each root of \(w^2\equiv y\pmod{3^h}\) therefore contributes exactly \(3\) preimages, in addition to the two regular preimages.

For \(h=0\), the unique class modulo \(1\) has one square root. For \(h\geq1\), each nonzero square class has even valuation \(2j<h\), and the number of such square classes of that valuation is \(3^{h-2j-1}\). Each has exactly \(2\cdot3^j\) roots modulo \(3^h\). The zero class has exactly \(3^{\lfloor h/2\rfloor}\) roots. These claims follow by dividing a root by \(3^j\) and using that exactly half the \(3^{h-2j-1}\cdot2\) units are squares. Thus each critical branch contributes \(3(2\cdot3^j)\) extra preimages for each of the \(3^{h-2j-1}\) square classes of valuation \(2j\), and \(3^{1+\lfloor h/2\rfloor}\) extra preimages for the zero square class. Exactly \(s_h\) residues per critical branch receive extras. Since the two critical images are disjoint, doubling these class counts and adding the regular multiplicity \(2\) yields precisely the stated histogram. The case \(k=1\) follows from the eight entries in the table. This completes the proof.

## Verification
The accompanying standalone Python program `verify_frequency.py` uses exact integer arithmetic. For both sequences and each \(1\leq k\leq11\), it computes every term of the purported least period, checks first return of the pair state, counts every residue's fiber, checks the predicted histogram, confirms complete residue coverage, and checks both the total number of residues and the weighted total of period terms. All \(22\) complete periods passed, comprising \(1,417,168\) evaluated terms. This finite verification is independent corroboration of the symbolic proof, not an infinite proof.

## Relationship to prior work
Lang and Lang (2013, arXiv:1307.7463), Propositions 5.1 and 5.2, classify the moduli for which Pell and Pell–Lucas sequences are residue complete. Their result implies the *nonzero support* of our histograms but does not determine the counts per residue, the equality of the two different histograms, or the quadratic hierarchy of the frequencies. Bragman and Rowland (first public arXiv submission February 1, 2022, arXiv:2202.00704) study limiting densities of attained Fibonacci residues modulo prime powers, with a square-map component in their \(p\)-adic analysis. Their objects, statistic, and formulas do not give this Pell/Pell–Lucas fiber-frequency classification. A finite computational comparison published in 2026 by Mason reports residue support counts for Pell at selected prime powers, without an all-exponent Pell/Pell–Lucas fiber-count law. The current result refines residue completeness to a complete counting law, beyond a support or density statement.

## Limitations
This result concerns only the prime \(3\), the named two sequences, and fiber frequencies per least period. It does not classify other primes, other recurrence parameters, or the ordered positions of the fibers. The combinatorial square-count formula is proved for every exponent, but novelty has been checked against accessible papers and searches, not by an exhaustive survey of all unpublished or unindexed mathematics. Independent mathematical validation has not been performed.

## References
1. C. L. Lang and M. L. Lang, *Three term recurrence and residue completeness*, arXiv:1307.7463 (first posted July 29, 2013), https://arxiv.org/abs/1307.7463.
2. N. Bragman and E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, arXiv:2202.00704 (first posted February 1, 2022), https://arxiv.org/abs/2202.00704.
3. Mason, *Fibonacci residues modulo prime powers*, finite computational comparison (August 2026), https://mason-m.com/fibonacci-prime-powers.
