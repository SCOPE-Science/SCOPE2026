# Rational Dyck arch-deficit series and exact near-universality strata

## Finding

For a Dyck word \(w\) of semilength \(n\) over \(\{0,1\}\), let \(\iota(w)\) be the largest \(k\) for which **every** binary word of length \(k\) occurs in \(w\) as an order-preserving (not necessarily contiguous) subsequence. Write \(\delta(w)=n-\iota(w)\), and let \(a_{n,d}\) count Dyck words of semilength \(n\) with \(\delta(w)=d\). Then **for every fixed \(d\ge0\)** the ordinary generating series \(G_d(z)=\sum_{n\ge0}a_{n,d}z^n\) is rational, given by the finite and explicit transfer formula below. In particular,

\[
\begin{aligned}
G_0(z)&=\frac{1}{1-z},\\
G_1(z)&=\frac{z^2}{(1-z)(1-2z)},\\
G_2(z)&=\frac{z^3(1-z)}{(1-2z)^3},\\
G_3(z)&=\frac{z^4(1-z)(1-2z+2z^2)}{(1-2z)^5}.
\end{aligned}
\]

Thus \(a_{n,1}=2^{n-1}-1\) for \(n\ge2\), and \(a_{n,2}=2^{n-5}(n-2)(n+1)\) for \(n\ge3\), with the latter interpreted as an integer at \(n=3,4\). These are not claimed as previously unknown integer sequences: \(a_{n,2}\), shifted by two indices, agrees with OEIS A001793, which already has another Dyck-path interpretation. The substantive result is the fixed-defect structural theorem and uniform rational computation, including the explicit third-defect distribution.

## Assumptions and scope

The empty word is included at \(n=0\). A Dyck word has exactly \(n\) opening letters \(0\), exactly \(n\) closing letters \(1\), and every prefix has at least as many openings as closings. The alphabet for universality is the full labeled binary alphabet \(\{0,1\}\). Distinct Dyck words are counted as distinct strings, without quotienting by symmetry. The greedy *arch decomposition* scans the string left to right and closes one arch each time both letters have appeared since the previous closure; the number of closed arches equals \(\iota(w)\). The result holds for all integer \(n,d\ge0\), with the parameter \(d\) fixed when describing a rational series. It does not say the joint bivariate series in \(n,d\) is rational.

## Proof

**Greedy arches.** Partition a word greedily into successive shortest nonempty blocks containing both letters, followed by a remainder containing at most one letter. Each such block realizes both one-letter subsequences; concatenating choices proves that the number of blocks is a lower bound for \(\iota\). Conversely, at the beginning of any unfinished block, one binary letter has not yet appeared in that block; choosing that missing letter at each greedy boundary constructs an absent subsequence of length one more than the number of completed blocks (equivalently, the standard arch-factorization theorem). Thus the index equals the greedy number of completed blocks [1,2]. In particular, each *two-letter input block* finishes at most one arch: after finishing it there is at most one symbol remaining in that input block.

**Pair decomposition.** Divide the Dyck word at even positions into exactly \(n\) blocks from \(\{00,01,10,11\}\). At even boundaries the ordinary Dyck height is even; write \(h\) for half this height. Reading blocks \(00,01,10,11\) changes \(h\) by \(+1,0,0,-1\), respectively. At \(h=0\) the blocks \(10\) and \(11\) are forbidden, and at \(h\ge1\) all four are allowed. This condition is necessary and sufficient for every *individual* symbol prefix to remain nonnegative. Therefore Dyck words are in bijection with excursions in this two-horizontal-color Motzkin step system.

Keep the greedy partial-arch state \(R\) (nothing seen since last closure), \(Z\) (only zero seen), or \(O\) (only one seen). Each block has one of the following next states; a subscript \(0\) means *no* arch closed during this block, and a subscript \(1\) means *one* arch closed:

| Current state | \(00\) | \(01\) | \(10\) | \(11\) |
|---|---|---|---|---|
| \(R\) | \(Z_0\) | \(R_1\) | \(R_1\) | \(O_0\) |
| \(Z\) | \(Z_0\) | \(R_1\) | \(Z_1\) | \(O_1\) |
| \(O\) | \(Z_1\) | \(O_1\) | \(R_1\) | \(O_0\) |

This table is obtained by processing the two bits consecutively. If \(b\) blocks fail to close an arch, the total number of closures is \(n-b\). Hence \(\delta(w)=b\) exactly.

**Height bound.** On the first ascent to any new paired-height maximum, the corresponding \(00\) block must have begun in state \(R\) or \(Z\), hence has subscript \(0\). Indeed, a *good* \(00\) could begin only in state \(O\). To reach state \(O\) at a paired height \(h\), starting from state \(R\) at height zero and without already visiting height \(h+1\), one would need an earlier \(11\) step from height \(h+1\): the only transition into state \(O\) from another state is \(11\), while \(01\) merely preserves \(O\). This contradicts the first visit to \(h+1\). Different newly reached height levels therefore consume distinct bad blocks, and

