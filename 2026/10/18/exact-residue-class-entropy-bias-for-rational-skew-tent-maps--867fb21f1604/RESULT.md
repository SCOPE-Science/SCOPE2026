# Exact residue-class entropy bias for rational skew tent maps

## Finding

Let \(p,q\) be coprime positive integers and put \(L=p+q\). Define the full-branch skew tent map on \([0,1]\) by
\[
 f_{p,q}(x)=\begin{cases}
 (L/p)x,&0\le x\le p/L,\\
 (L/q)(1-x),&p/L<x\le1.
 \end{cases}
\]
For each integer \(N\ge1\), partition \([0,1]\) into \(N\) equal cells. At each step, independently sample a Lebesgue-uniform point from the current cell, apply \(f_{p,q}\), and record its new cell. Denote the stationary one-step Shannon entropy (natural logarithms) of this \(N\)-state Markov chain by \(H_N\).

**Exact finite-resolution law.** There is an explicitly computable array of real constants \(C_0,\ldots,C_{L-1}\), with \(C_0=0\), such that, for **every** \(N\ge1\),
\[
 \boxed{H_N=H_\infty+\frac{C_{N\bmod L}}{N}.}
\]
In particular, \(H_N=H_\infty\) whenever \(L\) divides \(N\), and the rate \(O(N^{-1})\) is optimal along \(N\equiv1\pmod L\) because \(C_1=-H_\infty<0\). The constants are computed by the finite overlap formula below, not by an asymptotic limit.

**Opposite signs occur at infinitely many resolutions.** For \((p,q)=(1,4)\),
\[
 H_\infty=\log5-\frac45\log2-\frac6{25}\log3
 \approx0.791253218705798,
\]
and, for every integer \(k\ge0\),
\[
 \boxed{H_{5k+4}=H_\infty+\frac{2\log(32/27)}{25(5k+4)}>H_\infty,}
\]
whereas
\[
 \boxed{H_{5k+1}=H_\infty-\frac{H_\infty}{5k+1}<H_\infty.}
\]
Thus finite-resolution coarse-grained entropy can lie **above or below** its zero-noise limit for infinitely many resolutions in the *same* expanding map. In particular, convergence need not be monotone or one-sided.

## Assumptions and scope

The state space is \([0,1]\), and \(p,q\) range independently over all coprime positive integers; the cells are the half-open intervals \(B_j=[j/N,(j+1)/N)\), with the final endpoint included. The transition matrix, with rows indexed by \(j\in\{0,\ldots,N-1\}\), is
\[
 P_{jk}=N\operatorname{Leb}\bigl(B_j\cap f_{p,q}^{-1}(B_k)\bigr).
\]
Because the two branches cover \([0,1]\) with inverse-Jacobian contributions \(p/L\) and \(q/L\), the map preserves Lebesgue measure and \(P\) is doubly stochastic. Therefore \(\pi_j=1/N\) is stationary, and
\[
 H_N=-\frac1N\sum_{j,k=0}^{N-1}P_{jk}\log P_{jk},\qquad 0\log0:=0.
\]
This is the entropy **rate of the independently resampled Markov chain**, not necessarily the entropy rate of a deterministic symbol sequence observed without resampling. Results here concern rational branch lengths; no formula is claimed for irrational breakpoints or arbitrary observation partitions.

