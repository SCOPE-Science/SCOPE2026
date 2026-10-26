# Exact limiting event interval for a defective Jordan feedback pair

## Finding
Fix \(a,\gamma>0\) and
\[
J=\begin{pmatrix}-a&\gamma\\0&-a\end{pmatrix}.
\]
Consider the plant \(\dot x=u\) with static feedback \(u=J\hat x\), where \(\hat x(t)=x_k:=x(t_k)\) is held constant on \([t_k,t_{k+1})\). The next event is the first time \(s\ge T\) for which
\[
\|x_k-x(t_k+s)\|_2\ge\sigma\|x(t_k+s)\|_2,
\]
with \(\sigma>0\) and minimum wait \(T\ge0\).

Let \(L=\|J\|_2\) and \(m=\sigma_{\min}(J)>0\). Choose any \(\delta\) satisfying
\[
0<\delta<\min\{a^{-1},L^{-1}\},
\]
and choose parameters
\[
0<\sigma<\frac{\delta m}{1+\delta L},\qquad 0\le T<\delta.
\]
Then every nonzero initial state generates infinitely many events without Zeno accumulation, and its inter-event intervals satisfy the exact limit
\[
\boxed{\lim_{k\to\infty}(t_{k+1}-t_k)=\max\left\{T,\frac{\sigma}{a(1+\sigma)}\right\}.}
\]
The limit is independent of the Jordan shear \(\gamma\), although \(\gamma\) affects the transient. In particular, the exact unregularized limit is \(\sigma/[a(1+\sigma)]=\sigma/a-\sigma^2/a+O(\sigma^3)\), refining the leading-order estimate \(\sigma/a+O(\sigma^2)\).

## Assumptions and scope
All norms are Euclidean. The closed-loop matrix in the ideal continuous-feedback model is the defective Hurwitz Jordan matrix \(J\), with repeated eigenvalue \(-a\) and one-dimensional eigenspace. The plant, controller, and trigger are exactly those stated above; this is not a theorem for every plant whose closed-loop matrix has a defective eigenvalue. The zero initial state is excluded. The smallness assumptions are explicit and sufficient, not claimed necessary.

## Proof
For a held sample \(x\ne0\), the flow is \(x(s)=(I+sJ)x\), so the trigger function is
\[
g_x(s)=\frac{s\|Jx\|_2}{\|(I+sJ)x\|_2}.
\]
For \(0\le s< L^{-1}\), the denominator is nonzero and differentiation gives
\[
g_x'(s)=\frac{\|Jx\|_2\bigl(\|x\|_2^2+s x^\top Jx\bigr)}{\|(I+sJ)x\|_2^3}>0,
\]
because \(x^\top Jx\ge-L\|x\|_2^2\) and \(sL<1\). Thus there is at most one threshold crossing before \(\delta\).

Write \(\rho_\sigma(x)\) for that crossing. The bounds
\[
\frac{\sigma}{L(1+\sigma)}\le\rho_\sigma(x)\le\frac{\sigma}{m-\sigma L}<\delta
\]
hold uniformly in \(x\ne0\). For the lower bound, if \(s<\sigma/[L(1+\sigma)]\), then \(s\|Jx\|_2\le sL\|x\|_2<\sigma(1-sL)\|x\|_2\le\sigma\|(I+sJ)x\|_2\). For the upper bound, at \(s_+=\sigma/(m-\sigma L)\), one has \(s_+\|Jx\|_2\ge s_+m\|x\|_2=\sigma(1+s_+L)\|x\|_2\ge\sigma\|(I+s_+J)x\|_2\). The stated parameter restriction makes \(s_+<\delta\). Consequently the actual interval from sample \(x_k\) is \(\tau_k:=t_{k+1}-t_k=\max\{T,\rho_\sigma(x_k)\}\), and
\[
c:=\frac{\sigma}{L(1+\sigma)}\le\tau_k<\delta.
\]

The sampled-state recurrence is \(x_{k+1}=(I+\tau_kJ)x_k\). Put \(p_k=1-a\tau_k\) and \(q_k=\gamma\tau_k\). The bounds imply \(0<p_k<1\) and \(q_k\ge\gamma c>0\), and the coordinates obey
\[
x_{k+1,1}=p_kx_{k,1}+q_kx_{k,2},\qquad x_{k+1,2}=p_kx_{k,2}.
\]
Also \(\det(I+\tau_kJ)=p_k^2>0\), so a nonzero sample never becomes zero.

