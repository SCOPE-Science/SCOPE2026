# Operator norms do not control block scaling of a \(g\)-frame

## Finding
A published bounded-block criterion for scalable \(g\)-frames, later repeated for \(K\)-\(g\)-frames, is false.

Let
\[
H=\ell^2(\mathbb N),
\qquad
V_j=H,
\qquad
K=I.
\]
For the standard basis \(\{e_j\}\), let \(P_j\) be the orthogonal projection onto \(\operatorname{span}\{e_j\}\). Define
\[
\varepsilon_j=2^{-2j},
\qquad
\alpha_j=2^{-j},
\qquad
\Lambda_j=P_j+\varepsilon_jI.
\]
Every \(\Lambda_j\) is positive, diagonal, invertible, and bounded below. Its two spectral values are
\[
1+\varepsilon_j
\quad\text{and}\quad
\varepsilon_j,
\]
so
\[
\|\Lambda_j\|=1+\varepsilon_j
\]
and
\[
m(\Lambda_j)=\varepsilon_j,
\]
where \(m(T)=\inf_{\|x\|=1}\|Tx\|\). In particular,
\[
\liminf_{j\to\infty}\|\Lambda_j\|=1.
\]

Put
\[
E=\sum_{j=1}^{\infty}\varepsilon_j^2=\frac1{15}.
\]
For \(x=(x_k)\in H\),
\[
\sum_{j=1}^{\infty}\|\Lambda_jx\|^2
=
\sum_{k=1}^{\infty}\left((1+\varepsilon_k)^2+\sum_{j\ne k}\varepsilon_j^2\right)|x_k|^2
=
\sum_{k=1}^{\infty}\bigl(1+2\varepsilon_k+E\bigr)|x_k|^2.
\]
Therefore
\[
\frac{16}{15}\|x\|^2
\le
\sum_{j=1}^{\infty}\|\Lambda_jx\|^2
\le
\frac{47}{30}\|x\|^2,
\]
so \(\{\Lambda_j\}\) is a \(g\)-frame.

Now define
\[
D_j=\alpha_j\Lambda_j^{-1}.
\]
Each \(D_j\) is a positive diagonal bounded operator on \(V_j\), and
\[
D_j\Lambda_j=\alpha_jI.
\]
Hence
\[
\sum_{j=1}^{\infty}\|D_j\Lambda_jx\|^2
=
\sum_{j=1}^{\infty}\alpha_j^2\|x\|^2
=
\frac13\|x\|^2.
\]
The scaled family is therefore a tight \(g\)-frame.

On the orthogonal complement of \(e_j\), the operator \(D_j\) has eigenvalue
\[
\frac{\alpha_j}{\varepsilon_j}=2^j,
\]
so
\[
\|D_j\|=2^j.
\]
Consequently the block diagonal operator
\[
D=\bigoplus_{j=1}^{\infty}D_j
\]
is unbounded.

This directly contradicts Proposition 3.1 of Ahmadi--Rahimi. Theorem 24 of Kumar--Malhotra--Khanna repeats the same bounded-block necessity for \(K\)-\(g\)-frames; taking \(K=I\) gives the same contradiction.

## Assumptions and scope
The example uses ordinary \(g\)-frames, which are exactly the special case \(K=I\) of \(K\)-\(g\)-frames.

Every block \(\Lambda_j\) is not merely bounded below but invertible and diagonal. Thus the failure does not depend on a nonclosed range, a kernel, or an off-range action of \(D_j\).

The claim concerns only the asserted global boundedness of the block diagonal scaling operator. The surrounding range-restricted operator criteria are not contradicted.

## Proof
For each \(j\), the operator
\[
\Lambda_j=P_j+\varepsilon_jI
\]
acts by multiplication with \(1+\varepsilon_j\) on \(e_j\) and by multiplication with \(\varepsilon_j\) on every \(e_k\) with \(k\ne j\). Hence
\[
m(\Lambda_j)=\varepsilon_j>0
\]
and
\[
\|\Lambda_j\|=1+\varepsilon_j.
\]

For fixed \(k\), the contribution of the coordinate \(x_k\) to the full \(g\)-frame sum is
\[
(1+\varepsilon_k)^2|x_k|^2
+
\sum_{j\ne k}\varepsilon_j^2|x_k|^2.
\]
Since all terms are nonnegative, Tonelli's theorem permits interchange of the two sums. With
\[
E=\sum_{j=1}^{\infty}16^{-j}=\frac1{15},
\]
the coefficient of \(|x_k|^2\) is
\[
(1+\varepsilon_k)^2+E-\varepsilon_k^2
=
1+2\varepsilon_k+E.
\]
Because
\[
0<\varepsilon_k\le\frac14,
\]
the displayed \(g\)-frame bounds follow.

