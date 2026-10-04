# Exact mixed-measure \(L_1\) Daugavet and Delta constants
## Finding
Let \((\Omega,\Sigma,\mu)\) be a real sigma-finite measure space and let \(f\in B_{L_1(\mu)}\). For a \(\mu\)-atom \(A\), put
\[
p_A(f)=\int_A |f|\,d\mu,
\]
and define
\[
m(f)=\sup\{p_A(f):A\text{ is a }\mu\text{-atom}\},
\]
where the supremum of the empty set is \(0\). If \(\operatorname{dc}(f)\) is the pointwise Daugavet constant and \(\delta c(f)\) the pointwise Delta constant, then
\[
\operatorname{dc}(f)=\delta c(f)=1+\|f\|_1-2m(f).
\]
Consequently, on the unit sphere,
\[
\operatorname{dc}(f)=\delta c(f)=2(1-m(f)).
\]

## Assumptions and scope
A slice of \(B_{L_1(\mu)}\) is
\[
S(\varphi,\alpha)=\{g\in B_{L_1(\mu)}:\varphi(g)>1-\alpha\},
\]
where \(\varphi\in S_{L_\infty(\mu)}\) and \(\alpha>0\). The two constants are
\[
\operatorname{dc}(f)=\inf_S\sup_{g\in S}\|f-g\|_1
\]
with the infimum over all slices, and
\[
\delta c(f)=\inf_{S\ni f}\sup_{g\in S}\|f-g\|_1
\]
with the infimum over slices containing \(f\). The proof uses sigma-finiteness to identify the dual with \(L_\infty(\mu)\), to ensure atoms have finite measure, and to extract finite positive-measure subsets from an atomless set. No separability assumption is used.

## Proof
Write \(r=\|f\|_1\) and \(m=m(f)\). We first prove
\[
\operatorname{dc}(f)\ge 1+r-2m.
\]
Fix an arbitrary slice \(S(\varphi,\alpha)\). Choose \(0<\varepsilon<\min\{\alpha,1\}\), and set
\[
E=\{\omega:|\varphi(\omega)|>1-\varepsilon\}.
\]
Since \(\|\varphi\|_\infty=1\), the set \(E\) has positive measure.

Suppose first that \(E\) meets a \(\mu\)-atom \(A\) in positive measure. Then \(E\cap A=A\) modulo null sets, and both \(f\) and \(\varphi\) are essentially constant on \(A\). If \(h\) is the constant value of \(\varphi\) there, define
\[
g=\operatorname{sgn}(h)\frac{\chi_A}{\mu(A)}.
\]
Then \(\|g\|_1=1\) and \(\varphi(g)=|h|>1-\varepsilon>1-\alpha\), so \(g\in S(\varphi,\alpha)\). Put \(p=p_A(f)\). If the signs of \(f\) and \(g\) agree on \(A\), then
\[
\|f-g\|_1=(1-p)+(r-p)=1+r-2p\ge 1+r-2m.
\]
If the signs disagree, then \(\|f-g\|_1=1+r\), which is even larger.

Suppose instead that \(E\) contains no atom of positive measure. Then the restricted measure on \(E\) is atomless. Given \(\eta>0\), sigma-finiteness and atomless divisibility give a measurable set \(B\subset E\) with \(0<\mu(B)<\infty\) and
\[
q=\int_B|f|\,d\mu<\frac{\eta}{2}.
\]
Define
\[
g=\operatorname{sgn}(\varphi)\frac{\chi_B}{\mu(B)}.
\]
Again \(\|g\|_1=1\) and
\[
\varphi(g)=\frac{1}{\mu(B)}\int_B|\varphi|\,d\mu>1-\varepsilon>1-\alpha,
\]
so \(g\) belongs to the slice. The reverse triangle inequality on \(B\) gives
\[
\|f-g\|_1\ge (1-q)+(r-q)=1+r-2q>1+r-\eta.
\]
Since \(\eta\) is arbitrary, the supremum of the distance over this slice is at least \(1+r\), and hence certainly at least \(1+r-2m\). Thus every slice has supremal distance at least \(1+r-2m\), proving the lower bound for \(\operatorname{dc}(f)\).

We now prove the matching upper bound for \(\delta c(f)\). If \(m=0\), then the preceding estimate and the elementary inequality \(\|f-g\|_1\le r+1\) give
\[
1+r\le \operatorname{dc}(f)\le\delta c(f)\le 1+r,
\]
so equality holds.

Assume \(m>0\), and choose an atom \(A\) with \(p=p_A(f)>0\). On \(A\), the function \(f\) is essentially a nonzero constant. Let \(s\in\{-1,1\}\) be its sign there and set \(\psi=s\chi_A\in S_{L_\infty(\mu)}\). For \(0<\eta<p\), consider the slice
\[
S_A=\{g\in B_{L_1(\mu)}:\psi(g)>p-\eta\}.
\]
This is a slice containing \(f\). For \(g\in S_A\), the restriction of \(g\) to \(A\) is essentially constant. Put \(q=\psi(g)>p-\eta>0\). Then the \(L_1\)-mass of \(g\) on \(A\) is \(q\), and its mass off \(A\) is at most \(1-q\). Therefore
\[
\|f-g\|_1\le |p-q|+(r-p)+(1-q).
\]
If \(q\le p\), the right-hand side is \(1+r-2q<1+r-2p+2\eta\). If \(q\ge p\), it is exactly \(1+r-2p\). Hence
\[
\sup_{g\in S_A}\|f-g\|_1\le 1+r-2p+2\eta.
\]
Letting \(\eta\downarrow0\) yields \(\delta c(f)\le1+r-2p\). Finally take atoms with \(p_A(f)\uparrow m\) to obtain
\[
\delta c(f)\le1+r-2m.
\]
Combining this with \(\operatorname{dc}(f)\le\delta c(f)\) and the lower bound proves the formula.

## Verification
The proof above is analytic and does not depend on finite computation. The accompanying exact-rational checker independently replays the two algebraic inequalities used in the atomic lower and upper estimates over a dense finite grid of rational parameters and checks the endpoint identities. It is a consistency check only; it does not certify atomless set selection or replace the proof.

## Relationship to prior work
Abrahamsen, Haller, Lima and Pirk proved for sigma-finite real \(L_1(\mu)\) that a unit vector is a Daugavet point exactly when it is a Delta point, equivalently when its support contains no atom. That result is qualitative.

Choi and Jung later introduced the quantitative pointwise Daugavet and Delta constants. For sigma-finite purely atomic \(L_1\) spaces they computed the Daugavet constant exactly, and for a general atom in the support they obtained an upper bound for the Delta constant; in \(\ell_1\) they obtained equality of the two constants. The formula here gives the exact value of both constants for arbitrary mixtures of atomic and atomless measure and reduces to those atomic formulas in the purely atomic case.

## Limitations
The statement is for real sigma-finite \(L_1(\mu)\). No claim is made for complex \(L_1\), non-localizable measure spaces where the usual dual identification may fail, or other Banach function spaces. The literature comparison is based on the cited primary sources and targeted searches; an equivalent result under different terminology remains a residual bibliographic possibility.

## References
1. T. A. Abrahamsen, R. Haller, V. Lima, and K. Pirk, “Delta- and Daugavet-points in Banach spaces,” arXiv:1812.02450v1, first public version 2018-12-06.
2. G. Choi and M. Jung, “The Daugavet and Delta-constants of points in Banach spaces,” arXiv:2307.10647v1, first public version 2023-07-20.
