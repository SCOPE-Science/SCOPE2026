# Factorial suppression of Wilkinson growth under uniform pivot-tie breaking

## Finding

Consider the classical Wilkinson growth-factor matrix \(W_n\), \(n\ge2\), defined by
\[
(W_n)_{ij}=\begin{cases}
1,&j=n,\\
1,&i=j<n,\\
-1,&j<i\text{ and }j<n,\\
0,&i<j<n.
\end{cases}
\]
Perform exact Gaussian elimination with partial row pivoting in columns \(1,\ldots,n-1\). Among **all** rows attaining the largest absolute active-column entry, select uniformly and independently of earlier random choices conditional on the current matrix. Let \(G_n\) be the largest magnitude of an entry in any Schur complement or pivot row during elimination, divided by the original maximum entry magnitude (which is one). Equivalently here, \(G_n\) is the conventional upper-triangular element growth factor.

Write \((n)_{\underline{k}}=n(n-1)\cdots(n-k+1)\), with \((n)_{\underline0}=1\). Then \(G_n\) takes exactly the values \(2,4,\ldots,2^{n-1}\), and
\[
\Pr(G_n=2^j)=
\begin{cases}
\dfrac{n-j}{(n)_{\underline j}},&1\le j\le n-2,\\[3pt]
\dfrac2{n!},&j=n-1.
\end{cases}
\]
(The first branch is empty for \(n=2\).) In particular,
\[
\Pr(G_n\ge2^j)=\frac1{(n)_{\underline{j-1}}}
\quad(1\le j\le n-1),\qquad
\Pr(G_n=2^{n-1})=\frac2{n!}.
\]
The exact mean is
\[
\mathbb E G_n=2+\sum_{k=1}^{n-2}\frac{2^k}{(n)_{\underline k}}
=2+\frac2n+\frac4{n^2}+O(n^{-3})
\qquad(n\to\infty).
\]
Thus the standard deterministic first-tie pivot rule yields growth \(2^{n-1}\), whereas uniformly resolving the very same exact ties gives growth converging in probability and in mean to \(2\), with only factorial probability of realizing the worst-case factor. This is a distributional statement about a specified **tie-resolution policy**, not a smoothed-analysis result for perturbed entries.

## Assumptions and scope

All operations and comparisons are in exact real arithmetic; there are no numerical perturbations. The policy chooses uniformly among every exactly maximising absolute entry in the active column, not merely between the top and bottom candidates, and not by sampling pivots with arbitrary magnitude-dependent weights. Pivoting exchanges rows only, never columns. Growth includes every intermediate Schur complement and the eventual upper triangular factor; since partial-pivot multipliers are at most one, the usual definition that also includes the lower factor agrees here.

For clarity, denote by \(B_m\) the first \(m-1\) columns of \(W_m\); entries satisfy \((B_m)_{ij}=1\) for \(i=j\), \(-1\) for \(i>j\), and zero for \(i<j\). After an initial uninterrupted sequence of natural (first-current-row) pivots, the active matrix again has this \(B_m\) portion and a constant final column \(q\mathbf1\), with \(q\) a positive power of two.

## Proof

**1. Natural-prefix stages.** At a stage with \(m\ge2\) active rows, \(B_m\) in the leading columns and final column \(q\mathbf1\), the current pivot column is \((1,-1,\ldots,-1)^{\mathsf T}\); every row ties in absolute value. Choosing its first row leaves the same leading-column pattern of order \(m-1\), but doubles the final column from \(q\) to \(2q\). Hence after \(j-1\) natural pivots the remaining \(m=n-j+1\) rows all tie, and \(q=2^{j-1}\).

**2. A structural lemma after the first non-natural choice.** Consider such an active \(m\)-row matrix, choose one of its lower rows (local index \(s\ge2\)) as the first pivot, and retain the original local row labels. We claim that subsequent partial pivoting chooses only rows with labels \(2,\ldots,m\) until they are exhausted, and that the final column thereafter has value \(2q\) at the surviving original row \(1\) and zero at all other surviving rows. All other Schur entries have magnitude at most \(2\).

Here is a direct proof valid even when subsequent lower-row pivots tie. Suppose \(k\ge1\) pivots have been selected among rows with labels at least two. Their first-\(k\)-column minor cannot have two row indices greater than \(k\), since these rows are identical in their first \(k\) entries. Consequently any nonsingular selected row set must be
\[
S_k=\{2,3,\ldots,k\}\cup\{s\},\quad s>k.
\]
(The set \(\{2,\ldots,k\}\) is empty when \(k=1\).) Its leading minor has absolute determinant \(2^{k-1}\): replace the missing first row of the leading \(k\)-by-\(k\) lower-triangular matrix by the all-minus-one row, or solve the elementary triangular system explicitly. More generally, for a leading \(k\)-column minor formed from \(\{1,\ldots,k\}\) by replacing row \(r\) with any row above index \(k\), the absolute determinant equals \(2^{k-r}\). These identities follow also from the inverse of the leading triangular matrix, whose strict lower entries are \(2^{i-j-1}\).

For each unused row \(t\ge2\), the prospective next pivot is the ratio of the corresponding \((k+1)\)-column minor to this determinant. It is either zero or has absolute value \(2\); while any such unused row remains, at least one has value \(2\) (choose label \(k+1\) if \(s>k+1\), otherwise any label greater than \(k+1\)). The prospective pivot in original row \(1\) has absolute value only \(2^{1-k}\), because adjoining row \(1\) produces a leading minor of absolute determinant one. Therefore original row \(1\) cannot be selected until it is the only row remaining. Induction establishes the asserted pivot order class and also confirms that every selected leading minor is nonsingular.

