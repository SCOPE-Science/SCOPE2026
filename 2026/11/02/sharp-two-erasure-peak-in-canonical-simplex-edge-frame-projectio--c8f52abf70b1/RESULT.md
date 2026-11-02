# Sharp two-erasure peak in canonical simplex edge-frame projections

## Finding
Let \(n\ge9\) be an integer. The edge midpoints of the regular \((n-1)\)-simplex give a Parseval frame of \(\mathbf1^\perp\subset\mathbb R^n\) indexed by the edges of \(K_n\). Erase any matching of \(t\) edges and canonically renormalize the remaining frame to Parseval form. Write \(Q_t\) for the Gram matrix of the renormalized frame, considered as an orthogonal projection on the remaining edge-coordinate space, and let
\[
\Lambda_{n,t}=\|Q_t\|_{\ell_\infty\to\ell_\infty}
=\max_e\sum_f|(Q_t)_{ef}|.
\]
Put
\[
L_n=\frac{4(n-3)}n,\quad B_n(t)=n(n-4)+4t,\quad
C_n=n^3-16n^2+80n-112,\quad D_n=n^3-14n^2+68n-96.
\]
For \(0\le t\le\lfloor n/2\rfloor\), the exact values are
\[
\boxed{\begin{aligned}
\Lambda_{n,0}&=L_n,\\
\Lambda_{n,1}&=L_n+\frac{(n-4)(n^2-12n+24)}{n(n-2)^3},\\
\Lambda_{n,t}&=L_n+\frac{2[nC_n-2tD_n]}{n(n-4)(n-2)B_n(t)}
\quad(2\le t\le\lfloor n/2\rfloor).
\end{aligned}}
\]
For \(n=9\), this sequence decreases strictly at every step, so no erasure maximizes the norm. For every \(n\ge10\), the values increase strictly from \(t=0\) to \(t=2\), then decrease strictly for every remaining matching size. Thus **exactly two disjoint erasures uniquely maximize the canonical projection norm**, up to the choice of matching. In particular, a third erasure reduces the norm, despite deleting another frame vector.

This is a statement about the \(\ell_\infty\)-norm of the **canonical orthogonal projection** after frame renormalization. It does not assert that the canonical projection minimizes the norm among all projections onto its range.

## Assumptions and scope
Work over real scalars with standard basis \((\mathbf e_i)_{i=1}^n\). Let \(V=\mathbf1^\perp\), and for every unordered edge \(e=\{i,j\}\) set
\[
v_e=\frac{\mathbf e_i+\mathbf e_j-\tfrac2n\mathbf1}{\sqrt{n-2}}\in V.
\]
A matching \(M\) means a set of pairwise vertex-disjoint edges; its cardinality is \(t\). Put \(E=\binom{[n]}2\setminus M\), and define the reduced frame operator \(S_M=\sum_{e\in E}v_ev_e^\top|_V\). For the stated range of parameters, \(S_M\) is positive definite. Set \(w_e=S_M^{-1/2}v_e\), and define \((Q_t)_{ef}=\langle w_e,w_f\rangle\) for \(e,f\in E\). All matchings of the same size are equivalent by coordinate permutations, so \(\Lambda_{n,t}\) is unambiguous.

## Proof
**1. Parseval and reduced Gram formulas.** The full vectors satisfy \(\sum_e v_ev_e^\top=I_V\), \(\sum_ev_e=0\), and
\[
P_{ef}=\langle v_e,v_f\rangle=\frac{|e\cap f|-4/n}{n-2}.
\]
The Gram matrix on the erased matching is
\[
H=P_{MM}=\frac2{n-2}I_t-\frac4{n(n-2)}J_t,
\quad
(I_t-H)^{-1}=\frac{n-2}{n-4}\left(I_t-\frac4{B_n(t)}J_t\right).
\]
Since the two eigenvalues of \(I_t-H\) are positive for \(n\ge9\), the reduced vectors span \(V\). The Woodbury identity gives the Gram matrix of their canonical Parseval normalization:
\[
Q_t=P_{EE}+P_{EM}(I_t-H)^{-1}P_{ME}.
\]
For \(e\in E\), let \(r_e\in\{0,1\}^t\) indicate which erased edges meet \(e\); put \(s_e=\|r_e\|_1\in\{0,1,2\}\), \(c_{ef}=|e\cap f|\), and \(h_{ef}=r_e^\top r_f\). Substituting the last identities yields the **entrywise rational formula**
\[
\boxed{(Q_t)_{ef}=
\frac{[(n-4)c_{ef}+h_{ef}]B_n(t)-4(n-4+s_e)(n-4+s_f)}{(n-2)(n-4)B_n(t)}.}
\tag{1}
\]
The case \(t=0\) is the original full Gram matrix.

**2. Exact sign structure.** For \(n\ge9\), equation (1) is strictly positive when \(e\cap f\ne\varnothing\) and strictly negative when \(e\cap f=\varnothing\). To verify this, when \(c_{ef}=0\), one has \(h_{ef}\le2\) and \(s_e,s_f\ge h_{ef}\), giving the strict upper bounds \(B_n(t)-4(n-3)^2<0\) for \(h_{ef}=1\), and \(2B_n(t)-4(n-2)^2<0\) for \(h_{ef}=2\); for \(h_{ef}=0\) negativity is immediate. Here \(B_n(t)\le n(n-2)\). When \(c_{ef}=1\), if the shared vertex is unmatched then \(h_{ef}=0\) and \(s_e,s_f\le1\), so the numerator is at least \((n-4)n(n-4)-4(n-3)^2>0\); otherwise \(h_{ef}\ge1\) and the numerator is at least \((n-3)n(n-4)-4(n-2)^2>0\). The diagonal is positive by positive definiteness. All four polynomial bounds are valid at \(n=9\) and increase strictly thereafter.

