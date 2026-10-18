# Exact fork-frame confluence counts and exponential separation of FIK from IK

## Finding

Let \(P_k=\{o\}\sqcup L\), where \(k=|L|\ge 1\), the leaves in \(L\) are labelled and pairwise incomparable, and the only strict intuitionistic comparisons are \(o<\ell\) for \(\ell\in L\). Allow **every** binary modal accessibility relation \(R\subseteq P_k^2\): loops, empty rows, and nontransitive relations are all permitted. Write \(F_k\) for the number of such relations satisfying forward confluence (FC), and \(I_k\) for those satisfying **both** FC and backward confluence (BC), namely the standard FIK and IK frame conditions in this setting.

For integers \(k\ge1\) and \(m\ge0\), set
\[
H_{k,m}=(2^m+1)^k+\sum_{t=1}^{m}(-1)^t\binom mt 2^{k(m-t)},
\qquad
A_k=2^{k^2}+\sum_{t=1}^{k}(-1)^t\binom kt(2^{k-t}-1)^k.
\]
Empty sums vanish. Then the **exact labelled counts** are
\[
\boxed{F_k=2^{k(k+1)}+(2^{k+1}-1)^k+
2\sum_{j=1}^k\binom kj 2^{k(k+1-j)}}
\]
and
\[
\boxed{I_k=(2^k+1)^k+A_k+
\sum_{j=1}^k\binom kj\big((2^{k-j}+1)^k+H_{k,k-j}\big).}
\]
In particular,
\[
\boxed{\lim_{k\to\infty}2^k\frac{I_k}{F_k}=1.}
\]
Thus requiring backward confluence removes asymptotically a proportion \(1-2^{-k}(1+o(1))\) of the forward-confluent fork frames. For \(k=1,2,3,4\), the paired counts \((F_k,I_k)\) are \((11,9)\), \((185,81)\), \((10943,2043)\), and \((2547617,197529)\).

## Assumptions and scope

