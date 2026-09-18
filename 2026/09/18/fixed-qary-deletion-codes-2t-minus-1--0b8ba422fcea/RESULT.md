# Fixed-alphabet q-ary deletion codes attain the \(2t-1\) coefficient

## Result

Fix integers \(q\ge 2\) and \(t\ge 2\). Let \(\Sigma_q\) be an alphabet of size \(q\), and let
\[
\operatorname{red}^*_{q,t}(n)
   =\min_{\mathcal C\subseteq\Sigma_q^n}
     \left(n-\log_q|\mathcal C|\right),
\]
where the minimum is over codes correcting \(t\) deletions (equivalently, for equal-length codewords, \(t\) insertions and deletions).

Then, as \(n\to\infty\),
\[
\boxed{
\operatorname{red}^*_{q,t}(n)
\le
(2t-1)\log_q n+O_{q,t}(\log_q\log n).
}
\]

For \(q=2\) this is the theorem of En Gad (2026). For every fixed \(q>2\), it answers in the affirmative the fixed-larger-alphabet question explicitly left open in Section 8 of that paper.

Equivalently, for fixed \(q,t\) and all sufficiently large \(n\), there are \(q\)-ary \(t\)-deletion-correcting codes of size
\[
|\mathcal C|
\ge
\frac{q^n}{n^{2t-1}(\log n)^{O_{q,t}(1)}}.
\]

The proof is not a new unrelated construction. It shows that the linear-hashing/subword-spectrum argument of En Gad is alphabet-independent after two binary-specific bookkeeping points are replaced by their \(q\)-ary versions.

## Proof

We give the modifications needed to carry the argument over to \(\Sigma_q\). All vector spaces used by the hash are over \(\mathbb R\); spectra are integer vectors. Thus no finite-field algebra enters the hashing step.

### 1. A constant-density family of unique-substring words

Put
\[
k=2\lceil\log_q n\rceil+2,\qquad L=3(k+1).
\]
Call \(x\in\Sigma_q^n\) \(k\)-unique if its length-\(k\) substrings are pairwise distinct.

For two distinct starting positions \(i<j\), the event that the two length-\(k\) windows agree has probability \(q^{-k}\) for a uniformly random word. This remains true when the windows overlap: equality imposes period \(j-i\) on a string of length \(k+j-i\), leaving exactly \(j-i\) freely chosen symbols. Therefore
\[
\Pr[x\text{ is not }k\text{-unique}]
\le \binom n2q^{-k}
\le \frac18.
\]
Hence the set \(\mathcal W_{n,k}^{(q)}\) of \(k\)-unique \(q\)-ary words has size at least
\[
|\mathcal W_{n,k}^{(q)}|\ge \frac78q^n.
\]

The \(L\)-gram spectrum
\[
R_L(x)\in\mathbb Z^{q^L}
\]
counts occurrences of every length-\(L\) word. The usual \(q\)-ary de Bruijn graph has vertices \(\Sigma_q^{L-1}\) and edges \(\Sigma_q^L\). Exactly as in the binary proof, an \((L-1)\)-unique word traces a simple directed path, so its spectrum is Boolean and determines the word.

The shared-source-letters lemma also uses no binary feature: if two length-\(L-1\) windows in words at edit distance at most one from a fixed \(k\)-unique word are equal, removing the at most two inserted positions and splitting at the at most two deletion jumps leaves at most three intervals of total length at least \(L-3=3k\). One interval has length at least \(k\), and \(k\)-uniqueness identifies its source location. Consequently every word at edit distance at most one from a member of \(\mathcal W_{n,k}^{(q)}\) is \((L-1)\)-unique.

### 2. The only local binary change: bubbles over \(\Sigma_q\)

Let \(d\in\Sigma_q\), \(1\le \rho\le k+1\), and choose words \(A,B\) of length \(L-\rho\) with
\[
A_{\rm last}\ne d,\qquad B_{\rm first}\ne d.
\]
Define
\[
P=A\,d^\rho B,\qquad P'=A\,d^{\rho-1}B.
\]
Thus \(d^\rho\) is a whole maximal \(d\)-run in \(P\). The two de Bruijn walks have the same first and last \(L-1\) letters.