**3. A row sum depends only on the erasure incidence.** For the full frame, the sum of \(v_f\) over all edges meeting a fixed edge \(e\) equals \((n-3)v_e\). With \(u_e=P_{Me}\), the sign rule, the full-frame balance identity, and the Woodbury formula give
\[
R_{s_e}:=\sum_{f\in E}|(Q_t)_{ef}|
=2(n-3)(Q_t)_{ee}+u_e^\top(I_t-H)^{-1}(\mathbf1_t-2r_e).
\tag{2}
\]
The right side depends only on \(s_e\) because \(u_e=(r_e-\tfrac4n\mathbf1_t)/(n-2)\), and \((I_t-H)^{-1}\) has the form \(aI+bJ\). Exact expansion gives
\[
R_1-R_0=\frac{n^3-16n^2+80n-8t-120}{(n-4)(n-2)B_n(t)},\qquad
R_2-R_1=\frac{n^3-16n^2+80n-8t-104}{(n-4)(n-2)B_n(t)}.
\]
Both are strictly positive for \(n\ge9\) and \(0\le t\le\lfloor n/2\rfloor\) whenever the relevant classes exist; at \(n=9\), the smallest first numerator (\(t=4\)) is \(1\), and thereafter the bound increases. When \(t=1\), the largest available class is \(s=1\); when \(t\ge2\), two different erased pairs provide a retained cross edge with \(s=2\). Hence the canonical projection norm is \(R_1\) for \(t=1\) and \(R_2\) for \(t\ge2\). Substitution into (2) and simplification prove the three exact formulas.

**4. Sharp monotonicity and phase transition.** Direct subtraction yields
\[
\Lambda_{n,1}-\Lambda_{n,0}=\frac{(n-4)(n^2-12n+24)}{n(n-2)^3},
\quad
\Lambda_{n,2}-\Lambda_{n,1}=\frac{(n-4)^2(n^2-12n+24)}{(n-2)^3(n^2-4n+8)}.
\]
The shared quadratic factor is negative at \(n=9\) and positive for integers \(n\ge10\). For the rational branch \(t\ge2\), differentiation in a real interpolation parameter gives
\[
\frac{d}{dt}\Lambda_{n,t}
=-\frac{4(n-2)(n^2-12n+40)}{(n-4)[n(n-4)+4t]^2}<0.
\]
This proves the strict peak classification, including the boundary cases \(n=9\) and \(t=\lfloor n/2\rfloor\). \(\square\)

## Verification
A standalone standard-library checker `erasure_checker.py` forms the full Gram entries as exact rational numbers, independently inverts the deleted Gram complement, and compares every surviving entry to formula (1) for all \(9\le n\le16\) and all permitted matching sizes. It independently evaluates each absolute row sum, verifies the sign rule and the claimed exact norms, and checks the monotonicity profile. Running `python erasure_checker.py` produced `PASS: 633398 exact rational assertions for n=9..16, all matching sizes`. The assertion count is finite evidence only; the algebraic proof above supplies the universal quantifiers.

For example, at \(n=10\) the norms for erasing \(0,1,2,3\) edges are respectively \(2.8\), \(2.8046875\), \(2.8088235294117647\), and \(2.787037037037037\). These numerical displays are illustrative, not inputs to the proof.

## Relationship to prior work
Deregowska and Lewandowska (arXiv:2608.08695, Example 2.1) study the **unerased** edge-midpoint Parseval frame as a configuration relevant to maximal relative projection constants and obtain its symmetric row-sum value \(4(n-3)/n\). The present result fixes that frame but asks for the **canonical projection's** \(\ell_\infty\) norm after deleting an arbitrary matching and re-tightening the frame. The rows now split into three incidence orbits and yield the new two-erasure maximum. The result does not infer a minimal projection constant from its canonical operator norm.

Heineken, Morillas, and Tarazaga describe balanced frames, canonical Parseval normalization, and analysis projections in general. Haikin, Zamir, and Gavish study moment bounds under random erasures. Neither the general normalization machinery nor the moment problem by itself gives the matching-specific deterministic norm formulas here. A potentially equivalent result in earlier work on incidence projections, line graphs, or finite-frame erasures remains a publication-priority risk.

## Limitations
The result is for **real** regular-simplex edge-midpoint frames, matching erasures, and \(n\ge9\). It does not cover arbitrary erased-edge subgraphs, general tight frames, or a minimizing projection over all complements. The special bound \(n\ge9\) is used to keep every Gram-entry sign determined by edge intersection. Independent mathematical verification and publication-priority certification are not asserted.

## References
1. B. Deregowska and B. Lewandowska, *Maximal Projection Constants and Extremal Vector Configurations: Some Conjectures and Examples*, arXiv:2608.08695 (first posted 2026-08-09), especially Example 2.1. https://arxiv.org/abs/2608.08695
2. S. Heineken, M. Morillas, and P. Tarazaga, *Balanced frames: a useful tool in signal processing with good properties*, https://www.researchgate.net/publication/332138988_Balanced_frames_a_useful_tool_in_signal_processing_with_good_properties
3. M. Haikin, R. Zamir, and M. Gavish, *Frame Moments and Welch Bound with Erasures*, arXiv:1801.04548. https://arxiv.org/abs/1801.04548
