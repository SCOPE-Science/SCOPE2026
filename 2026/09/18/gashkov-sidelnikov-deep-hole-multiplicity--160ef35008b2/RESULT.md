# A sharpened explicit deep-hole leader discrepancy for ternary Gashkov--Sidel'nikov codes

## Statement

Let \(q=3^m\), and let \(C\) be either ternary Gashkov--Sidel'nikov family considered by Shi, Li, Xia, Helleseth and Özbudak: the cyclic family for even \(m\ge2\), or the constacyclic family for odd \(m\ge3\). Both have length \((q+1)/2\), minimum distance \(5\), and covering radius \(3\).

Put \(K=\mathbb F_{q^2}\) and
\[
T=\{x\in K:N_{K/\mathbb F_q}(x)=1\},\qquad |T|=q+1.
\]
The signed parity-check columns are in bijection with \(T\). For a syndrome \(S\) of coset weight three, let \(M(S)\) be the number of minimum-weight error vectors in that coset, equivalently the number of nearest codewords at distance three from a word with syndrome \(S\).

Then
\[
\boxed{\left|M(S)-\frac q6\right|\le \frac{\sqrt q}{2}+\frac{14}{3}.}
\]
Moreover, if \(N(S)=N(S')\ne0\), then
\[
M(S)=M(S').
\]

The novelty claim is deliberately limited to the explicit sharpened discrepancy estimate and its transparent marked-leader derivation. The older 1986 proof of quasi-perfectness already contains a character-sum count on the \(q+O(\sqrt q)\) scale for the underlying three-term conic system, so this record does **not** claim that the qualitative asymptotic \(M(S)=q/6+O(\sqrt q)\) is new.

## Marked leaders

For a weight-three syndrome define
\[
V(S)=\{\beta\in T:\ell_T(S-\beta)=2\},
\]
where \(\ell_T\) is minimum additive length with respect to \(T\).

Shi et al. prove that every length-two element has a unique unordered two-term representation in \(T\). A minimum three-term representation has neither repeated nor opposite summands. Hence marking one summand of a minimum triple gives a bijection between marked minimum leaders and \(V(S)\), so
\[
\boxed{|V(S)|=3M(S).}
\]

## Search parameters and all marked leaders

Fix the one of the four conic normalizations selected by the syndrome in Algorithms 1 and 2 of Shi et al., and let \(A(S)\) be the number of admissible values of the branch's first base-field parameter.

In each branch their weighted character sum has the form
\[
4A(S)=\sum_{u\in\mathbb F_q\setminus E}
(1\pm\chi(g(u)))(1+\chi(\Delta(u))),
\]
with \(|E|\le6\). The corresponding complete sum over \(\mathbb F_q\) has main term \(q\), while its three nonconstant character sums have absolute values at most \(1\), \(3\sqrt q\), and \(3\). Therefore
\[
\frac{q-3\sqrt q-28}{4}\le A(S)\le
\frac{q+3\sqrt q+4}{4}.
\]
The lower bound is the branchwise estimate recorded by Shi et al.; the upper bound follows from the same expansion because the deleted weighted summands are nonnegative.

There is also a uniform comparison with *all* marked leaders:
\[
\boxed{2A(S)\le |V(S)|\le 2A(S)+12.}
\]

For the lower bound, every admissible base-field parameter has exactly two lifts on the relevant norm conic. Each lift gives a distinct possible first torus summand; the quadratic branch equation then supplies the remaining pair. Its two roots only exchange the second and third summands.

Conversely, take \(\beta\in V(S)\) and normalize it to the branch's first torus element. The conic coordinate map is invertible. Outside the branch exceptional set \(E=\{0\}\cup\{A\Delta=0\}\), the norm equation forces exactly the square/nonsquare condition imposed on the first parameter, and existence of the distinct two-term remainder forces the second-coordinate quadratic to have a nonzero square discriminant. Thus the parameter is admissible. At most six exceptional parameter values remain, and each has at most two conic lifts, so at most twelve marked first summands can escape the admissible count.

Combining \(|V|=3M\) with these inequalities gives
\[
\frac{q-3\sqrt q-28}{6}\le M(S)\le
\frac{q+3\sqrt q+28}{6},
\]
which is the displayed discrepancy estimate.

## Norm-orbit invariance

If \(N(S)=N(S')\ne0\), then \(\lambda=S'/S\) has norm one. Multiplication by \(\lambda\) permutes \(T\) and bijects the minimum three-term representations of \(S\) with those of \(S'\). Hence \(M(S)=M(S')\).

## Finite verification

The archived `artifacts/verify_q9.py` exhaustively checks the \(q=9\) cyclic example. It recovers syndrome-layer counts \(1,10,40,30\); every one of the thirty deep cosets has exactly two minimum leaders and six marked first summands, so \(|V(S)|=3M(S)\) there.

## Relation to prior work

Gashkov and Sidel'nikov's 1986 proof of quasi-perfectness reduces three-term representation to a conic system and then counts solutions of an eliminated system by
\[
N=\sum_x (1-\chi(x^2-1))(1+\chi(\Delta(x))),
\]
obtaining a \(q+O(\sqrt q)\) estimate (their displayed bound is centered at \(q+1\) with an \(8\sqrt q\) error term). That counting argument substantially anticipates a uniform multiplicity asymptotic, even though it is used there to prove existence rather than stated as the present nearest-neighbor multiplicity theorem. Accordingly, this record no longer presents \(q/6+O(\sqrt q)\) itself as a new phenomenon.

Shi, Li, Xia, Helleseth and Özbudak (2026) give the modern signed-column/norm-one-torus model, the unique two-term decomposition, the complete coset-weight distribution, and four explicit conic decoding branches. Their branchwise character-sum estimates supply the sharper ingredients used above.

Dodunekov and Nilsson's 1992 paper on binary Zetterberg codes was inspected during the independent audit. It provides an algebraic 0/1/2/3-error decision-and-location algorithm, not a count of all minimum leaders in deep cosets. The 1987 FCT conference paper of Gashkov and Sidel'nikov was located bibliographically but its theorem text was not obtained; it remains a priority limitation.

## Limitations

- The constants are not claimed optimal.
- No exact formula for \(M(S)\) as a function of the syndrome norm is obtained.
- No complete-regularity claim is made.
- The qualitative \(q/6+O(\sqrt q)\) scale is not claimed as new because the 1986 character-sum proof already contains closely related solution-count asymptotics.
- The 1987 FCT conference paper could not be inspected at theorem level.

## References

1. M. Shi, S. Li, Y. Xia, T. Helleseth, F. Özbudak, *Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes*, arXiv:2609.20402 (2026).
2. I. B. Gashkov, V. M. Sidel'nikov, *Linear Ternary Quasi-perfect Codes Correcting Double Errors*, Problems of Information Transmission 22 (1986), 284--288; Russian original available from Math-Net.Ru, Mi ppi957.
3. S. M. Dodunekov, J. E. M. Nilsson, *Algebraic Decoding of the Zetterberg Codes*, IEEE Transactions on Information Theory 38 (1992), 1570--1573, doi:10.1109/18.149509.