To inspect all Schur entries explicitly, observe that every selected row in \(S_k\) has first-column entry \(-1\). For any unused lower row \(i\ge2\), its first \(k\) entries coincide with those of the selected row \(s\), namely \((-1,\ldots,-1)\). Hence its Schur entry in column \(j>k\) is \((B_m)_{ij}-(B_m)_{sj}\), of absolute value at most two; its final-column Schur entry is \(q-q=0\).

For original row \(1\), write its first \(k\) entries as a linear combination of the selected rows. The sum of the combination coefficients is \(-1\), by looking at column one. The coefficient of selected row \(s\) is \(-2^{1-k}\), as follows by back-substitution from columns \(k,k-1,\ldots,2\). In columns \(j>k\) other than the final column, the selected rows \(2,\ldots,k\) and original row \(1\) have zero entries, so this row's Schur entry is \(2^{1-k}(B_m)_{sj}\), of magnitude at most one. Its final-column entry is \(q-(-1)q=2q\). Because the future pivot rows all have zero final-column entry, this value persists until it becomes the very last pivot. This proves the lemma.

**3. Growth once a tie is broken.** Suppose the first non-natural pivot occurs at stage \(j\). Before it, the largest entry encountered is at most \(q=2^{j-1}\). The lemma shows that the largest later entry is at most \(\max\{2,2q\}=2q\), and that the final pivot is exactly \(2q\). Therefore \(G_n=2^j\). If no non-natural choice occurs at stages \(1,\ldots,n-2\), the remaining two-by-two matrix necessarily creates a final entry \(2^{n-1}\), regardless of which tied row is selected.

**4. Exact law and mean.** At stage \(j\), conditional on \(j-1\) natural choices, the active matrix has \(n-j+1\) tied rows. The conditional probability of another natural choice is \(1/(n-j+1)\). Thus the probability that the first non-natural pivot is stage \(j\le n-2\) is
\[
\frac{1}{(n)_{\underline{j-1}}}
\frac{n-j}{n-j+1}=\frac{n-j}{(n)_{\underline j}}.
\]
The remaining mass is the probability of choosing natural pivots for the first \(n-2\) stages, equal to \(1/(n)_{\underline{n-2}}=2/n!\). The survival identity follows by requiring the first \(j-1\) natural choices. Summing survival increments on the support \(2,4,\ldots,2^{n-1}\) gives the stated mean. In the mean expansion, the \(k=1\) term is \(2/n\), the \(k=2\) term is \(4/[n(n-1)]\), and for \(k\ge3\) successive terms have ratio at most \(2/3\); consequently their total is \(O(n^{-3})\). The formulas include \(n=2\) under the empty-sum convention. This completes the proof.

## Verification

The accompanying `check.py` uses exact rational arithmetic to enumerate all legal pivot ties, keeping the full Schur matrix and current growth maximum as separate dynamic-programming state components. It compares the resulting distribution, mean, and every tail probability to the formulas for \(2\le n\le9\). It reports `EXACT_CHECKS_OK 576`; all assertions passed. These finite enumerations are independent checks of the formulas and are not used as proofs for general \(n\). Run with `python3 check.py` using only the Python standard library.

## Relationship to prior work

Wilkinson's classical matrix and its deterministic worst-case growth of \(2^{n-1}\) are standard. Higham and Higham (1989, Theorem 2.2) characterize all real matrices attaining that maximal value under the usual pivot order. Shah and Urschel (2026, Sections 2 and 5) substantially extend worst-case and randomized-pivot growth theory, including exponential growth on sparse matrices and nearly exponential growth for other randomized partial-pivot models. Those results do not give the finite-size probability law for uniform **ties on this fixed matrix**. An openly accessible numerical exposition, *The order the greedy rule cannot choose*, observes that opposite deterministic tie policies yield growth \(2\) versus \(2^{n-1}\), but does not derive the complete uniform-tie distribution. The present result quantifies the entire middle ground, including all tails and the factorial worst-case probability.

## Limitations

The random model changes only the tie-breaking rule, not the matrix entries. Uniform tie-breaking is not equivalent to adding small independent Gaussian perturbations; such perturbations also change Schur entries, especially with finite precision. The statement is restricted to the classical Wilkinson construction and exact arithmetic. It neither bounds general matrices nor negates large-growth phenomena with strict pivot inequalities, nor does it imply corresponding backward-error probabilities. Bibliographic equivalence to an unindexed exact-tie treatment cannot be ruled out without further human investigation.

## References

1. R. Shah and J. Urschel, *Entry growth in Gaussian elimination*, arXiv:2608.19189v1 (first submitted 2026-08-19), especially Sections 1, 2 and 5. https://arxiv.org/html/2608.19189
2. N. J. Higham and D. J. Higham, *Large Growth Factors in Gaussian Elimination with Pivoting*, SIAM J. Matrix Anal. Appl. 10 (1989), 155–164, Theorem 2.2. https://eprints.maths.manchester.ac.uk/356/1/0610012.pdf
3. *The order the greedy rule cannot choose*, Numerical Linear Algebra, section on Wilkinson matrix pivot ties (accessible online). https://www.numerical-linear-algebra.com/essays/the-order-the-greedy-rule-cannot-choose/
4. *A worst case is as fragile as its margin*, Numerical Linear Algebra, section on measured random perturbations (not a proof of the present discrete law). https://www.numerical-linear-algebra.com/essays/a-worst-case-is-as-fragile-as-its-margin/
5. D. A. Spielman and X. Yu, *Large Growth Happens: Gaussian Elimination with Partial Pivoting on Random Matrices*, arXiv:2610.08701v1 (2026-10-06); its Gaussian-matrix random model differs from uniform tie-breaking on fixed \(W_n\). https://arxiv.org/abs/2610.08701
