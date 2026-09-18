# Uniform deep-hole leader multiplicity for ternary Gashkov--Sidel'nikov codes

## Statement

Let \(q=3^m\), and let \(C\) be either of the ternary Gashkov--Sidel'nikov code families treated by Shi, Li, Xia, Helleseth and Ozbudak: the cyclic family for even \(m\ge 2\), or the constacyclic family for odd \(m\ge 3\). Both have length \((q+1)/2\), minimum distance \(5\), and covering radius \(3\).

Write \(K=\mathbb F_{q^2}\) and
\[
T=\{x\in K:N_{K/\mathbb F_q}(x)=1\},\qquad |T|=q+1.
\]
The signed parity-check columns are identified bijectively with \(T\). For a syndrome \(S\in K\) of coset weight three, let \(M(S)\) denote the number of minimum-weight error vectors in that coset, equivalently the number of nearest codewords at distance three from any received word with syndrome \(S\).

Then every deep-hole syndrome satisfies
\[
\boxed{\left|M(S)-\frac q6\right|\le \frac{\sqrt q}{2}+\frac{14}{3}.}
\]
In particular,
\[
M(S)=\frac q6+O(\sqrt q)
\]
uniformly over all weight-three cosets.

Moreover, \(M(S)\) is constant on nonzero norm classes: if \(N(S)=N(S')\ne0\), then
\[
M(S)=M(S').
\]
Thus the farthest syndrome layer is asymptotically almost regular with respect to nearest-neighbor multiplicity, although no claim of complete regularity is made.

## Marked leaders

For a weight-three syndrome \(S\), define
\[
V(S)=\{\beta\in T:\ell_T(S-\beta)=2\},
\]
where \(\ell_T\) is the minimum number of elements of \(T\) whose sum is the argument.

The torus description of the code identifies every minimum error vector of weight three with an unordered representation
\[
S=t_1+t_2+t_3,\qquad t_i\in T.
\]
Minimum representations have no repeated or opposite summands. The two-term theorem of Shi et al. gives a unique unordered pair representing every element of torus length two. Consequently, marking one summand of a minimum triple gives a bijection between
\[
\{(E,\beta): E\text{ is a weight-three leader for }S,\ \beta\text{ is one of its three torus summands}\}
\]
and \(V(S)\). Hence
\[
\boxed{|V(S)|=3M(S).}
\]

## Comparison with the torus search parameter

Shi et al. construct one three-term representation by normalizing the syndrome and splitting into four cases. In the case selected by \(S\), let \(A(S)\) be the number of admissible values of their first base-field search parameter.

Their character-sum calculation shows
\[
\frac{q-3\sqrt q-28}{4}\le A(S).
\]
The same displayed character expansion also gives the complementary upper estimate
\[
A(S)\le \frac{q+3\sqrt q+4}{4}.
\]
Indeed, before removal of the exceptional set, the complete weighted character sum has main term \(q\) and three nonconstant contributions with absolute values bounded by \(1\), \(3\sqrt q\), and \(3\); the restricted weighted sum is \(4A(S)\) and is nonnegative.

The search parameter and marked leaders are related by
\[
\boxed{2A(S)\le |V(S)|\le 2A(S)+12.}
\]
To see the lower bound, each admissible base-field value has exactly two nonzero lifts on the relevant norm conic. They give two distinct possible first torus summands, and the branch quadratic supplies the remaining two summands.

For the upper bound, start instead from \(\beta\in V(S)\) and normalize it to the first torus element in the branch. The branch coordinate map is invertible, so this determines its base-field search parameter. Away from the branch exceptional set, existence of the required two-term remainder forces precisely the square-character condition used by the search. Thus the parameter is admissible. The exceptional set used in each branch has size at most six, and each parameter has at most two norm-conic lifts, so at most twelve marked first summands can escape the admissible count. This argument applies to both cyclic branches and both constacyclic branches.

Combining these estimates with \(|V(S)|=3M(S)\) yields
\[
\frac{q-3\sqrt q-28}{6}
\le M(S)\le
\frac{q+3\sqrt q+28}{6},
\]
which is the stated uniform bound.

## Norm-orbit invariance

If \(N(S)=N(S')\ne0\), then \(\lambda=S'/S\) has norm one, so \(\lambda\in T\). Multiplication by \(\lambda\) permutes \(T\) and sends
\[
S=t_1+t_2+t_3
\]
to
\[
S'=\lambda t_1+\lambda t_2+\lambda t_3.
\]
This is a bijection of minimum torus representations, proving \(M(S)=M(S')\).

## Finite verification

A standalone exhaustive check is included for the \(q=9\) cyclic example. It uses the same model \(\mathbb F_{81}=\mathbb F_3[w]/(w^4+2w^3+2)\), enumerates all \(3^5\) error vectors, and recovers the syndrome-layer distribution
\[
1,\ 10,\ 40,\ 30
\]
for coset weights \(0,1,2,3\), respectively. All thirty deep-hole cosets have exactly two minimum leaders. Each also has exactly six valid marked first torus summands, verifying \(|V(S)|=3M(S)\) in this example.

Run:

```text
python artifacts/verify_q9.py
```

The expected output is recorded in `artifacts/verification.txt`.

## Relation to prior work

Shi, Li, Xia, Helleseth and Ozbudak establish the covering radius, classify syndrome torus length, give the unique two-term decomposition, and construct a three-term decomposition for every deep syndrome. Their branchwise character-sum argument proves that admissible first search parameters have density \(1/4+O(q^{-1/2})\). The result here converts that search-density statement into a uniform theorem about the number of all minimum coset leaders.

The original Gashkov--Sidel'nikov work proves quasi-perfectness by establishing existence of three-term representations and studies ordinary codeword weight spectra. Counting minimum leaders inside each deep coset is a different statistic. Coset-leader multiplicities have been studied for other code families; for example Charpin, Helleseth and Zinoviev determine leader counts for weight-four cosets of a binary BCH code. No novelty is claimed for the general idea of counting leaders.

## Limitations

The estimate is asymptotic and its constants are not claimed to be optimal. It does not determine the exact multiplicity as a function of the syndrome norm, nor the distribution of these multiplicities across norm classes. The theorem concerns the two Gashkov--Sidel'nikov families above and uses the four-branch torus decomposition established for them. It does not imply that the codes are completely regular.

Originality is asserted only to the best of our knowledge. The 1987 paper by Gashkov and Sidel'nikov on these codes and their decoding was identified bibliographically but its theorem text was not inspected here; an equivalent older decoding observation therefore remains a residual risk. A 1992 algebraic-decoding paper for Zetterberg codes is also closely related but was only available at bibliographic level. The motivating 2026 preprint is very recent, so a near-simultaneous observation or later revision is another residual risk.

## References

1. M. Shi, S. Li, Y. Xia, T. Helleseth, F. Ozbudak, *Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes*, arXiv:2609.20402, 2026.
2. S. B. Gashkov, V. M. Sidel'nikov, *Linear ternary quasi-perfect codes correcting double errors*, Problems of Information Transmission 22 (1986).
3. P. Charpin, T. Helleseth, V. A. Zinoviev, *On Cosets of Weight 4 of BCH(2^m,8), m Even, and Exponential Sums*, SIAM Journal on Discrete Mathematics 23 (2008), doi:10.1137/070692649.
