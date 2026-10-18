# Parity-alternating Turán inequalities for strongly \(132\)-avoiding permutations

## Finding

Let \(a_n\) be the number of permutations \(\pi\in S_n\) such that both \(\pi\) and its square \(\pi^2\), in one-line notation, avoid the pattern \(132\), and put \(a_0=1\). Define the adjacent Turán determinant
\[
T_n=a_n^2-a_{n-1}a_{n+1}\qquad(n\ge1).
\]
Write \(C(z)=(1-\sqrt{1-4z})/(2z)\), with \(C(0)=1\), and set
\[
B(z)=C\bigl(z^3C(z^3)\bigr),\quad
P(z)=\frac{B(z)}{2-(1+z)B(z)},\quad P_+=P(1/2),\quad P_-=P(-1/2).
\]
Both constants \(P_+\) and \(P_-\) are strictly positive. The asymptotic formula is
\[
\boxed{T_n=(-1)^n\frac{3P_+P_-}{2\pi}\frac{4^n}{n^2}
       +O\!\left(\frac{4^n}{n^3}\right).}
\]
Numerically, the positive leading constant is approximately \(1.95140809093\). Consequently, for every sufficiently large even \(n\) the sequence is strictly log-concave at \(n\), while for every sufficiently large odd \(n\) it is strictly log-convex at \(n\). In particular it is neither eventually log-concave nor eventually log-convex. This is a parity-resolved shape theorem, not a new enumeration of the \(a_n\).

## Assumptions and scope

All permutations are on the labeled set \(\{1,\ldots,n\}\); composition is functional, so \(\pi^2(i)=\pi(\pi(i))\). A permutation avoids \(132\) if no indices \(i<j<k\) satisfy \(\pi(i)<\pi(k)<\pi(j)\). The asymptotic is as \(n\to\infty\) through all positive integers; it does not specify a least threshold. Every square root in the analytic argument is the branch analytic at the origin with positive value there. All asymptotics are for real integer-valued counts, and the implied constants are absolute.

The sole enumerative input is the already published generating function of Archer and Graves [1, Theorem 1.2]. The new assertion concerns adjacent coefficient inequalities and their exact parity-dependent leading defect. Classifying permutations or reproving the published generating function is not part of this finding.

## Proof

**1. Published generating function and factorization.** The generating function of the counts is [1, Theorem 1.2]
\[
A(z)=\sum_{n\ge0}a_nz^n=P(z)\bigl(F(z)+G(z)\bigr),
\]
where
\[
F(z)=\frac{1-z}{1-z-z^2C(z^2)}
=\frac{2(1-z)}{1-2z+\sqrt{1-4z^2}},
\qquad
G(z)=\frac{2z(1+2z)(C(z^3)-1)}{1-z^2}.
\]
The exact factorization is essential: \(F\) has different singular orders at the two boundary points \(\pm1/2\), while \(P\) and \(G\) are analytic at both points.

**2. Isolation of the two dominant singularities.** Since Catalan coefficients are nonnegative, for \(|z|\le1/2\),
\[
|z^3C(z^3)|\le\tfrac18 C(\tfrac18)
=\tfrac12\bigl(1-1/\sqrt2\bigr)<\tfrac3{20}.
\]
Monotonicity of the Catalan series gives
\[
|(1+z)B(z)|\le\tfrac32 C(\tfrac3{20})<2.
\]
The last inequality follows directly from \(C(3/20)=(10/3)(1-\sqrt{2/5})<4/3\). Hence the denominator of \(P\) has no zero on the closed disk \(|z|\le1/2\). Since the composition is analytic on a larger disk (its inner argument remains strictly below \(1/4\)), compactness and strictness give an \(\varepsilon>0\) such that \(P\) is analytic on \(|z|<1/2+\varepsilon\). Likewise \(G\) is analytic in a disk strictly larger than radius \(1/2\), because its only possible singularities lie beyond that circle.

The original denominator \(1-z-z^2C(z^2)\) of \(F\) is nonzero for \(|z|<1/2\): its nonconstant part has modulus at most \(r+r^2C(r^2)<1\) for \(r<1/2\). On \(|z|=1/2\) the triangle inequality is strict away from \(z=1/2\), and \(F\) has its explicit branch singularity at \(z=-1/2\). Thus the only modulus-\(1/2\) singularities of \(A\) are \(z=1/2\) and \(z=-1/2\). All functions involved are algebraic, so suitably slit neighborhoods furnish the standard delta domains needed for singularity transfer [4].

