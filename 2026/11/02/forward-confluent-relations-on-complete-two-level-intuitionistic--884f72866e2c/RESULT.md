# Forward-confluent relations on complete two-level intuitionistic frames: an exact census and uniform probability law

## Finding

For integers \(a,b\geq1\), let \(P_{a,b}=M\sqcup T\) be the labelled poset with \(|M|=a\), \(|T|=b\), all points in \(M\) below all points in \(T\), and no further strict comparisons. Write \(F(a,b)\) for the number of **arbitrary binary relations** \(R\subseteq P_{a,b}\times P_{a,b}\) satisfying forward confluence:
\[
\forall x,x',y\quad [x\leq x'\ \&\ xRy\ \Longrightarrow\ \exists y'\ (x'Ry'\ \&\ y\leq y')].
\]
There is no seriality, reflexivity, transitivity, valuation, or symmetry assumption on \(R\). Put \(A=2^a\), \(B=2^b\), and \(H=A+B-1\). Then
\[
\boxed{\begin{aligned}
F(a,b)={}&2^{a^2+ab}\bigl[(B-1)^b+H^b-B^b\bigr]\\
&+\sum_{z=1}^b\binom bz (B-1)^{b-z}2^{a(b-z)}(A+2^z-1)^a.
\end{aligned}}
\]
The census counts **labelled** relations on the fixed two-level order, not isomorphism classes.

The weighted relaxation used below additionally gives an **exact rejection sampler** for uniform forward-confluent relations: an explicit independent-column proposal is accepted with probability at least \(1-b2^{-b}\geq\tfrac12\) for all positive \(a,b\). This sampling consequence is part of the same structural counting theorem, not a separate classification claim.

A second, uniform result controls a uniformly chosen relation among the \(2^{(a+b)^2}\) possible relations. Define \(L(a,b)=2^{a^2+ab}H^b\). Then the **finite, explicit relative-error estimate**
\[
\boxed{0\leq 1-\frac{F(a,b)}{L(a,b)}\leq
 b\left(\frac{2^{b-1}}{H}\right)^b\leq b2^{-b}}
\]
holds for every \(a,b\geq1\). Consequently, as \(b\to\infty\), **uniformly over arbitrary positive integers \(a=a(b)\)**,
\[
\boxed{\Pr(R\text{ is forward confluent})
=2^{-ab}\bigl(1+2^{a-b}\bigr)^b\bigl(1+O(b2^{-b})\bigr).}
\]
For example, if \(a=b+s\) for a fixed integer \(s\), this probability is asymptotic to \(2^{-ab}(1+2^s)^b\); if \(b2^{a-b}\to0\), it is asymptotic to \(2^{-ab}\); and if \(b2^{b-a}\to0\), it is asymptotic to \(2^{-b^2}\). Thus the balance of the two levels controls the exponential scale of forward-confluent-frame rarity.

## Assumptions and scope

The complete two-level poset has one strict order relation from each member of \(M\) to each member of \(T\), and no relations between different members of the same level. All quantifiers over worlds refer to \(P_{a,b}\). The imposed condition is precisely the forward-confluence condition defining FIK bi-relational frames, without the additional backward-confluence condition used for stronger logics.

The distinguished lower level and upper level are part of the fixed labelled order. This asymmetry matters: \(F(1,2)=185\) whereas \(F(2,1)=281\). The smallest genuinely two-sided branching case is \(F(2,2)=11{,}401\), out of \(65{,}536\) binary relations. The \(a=1\) case reduces to an earlier exact rooted-fork enumeration and is **not** separately claimed as new.

## Proof

