# Universal asymptotic attractor for tie-free largest-dihedral-angle bisection

## Statement

Korotov and Michaud (arXiv:2609.18788) exhibit the invariant family
\[
T(a,b)=\operatorname{conv}\{O,P,A,B\},\qquad
A=(a,0,0),\quad B=(bc,bs,0),
\]
with
\[
c=\frac78,\qquad s=\frac{\sqrt{15}}8,
\qquad 0<b\le \frac14,\qquad \frac34\le t:=\frac ab\le\frac45.
\]
They prove that the edge \(PA\) is the unique largest-dihedral-angle edge throughout the branch and that retaining the indicated child gives the exact recurrence
\[
a_{n+1}=\frac{a_nb_n}{a_n+W_n},\qquad b_{n+1}=a_n,
\]
where
\[
W_n=\sqrt{a_n^2+b_n^2-2ca_nb_n+s^2a_n^2b_n^2}.
\]
Their fixed-seed theorem obtains geometric upper/lower bounds with bases \(4/5\) and \(5/4\). The recurrence has a sharper universal asymptotic structure on the entire invariant rectangle.

Let \(t_n=a_n/b_n\). Define \(\rho\) to be the unique root in \([3/4,4/5]\) of
\[
7\rho^3-12\rho^2+4=0.
\]
Numerically,
\[
\rho=0.7835533375134631256\ldots,
\qquad \rho^{-1}=1.2762373052655370214\ldots,
\qquad \rho^2=0.6139558327284870603\ldots.
\]

**Theorem.** For every initial pair in the invariant region above, the tie-free retained LAB branch satisfies:

1. **Universal projective attractor.**
   \[
   t_n\longrightarrow \rho.
   \]
   More precisely, there is a positive constant \(C=C(a_0,b_0)\) such that
   \[
   \frac{b_n}{\rho^n}\longrightarrow C,
   \qquad
   \frac{a_n}{\rho^{n+1}}\longrightarrow C.
   \]

2. **Universal second-order approach to the attractor.** If \(u_n=b_n^2\), then
   \[
   \frac{t_n-\rho}{b_n^2}\longrightarrow A,
   \]
   where
   \[
   A=-\frac{s^2\rho^5}{(1-\rho^2)(2\rho^2+1)}
   =-0.08048577802046797136\ldots.
   \]

3. **Sharp degeneration rate.** The collapsing face angle from the source satisfies
   \[
   \angle OPA_n=\arctan(a_n)\sim C\rho^{n+1}.
   \]
   The inradius has the exact expression
   \[
   r_n=\frac{a_nb_ns}{a_nb_ns+a_n+b_n+W_n},
   \]
   and hence
   \[
   r_n\sim \frac{\rho^2s}{1+\rho}\,C\rho^n.
   \]
   Since the diameter is \(h_n=\sqrt{1+b_n^2}\to1\),
   \[
   \frac{h_n}{r_n}
   \sim
   \frac{1+\rho}{\rho^2sC}\,\rho^{-n}.
   \]
   Thus the exact exponential growth base of this shape metric is \(\rho^{-1}=1.2762373052\ldots\), sharpening the source's lower-bound base \(5/4\).

4. **Asymptotic split law.** If \(E_n\in OB_n\) is the angle-bisector intersection retained in the active child, then
   \[
   \frac{|OE_n|}{|OB_n|}=t_nt_{n+1}\longrightarrow\rho^2.
   \]
   This is also exactly the active-child volume fraction:
   \[
   \frac{\operatorname{vol}(T_{n+1})}{\operatorname{vol}(T_n)}
   =t_nt_{n+1}\longrightarrow\rho^2.
   \]
   Consequently
   \[
   \operatorname{vol}(T_n)
   \sim \frac{s\rho C^2}{6}\,\rho^{2n}.
   \]

