# Exact ternary length-four single-insertion covering number

## Finding

Let \(\Sigma=\{0,1,2\}\). A set \(C\subseteq\Sigma^4\) is a single-insertion covering code when every \(y\in\Sigma^5\) contains some \(x\in C\) as an ordered subsequence. The minimum possible cardinality is
\[
I(3,4,1)=S(3,5,4)=31.
\]
Equivalently, no \(30\) ternary words of length \(4\) cover every ternary word of length \(5\), and the explicit \(31\)-word code below does.

## Assumptions and scope

All words are ordered tuples, and repeated symbols are allowed. Subsequence deletion can remove any one of the five positions, including endpoints; duplicate deletion outcomes are counted once. This statement concerns unrestricted, not necessarily linear, codes, a ternary alphabet, one insertion, and exactly lengths \(4\) and \(5\). No statement about other alphabets, lengths, or insertion radii is implied.

## Proof

Number the \(81\) elements of \(\Sigma^4\) and the \(243\) elements of \(\Sigma^5\) lexicographically, starting from index zero. Write \(x_j\) for the length-four word numbered \(j\), and \(y_i\) for the length-five word numbered \(i\). Form the binary incidence matrix \(A\) of size \(243\) by \(81\), with \(A_{ij}=1\) precisely when \(x_j\) is obtained by deleting one coordinate of \(y_i\). A code corresponds bijectively to a binary vector \(u\in\{0,1\}^{81}\). The covering property is equivalent, without relaxation, to
\[
Au\ge\mathbf1_{243}.
\]
Therefore its minimum size is the integer optimum \(\min\{\mathbf1_{81}^{\mathsf T}u:Au\ge\mathbf1_{243},\ u\in\{0,1\}^{81}\}\).

For the upper bound, choose the lexicographic indices
\[
\begin{gathered}
0,4,5,7,8,9,13,17,21,24,27,31,35,36,38,40,\\
42,44,46,51,55,56,66,68,69,70,72,76,77,79,80.
\end{gathered}
\]
Index \(j\) denotes the base-three four-digit word with integer value \(j\), leading zeros retained. The accompanying verifier independently forms every distinct deletion word of each of the \(243\) length-five inputs. It confirms that at least one deletion lies in the displayed set for every input. Thus \(I(3,4,1)\le31\).

For the lower bound, the accompanying reproducible integer-program computation solves the exact finite binary optimization above, with every one of the \(243\) constraints and \(81\) decision variables. A completed branch-and-bound/branch-and-cut solution reports integral optimum \(31\), a matching global dual bound of \(31\), and zero optimality gap. As a second equivalent but independently specified model, let \(v=\mathbf1_{81}-u\) be the vector of omitted codewords and \(r=A\mathbf1_{81}\). The covering conditions are exactly \(Av\le r-\mathbf1_{243}\). Maximizing \(\mathbf1_{81}^{\mathsf T}v\) with \(v\) binary gives the certified optimum \(50\), again with matching global dual bound and zero gap. Consequently every covering code has at least \(81-50=31\) words. Together with the construction, this proves the stated value, subject to the computational-verification conditions described below.

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy (tested with SciPy 1.17.0, HiGHS backend). The verifier recomputes the incidence matrix from distinct one-coordinate deletions rather than from insertion-ball expansion, validates the displayed construction, and independently formulates both the direct minimum-set-cover problem and the complementary maximum-omission problem. On completion, both exact mixed-integer optimizations return optimal status and matching primal and global bounds, with reported gap zero; the script then prints `VERIFY_OK`. The original run visited \(355\) nodes in the direct integer optimization and \(180\) nodes in its complementary formulation. No samples or extrapolations are used in place of the complete finite model.

## Relationship to prior work

The definition follows Xie, Sun and Ge, *New bounds for covering codes under insertions or deletions* (arXiv:2606.15379v1, first public June 13, 2026), which proves general bounds but no exact value for these parameters. Pikhurko, Verbitsky and Zhukovskii, *New bounds for the optimal density of covering single-insertion codes via the Turán density* (arXiv:2409.06425), denote the same invariant by \(S(q,k,r)\) and quote Grozea's exact ternary instance \(S(3,4,3)=12\); their treatment is principally asymptotic. Lenz, Rashtchian, Siegel and Yaakobi (2021) address general insertion/deletion covering bounds. These results do not imply the exact value \(S(3,5,4)=31\). The standard one-insertion ball count yields only \(\lceil243/11\rceil=23\) in this instance.

## Limitations

The lower bound relies on successful completion of two finite integer-program optimizations by the specified solver, not on a short human-checkable combinatorial lower-bound certificate. The verifier exposes all integer variables, incidence relations and constraints, and checks the solver's optimality status, primal bound, dual bound and integrality; it does not independently verify a proof trace of the solver's internal search. An unpublished or unindexed exact table could contain the same finite invariant.

## References

1. C. Xie, Y. Sun, G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1 (June 13, 2026).
2. O. Pikhurko, O. Verbitsky, M. Zhukovskii, *New bounds for the optimal density of covering single-insertion codes via the Turán density*, arXiv:2409.06425v1 (September 10, 2024).
3. A. Lenz, C. Rashtchian, P. H. Siegel, E. Yaakobi, *Covering codes using insertions or deletions*, IEEE Transactions on Information Theory **67** (2021), 3376–3388.
4. C. Grozea, finite covering-code data and the ternary length-three example as cited in Reference 2.
