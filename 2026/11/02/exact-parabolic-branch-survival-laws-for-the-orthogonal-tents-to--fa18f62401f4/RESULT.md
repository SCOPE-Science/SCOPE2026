# Exact parabolic-branch survival laws for the orthogonal tents toral map

## Finding
Let \(\operatorname{Leb}\) denote normalized area on the two-torus. For the orthogonal-tent shear composition \(H\) and the strict neutral branch \(A_3\) defined below, write
\[
S_n=\operatorname{Leb}\bigl\{z\in A_3:H^j(z)\in A_3\text{ for }0\le j<n\bigr\}.
\]
Then \(S_1=1/4\) and for **every integer** \(k\ge1\),
\[
S_{2k}=\frac{2k-1}{4(4k-1)(4k-3)},\qquad
S_{2k+1}=\frac{k}{2(16k^2-1)}.
\]
In particular \(\lim_{n\to\infty}nS_n=1/16\). With initial probability \(\operatorname{Leb}(\cdot\mid A_3)\) and first exit \(\tau=\inf\{j\ge1:H^j(z)\notin A_3\}\),
\[
\Pr(\tau\ge n)=4S_n\sim\frac1{4n},\qquad \mathbb E[\tau]=\infty.
\]
The first-exit mass is \(\Pr(\tau=n)=4(S_n-S_{n+1})\sim1/(4n^2)\).

## Assumptions and scope
All coordinates lie in \([0,1)\) and are taken modulo one. Set
\[
F(x,y)=(x+2\min\{y,1-y\},y)\bmod1,\quad
G(x,y)=(x,y+2\min\{x,1-x\})\bmod1,\quad H=G\circ F.
\]
The neutral branch is exactly \(A_3=\{(x,y):1/2<y<1,\ 0<\{x-2y\}<1/2\}\). The braces denote fractional part. Singular lines and their preimages have zero area and can be ignored in the area formulas. No claim is made about global return to an inducing region or correlation coefficients.

## Proof
**Step 1: exact fiber coordinates.** The torus coordinate change \(t=(x-y)\bmod1\) with \(y\) unchanged has determinant one, so preserves area. For a point on \(A_3\), direct substitution into the two shears gives
\[
(t,y)\longmapsto(1-t,\,2t-y\bmod1).
\]
Write \(s=\min\{t,1-t\}\in(0,1/2)\). If \(t=s\), the allowable first-visit fiber is \(I_A(s)=(1/2+s,1)\). If \(t=1-s\), it is \(I_B(s)=(1/2,1-s)\). Each has length \(1/2-s\), giving \(S_1=2\int_0^{1/2}(1/2-s)\,ds=1/4\).

**Step 2: two-visit fibers and parabolic translation.** Substituting the first iterate into the opposite fiber gives (up to boundaries)
\[
J_A(s)=\begin{cases}(1/2+s,1/2+2s),&0<s\le1/4,\\(3s,1),&1/4<s<1/3,\\\varnothing,&s\ge1/3,\end{cases}
\]
\[
J_B(s)=\begin{cases}(1-2s,1-s),&0<s\le1/4,\\(1/2,3/2-3s),&1/4<s<1/3,\\\varnothing,&s\ge1/3.\end{cases}
\]
Two successive steps fix \(t\) and translate \(y\) by \(1-4s\) modulo one on side \(A\), and by \(4s-1\) modulo one on side \(B\). Already the existence of **four** consecutive visits forces \(1/5<s<2/7\): for \(s\le1/4\), adjacent two-visit fibers overlap only if \(1-4s<s\); for \(s\ge1/4\), they overlap only if \(4s-1<1-3s\). On these narrowed supports, the vertical drift has magnitude smaller than the initial two-visit interval, and no other mod-one lift can return to that interval at the next pair. Therefore successive pair constraints clip one endpoint monotonically; induction also covers all larger times. For the case \(n=2\), the explicit \(J_A,J_B\) above provide the starting step.

