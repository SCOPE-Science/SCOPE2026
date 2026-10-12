# Exact parity Tor algebra for valuation idealizations by the fraction quotient
## Finding
Let \(D\) be a valuation domain that is not a field, let \(Q=\operatorname{Frac}(D)\), set \(E=Q/D\), and form the idealization
\[
R=D\ltimes E,
\qquad
(d,e)(d',e')=(dd',de'+d'e).
\]
Write \(N=0\ltimes E\). Then \(R/N\cong D\), and the canonical kernel \(K=\ker(R\to\phi(R))\) of Zhang--Qi is exactly \(N\). The full Tor table on the two canonical modules \(D\) and \(N\) is
\[
\operatorname{Tor}^{R}_{n}(N,N)\cong
\begin{cases}
0,&n\text{ even},\\
N,&n\text{ odd},
\end{cases}
\qquad
\operatorname{Tor}^{R}_{n}(D,N)\cong
\begin{cases}
N,&n\text{ even},\\
0,&n\text{ odd},
\end{cases}
\]
for all \(n\ge0\), while
\[
\operatorname{Tor}^{R}_{0}(D,D)\cong D,
\qquad
\operatorname{Tor}^{R}_{n}(D,D)\cong
\begin{cases}
N,&n\ge1\text{ odd},\\
0,&n\ge2\text{ even}.
\end{cases}
\]
Hence, as a graded \(D\)-algebra,
\[
\operatorname{Tor}^{R}_{*}(D,D)
\cong
D\oplus\bigoplus_{m\ge0}N[2m+1],
\]
where every product of two positive-degree classes is zero.

## Assumptions and scope
The only assumptions are that \(D\) is a valuation domain and is not a field. No Noetherian, discrete-valuation, completeness, or residue-field hypothesis is used. The statement includes the classical Clark-type example obtained from a discrete valuation domain, such as \(D=\mathbb Q[[x]]\), but it is not restricted to that case.

The first public source date governing this finding is 2026-10-04, the submission date of Zhang--Qi's preprint. Their theorem supplies the general alternating self-Tor mechanism for canonical kernels of local non-strong \(\phi\)-Prüfer rings; the exact module isomorphism in every odd degree and the mixed/reduced-quotient Tor groups are the additional conclusions here.

## Proof
First, \(N^2=0\) and \(R/N\cong D\). If \((d,e)\notin N\), then \(d\ne0\). Because \(E=Q/D\) is divisible as a \(D\)-module, for every \((0,u)\in N\) there is \(v\in E\) with \(dv=u\), and therefore
\[
(d,e)(0,v)=(0,u).
\]
Thus \(N\subsetneq(d,e)R\) for every \((d,e)\notin N\). Since \(R/N\) is the domain \(D\), \(N\) is a divided prime nilradical, so \(R\) is a \(\phi\)-ring. Since \(D\) is a valuation domain, the structural characterization of \(\phi\)-Prüfer rings gives that \(R\) is \(\phi\)-Prüfer. It is local because \(D\) is local.

The ring is not strong. Choose a nonzero nonunit \(d\in D\). Then \(1/d+D\ne0\) in \(E\), and
\[
(d,0)(0,1/d+D)=0.
\]
Hence there is a zero-divisor outside \(N\).

Let \(K\) be Zhang--Qi's canonical kernel. Their general result gives \(K\subseteq N\). Conversely, if \(0\ne e\in E\), then \(e\) is torsion, so some nonzero nonunit \(a\in D\) satisfies \(ae=0\). Therefore \((a,0)\notin N\) is a zero-divisor and annihilates \((0,e)\), which places \((0,e)\) in \(K\). Hence \(K=N\).

Now use the flat resolution of \(E\) over \(D\),
\[
0\longrightarrow D\longrightarrow Q\longrightarrow E\longrightarrow0.
\]
The module \(Q\) is flat because it is a localization of \(D\). Since \(E\) is torsion, \(Q\otimes_D E=0\). Since \(E\) is divisible and torsion, the elementary divisible--torsion tensor lemma gives \(E\otimes_D E=0\). Tensoring the displayed resolution with \(E\) therefore yields
\[
\operatorname{Tor}^{D}_{1}(E,E)\cong E,
\qquad
\operatorname{Tor}^{D}_{i}(E,E)=0\quad(i\ge2).
\]

Put \(T_n=\operatorname{Tor}^{R}_{n}(N,N)\). Zhang--Qi prove for a local non-strong \(\phi\)-Prüfer ring that \(T_0=0\), \(T_2=0\), and
\[
T_1\cong\operatorname{Tor}^{D}_{1}(N,N),
\qquad
T_{2m+1}\cong\operatorname{Tor}^{D}_{1}(T_{2m-1},N),
\qquad
T_{2m+2}=0.
\]
Identifying \(N\) with \(E\) as a \(D\)-module and using \(\operatorname{Tor}^{D}_{1}(E,E)\cong E\), induction gives
\[
T_{2m}=0,
\qquad
T_{2m+1}\cong N
\]
for every \(m\ge0\).

Finally apply \(-\otimes_R N\) and \(-\otimes_R D\) to
\[
0\longrightarrow N\longrightarrow R\longrightarrow D\longrightarrow0.
\]
Because \(N\otimes_RN=0\), one gets \(\operatorname{Tor}^{R}_{1}(D,N)=0\), and for \(n\ge2\),
\[
\operatorname{Tor}^{R}_{n}(D,N)
\cong
\operatorname{Tor}^{R}_{n-1}(N,N).
\]
This is exactly the stated even/odd pattern for \(\operatorname{Tor}^{R}_{n}(D,N)\). A second dimension shift gives \(\operatorname{Tor}^{R}_{1}(D,D)\cong N\) and, for \(n\ge2\),
\[
\operatorname{Tor}^{R}_{n}(D,D)
\cong
\operatorname{Tor}^{R}_{n-1}(N,D),
\]
which gives the remaining table. The positive-degree part of \(\operatorname{Tor}^{R}_{*}(D,D)\) is concentrated in odd degrees, so the product of any two positive-degree classes lands in a positive even degree and is zero.

## Verification
The argument is symbolic and does not depend on finite experimentation. The critical checks are: divisibility and torsion of \(Q/D\); identification of the canonical kernel with the square-zero ideal; exactness and flatness of \(0\to D\to Q\to Q/D\to0\); the vanishings \(Q\otimes_D(Q/D)=0\) and \((Q/D)\otimes_D(Q/D)=0\); and the two dimension shifts from \(0\to N\to R\to D\to0\). Each is proved above or is an explicit hypothesis/result of the cited source.

## Relationship to prior work
Zhang and Qi prove that in every local non-strong \(\phi\)-Prüfer ring the canonical kernel has zero even self-Tor in positive degree and nonzero torsion-divisible odd self-Tor. Their theorem does not identify those odd modules up to isomorphism and does not give the complete mixed Tor table with the reduced quotient. In the valuation idealization \(D\ltimes(Q/D)\), the flat two-term resolution of \(Q/D\) closes their recurrence exactly: every odd self-Tor is the canonical kernel itself.

Idealizations are classical; Anderson--Winders survey the construction, and the specific \(D\ltimes(Q/D)\) pattern includes Clark's uniserial ring. The older morphic-ring literature studies that ring's ideal and morphic structure rather than the parity-resolved Tor algebra described here.

## Limitations
No claim is made that every local non-strong \(\phi\)-Prüfer ring has odd self-Tor isomorphic to its canonical kernel; the exact stabilization uses the special module \(Q/D\). No minimal free resolution is asserted: the modules involved need not be finitely generated. The literature search did not locate an older source computing this exact graded Tor algebra for the valuation idealization, but the idealization literature is extensive, so this remains the principal originality risk.

## References
X. Zhang and W. Qi, *On the \(\phi\)-Weak Global Dimensions and \(\phi\)-Global Dimensions*, arXiv:2610.05567v1, 2026.

D. D. Anderson and M. Winders, *Idealization of a Module*, Journal of Commutative Algebra 1 (2009), 3--56, DOI 10.1216/JCA-2009-1-1-3.

W. K. Nicholson and E. Sánchez Campos, *Principal Rings with the Dual of the Isomorphism Theorem*, Glasgow Mathematical Journal 46 (2004), 181--191, DOI 10.1017/S0017089503001654.