Next,
\[
D_j=\alpha_j\Lambda_j^{-1}
\]
is positive and diagonal. The product is exactly
\[
D_j\Lambda_j=\alpha_jI.
\]
Since
\[
\sum_{j=1}^{\infty}\alpha_j^2
=
\sum_{j=1}^{\infty}4^{-j}
=
\frac13,
\]
the scaled family is tight.

The norm of \(D_j\) is the larger of
\[
\frac{\alpha_j}{1+\varepsilon_j}
\quad\text{and}\quad
\frac{\alpha_j}{\varepsilon_j}.
\]
Therefore
\[
\|D_j\|
=
2^j\longrightarrow\infty.
\]
A block diagonal operator on the Hilbert direct sum is bounded only if the block norms are uniformly bounded, so \(D\) is unbounded.

The hypothesis
\[
\liminf_j\|\Lambda_j\|>0
\]
does not prevent this behavior because it controls maximal singular values. The lower-bound constants used in the published proofs are instead controlled by minimum moduli:
\[
c_j=m(\Lambda_j)^2=\varepsilon_j^2=2^{-4j}\longrightarrow0.
\]

## Verification
The complete proof of Ahmadi--Rahimi Proposition 3.1 was inspected. It explicitly passes from
\[
\liminf_i\|G_i\|>0
\]
to an eventual uniform positive lower bound for constants \(A_i\) satisfying
\[
A_i\|f\|^2\le\|G_if\|^2.
\]
The implication is invalid because the operator norm and minimum modulus measure opposite spectral extremes.

The complete statement and proof of Kumar--Malhotra--Khanna Theorem 24 were also inspected. It makes the same passage from
\[
\liminf_j\|\Lambda_j\|>0
\]
to a uniform lower bound for the constants \(c_j\), and then concludes that the full block diagonal operator is bounded.

The example above was verified symbolically from the spectra of the diagonal blocks. No finite truncation or numerical approximation is used.

The analysis-range behavior is also explicit:
\[
T_\Lambda^*x=(\Lambda_jx)_j,
\qquad
DT_\Lambda^*x=(\alpha_jx)_j,
\]
and hence
\[
\|DT_\Lambda^*x\|^2=\frac13\|x\|^2.
\]
Thus the scaling is perfectly controlled on the data actually produced by the analysis operator even though \(D\) is unbounded on the ambient direct sum.

## Relationship to prior work
Ahmadi--Rahimi Proposition 3.1 is the earlier \(g\)-frame statement. Kumar--Malhotra--Khanna cite that work and extend the same block-scaling mechanism to \(K\)-\(g\)-frames. The accepted counterexample therefore corrects a shared quantitative step rather than treating the 2024 theorem as unrelated to its predecessor.

The closest published range-sensitive frame results concern boundedness of a scaling composition on an analysis range rather than boundedness of the ambient diagonal multiplier. That distinction is exactly the one exposed here: the composition \(DT_\Lambda^*\) is bounded while \(D\) itself is not.

The natural general criterion is therefore range-restricted. In the ordinary \(g\)-frame paper, the preceding theorem formulates the condition using \(D\) on \(R(T_\Lambda^*)\). The \(K\)-\(g\)-frame paper likewise gives a preceding range-based criterion before adding the false global-boundedness conclusion.

## Limitations
The finding does not claim that every version of a bounded-block criterion is impossible. Additional hypotheses that quantitatively control the action of each block on all relevant directions can force global boundedness.

The result does not reassess the remaining scalability theorems in either paper.

A nonindexed correction or informal author note may contain the same counterexample.

## References
1. A. Ahmadi and A. Rahimi, *Scalability of \(G\)-frames by diagonal operators*, Proceedings of the Institute of Mathematics and Mechanics, National Academy of Sciences of Azerbaijan 47(2) (2021), 215--225, DOI 10.30546/2409-4994.47.2.215.
2. V. Kumar, S. Malhotra and N. Khanna, *Scalability of Generalized Frames for Operators*, Journal of Function Spaces (2024), Article ID 8358987, DOI 10.1155/2024/8358987.