\[\max h\le\delta(w).\]

The usual Dyck height, including intermediate odd positions, is consequently at most \(2\delta(w)+1\).

**Finite matrices and rationality.** Fix \(d\ge0\). Index \(3(d+1)\) states by \((h,s)\), with \(0\le h\le d\) and \(s\in\{R,Z,O\}\). Let \(P_d\) and \(Q_d\) be the nonnegative integral adjacency matrices for allowed pair transitions whose table subscripts are, respectively, \(1\) and \(0\). Parallel transitions are counted separately. Let \(e\) select \((0,R)\), and let \(f\) select all three terminal states at height zero. Set \(R_d(z)=(I-zP_d)^{-1}\) as a matrix over rational functions. The height lemma shows no qualifying word is lost through truncation. Exactly \(d\) bad pair blocks give the identity

\[
\boxed{G_d(z)=e\,R_d(z)\bigl[zQ_dR_d(z)\bigr]^d f.}
\]

The formula expands each Dyck word exactly once into good-block runs separated by its \(d\) bad blocks. The matrix inverse exists as a formal series (its constant term is the identity), and its entries are rational functions of \(z\), proving rationality for all fixed \(d\). For \(d=0\), the only feasible word at each semilength is \((01)^n\). Substituting the displayed pair-transition table for \(d=1,2,3\), and simplifying finite rational matrices, gives exactly the four series in the Finding. Ordinary coefficient extraction yields the two displayed closed forms. No numerical experiment is used to extrapolate an infinite identity.

**Sparsity corollary.** At fixed \(d\), every counted Dyck path has ordinary height at most \(2d+1\). Such paths have a finite nearest-neighbor height transition graph with spectral radius strictly below \(2\); their counts therefore grow as \(O_d(\lambda_d^{2n})\) for some \(\lambda_d<2\). Since the total number of Dyck paths grows as \(4^n/(\sqrt\pi n^{3/2})\), a fixed arch-defect stratum has exponentially vanishing relative density.

## Verification

`verify.py` uses an independent symbol-by-symbol greedy-state evaluator and two separate counts: a direct enumeration of all \(82{,}500\) Dyck words of semilength at most \(11\), and a finite-pair dynamic program through semilength \(80\). All entries for defects \(0,1,2,3\) agree with coefficients of the four rational generating functions. `symbolic_certificate.py` separately constructs the finite rational transition matrices and checks symbolic equality for \(d=0,1,2,3\) (SymPy required for this optional algebraic check). The finite experiments validate implementation but do not replace the all-length proof using the height lemma and matrix formula.

## Relationship to prior work

The greedy arch characterization of subsequence universality and investigations of nearly universal words are established [1,2]. Adamson et al. count subsequence-universal words admitted by specified finite automata [1]; arbitrary Dyck words are not a regular language, and the fixed-deficit bounded-height reduction is not one of their stated results. Fleischmann et al. [2] study *numbers of missing subsequences* at a target length, distinct from the semilength-minus-universality statistic here. The exact sequence \(a_{n,2}\) is already OEIS A001793 [3], whose published Dyck interpretation counts pyramid weight, a different *pathwise* statistic; an illustrative path \(01001011\) lies in the cited pyramid-weight-three length-eight list but has arch deficit one, not two. Thus mere coincidence of a generating function is not evidence that the statistics agree objectwise. The present result claims the bounded-height mechanism, general fixed-deficit rationality, and corresponding explicit arch-defect counts, not discovery of the preexisting numerical sequence. No equivalence to a stronger unlocated result is ruled out.

## Limitations

Rationality is only asserted separately for fixed defect, with matrix size depending on the defect. The finite symbolic simplifications were carried out only through defect three. There is no assertion that the joint distribution, or any conditional limit theorem as the defect grows, is rational. The novelty comparison is based on inspected accessible primary material and an integer-sequence cross-check, not a proof of global uniqueness; analogous enumerations could be implicit in broader lattice-path or automata work. Independent assessment has not been performed.

## References

[1] D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea and D. Nowotka, *\(k\)-Universality of Regular Languages*, arXiv:2311.10658 (first posted 2023-11-17), https://arxiv.org/html/2311.10658v1.

[2] P. Fleischmann, L. Haschke, A. Huch, A. Mayrock and D. Nowotka, *\(m\)-Nearly \(k\)-Universal Words — Investigating Simon Congruence*, arXiv:2202.07981 (first posted 2022-02-16), https://arxiv.org/abs/2202.07981.

[3] OEIS Foundation, *A001793*, https://oeis.org/A001793 (accessed 2026-10-27); includes the earlier Dyck pyramid-weight interpretation attributed to E. Deutsch.
