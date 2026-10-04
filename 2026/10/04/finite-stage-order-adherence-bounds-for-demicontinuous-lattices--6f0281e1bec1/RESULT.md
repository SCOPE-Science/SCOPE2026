# Finite-stage order-adherence bounds for demicontinuous lattices
## Finding
Let \(F\neq\{0\}\) be a normed lattice with unit ball \(B_F\). For a set \(S\subset F\), let \(\operatorname{adh}_o(S)\) denote the set of order limits of nets from \(S\), and define finite iterates by \(A_0=B_F\) and \(A_{n+1}=\operatorname{adh}_o(A_n)\). If \(F\) is \(r\)-demicontinuous, then for every integer \(n\ge 0\),
\[
A_n\subset r^n B_F.
\]
Therefore every \(x\in A_n\) satisfies \(\|x\|\le r^n\). If \(r>1\) and \(\|x\|>1\), any finite adherence depth placing \(x\) in \(A_n\) must satisfy
\[
n\ge \left\lceil \log_r \|x\| \right\rceil.
\]

If, in addition, \(F\) is anti-semicontinuous, meaning that the order closure of \(B_F\) is \(F\), then no finite \(A_n\) can equal \(F\). Thus the transfinite iteration of order adherence which produces the order closure can reach the whole nonzero space only at a stage at least \(\omega\). Anti-semicontinuity also implies
\[
F^*_{oc}=\{0\},
\]
where \(F^*_{oc}\) denotes the norm-bounded order-continuous functionals.

## Assumptions and scope
The statement uses order convergence of nets, not only sequential or \(\sigma\)-order convergence. The quantitative hypothesis is exactly \(r\)-demicontinuity in the sense that the order adherence of \(B_F\) lies in \(rB_F\). The conclusion is a necessary obstruction for the open coexistence problem of demicontinuity and anti-semicontinuity; it does not construct such a lattice and does not rule out coexistence at genuinely transfinite closure depth.

## Proof
Write \(A(S)=\operatorname{adh}_o(S)\). Order convergence is homogeneous, so for every scalar \(c>0\),
\[
A(cS)=cA(S).
\]
By \(r\)-demicontinuity, Bilokopytov's Proposition 3.7 gives \(A(B_F)\subset rB_F\). We prove \(A_n\subset r^nB_F\) by induction. The case \(n=0\) is immediate. If \(A_n\subset r^nB_F\), monotonicity and homogeneity of adherence give
\[
A_{n+1}=A(A_n)\subset A(r^nB_F)=r^nA(B_F)\subset r^{n+1}B_F.
\]
This proves the finite-stage bound and the logarithmic lower bound on adherence depth.

Bilokopytov recalls that order closure is obtained by transfinite iteration of order adherence. If the order closure of \(B_F\) equals \(F\), then a finite stage cannot already equal \(F\), because every \(A_n\) is norm bounded by \(r^n\), whereas a nonzero normed vector space is unbounded. Hence the first possible stage yielding all of \(F\) is at least \(\omega\).

For the dual obstruction, let \(0\neq\varphi\in F^*_{oc}\). The strip
\[
C_\varphi=\left\{x\in F:|\varphi(x)|\le \|\varphi\|\right\}
\]
contains \(B_F\). Because \(\varphi\) is order continuous, \(C_\varphi\) is order closed. Therefore the order closure of \(B_F\) is contained in \(C_\varphi\). Since \(\varphi\neq0\), scalar multiplication produces an element outside \(C_\varphi\), so \(C_\varphi\neq F\). Thus the order closure of \(B_F\) cannot be \(F\). Contrapositively, anti-semicontinuity forces \(F^*_{oc}=\{0\}\).

## Verification
The proof uses only the definition of order adherence, homogeneity of order convergence, the characterization \(\operatorname{adh}_o(B_F)\subset rB_F\) of \(r\)-demicontinuity, and order continuity of functionals. The induction was checked at the base and successor steps; the anti-semicontinuous conclusion then uses only boundedness of each finite iterate. The dual strip argument was checked for containment of the unit ball, order closedness, and properness.

## Relationship to prior work
Bilokopytov defines order adherence and notes that order closure is obtained by transfinite iteration; Proposition 3.7 characterizes \(r\)-demicontinuity by \(\operatorname{adh}_o(B_F)\subset rB_F\). Remark 4.11 asks whether a demicontinuous normed lattice can be anti-semicontinuous. The paper states a trivial-dual obstruction for the stronger notion of anti-demicontinuity, but does not state the anti-semicontinuous dual obstruction or the finite-iterate growth bound above.

Avilés, Taylor and Tradacete study the distinction between order closure and order adherence and exhibit a weakly Fatou Banach lattice with no equivalent Fatou lattice norm. Avilés, Rosendal, Taylor and Tradacete develop a transfinite Fatou hierarchy for sequential order convergence. Those works are closely related context, but the indexed statements inspected do not give the present quantitative net-adherence bound or the stated necessary conditions for Bilokopytov's demicontinuous/anti-semicontinuous coexistence question.

## Limitations
This result is only a necessary-condition theorem. It does not decide whether a demicontinuous anti-semicontinuous normed lattice exists. The two closely related 2026 papers by Avilés and coauthors were available through abstracts and indexed descriptions rather than complete text, so an unindexed equivalent formulation remains a residual novelty risk. The full text of Bilokopytov's focal preprint was inspected at the relevant definitions, propositions, and open-problem remark.

## References
1. Eugene Bilokopytov, *Variants of order semicontinuity in Banach lattices*, arXiv:2609.03070, first public version 2 September 2026.
2. A. Avilés, M. A. Taylor, P. Tradacete, *Order closure, order adherence and Fatou norms*, arXiv:2609.06689, first public version 6 September 2026.
3. Antonio Avilés, Christian Rosendal, Mitchell A. Taylor, Pedro Tradacete, *A Classification of Order Convergence via a Transfinite Fatou Hierarchy*, arXiv:2604.02588, first public version 2 April 2026.