5. **Limiting nondegenerate dihedral profile.** Let \(\beta=\arccos(1/(2\rho))\). Then
   \[
   \theta_{PB_n}\to\beta=50.3483252094\ldots^\circ,
   \qquad
   \theta_{PA_n}\to2\beta=100.6966504188\ldots^\circ,
   \]
   while \(\theta_{OP}=\arccos(7/8)=28.9550243719\ldots^\circ\), and the other three dihedrals tend to \(90^\circ\). Hence the branch approaches a universal transverse fixed profile even while its face geometry and inradius degenerate.

## Proof

Write
\[
Q(t,b)=\sqrt{1+t^2-2ct+s^2t^2b^2},
\qquad
F(t,b)=\frac{1}{t+Q(t,b)}.
\]
The source recurrence is equivalent to
\[
t_{n+1}=F(t_n,b_n),\qquad b_{n+1}=t_nb_n.
\]
Its invariant-range lemma gives \(t_n\in[3/4,4/5]\) and therefore \(b_n\le b_0(4/5)^n\to0\).

Set
\[
F_0(t)=F(t,0)=\frac{1}{t+\sqrt{1+t^2-2ct}}.
\]
A fixed point \(t=F_0(t)\) in the invariant interval obeys
\[
3t^2-2ct^3=1,
\]
which for \(c=7/8\) is precisely \(7t^3-12t^2+4=0\). That cubic is strictly decreasing on \([3/4,4/5]\), changes sign across the interval, and hence has the unique root \(\rho\) stated above.

For \(t<c\), direct differentiation gives
\[
|F_0'(t)|
=F_0(t)^2\left(1+\frac{t-c}{\sqrt{1+t^2-2ct}}\right)
<F_0(t)^2\le \left(\frac45\right)^2<1.
\]
Moreover, on the compact invariant rectangle, \(F(t,b)-F_0(t)=O(b^2)\) uniformly. Hence
\[
|t_{n+1}-\rho|\le q|t_n-\rho|+K b_n^2
\]
for some \(q<1\), which implies \(t_n\to\rho\). The same estimate and geometric decay of \(b_n\) imply \(\sum_n|t_n-\rho|<\infty\). Therefore
\[
\frac{b_n}{\rho^n}
=b_0\prod_{j=0}^{n-1}\frac{t_j}{\rho}
\]
converges to a finite positive constant \(C\); multiplying by \(t_n\) gives the corresponding limit for \(a_n\).

For the sharper projective asymptotic, regard \(F\) as a smooth function of \((t,u)\), with \(u=b^2\). At \((\rho,0)\), the fixed-point relation gives
\[
\partial_tF(\rho,0)=-\frac12,
\qquad
\partial_uF(\rho,0)
=-\frac{s^2\rho^5}{2(1-\rho^2)}=:k.
\]
Thus, with \(x_n=t_n-\rho\),
\[
x_{n+1}
=-\frac12x_n+k b_n^2
+O\!\left(x_n^2+|x_n|b_n^2+b_n^4\right).
\]
Since \(b_{n+1}^2/b_n^2=t_n^2\to\rho^2>1/2\), the normalized recurrence is asymptotically contractive and yields
\[
\frac{x_n}{b_n^2}\to A,
\qquad
A\rho^2=-\frac12A+k,
\]
which is the displayed formula for \(A\).

The angle asymptotic follows from \(\arctan a_n\sim a_n\). For the inradius, the volume and four face areas are
\[
V_n=\frac{a_nb_ns}{6},
\qquad
\frac{a_nb_ns}{2},\ \frac{a_n}{2},\ \frac{b_n}{2},\ \frac{W_n}{2},
\]
so \(r_n=3V_n/S_n\) gives the exact formula above. Since
\[
\frac{W_n}{b_n}=Q(t_n,b_n)\to Q_*=\frac1\rho-\rho,
\]
and \(\rho+Q_*=1/\rho\), division by \(b_n\) gives
\[
\frac{r_n}{b_n}\to\frac{\rho^2s}{1+\rho}.
\]
This proves the sharp angle, inradius, and shape-ratio asymptotics.

