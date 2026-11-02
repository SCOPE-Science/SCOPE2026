# Six cells are sharp for the two-plateau SSPRK3 Burgers entropy obstruction

## Finding

For the canonical periodic two-plateau construction of Liu, Jiang and Zhang [1], the smallest even number of cells producing an increase of *global cell-average exponential entropy* after one unlimited SSPRK3 DG step is **six** (rather than the twelve cells used to establish the published family). This sharp minimum holds at every dimensionless step \(0<s\le1/4\). For two and four cells, the updated cell means remain in the original interval and therefore do not produce global cell-average growth for *any* convex entropy. This smaller-grid conclusion is restricted to the specified two-plateau family, not a universal entropy-stability statement.

## Assumptions and scope

Solve Burgers' equation \(u_t+(u^2/2)_x=0\) on the periodic unit interval using \(N\ge2\) uniform cells, \(N\) even, piecewise linear DG with exact volume integrals, the standard three-stage SSPRK3 update without stage limiting, and the Lax--Friedrichs flux
\[
\widehat f(a,b)=\frac{a^2+b^2}{4}-\frac{\alpha}{2}(b-a),\qquad \alpha=\frac{3A}{2}.
\]

Set \(s\in(0,1/4]\), \(A=8/s^2\), \(h=1/N\), \(\Delta t=sh/A\). Initially set the first \(N/2\) cells to zero and the remaining \(N/2\) cells to \(A\). Thus the Courant parameter is \(\nu=\alpha\Delta t/h=3s/2\le3/8\). Express a stage polynomial on cell \(i\) as \(A(m_i+b_i\xi)\), \(-1\le\xi\le1\), and use periodic zero-based indexing.

The exponential entropy is \(U(u)=e^u\) with Burgers entropy flux \((u-1)e^u\). A terminal cell-average-preserving correction leaves every updated mean unchanged; if the total entropy of the means increases then no such correction and no periodic shared numerical entropy flux can enforce all weak cell entropy inequalities.

## Proof

**Exact recurrence.** Write the dimensionless flux at interface \(i+1/2\) as
\[
F_i=\frac{(m_i+b_i)^2+(m_{i+1}-b_{i+1})^2}{4}-\frac34[(m_{i+1}-b_{i+1})-(m_i+b_i)].
\]
The exact DG modal right-hand side (in units of \(A^2/h\)) is
\[
L_m(i)=F_{i-1}-F_i,\qquad L_b(i)=3m_i^2+b_i^2-3(F_{i-1}+F_i).
\]
For \(z=(m,b)\) the three stages therefore obey
\[
z^{(1)}=z^0+sL(z^0),\quad z^{(2)}=\tfrac34z^0+\tfrac14[z^{(1)}+sL(z^{(1)})],\quad z^+=\tfrac13z^0+\tfrac23[z^{(2)}+sL(z^{(2)})].\]
All stage and output coordinates are rational polynomials in \(s\). Periodic flux cancellation gives \(\sum_i m_i^+=N/2\).

**Positive side at six or more cells.** Let \(j=N/2+1\), the second initially high cell, and write \(m_j^+=1+\delta_N(s)\). Direct substitution in the displayed three-stage recurrence gives
\[
\begin{aligned}
\delta_6(s)&=\frac{s^2}{384}(528-1560s-392s^2+1545s^3+1158s^4-195s^5),\\
\delta_8(s)&=\frac{s^2}{384}(480-1320s-728s^2+1999s^3+578s^4+63s^5),\\
\delta_N(s)&=\frac{s^2}{24}(30-82s-46s^2+125s^3+36s^4+4s^5),\quad N\ge10\text{ even}.
\end{aligned}
\]
The last formula follows from the three-neighbor propagation radius of three DG evaluations and is the already published large-grid expression [1], additionally checked exactly at \(N=10,12\). Each of the three parentheses is greater, respectively, than \(528-1560/4-392/16-195/1024>96\), \(480-1320/4-728/16>96\), and \(30-82/4-46/16>6\). Hence \(\delta_N(s)>s^2/4\) for all even \(N\ge6\), and \(A m_j^+>A+2\).

To certify that the chosen constant LF speed is legitimate, convert every stage-input endpoint trace polynomial \(m_i\pm b_i\) to its Bernstein form on \(s\in[0,1/4]\). Its coefficients are all within \([-1/2,3/2]\) on each relevant stencil, for all even \(N\ge2\); exact rational verification of \(N=2,4,6,8,10,12\), together with stencil locality, covers all larger even meshes. Therefore every evaluated characteristic speed satisfies \(|u|\le3A/2=\alpha\).

