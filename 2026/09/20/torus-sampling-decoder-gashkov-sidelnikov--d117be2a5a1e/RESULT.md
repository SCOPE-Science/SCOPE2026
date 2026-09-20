# Elliptic-curve control of direct torus sampling for Gashkov-Sidel'nikov decoding

## Result

Let \(q=3^m\), let \(K=\mathbb F_{q^2}\), and let
\[
\mathcal T=\{x\in K^*:N_{K/\mathbb F_q}(x)=1\}.
\]
Shi, Li, Xia, Helleseth and Ozbudak (2026) identify \(\mathcal T\) with the signed
parity-check columns of both original ternary Gashkov-Sidel'nikov families.  For a
syndrome \(S\), the coset weight is therefore its minimum additive length
\(\ell_{\mathcal T}(S)\).  Their direct weight-three construction searches for a
\(\beta\in\mathcal T\) for which \(S-\beta\) has additive length two; the cited
paper proves existence but gives only a worst-case bound of \(q+1\) torus probes.

The following theorem gives the exact number of successful probes.

**Theorem.**  Suppose \(\ell_{\mathcal T}(S)=3\), put
\(n=N(S)\in\mathbb F_q^*\), and define
\[
M(S)=\#\{\beta\in\mathcal T:\ell_{\mathcal T}(S-\beta)=2\}.
\]
Let \(C_n\) be the smooth projective model of
\[
C_n:\qquad
Y^2=X(X-1)\bigl((n+1-X)^2-n\bigr).
\]
Then \(C_n\) is a genus-one curve over \(\mathbb F_q\) and
\[
\boxed{M(S)=\frac{\#C_n(\mathbb F_q)}2.}
\]
Consequently
\[
\boxed{\left|M(S)-\frac{q+1}{2}\right|\le \sqrt q.}
\]
In particular, \(M(S)\) depends only on \(N(S)\).

Thus a uniformly random \(\beta\in\mathcal T\) succeeds with probability
\[
\boxed{
\frac12-\frac{\sqrt q}{q+1}
\le
\Pr[\ell_{\mathcal T}(S-\beta)=2]
\le
\frac12+\frac{\sqrt q}{q+1}.
}
\]
For every nontrivial original Gashkov-Sidel'nikov code, \(q\ge9\).  Independent
uniform sampling with replacement therefore gives a Las Vegas maximum-likelihood
decoder whose expected number of torus probes on every weight-three syndrome is
\[
\boxed{
\frac{q+1}{M(S)}
\le
\frac{2(q+1)}{q+1-2\sqrt q}
=2+O(q^{-1/2}).
}
\]
A uniform torus element can be sampled directly by choosing a coordinate position
uniformly and then one of the two nonzero ternary error values uniformly, using the
signed-column bijection from the cited paper.  Once a successful \(\beta\) is found,
the remaining two summands are the unique unordered roots of the paper's quadratic
for \(S-\beta\), and the inverse signed-column map returns the corresponding error
vector.  The statement concerns the number of candidate probes; finite-field
arithmetic costs are unchanged.

There is also an exact multiplicity consequence.  Let \(L(S)\) be the number of
minimum-weight error vectors of weight three having syndrome \(S\).  Then
\[
\boxed{L(S)=\frac{M(S)}3=\frac{\#C_n(\mathbb F_q)}6}
\]
and hence
\[
\boxed{
\left|L(S)-\frac{q+1}{6}\right|\le\frac{\sqrt q}{3}.
}
\]
Thus every weight-three coset has \(q/6+O(\sqrt q)\) maximum-likelihood error
patterns.

## Proof

Because \(\ell_{\mathcal T}(S)=3\), one has \(S\notin\mathcal T+\mathcal T\), so
\(n=N(S)\ne0,1\).  For \(\beta\in\mathcal T\), set
\[
a=N(S-\beta).
\]
Again by the length-three assumption, \(a\ne0,1\).  The length-two criterion in
Shi et al. gives
\[
\ell_{\mathcal T}(S-\beta)=2
\quad\Longleftrightarrow\quad
\chi(1-a^{-1})=-1.
\]
Since \(a\ne0,1\),
\[
\chi(1-a^{-1})=\chi(a(a-1)),
\]
where \(\chi\) denotes the quadratic character of \(\mathbb F_q\), extended by
\(\chi(0)=0\).  Therefore
\[
M(S)=\frac12\sum_{\beta\in\mathcal T}
\bigl(1-\chi(a(a-1))\bigr).
\tag{1}
\]

We now count the fibers of \(\beta\mapsto N(S-\beta)\).  Since
\(\bar\beta=\beta^{-1}\) on \(\mathcal T\), the equation
\(N(S-\beta)=a\) is equivalent to
\[
\bar S\,\beta^2-(n+1-a)\beta+S=0.
\tag{2}
\]
Its discriminant lies in \(\mathbb F_q\) and, in characteristic three, is
\[
\Delta_n(a)=(n+1-a)^2-4n=(n+1-a)^2-n.
\]
The number of roots of (2) lying in \(\mathcal T\) is
\[
1-\chi(\Delta_n(a)).
\tag{3}
\]
Indeed, if \(\Delta_n(a)\) is a nonsquare, its two square roots in \(K\) are
conjugate negatives and the two quadratic roots have norm one; if the discriminant
vanishes there is one double torus root; and a nonzero square discriminant gives no
torus root.  This also recovers the at-most-two fiber bound used in the source
paper.

Let
\[
J_n=\sum_{a\in\mathbb F_q}
\chi\!\left(a(a-1)\bigl((n+1-a)^2-n\bigr)\right).
\]
Using (3) and the standard quadratic character identity
\(\sum_a\chi(a(a-1))=-1\),
\[
\begin{aligned}
\sum_{\beta\in\mathcal T}\chi(a(a-1))
&=\sum_{a\in\mathbb F_q}
(1-\chi(\Delta_n(a)))\chi(a(a-1))\\
&=-1-J_n.
\end{aligned}
\]
Substitution into (1) gives
\[
M(S)=\frac{q+2+J_n}{2}.
\tag{4}
\]

The quartic
\[
F_n(X)=X(X-1)((n+1-X)^2-n)
\]
is squarefree when \(n\ne0,1\): the quadratic factor is separable, and its
intersection with \(X(X-1)\) occurs only when \(n=1\).  Hence its smooth
projective model has genus one.  The quartic has square leading coefficient, so
there are two \(\mathbb F_q\)-rational points at infinity.  Therefore
\[
\#C_n(\mathbb F_q)=q+J_n+2=2M(S),
\]
which proves the exact identity.  Hasse's bound
\[
|\#C_n(\mathbb F_q)-(q+1)|\le2\sqrt q
\]
gives the stated uniform estimate.

Finally, for a successful first summand \(\beta\), the residual length-two
representation is unique up to order by the source paper's quadratic description.
Conversely, every minimum three-term decomposition has three choices for the first
summand.  Minimum decompositions contain neither equal nor opposite summands, so
under the signed-column bijection they correspond bijectively to weight-three
error vectors with distinct coordinate positions.  Thus \(M(S)=3L(S)\), proving
the leader-multiplicity formula and its Hasse bound.

## Relation to the recent decoder

The 2026 paper proves the exact additive-length classification, the signed-column
bijection, and a direct sequential construction that may inspect all \(q+1\) torus
elements in the worst case.  Its two structured conic procedures have an
asymptotic admissible-parameter density of \(1/4\), giving \(4+o(1)\) expected
uniform parameter trials.  The theorem above analyzes the paper's simpler direct
torus search itself: its success density is \(1/2+O(q^{-1/2})\) for every
weight-three syndrome, with the exact density controlled by a genus-one point
count.  No claim is made that the per-probe arithmetic cost is lower than in the
structured constructions.

## Verification

`artifacts/verify_torus_random_decoder.py` independently enumerates
\(\mathbb F_{q^2}\), the norm-one torus, all exact length-three syndromes, and all
three-element torus subsets for \(q=9,27,81\).  It checks
\[
2M(S)=q+2+J_{N(S)},
\]
the Hasse bound, divisibility of \(M(S)\) by three, and the equality between
\(M(S)/3\) and the number of unordered three-term decompositions.  The recorded
output is in `artifacts/verification.txt` and reports `PASS`.

## Limitations

The result applies to the original ternary Gashkov-Sidel'nikov families through
their norm-one-torus signed-column model.  It does not by itself extend the same
half-density law to generalized Zetterberg codes over arbitrary odd
characteristic.  It improves the candidate-count analysis of the direct
weight-three search, not the asymptotic bit complexity of finite-field arithmetic.
The elliptic curve varies with \(N(S)\); no attempt is made here to classify its
isogeny classes or determine its Frobenius trace in closed form.

## References

1. M. Shi, S. Li, Y. Xia, T. Helleseth, F. Ozbudak, “Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes,” arXiv:2609.20402, 2026. https://arxiv.org/abs/2609.20402
2. M. Shi, S. Li, T. Helleseth, F. Ozbudak, “Determining the Covering Radius of All Generalized Zetterberg Codes in Odd Characteristic,” IEEE Trans. Inf. Theory 71(5), 3602–3613, 2025. https://doi.org/10.1109/TIT.2025.3544025
3. S. M. Dodunekov, J. E. M. Nilsson, “Algebraic Decoding of the Zetterberg Codes,” IEEE Trans. Inf. Theory 38(5), 1570–1573, 1992.
