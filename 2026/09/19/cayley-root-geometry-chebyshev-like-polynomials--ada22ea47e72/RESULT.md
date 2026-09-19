# Cayley root geometry and an exact companion discriminant for two Chebyshev-like polynomial families

## Statement

Let \(p_n,q_n\) be the reciprocal polynomial families introduced by Dilcher, Kim and Stolarsky in arXiv:2607.16940. For \(n\ge 1\), set
\[
P_n(u)=\sum_{k=0}^n (k+1)u^k,\qquad
Q_n(u)=1+u+\cdots+u^{n-1}+(n+2)u^n,
\]
and use the Cayley coordinate
\[
w=\frac{z+1}{z-1},\qquad u=w^2.
\]
Then
\[
\boxed{
p_n(z)=(z-1)^{2n}P_n\!\left(\left(\frac{z+1}{z-1}\right)^2\right)
}
\]
and
\[
\boxed{
q_n(z)=\frac{(z-1)^{2n}}2
Q_n\!\left(\left(\frac{z+1}{z-1}\right)^2\right).
}
\]

These reductions have three consequences.

### 1. Hurwitz stability and explicit finite-\(n\) zero regions

Every zero of both \(p_n\) and \(q_n\) lies in the open left half-plane.

More precisely, every zero \(z\) of \(p_n\) satisfies
\[
\frac1{\sqrt2}\le
\left|\frac{z+1}{z-1}\right|
\le \sqrt{\frac n{n+1}},
\]
equivalently,
\[
|z+3|\ge 2\sqrt2,\qquad
|z+(2n+1)|\le 2\sqrt{n(n+1)}.
\]
In particular,
\[
\operatorname{Re}z\le
-(\sqrt{n+1}-\sqrt n)^2<0.
\]

Every zero \(z\) of \(q_n\) satisfies
\[
\frac1{\sqrt{n+2}}\le
\left|\frac{z+1}{z-1}\right|<1,
\]
equivalently,
\[
|z+\tfrac{n+3}{n+1}|
\ge \frac{2\sqrt{n+2}}{n+1},
\qquad
\operatorname{Re}z<0.
\]

### 2. Exact discriminant of the companion family

The companion discriminant is
\[
\boxed{
\operatorname{Disc}(q_n)
=
(-1)^n\,2^{4n(n-1)}(n+2)(n+1)^{2n-2}
\left(\frac{(n+2)^n+n^n}{2}\right)^2.
}
\]
Consequently every zero of \(q_n\) is simple.

The extra factor
\[
\left(\frac{(n+2)^n+n^n}{2}\right)^2
\]
explains why the companion discriminants do not have the same small-prime-factor form as the formula for \(\operatorname{Disc}(p_n)\) in the source paper.

### 3. Cauchy-law zero distribution

Let
\[
\nu_n^{(p)}=\frac1{2n}\sum_{p_n(z)=0}\delta_z,\qquad
\nu_n^{(q)}=\frac1{2n}\sum_{q_n(z)=0}\delta_z,
\]
with roots counted with multiplicity. Then both empirical zero measures converge weakly on \(\mathbb C\) to the standard Cauchy measure supported on the imaginary axis:
\[
\boxed{
\nu_n^{(p)},\,\nu_n^{(q)}
\Longrightarrow \mu_{\mathrm C},
\qquad
\int_{\mathbb C}\varphi\,d\mu_{\mathrm C}
=
\int_{\mathbb R}\varphi(it)\frac{dt}{\pi(1+t^2)}
}
\]
for every bounded continuous \(\varphi:\mathbb C\to\mathbb C\).

In the intermediate \(u\)-plane, the zero arguments of both \(P_n\) and \(Q_n\) have Erdős--Turán discrepancy
\[
O\!\left(\sqrt{\frac{\log n}{n}}\right),
\]
while for every fixed \(0<\delta<1\), at most \(O_\delta(\log n)\) of their \(n\) zeros can satisfy \(|u|\le 1-\delta\).

## Context

Dilcher--Kim--Stolarsky define \(p_n\) by a modified Chebyshev generating function and introduce \(q_n\) as its companion. Their equation (2.4) gives the displayed Cayley representation of \(p_n\), and Proposition 4.1 gives
\[
q_n(z)=p_n(z)-(z^2+1)p_{n-1}(z).
\]
They compute \(\operatorname{Disc}(p_n)\) in Proposition 5.4. Immediately after that computation they note that no analogous identity with only small prime factors seems to occur for \(\operatorname{Disc}(q_n)\). The conclusions above give a zero-geometric interpretation of both families and an exact closed form for that missing companion discriminant.

## Proof

### A. The two Cayley reductions

