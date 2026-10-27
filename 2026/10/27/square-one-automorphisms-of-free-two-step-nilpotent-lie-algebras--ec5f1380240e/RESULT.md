# Square-one automorphisms of free two-step nilpotent Lie algebras: a characteristic-dependent census

## Finding

Let \(k\) be a field, let \(d\ge2\), let \(V=k^d\), and let \(L_d=V\oplus\bigwedge^2 V\) have the class-two Lie bracket \([v+w,v'+w']=v\wedge v'\). Write \(w=\binom d2\). An **involution-inclusive square-one automorphism** is \(F\in\operatorname{Aut}_k(L_d)\) satisfying \(F^2=\operatorname{id}\); the identity is included. Over a finite field \(k=\mathbb F_q\), the number of nonidentity automorphisms of order exactly two is the displayed square-one count minus one.

**Odd characteristic.** For \(q\) odd, let \(a+b=d\) and define
\[
K_{a,b}=a^2b+b\left(\binom a2+\binom b2\right),\qquad
P_{d,a}(q)={d\brack a}_q q^{ab+K_{a,b}}.
\]
Here \({d\brack a}_q\) is the Gaussian binomial coefficient. The total square-one count is exactly \(\sum_{a=0}^d P_{d,a}(q)\). More strongly, over **every** field of characteristic different from two, square-one automorphisms have precisely \(d+1\) conjugacy classes, indexed by the dimension \(a\) of the \(+1\)-eigenspace of the induced map on \(L_d/[L_d,L_d]\cong V\). Each such automorphism has fixed-space dimension
\[
H_{d,a}=a+\binom a2+\binom{d-a}2.
\]
In particular, the sharp universal bound is
\[
\dim_k\operatorname{Fix}(F)\ge\left\lfloor d^2/4\right\rfloor.
\]
Equality holds at \(a=(d-1)/2\) when \(d\) is odd, and at \(a=d/2-1,d/2\) when \(d\) is even.

**Characteristic two.** For \(q\) even, define for each integer \(0\le r\le\lfloor d/2\rfloor\)
\[
s=d-2r,\quad t_2=2\binom r2+rs,\quad t_1=r+\binom s2,
\quad E_{d,r}=r(2t_2+t_1)+s(t_2+t_1).
\]
Then the exact square-one count is
\[
\boxed{\sum_{r=0}^{\lfloor d/2\rfloor}{d\brack r}_q{d-r\brack r}_q\,|\operatorname{GL}_r(\mathbb F_q)|\,q^{E_{d,r}}.}
\]
The summand indexed by \(r\) counts precisely those \(F\) for which the induced map on \(V\) is \(I+N\) with \(N^2=0\) and \(\operatorname{rank}N=r\). We use \(|\operatorname{GL}_0(\mathbb F_q)|=1\). In particular, the \(r=0\) term is \(q^{d\binom d2}\), which consists of all square-one central shears whose action on the abelianization is the identity. This produces a genuine change from the odd-characteristic semisimple classification.

## Assumptions and scope

The Lie algebra is the **free two-step nilpotent** Lie algebra on \(d\) generators, not an arbitrary class-two quotient. The exterior square is the usual alternating construction even in characteristic two. All statements about group conjugacy and fixed spaces apply to arbitrary fields of characteristic different from two. Enumerations apply to finite fields of any prime-power size. No claim about characteristic-two conjugacy classes or their complete fixed-space distribution is made. The formulas count actual linear automorphisms, not isomorphism types of Lie algebras.

## Proof

**1. Automorphism coordinates.** The derived ideal \([L_d,L_d]=\bigwedge^2 V\) is characteristic. Every automorphism is uniquely determined by an invertible linear map \(G\in\operatorname{GL}(V)\) and an arbitrary \(f\in\operatorname{Hom}(V,\bigwedge^2 V)\):
\[
F_{G,f}=\begin{pmatrix}G&0\\ f&\bigwedge^2G\end{pmatrix}.
\]
Conversely this block matrix preserves the bracket, because \([F(v),F(v')]=Gv\wedge Gv'=(\bigwedge^2G)(v\wedge v')\). Its determinant is nonzero. Put \(Q=\bigwedge^2G\). Matrix multiplication gives the necessary and sufficient conditions
\[
G^2=I,\qquad fG+Qf=0.
\tag{1}
\]
Thus the count is the sum, over square-one \(G\), of the cardinalities of linear solution spaces in \(f\).

**2. Odd characteristic.** If \(2\ne0\) in \(k\), the two eigenspaces \(V_+,V_-\) of \(G\) have dimensions \(a,b\). The induced operator \(Q\) is \(+I\) on \(\bigwedge^2V_+\oplus\bigwedge^2V_-\), of dimension \(B=\binom a2+\binom b2\), and \(-I\) on \(V_+\wedge V_-\), of dimension \(ab\). Equation (1) requires \(f(V_+)\subseteq V_+\wedge V_-\) and \(f(V_-)\subseteq\bigwedge^2V_+\oplus\bigwedge^2V_-\). Its solution space therefore has dimension \(a(ab)+bB=K_{a,b}\). There are \({d\brack a}_q\) choices of \(V_+\) and exactly \(q^{ab}\) complementary \(b\)-planes \(V_-\), so the count in this stratum is \(P_{d,a}(q)\).

For conjugacy, the central shear \(S_h=\begin{psmallmatrix}I&0\\h&I\end{psmallmatrix}\) sends \(F_{G,f}\) to \(F_{G,f+hG-Qh}\) under \(S_hF_{G,f}S_h^{-1}\). Since \(Qf=-fG\) and \(G^2=I\), the choice \(h=-\tfrac12 fG\) yields \(f+hG-Qh=0\). Thus each involution is conjugate to its split lift \(F_{G,0}\). Two split lifts are conjugate only if their induced \(G\) are conjugate; the \(G\)'s are classified by \(a\). This gives exactly \(d+1\) conjugacy classes over an arbitrary field of odd characteristic. The square-one map is semisimple, and its \(+1\)-eigenspace on \(L_d\) has dimension \(a+B=H_{d,a}\), independent of \(f\). Completing the square gives
\[
H_{d,a}=a^2-(d-1)a+\frac{d(d-1)}2,
\]
whose minimum over integral \(a\in[0,d]\) is \(\lfloor d^2/4\rfloor\) with the stated equality cases.

**3. Characteristic two.** Write \(G=I+N\). Then \(G^2=I\) if and only if \(N^2=0\). If \(r=\operatorname{rank}N\), the natural \(k[C_2]\)-module \(V\) decomposes into \(r\) two-dimensional Jordan blocks \(J_2\) and \(s=d-2r\) trivial blocks \(J_1\). As a \(k[C_2]\)-module, \(W=\bigwedge^2V\) decomposes into \(t_2\) blocks \(J_2\) and \(t_1\) blocks \(J_1\). Indeed, the exterior square of a single \(J_2\) is one \(J_1\), the tensor product of two distinct \(J_2\)'s is \(J_2\oplus J_2\), a tensor product \(J_2\otimes J_1\) is \(J_2\), and \(J_1\otimes J_1=J_1\). This gives
\[
t_2=2\binom r2+rs,\qquad t_1=r+\binom s2.
\]
Since \(-1=1\), equation (1) is precisely \(fG=Qf\), so the allowed \(f\)'s are module homomorphisms \(V\to W\). The elementary dimensions \(\dim\operatorname{Hom}_{k[C_2]}(J_1,J_1)=1\), \(\dim\operatorname{Hom}(J_1,J_2)=\dim\operatorname{Hom}(J_2,J_1)=1\), and \(\dim\operatorname{Hom}(J_2,J_2)=2\) yield \(\dim\operatorname{Hom}_{k[C_2]}(V,W)=E_{d,r}\).

To count \(N\) with \(N^2=0\) and rank \(r\), first choose its image \(U\) (\({d\brack r}_q\) choices), then its kernel \(K\supseteq U\) of dimension \(d-r\) (\({d-r\brack r}_q\) choices), then an isomorphism \(V/K\to U\) (\(|\operatorname{GL}_r(\mathbb F_q)|\) choices). For each such \(G=I+N\), precisely \(q^{E_{d,r}}\) maps \(f\) satisfy equation (1). Summation proves the even-characteristic formula.

## Verification

The standalone script `verify_involutions.py` implements matrix arithmetic, exterior squares and Gaussian elimination over small prime fields. It enumerates all candidate \(G\) and solves the linear condition \(fG+Qf=0\). For \(d=2\), it also exhaustively tests every central part \(f\) and checks the actual square-one identity on \(L_d\). For \(d=3\) over \(\mathbb F_2\), it performs that full \(f\)-enumeration as well. It yields the following square-one totals (including identity):

| \(d\) | \(q\) | Count | Verification |
| --- | --- | ---: | --- |
| 2 | 3 | 46 | exhaustive \(G,f\) |
| 2 | 5 | 176 | exhaustive \(G,f\) |
| 3 | 3 | 57,592 | exhaustive \(G\), linear-kernel verification for \(f\) |
| 2 | 2 | 10 | exhaustive \(G,f\) |
| 3 | 2 | 1,184 | exhaustive \(G,f\) |
| 4 | 2 | 19,357,696 | exhaustive \(G\), linear-kernel verification for \(f\) |

A successful run ends with `FREE_TWO_STEP_ALL_CHARACTERISTICS_OK`. The finite computations are checks, not a substitute for the uniform proof above.

## Relationship to prior work

Payne's 2008 study of automorphisms of free nilpotent Lie algebras examines induced eigenvalues and rational invariant subspaces in the Anosov setting, not exact finite-field square-one counts. Benito and Roldán-López's 2019 work describes the automorphism groups of free nilpotent Lie algebras via automorphisms induced on generators and unipotent automorphisms. This general structure supplies the natural starting coordinates but does not state the characteristic-two modular-Hom census, odd-characteristic conjugacy distribution, or sharp fixed-space bound derived here. Results on fixed-point-free automorphisms of Heisenberg Lie algebras concern a different condition and do not count square-one automorphisms of the free class-two family.

## Limitations

Originality is assessed against the cited and searched accessible literature and research records, not certified independently. A broader representation-theoretic enumeration might subsume the formulas indirectly; none was identified in the documented searches. Only \(d\ge2\) is asserted. The checker directly enumerates prime fields of small orders, whereas the proof covers all finite extension fields. Conjugacy classification and sharp fixed-dimension profiles in characteristic two are not claimed. Independent verification has not been performed.

## References

1. T. L. Payne, “Anosov Automorphisms of Nilpotent Lie Algebras,” arXiv:0809.3131v1, publicly submitted 2008-09-18. https://arxiv.org/abs/0809.3131
2. P. Benito and J. Roldán-López, “Derivations and automorphisms of free nilpotent Lie algebras and their quotients,” arXiv:1911.01897v1, publicly submitted 2019-11-05; especially Proposition 1, Corollary 1 and Remark 2. https://arxiv.org/abs/1911.01897
3. E. I. Khukhro, N. Yu. Makarenko and P. Shumyatsky, “Finite groups and Lie rings with an automorphism of order \(2^n\),” publicly deposited 2015-02-24. https://eprints.maths.manchester.ac.uk/2257/