**Step 3: exact fiber widths.** On **each** of the two sides \(t=s\) and \(t=1-s\), the length of the surviving vertical fiber after \(2k\) consecutive visits is exactly
\[
w_{2k}(s)=\begin{cases}
\bigl[(4k-3)s-(k-1)\bigr]_+,&0<s\le1/4,\\
\bigl[k-(4k-1)s\bigr]_+,&1/4<s<1/2.
\end{cases}
\]
Here \([u]_+=\max\{u,0\}\). For \(2k+1\) visits, impose one further first-branch fiber condition after the \(k\)-th two-step translation; its width is
\[
w_{2k+1}(s)=\begin{cases}
\bigl[(4k-1)s-(k-1/2)\bigr]_+,&0<s\le1/4,\\
\bigl[k+1/2-(4k+1)s\bigr]_+,&1/4<s<1/2.
\end{cases}
\]
For completeness, the two-visit intersection on side \(A\) at \(s<1/4\) is \((1/2+s,1/2+2s)\); after \(k-1\) pair translations, its upper endpoint becomes \(1/2+2s-(k-1)(1-4s)\), and imposing the odd final visit replaces it by \(1-k(1-4s)\). For \(s>1/4\) the lower endpoint of \(J_A\) moves upward by \((k-1)(4s-1)\); the odd visit moves it to \(1/2+s+k(4s-1)\). On side \(B\), the opposite drift clips the opposite endpoints and yields exactly the same width formulas. This establishes the stated expressions for every integer \(k\ge1\).

**Step 4: exact integration.** Each width function is a triangle in \(s\), with its apex of height \(1/4\) at \(s=1/4\), and vanishes elsewhere. For even time its base runs from \((k-1)/(4k-3)\) to \(k/(4k-1)\); for odd time its base runs from \((2k-1)/(2(4k-1))\) to \((2k+1)/(2(4k+1))\). Integrating both equal-area sides yields
\[
S_{2k}=2\int_0^{1/2}w_{2k}(s)\,ds
=\frac14\left(\frac{k}{4k-1}-\frac{k-1}{4k-3}\right)
=\frac{2k-1}{4(4k-1)(4k-3)},
\]
\[
S_{2k+1}=2\int_0^{1/2}w_{2k+1}(s)\,ds
=\frac14\left(\frac{2k+1}{2(4k+1)}-\frac{2k-1}{2(4k-1)}\right)
=\frac{k}{2(16k^2-1)}.
\]
The limits for \(nS_n\), the first-exit distribution and divergence of \(\mathbb E[\tau]=\sum_{n\ge1}\Pr(\tau\ge n)\) follow immediately. This proves the theorem.

## Verification
The included `checker.py` compares the original two-shear map against the independently derived pointwise fiber inequalities using integer/rational arithmetic at 371046 test cases, with 198 further exact triangle-area identities. It is finite corroboration and does not substitute for the preceding proof. Run `python checker.py` from the extracted package. The first six areas are \(1/4,1/12,1/30,3/140,1/63,5/396\).

## Relationship to prior work
Myers Hill, Sturman and Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, arXiv:2303.08515, define the orthogonal-tents system and its neutral region \(A_3\), prove almost-sure escape in their equation (11), construct a detailed partition by escape times (Section 3, Figure 5 and Appendix), and establish \(O(1/n)\) mixing bounds. Their Section 6.2 uses triangular wedges to show sharp-order correlation obstructions. These achievements are not claimed as new. The present theorem instead evaluates the **entire consecutive-neutral-branch survivor law** exactly at each positive integer time, its leading constant, and the resulting first-exit distribution and divergent conditional mean. Their 2021 preprint arXiv:2112.07346 concerns a broader non-monotonic shear family, without the stated exact \(A_3\) survival formula.

## Limitations
Only the specified branch and consecutive stays are counted, not general visits after escape, return times to the induced section, or exact correlation coefficients. The formulas are for the exactly symmetric tent slopes \(2\), not arbitrary shear parameters. Although relevant primary texts were inspected and searches found no covering formula, wider unindexed publication priority remains unverified. Independent scientific validation has not been performed.

## References
1. J. Myers Hill, R. Sturman, M. C. T. Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, arXiv:2303.08515v1 (15 March 2023), especially Sections 3 and 6, Appendix 8.1. https://arxiv.org/abs/2303.08515
2. J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Continuous Family of Non-Monotonic Toral Mixing Maps*, arXiv:2112.07346v1 (14 December 2021); published as *A Family of Non-Monotonic Toral Mixing Maps*, J. Nonlinear Sci. 32 (2022), article 31. https://arxiv.org/abs/2112.07346
