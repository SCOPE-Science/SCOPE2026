# A stationary occupancy inequality for variable-length non-overlapping codes

## Statement

Let \(S\) be a finite variable-length non-overlapping code over a finite
alphabet \(\Sigma\), in the sense that

1. no nonempty proper prefix of a codeword is a suffix of any codeword
   (including itself), and
2. no codeword is a subword of a distinct codeword.

Let \((X_i)_{i\in\mathbb Z}\) have any stationary probability law on
\(\Sigma^{\mathbb Z}\).  For a word \(w=w_1\cdots w_\ell\), write
\[
\mu[w]=\Pr(X_1\cdots X_\ell=w).
\]
Then
\[
\boxed{\sum_{w\in S}|w|\,\mu[w]\le 1.}
\tag{1}
\]
No independence, Markov property, or ergodicity is required.

For the uniform iid law on a \(q\)-letter alphabet, (1) becomes the
synchronization-weighted Kraft inequality
\[
\boxed{\sum_{w\in S}|w|q^{-|w|}\le 1.}
\tag{2}
\]
For an iid law with letter probabilities \(p_a\), it gives the
composition-sensitive family
\[
\boxed{\sum_{w\in S}|w|\prod_{j=1}^{|w|}p_{w_j}\le 1.}
\tag{3}
\]

## Proof of the stationary inequality

For each \(w\in S\), \(|w|=\ell\), and each offset
\(r\in\{0,\ldots,\ell-1\}\), let \(E_{w,r}\) be the event that an occurrence
of \(w\) covers coordinate \(0\) with coordinate \(0\) in offset \(r\):
\[
E_{w,r}=\{X_{-r}\cdots X_{\ell-r-1}=w\}.
\]
Stationarity gives \(\Pr(E_{w,r})=\mu[w]\).

The events \(E_{w,r}\) are pairwise disjoint.  Indeed, two distinct
occurrences that both cover coordinate \(0\) have overlapping occurrence
intervals.  If neither interval contains the other, their intersection is a
nonempty proper suffix of the left-hand codeword and a nonempty proper prefix
of the right-hand codeword, contradicting condition 1.  If one interval is
strictly contained in the other, the shorter codeword occurs as a subword of
the longer one, contradicting condition 2.  Equal intervals force equal words
and the same offset, hence the same event.

Therefore countable additivity on this finite family gives
\[
1\ge \Pr\!\left(\bigcup_{w\in S}\bigcup_{r=0}^{|w|-1}E_{w,r}\right)
 =\sum_{w\in S}\sum_{r=0}^{|w|-1}\Pr(E_{w,r})
 =\sum_{w\in S}|w|\mu[w],
\]
which proves (1).

## Consequences for average codeword length

Assume now that \(|\Sigma|=q\ge2\) and use the uniform iid law.  Write
\(M=|S|\), let the codeword lengths be \(\ell_1,\ldots,\ell_M\), and set
\[
L=\frac1M\sum_{i=1}^M\ell_i,
\qquad
G=\left(\prod_{i=1}^M\ell_i\right)^{1/M}.
\]
All lengths satisfy \(\ell_i\ge2\).  Applying AM--GM to (2) gives
\[
1\ge\sum_{i=1}^M \ell_iq^{-\ell_i}
 \ge MGq^{-L},
\]
so
\[
\boxed{L\ge \log_q(MG)\ge \log_q(2M).}
\tag{4}
\]
Thus the synchronization constraint yields more than the ordinary
\(L\ge\log_q M\) prefix-code entropy inequality.

