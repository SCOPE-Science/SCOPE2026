# Quantitative inflection density below unit order for holomorphic curves

## Finding

Let
\[
f:\mathbb C\longrightarrow\mathbb P^n
\]
be a transcendental linearly non-degenerate holomorphic curve of ordinary order
\[
0\le\rho<1.
\]
Let \(N_1(r,f)\) denote the counting function of the zeros of the Wronskian of a reduced homogeneous representation, and let \(T(r,f)\) be the Cartan--Nevanlinna characteristic.

Define
\[
J(\rho)
=
\int_0^\infty
\frac{\max\{1,u^\rho\}}{(1+u)^2}\,du
=
\frac12+
\int_1^\infty
\frac{u^\rho}{(1+u)^2}\,du.
\]
Then
\[
\limsup_{r\to\infty}
\frac{N_1(r,f)}{T(r,f)}
\ge
\frac1{J(\rho)}.
\]

Thus every transcendental linearly non-degenerate curve of order strictly below one has a quantitatively positive asymptotic inflection density.

The bound specializes to
\[
J(0)=1,
\]
so the order-zero case recovers the sharp estimate
\[
\limsup_{r\to\infty}
\frac{N_1(r,f)}{T(r,f)}
\ge1
\]
from the recent primary source.

At order one half,
\[
J\!\left(\frac12\right)
=
1+\frac\pi4,
\]
and hence
\[
\limsup_{r\to\infty}
\frac{N_1(r,f)}{T(r,f)}
\ge
\frac4{4+\pi}.
\]

Finally,
\[
J(\rho)\sim\frac1{1-\rho}
\qquad(\rho\uparrow1),
\]
so the displayed lower bound is asymptotic to
\[
1-\rho.
\]
No sharpness is claimed when
\[
0<\rho<1.
\]

## Assumptions and scope

The definitions of the characteristic, Wronskian counting function, normalized entire representation, and order are those of arXiv:2609.38032v1.

The hypothesis is on ordinary order, not merely lower order. This is essential for the source's Section 6 construction, which produces normalized entire coordinates whose orders are at most \(\rho\).

The result is dimension-independent in its numerical constant, although the target dimension enters the logarithmic term in the proof.

The theorem does not determine the optimal lower bound for positive orders below one. It gives an explicit universal lower bound extracted from the integral method of the source.

## Proof

The source's Lemma 6.5 associates to \(f\) a normalized entire system
\[
y=(y_0,\ldots,y_n)
\]
whose components have order at most \(\rho\). Put
\[
H_y(r)=\log\max_{0\le j\le n}M(r,y_j)
\]
and let \(N_y(r)\) be the integrated counting function of the zeros of its Wronskian.

The same lemma gives constants \(B,C,C_b\) such that
\[
T(s,f)\le H_y(s+B)+C
\]
and
\[
N_y(t)\le N_{W_f}(t+B)+C_b.
\]
The difference between \(N_{W_f}\) and \(N_1(\cdot,f)\) is an additive normalization constant, irrelevant after division by the transcendental characteristic.

Let
\[
L=
\limsup_{r\to\infty}
\frac{N_1(r,f)}{T(r,f)}.
\]
If \(L=+\infty\), there is nothing to prove. Suppose for contradiction that
\[
L<\frac1{J(\rho)}.
\]
Choose
\[
L<c<\frac1{J(\rho)}.
\]
Then for all sufficiently large \(s\),
\[
N_{W_f}(s)\le cT(s,f)+C.
\]

We use a slight parameterized form of the source's Lemma 6.4. Fix
\[
a>1
\]
and
\[
\rho<\alpha<1.
\]
Define
\[
I_{\alpha,a}
=
\int_0^\infty
\frac{\max\{1,(au)^\alpha\}}{(1+u)^2}\,du.
\]
If a continuous nondecreasing function \(H\) satisfies
\[
H(r)=o(r^\alpha),
\]
then there are radii \(r_\nu\to\infty\) such that
\[
r_\nu
\int_0^\infty
\frac{H(at)}{(r_\nu+t)^2}\,dt
\le
I_{\alpha,a}H(r_\nu).
\]
Indeed, as in the source proof, choose \(r_\nu\) maximizing
\[
H(r)/r^\alpha
\]
on a tail interval. Then
\[
H(ar_\nu u)
\le
H(r_\nu)\max\{1,(au)^\alpha\},
\]
and the substitution
\[
t=r_\nu u
\]
gives the estimate.

Because \(a>1\), for all sufficiently large \(t\),
\[
t+2B\le at.
\]
Combining the preceding source inequalities and absorbing the bounded interval into a constant gives
\[
N_y(t)
\le
cH_y(at)+C
\qquad(t>0).
\]
Since every component of \(y\) has order at most \(\rho\),
\[
H_y(r)=o(r^\alpha).
\]

