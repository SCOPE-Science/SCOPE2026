# One excess multiplicity forces a doubled trivial sheet
## Finding
Let \(k\) be a field of characteristic \(0\), let \(Y\) be a connected reduced \(k\)-variety, and let \(\varphi:X\to Y\) be a quasi-finite flat morphism. Assume every geometric fiber has exactly \(s\ge1\) distinct points and that the finite-flat degree is \(s+1\). Then there exist an invertible sheaf \(L\) on \(Y\) and a finite étale morphism \(Z\to Y\) of degree \(s-1\) for which
\[
X\cong \operatorname{Spec}_Y(\mathcal O_Y\oplus L)\;\sqcup\;Z,
\]
where multiplication on the first algebra is
\[
(a,u)(b,v)=(ab,av+bu),
\]
so \(L^2=0\). When \(s=1\), the étale summand \(Z\) is empty.

Equivalently, if the finite-flat degree exceeds the number of distinct geometric points by exactly one, the entire nonreduced defect is one doubled trivial sheet. Consequently, if \(X_{\mathrm{red}}\to Y\) is connected of degree \(s>1\), then
\[
\deg(\varphi)-s\ne1.
\]

## Assumptions and scope
The base \(Y\) is assumed reduced and connected, and the ground field has characteristic \(0\). Connectedness is used only to make the finite-flat degree and geometric-fiber cardinality single integers; the statement applies componentwise without it.

The conclusion concerns the scheme structure of \(X\), not only its set of geometric points. The invertible sheaf \(L\) may be nontrivial. No assertion is made in positive characteristic, where the reduced morphism need not be étale under the same hypotheses.

## Proof
Chen proves that such a quasi-finite flat morphism is finite. Write locally
\[
Y=\operatorname{Spec}A,\qquad X=\operatorname{Spec}B,
\]
with \(A\) reduced and \(B\) finite free of rank \(r=s+1\). In the proof of Theorem 3.3, the trace-pairing map
\[
\Theta:B\longrightarrow B^\vee
\]
has constant fiber rank \(s\); its kernel is the nilradical \(N=\operatorname{nil}B\), and \(N\) is finite locally free of rank
\[
r-s=1.
\]
Moreover
\[
E:=B/N
\]
is finite étale of rank \(s\) over \(A\).

We first show that \(N^2=0\). On an open set where \(N=A\varepsilon\), ideality gives
\[
\varepsilon^2=c\varepsilon
\]
for some \(c\in A\). Since \(\varepsilon\) is nilpotent, for some \(m\ge2\),
\[
0=\varepsilon^m=c^{m-1}\varepsilon.
\]
Because \(\varepsilon\) is a basis of the free rank-one \(A\)-module \(N\), this implies \(c^{m-1}=0\). Reducedness of \(A\) gives \(c=0\). Hence \(N^2=0\) locally and therefore globally.

Multiplication of \(B\) on the invertible \(A\)-module \(N\) gives an \(A\)-algebra homomorphism
\[
\rho:B\longrightarrow\operatorname{End}_A(N)\cong A.
\]
It restricts to the identity on \(A\). Since \(N^2=0\), the ideal \(N\) acts trivially on itself, so \(\rho\) factors through an \(A\)-algebra retraction
\[
\bar\rho:E=B/N\longrightarrow A.
\]
Thus the finite étale cover \(\operatorname{Spec}E\to\operatorname{Spec}A\) has a section. A section of a finite étale morphism is an open-and-closed component, so
\[
E\cong A\times C
\]
with \(C\) finite étale of rank \(s-1\). Under this product decomposition, \(\bar\rho\) is projection onto \(A\); hence the \(C\)-factor acts trivially on \(N\).

Let \(\bar e=(0,1)\in A\times C\). Idempotents lift uniquely through nilpotent ideals, so \(\bar e\) has an idempotent lift \(e\in B\). Because the \(C\)-factor acts trivially on \(N\), we have \(eN=0\). Therefore
\[
eB\xrightarrow{\sim} C.
\]
The complementary factor has reduction \(A\), nilradical \(N\), and square-zero multiplication on \(N\); explicitly
\[
(1-e)B\cong A\oplus N.
\]
Thus
\[
B\cong(A\oplus N)\times C.
\]
These local decompositions glue: \(N\) is globally invertible and the lifted idempotent is unique. Writing \(L\) for the corresponding invertible sheaf on \(Y\) gives the asserted decomposition.

If \(s>1\), then \(X_{\mathrm{red}}\cong Y\sqcup Z\) is disconnected. This proves the final connectedness obstruction.

## Verification
The proof uses no finite experiment. The critical source-dependent step is Chen's trace-pairing argument: for finite-flat rank \(r\) and constant distinct geometric-fiber count \(s\), the trace radical is exactly the nilradical and is locally free of rank \(r-s\), while the reduction is finite étale of rank \(s\).

The remaining steps were checked directly as ring identities. Rank one plus reducedness forces the nilradical to square to zero; its multiplication representation gives the retraction of the reduced étale algebra; the resulting étale section supplies a clopen factor; and unique idempotent lifting through the nilpotent ideal reconstructs the product decomposition before reduction.

The argument does not infer an infinite statement from a sample computation.

## Relationship to prior work
Chen's current preprint proves that the reduced map is finite étale and, in its revised trace-pairing proof, identifies the nilradical as a locally free module of rank \(r-s\). It does not state the rank-one consequence \(N^2=0\), the induced section of the reduced cover, or the resulting global product decomposition.

The superseded 2025 predecessor already uses the double line as a motivating toy example, which is the special case \(s=1\) with trivial \(L\). Its full text does not formulate the general rank-one-nilradical classification or the forced trivial sheet for \(s>1\).

Targeted searches for the exact source identifier, rank-one nilradicals, square-zero thickenings, finite-flat degree excess one, and the equivalent connected-cover obstruction found no published statement implying this classification. General facts about idempotent lifting and sections of finite étale morphisms supply proof ingredients but not the stated consequence for Chen's covering criterion.

## Limitations
This result treats only the minimal nonreduced excess \(r-s=1\). For larger excess, a higher-rank nilradical need not square to zero, and the action on it need not force a trivial étale component by the same argument.

The result assumes a reduced base. It does not classify nilpotent structure inherited from a nonreduced base and makes no positive-characteristic claim.

A residual literature risk is that an equivalent rank-one finite-algebra lemma may appear in older commutative-algebra or finite-flat-scheme literature under different terminology.

## References
1. Rizeng Chen, *An Effective Criterion for Covering Maps Between Real Varieties*, arXiv:2602.21708v3, 2026; especially Proposition 3.1 and Theorem 3.3, Steps 1--5.
2. Rizeng Chen, *What Kind of Morphisms Induces Covering Maps over a Real Closed Field?*, arXiv:2502.05834v3, 2025; motivating double-line example and the predecessor reduction theorem.
3. The Stacks Project, Tag 00J9, idempotents lift uniquely through locally nilpotent ideals.