There is also a stronger mean-length consequence.  Put
\(a_k=kq^{-k}\) for integers \(k\ge2\).  A direct calculation gives
\[
a_k-2a_{k+1}+a_{k+2}
 =\frac{(q-1)(k(q-1)-2)}{q^{k+2}}\ge0.
\tag{5}
\]
Hence the piecewise-linear interpolation \(\psi_q\) with
\(\psi_q(k)=a_k\) is convex.  Since the lengths are integer-valued, Jensen's
inequality and (2) imply
\[
\boxed{M\psi_q(L)\le1.}
\tag{6}
\]
If \(k=\lfloor L\rfloor\), then \(a_k\ge a_{k+1}\), so
\(\psi_q(L)\ge a_{\lceil L\rceil}\ge Lq^{-L-1}\).  Consequently every
\(q\ge2\) satisfies
\[
\boxed{q^{L+1}\ge ML.}
\tag{7}
\]
For fixed \(q\) and \(M\to\infty\), this yields
\[
\boxed{L\ge \log_q M+\log_q\log_q M-O_q(1).}
\tag{8}
\]

For \(q\ge3\), the continuous function \(f(x)=xq^{-x}\) is convex for
\(x\ge2\), because
\[
f''(x)=q^{-x}\ln q\,(x\ln q-2)\ge0.
\]
Jensen therefore sharpens (7) to
\[
\boxed{q^L\ge ML,}
\tag{9}
\]
and the solution of \(L-\log_q L\ge\log_q M\) gives the more precise
fixed-alphabet asymptotic
\[
\boxed{L\ge \log_q M+\log_q\log_q M+o(1)}
\qquad(q\ge3).
\tag{10}
\]

## Relation to prior bounds

Wang and Wang studied the minimum average length of variable-length
non-overlapping codes and obtained a prefix-code lower bound together with an
asymptotic \(n-2\) statement in a regime where \(q\to\infty\) and the
cardinality lies between consecutive fixed-length maxima.  Equations (6)--(10)
address a different and complementary regime: for every fixed alphabet, the
non-overlap condition contributes a logarithmic-in-logarithm term beyond the
basic entropy scale as the code cardinality grows.

The uniform inequality (2) is compatible with the avoidance generating
function used by Wang and Wang in their earlier work, and can also be recovered
from that framework by a short convexity/root argument.  The stationary form
(1), the arbitrary-source specialization (3), and the average-length
consequences above do not require generating functions.

Shen, Shangguan, Lin and Ge obtained a stronger cardinality bound when only the
maximum codeword length \(n\) is prescribed.  This record does not improve that
maximum-cardinality result.  In particular, the fixed-length specialization of
(2), \(M\le q^n/n\), is only the elementary cyclic-packing-scale bound.

## Limitations

The originality claim is to the best of our knowledge.  The occupancy proof is
elementary, and no novelty is claimed for the general principle that disjoint
cylinder events have total probability at most one.  The claimed contribution
is the explicit stationary inequality for this variable-length non-overlap
condition and its source-sensitive and average-length consequences.

Older literature uses several partially overlapping terms, including
comma-free, self-synchronizing, cross-bifix-free and solid codes.  Some older
variable-length comma-free papers were not available in full text, so an
unlocated equivalent measure-theoretic formulation remains the main
originality risk.

## References

1. G. Wang and Q. Wang, *On the maximum size of variable-length non-overlapping codes*, Designs, Codes and Cryptography 93 (2025), 871--878. DOI: 10.1007/s10623-024-01445-3. Preprint: https://arxiv.org/abs/2402.18896
2. G. Wang and Q. Wang, *Q-ary non-overlapping codes: a generating function approach*, IEEE Transactions on Information Theory 68 (2022). Preprint: https://arxiv.org/abs/2108.06934
3. Y. Shen, C. Shangguan, Z. Lin and G. Ge, *Constrained coding upper bounds via Goulden--Jackson cluster theorem*, https://arxiv.org/abs/2407.16449
4. S. Bilotta, *Variable-length Non-overlapping Codes*, IEEE Transactions on Information Theory 63 (2017), 6530--6537. DOI: 10.1109/TIT.2017.2742506
5. J. A. Llewellyn, *The Construction of Variable-length Comma-Free Codes*, The Computer Journal 28 (1985), 379--390. DOI: 10.1093/comjnl/28.4.379