Corollary 6.3 of the source says
\[
H_y(r)
\le
n\log^+r
+
r\int_0^\infty
\frac{N_y(t)}{(r+t)^2}\,dt.
\]
Using the parameterized radius-selection estimate therefore yields
\[
(1-cI_{\alpha,a})H_y(r_\nu)
\le
n\log r_\nu+C.
\]

The map
\[
(\alpha,a)
\longmapsto
I_{\alpha,a}
\]
is continuous as
\[
(\alpha,a)\to(\rho,1)
\]
from \(\rho<\alpha<1\), \(a>1\), by dominated convergence on any compact subinterval of exponents below one. Moreover,
\[
I_{\alpha,a}
\longrightarrow
J(\rho).
\]
Our choice of \(c\) therefore permits \(\alpha\) and \(a\) close enough to \(\rho\) and one that
\[
cI_{\alpha,a}<1.
\]

It follows that
\[
H_y(r_\nu)
\le
\Gamma\log r_\nu+C
\]
for some finite \(\Gamma\). Hence
\[
M(r_\nu,y_j)
\le
Cr_\nu^\Gamma
\]
for every component. Cauchy's estimate, followed by \(r_\nu\to\infty\), forces every Taylor coefficient of integer degree larger than \(\Gamma\) to vanish. Thus all components \(y_j\) are polynomials.

A holomorphic curve admitting a polynomial homogeneous representation is rational. This contradicts the hypothesis that \(f\) is transcendental. Therefore
\[
L\ge\frac1{J(\rho)}.
\]

For \(\rho=1/2\), the substitution \(u=x^2\) gives
\[
\int_1^\infty
\frac{\sqrt u}{(1+u)^2}\,du
=
\frac12+\frac\pi4,
\]
which yields
\[
J\!\left(\frac12\right)=1+\frac\pi4.
\]

For \(\rho\uparrow1\), the tail integral is equivalent to
\[
\int_1^\infty u^{\rho-2}\,du
=
\frac1{1-\rho},
\]
so
\[
J(\rho)\sim(1-\rho)^{-1}.
\]

## Verification

The recent primary paper was inspected through Corollary 6.3, Lemma 6.4, Lemma 6.5, Proposition 6.6, and Proposition 6.7. In particular, it supplies the exact integral estimate, the normalized coordinates of order at most \(\rho\), the comparison between the source and normalized Wronskian counting functions, and the polynomial-growth contradiction used at order zero.

The new step is quantitative rather than computational: the fixed dilation factor in the source's radius-selection argument is replaced by an arbitrary number greater than one, and then sent to one after the translation error has been absorbed on a bounded interval.

The limiting integral
\[
J(\rho)
\]
is finite exactly for \(\rho<1\). The order-one-half value and the unit-order asymptotic were checked symbolically from the defining integral.

No finite sampling or numerical experiment is used as proof.

## Relationship to prior work

Eremenko and Zhang prove the sharp order-zero bound and, separately, show that a curve of order below one with
\[
N_1(r,f)=o(T(r,f))
\]
must be rational. Their paper does not state a positive lower bound depending on a nonzero order \(\rho<1\).

Eremenko's earlier note on holomorphic curves with few inflection points formulates the qualitative small-ramification conjecture that motivated the new paper, without a quantitative subunit-order density law.

Earlier lower-order defect-relation literature, including work of Lianzhong Yang, treats deficiency relations for holomorphic curves of lower order below one. The accessible published description does not state a lower bound for the Wronskian counting ratio of the form proved here. Because the full text of that older paper was not available in the bounded comparison, it remains a literature-access risk rather than evidence of coverage.

Targeted searches under Wronskian density, inflection counting, finite order below one, and equivalent normalized-ratio formulations did not locate a statement implying the displayed bound.

## Limitations

The bound is not asserted sharp for positive orders below one.

The proof requires ordinary order less than one. It does not extend as stated to curves known only to have lower order less than one.

The argument gives a limsup bound rather than a pointwise or liminf density estimate.

An older inaccessible defect-relation paper for lower-order curves remains a residual originality risk, although its available abstract concerns deficiency relations rather than Wronskian-density estimates.

## References

1. A. Eremenko and T. Zhang, *Holomorphic curves of finite lower order with few inflection points*, arXiv:2609.38032v1, 2026.
2. A. Eremenko, *Holomorphic curves with few inflection points*, 2015 note.
3. L. Yang, *Defect relations of holomorphic curves of lower order less than one*, Complex Variables, Theory and Application 22 (1993), 121--128. DOI: 10.1080/17476939308814652.
4. A. Eremenko, *Meromorphic functions with small ramification*, Indiana University Mathematics Journal 42 (1993), 1193--1218.
