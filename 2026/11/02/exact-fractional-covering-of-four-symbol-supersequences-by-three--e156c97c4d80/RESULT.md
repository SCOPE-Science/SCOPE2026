# Exact fractional covering of four-symbol supersequences by three-symbol subsequences

## Finding

For any integer alphabet size \(q\ge 2\), let \(\Sigma_q=\{0,\ldots,q-1\}\), and let \(\mathsf F_q\) be the optimum of the fractional single-insertion covering problem
\[
\mathsf F_q=\min\left\{\sum_{w\in\Sigma_q^3}x_w:\ x_w\ge0,\quad \sum_{w\in\operatorname{Del}_1(z)}x_w\ge1\ \text{for all }z\in\Sigma_q^4\right\}.
\]
Here \(\operatorname{Del}_1(z)\) is the **set of distinct** words obtained from \(z\) by deleting exactly one position; repeated deletion outputs count once.

The exact optimum for every alphabet is
\[
\boxed{\mathsf F_2=4,\qquad \mathsf F_q=\frac{q(q+1)^2}{4}\quad(q\ge3).}
\]
For \(q\ge3\), the optimum follows from explicit primal and dual fractional coverings that are invariant under alphabet permutations. In particular, \(\mathsf F_q/q^3\to1/4\). The integer optimum \(I(q,3,1)\) has limiting density \(s(4,3)>1/3\) by Pikhurko, Verbitsky and Zhukovskii [2]; therefore the integrality gap is structurally bounded away from one:
\[
\liminf_{q\to\infty}\frac{I(q,3,1)}{\mathsf F_q}\ge4s(4,3)>\frac43.
\]
The constant \(s(4,3)\) is the published limit for the integer covering problem, not a value computed here.

## Assumptions and scope

The alphabet \(\Sigma_q\) is labeled and finite; words are ordered, and the error operation is **one arbitrary insertion** into a length-three center, equivalently one deletion from a length-four received word. The variables \(x_w\) are nonnegative real weights. No symmetry constraint is imposed on the optimization: the displayed symmetric constructions are feasible in the unrestricted primal and dual programs. All statements are exact; no assumption that \(q\) is a prime power is used.

The dual program maximizes \(\sum_{z\in\Sigma_q^4}y_z\) over nonnegative \(y_z\), subject to \(\sum_{z:w\in\operatorname{Del}_1(z)}y_z\le1\) for each \(w\in\Sigma_q^3\).

## Proof

**Primal construction for \(q\ge3\).** Give a length-three word \(w\) weight
\[
x_w=\begin{cases}
1,&w=aaa,\\
\frac12,&w=aab\text{ or }w=abb\text{ with }a\ne b,\\
\frac14,&\text{otherwise}.
\end{cases}
\]
The remaining cases are nonadjacent repeats \(aba\) and three distinct letters \(abc\). To verify all coverage inequalities, classify a received word by the partition of its four positions into equal-symbol classes. The following exhaustive list uses first-occurrence labels; the tuple \((A,B,C,D)\) counts distinct length-three deletion outputs respectively of types \(aaa\), adjacent equal \(aab/abb\), separated equal \(aba\), and all distinct \(abc\).

| Equality pattern | \((A,B,C,D)\) | Total primal weight |
|---|---|---|
| `0000` | `(1,0,0,0)` | \(1\) |
| `0001`, `0111` | `(1,1,0,0)` | \(3/2\) |
| `0010`, `0100` | `(1,1,1,0)` | \(7/4\) |
| `0011` | `(0,2,0,0)` | \(1\) |
| `0012`, `0112`, `0122` | `(0,2,0,1)` | \(5/4\) |
| `0101` | `(0,2,2,0)` | \(3/2\) |
| `0102`, `0121` | `(0,1,1,2)` | \(5/4\) |
| `0110` | `(0,2,1,0)` | \(5/4\) |
| `0120` | `(0,0,2,2)` | \(1\) |
| `0123` | `(0,0,0,4)` | \(1\) |

These are the fifteen equality partitions of four positions, with the last pattern absent for \(q=3\). Every covering sum is at least one. Counting primal variables by type gives
\[
\sum_w x_w=q+\frac{2q(q-1)}2+\frac{q(q-1)+q(q-1)(q-2)}4=\frac{q(q+1)^2}{4}.
\]

