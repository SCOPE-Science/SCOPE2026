# The `2t-1` deletion-code redundancy coefficient extends to q-ary alphabets

## Statement

Let \(t\ge 2\) be fixed. There are constants \(A_t,B_t,N_t>0\) such that for every alphabet size \(q\ge2\) and every \(n\ge N_t\), there is a code \(\mathcal C\subseteq\Sigma_q^n\) correcting \(t\) deletions with

\[
|\mathcal C|\ge
\frac{q^n}{q^{A_t}n^{2t-1}(\log_2 n)^{B_t}}.
\]

Equivalently, its redundancy in bits satisfies

\[
 n\log_2q-\log_2|\mathcal C|
 \le (2t-1)\log_2 n+O_t(\log_2q+\log_2\log_2 n).
\]

In q-ary symbols,

\[
 n-\log_q|\mathcal C|
 \le (2t-1)\log_q n+O_t\!\left(1+\log_q\log_2 n\right).
\]

In particular, for every fixed finite alphabet the leading coefficient is \(2t-1\). For \(t=2\), every fixed q-ary alphabet therefore admits two-deletion-correcting codes with bit redundancy

\[
3\log_2 n+O_q(\log_2\log_2 n).
\]

The motivating binary result proves the same leading coefficient only for \(q=2\), and explicitly lists fixed larger alphabets as an open case.

## Proof

The proof transfers the substring-spectrum/random-hash argument of En Gad from the binary de Bruijn graph to the q-ary de Bruijn graph. The points at which the binary alphabet enters that argument are isolated below; each changes only a factor exponential in the number of local edits, and hence only the lower-order dependence on \(q\).

### 1. A dense q-ary unique family

Set

\[
k=2\lceil\log_2 n\rceil+2,\qquad L=3(k+1).
\]

Call a q-ary word \(k\)-unique if its length-\(k\) substrings are pairwise distinct. For two distinct starting positions, the probability that the corresponding length-\(k\) windows of a uniform random q-ary word agree is exactly \(q^{-k}\), including when the windows overlap. Indeed, if their starts differ by \(s\), equality makes the length-\(k+s\) covered segment periodic with period \(s\), leaving \(s\) free letters out of \(k+s\); for \(s\ge k\), the same count follows from \(k\) pairwise equality constraints.

Hence a union bound gives

\[
\Pr[\text{not }k\text{-unique}]
\le {n\choose2}q^{-k}
\le {n\choose2}2^{-k}
\le \frac18.
\]

Thus the q-ary family \(\mathcal W^{(q)}_{n,k}\) of \(k\)-unique words has size at least \((7/8)q^n\). The spectrum \(R_L(x)\in\mathbb Z^{q^L}\) of length-\(L\) substrings is the edge-incidence vector of the q-ary de Bruijn walk spelled by \(x\). The simple-path reconstruction lemma and the shared-source-letters lemma from the binary proof use only substring equality and source positions, so they hold verbatim over \(\Sigma_q\).

### 2. One edit is still a bubble

Let an edited symbol be \(d\in\Sigma_q\). Around its maximal constant run, the two local words have the form

\[
P=A d^\rho B,
\qquad
P'=A d^{\rho-1}B,
\]

where \(1\le\rho\le k+1\), \(|A|=|B|=L-\rho\), and now only

\[
\operatorname{last}(A)\ne d,
\qquad
\operatorname{first}(B)\ne d
\]

is required. The two boundary letters need not equal one another.

The binary proof that the two de Bruijn paths meet only at their common endpoints uses no complement identity beyond these inequalities. If equal vertex windows occur at offsets \(a,b\), the shared-source lemma gives \(a-b\in\{0,1\}\). In the case \(a=b>0\), the compared windows include

\[
P[L-1]=d,
\qquad
P'[L-1]=P[L]=\operatorname{first}(B)\ne d,
\]

which is impossible. In the case \(a=b+1\) away from the terminal endpoint, with \(j=L-\rho-1\), the compared windows include

\[
P[j+1]=d,
\qquad
P'[j]=P[j]=\operatorname{last}(A)\ne d,
\]

again impossible. Therefore the only common vertices are the endpoints. Different sufficiently separated edits have disjoint source neighborhoods, so the shared-source lemma also gives vertex-disjoint bubbles exactly as in the binary argument.

Consequently every separated alignment with exactly \(t\) deletions and \(t\) insertions has spectrum difference equal to a sum of \(2t\) disjoint signed bubbles. Every resulting rule is still a nonzero integer vector with entries in \(\{-1,0,1\}\).

### 3. Exceptional conflicts gain only a \(q^{O_t(1)}\) factor

Use the same additive random hash of q-ary substring spectra. For a fixed nonzero integer spectrum difference, the hash survival probability remains \(2/Q\), and linearly independent differences survive independently, because this statement depends only on the integer vectors and the random torus coefficients.

For an alignment with \(d\) deletions and \(d\) insertions, record the \(2d\) edit anchors and the \(d\) inserted symbols. The binary count \(n^{2d}2^d\) becomes

\[
n^{2d}q^d.
\]

Thus the family with fewer than \(t\) edits, or with \(t\) edits that are not separated, has at most

