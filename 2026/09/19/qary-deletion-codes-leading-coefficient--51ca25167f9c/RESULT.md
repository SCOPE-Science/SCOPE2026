# The `2t-1` deletion-code redundancy coefficient extends to q-ary alphabets

## Statement

Let \(t\ge2\) be fixed. There are constants \(A_t,B_t,N_t>0\) such that for every alphabet size \(q\ge2\) and every \(n\ge N_t\), there is a code \(\mathcal C\subseteq\Sigma_q^n\) correcting \(t\) deletions with

\[
|\mathcal C|\ge \frac{q^n}{q^{A_t}n^{2t-1}(\log_2 n)^{B_t}}.
\]

Equivalently,

\[
n\log_2 q-\log_2|\mathcal C|
\le (2t-1)\log_2 n+O_t(\log_2 q+\log_2\log_2 n).
\]

In q-ary symbols this is

\[
n-\log_q|\mathcal C|
\le (2t-1)\log_q n+O_t(1+\log_q\log_2 n).
\]

Thus every fixed finite alphabet has the same leading coefficient \(2t-1\) as the recent binary theorem. In particular, for \(t=2\), every fixed q-ary alphabet admits two-deletion-correcting codes with bit redundancy

\[
3\log_2 n+O_q(\log_2\log_2 n).
\]

## Proof

The proof transfers the substring-spectrum/random-hash argument of En Gad from the binary de Bruijn graph to the q-ary de Bruijn graph. Only four parts of that proof use the alphabet size, and each changes by at most a factor \(q^{O_t(R)}\) for a witness with \(R\) rules.

### Dense q-ary unique words

Set

\[
k=2\lceil\log_2 n\rceil+2,\qquad L=3(k+1).
\]

Call a q-ary word \(k\)-unique when its length-\(k\) substrings are pairwise distinct. For two distinct starts separated by \(s\), equality of the two length-\(k\) windows has probability exactly \(q^{-k}\), even when they overlap: on the covered length-\(k+s\) segment the equality condition leaves exactly \(s\) freely chosen letters. Hence

\[
\Pr[\text{not }k\text{-unique}]
\le {n\choose2}q^{-k}
\le {n\choose2}2^{-k}
\le \frac18.
\]

So the family \(\mathcal W^{(q)}_{n,k}\) of q-ary \(k\)-unique words has size at least \((7/8)q^n\). The spectrum \(R_L(x)\in\mathbb Z^{q^L}\) is the edge-incidence vector of the q-ary de Bruijn walk spelled by \(x\). The simple-path reconstruction lemma and the shared-source-letters lemma use only substring equality and source positions, and therefore remain valid over \(\Sigma_q\).

### Local edits remain bubbles

Let the edited symbol be \(d\in\Sigma_q\). Around its maximal constant run, the longer and shorter local words are

\[
P=A d^\rho B,\qquad P'=A d^{\rho-1}B,
\]

where \(1\le\rho\le k+1\), \(|A|=|B|=L-\rho\), and now only

\[
\operatorname{last}(A)\ne d,\qquad \operatorname{first}(B)\ne d
\]

is required. The two boundary symbols need not equal each other.

The binary proof that the two de Bruijn paths meet only at their common endpoints uses only those inequalities. If equal vertex windows occur at offsets \(a,b\), the shared-source lemma gives \(a-b\in\{0,1\}\). If \(a=b>0\), the compared windows contain

\[
P[L-1]=d,\qquad P'[L-1]=P[L]=\operatorname{first}(B)\ne d,
\]

which is impossible. If \(a=b+1\) away from the terminal endpoint and \(j=L-\rho-1\), they contain

\[
P[j+1]=d,\qquad P'[j]=P[j]=\operatorname{last}(A)\ne d,
\]

again impossible. Thus the paths share only their endpoints. Sufficiently separated edits have disjoint source neighborhoods, so their bubbles share no de Bruijn vertex. A separated alignment with exactly \(t\) deletions and \(t\) insertions therefore has spectrum difference equal to a sum of \(2t\) disjoint signed bubbles, and every rule still has coordinates in \(\{-1,0,1\}\).

### Exceptional conflicts

Use the same additive random hash on q-ary substring spectra. For every fixed nonzero integer spectrum difference, the survival probability remains \(2/Q\); rationally independent differences survive independently. This statement is unaffected by the number \(q^L\) of spectrum coordinates.

An alignment with \(d\) deletions and \(d\) insertions is specified by its \(2d\) edit anchors and its \(d\) inserted symbols. Thus the binary record count \(n^{2d}2^d\) becomes \(n^{2d}q^d\). Consequently the family with fewer than \(t\) edits, or with \(t\) edits that violate the separation condition, has at most