The source formula
\[
p_n(z)=(z-1)^{2n}\sum_{k=0}^n(k+1)
\left(\frac{z+1}{z-1}\right)^{2k}
\]
is exactly the first identity.

For the companion relation, write \(u=((z+1)/(z-1))^2\). Since
\[
\frac{z^2+1}{(z-1)^2}=\frac{u+1}{2},
\]
we obtain
\[
q_n(z)
=(z-1)^{2n}
\left(P_n(u)-\frac{u+1}{2}P_{n-1}(u)\right).
\]
A coefficient comparison gives
\[
2P_n(u)-(u+1)P_{n-1}(u)
=
1+u+\cdots+u^{n-1}+(n+2)u^n=Q_n(u),
\]
which proves the second identity.

### B. Zero localization and Hurwitz stability

The Eneström--Kakeya annulus theorem applied to
\[
P_n(u)=1+2u+\cdots+(n+1)u^n
\]
gives
\[
\frac12\le |u|\le \frac n{n+1}.
\]
For \(Q_n\), it gives
\[
\frac1{n+2}\le |u|\le 1.
\]
The outer inequality is actually strict. If \(Q_n(u)=0\) and \(|u|\ge1\), then
\[
(n+2)|u|^n
=
|1+u+\cdots+u^{n-1}|
\le n|u|^{n-1},
\]
which is impossible.

Taking square roots yields the stated bounds for \(|w|\). The inverse Cayley map is
\[
z=\frac{w+1}{w-1},
\]
and
\[
\operatorname{Re}z
=
\frac{|w|^2-1}{|w-1|^2}.
\]
Thus \(|w|<1\) is equivalent to \(\operatorname{Re}z<0\), proving Hurwitz stability.

The stated Euclidean disks are just the Apollonius-circle form of
\[
|z+1|\le \rho |z-1|
\quad\text{or}\quad
|z+1|\ge \rho |z-1|.
\]
For \(p_n\), \(\rho^2=n/(n+1)\) gives center \(-(2n+1)\), radius \(2\sqrt{n(n+1)}\), while \(\rho^2=1/2\) gives center \(-3\), radius \(2\sqrt2\). For \(q_n\), \(\rho^2=1/(n+2)\) gives center \(-(n+3)/(n+1)\), radius \(2\sqrt{n+2}/(n+1)\).

### C. The companion discriminant