**1. Exact row criterion.** For each maximal source \(t\in T\), write its accessibility row as \(R(t)=Q_t\cup S_t\), with \(Q_t\subseteq M\) and \(S_t\subseteq T\). Define
\[
I=\bigcap_{t\in T}S_t,\quad
Z=\{t\in T:S_t=\varnothing\},\quad
J=\begin{cases}M,&Z=\varnothing,\\\bigcap_{t\in Z}Q_t,&Z\ne\varnothing.\end{cases}
\]
For each minimal source \(m\in M\), write \(R(m)=Y_m\cup X_m\), where \(Y_m\subseteq M\) and \(X_m\subseteq T\). Forward confluence is **equivalent** to
\[
\forall m\in M:\qquad X_m\subseteq I\quad\text{and}\quad Y_m\subseteq J.
\]
Indeed, the only nontrivial comparisons are \(m<t\). An upper target \(y\in X_m\) cannot be strictly refined, so it must occur in every upper-source row, giving \(X_m\subseteq I\). A lower target \(y\in Y_m\) is refined by every upper target: if \(S_t\ne\varnothing\), any element of \(S_t\) witnesses confluence; if \(S_t=\varnothing\), the only possible witness is \(y\) itself, requiring \(y\in Q_t\). This proves the equivalence with \(Y_m\subseteq J\). Once the \(b\) maximal rows are fixed, there are exactly \(2^{a(|I|+|J|)}\) allowed choices of all minimal-source rows.

**2. Count with no empty upper-target row.** If \(Z=\varnothing\), then \(J=M\), and the \(b\) lower-target sets \(Q_t\) are arbitrary. They contribute \(2^{ab}\), while the minimal-source rows contribute \(2^{a^2+a|I|}\). Hence this case contributes
\[
2^{a^2+ab}\sum_{\substack{S_t\subseteq T\\S_t\ne\varnothing\ \forall t}}2^{a|\cap_tS_t|}.
\]
Expand \(2^{a|I|}=\sum_{U\subseteq I}(2^a-1)^{|U|}\). The empty \(U\) yields \((B-1)^b\), and for nonempty \(U\) of size \(k\), each of the \(b\) sets \(S_t\) has \(2^{b-k}\) choices. Therefore the displayed sum is
\[
(B-1)^b+\sum_{k=1}^b\binom bk(A-1)^k2^{b(b-k)}
=(B-1)^b+H^b-B^b.
\]

**3. Count with empty upper-target rows.** Suppose exactly \(z\geq1\) maximal-source rows have \(S_t=\varnothing\). Then \(I=\varnothing\). Choose those rows in \(\binom bz\) ways; the remaining rows have \((B-1)^{b-z}\) choices for their nonempty upper-target subsets and \(2^{a(b-z)}\) choices for their unrestricted lower-target subsets. For the \(z\) empty-upper rows, sum over their lower-target subsets \(Q_t\). Every fixed element of \(M\) has \(2^z-1\) membership patterns not present in all \(Q_t\), each with weight one, and one all-present pattern with weight \(2^a\), because it is then available in each of the \(a\) minimal-source rows. Independence over the \(a\) elements of \(M\) gives \((2^z-1+2^a)^a\). Summing over \(z=1,\ldots,b\) and adding Step 2 proves the exact formula.

**4. Uniform error bound.** Relax the row criterion by imposing only \(X_m\subseteq I\), leaving every \(Y_m\subseteq M\) free. The number of relaxed relations is
\[
L(a,b)=2^{a^2+ab}\sum_{(S_t)_{t\in T}}2^{a|\cap_t S_t|}
=2^{a^2+ab}H^b.
\]
The last equality follows by treating each upper target as one column of \(b\) indicator bits: the all-one column has weight \(2^a\), and the other \(2^b-1\) patterns have weight one. The relaxation is exact whenever every \(S_t\) is nonempty. In the probability space on these columns weighted by the same factors, columns are independent and each fixed indicator in a given row equals zero with probability \(2^{b-1}/H\). Hence the weighted probability that a particular row \(S_t\) is empty equals \((2^{b-1}/H)^b\). The union bound over all \(b\) rows gives
\[
0\leq L(a,b)-F(a,b)\leq L(a,b)\,b(2^{b-1}/H)^b.
\]
As \(H\geq2^b\), the claimed finite uniform bound follows.

For completeness, the relaxation provides a constructive uniform sampler. Choose independently for each upper-target column one \(b\)-bit vector, with probability \(2^a/H\) for the all-one vector and \(1/H\) for every other vector. Given these columns, fill all upper-source-to-minimal-target bits and all minimal-source-to-minimal-target bits independently and fairly. For each upper target in the intersection \(I\), fill its minimal-source column independently and fairly, and force all other minimal-source-to-upper-target bits to zero. Every relaxed relation then has the same probability. Reject exactly when forward confluence fails. The resulting accepted law is uniform on the \(F(a,b)\) valid relations; its acceptance probability is \(F(a,b)/L(a,b)\), which is at least \(1-b2^{-b}\geq1/2\). In particular the expected number of proposals is at most two.