When \(x_{k,1}\ne0\), define the projective ratio \(r_k=x_{k,2}/x_{k,1}\). If \(r_k>0\), then
\[
r_{k+1}=\frac{p_kr_k}{p_k+q_kr_k}\in(0,r_k).
\]
If \(r_k<0\) and \(p_k+q_kr_k>0\), then \(r_{k+1}<0\) and
\[
|r_{k+1}|-|r_k|=\frac{q_k|r_k|^2}{p_k-q_k|r_k|}\ge\gamma c\,|r_k|^2.
\]
Hence the magnitude cannot remain negative and bounded indefinitely: while the denominator is positive, the magnitude increases by at least the fixed positive amount \(\gamma c|r_0|^2\). Eventually \(p_k+q_kr_k\le0\), which makes the next ratio positive, or makes the next first coordinate zero; in the latter case the following ratio is \(p_{k+1}/q_{k+1}>0\). If \(x_{k,1}=0\) initially, the next ratio is positive directly. Thus every nonzero initial state eventually has \(r_k>0\).

Thereafter \(r_k\) decreases to a limit \(r_\infty\ge0\). If \(r_\infty>0\), then
\[
r_k-r_{k+1}=\frac{q_kr_k^2}{p_k+q_kr_k}
\]
is bounded below by a positive constant, since \(q_k\ge\gamma c\), \(r_k\ge r_\infty\), and \(p_k+q_kr_k\le1+\gamma\delta r_1\). This is impossible, so \(r_k\to0\). The sampled directions therefore converge projectively to the eigenline spanned by \(e_1=(1,0)^\top\).

The crossing \(\rho_\sigma(x)\) depends continuously on the projective direction because \(g_x(s)\) is continuous and strictly increasing on \([0,\delta]\). At \(e_1\), \(Je_1=-ae_1\) and \(\|(I+sJ)e_1\|_2=1-as\); hence the threshold equation is \(as=\sigma(1-as)\), whose unique root is \(s=\sigma/[a(1+\sigma)]\). It follows that \(\rho_\sigma(x_k)\to\sigma/[a(1+\sigma)]\), and therefore \(\tau_k=\max\{T,\rho_\sigma(x_k)\}\) converges to the claimed limit.

Finally, \(\tau_k\ge c>0\) rules out Zeno accumulation. Since \(p_k\le1-ac<1\), products of the upper-triangular update matrices have diagonal entries decaying geometrically and off-diagonal entries bounded by a constant times \(k(1-ac)^{k-1}\). Thus the sampled states, and the inter-event flow between them, decay exponentially under these parameter restrictions.

## Verification
The proof uses the exact held-input flow and the exact trigger equation; no finite experiment is used to infer an infinite-time limit. The key nonstandard step is the projective recurrence, which shows that the defective Jordan shear sends every nonzero initial direction to the eigendirection. At that direction the trigger equation is solved exactly. The uniform root bounds also prove a positive minimum interval and keep every interval below \(\delta\).

## Relationship to prior work
Postoyan, Sanfelice, and Heemels (2019) give the leading-order expansion \(\tau_\sigma(x)=\sigma\|x\|_2/\|Jx\|_2+O(\sigma^2)\) and treat a semisimple repeated eigenvalue, but explicitly leave the repeated eigenvalue with geometric multiplicity one untreated. Their 2023 time-regularized extension likewise states the defective case as a conjecture, suggesting convergence near \(\max\{T,\sigma/a\}\) on the basis of the general \(O(\sigma^2)\) estimate and simulations. The present result proves the convergence for the canonical realization \(\dot x=J\hat x\) and identifies its exact limit \(\max\{T,\sigma/[a(1+\sigma)]\}\). It does not claim to resolve the conjecture for arbitrary defective closed-loop systems.

## Limitations
The result applies to the specified two-dimensional zero-order-hold realization and to the stated sufficient smallness conditions. It does not classify arbitrary plants \(\dot x=Ax+Bu\), general defective matrices \(A+BK\), nonlinear systems, measurement noise, or perturbed trigger rules. The exact formula is not claimed to be the only possible limit for other implementations. Independent validation has not been performed.

## References
1. R. Postoyan, R. G. Sanfelice, and W. P. M. H. Heemels, “Inter-event Times Analysis for Planar Linear Event-triggered Controlled Systems,” 2019 IEEE Conference on Decision and Control, pp. 1662–1667. DOI: 10.1109/CDC40024.2019.9028888. First public conference date: 2019-12-11.
2. R. Postoyan, R. G. Sanfelice, and W. P. M. H. Heemels, “Explaining the ‘Mystery’ of Periodicity in Inter-Transmission Times in Two-Dimensional Event-Triggered Controlled Systems,” IEEE Transactions on Automatic Control 68(2), 912–927. DOI: 10.1109/TAC.2022.3147009. Published online 2022-01-31.