The source angle-bisector formula gives \(|OE_n|/|OB_n|=a_n/(a_n+W_n)\). Using the recurrence,
\[
\frac{|OE_n|}{|OB_n|}=t_nt_{n+1}.
\]
Because the child is cut by a plane through the opposite edge, the same ratio is its volume fraction; alternatively it follows directly from \(V_n=a_nb_ns/6\). Taking limits yields \(\rho^2\), and the volume asymptotic follows from \(t_n\to\rho\) and \(b_n\sim C\rho^n\).

Finally, the source formulas for the selected dihedrals give
\[
\cos\theta_{PA_n}=\frac{t_n-c}{Q(t_n,b_n)},
\qquad
\cos\theta_{PB_n}=\frac{1-ct_n}{Q(t_n,b_n)}.
\]
Using the cubic relation to eliminate \(c\) at the fixed point gives
\[
\cos\theta_{PB,\infty}=\frac1{2\rho},
\qquad
\cos\theta_{PA,\infty}=2\left(\frac1{2\rho}\right)^2-1.
\]
The relevant angle ranges imply \(\theta_{PA,\infty}=2\theta_{PB,\infty}=2\beta\). The remaining limits follow directly from the source dihedral formulas and \(b_n\to0\).

## Computational check

`artifacts/verify_asymptotics.py` uses only the Python standard library and high-precision decimal arithmetic. It recomputes \(\rho\), \(A\), and the recurrence for the source seed and three additional initial points in the invariant family. The output verifies convergence of \((t_n-\rho)/b_n^2\) to \(A\), the child-volume ratio to \(\rho^2\), and the normalized angle and shape-ratio constants. See `artifacts/verification.txt`.

## Relation to prior work and originality scope

Korotov--Michaud prove the invariant two-parameter family, unique LAB selection, exact recurrence, a fixed-seed degenerating branch, coarse geometric rates, uniform angle bounds, and a conforming realization. Those results are prior and are not claimed here. Adiprasito--Kalmanovich--Solomon study longest-edge bisection as a projective dynamical system and establish hyperbolic degeneration phenomena for that different refinement rule; Korotov gives an earlier explicit longest-edge degenerating recurrence.

The present claim is restricted to the largest-dihedral-angle recurrence of arXiv:2609.18788: the universal projective attractor on its full invariant rectangle, the exact asymptotic degeneration base, the second-order attraction coefficient, the asymptotic cut/volume fraction, and the limiting dihedral fixed profile. Searches by the source paper, recurrence, fixed-point polynomial, numerical constants, and synonymous LAB/asymptotic terminology found no accessible prior statement of these conclusions. Originality is therefore asserted only to the best of our knowledge; the motivating preprint is very recent, so contemporaneous or not-yet-indexed follow-up remains a material residual risk.

## Limitations

This result analyzes only the retained branch inside the specific invariant family with \(c=7/8\). It does not classify all LAB orbits, all children, global conformity closure strategies, or alternative largest-angle rules. The constant \(C\) depends on the initial tetrahedron and is characterized by a convergent product rather than a closed form. The result sharpens the asymptotic geometry of the counterexample family; it does not imply that typical practical LAB refinement follows this attractor.

## References

1. S. Korotov and J. Michaud, *Largest-dihedral-angle bisection algorithm does not preserve mesh regularity for tetrahedral partitions*, arXiv:2609.18788 (2026). https://arxiv.org/abs/2609.18788
2. K. A. Adiprasito, D. Kalmanovich, and Y. Solomon, *Degenerating orbits of the Longest Edge Bisection process*, arXiv:2609.08846 (2026). https://arxiv.org/abs/2609.08846
3. S. Korotov, *The longest-edge bisection algorithm may produce degenerating tetrahedra*, arXiv:2608.23139 (2026). https://arxiv.org/abs/2608.23139
