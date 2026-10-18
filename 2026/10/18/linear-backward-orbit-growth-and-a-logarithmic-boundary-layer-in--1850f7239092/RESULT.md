# Linear backward-orbit growth and a logarithmic boundary layer in discrete Huygens stars

## Finding

Let \(d\ge 2\) and consider the unit-weight star Huygens phase map on \(\mathbb T^d=(\mathbb R/2\pi\mathbb Z)^d\),
\[
G_h(z)=z+h(I_d+\mathbf1\mathbf1^{\mathsf T})\sin z\pmod{2\pi}.
\]
Write \(p=(\pi,\ldots,\pi)\), \(p_t=p+t\mathbf1\), and let \(N_n(t)=\#G_h^{-n}(\{p_t\})\), the number of *distinct* \(n\)-step ancestors. For
\[
\frac1{d+1}<h<\frac2{d+1},\qquad c=(d+1)h\in(1,2),
\]
all inverse ancestors of every \(p_t\) belong to the diagonal circle \(p+\mathbb T\mathbf1\). For every integer \(n\ge0\),
\[
\boxed{N_n(0)=2n+1.}
\]
For each \(t\not\equiv0\pmod{2\pi}\), the sequence \(N_n(t)\) eventually stabilizes to a finite \(N_\infty(t)\). Near the exceptional target, its exact leading logarithmic divergence is
\[
\boxed{N_\infty(t)=\frac{2\log(1/|t|)}{\log(1/(c-1))}+O_c(1)\qquad(t\to0,\ t\ne0).}
\]
These laws are independent of \(d\) after fixing \(c\). By contrast, for \(0<h\le1/(d+1)\), \(N_n(t)=1\) for all diagonal targets and all \(n\). The threshold \(h=1/(d+1)\) therefore marks exact inverse-fiber proliferation, even though the all-opposition equilibrium remains attracting in the asserted supercritical interval.

## Assumptions and scope

All counts refer to distinct points on the entire phase torus, not merely ancestors known in advance to lie on the diagonal. The unit-weight star has one central vertex and \(d\) leaves, and the edge orientation is chosen outward from its centre. Under translation \(z=p+u\), the update becomes
\[
F_h(u)=u-h(I_d+\mathbf1\mathbf1^{\mathsf T})\sin u\pmod{2\pi}.
\]
Here \(\sin\) operates componentwise. In the supercritical range \(c\in(1,2)\), put
\[
s_c=\arccos(1/c),\qquad a_c=\sqrt{c^2-1}-s_c.
\]
Both are positive, and \(0<a_c<s_c<\pi\). The scalar diagonal restriction is \(f_c(u)=u-c\sin u\), represented on \([-\pi,\pi]\). At a critical target \(|t|=a_c\), coincident inverse branches are counted only once; the logarithmic statement is asymptotic for \(t\ne0\) and does not claim continuity of \(N_\infty\).

## Proof

**1. Entire inverse fibers are diagonal.** Suppose \(F_h(u)\equiv t\mathbf1\pmod{2\pi}\). Subtracting components yields
\[
(u_i-h\sin u_i)-(u_j-h\sin u_j)\equiv0\pmod{2\pi}.
\]
Since \(0<h<2/(d+1)\le2/3<1\), the circle map \(q_h(v)=v-h\sin v\) has derivative \(1-h\cos v>0\); it is a degree-one orientation-preserving diffeomorphism. Consequently all \(u_i\equiv u_j\) and \(u\) is diagonal. The diagonal circle is forward invariant, so applying this argument inductively proves that **every** iterated predecessor of \(p_t\) is diagonal. There it is enough to count \(f_c^{-n}(t)\).

**2. Shape of the scalar inverse.** For \(1<c<2\), \(f_c'(v)=1-c\cos v\), with exactly two turning points \(\pm s_c\) on \((-\pi,\pi)\). Direct evaluation gives \(f_c(-s_c)=a_c\), \(f_c(s_c)=-a_c\), and \(f_c(\pm\pi)=\pm\pi\). The map sends \([-\pi,\pi]\) into itself and takes no value differing by \(2\pi\) from its target there. For \(|t|<a_c\) there are precisely three inverse points: one central in \((-s_c,s_c)\) and two outer in \((-\pi,-s_c)\cup(s_c,\pi)\); for \(|t|=a_c\) there are two distinct inverse points, while for \(a_c<|t|\le\pi\) there is just one circle inverse point. To see \(a_c<s_c\), write \(c=\sec s_c\); then \(s_c\in(0,\pi/3)\), and \(a_c=\tan s_c-s_c<s_c\) because \(\tan s<2s\) on \((0,\pi/3)\). Indeed the function \(2s-\tan s\) has a single interior maximum there and endpoint values \(0\) and \(2\pi/3-\sqrt3>0\).

**3. Linear growth at the sink.** Let \(b_1\in(s_c,\pi)\) be the unique positive, nonzero solution of \(f_c(b_1)=0\). It lies beyond \(s_c>a_c\). Let \(b_{j+1}\in(b_j,\pi)\) be the unique solution of \(f_c(b_{j+1})=b_j\), for \(j\ge1\). Existence and uniqueness follow because \(f_c\) increases strictly on \((s_c,\pi)\), while \(f_c(b_j)=b_{j-1}<b_j\) and \(f_c(\pi)=\pi\). Thus \(b_j\uparrow\pi\). The entire inverse fiber of \(0\) is \(\{0,\pm b_1\}\); each \(\pm b_j\) has exactly one predecessor \(\pm b_{j+1}\), since \(|b_j|>a_c\). Hence inductively
\[
f_c^{-n}(0)=\{0,\pm b_1,\ldots,\pm b_n\},
\]
which has exactly \(2n+1\) points. All points are distinct since \(b_j<\pi\).

**4. Finite counts away from the sink.** The two outer inverse points from any \(|t|<a_c\) have modulus \(>s_c>a_c\). Every such outer ancestor has only one inverse point, itself still on the same outer side with modulus increasing toward \(\pi\). Hence an outer ancestor can never branch again. A new pair of branches can only be created along the unique central inverse chain while its current argument lies in \((-a_c,a_c)\). On that chain, \(f_c\) is strictly decreasing, and if \(w\) is a central inverse of \(t\ne0\), then
\[
|t|=c\sin|w|-|w|\le(c-1)|w|,
\]
so \(|w|\ge |t|/(c-1)>|t|\). The central chain must leave \((-a_c,a_c)\) after finitely many iterations. Each earlier step creates two persistent outer branches, except at a critical target where two inverse branches coalesce; hence \(N_n(t)\) eventually stabilizes and is finite. If \(|t|>a_c\), no branch ever occurs, and \(N_n(t)=1\). The same is true for \(t=\pi\) modulo \(2\pi\).

**5. Exact logarithmic coefficient.** Denote by \(K(t)\) the number of strict, noncritical steps along the central inverse chain before its modulus first reaches or exceeds \(a_c\) (boundary equality affects the count by at most one). If the successive central inverse magnitudes are \(r_j\), the preceding expansion gives \(r_{j+1}\ge r_j/(c-1)\). At termination the last magnitude is bounded above by \(s_c\), so the geometric bound gives \(\sum_{j\le K(t)}r_j^2=O_c(1)\). Near zero,
\[
|f_c(w)|=(c-1)|w|\left(1-\frac{c}{6(c-1)}w^2+O_c(w^4)\right).
\]
Uniformly along the central chain with \(0<r_j\le s_c\), the difference between \(\log(r_{j+1}/r_j)\) and \(\log(1/(c-1))\) is \(O_c(r_{j+1}^2)\): the Taylor estimate handles a small fixed neighbourhood, and the remaining compact subinterval contributes a bounded amount because the chain crosses it in a bounded number of steps. Summing telescopically gives
\[
K(t)\log(1/(c-1))=\log(1/|t|)+O_c(1),
\]
since the terminal magnitude lies in a compact subinterval of \((0,s_c]\). Each strict central step adds exactly two outer predecessors; a possible critical merger changes the final total by at most one. Thus \(N_\infty(t)=2K(t)+O(1)\), proving the claimed asymptotic.

**6. Sharp onset.** If \(0<c\le1\), then \(f_c'(w)=1-c\cos w\ge0\), with strict monotonicity even at \(c=1\). Thus it is an orientation-preserving circle homeomorphism. Step 1 also applies because \(h<1\). Every diagonal target therefore has exactly one \(n\)-step preimage.

## Verification

The accompanying `check_preimages.py` independently partitions the scalar map at its exact critical points and locates roots numerically with bracketing. Across dimensions \(d=2,3,5,9\) and normalized couplings \(c=1.2,1.5,1.9\), it checks \(N_n(0)=2n+1\) for \(1\le n\le7\), confirms scalar reduction in the original network map, and tests fiber stabilization and the predicted logarithmic slope near zero. All twelve parameter combinations passed. Root-finding tolerance and finite loops are diagnostics only; the proof above covers all permitted dimensions, parameters, and iteration numbers.

Reproduction: run `python check_preimages.py` with Python 3, NumPy and SciPy installed. No input data or external network access is required.

## Relationship to prior work

Buescu, D'Aniello and Oliveira study the same reduced Huygens network and establish its gradient and Morse--Smale structure for \(h<1/(d+1)\) in the eligible star setting; their global invertibility criterion becomes sharp at that threshold. The present claim instead counts *all backward fibers* immediately above that loss of invertibility, at parameters \(1/(d+1)<h<2/(d+1)\). Its linear sink-fiber growth, finite generic fibers and singular logarithmic boundary layer are not stated in the inspected primary text. Classical degree-one sine circle maps give the scalar formalism; the novel network assertion includes the exclusion of off-diagonal ancestors. Schaeffer and McCalla's general step-size work on gradient descent addresses saddle avoidance, not the backward-fiber count; no such avoidance assertion is claimed here.

## Limitations

The theorem is specific to **equal edge weights** and diagonal target phases of a star. It does not assert corresponding formulas for arbitrary off-diagonal targets or arbitrary tree graphs, nor does it prove global Morse--Smale behavior beyond the paper's invertibility threshold. The limiting count is discontinuous at critical values; the \(O_c(1)\) bound is not uniform as \(c\downarrow1\) or \(c\uparrow2\). Search and source inspection cannot establish absolute novelty; an equivalent computation under older circle-map terminology remains a bibliographic risk. No independent audit has been performed.

## References

1. J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse--Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first publicly posted 2026-10-07), https://arxiv.org/html/2610.10993v1 .
2. H. Schaeffer and S. G. McCalla, *Extending the step-size restriction for gradient descent to avoid strict saddle points*, arXiv:1908.01753 (2019), https://arxiv.org/abs/1908.01753 .
3. E. Pia, *Kneading theory of the circle map*, Physical Review A 34 (1986), 574. Bibliographic background; only public abstract inspected, not asserted noncovering by full-text inspection.