The binary proof writes both boundary symbols as \(1-d\). Equality of the two boundary symbols is never needed. What is needed is only that each boundary symbol differs from \(d\).

Indeed, suppose a vertex window of \(P\), beginning at offset \(a\), equals a vertex window of \(P'\), beginning at offset \(b\). The shared-source-letters lemma gives \(a-b\in\{0,1\}\), exactly as in the binary argument.

If \(a=b>0\), the two compared windows include offset \(L-1\). At that location
\[
P[L-1]=d,\qquad P'[L-1]=P[L]=B_{\rm first}\ne d,
\]
a contradiction. Hence \(a=b=0\).

If \(a=b+1\) before the terminal vertex, let \(j=L-\rho-1\), the last offset of \(A\). Then the compared windows include
\[
P[j+1]=d,\qquad P'[j]=A_{\rm last}\ne d,
\]
again a contradiction. Hence the only common vertices are the two endpoints.

Therefore every separated single insertion or deletion gives the same kind of bubble as in the binary proof: two internally vertex-disjoint paths between common endpoints, with signed spectrum difference in \(\{-1,0,1\}^{q^L}\). For a separated alignment with exactly \(t\) deletions and \(t\) insertions, the \(2t\) local bubbles have disjoint vertex sets and their sum is a rule. The catalogue of rules is still closed under negation, every rule has exactly \(2t\) connected bubble components, and no cancellation occurs between its bubbles.

All support-connectivity arguments used later therefore remain unchanged.

### 3. Exceptional alignments remain thinner by one power of \(n\)

For a fixed \(x\in\mathcal W_{n,k}^{(q)}\), an alignment with \(d\) deletions and \(d\) insertions is specified by its edit anchors and the \(d\) inserted symbols. Thus there are at most
\[
q^d n^{2d}
\]
records. Since \(q,t\) are fixed, alignments with \(d<t\), or with \(d=t\) but with two edits too close to each other or to a boundary, number at most
\[
c_{q,t} L n^{2t-1}
\]
for a constant \(c_{q,t}\).

The random torus hash of En Gad applies verbatim to the \(q^L\)-coordinate integer spectrum. A fixed nonzero spectrum difference passes the equal-label test with probability at most \(2/Q\). Hence the probability that a fixed \(x\) has an equal-label exceptional partner is at most
\[
\frac{2c_{q,t}Ln^{2t-1}}{Q}.
\]

### 4. The witness combinatorics is alphabet-free

After exceptional equal-label conflicts are discarded, every edge of the equal-label conflict graph has a rule as its spectrum difference. The bounded-witness argument depends only on the following facts:

1. a rule is a nonzero integer vector with entries in \(\{-1,0,1\}\);
2. it is the sum of \(2t\) bubbles with pairwise vertex-disjoint supports;
3. bubble supports are connected;
4. equal-length codeword spectra are Boolean.

These properties hold over every alphabet. Consequently, if a component of the conflict graph is not bipartite, it contains a generating witness of \(R\) linearly independent surviving rules with
\[
2\le R\le 1+4tL^2,
\]
and with at most
\[
(2t-1)R
\]
bubble-support components when \(R\le L\), or at most
\[
(2t-1)R+1
\]
when \(R>L\).

### 5. Counting witnesses over a fixed \(q\)-ary alphabet

The recovery/counting lemma also changes only by constant factors.

A bubble header records its orientation, run length \(\rho\), and edited symbol \(d\). The symbol \(d\) now has \(q\) choices instead of two. If a known \(k\)-letter stretch crosses a deletion and must be extended by one letter when transferred between the two paths of a bubble, that one extra letter has \(q\) choices instead of two. No boundary symbol needs to be recorded separately: once the negative local path is known, the header specifies where the symbol \(d\) is inserted or deleted, and hence determines the positive path.

Thus, for fixed \(q,t\), the number of generating witness sets with \(R\) rules and \(c\) bubble-support components is bounded by
\[
n^c(LR)^{a_{q,t}R}
\]
for some constant integer \(a_{q,t}\).

For the one-extra-component case \(R>L\), the binary proof uses \(n\le 2^R\). Here
\[
L\ge \log_q n,\qquad R>L
\]
gives
\[
n\le q^R.
\]
Since \(q\) is fixed, this is again only a constant factor per rule and is absorbed into a sufficiently large power of \(L\).

Hence there is a constant \(b_{q,t}\) such that the number of possible witnesses of size \(R\) at a fixed word is at most
\[
\bigl(n^{2t-1}L^{b_{q,t}}\bigr)^R.
\]

The rules of a witness are linearly independent, so the torus hash makes all \(R\) survive with probability \((2/Q)^R\). Choosing
\[
Q=\left\lceil 8n^{2t-1}L^{b_{q,t}}\right\rceil
\]
therefore makes the probability that a fixed nonexceptional word lies in a nonbipartite component at most
\[
\sum_{R\ge2}4^{-R}=\frac1{12}.
\]

The exceptional-alignment probability is
\[
O_{q,t}(L^{1-b_{q,t}}),
\]
which is at most \(1/4\) for all sufficiently large \(n\). Thus some hash retains a positive constant fraction of \(\mathcal W_{n,k}^{(q)}\) after both discards.

Each retained conflict component is bipartite. Taking the larger side of every component loses at most another factor two. Taking the largest of the \(Q\) hash-label classes loses at most a factor \(Q\). Therefore, for a constant \(c_{q,t}>0\),
\[
|\mathcal C|
\ge c_{q,t}\frac{q^n}{Q}
\ge
\frac{c'_{q,t}q^n}
     {n^{2t-1}(\log n)^{b_{q,t}}}.
\]
Any two distinct members of \(\mathcal C\) with the same label would be adjacent in the conflict graph if they were confusable, contradicting the choice of one bipartition side. Hence \(\mathcal C\) corrects \(t\) insertions/deletions, and therefore \(t\) deletions.

Finally,
\[
\begin{aligned}
\operatorname{red}(\mathcal C)
&=n-\log_q|\mathcal C|\\
&\le \log_q Q+O_{q,t}(1)\\
&=(2t-1)\log_q n+O_{q,t}(\log_q\log n),
\end{aligned}
\]
as claimed.

## Significance and relation to prior work

En Gad proved the coefficient \(2t-1\) for binary deletion codes and explicitly listed extension to a fixed larger alphabet as an open question. The argument above shows that the binary-looking uses of the alphabet are bookkeeping rather than structural: in the local bubble proof, “the opposite bit” can be replaced by arbitrary boundary symbols unequal to the edited symbol; in the counting proof, the larger finite alphabet contributes only constant choices per local instruction.

Earlier \(q\)-ary work includes explicit two-deletion constructions with larger leading redundancy. For example, Liu, Tjuawinata and Xing give fixed-\(q\) explicit two-deletion codes with \(5\log n+O(\log\log n)\) bits of redundancy. The present result is existential, not an efficient construction, and does not address the explicit-code question.

## Limitations

- The alphabet size \(q\) is fixed as \(n\to\infty\). The proof is not uniform for growing \(q\); the constants in the local-description count may depend on \(q\).
- The result does not improve the binary theorem and does not lower the coefficient below \(2t-1\).
- The construction remains probabilistic and does not supply efficient encoding or decoding.
- Originality is asserted only to the best of our knowledge. The motivating preprint is very recent, so simultaneous or not-yet-indexed work is a real residual risk.

## References

1. E. En Gad, “Polynomially larger deletion codes by linear hashing of substring counts,” arXiv:2609.19493, 2026. https://arxiv.org/abs/2609.19493
2. S. Liu, I. Tjuawinata and C. Xing, “Explicit Construction of q-ary 2-deletion Correcting Codes with Low Redundancy,” IEEE Transactions on Information Theory 70(6), 4093–4101, 2024; arXiv:2306.02868. https://arxiv.org/abs/2306.02868
3. N. Alon, G. Bourla, B. Graham, X. He and N. Kravitz, “Logarithmically Larger Deletion Codes of All Distances,” IEEE Transactions on Information Theory 70(1), 125–130, 2024; arXiv:2209.11882. https://arxiv.org/abs/2209.11882