Write
\[
R_n(u)=(1-u)Q_n(u)
=
1+(n+1)u^n-(n+2)u^{n+1}.
\]
If \(\alpha_1,\ldots,\alpha_n\) are the roots of \(Q_n\), counted with multiplicity, then at a root
\[
Q_n'(\alpha)
=
\frac{R_n'(\alpha)}{1-\alpha}
=
(n+1)\alpha^{n-1}
\frac{n-(n+2)\alpha}{1-\alpha}.
\]
The elementary products are
\[
\prod_{j=1}^n\alpha_j=\frac{(-1)^n}{n+2},
\qquad
\prod_{j=1}^n(1-\alpha_j)=\frac{2(n+1)}{n+2}.
\]
If \(c=n/(n+2)\), then
\[
\prod_{j=1}^n\bigl(n-(n+2)\alpha_j\bigr)
=(n+2)^{n-1}Q_n(c)
=\frac{(n+2)^n+n^n}{2}.
\]
Hence
\[
\prod_{j=1}^n Q_n'(\alpha_j)
=
\frac{(n+1)^{n-1}}{4(n+2)^{n-2}}
\bigl((n+2)^n+n^n\bigr),
\]
and therefore
\[
\boxed{
\operatorname{Disc}(Q_n)
=
(-1)^{n(n-1)/2}
\frac{(n+1)^{n-1}}4
\bigl((n+2)^n+n^n\bigr).
}
\]

Now set \(H_n(w)=Q_n(w^2)\). Pairing the roots
\(\pm\sqrt{\alpha_j}\) in the derivative formula for the discriminant gives
\[
\operatorname{Disc}(H_n)
=
(-1)^n4^n(n+2)\operatorname{Disc}(Q_n)^2.
\]
Finally use the following standard Möbius covariance. If \(H\) has degree \(m\) and
\[
G(z)=\kappa(cz+d)^m
H\!\left(\frac{az+b}{cz+d}\right),
\]
then
\[
\operatorname{Disc}(G)
=
\kappa^{2m-2}(ad-bc)^{m(m-1)}
\operatorname{Disc}(H).
\]
Here \(m=2n\), \(\kappa=1/2\), and
\[
(a,b,c,d)=(1,1,1,-1),\qquad ad-bc=-2.
\]
Substitution and simplification give
\[
\operatorname{Disc}(q_n)
=
(-1)^n\,2^{4n(n-1)}(n+2)(n+1)^{2n-2}
\left(\frac{(n+2)^n+n^n}{2}\right)^2.
\]

As a consistency check, the identical route applied to
\(P_n\) gives
\[
\operatorname{Disc}(P_n)
=
(-1)^{n(n-1)/2}
2(n+1)^{n-2}(n+2)^{n-1},
\]
and after the squared Cayley transform it reproduces exactly the source-paper formula
\[
\operatorname{Disc}(p_n)
=
(-1)^n2^{4n^2+2}(n+1)^{2n-3}(n+2)^{2n-2}.
\]

### D. Limiting zero measure

For a degree-\(n\) polynomial \(A(u)=\sum_{k=0}^n a_k u^k\), the classical Erdős--Turán theorem bounds angular discrepancy by a constant multiple of
\[
\sqrt{
\frac1n
\log\frac{\max_{|u|=1}|A(u)|}
{\sqrt{|a_0a_n|}}
}.
\]
Using \(\max_{|u|=1}|A(u)|\le\sum_k|a_k|\), we have
\[
\sum_{k=0}^n(k+1)=\frac{(n+1)(n+2)}2
\]
for \(P_n\), and
\[
1+\cdots+1+(n+2)=2(n+1)
\]
for \(Q_n\). Thus both angular discrepancies are
\[
O\!\left(\sqrt{\frac{\log n}{n}}\right).
\]

The roots are also radially concentrated near the unit circle. Since every root has modulus at most \(1\), while
\[
\prod_{P_n(\alpha)=0}|\alpha|=\frac1{n+1},
\qquad
\prod_{Q_n(\alpha)=0}|\alpha|=\frac1{n+2},
\]
the number \(N_\delta\) of roots satisfying \(|\alpha|\le1-\delta\) obeys
\[
N_\delta\le
\frac{\log(n+2)}{-\log(1-\delta)}.
\]
Therefore the empirical zero measures of both \(P_n\) and \(Q_n\) converge to normalized arclength on \(|u|=1\).

Passing from \(u\) to its two square roots preserves the Haar limit, so the corresponding \(w\)-root measures converge to normalized arclength on \(|w|=1\). The inverse Cayley map
\[
C(w)=\frac{w+1}{w-1}
\]
is continuous on the unit circle except at \(w=1\), a Haar-null point. Hence the zero measures of \(p_n\) and \(q_n\) converge to the pushforward of Haar measure by \(C\). Since
\[
C(e^{i\theta})=-i\cot(\theta/2),
\]
that pushforward is precisely
\[
\frac{dt}{\pi(1+t^2)}
\]
on \(i\mathbb R\).

## Verification

The symbolic verification artifact `artifacts/verify_companion_discriminant.py` constructs \(p_n\) and \(q_n\) directly from the source formula, checks the Cayley reduction, and compares the closed discriminant formula with SymPy's exact discriminant for \(1\le n\le6\). It was executed with SymPy 1.14.0 and all checks passed.

## Scientific limitations

The finite-\(n\) Apollonius regions are inclusion regions and are not claimed to be optimal. The Cauchy-law statement is weak convergence; no optimal discrepancy rate is claimed after the unbounded Cayley pushforward. The result is specific to the two families in arXiv:2607.16940 and does not classify general reciprocal positive-coefficient families.

The tools used in the proof are classical. In particular, Eneström--Kakeya supplies the finite-\(n\) disk control and Erdős--Turán supplies angular equidistribution. Standard Cauchy laws on the imaginary axis also occur for other Cayley/root-of-unity constructions, for example in O'Rourke--Reddy's discussion of zeros of \((z-1)^n+(z+1)^n\). The claim of originality here is only for the combined conclusions for the Dilcher--Kim--Stolarsky families, especially the exact \(q_n\) discriminant and the associated root geometry, to the best of our knowledge.

## References

1. K. Dilcher, S.-H. Kim, K. B. Stolarsky, *Properties of two Chebyshev-like polynomial sequences*, arXiv:2607.16940 (2026). https://arxiv.org/abs/2607.16940
2. K. Soundararajan, *Equidistribution of Zeros of Polynomials*, American Mathematical Monthly 126 (2019), 226--236. https://doi.org/10.1080/00029890.2019.1546078
3. W. T. Frazier, R. Gardner, *An Eneström--Kakeya theorem for new classes of polynomials*, Acta et Commentationes Universitatis Tartuensis de Mathematica 23 (2019), 103--115. https://doi.org/10.12697/ACUTM.2019.23.11
4. S. O'Rourke, T. R. Reddy, *Sums of random polynomials with independent roots*, Journal of Mathematical Analysis and Applications 495 (2021), 124719. https://doi.org/10.1016/j.jmaa.2020.124719