Finally, divide by \(2^{(a+b)^2}\):
\[
\frac{L(a,b)}{2^{(a+b)^2}}=2^{-ab}(1+2^{a-b}-2^{-b})^b.
\]
For \(\theta=2^{a-b}\), the ratio \([(1+\theta-2^{-b})/(1+\theta)]^b\) differs from one by at most \(b2^{-b}\), uniformly in \(a\). Combining this with the bound above proves the stated uniform probability law and its three regimes. Neither the counting formula nor this step uses any limiting assumption other than \(b\to\infty\) for asymptotic notation.

## Verification

The standalone file `checker.py` supplies two distinct finite tests. First, it evaluates the original three-quantifier forward-confluence condition for every binary relation on \(P_{a,b}\) for \((a,b)=(1,1),(1,2),(2,1),(1,3),(2,2),(3,1)\), independently checks the row criterion, and obtains respective counts \(11,185,281,10943,11401,33497\). Second, it sums over every possible family of maximal-source rows, without the closed-form algebraic simplification, for \((a,b)=(1,4),(2,3),(3,2),(3,3),(4,3)\), obtaining respectively \(2547617,1252925,3771875,847519079,3223875731057\). Exact integer tests additionally check the finite error bound for all \(1\leq a,b\leq8\). The checker returns `ALL_CHECKS_OK`.

These finite computations check implementation and several boundary cases; the all-parameter theorem and uniform asymptotic follow from the symbolic proof above, not from extrapolating finite data.

## Relationship to prior work

Balbiani, Gao, Gencer and Olivetti introduced FIK and its forward-confluence semantics in 2023. Gao and Olivetti's publicly posted 2026 study develops shallow proof theory and an EXPSPACE upper bound, rather than enumerating relations on fixed orders. The new object of study here is the labelled finite-frame census for **complete two-level orders with both level sizes free** and a uniform random-frame law.

An earlier rooted-fork count already gives the special case \(a=1\), and a previously published FIK-chain census concerns a total order instead of the two-antichain order \(P_{a,b}\). Neither statement by itself determines the formula for all \(a,b\geq2\) or the uniform two-parameter probability law. Results about IK with *both* forward and backward confluence count a more restricted frame class. Searches under forward-confluent relations, monotone relational simulation, complete bipartite posets, and two-level Kripke frames did not identify a theorem proving the precise formula and error estimate. Absence from a search index is not a proof of historical novelty.

## Limitations

The theorem assumes the complete two-level order, not an arbitrary height-two partial order. It counts labelled, unvalued relations without additional modal axioms; it does not enumerate models with valuations, isomorphism classes, or serial/reflexive/transitive subfamilies. The uniform asymptotic is as the number of upper points tends to infinity, with any positive number of lower points. The underlying FIK confluence semantics is established prior work. An older equivalent enumeration under relation-algebra or order-enriched powerset terminology remains possible, and full text of a relevant published chain census was not accessible for complete document comparison. No independent mathematical audit has been performed.

## References

1. H. Gao and N. Olivetti, *Taming Complexity in Intuitionistic Modal Logic: The Case of FIK and Its Shallow Calculus*, arXiv:2606.31877, first posted 2026-06-30, especially Definition 2.2 and the introduction. https://arxiv.org/abs/2606.31877
2. P. Balbiani, H. Gao, Ç. Gencer and N. Olivetti, *A Natural Intuitionistic Modal Logic: Axiomatization and Bi-nested Calculus*, arXiv:2309.06309, first posted 2023-09-12, especially Section 2 and the forward-confluence definition. https://arxiv.org/abs/2309.06309
3. *Gaussian-binomial census of FIK relations on finite chains*, public research record, title and published summary inspected; full text not obtained. (Compared only for scope of the reported chain theorem.)
4. *Exact fork-frame confluence counts and exponential separation of FIK from IK*, earlier research note, claim-level comparison; publication details unavailable. (The \(a=1\) case is excluded from the novelty assessment.)