For \(N=6,8,10\), a single updated cell gives \(\sum_i e^{A m_i^+}>e^{A+2}>7e^A>(N/2)(1+e^A)\), since \(A\ge128\). For \(N\ge12\), the radius-three locality bound of [1] says that at most twelve cells change, six initially zero and six initially \(A\). Outside this support the means remain unchanged. As \(e^{A+2}>7e^A>6(1+e^A)\), the change in total exponential entropy is again strictly positive. Jensen's inequality rules out any terminal average-preserving correction.

**Sharp negative side.** When \(N=2\), the first output mean equals
\[
m_0^+=\frac{3s(1-s)(3s^4+2s^2+4)}8,\qquad m_1^+=1-m_0^+.
\]
Both lie in \([0,1]\) throughout \(0\le s\le1/4\). When \(N=4\), the four normalized means are
\[
\begin{aligned}
m_0^+&=\frac{s(675s^6-2046s^5+1821s^4-1416s^3+1096s^2-456s+192)}{192},\\
m_1^+&=-\frac{s(675s^6+1596s^5-15s^4-744s^3-416s^2+312s-96)}{192},\\
m_2^+&=\frac{675s^7+1236s^6-513s^5-816s^4+680s^3+24s^2-192s+192}{192},\\
m_3^+&=-\frac{675s^7-2406s^6+1323s^5-1488s^4+2192s^3-744s^2+96s-192}{192}.
\end{aligned}
\]
For each of these eight polynomials \(m_i^+\) and \(1-m_i^+\), the minimum degree-seven Bernstein coefficient on \(t=4s\in[0,1]\) is nonnegative. The minima for \(m_i^+\) are \(0,0,2503139/3145728,3036229/3145728\), and for \(1-m_i^+\) are \(2614661/3145728,2924707/3145728,0,0\), respectively. Thus all four means lie in \([0,1]\). For every convex \(U\), the chord bound \(U(Am_i^+)\le(1-m_i^+)U(0)+m_i^+U(A)\), summed using mass conservation, gives
\[
\sum_i U(A m_i^+)\le\frac N2[U(0)+U(A)]=\sum_i U(u_i^0).
\]
This proves sharpness **for this family of initial data and global cell-mean criterion**.

## Verification

The included standalone `verify.py` implements exact arithmetic using only `fractions.Fraction` and the Python standard library. It independently reconstructs the full modal recurrence on periodic grids \(N=2,4,6,8,10,12\); compares all three closed overshoot polynomials coefficient-by-coefficient; certifies the Bernstein trace interval at every stage; proves the Bernstein cell-mean bounds at \(N=2,4\); and checks conservation and exact endpoint witnesses. All tests pass. The extension to arbitrary even \(N\) uses finite-stage stencil locality, not an inference from sampled grids.

## Relationship to prior work

Liu, Jiang and Zhang [1, section 2.3] derive the same large-grid overshoot formula for even \(N\ge12\) and the criterion excluding terminal average-preserving entropy correction. The additional result here supplies the previously unclassified meshes \(N=2,4,6,8,10\), proves the universal-convex nonincrease statement for the two smaller meshes, and identifies the exact minimum six-cell instance. Wei and Shu [2] give an independent SSPRK3 Burgers non-strong-\(L^2\)-stability construction for quadratic DG elements and smooth initial data; it does not classify the cell-average exponential-entropy obstruction in the present piecewise-linear two-plateau construction.

## Limitations

The cutoff concerns even uniform periodic meshes with exactly the displayed two-plateau states, the specified fixed LF viscosity, piecewise linear DG, unlimited SSPRK3 stages, and \(0<s\le1/4\). The nonincrease for \(N=2,4\) is a **necessary global entropy condition**, not a proof of per-cell weak-flux feasibility, strong entropy stability, or absence of other counterexamples. The entropy-growth statement concerns cell averages and terminal average-preserving corrections, not the entropy of intermediate DG polynomials. Independent audit has not been performed.

## References

1. Y. Liu, Y. Jiang and M. Zhang, *High-Order Fully Discrete Entropy-Stable DG Methods with Compact Explicit Single-Step Time Discretizations*, arXiv:2610.30535v1 (first publicly available 21 October 2026), https://arxiv.org/html/2610.30535v1, especially section 2.3.
2. Y. Wei and C.-W. Shu, *Counterexample to the one-step strong \(L^2\)-stability of a class of third order Runge–Kutta discontinuous Galerkin methods for Burgers equation*, preprint dated 2 September 2025, https://bpb-us-w2.wpmucdn.com/sites.brown.edu/dist/0/348/files/2025/09/Counterexample-to-the-one-step-strong.pdf.