**Dual construction for \(q\ge3\).** Define \(y_z\) for a length-four word \(z=(a,b,c,d)\) by
\[
y_z=\begin{cases}
1,&z=aaaa,\\
1,&z=aabb,\ a\ne b,\\
\frac{1}{2(q-2)},&z=abca,\ a,b,c\text{ pairwise distinct},\\
\frac{1}{4(q-2)},&a,b,c,d\text{ pairwise distinct},\\
0,&\text{otherwise}.
\end{cases}
\]
Check each center type. A constant \(aaa\) is covered among positive-weight received words only by \(aaaa\), of dual mass one. An adjacent-double center \(aab\) or \(abb\) is covered among positive-weight received words only by the appropriate \(aabb\), also mass one. A nonadjacent-double center \(aba\) has precisely \(2(q-2)\) positive-weight supersequences of the form \(acba\) or \(abca\) with a fresh third symbol; their combined mass is one. A three-distinct-letter center \(abc\) has precisely two length-four positive-weight supersequences with equal first/last letters and precisely \(4(q-3)\) with four distinct letters; their combined mass is
\[
\frac{2}{2(q-2)}+\frac{4(q-3)}{4(q-2)}=1.
\]
This covers every center type, proving dual feasibility. Summing the nonzero dual weights yields
\[
q+q(q-1)+\frac{q(q-1)(q-2)}{2(q-2)}+\frac{q(q-1)(q-2)(q-3)}{4(q-2)}
=\frac{q(q+1)^2}{4}.
\]
The final term vanishes at \(q=3\). Weak linear-programming duality matches the primal objective exactly, establishing optimality for all \(q\ge3\).

**Binary boundary.** For \(q=2\), the four centers `000`, `011`, `100`, `111` cover all sixteen length-four binary words by one insertion. Conversely, assign dual mass one to each of the four words `0000`, `1111`, `0011`, `1100` and zero elsewhere. Every length-three word is a distinct one-deletion descendant of at most one of these four words, so the dual is feasible with objective four. Thus \(\mathsf F_2=4\).

**Integrality gap.** For any \(q\), the integer insertion-cover size \(I(q,3,1)\) is at least \(\mathsf F_q\). Theorem 3 and Lemma 5 of [2] imply \(I(q,3,1)\ge s(4,3)q^3\) with \(s(4,3)>1/3\). Since \(\mathsf F_q/q^3\to1/4\), division and passage to the limit establish the asserted strict asymptotic gap.

## Verification

Run `python3 verify.py` in the same directory. The standalone standard-library checker reconstructs every deletion-incidence set, both rational certificates and their objectives for all \(q=3,\ldots,9\), and checks the binary primal and dual witnesses independently. It also enumerates all fifteen equality partitions and verifies the table. Output `VERIFY_OK` indicates all assertions passed. Finite checks are not used as proof of the universal formula; the explicit all-type primal/dual arguments above establish it for every \(q\ge3\).

## Relationship to prior work

Lenz, Rashtchian, Siegel and Yaakobi [1] introduce insertion coverings and derive sphere-volume bounds and probabilistic constructions, not the exact optimum of this fractional incidence linear program. Pikhurko, Verbitsky and Zhukovskii [2] prove a **strictly larger** than one-third asymptotic integer covering density at center length three, but do not determine this fractional optimum; indeed their integer density theorem combines with the present value to yield the asymptotic integrality-gap separation. Xie, Sun and Ge [3] extend insertion-covering lower bounds to higher insertion radii and identify an open gap between lower and upper bounds; they discuss stronger programming bounds in a different metric, rather than solve this fractional program. Grozea's publicly posted [4] integer-covering table provides the exact values \(I(3,3,1)=12\), \(I(4,3,1)=30\) and \(I(5,3,1)=57\), but those integer values do not imply the fractional optimum for all \(q\).

## Limitations

This is an exact result for the standard **fractional vertex-cover relaxation**, not a formula for the integer optimum \(I(q,3,1)\) or for stronger valid-inequality and semidefinite relaxations. The integer asymptotic constant \(s(4,3)\) is known to exist and exceed \(1/3\), but its precise value remains unresolved. The proof is specific to one insertion and three-symbol codewords. A review of searchable indexed literature and the cited primary texts did not find an equivalent general fractional optimum, but cannot exclude unpublished or unindexed earlier calculations.

## References

1. A. Lenz, C. Rashtchian, P. H. Siegel, and E. Yaakobi, *Covering Codes Using Insertions or Deletions*, IEEE Transactions on Information Theory 67 (2021), 3376–3388. https://arxiv.org/abs/1911.09944
2. O. Pikhurko, O. Verbitsky, and M. Zhukovskii, *New Bounds for the Optimal Density of Covering Single-Insertion Codes via the Turán Density*, IEEE Transactions on Information Theory 71 (2025), 4260–4266. https://arxiv.org/abs/2409.06425
3. C. Xie, Y. Sun, and G. Ge, *New Bounds for Covering Codes under Insertions or Deletions*, first publicly posted June 13, 2026. https://arxiv.org/abs/2606.15379
4. C. Grozea, *The Optimal Densities of Covering Single-Insertion Codes*, public integer covering tables (2024). https://www.brainsignals.de/users/cristian.grozea/combinatorial.html
