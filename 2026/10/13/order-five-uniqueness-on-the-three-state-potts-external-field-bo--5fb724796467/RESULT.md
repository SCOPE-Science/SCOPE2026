# Order-five uniqueness on the three-state Potts external-field boundary

## Finding
For the three-state ferromagnetic Potts model with constant external field on the Cayley tree of order \(k=5\), use the notation of Bogachev and Rozikov and let \(\alpha_1(\theta)\) be their exceptional boundary field. For every
\[
\frac32<\theta\le\frac{\sqrt{11}}2,
\]
the positive system (2.33) of the source at \(\alpha=\alpha_1(\theta)\) has exactly one solution,
\[
(u,v)=\left(\frac{4\theta-2}{5},1\right).
\]
Equivalently, the source function \(K_1(v;\theta)\) has its unique global maximum on \(\mathscr V_1^+(\theta)\) at \(v=1\). Hence Conjecture 2.1 of the source holds for the first previously unresolved order \(k=5\).

## Assumptions and scope
The model, variables, and reduction are those of Bogachev--Rozikov for \(q=3\), constant external field, ferromagnetic interaction, and completely homogeneous splitting Gibbs measures. Set
\[
t=\theta-1,\qquad p(v)=v+v^2+v^3+v^4,
\]
\[
L(v;t)=t\,p(v)-v^5-1,\qquad S(v)=p(v)+1,
\]
and
\[
K(v;t)=\frac{L(v;t)S(v)^5}{(p(v)+L(v;t))^5}.
\]
This is the source function \(K_1(v;\theta)\) with \(k=5\). Its positive domain is
\[
\mathscr V_1^+(\theta)=\{v>0:L(v;\theta-1)>0\}.
\]
For \(k=5\), the source values become
\[
\theta_1=\frac32,\qquad \widetilde\theta_1=\frac{\sqrt{11}}2,
\]
so the nontrivial boundary segment is exactly \(3/2<\theta\le\sqrt{11}/2\).

## Proof
Differentiate the displayed rational function directly. On the positive domain,
\[
K'(v;t)=\frac{S(v)^4}{(p(v)+L(v;t))^6}P(v;t),
\]
where
\[
P=S(p-4L)L'+5L(L-1)p'.
\]
An exact factorization is
\[
P(v;t)=(v-1)(v+1)v^5\,R(v+v^{-1};t),
\]
with
\[
\begin{aligned}
R(y;t)={}&4t^2y^4+11t^2y^3+8t^2y^2+8t^2y\\
&-4ty^5+2ty^4+33ty^3+34ty^2+44ty+8t\\
&-10y^5-20y^4+10y^3+20y^2+50y+30.
\end{aligned}
\]
Put \(z=y-2\). Since \(y=v+v^{-1}\ge2\), one has \(z\ge0\), with \(z=0\) exactly at \(v=1\). Expanding gives
\[
\begin{aligned}
R(2+z;t)={}&50(4t^2+8t-7)\\
&+10(30t^2+32t-119)z\\
&+10(17t^2-4t-120)z^2\\
&+(43t^2-111t-550)z^3\\
&+2(t-12)(2t+5)z^4-2(2t+5)z^5.
\end{aligned}
\]
The upper endpoint is
\[
t_*=\frac{\sqrt{11}-2}{2}<1,
\]
and it satisfies \(4t_*^2+8t_*-7=0\). Thus for \(0\le t\le t_*\) the constant coefficient above is nonpositive. Every other displayed coefficient is strictly negative: using \(0\le t<1\),
\[
30t^2+32t-119\le-57,
\]
\[
17t^2-4t-120\le-103,
\]
\[
43t^2-111t-550\le-507,
\]
while \(2(t-12)(2t+5)<0\) and \(-2(2t+5)<0\). Therefore
\[
R(2+z;t)<0\qquad(z>0,\ 0\le t\le t_*).
\]
For \(v>1\), all factors in the derivative except \(R\) are positive, so \(K'(v;t)<0\) throughout the physical domain. The exact reciprocal identities
\[
p(v^{-1})=v^{-5}p(v),\qquad L(v^{-1};t)=v^{-5}L(v;t)
\]
and
\[
S(v^{-1})=v^{-4}S(v),\qquad p(v^{-1})+L(v^{-1};t)=v^{-5}(p(v)+L(v;t))
\]
imply
\[
K(v^{-1};t)=K(v;t).
\]
Hence \(K\) increases toward \(v=1\) from the left and decreases strictly from \(v=1\) to the right. Thus \(v=1\) is its unique global maximizer on \(\mathscr V_1^+(\theta)\).

At the boundary field \(\alpha_1(\theta)\), the source reduction is reversible and sets \(\theta^{\alpha_1}=K_1^*(\theta)\). Uniqueness of the maximizer therefore forces \(v=1\). The source reconstruction formula then gives
\[
u=\frac{p(1)+L(1;t)}{p(1)+1}=\frac{4\theta-2}{5}.
\]
This is exactly the solution stated in Conjecture 2.1 for \(k=5\).

## Verification
The accompanying `verify.py` uses integer-coefficient polynomial arithmetic only. It reconstructs \(P\) from \(p\), \(L\), and the derivative formula; independently substitutes \(y=v+v^{-1}\) into \(R\); verifies the complete factorization coefficient by coefficient; and checks the exact expansion after \(y=2+z\). These checks verify algebraic identities, while the global sign argument above is the proof of uniqueness.

## Relationship to prior work
Bogachev--Rozikov state Conjecture 2.1 for all orders and prove the needed global maximizer statement only for \(k=2,3,4\). Their Appendix B gives a reciprocal-polynomial strategy and implements it separately for those three orders. A 2021 survey by Rozikov still states that the corresponding “only if” result is known at least for \(k=2,3,4\). The present factorization supplies the next order, \(k=5\), by turning the reciprocal derivative into a polynomial in \(z=v+v^{-1}-2\) whose coefficients have uniform sign on the whole critical interval.

## Limitations
The result is confined to \(q=3\), \(k=5\), constant external field, and the completely homogeneous splitting-Gibbs-measure reduction of the cited source. It does not prove Conjecture 2.1 for \(k\ge6\), does not classify nonhomogeneous or periodic boundary laws, and does not assert uniqueness of every Gibbs measure outside the source's reduction.

## References
1. L. V. Bogachev and U. A. Rozikov, *On the uniqueness of Gibbs measure in the Potts model on a Cayley tree with external field*, arXiv:1903.11440v1, first posted 2019-03-27; DOI:10.1088/1742-5468/ab270b.
2. U. A. Rozikov, *Gibbs measures of Potts model on Cayley trees: a survey and applications*, arXiv:2103.07391v1, 2021.
