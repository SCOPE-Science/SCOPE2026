# Endpoint normal form and exact census for finite-chain KI frames
## Finding

Sato's completeness theorem for the new logic \(\mathbf{KI}\) uses fusion frames
\[
(W,\le,R)
\]
that satisfy both the \(\Box\)-p and \(\Diamond\)-p interaction conditions. These are also known as downward and forward confluence.

On a finite chain, those quantified conditions collapse to a complete endpoint normal form.

Let
\[
C_n=\{0<1<\cdots<n-1\}
\]
and let
\[
R\subseteq C_n\times C_n.
\]
For each row define
\[
m_i=
\begin{cases}
\min R(i),&R(i)\ne\varnothing,\\
n,&R(i)=\varnothing,
\end{cases}
\qquad
M_i=
\begin{cases}
\max R(i),&R(i)\ne\varnothing,\\
-1,&R(i)=\varnothing.
\end{cases}
\]

Then:
\[
\boxed{
R\text{ is }\Box\text{-p}
\iff
m_0\le m_1\le\cdots\le m_{n-1},
}
\]
and
\[
\boxed{
R\text{ is }\Diamond\text{-p}
\iff
M_0\le M_1\le\cdots\le M_{n-1}.
}
\]

Consequently, a finite-chain frame lies in the complete frame class of \(\mathbf{KI}\) exactly when either
\[
R=\varnothing,
\]
or every row is nonempty and
\[
0\le m_0\le\cdots\le m_{n-1}<n,
\qquad
0\le M_0\le\cdots\le M_{n-1}<n,
\]
with
\[
m_i\le M_i
\qquad(0\le i<n).
\]

For fixed admissible endpoint sequences \(m,M\), the rows are independent: row \(i\) can be any subset of
\[
[m_i,M_i]
\]
that contains both endpoints. Hence the number of relations with those endpoints is
\[
2^{\sum_{i=0}^{n-1}\max(M_i-m_i-1,0)}.
\]

Therefore the exact number of modal relations on the labelled \(n\)-chain satisfying both confluence conditions is
\[
\boxed{
N_n
=
1+
\sum_{\substack{
0\le m_0\le\cdots\le m_{n-1}<n\\
0\le M_0\le\cdots\le M_{n-1}<n\\
m_i\le M_i\ \forall i
}}
2^{\sum_i\max(M_i-m_i-1,0)}.
}
\]

The first six values are
\[
\boxed{
2,\ 7,\ 80,\ 2855,\ 374660,\ 195589841.
}
\]

The same frame conditions occur in the earlier local intuitionistic modal logic \(\mathbf{LIK}\), so the normal form also classifies finite-chain \(\mathbf{LIK}\) frames. Its direct relevance here is that Sato's 2026 theorem identifies exactly this two-confluence frame class as complete for the newly introduced \(\mathbf{KI}\) under the hybrid satisfaction relation.

## Assumptions and scope

The result fixes the intuitionistic preorder to the labelled chain \(C_n\). No seriality, reflexivity, or transitivity assumption is imposed on the modal relation \(R\).

The \(\Box\)-p condition is Sato's Definition 3.6 condition
\[
x\le x'Ry'
\Longrightarrow
\exists y\,(xRy\ \text{and}\ y\le y'),
\]
which is also called downward confluence.

The \(\Diamond\)-p condition is
\[
x'\ge xRy
\Longrightarrow
\exists y'\,(x'Ry'\ \text{and}\ y'\ge y),
\]
which is also called forward confluence.

Sato's Theorem C.14 proves completeness of \(\mathbf{KI}\) over frames satisfying both conditions, using the paper's hybrid satisfaction relation. The theorem here classifies only the underlying finite-chain frame relations; it does not count valuations or formulas and does not assert a finite-model property for \(\mathbf{KI}\).

The empty relation is permitted and satisfies both confluence conditions vacuously.

## Proof

We first characterize downward confluence.

Assume the \(\Box\)-p condition. Take
\[
i\le j.
\]
If row \(j\) is empty, then
\[
m_j=n,
\]
so automatically \(m_i\le m_j\).

If row \(j\) is nonempty, then
\[
jR m_j.
\]
Applying downward confluence to
\[
i\le jR m_j
\]
gives some \(y\) such that
\[
iRy\le m_j.
\]
Thus row \(i\) is nonempty and
\[
m_i\le y\le m_j.
\]
Therefore \((m_i)\) is nondecreasing.

Conversely, assume
\[
m_0\le\cdots\le m_{n-1}.
\]
Suppose
\[
i\le jRy'.
\]
Then row \(j\) is nonempty, hence
\[
m_j\le y'.
\]
Monotonicity gives
\[
m_i\le m_j<n,
\]
so row \(i\) is nonempty and \(iRm_i\). Taking
\[
y=m_i
\]
gives
\[
iRy\le y'.
\]
Thus \(R\) is \(\Box\)-p.

