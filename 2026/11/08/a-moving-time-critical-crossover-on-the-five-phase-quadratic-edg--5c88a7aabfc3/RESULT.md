# A moving-time critical crossover on the five-phase quadratic edge cycle

## Finding
For the symmetric permuted-Volterra quadratic stochastic map of Ganikhodjaev, Pah and Rozikov, an invariant one-dimensional edge returns after five applications. Its return map is **exactly the fifth iterate of one scalar quadratic**. This exposes a sharp singular boundary between geometric and double-exponential attraction, together with a moving-observation-time critical profile.

Fix \(s\in(0,1)\), put \(t_0=1-s\), and fix \(c>0\). For each sufficiently large integer \(n\), set
\[
q_n=\frac{t_0^{32^n}}{c},\qquad p_n=1-q_n.
\]
Initialize the five-component map at \((s,1-s,0,0,0)\), with parameter \(p_n\) fixed throughout that trajectory, and write \(S_j^{(n)}\) for its **first coordinate at time \(j\)**. Then
\[
\lim_{n\to\infty}\frac{1-S_{5n}^{(n)}}{q_n}=c,
\]
and for every *fixed* integer \(\ell\ge1\),
\[
\boxed{\lim_{n\to\infty}\frac{1-S_{5(n+\ell)}^{(n)}}{q_n^{5\ell+1}}=c+c^2.}
\]
The exponent \(5\ell+1\) and two-term coefficient identify the crossover when the parameter distance \(1-p_n\) is on the same scale as the unperturbed, doubly exponentially small distance to the vertex cycle at time \(5n\). These assertions concern edge initial states and the specified joint parameter/time limit, not generic interior populations.

At the exactly singular parameter \(p=1\), all positive integers \(n\) satisfy
\[
1-S_{5n}=(1-s)^{32^n},
\]
whereas for fixed \(0<p<1\), successive five-step deficits have limiting ratio \((1-p)^5\). At \(p=-1\) the companion endpoint law is \(S_{5n}=s^{32^n}\).

## Assumptions and scope
Use the symmetric five-dimensional stochastic map \(W_p\), \(-1\le p\le1\), defined by
\[
\begin{aligned}
x'_1&=x_5[1+p(x_1-x_2+x_3-x_4)],\\
x'_2&=x_1[1+p(x_2-x_3+x_4-x_5)],\\
x'_3&=x_2[1-p(x_1-x_3+x_4-x_5)],\\
x'_4&=x_3[1+p(x_1-x_2+x_4-x_5)],\\
x'_5&=x_4[1-p(x_1-x_2+x_3-x_5)].
\end{aligned}
\]
The state space is the simplex \(x_i\ge0\), \(\sum_{i=1}^5x_i=1\). For the edge \(E_{12}=\{(s,1-s,0,0,0):0\le s\le1\}\), five iterations return to the same edge. Superscript \((n)\) labels the separate trajectory with the \(n\)-dependent parameter \(p_n\). The offset \(\ell\) stays fixed when \(n\to\infty\). No statement uniform in growing \(\ell\) is claimed.

## Proof
**1. The hidden fifth iterate.** The five-step first-coordinate return for this edge is expressed in the originating work as \(F_p=h_p\circ g_p\circ f_p\circ f_p\circ f_p\), where
\[
f_p(z)=z[1+p(1-z)],\quad g_p(z)=(1-z)(1-pz),\quad h_p(z)=(1-z)(1+pz).
\]
Direct calculation gives \(g_p(z)=1-f_p(z)\) and \(h_p(z)=f_p(1-z)\), hence \(h_p\circ g_p=f_p\circ f_p\). Consequently the full edge return is **exactly** \(F_p=f_p^{\circ5}\). Induction then gives \(S_{5r}=f_p^{\circ5r}(s)\) for all nonnegative integers \(r\).

**2. Deficit dynamics and singular endpoints.** Set \(q=1-p\) and \(t=1-z\). One step of the scalar map obeys
\[
1-f_p(1-t)=T_q(t),\qquad T_q(t)=qt+(1-q)t^2.
\]
Thus \(1-S_{5r}=T_q^{\circ5r}(t_0)\) exactly. For \(p=1\) one has \(q=0\) and \(T_0(t)=t^2\), giving the stated exponent \(2^{5r}=32^r\). For \(p=-1\), \(f_{-1}(z)=z^2\), giving the stated companion formula. For fixed \(0<p<1\), \(q\in(0,1)\), \(T_q(t)<t\) for \(t\in(0,1)\), so \(T_q^{\circ j}(t_0)\to0\), and \(T_q(t)/t\to q\) as \(t\to0\). Taking five consecutive ratios gives the five-step limiting factor \(q^5\).