The frame \((P_k,\le,R)\) has \(x\le y\) exactly when \(x=y\) or \(x=o\) and \(y\in L\). The two conditions are, with **all variables universally quantified**,
\[
\mathrm{FC}:\quad x\le x'\ \land\ xRz\ \Longrightarrow\
\exists z'\,(x'Rz'\ \land\ z\le z'),
\]
\[
\mathrm{BC}:\quad xRz\ \land\ z\le z'\ \Longrightarrow\
\exists x'\,(x\le x'\ \land\ x'Rz').
\]
These are the forward and backward confluence conditions from the bi-relational intuitionistic modal semantics, without adding the frame axioms of the modal cube. Counts are for **labelled** leaves, with the root distinguished. They do not count valuations, formulas, or isomorphism classes. In particular, no reflexivity, seriality, symmetry or transitivity of \(R\) is silently imposed.

## Proof

**Step 1 (exact row normal form).** Define \(e\in\{0,1\}\) by \(e=1\iff oRo\), and set \(J=\{\ell\in L:oR\ell\}\), with \(j=|J|\). For each leaf \(a\in L\), let \(U_a=\{z\in P_k:aRz\}\). FC is equivalent to
\[
J\subseteq U_a\quad(a\in L),\qquad
(e=1\Longrightarrow U_a\ne\varnothing\quad(a\in L)). \tag{1}
\]
Indeed, the only nonidentity comparisons have source \(o\) and upper point a leaf. A root arrow to a leaf \(b\) must be witnessed by the same leaf \(b\), whereas a root arrow to \(o\) merely requires a nonempty successor row. Conversely these are all the nontrivial FC cases.

Under (1), BC is equivalent to two additional rules:
\[
\big(o\in U_a\big)\Longrightarrow L\subseteq U_a
\quad(a\in L), \tag{2}
\]
\[
e=1\Longrightarrow J\cup\bigcup_{a\in L}(U_a\cap L)=L.\tag{3}
\]
For (2), a leaf arrow \(aRo\) must extend to \(aRb\) for every \(b\in L\), since \(a\) has no proper upper world. For (3), the root loop \(oRo\) must extend to an arrow into each leaf; the source witness can be the root or any leaf. Conversely the only nonidentity target comparisons begin at \(o\), so (2) and (3) exhaust BC.

**Step 2 (count FC).** If \((e,J)=(0,\varnothing)\), each leaf row is arbitrary, giving \(2^{k(k+1)}\) relations. If \((e,J)=(1,\varnothing)\), each leaf row is nonempty, giving \((2^{k+1}-1)^k\). If \(J\ne\varnothing\) and \(|J|=j\), each leaf row must include \(J\), but its other \(k+1-j\) bits are free. There are \(2^{k(k+1-j)}\) choices for the \(k\) leaf rows. Either value of \(e\) is allowed. Summing over the \(\binom kj\) choices of \(J\) proves the displayed formula for \(F_k\).

**Step 3 (count FC+BC with no root loop).** If \(e=0\), rule (3) is vacuous. For each leaf row, (2) says either omit \(o\) and freely choose a subset of \(L\) containing \(J\), or include \(o\) together with **all** leaves. The first option has \(2^{k-j}\) choices and the second has one. Thus the contribution from each particular \(J\) is \((2^{k-j}+1)^k\), including \(J=\varnothing\). This yields the \((2^k+1)^k\) term and the first summand within the sum defining \(I_k\).

**Step 4 (count FC+BC with a root loop).** Suppose \(e=1\) and \(J\ne\varnothing\). Let \(M=L\setminus J\), \(m=|M|=k-j\). Each leaf row is either (i) a subset of leaves containing \(J\), with an arbitrary chosen subset of \(M\) and without \(o\), or (ii) the entire \(P_k\). There are \(2^m+1\) row choices. Rule (3) says that the union of the chosen rows covers \(M\). By inclusion-exclusion over the set \(T\subseteq M\) of missed columns: for \(T\ne\varnothing\), a row of type (ii) is impossible, and each row of type (i) has \(2^{m-|T|}\) choices. The count is exactly \(H_{k,m}\), including \(m=0\) where the sum is empty.

If \(e=1\) and \(J=\varnothing\), rule (1) also excludes the empty row. Each leaf row is therefore a nonempty subset of leaves without \(o\), or the full set \(P_k\); there are exactly \(2^k\) choices. To enforce (3), use inclusion-exclusion over uncovered leaf columns. If at least one column is forbidden, the full row is excluded and one must choose a nonempty subset of the remaining \(k-t\) leaves, hence \((2^{k-t}-1)^k\) configurations for a fixed forbidden \(t\)-set. This gives \(A_k\). Adding the four cases proves the formula for \(I_k\).

**Step 5 (sharp asymptotic ratio).** Put \(B_k=2^{k(k+1)}\) and \(C_k=2^{k^2}\). From the FC formula,
\[
F_k=B_k\big(2+O(k2^{-k})\big),\tag{4}
\]
since \((1-2^{-(k+1)})^k=1+O(k2^{-k})\) and
\(\sum_{j\ge1}\binom kj2^{-kj}=(1+2^{-k})^k-1=O(k2^{-k})\).

For the BC formula, \((2^k+1)^k=C_k(1+O(k2^{-k}))\). Moreover \(0\le C_k-A_k\le k2^{k(k-1)}\) by the union bound on a missing leaf column, so \(A_k=C_k(1+O(k2^{-k}))\). The \(J\ne\varnothing\) part is \(o(C_k)\): each of its two root-loop choices has at most \((2^{k-j}+1)^k\) leaf-row assignments. For \(1\le j\le\lfloor k/2\rfloor\), the sum of these upper bounds divided by \(C_k\) is at most
\[
2e^{k2^{-k/2}}\sum_{j=1}^{k}\binom kj2^{-kj}
=O(k2^{-k});
\]
for \(j>k/2\), it is at most \(2^{k+1}\,(2^{k/2}+1)^k/C_k=o(k2^{-k})\). Therefore
\[
I_k=C_k\big(2+O(k2^{-k})\big).\tag{5}
\]
Dividing (5) by (4) gives \(I_k/F_k=2^{-k}(1+O(k2^{-k}))\), proving the limit.

## Verification

The standalone `check.py` implements two independent tests of these formulas. First it exhaustively evaluates **the original quantified FC and BC conditions** over every relation on \(P_k\) for \(k=1,2,3\), a total of \(66064\) relations. Second, without using the closed sums, a dynamic count scans every possible root row, every allowed leaf-row bitmask and the union of reached leaf columns, reproducing \((F_k,I_k)\) for \(1\le k\le6\). Execute with `python3 check.py` in a directory containing the script; no libraries beyond the Python standard library are required. The symbolic argument above proves all \(k\ge1\), independent of those finite checks.

## Relationship to prior work

Balbiani, Gao, Gencer and Olivetti established the FIK semantics and its forward-confluence condition, including its distinction from IK. Gao and Olivetti's 2026 paper studied proof theory and a complexity upper bound for FIK; it supplies the recent point of departure, not these counts. De Groot, Shillito and Clouston supplied independent semantic comparisons of logics between CK and IK. Earlier finite-chain classifications use a **linear** intuitionistic order, whereas \(P_k\) here has \(k\) incomparable leaves. A transitive fork classification imposes **additional transitivity** and therefore concerns a strict subclass: it cannot yield the present unrestricted counts. The original FC and BC clauses are standard; the contribution here is the simultaneous unrestricted labelled enumeration and sharp asymptotic separation on rooted forks.

## Limitations

The enumeration is for rooted forks with one root and labelled incomparable leaves, and does not extend automatically to taller posets or to frame relations constrained by modal reflexivity/transitivity. It counts semantic frames rather than formula equivalence classes, and establishes no complexity lower bound or axiom-independence result. Although relevant accessible sources were compared, an unindexed equivalent enumeration could exist. No independent external validation has been performed.

## References

1. P. Balbiani, H. Gao, Ç. Gencer, and N. Olivetti, *A Natural Intuitionistic Modal Logic: Axiomatization and Bi-Nested Calculus*, CSL 2024, DOI `10.4230/LIPIcs.CSL.2024.13`; arXiv `2309.06309` (first posted 2023-09-12).
2. H. Gao and N. Olivetti, *Taming Complexity in Intuitionistic Modal Logic: The Case of FIK and Its Shallow Calculus*, EPTCS 447 (2026), 407–426, DOI `10.4204/EPTCS.447.23`; arXiv `2606.31877` (first posted 2026-06-30).
3. J. de Groot, I. Shillito, and R. Clouston, *Semantical Analysis of Intuitionistic Modal Logics between CK and IK*, LICS 2025, DOI `10.1109/LICS65433.2025.00020`; arXiv `2408.00262`.