The forward-confluence statement is dual with maxima. Assume \(R\) is \(\Diamond\)-p and take \(i\le j\). If row \(i\) is empty then
\[
M_i=-1\le M_j.
\]
Otherwise
\[
iRM_i.
\]
Forward confluence applied to
\[
j\ge iRM_i
\]
gives some \(y'\) with
\[
jRy'\ge M_i.
\]
Hence
\[
M_j\ge y'\ge M_i.
\]
So \((M_i)\) is nondecreasing.

Conversely, assume \((M_i)\) is nondecreasing and suppose
\[
j\ge iRy.
\]
Then
\[
y\le M_i\le M_j.
\]
In particular \(M_j\ge0\), so row \(j\) is nonempty and
\[
jRM_j.
\]
Taking
\[
y'=M_j
\]
proves forward confluence.

Now assume both conditions. If any row \(i\) is nonempty, downward confluence forces every lower row \(j\le i\) to be nonempty, while forward confluence forces every higher row \(j\ge i\) to be nonempty. Since the order is total, every row is nonempty. Thus the only alternative is that every row is empty, namely \(R=\varnothing\).

In the nonempty case the two conditions are therefore equivalent to nondecreasing finite endpoint sequences \(m_i,M_i\) with
\[
m_i\le M_i.
\]

Fix such sequences. A row with exact minimum \(m_i\) and exact maximum \(M_i\) must contain those endpoints, can contain no point outside the interval, and can choose each strictly intermediate point independently. Hence its number of possibilities is
\[
2^{\max(M_i-m_i-1,0)}.
\]
Rows are otherwise independent because the confluence conditions have already been completely reduced to endpoint monotonicity. Multiplying the row counts and then summing over all endpoint pairs proves the displayed formula. The initial values follow by exact evaluation of that finite sum.

## Verification

The bundled checker verifies the theorem in two independent ways.

For
\[
1\le n\le4,
\]
it enumerates all
\[
2^{n^2}
\]
binary relations on the chain and tests the two source conditions literally, including their existential witnesses. It separately computes the row minima and maxima and verifies exact equivalence with monotonicity of the two endpoint sequences.

The direct counts are
\[
2,\ 7,\ 80,\ 2855.
\]

Independently, a weighted dynamic program evaluates the endpoint formula through
\[
n=10.
\]
It regards each nonempty row endpoint pair \((m,M)\) as a state with weight
\[
2^{\max(M-m-1,0)},
\]
and sums over nondecreasing state sequences. Its first six values are
\[
2,\ 7,\ 80,\ 2855,\ 374660,\ 195589841,
\]
and its first four agree exactly with direct relation enumeration.

The script prints `VERIFY_OK`.

## Relationship to prior work

Sato's 2026 survey introduces the logic \(\mathbf{KI}\), defines the \(\Box\)-p and \(\Diamond\)-p frame conditions, and proves completeness of \(\mathbf{KI}\) over frames satisfying both. The paper does not specialize the complete frame class to finite chains, reduce the conditions to endpoint monotonicity, or count the resulting relations.

The two confluence conditions themselves are older. Balbiani, Gao, Gencer, and Olivetti use forward and downward confluence for the local intuitionistic modal logic \(\mathbf{LIK}\), with locally interpreted modalities. Their 2024 work develops axiomatization, proof search, and finite countermodel extraction, but the checked full text does not give a finite-chain endpoint classification or an exact census.

The normal form here is stronger than merely observing that confluence is easy to test on a chain. It identifies complete invariants for both conditions, proves that simultaneous confluence forces the row-support set to be either empty or all of the chain, and decomposes every nonempty relation into two monotone endpoint sequences plus independent interior bits. This yields an exact finite search space for the complete frame class of the newly introduced logic \(\mathbf{KI}\).

Targeted searches for finite-chain downward/forward confluent relations, endpoint formulations, local intuitionistic modal chain frames, and the initial numerical census did not locate an equivalent theorem.

## Limitations

The theorem uses totality of the intuitionistic order. For a general finite partial order, a row need not have a single minimum or maximum that witnesses all confluence requirements.

The count concerns modal relations on a fixed labelled chain, not valuations, generated models, or inequivalent formulas.

No closed recurrence or asymptotic formula for \(N_n\) is claimed beyond the exact weighted multichain sum.

Because the same two confluence conditions predate \(\mathbf{KI}\), an equivalent combinatorial classification may exist under order-theoretic or relation-theoretic terminology not recovered by the checked searches.

## References

[1] Yuta Sato, “Intuitionistic and Constructive Modal Logics for Classical Modal Logicians,” arXiv:2608.29708, first posted 30 August 2026.

[2] Philippe Balbiani, Han Gao, Çiğdem Gencer, and Nicola Olivetti, “Local Intuitionistic Modal Logics and Their Calculi,” arXiv:2403.06772; in *Automated Reasoning — IJCAR 2024*, LNCS 14740, 78–96. DOI:10.1007/978-3-031-63501-4_5.

[3] Alex K. Simpson, *The Proof Theory and Semantics of Intuitionistic Modal Logic*, PhD thesis, University of Edinburgh, 1994.