Here is a finite rational-overlap specification of every constant. For \(s\in\{p,q\}\), set
\[
 I_{s,j}=[Lj/s,L(j+1)/s],\quad
 w_{s,j,k}=\frac{s}{L}\operatorname{Leb}\bigl(I_{s,j}\cap[k,k+1]\bigr),\quad
 e_s(j)=-\sum_{k\in\mathbb Z}w_{s,j,k}\log w_{s,j,k}.
\]
The sums have finite support; \(\sum_k w_{s,j,k}=1\). Write \(S_s(a)=\sum_{j=0}^{a-1}e_s(j)\) for \(a\ge0\), and \(\bar e_s=S_s(s)/s\). Then
\[
 \boxed{H_\infty=\frac{S_p(p)+S_q(q)}L.}
\]
For \(N\) not divisible by \(L\), let \(\tau=\{Np/L\}\in(0,1)\) and put
\[
 A=\frac Lp\tau,\qquad B=\frac Lq(1-\tau),
\]
\[
 u_k(\tau)=\frac pL\operatorname{Leb}([k,k+1]\cap[0,A])
 +\frac qL\operatorname{Leb}([k,k+1]\cap[0,B]),\qquad k\ge0,
\]
\[
 E_*(\tau)=-\sum_{k\ge0}u_k(\tau)\log u_k(\tau).
\]
Again the support is finite and \(\sum_k u_k=1\). With \(E_*(0)=0\), the **exact finite-resolution formula** is
\[
 \boxed{NH_N=S_p(\lfloor Np/L\rfloor)+S_q(\lfloor Nq/L\rfloor)+E_*(\{Np/L\}).}
\]
For \(r=1,\ldots,L-1\) define \(C_r=rH_r-rH_\infty\) using this finite formula; let \(C_0=0\). No arbitrary cutoffs or convergence assumptions enter this computation.

## Proof

**1. Stationary coarse-graining.** On the increasing branch the inverse image of an output interval has length \(p/L\) times its output length; on the decreasing branch the factor is \(q/L\). Consequently \(\operatorname{Leb}(f^{-1}(B_k))=\operatorname{Leb}(B_k)\), and every column of \(P\) sums to one. Every row sums to one because it is a conditional distribution. This proves the asserted stationary entropy formula.

**2. Complete cells.** Rescale the input and output by \(N\). An input cell fully inside the increasing branch, indexed by \(j\), is sent onto the rescaled interval \(I_{p,j}\); the pushforward density is \(p/L\). Its transition probabilities are precisely \(w_{p,j,k}\) and its row entropy is \(e_p(j)\). A cell fully inside the decreasing branch and \(k\) cells away from the right endpoint similarly has row entropy \(e_q(k)\). The number of full cells in the two branches is \(a=\lfloor Np/L\rfloor\) and \(b=\lfloor Nq/L\rfloor\).

**3. The unique crossing cell.** If \(L\mid N\), no cell crosses the turning point and \(a+b=N\). Otherwise \(a+b=N-1\), and the remaining cell straddles \(p/L\). Its increasing-branch fraction has rescaled length \(\tau\), and its decreasing-branch fraction has length \(1-\tau\). Both branch images end at rescaled output coordinate \(N\). Measure the output distance downward from this common endpoint. The two contributions occupy exactly \([0,A]\) and \([0,B]\), with constant densities \(p/L\) and \(q/L\). Their (possibly overlapping) masses in the unit output bins are exactly \(u_k(\tau)\). This proves the displayed finite-resolution formula, including \(N=1\) and the cases in which a branch breakpoint coincides with a cell boundary.

**4. Exact arithmetic periodicity.** The identity \(I_{s,j+s}=I_{s,j}+L\) translates every output bin by an integer, so \(e_s(j+s)=e_s(j)\). Therefore
\[
 S_p(a+p)=S_p(a)+S_p(p),\qquad S_q(b+q)=S_q(b)+S_q(q).
\]
Replacing \(N\) by \(N+L\) adds \(p\) and \(q\), respectively, to the two full-cell counts without changing \(\tau\). Hence, **exactly**,
\[
 (N+L)H_{N+L}-NH_N=S_p(p)+S_q(q)=LH_\infty.
\]
This recursion proves that \(N(H_N-H_\infty)\) is \(L\)-periodic for positive integer \(N\). At \(N=L\) there is no crossing cell, and the two sums comprise complete periods, so \(H_L=H_\infty\), giving \(C_0=0\). The formula for the other constants follows by taking the representatives \(N=1,\ldots,L-1\). Because \(H_1=0\) for a one-state Markov chain and \(H_\infty>0\) for this full-branch expanding family, \(C_1=-H_\infty\ne0\), proving the globally sharp \(1/N\) order.