\[
C_t q^t L n^{2t-1}
\]

records for a constant \(C_t\). Its equal-label probability is therefore at most

\[
\frac{2C_t q^t L n^{2t-1}}{Q}.
\]

### 4. Bounded witnesses are alphabet-independent

After the separated-conflict lemma, the entire bounded-witness argument concerns only supports of rules, connectivity of their de Bruijn paths, linear independence over \(\mathbb Q\), and the fact that rule coordinates lie in \(\{-1,0,1\}\). These properties are unchanged for the q-ary catalogue. In particular, an odd component still supplies an independent generating witness of size \(R=O_t(L^2)\) whose bubble union has at most \((2t-1)R+1\) connected components, with the extra `+1` only in the same large-witness case as in the binary proof.

### 5. Witness descriptions gain only \(q^{O_t(R)}\)

The binary generating-set count describes each bubble by its orientation, run length and edited bit, and each path-transfer instruction needs at most one additional bit. Over \(\Sigma_q\), replace the edited bit by an edited symbol and the possible additional bit by one alphabet symbol. A witness with \(R\) rules has \(2tR\) bubbles and \(O_t(R)\) recovery instructions. Hence for some constants \(a_t,b_t\), the number of generating witness sets with \(R\) rules and \(c\) bubble components is at most

\[
n^c q^{a_tR}(LR)^{b_tR}.
\]

No further alphabet choices are needed: once a known length-\(k\) stretch is located in the \(k\)-unique source, the containing window is determined, exactly as in the original recovery count.

Choose a constant \(B_t\) large enough to absorb the polynomial factors in \(L\) and \(R\), and choose \(A_t\ge\max\{a_t,t\}\). Taking

\[
Q=\left\lceil 8q^{A_t}n^{2t-1}L^{B_t}\right\rceil
\]

makes the witness union bound converge exactly as in the binary proof: the factor \(q^{a_tR}\) is cancelled by the q-factor built into \(Q^R\), while the positional exponent remains \((2t-1)R\). The exceptional-conflict probability above also tends to zero uniformly in \(q\), since \(A_t\ge t\) and \(B_t\ge2\).

Therefore some hash leaves a fixed positive fraction of \(\mathcal W^{(q)}_{n,k}\) in bipartite conflict components. Taking the larger side of each component and then the largest of the \(Q\) hash classes gives a t-deletion-correcting code of size

\[
|\mathcal C|\ge c_t\frac{q^n}{Q}
\]

for a constant \(c_t>0\). Since \(L=O(\log n)\), this is the claimed bound.

## Consequences

For fixed \(q\), the leading bit-redundancy coefficient for the known existential upper bound is therefore \(2t-1\), not \(2t\). At \(t=2\), this gives coefficient \(3\) for every fixed nonbinary alphabet. Existing explicit q-ary two-deletion constructions have larger leading coefficients; for example, Ye--Sun--Yu--Ge--Elishco give \(5\log n+O(\log\log n)\) bits for q-ary two-deletion codes, while the result here is existential rather than efficiently encodable or decodable.

The quantitative form above is uniform in \(q\): allowing the alphabet size itself to vary contributes only \(O_t(\log q)\) additional bits in this argument.

## Verification

`artifacts/verify_qary_transfer.py` performs two finite checks of the alphabet-sensitive steps. It exhaustively verifies the exact \(q^{-k}\) equal-window probability/count for 94 small \((q,k,s)\) cases, including overlapping windows, and checks 2,160 q-ary bubble instances sampled from k-unique words over alphabets of sizes 3, 4 and 5. In every checked bubble, each route is simple and the two routes share exactly their two endpoints. The recorded output is in `artifacts/verification.txt`.

These computations are sanity checks only; the general result is established by the proof above.

## Originality boundary and limitations

The binary \((2t-1)\)-coefficient theorem, its random linear hash, bounded-witness extraction, and witness-counting mechanism are due to En Gad. The new claim is the q-ary extension, including the uniform dependence \(O_t(\log q)\) in bit redundancy. En Gad's Section 8 explicitly says that codes over a fixed larger alphabet appear to share the needed properties and asks whether the coefficient \(2t-1\) holds for them.

The argument is existential and randomized. It does not give an efficient encoder or decoder, does not improve the coefficient below \(2t-1\), and does not sharpen the doubly logarithmic correction term for fixed \(q\). Because the motivating preprint is very recent and the alphabet transfer becomes short after isolating its binary-specific steps, near-simultaneous discovery and folklore risk remain material.

## References

1. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493v1, 2026. https://arxiv.org/abs/2609.19493
2. Z. Ye, Y. Sun, W. Yu, G. Ge, and O. Elishco, *Codes Correcting Two Bursts of Exactly b Deletions*, arXiv:2408.03113; IEEE Transactions on Information Theory 72(4), 2026. https://arxiv.org/abs/2408.03113
3. W. Song and K. Cai, *Non-binary Two-Deletion Correcting Codes and Burst-Deletion Correcting Codes*, arXiv:2210.14006; IEEE Transactions on Information Theory 69(10), 2023. https://arxiv.org/abs/2210.14006