**3. An explicit uniform moving-time estimate.** Write \(m=5n\), \(v_j=t_0^{2^j}\), \(q=q_n=v_m/c\) and \(t_j=T_q^{\circ j}(t_0)\). For sufficiently large \(m\), \(0<q<1\). Because \(T_q(t)-t^2=qt(1-t)\ge0\) on \([0,1]\), induction gives \(t_j\ge v_j\). Put \(\delta_j=\log(t_j/v_j)\ge0\). Exact iteration yields
\[
\delta_{j+1}=2\delta_j+\log\left(1+q\frac{1-t_j}{t_j}\right)
\le2\delta_j+\frac q{v_j}.
\]
Since \(v_j\ge v_{m-1}=\sqrt{v_m}\) for \(0\le j<m\), repeated substitution gives the **explicit bound**
\[
0\le\delta_m\le \frac{(2^m-1)\sqrt{v_m}}{c}
=\frac{(2^m-1)t_0^{2^{m-1}}}{c}\longrightarrow0.
\]
Therefore \(t_m/v_m\to1\), and since \(v_m=cq\), the first asserted limit follows.

**4. Critical profile at and beyond the transition.** The next scalar step satisfies
\[
\frac{t_{m+1}}{q^2}=\frac{t_m}{q}+(1-q)\left(\frac{t_m}{q}\right)^2\longrightarrow c+c^2.
\]
For every fixed integer \(r\ge1\), if \(t_{m+r}/q^{r+1}\to c+c^2\), then
\[
\frac{t_{m+r+1}}{q^{r+2}}=
\frac{t_{m+r}}{q^{r+1}}+(1-q)q^r
\left(\frac{t_{m+r}}{q^{r+1}}\right)^2\longrightarrow c+c^2.
\]
Induction gives this limit for all fixed \(r\ge1\). Taking \(r=5\ell\) completes the theorem. The coefficient is nonzero for \(c>0\), so the stated power is sharp.

## Verification
The accompanying `check_edge_crossover.py` tests the five-step decomposition against the full five-coordinate map with exact rational arithmetic, corroborates the displayed elementary identities at rational test cases, and numerically checks the moving-time estimates with high-precision decimal arithmetic for increasing return horizons. The infinite-limit proof is the induction and explicit inequality above; the numerical output is corroboration, not a replacement for proof.

To reproduce from the containing directory, run `python3 check_edge_crossover.py`. No external Python packages are needed.

## Relationship to prior work
Ganikhodjaev–Pah–Rozikov introduced this symmetric permuted Volterra operator, the invariant edge-cycle and the composition \(h_p\circ g_p\circ f_p^{\circ3}\), and established qualitative edge convergence and fixed-parameter derivative \(F_p'(1)=(1-p)^5\). Those are prior results. The new quantitative claim is **the simultaneous divergent-time/vanishing-parameter limit**, including the exact \(q^{5\ell+1}\) scale, nonlinear coefficient \(c+c^2\), and an explicit error bound at the transition. The algebraic collapse of the five-step return is used as a proof device, not treated alone as the principal novel theorem.

General theory of one-dimensional polynomial iteration and local superattracting dynamics supplies context, but fixed-parameter stability does not yield this nonuniform joint limit. Literature searches did not identify an equivalent moving-time result for this operator; this is evidence-limited, not proof of publication priority.

## Limitations
Only a naturally invariant one-dimensional boundary edge is analyzed; no result on generic interior simplex orbits is asserted. The critical path tunes \(p_n\) in dependence on the observation horizon and fixed initial condition; it is not a claim about one fixed parameter as \(n\to\infty\). The offset \(\ell\) must remain fixed. The originating journal article was available through metadata, while its matching lawful arXiv preprint was inspected in detail. Equivalent statements in unindexed literature remain possible.

## References
1. N. N. Ganikhodjaev, C. H. Pah, U. A. Rozikov, *Dynamics of quadratic operators generated by China's Five elements philosophy*, arXiv:1908.07740, first public 2019-08-21; https://arxiv.org/abs/1908.07740 (especially Section 4.3, Eq. 4.11 and Proposition 5).
2. N. N. Ganikhodjaev, C. H. Pah, U. Rozikov, *Dynamics of quadratic stochastic operators generated by China's five element philosophy*, Journal of Difference Equations and Applications 27 (2021), 1173–1192, DOI 10.1080/10236198.2021.1968385 (journal version of reference 1).