**5. Exact sign change.** For \((p,q)=(1,4)\), write \(h(t)=-t\log t-(1-t)\log(1-t)\). The single increasing-branch row has entropy \(\log5\), and the four decreasing-branch rows have entropies
\[
 h(1/5),\quad h(2/5),\quad h(2/5),\quad h(1/5).
\]
Thus
\[
 H_\infty=\frac{\log5+2h(1/5)+2h(2/5)}5
 =\log5-\frac45\log2-\frac6{25}\log3.
\]
At \(N=4\), the crossing cell has output-bin probabilities \((1/5,1/5,1/5,2/5)\), with entropy \(\log5-(2/5)\log2\). The other three cells contribute \(h(1/5)+2h(2/5)\). Therefore
\[
 4H_4=\log5-\frac25\log2+h(1/5)+2h(2/5),
\]
and direct simplification gives
\[
 C_4=4(H_4-H_\infty)=\frac2{25}\log\frac{32}{27}>0.
\]
The recursion in step 4 extends this to all \(N\equiv4\pmod5\). At \(N=1\), entropy is zero, so \(C_1=-H_\infty<0\), extending likewise to all \(N\equiv1\pmod5\). The claimed infinitely repeated sign reversal follows.

## Verification

The accompanying standalone `verify.py` constructs all transition probabilities independently by exact rational intersection lengths in the **original input coordinate**. It checks row and column stochasticity, compares each directly computed row entropy with the overlap decomposition, and verifies the \(L\)-step additive recursion for 338 triples \((p,q,N)\) with coprime \(1\le p,q\le6\). It also checks the closed-form constants and both infinite arithmetic progressions for the explicit \((1,4)\) example at ten finite representatives. Execution: `python verify.py`, expected output beginning `VERIFY_OK`.

The program's finite checks are not the proof of the all-parameter statement; the exact rational geometry and periodicity argument above prove it for arbitrary coprime positive integers and all \(N\ge1\). Floating-point evaluation of logarithms is confined to consistency checks. The strict sign \(C_4>0\) follows symbolically from \(32>27\), not from numerical rounding.

## Relationship to prior work

Kouji Yano's *Entropy of random chaotic interval map with noise which causes coarse-graining* (arXiv:1205.1848, public from 2012-05-09) introduces the independently resampled Markov-chain entropy considered here. Theorem 4.1 and Section 5 prove and evaluate its \(N\to\infty\) limit for piecewise-linear and skew tent maps, including rational slopes. The calculation here uses the same object and recovers that limit. It adds an **exact equality for every finite \(N\)**, including the formerly discarded turning-point row, its complete residue-class fluctuation array, and an explicit family of resolutions at which the coarse-grained entropy overshoots its limit. Yano's finite-cell entropy identity (Equation 4.27) is closely related to the full-cell part of the present proof; this overlap is credited rather than presented as a new identity.

Studies of Markov coarse-graining spectra, e.g. MacKernan and Nicolis (1994), concern spectral decompositions of transfer operators for Markov partitions. Those are not statements about this independently resampled equal-cell Shannon entropy or its exact \(N\)-residue bias. Work on symbolic thresholds of the ordinary tent map concerns deterministic observation processes, without the independent within-cell resampling used here.

## Limitations

The explicit coefficients apply to **rational** turning points and equal-length cells. No convergence rate for irrational turning points is proved. The \(L\)-period is a valid period of the scaled error, but it is not asserted always to be its least positive period. The possible sign patterns of all \(C_r\) for arbitrary \((p,q)\) are not classified. The result concerns the entropy of the stationary resampled chain, not deterministic coarse-grained observations or topological entropy. The calculation is original to the present analysis to the extent of the inspected sources; it does not establish absolute historical priority against unindexed literature.

## References

1. K. Yano, *Entropy of random chaotic interval map with noise which causes coarse-graining*, arXiv:1205.1848 (first version 2012-05-09; inspected publicly accessible arXiv v2, 2012-06-28), Theorem 4.1, Equations (4.20)–(4.38), Section 5. https://arxiv.org/abs/1205.1848
2. D. MacKernan and G. Nicolis, *Generalized Markov coarse graining and spectral decompositions of chaotic piecewise linear maps*, Physical Review E **50** (1994), 988–999, DOI:10.1103/PhysRevE.50.988. Cited only for broader coarse-graining context; not used as a proof ingredient.