**3. The positive singularity.** Put \(s=\sqrt{1-2z}\), so \(z=(1-s^2)/2\). Direct expansion gives
\[
F(z)=\frac{1+s^2}{s(s+\sqrt{2-s^2})}
=\frac1{\sqrt2}s^{-1}-\frac12+\frac7{4\sqrt2}s+O(s^2).
\]
Since \(P(z)=P_+-\frac12P'(1/2)s^2+O(s^4)\) and \(G\) is analytic at \(1/2\), the terms having half-integer singular powers begin with
\[
\frac{P_+}{\sqrt2}(1-2z)^{-1/2}
+\frac{7P_+-2P'(1/2)}{4\sqrt2}(1-2z)^{1/2}.
\]
Analytic integer-power terms have no contribution to the dominant algebraic coefficient asymptotics at this point.

**4. The negative singularity.** Put \(t=\sqrt{1+2z}\), so \(z=(-1+t^2)/2\). Here
\[
F(z)=\frac{3-t^2}{2-t^2+t\sqrt{2-t^2}}
=\frac32-\frac{3\sqrt2}{4}t+O(t^2).
\]
Analyticity of \(P\) and \(G\) implies that the first nonanalytic term of \(A\) near \(-1/2\) is exactly
\[
-\frac{3\sqrt2}{4}P_-(1+2z)^{1/2}.
\]
It is nonzero: \(P_->0\), since \(C(-1/8)>0\), its composed argument is negative, and the relevant denominator exceeds \(3/2\). The local analytic terms and next odd powers contribute only to lower orders.

**5. Coefficient transfer and subtraction.** For the indicated slit neighborhoods, the standard square-root transfer rules are
\[
[z^n](1-2z)^{-1/2}
=\frac{2^n}{\sqrt{\pi n}}\left(1-\frac1{8n}+O(n^{-2})\right),
\]
\[
[z^n](1\mp2z)^{1/2}=
-\frac{(\pm2)^n}{2\sqrt\pi\,n^{3/2}}
\left(1+O(n^{-1})\right).
\]
Combining the two dominant singularities yields
\[
a_n=K\frac{2^n}{\sqrt n}
\left(1+\frac{\alpha+\beta(-1)^n}{n}+O(n^{-2})\right),
\]
with exact constants
\[
K=\frac{P_+}{\sqrt{2\pi}}>0,\qquad
\alpha=\frac{P'(1/2)}{4P_+}-1,\qquad
\beta=\frac{3P_-}{4P_+}>0.
\]
(The \(O(n^{-2})\) is uniform over both parities.) Squaring the expression at index \(n\), and multiplying it at indices \(n-1\) and \(n+1\), gives
\[
T_n=K^2\frac{4^n}{n}
\left(\frac{4\beta(-1)^n}{n}+O(n^{-2})\right).
\]
Since \(4K^2\beta=3P_+P_-/(2\pi)>0\), this is the claimed asymptotic and proves the eventual strict parity alternation.

## Verification

The standalone standard-library program `verify_turan.py` independently enumerates permutations for \(1\le n\le8\) and checks avoidance in both \(\pi\) and \(\pi^2\). It also computes Catalan compositions in exact integer series arithmetic through degree \(240\), reproduces the first sixteen sequence terms in [1, Table 1] and [3], verifies the finite Turán signs for \(8\le n\le239\), and checks numerical convergence of the normalized asymptotic defect. The finite-range sign checks do **not** prove that the sign theorem begins at \(n=8\); the infinite proof is the two-singularity calculation above. Reproduce by running `python3 verify_turan.py` from the directory containing that file; there are no third-party dependencies.

## Relationship to prior work

Archer and Graves [1] obtain the exact generating function \(A(z)\) and the first-order asymptotic \(a_n\sim K2^n/\sqrt n\). Their analysis concentrates on \(z=1/2\) and gives no asymptotic for \(T_n\). Their formula and leading asymptotic are used here rather than re-claimed. The new feature is the weak singularity at \(z=-1/2\): it enters \(a_n\) one order below the main term but **dominates its second multiplicative difference**, producing the alternating sign and the explicit positive constant. The leading positive-singularity asymptotic alone cannot decide the Turán sign.

Bóna and Smith [2] originally posed questions for strong \(132\)-avoidance and supplied initial computations; OEIS A322779 [3] records early values. Both are compatible with but do not assert an eventual alternating Turán law. The algebraic transfer principle itself is classical [4]; the theorem here consists of identifying and comparing the two concrete singular contributions and demonstrating their effect on adjacent-coefficient shape.

## Limitations

No least eventuality threshold is proved. The computed pattern beginning at \(n=8\) is evidence only. The result depends on the published exact generating function of [1], not on a separate combinatorial derivation of it. The analysis establishes the indicated leading term and order of error, not a fully explicit all-order expansion. An unindexed independent derivation of the same Turán law remains possible. The review here is not an independent external audit.

## References

[1] K. Archer and C. Graves, *Permutations that strongly avoid 132*, arXiv:2604.25912v1, first posted 2026-04-28, especially Theorem 1.2 and Section 4. https://arxiv.org/html/2604.25912v1

[2] M. Bóna and R. Smith, *Pattern avoidance in permutations and their squares*, arXiv:1901.00026 (2018). https://arxiv.org/abs/1901.00026

[3] OEIS A322779, *132-avoiding permutations whose squares are also 132-avoiding*. https://oeis.org/A322779

[4] P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapters VI–VII (singularity transfer for algebraic functions).