\[
C_t q^t L n^{2t-1}
\]

records. Its equal-label probability is at most

\[
\frac{2C_tq^tLn^{2t-1}}{Q}.
\]

### Witness extraction and counting

After the separated-conflict lemma, the bounded-witness argument is alphabet-independent: it uses only rule supports, de Bruijn connectivity, rational linear dependence, and the fact that rule coordinates lie in \(\{-1,0,1\}\). Hence every odd conflict component again yields an independent generating witness with \(R=O_t(L^2)\) rules and at most \((2t-1)R+1\) bubble components, exactly as in the binary proof.

The binary generating-set description gives each bubble an orientation, a run length, and an edited bit; path-transfer instructions require at most one extra bit. Over \(\Sigma_q\), replace these bits by alphabet symbols. A witness with \(R\) rules has \(2tR\) bubbles and only \(O_t(R)\) recovery instructions, so for constants \(a_t,b_t\) the number of generating witness sets with \(R\) rules and \(c\) bubble components is bounded by

\[
n^c q^{a_tR}(LR)^{b_tR}.
\]

Choose \(A_t\ge\max\{a_t,t\}\) and choose \(B_t\) large enough to absorb the polynomial factors in \(L\) and \(R\). With

\[
Q=\left\lceil 8q^{A_t}n^{2t-1}L^{B_t}\right\rceil,
\]

the factor \(q^{a_tR}\) is cancelled by the q-dependent part of \(Q^R\), while the positional exponent remains \((2t-1)R\). The same witness union bound therefore converges, and the exceptional-conflict probability above also tends to zero uniformly in \(q\).

For some hash, a fixed positive fraction of \(\mathcal W^{(q)}_{n,k}\) remains in bipartite conflict components. Taking the larger side of each component and then the largest of the \(Q\) hash classes gives

\[
|\mathcal C|\ge c_t\frac{q^n}{Q}
\]

for a constant \(c_t>0\). Since \(L=O(\log n)\), this proves the theorem.

## Consequences

For every fixed \(q\), the existential leading bit-redundancy coefficient is therefore at most \(2t-1\), rather than the generic greedy coefficient \(2t\). At \(t=2\), the coefficient is \(3\) for every fixed nonbinary alphabet. Existing explicit q-ary two-deletion constructions have larger leading coefficients; for example, Ye--Sun--Yu--Ge--Elishco give \(5\log n+O(\log\log n)\) bits for q-ary two-deletion codes. The result here is existential rather than efficiently encodable or decodable.

The quantitative form is uniform in \(q\): allowing the alphabet size to vary contributes only \(O_t(\log q)\) additional bits.

## Verification

`artifacts/verify_qary_transfer.py` checks two elementary alphabet-sensitive identities used above. It exhaustively verifies the exact equal-window count in 42 small \((q,k,s)\) cases, including overlapping windows, and verifies 532 boundary-symbol choices across alphabet sizes 2 through 7. The recorded output is in `artifacts/verification.txt` and is `PASS`. These finite checks are sanity checks only; the theorem is established by the analytic proof.

## Originality boundary and limitations

The binary \((2t-1)\)-coefficient theorem, random linear hash, bounded-witness extraction, and witness-counting mechanism are due to En Gad. The new claim is the q-ary extension and its uniform \(O_t(\log q)\) dependence in bit redundancy. En Gad's Section 8 explicitly says that codes over a fixed larger alphabet appear to share the required properties and asks whether the coefficient \(2t-1\) holds for them.

The construction remains existential and randomized. It does not provide an efficient encoder or decoder, improve the leading coefficient below \(2t-1\), or sharpen the doubly logarithmic correction for fixed \(q\). Because the motivating preprint is very recent and the transfer is short once its alphabet-sensitive steps are isolated, near-simultaneous discovery and folklore risk remain material.

## References

1. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493v1, 2026. https://arxiv.org/abs/2609.19493
2. Z. Ye, Y. Sun, W. Yu, G. Ge, and O. Elishco, *Codes Correcting Two Bursts of Exactly b Deletions*, arXiv:2408.03113; IEEE Transactions on Information Theory 72(4), 2026. https://arxiv.org/abs/2408.03113
3. W. Song and K. Cai, *Non-binary Two-Deletion Correcting Codes and Burst-Deletion Correcting Codes*, arXiv:2210.14006; IEEE Transactions on Information Theory 69(10), 2023. https://arxiv.org/abs/2210.14006
